# agprof summary

- Duration: **10410.757 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **111 calls**, 111 succeeded, 0 failed, 0 interrupted, n/a reported retries, 9928.382 s total wait
- Tools: **160/160 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **1150688** at 1.972 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 10404495.172 / 10404495.172 ms |
| LLM latency p50 / p95 | 61546.290 / 260440.868 ms |
| LLM TTFT p50 / p95 | 38515.057 / 248061.595 ms |
| LLM input / output tokens | 14180919 / 171690 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 111 total, 111 succeeded, 0 failed, 0 interrupted |
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
| edit_file | 1/1 | 1 | 0 | 0 | n/a | n/a |
| manage_task | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 8/8 | 8 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 13/13 | 13 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 4/4 | 4 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 4/4 | 4 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 13/13 | 13 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__submitted_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 5/5 | 5 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 6/6 | 6 | 0 | 0 | n/a | n/a |
| read_file | 29/29 | 29 | 0 | 0 | n/a | n/a |
| run_command | 63/63 | 63 | 0 | 0 | n/a | n/a |
| write_file | 7/7 | 7 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 2.527% | 116.666% | 263.289 s | 9020.232 MB | 10082.281 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 2240 |  | 10349 | 0.000% | 0.000% | 0.000 s | 12.136 MB | 12.180 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| python | 2196 |  | 10349 | 1.214% | 115.677% | 126.650 s | 2968.262 MB | 3735.875 MB | 15756.158 MB | 16890.020 MB | 106.625000 MB | 1695.128906 MB |
| lsb_guard.sh | 2201 |  | 10349 | 0.001% | 0.995% | 0.090 s | 3.322 MB | 3.340 MB | 7.570 MB | 7.570 MB | 0.054688 MB | 0.000000 MB |
| sleep | 2318 |  | 40 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 2241 |  | 10349 | 1.170% | 45.756% | 121.770 s | 2309.559 MB | 2310.094 MB | 21203.113 MB | 21203.113 MB | 0.011719 MB | 0.070312 MB |
| lsb_grid_worker | 2187 |  | 10349 | 0.000% | 0.000% | 0.000 s | 3.369 MB | 3.387 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 2346 |  | 10349 | 0.035% | 4.967% | 3.610 s | 44.750 MB | 45.605 MB | 131.256 MB | 131.945 MB | 0.003906 MB | 0.347656 MB |
| vllm | 2206 |  | 10349 | 0.080% | 8.857% | 8.370 s | 1787.248 MB | 1788.008 MB | 11041.678 MB | 11056.633 MB | 0.011719 MB | 0.066406 MB |
| docker-init | 2460 | sandbox_agent_lsb-antigravity_0000_0000 | 10342 | 0.002% | 1.990% | 0.220 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2494 | sandbox_agent_lsb-antigravity_0000_0000 | 10342 | 0.003% | 0.995% | 0.260 s | 1.273 MB | 1.273 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 2595 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 56.089% | 60.581% | 1.130 s | 48.497 MB | 77.027 MB | 58.997 MB | 92.902 MB | n/a MB | n/a MB |
| bash | 2589 | sandbox_agent_lsb-antigravity_0000_0000 | 10342 | 44.110% | 92.027% | 4588.200 s | 105.138 MB | 133.656 MB | 966.876 MB | 985.586 MB | n/a MB | n/a MB |
| antigravity | 2603 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 119.062 MB | 119.062 MB | 1849.492 MB | 1849.492 MB | n/a MB | n/a MB |
| antigravity | 2612 | sandbox_agent_lsb-antigravity_0000_0000 | 10312 | 1.885% | 22.839% | 195.530 s | 266.688 MB | 319.633 MB | 2211.806 MB | 2273.488 MB | n/a MB | n/a MB |
| sleep | 2636 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 2638 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 2650 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 2744 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 2746 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3033 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3098 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3103 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3260 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3262 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3382 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3502 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 3510 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3511 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.301 MB | 18.301 MB | 24.172 MB | 24.172 MB | n/a MB | n/a MB |
| sleep | 3639 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3727 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3729 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3734 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3736 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3739 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 3904 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.773 MB | 14.773 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| sh | 3903 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 3920 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3922 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3934 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3947 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4032 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4119 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4121 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4123 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4126 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.586 MB | 8.586 MB | 13.195 MB | 13.195 MB | n/a MB | n/a MB |
| sleep | 4142 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4145 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4257 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4259 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4261 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4263 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4279 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4376 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4378 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4380 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4404 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.852 MB | 9.852 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sh | 4403 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 4430 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4433 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4530 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4532 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 4533 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.426 MB | 1.426 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4534 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.812 MB | 9.812 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| pgrep | 4545 |  | 1 | n/a% | n/a% | n/a s | 3.305 MB | 3.305 MB | 10.102 MB | 10.102 MB | n/a MB | n/a MB |
| sleep | 4546 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4548 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4550 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4649 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4652 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4656 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 31.676 MB | 31.676 MB | 35.508 MB | 35.508 MB | n/a MB | n/a MB |
| sleep | 4666 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 4696 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.945 MB | 20.945 MB | 25.699 MB | 25.699 MB | n/a MB | n/a MB |
| sh | 4695 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.281 MB | 1.281 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 4701 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4702 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.586 MB | 9.586 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sleep | 4712 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 4713 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4714 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.590 MB | 9.590 MB | 13.727 MB | 13.727 MB | n/a MB | n/a MB |
| sh | 4771 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4772 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.492 MB | 20.492 MB | 25.461 MB | 25.461 MB | n/a MB | n/a MB |
| sleep | 4778 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4897 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4901 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4903 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4959 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4989 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5098 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5135 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5142 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.055 MB | 9.055 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 5141 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.488 MB | 1.488 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 5148 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5149 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.953 MB | 16.953 MB | 23.020 MB | 23.020 MB | n/a MB | n/a MB |
| sleep | 5159 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5179 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5201 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5354 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5398 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5501 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 5506 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5507 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.086 MB | 15.086 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| sleep | 5517 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5532 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 5555 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5556 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.875 MB | 20.875 MB | 25.828 MB | 25.828 MB | n/a MB | n/a MB |
| sleep | 5560 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5576 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5584 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 134.488% | 153.916% | 2.710 s | 867.079 MB | 1305.430 MB | 1079.302 MB | 1527.496 MB | n/a MB | n/a MB |
| sleep | 5595 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5604 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 134.453% | 168.894% | 2.710 s | 752.309 MB | 1158.977 MB | 964.346 MB | 1380.973 MB | n/a MB | n/a MB |
| sleep | 5616 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5619 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5637 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.852 MB | 16.852 MB | 208.582 MB | 208.582 MB | n/a MB | n/a MB |
| sleep | 5654 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5732 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5734 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5742 | sandbox_agent_lsb-antigravity_0000_0000 | 8 | 171.312% | 177.302% | 12.070 s | 59.388 MB | 131.422 MB | 256.946 MB | 349.270 MB | n/a MB | n/a MB |
| sleep | 5755 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 5776 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5777 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.516 MB | 21.516 MB | 27.000 MB | 27.000 MB | n/a MB | n/a MB |
| sleep | 5775 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 5811 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.480 MB | 1.480 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5812 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.547 MB | 10.547 MB | 15.062 MB | 15.062 MB | n/a MB | n/a MB |
| sleep | 5819 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 5823 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5824 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.504 MB | 19.504 MB | 24.812 MB | 24.812 MB | n/a MB | n/a MB |
| sleep | 5838 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5922 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.578 MB | 7.578 MB | 11.988 MB | 11.988 MB | n/a MB | n/a MB |
| sleep | 5930 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5932 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5935 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5964 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| pgrep | 5965 |  | 1 | n/a% | n/a% | n/a s | 3.289 MB | 3.289 MB | 10.102 MB | 10.102 MB | n/a MB | n/a MB |
| sleep | 5966 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 5968 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 5976 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5977 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.203 MB | 14.203 MB | 19.957 MB | 19.957 MB | n/a MB | n/a MB |
| sh | 5997 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5998 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.387 MB | 16.387 MB | 21.848 MB | 21.848 MB | n/a MB | n/a MB |
| sleep | 6012 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 6026 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.586 MB | 1.586 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6027 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.250 MB | 7.250 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| sleep | 6052 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6088 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.422 MB | 19.422 MB | 24.812 MB | 24.812 MB | n/a MB | n/a MB |
| sh | 6087 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 6094 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6123 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.566 MB | 21.566 MB | 27.000 MB | 27.000 MB | n/a MB | n/a MB |
| sh | 6122 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 6129 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6133 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 125.113 MB | 125.113 MB | 130.758 MB | 130.758 MB | n/a MB | n/a MB |
| sleep | 6153 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 6159 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6160 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.812 MB | 9.812 MB | 13.727 MB | 13.727 MB | n/a MB | n/a MB |
| python3 | 6166 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.730 MB | 7.730 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 6165 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.480 MB | 1.480 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 6176 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 6177 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.605 MB | 1.605 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6178 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.766 MB | 20.766 MB | 25.828 MB | 25.828 MB | n/a MB | n/a MB |
| sh | 6193 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6194 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sleep | 6209 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| pgrep | 6225 |  | 1 | n/a% | n/a% | n/a s | 3.055 MB | 3.055 MB | 10.102 MB | 10.102 MB | n/a MB | n/a MB |
| sleep | 6226 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 6230 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6231 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.980 MB | 7.980 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sleep | 6245 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6250 | sandbox_agent_lsb-antigravity_0000_0000 | 46 | 175.291% | 180.241% | 79.550 s | 160.622 MB | 165.637 MB | 379.882 MB | 385.047 MB | n/a MB | n/a MB |
| sleep | 6260 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6268 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6272 | sandbox_agent_lsb-antigravity_0000_0000 | 101 | 176.188% | 181.831% | 177.510 s | 213.155 MB | 279.277 MB | 432.876 MB | 498.441 MB | n/a MB | n/a MB |
| sleep | 6279 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6303 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6322 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6334 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6336 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6339 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6356 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 6368 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6369 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.824 MB | 20.824 MB | 25.586 MB | 25.586 MB | n/a MB | n/a MB |
| sleep | 6381 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6383 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6385 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6389 | sandbox_agent_lsb-antigravity_0000_0000 | 48 | 174.027% | 183.979% | 82.460 s | 163.227 MB | 247.113 MB | 382.222 MB | 465.281 MB | n/a MB | n/a MB |
| sleep | 6402 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6426 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6428 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6430 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6432 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6442 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| pgrep | 6461 |  | 1 | n/a% | n/a% | n/a s | 3.289 MB | 3.289 MB | 10.102 MB | 10.102 MB | n/a MB | n/a MB |
| sleep | 6462 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6464 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6466 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6493 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6497 | sandbox_agent_lsb-antigravity_0000_0000 | 53 | 173.030% | 182.086% | 90.670 s | 468.896 MB | 2545.449 MB | 717.998 MB | 4354.801 MB | n/a MB | n/a MB |
| python3 | 6509 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.227 MB | 9.227 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 6508 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 6512 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6536 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6540 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 148.061% | 173.844% | 2.980 s | 761.206 MB | 1126.352 MB | 973.335 MB | 1348.160 MB | n/a MB | n/a MB |
| sleep | 6554 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6632 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6678 | sandbox_agent_lsb-antigravity_0000_0000 | 93 | 174.119% | 181.802% | 161.380 s | 410.320 MB | 4171.953 MB | 648.646 MB | 4495.828 MB | n/a MB | n/a MB |
| sleep | 6685 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6692 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6722 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6727 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 56.137 MB | 56.137 MB | 248.137 MB | 248.137 MB | n/a MB | n/a MB |
| sleep | 6739 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6743 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.938 MB | 7.938 MB | 12.926 MB | 12.926 MB | n/a MB | n/a MB |
| sleep | 6752 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6754 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6756 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6787 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6789 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6810 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.871 MB | 7.871 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 6809 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 6831 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6832 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.570 MB | 10.570 MB | 15.062 MB | 15.062 MB | n/a MB | n/a MB |
| sleep | 6838 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6840 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6843 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 6867 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6868 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.711 MB | 10.711 MB | 15.273 MB | 15.273 MB | n/a MB | n/a MB |
| antigravity | 6878 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 290.152 MB | 290.152 MB | 2272.605 MB | 2272.605 MB | n/a MB | n/a MB |
| sleep | 6887 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6892 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6900 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.727 MB | 18.727 MB | 24.559 MB | 24.559 MB | n/a MB | n/a MB |
| sh | 6899 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6915 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 154.790% | 166.103% | 4.670 s | 834.975 MB | 1096.246 MB | 1052.942 MB | 1318.742 MB | n/a MB | n/a MB |
| sh | 6920 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6921 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.031 MB | 5.031 MB | 11.383 MB | 11.383 MB | n/a MB | n/a MB |
| sleep | 6927 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6931 | sandbox_agent_lsb-antigravity_0000_0000 | 4 | 165.786% | 167.447% | 5.020 s | 178.431 MB | 244.391 MB | 397.988 MB | 463.961 MB | n/a MB | n/a MB |
| python3 | 6937 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.211 MB | 21.211 MB | 25.840 MB | 25.840 MB | n/a MB | n/a MB |
| sh | 6936 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.387 MB | 1.387 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 6943 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 6946 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 163.898% | 170.399% | 8.270 s | 197.158 MB | 276.141 MB | 417.373 MB | 495.754 MB | n/a MB | n/a MB |
| sleep | 6958 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6978 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6980 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6986 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6992 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 6998 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7017 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7021 | sandbox_agent_lsb-antigravity_0000_0000 | 30 | 173.265% | 178.843% | 50.640 s | 216.787 MB | 320.684 MB | 436.859 MB | 540.559 MB | n/a MB | n/a MB |
| sleep | 7036 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7039 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7041 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7054 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7073 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7077 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 134.165% | 134.165% | 1.350 s | 596.488 MB | 1130.398 MB | 811.453 MB | 1350.777 MB | n/a MB | n/a MB |
| sleep | 7090 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7092 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 7093 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.586 MB | 1.586 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7094 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.109 MB | 7.109 MB | 11.660 MB | 11.660 MB | n/a MB | n/a MB |
| sleep | 7106 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7122 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1545.391 MB | 1545.391 MB | 1739.719 MB | 1739.719 MB | n/a MB | n/a MB |
| sleep | 7134 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7354 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7359 | sandbox_agent_lsb-antigravity_0000_0000 | 39 | 173.658% | 180.426% | 66.520 s | 2321.333 MB | 4032.359 MB | 2552.481 MB | 4493.957 MB | n/a MB | n/a MB |
| sleep | 7375 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7381 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 7391 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7392 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.758 MB | 16.758 MB | 22.141 MB | 22.141 MB | n/a MB | n/a MB |
| sleep | 7414 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 7418 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.605 MB | 1.605 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7419 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.672 MB | 14.672 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| sleep | 7431 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7529 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7537 | sandbox_agent_lsb-antigravity_0000_0000 | 5 | 159.195% | 162.595% | 6.430 s | 162.227 MB | 201.805 MB | 384.411 MB | 432.387 MB | n/a MB | n/a MB |
| sh | 7543 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7544 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.367 MB | 20.367 MB | 25.199 MB | 25.199 MB | n/a MB | n/a MB |
| sleep | 7550 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7552 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 7553 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7554 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.723 MB | 21.723 MB | 27.039 MB | 27.039 MB | n/a MB | n/a MB |
| python3 | 7560 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 163.912% | 169.009% | 8.280 s | 174.200 MB | 290.945 MB | 389.207 MB | 509.953 MB | n/a MB | n/a MB |
| sleep | 7572 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7589 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 123.661% | 146.099% | 2.490 s | 790.382 MB | 1211.340 MB | 1043.007 MB | 1743.078 MB | n/a MB | n/a MB |
| sh | 7593 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7594 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.516 MB | 10.516 MB | 15.117 MB | 15.117 MB | n/a MB | n/a MB |
| sleep | 7601 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 7618 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.582 MB | 1.582 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7619 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.848 MB | 20.848 MB | 25.836 MB | 25.836 MB | n/a MB | n/a MB |
| python3 | 7721 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 160.051 MB | 160.051 MB | 769.887 MB | 769.887 MB | n/a MB | n/a MB |
| sleep | 7732 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7734 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7738 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 83.066 MB | 83.066 MB | 304.020 MB | 304.020 MB | n/a MB | n/a MB |
| sleep | 7750 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7752 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7761 | sandbox_agent_lsb-antigravity_0000_0000 | 9 | 173.065% | 178.035% | 13.930 s | 2038.725 MB | 2489.793 MB | 2488.615 MB | 4383.273 MB | n/a MB | n/a MB |
| python3 | 7767 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.691 MB | 7.691 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 7766 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.598 MB | 1.598 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 7773 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7870 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7872 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.359 MB | 20.359 MB | 25.188 MB | 25.188 MB | n/a MB | n/a MB |
| sh | 7871 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7879 | sandbox_agent_lsb-antigravity_0000_0000 | 28 | 171.843% | 180.368% | 46.800 s | 1960.554 MB | 3753.492 MB | 2222.521 MB | 4532.156 MB | n/a MB | n/a MB |
| sleep | 7884 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7916 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7918 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 7927 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 7953 | sandbox_agent_lsb-antigravity_0000_0000 | 28 | 170.838% | 181.322% | 46.490 s | 1912.663 MB | 2376.195 MB | 2148.152 MB | 2592.844 MB | n/a MB | n/a MB |
| sleep | 8042 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 8043 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8044 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.672 MB | 15.672 MB | 20.500 MB | 20.500 MB | n/a MB | n/a MB |
| sleep | 8052 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 8058 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 8059 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8060 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.609 MB | 9.609 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sleep | 8071 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 8083 |  | 48 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| docker | 8123 |  | 1 | n/a% | n/a% | n/a s | 30.219 MB | 30.219 MB | 1907.832 MB | 1907.832 MB | n/a MB | n/a MB |
| docker | 8140 |  | 23 | 0.000% | 0.000% | 0.000 s | 28.621 MB | 29.922 MB | 1824.412 MB | 1907.340 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0.182% | 93.000% | 11827.756 MB | 12140.000 MB | 27.825 W | 63.915 W | 289640.924 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-antigravity_0000_0000 | 55.111% | 218.497% | 5734.323 s | 406.778 MB | 4560.008 MB | 221.324219 MB | 356.863281 MB | 0.414234 MB | 2.683685 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2352 | 10410.692 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 10404.495 | n/a | n/a | 221.324 | 10404495.172 | 10404495.172 | 10404495.172 |
| engine:execute | 1/1 | 0 | 0 | 10404.493 | 8.529 | 10395.893 | 221.324 | 10404493.499 | 10404493.499 | 10404493.499 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 10374.546 | 0.017 | 10374.529 | 188.876 | 10374545.763 | 10374545.763 | 10374545.763 |
| llm:attempt | 111/111 | 0 | 0 | 9928.382 | 5.044 | 9923.323 | 22.916 | 89444.881 | 61546.290 | 260440.868 |
| tool:run_command | 63/63 | 0 | 0 | 558.421 | n/a | n/a | 148.213 | 8863.828 | 769.742 | 47941.320 |
| run:container_call | 13/13 | 0 | 0 | 24.369 | 0.002 | 24.366 | 0.563 | 1874.519 | 56.333 | 9479.794 |
| teardown:commit | 1/1 | 0 | 0 | 23.724 | 0.005 | 23.719 | 0.564 | 23723.831 | 23723.831 | 23723.831 |
| sandbox:commit | 1/1 | 0 | 0 | 23.507 | 0.003 | 23.504 | 0.564 | 23506.738 | 23506.738 | 23506.738 |
| checkpoint.total | 1/1 | 0 | 0 | 23.507 | 0.003 | 23.504 | 0.564 | 23506.562 | 23506.562 | 23506.562 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 23.506 | 0.003 | 23.504 | 0.564 | 23506.405 | 23506.405 | 23506.405 |
| tool:mcp__agency__token_stats | 5/5 | 0 | 0 | 10.693 | n/a | n/a | 0.012 | 2138.695 | 2282.240 | 2456.678 |
| tool:mcp__agency__generate | 13/13 | 0 | 0 | 9.993 | n/a | n/a | 0.007 | 768.697 | 692.537 | 1348.232 |
| tool:mcp__agency__trace | 6/6 | 0 | 0 | 9.888 | n/a | n/a | 0.000 | 1648.000 | 1437.710 | 2899.940 |
| tool:mcp__agency__inspect_module_inputs | 4/4 | 0 | 0 | 7.941 | n/a | n/a | 0.000 | 1985.373 | 1960.499 | 2110.077 |
| tool:mcp__agency__inspect | 4/4 | 0 | 0 | 7.578 | n/a | n/a | 0.081 | 1894.531 | 1896.202 | 1919.817 |
| tool:read_file | 29/29 | 0 | 0 | 6.376 | n/a | n/a | 0.047 | 219.851 | 231.803 | 269.960 |
| tool:mcp__agency__patch | 13/13 | 0 | 0 | 6.043 | n/a | n/a | 0.000 | 464.881 | 453.096 | 514.994 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.857 | 1.113 | 3.745 | 31.291 | 4857.362 | 4857.362 | 4857.362 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.857 | 1.112 | 3.745 | 31.290 | 4857.090 | 4857.090 | 4857.090 |
| syscall:connect | 1240/1240 | 0 | 0 | 4.837 | n/a | n/a | 0.843 | 3.901 | 2.457 | 6.378 |
| tool:mcp__agency__attribution | 8/8 | 0 | 0 | 2.633 | n/a | n/a | 0.000 | 329.093 | 322.904 | 363.891 |
| tool:write_file | 7/7 | 0 | 0 | 2.133 | n/a | n/a | 0.001 | 304.707 | 328.204 | 364.808 |
| syscall:sendto | 640/640 | 0 | 0 | 1.392 | n/a | n/a | 0.164 | 2.176 | 2.049 | 3.679 |
| syscall:execve | 786/786 | 0 | 0 | 0.992 | n/a | n/a | 0.330 | 1.262 | 1.213 | 1.553 |
| sandbox:create | 1/1 | 0 | 0 | 0.904 | 0.249 | 0.655 | 0.000 | 903.904 | 903.904 | 903.904 |
| tool:mcp__agency__attention | 2/2 | 0 | 0 | 0.695 | n/a | n/a | 0.000 | 347.538 | 347.538 | 388.571 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.586 | n/a | n/a | 0.000 | 585.549 | 585.549 | 585.549 |
| sandbox:start | 1/1 | 0 | 0 | 0.578 | 0.002 | 0.575 | 0.000 | 577.820 | 577.820 | 577.820 |
| runtime.container_create | 1/1 | 0 | 0 | 0.578 | 0.002 | 0.575 | 0.000 | 577.680 | 577.680 | 577.680 |
| run:detect | 1/1 | 0 | 0 | 0.552 | 0.001 | 0.551 | 0.000 | 552.184 | 552.184 | 552.184 |
| tool:manage_task | 2/2 | 0 | 0 | 0.461 | n/a | n/a | 0.000 | 230.564 | 230.564 | 240.194 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.422 | n/a | n/a | 0.015 | 422.099 | 422.099 | 422.099 |
| tool:mcp__agency__submitted_output | 1/1 | 0 | 0 | 0.380 | n/a | n/a | 0.000 | 380.049 | 380.049 | 380.049 |
| tool:edit_file | 1/1 | 0 | 0 | 0.334 | n/a | n/a | 0.001 | 334.219 | 334.219 | 334.219 |
| sandbox:stop | 1/1 | 0 | 0 | 0.217 | 0.002 | 0.215 | 0.000 | 216.789 | 216.789 | 216.789 |
| agency:services_close | 1/1 | 0 | 0 | 0.186 | 0.001 | 0.185 | 0.325 | 186.154 | 186.154 | 186.154 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.088 | 0.088 | 0.000 | 0.153 | 87.625 | 87.625 | 87.625 |
| agency:services_start | 1/1 | 0 | 0 | 0.087 | 0.042 | 0.045 | 0.000 | 87.331 | 87.331 | 87.331 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.008 | 0.041 | 0.000 | 48.842 | 48.842 | 48.842 |
| syscall:bind | 4/4 | 0 | 0 | 0.008 | n/a | n/a | 0.119 | 1.879 | 1.947 | 2.376 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.212 | 1.212 | 1.212 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.076 | 0.080 | 0.102 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.165 | 0.165 | 0.165 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.075 | 0.075 | 0.075 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 10347 | 0.152 | 0.032 | 52.207 | 0.036 | 15.769663 CPU seconds | n/a |
| GPU 0 memory | MB | 10349 | 11827.756 | 11670.000 | 12140.000 | 11864.000 | n/a | n/a |
| GPU 0 power | W | 10349 | 27.825 | 27.494 | 63.915 | 27.859 | n/a | 289640.924 J |
| GPU 0 proc / 2196-10119 / sandbox / ~ / device / GPU-5f3ca4bb-93a4-a05c-6f61-09226878be52 memory | MB | 10349 | 3206.276 | 3118.000 | 3498.000 | 3222.000 | n/a | n/a |
| GPU 0 proc / 2196-10119 / sandbox / ~ / device / GPU-5f3ca4bb-93a4-a05c-6f61-09226878be52 estimated power | W | 9050 | 0.213 | 0.000 | 53.710 | 0.000 | n/a | n/a |
| GPU 0 proc / 2196-10119 / sandbox / ~ / device / GPU-5f3ca4bb-93a4-a05c-6f61-09226878be52 utilization | percent | 9050 | 0.140 | 0.000 | 46.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2241-13630 / sandbox / ~ / device / GPU-5f3ca4bb-93a4-a05c-6f61-09226878be52 memory | MB | 10349 | 8139.480 | 8070.000 | 8160.000 | 8160.000 | n/a | n/a |
| GPU 0 proc / 2241-13630 / sandbox / ~ / device / GPU-5f3ca4bb-93a4-a05c-6f61-09226878be52 estimated power | W | 1125 | 0.482 | 0.000 | 63.915 | 0.000 | n/a | n/a |
| GPU 0 proc / 2241-13630 / sandbox / ~ / device / GPU-5f3ca4bb-93a4-a05c-6f61-09226878be52 utilization | percent | 1125 | 0.420 | 0.000 | 81.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 10349 | 11345.756 | 11188.000 | 11658.000 | 11382.000 | n/a | n/a |
| GPU 0 utilization | percent | 10349 | 0.182 | 0.000 | 93.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 10349 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 10348 | 3.701 | 0.102 | 74.366 | 0.233 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 10348 | 14.271 | 0.251 | 59.406 | 0.251 | n/a | n/a |
| host disk_read_mb_s | MB/s | 10348 | 0.205 | 0.000 | 196.572 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 10348 | 0.221 | 0.000 | 198.168 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 10348 | 0.104 | 0.000 | 40.565 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 10348 | 0.107 | 0.000 | 40.719 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 10349 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 10349 | 7189.725 | 6344.496 | 11844.836 | 7442.453 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 10348 | 0.003 | 0.000 | 7.457 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 10348 | 0.003 | 0.000 | 7.490 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 10348 | 0.001 | 0.000 | 2.008 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 10348 | 0.005 | 0.000 | 0.862 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2187) CPU | percent | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2187) io read MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2187) io write MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2187) rss_mb | MB | 10349 | 3.369 | 3.262 | 3.387 | 3.262 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2187) main thread run-queue wait | percent | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2187) vms_mb | MB | 10349 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2196) CPU | percent | 10348 | 1.214 | 0.000 | 115.677 | 0.000 | 126.650000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2196) io read MB/s | MB/s | 10348 | 0.010 | 0.000 | 50.099 | 0.000 | 106.625000 MB | n/a |
| Agency harness — python -m lsbench (PID 2196) io write MB/s | MB/s | 10348 | 0.162 | 0.015 | 375.180 | 0.039 | 1695.128906 MB | n/a |
| Agency harness — python -m lsbench (PID 2196) rss_mb | MB | 10349 | 2968.262 | 2147.113 | 3735.875 | 3461.453 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2196) main thread run-queue wait | percent | 10348 | 0.000 | 0.000 | 0.211 | 0.000 | 0.009625 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2196) vms_mb | MB | 10349 | 15756.158 | 13591.828 | 16890.020 | 16473.770 | n/a | n/a |
| bash lsb_guard.sh (PID 2201) CPU | percent | 10348 | 0.001 | 0.000 | 0.995 | 0.000 | 0.090000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 2201) io read MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.047 | 0.000 | 0.054688 MB | n/a |
| bash lsb_guard.sh (PID 2201) io write MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 2201) rss_mb | MB | 10349 | 3.322 | 3.215 | 3.340 | 3.215 | n/a | n/a |
| bash lsb_guard.sh (PID 2201) main thread run-queue wait | percent | 10348 | 0.000 | 0.000 | 0.099 | 0.000 | 0.001875 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 2201) vms_mb | MB | 10349 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Python — vllm (PID 2206) CPU | percent | 10348 | 0.080 | 0.000 | 8.857 | 0.000 | 8.370000 CPU seconds | n/a |
| Python — vllm (PID 2206) io read MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| Python — vllm (PID 2206) io write MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.008 | 0.000 | 0.066406 MB | n/a |
| Python — vllm (PID 2206) rss_mb | MB | 10349 | 1787.248 | 1786.203 | 1788.008 | 1786.203 | n/a | n/a |
| Python — vllm (PID 2206) main thread run-queue wait | percent | 10348 | 0.003 | 0.000 | 3.623 | 0.000 | 0.288846 run-queue seconds | n/a |
| Python — vllm (PID 2206) vms_mb | MB | 10349 | 11041.678 | 10984.613 | 11056.633 | 11056.633 | n/a | n/a |
| Python — python -c (PID 2240) CPU | percent | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2240) io read MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2240) io write MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2240) rss_mb | MB | 10349 | 12.136 | 12.055 | 12.180 | 12.055 | n/a | n/a |
| Python — python -c (PID 2240) main thread run-queue wait | percent | 10348 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2240) vms_mb | MB | 10349 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2241) CPU | percent | 10348 | 1.170 | 0.000 | 45.756 | 1.991 | 121.770000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2241) io read MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.008 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 2241) io write MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.008 | 0.000 | 0.070312 MB | n/a |
| VLLM::EngineCore (PID 2241) rss_mb | MB | 10349 | 2309.559 | 2308.402 | 2310.094 | 2308.402 | n/a | n/a |
| VLLM::EngineCore (PID 2241) main thread run-queue wait | percent | 10348 | 0.000 | 0.000 | 0.162 | 0.000 | 0.008093 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2241) vms_mb | MB | 10349 | 21203.113 | 21203.113 | 21203.113 | 21203.113 | n/a | n/a |
| sleep (PID 2318) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2318) io read MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2318) io write MB/s | MB/s | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2318) rss_mb | MB | 40 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2318) main thread run-queue wait | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2318) vms_mb | MB | 40 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2346) CPU | percent | 10348 | 0.035 | 0.000 | 4.967 | 0.000 | 3.610000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2346) io read MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2346) io write MB/s | MB/s | 10348 | 0.000 | 0.000 | 0.008 | 0.000 | 0.347656 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2346) rss_mb | MB | 10349 | 44.750 | 43.613 | 45.605 | 44.105 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2346) main thread run-queue wait | percent | 10348 | 0.001 | 0.000 | 1.286 | 0.000 | 0.088148 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2346) vms_mb | MB | 10349 | 131.256 | 131.172 | 131.945 | 131.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 2460) CPU | percent | 10341 | 0.002 | 0.000 | 1.990 | 0.000 | 0.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 2460) rss_mb | MB | 10342 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 2460) main thread run-queue wait | percent | 10341 | 0.004 | 0.000 | 5.463 | 0.000 | 0.386179 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 2460) vms_mb | MB | 10342 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 2494) CPU | percent | 10341 | 0.003 | 0.000 | 0.995 | 0.000 | 0.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 2494) rss_mb | MB | 10342 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 2494) main thread run-queue wait | percent | 10341 | 0.004 | 0.000 | 5.155 | 0.018 | 0.460478 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 2494) vms_mb | MB | 10342 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 2589) CPU | percent | 10341 | 44.110 | 0.000 | 92.027 | 0.000 | 4588.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 2589) rss_mb | MB | 10342 | 105.138 | 3.035 | 133.656 | 133.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 2589) main thread run-queue wait | percent | 10341 | 0.000 | 0.000 | 0.011 | 0.000 | 0.000219 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 2589) vms_mb | MB | 10342 | 966.876 | 4.262 | 985.586 | 972.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 2595) CPU | percent | 2 | 56.089 | 51.597 | 60.581 | 60.581 | 1.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 2595) rss_mb | MB | 3 | 48.497 | 20.254 | 77.027 | 77.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 2595) main thread run-queue wait | percent | 2 | 0.034 | 0.034 | 0.035 | 0.035 | 0.000693 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 2595) vms_mb | MB | 3 | 58.997 | 27.016 | 92.902 | 92.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 2603) rss_mb | MB | 1 | 119.062 | 119.062 | 119.062 | 119.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 2603) vms_mb | MB | 1 | 1849.492 | 1849.492 | 1849.492 | 1849.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 2612) CPU | percent | 10311 | 1.885 | 0.000 | 22.839 | 0.995 | 195.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 2612) rss_mb | MB | 10312 | 266.688 | 215.293 | 319.633 | 319.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 2612) main thread run-queue wait | percent | 10311 | 0.645 | 0.000 | 60.265 | 0.009 | 67.000334 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 2612) vms_mb | MB | 10312 | 2211.806 | 1988.535 | 2273.488 | 2273.457 | n/a | n/a |
| sleep (PID 2636) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2636) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2636) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2636) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2636) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2636) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 2638) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2638) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2638) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2638) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2638) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2638) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 2650) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2650) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2650) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2650) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2650) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2650) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 2744) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2744) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2744) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2744) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2744) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2744) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 2746) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 2746) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2746) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 2746) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 2746) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 2746) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3033) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3033) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3033) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3033) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3033) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3033) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3098) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3098) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3098) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3098) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3098) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3098) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3103) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3103) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3103) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3103) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3103) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3103) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3260) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3260) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3260) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3260) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3260) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3260) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3262) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3262) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3262) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3262) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3262) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3262) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3382) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3382) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3382) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3382) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3382) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3382) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3502) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3502) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3502) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3502) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3502) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3502) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 3510) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 3510) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 3511) rss_mb | MB | 1 | 18.301 | 18.301 | 18.301 | 18.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 3511) vms_mb | MB | 1 | 24.172 | 24.172 | 24.172 | 24.172 | n/a | n/a |
| sleep (PID 3639) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3639) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3639) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3639) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3639) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3639) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3727) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3727) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3727) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3727) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3727) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3727) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3729) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3729) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3729) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3729) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3729) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3729) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3734) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3734) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3734) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3734) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3734) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3734) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3736) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3736) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3736) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3736) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 3736) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3736) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3739) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3739) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3739) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3739) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3739) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3739) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 3903) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 3903) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 3904) rss_mb | MB | 1 | 14.773 | 14.773 | 14.773 | 14.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 3904) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sleep (PID 3920) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3920) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3920) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3920) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3920) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3920) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3922) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3922) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3922) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3922) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3922) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3922) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3934) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3934) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3934) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3934) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3934) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3934) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 3947) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3947) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3947) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3947) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3947) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3947) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4032) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4032) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4032) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4032) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4032) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4032) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4119) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4119) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4119) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4119) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4119) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4119) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4121) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4121) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4121) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4121) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4121) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4121) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4123) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4123) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4123) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4123) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4123) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4123) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 4126) rss_mb | MB | 1 | 8.586 | 8.586 | 8.586 | 8.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 4126) vms_mb | MB | 1 | 13.195 | 13.195 | 13.195 | 13.195 | n/a | n/a |
| sleep (PID 4142) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4142) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4142) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4142) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4142) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4142) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4145) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4145) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4145) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4145) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 4145) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4145) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4257) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4257) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4257) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4257) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4257) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4257) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4259) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4259) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4259) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4259) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4259) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4259) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4261) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4261) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4261) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4261) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4261) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4261) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4263) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4263) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4263) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4263) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4263) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4263) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4279) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4279) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4279) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4279) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4279) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4279) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4376) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4376) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4376) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4376) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4376) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4376) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4378) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4378) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4378) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4378) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4378) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4378) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4380) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4380) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4380) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4380) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4380) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4380) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4403) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4403) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4404) rss_mb | MB | 1 | 9.852 | 9.852 | 9.852 | 9.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4404) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sleep (PID 4430) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4430) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4430) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4430) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4430) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4430) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4433) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4433) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4433) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4433) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4433) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4433) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4530) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4530) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4530) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4530) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4530) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4530) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4532) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4532) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4532) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4532) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4532) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4532) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4533) rss_mb | MB | 1 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4533) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4534) rss_mb | MB | 1 | 9.812 | 9.812 | 9.812 | 9.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4534) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| pgrep (PID 4545) rss_mb | MB | 1 | 3.305 | 3.305 | 3.305 | 3.305 | n/a | n/a |
| pgrep (PID 4545) vms_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sleep (PID 4546) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4546) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4546) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4546) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4546) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4546) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4548) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4548) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4548) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4548) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 4548) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4548) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4550) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4550) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4550) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4550) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4550) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4550) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4649) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4649) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4649) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4649) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4649) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4649) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4652) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4652) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4652) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4652) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 4652) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4652) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 4656) rss_mb | MB | 1 | 31.676 | 31.676 | 31.676 | 31.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 4656) vms_mb | MB | 1 | 35.508 | 35.508 | 35.508 | 35.508 | n/a | n/a |
| sleep (PID 4666) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4666) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4666) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4666) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4666) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4666) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4695) rss_mb | MB | 1 | 1.281 | 1.281 | 1.281 | 1.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4695) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4696) rss_mb | MB | 1 | 20.945 | 20.945 | 20.945 | 20.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4696) vms_mb | MB | 1 | 25.699 | 25.699 | 25.699 | 25.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4701) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4701) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4702) rss_mb | MB | 1 | 9.586 | 9.586 | 9.586 | 9.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4702) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sleep (PID 4712) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4712) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4712) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4712) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4712) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4712) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4713) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4713) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4714) rss_mb | MB | 1 | 9.590 | 9.590 | 9.590 | 9.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4714) vms_mb | MB | 1 | 13.727 | 13.727 | 13.727 | 13.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4771) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 4771) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4772) rss_mb | MB | 1 | 20.492 | 20.492 | 20.492 | 20.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 4772) vms_mb | MB | 1 | 25.461 | 25.461 | 25.461 | 25.461 | n/a | n/a |
| sleep (PID 4778) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4778) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4778) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4778) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4778) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4778) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4897) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4897) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4897) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4897) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4897) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4897) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4901) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4901) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4901) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4901) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4901) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4901) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4903) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4903) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4903) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4903) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4903) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4903) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4959) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4959) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4959) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4959) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4959) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4959) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4989) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4989) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4989) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4989) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4989) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4989) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5098) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5098) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5098) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5098) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5098) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5098) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5135) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5135) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5135) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5135) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5135) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5135) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5141) rss_mb | MB | 1 | 1.488 | 1.488 | 1.488 | 1.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5141) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5142) rss_mb | MB | 1 | 9.055 | 9.055 | 9.055 | 9.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5142) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5148) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5148) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5149) rss_mb | MB | 1 | 16.953 | 16.953 | 16.953 | 16.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5149) vms_mb | MB | 1 | 23.020 | 23.020 | 23.020 | 23.020 | n/a | n/a |
| sleep (PID 5159) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5159) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5159) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5159) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5159) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5159) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5179) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5179) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5179) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5179) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5179) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5179) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5201) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5201) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5201) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5201) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5201) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5201) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5354) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5354) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5354) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5354) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5354) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5354) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5398) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5398) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5398) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5398) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5398) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5398) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5501) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5501) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5501) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5501) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5501) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5501) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5506) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5506) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5507) rss_mb | MB | 1 | 15.086 | 15.086 | 15.086 | 15.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5507) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sleep (PID 5517) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5517) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5517) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5517) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 5517) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5517) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5532) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5532) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5532) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5532) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5532) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5532) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5555) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5555) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5556) rss_mb | MB | 1 | 20.875 | 20.875 | 20.875 | 20.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5556) vms_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| sleep (PID 5560) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5560) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5560) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5560) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5560) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5560) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5576) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5576) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5576) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5576) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5576) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5576) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_heads.py (PID 5584) CPU | percent | 2 | 134.488 | 115.061 | 153.916 | 153.916 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_heads.py (PID 5584) rss_mb | MB | 3 | 867.079 | 23.379 | 1305.430 | 1305.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_heads.py (PID 5584) main thread run-queue wait | percent | 2 | 37.501 | 15.543 | 59.459 | 59.459 | 0.755484 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_heads.py (PID 5584) vms_mb | MB | 3 | 1079.302 | 215.922 | 1527.496 | 1527.496 | n/a | n/a |
| sleep (PID 5595) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5595) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5595) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5595) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5595) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5595) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 5604) CPU | percent | 2 | 134.453 | 100.011 | 168.894 | 168.894 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 5604) rss_mb | MB | 3 | 752.309 | 18.453 | 1158.977 | 1158.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 5604) main thread run-queue wait | percent | 2 | 30.520 | 5.424 | 55.616 | 55.616 | 0.614576 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 5604) vms_mb | MB | 3 | 964.346 | 210.445 | 1380.973 | 1380.973 | n/a | n/a |
| sleep (PID 5616) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5616) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5616) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5616) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5616) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5616) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5619) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5619) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5619) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5619) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5619) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5619) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 5637) rss_mb | MB | 1 | 16.852 | 16.852 | 16.852 | 16.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 5637) vms_mb | MB | 1 | 208.582 | 208.582 | 208.582 | 208.582 | n/a | n/a |
| sleep (PID 5654) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5654) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5654) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5654) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5654) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5654) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5732) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5732) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5732) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5732) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5732) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5732) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5734) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5734) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5734) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5734) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5734) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5734) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_mechanisms.py (PID 5742) CPU | percent | 7 | 171.312 | 162.830 | 177.302 | 168.034 | 12.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_mechanisms.py (PID 5742) rss_mb | MB | 8 | 59.388 | 10.688 | 131.422 | 131.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_mechanisms.py (PID 5742) main thread run-queue wait | percent | 7 | 67.520 | 54.662 | 72.258 | 71.288 | 4.757096 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_mechanisms.py (PID 5742) vms_mb | MB | 8 | 256.946 | 46.172 | 349.270 | 349.270 | n/a | n/a |
| sleep (PID 5755) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5755) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5755) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5755) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5755) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5755) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5775) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5775) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5775) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5775) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5775) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5775) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5776) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5776) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5777) rss_mb | MB | 1 | 21.516 | 21.516 | 21.516 | 21.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5777) vms_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5811) rss_mb | MB | 1 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5811) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5812) rss_mb | MB | 1 | 10.547 | 10.547 | 10.547 | 10.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5812) vms_mb | MB | 1 | 15.062 | 15.062 | 15.062 | 15.062 | n/a | n/a |
| sleep (PID 5819) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5819) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5819) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5819) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5819) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5819) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5823) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5823) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5824) rss_mb | MB | 1 | 19.504 | 19.504 | 19.504 | 19.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5824) vms_mb | MB | 1 | 24.812 | 24.812 | 24.812 | 24.812 | n/a | n/a |
| sleep (PID 5838) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5838) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5838) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5838) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5838) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5838) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 5922) rss_mb | MB | 1 | 7.578 | 7.578 | 7.578 | 7.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 5922) vms_mb | MB | 1 | 11.988 | 11.988 | 11.988 | 11.988 | n/a | n/a |
| sleep (PID 5930) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5930) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5930) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5930) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5930) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5930) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5932) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5932) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5932) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5932) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5932) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5932) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5935) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5935) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5935) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5935) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5935) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5935) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5964) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5964) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5964) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5964) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5964) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5964) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| pgrep (PID 5965) rss_mb | MB | 1 | 3.289 | 3.289 | 3.289 | 3.289 | n/a | n/a |
| pgrep (PID 5965) vms_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sleep (PID 5966) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5966) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5966) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5966) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5966) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5966) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 5968) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 5968) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5968) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 5968) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 5968) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 5968) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5976) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5976) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5977) rss_mb | MB | 1 | 14.203 | 14.203 | 14.203 | 14.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5977) vms_mb | MB | 1 | 19.957 | 19.957 | 19.957 | 19.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5997) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 5997) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5998) rss_mb | MB | 1 | 16.387 | 16.387 | 16.387 | 16.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 5998) vms_mb | MB | 1 | 21.848 | 21.848 | 21.848 | 21.848 | n/a | n/a |
| sleep (PID 6012) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6012) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6012) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6012) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6012) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6012) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6026) rss_mb | MB | 1 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6026) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6027) rss_mb | MB | 1 | 7.250 | 7.250 | 7.250 | 7.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6027) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sleep (PID 6052) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6052) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6052) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6052) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6052) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6052) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6087) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6087) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6088) rss_mb | MB | 1 | 19.422 | 19.422 | 19.422 | 19.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6088) vms_mb | MB | 1 | 24.812 | 24.812 | 24.812 | 24.812 | n/a | n/a |
| sleep (PID 6094) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6094) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6094) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6094) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6094) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6094) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6122) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6122) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6123) rss_mb | MB | 1 | 21.566 | 21.566 | 21.566 | 21.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6123) vms_mb | MB | 1 | 27.000 | 27.000 | 27.000 | 27.000 | n/a | n/a |
| sleep (PID 6129) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6129) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6129) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6129) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6129) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6129) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — prep_trace2.py (PID 6133) rss_mb | MB | 1 | 125.113 | 125.113 | 125.113 | 125.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — prep_trace2.py (PID 6133) vms_mb | MB | 1 | 130.758 | 130.758 | 130.758 | 130.758 | n/a | n/a |
| sleep (PID 6153) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6153) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6153) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6153) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6153) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6153) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6159) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6159) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6160) rss_mb | MB | 1 | 9.812 | 9.812 | 9.812 | 9.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6160) vms_mb | MB | 1 | 13.727 | 13.727 | 13.727 | 13.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6165) rss_mb | MB | 1 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6165) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6166) rss_mb | MB | 1 | 7.730 | 7.730 | 7.730 | 7.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6166) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sleep (PID 6176) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6176) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6176) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6176) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6176) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6176) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6177) rss_mb | MB | 1 | 1.605 | 1.605 | 1.605 | 1.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6177) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6178) rss_mb | MB | 1 | 20.766 | 20.766 | 20.766 | 20.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6178) vms_mb | MB | 1 | 25.828 | 25.828 | 25.828 | 25.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6193) rss_mb | MB | 1 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6193) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6194) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6194) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sleep (PID 6209) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6209) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6209) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6209) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6209) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6209) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| pgrep (PID 6225) rss_mb | MB | 1 | 3.055 | 3.055 | 3.055 | 3.055 | n/a | n/a |
| pgrep (PID 6225) vms_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sleep (PID 6226) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6226) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6226) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6226) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6226) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6226) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6230) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6230) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6231) rss_mb | MB | 1 | 7.980 | 7.980 | 7.980 | 7.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6231) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sleep (PID 6245) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6245) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6245) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6245) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6245) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6245) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_subspaces_and_gates.py (PID 6250) CPU | percent | 45 | 175.291 | 148.171 | 180.241 | 177.040 | 79.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_subspaces_and_gates.py (PID 6250) rss_mb | MB | 46 | 160.622 | 57.852 | 165.637 | 165.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_subspaces_and_gates.py (PID 6250) main thread run-queue wait | percent | 45 | 59.187 | 47.310 | 79.666 | 49.360 | 26.867811 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_subspaces_and_gates.py (PID 6250) vms_mb | MB | 46 | 379.882 | 256.816 | 385.047 | 384.426 | n/a | n/a |
| sleep (PID 6260) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6260) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6260) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6260) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6260) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6260) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6268) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6268) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6268) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6268) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6268) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6268) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_internals_deep.py (PID 6272) CPU | percent | 100 | 176.188 | 162.449 | 181.831 | 177.153 | 177.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_internals_deep.py (PID 6272) rss_mb | MB | 101 | 213.155 | 124.449 | 279.277 | 279.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_internals_deep.py (PID 6272) main thread run-queue wait | percent | 100 | 55.133 | 45.926 | 77.090 | 46.946 | 55.543997 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_internals_deep.py (PID 6272) vms_mb | MB | 101 | 432.876 | 343.625 | 498.441 | 498.441 | n/a | n/a |
| sleep (PID 6279) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6279) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6279) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6279) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6279) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6279) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6303) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6303) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6303) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6303) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6303) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6303) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6322) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6322) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6322) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6322) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6322) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6322) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6334) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6334) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6334) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6334) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6334) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6334) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6336) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6336) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6336) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6336) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6336) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6336) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6339) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6339) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6339) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6339) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6339) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6339) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6356) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6356) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6356) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6356) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6356) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6356) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6368) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6368) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6369) rss_mb | MB | 1 | 20.824 | 20.824 | 20.824 | 20.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6369) vms_mb | MB | 1 | 25.586 | 25.586 | 25.586 | 25.586 | n/a | n/a |
| sleep (PID 6381) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6381) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6381) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6381) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6381) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6381) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6383) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6383) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6383) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6383) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6383) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6383) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6385) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6385) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6385) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6385) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6385) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6385) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_weight_geometry.py (PID 6389) CPU | percent | 47 | 174.027 | 152.394 | 183.979 | 164.998 | 82.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_weight_geometry.py (PID 6389) rss_mb | MB | 48 | 163.227 | 14.605 | 247.113 | 247.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_weight_geometry.py (PID 6389) main thread run-queue wait | percent | 47 | 58.435 | 43.605 | 74.962 | 70.824 | 27.688913 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_weight_geometry.py (PID 6389) vms_mb | MB | 48 | 382.222 | 208.988 | 465.281 | 465.281 | n/a | n/a |
| sleep (PID 6402) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6402) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6402) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6402) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6402) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6402) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6426) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6426) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6426) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6426) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6426) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6426) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6428) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6428) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6428) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6428) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6428) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6428) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6430) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6430) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6430) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6430) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6430) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6430) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6432) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6432) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6432) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6432) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6432) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6432) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6442) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6442) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6442) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6442) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6442) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6442) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| pgrep (PID 6461) rss_mb | MB | 1 | 3.289 | 3.289 | 3.289 | 3.289 | n/a | n/a |
| pgrep (PID 6461) vms_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sleep (PID 6462) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6462) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6462) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6462) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6462) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6462) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6464) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6464) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6464) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6464) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6464) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6464) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6466) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6466) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6466) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6466) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6466) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6466) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6493) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6493) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6493) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6493) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6493) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6493) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_unembed_nullspace.py (PID 6497) CPU | percent | 52 | 173.030 | 133.528 | 182.086 | 158.019 | 90.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_unembed_nullspace.py (PID 6497) rss_mb | MB | 53 | 468.896 | 21.129 | 2545.449 | 2545.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_unembed_nullspace.py (PID 6497) main thread run-queue wait | percent | 52 | 53.011 | 14.267 | 74.353 | 37.842 | 27.779665 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_unembed_nullspace.py (PID 6497) vms_mb | MB | 53 | 717.998 | 212.453 | 4354.801 | 4354.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6508) rss_mb | MB | 1 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6508) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6509) rss_mb | MB | 1 | 9.227 | 9.227 | 9.227 | 9.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6509) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sleep (PID 6512) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6512) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6512) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6512) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6512) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6512) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6536) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6536) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6536) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6536) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6536) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6536) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 6540) CPU | percent | 2 | 148.061 | 122.279 | 173.844 | 173.844 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 6540) rss_mb | MB | 3 | 761.206 | 71.902 | 1126.352 | 1126.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 6540) main thread run-queue wait | percent | 2 | 43.150 | 18.675 | 67.625 | 67.625 | 0.868598 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 6540) vms_mb | MB | 3 | 973.335 | 264.410 | 1348.160 | 1348.160 | n/a | n/a |
| sleep (PID 6554) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6554) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6554) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6554) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6554) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6554) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6632) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6632) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6632) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6632) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6632) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6632) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — design_detectors_and_vectors.py (PID 6678) CPU | percent | 92 | 174.119 | 138.212 | 181.802 | 181.802 | 161.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — design_detectors_and_vectors.py (PID 6678) rss_mb | MB | 93 | 410.320 | 23.762 | 4171.953 | 2621.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — design_detectors_and_vectors.py (PID 6678) main thread run-queue wait | percent | 92 | 60.838 | 16.889 | 79.705 | 42.446 | 56.385659 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — design_detectors_and_vectors.py (PID 6678) vms_mb | MB | 93 | 648.646 | 216.234 | 4495.828 | 4495.828 | n/a | n/a |
| sleep (PID 6685) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6685) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6685) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6685) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 6685) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6685) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6692) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6692) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6692) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6692) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6692) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6692) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6722) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6722) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6722) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6722) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6722) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6722) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — prep_heldout.py (PID 6727) rss_mb | MB | 1 | 56.137 | 56.137 | 56.137 | 56.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — prep_heldout.py (PID 6727) vms_mb | MB | 1 | 248.137 | 248.137 | 248.137 | 248.137 | n/a | n/a |
| sleep (PID 6739) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6739) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6739) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6739) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6739) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6739) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 6743) rss_mb | MB | 1 | 7.938 | 7.938 | 7.938 | 7.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 6743) vms_mb | MB | 1 | 12.926 | 12.926 | 12.926 | 12.926 | n/a | n/a |
| sleep (PID 6752) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6752) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6752) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6752) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6752) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6752) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6754) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6754) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6754) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6754) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6754) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6754) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6756) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6756) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6756) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6756) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6756) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6756) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6787) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6787) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6787) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6787) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6787) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6787) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6789) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6789) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6789) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6789) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6789) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6789) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6809) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6809) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6810) rss_mb | MB | 1 | 7.871 | 7.871 | 7.871 | 7.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6810) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6831) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6831) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6832) rss_mb | MB | 1 | 10.570 | 10.570 | 10.570 | 10.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6832) vms_mb | MB | 1 | 15.062 | 15.062 | 15.062 | 15.062 | n/a | n/a |
| sleep (PID 6838) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6838) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6838) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6838) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6838) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6838) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6840) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6840) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6840) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6840) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6840) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6840) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6843) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6843) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6843) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6843) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6843) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6843) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6867) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6867) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6868) rss_mb | MB | 1 | 10.711 | 10.711 | 10.711 | 10.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6868) vms_mb | MB | 1 | 15.273 | 15.273 | 15.273 | 15.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 6878) rss_mb | MB | 1 | 290.152 | 290.152 | 290.152 | 290.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 6878) vms_mb | MB | 1 | 2272.605 | 2272.605 | 2272.605 | 2272.605 | n/a | n/a |
| sleep (PID 6887) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6887) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6887) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6887) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6887) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6887) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6892) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6892) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6892) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6892) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6892) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6892) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6899) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6899) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6900) rss_mb | MB | 1 | 18.727 | 18.727 | 18.727 | 18.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6900) vms_mb | MB | 1 | 24.559 | 24.559 | 24.559 | 24.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_heldout_oos.py (PID 6915) CPU | percent | 3 | 154.790 | 132.210 | 166.103 | 166.057 | 4.670000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_heldout_oos.py (PID 6915) rss_mb | MB | 4 | 834.975 | 51.160 | 1096.246 | 1096.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_heldout_oos.py (PID 6915) main thread run-queue wait | percent | 3 | 44.211 | 16.293 | 63.427 | 63.427 | 1.333760 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_heldout_oos.py (PID 6915) vms_mb | MB | 4 | 1052.942 | 255.543 | 1318.742 | 1318.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6920) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6920) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6921) rss_mb | MB | 1 | 5.031 | 5.031 | 5.031 | 5.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6921) vms_mb | MB | 1 | 11.383 | 11.383 | 11.383 | 11.383 | n/a | n/a |
| sleep (PID 6927) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6927) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6927) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6927) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6927) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6927) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — eval_oos_detectors.py (PID 6931) CPU | percent | 3 | 165.786 | 164.418 | 167.447 | 165.493 | 5.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — eval_oos_detectors.py (PID 6931) rss_mb | MB | 4 | 178.431 | 119.516 | 244.391 | 167.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — eval_oos_detectors.py (PID 6931) main thread run-queue wait | percent | 3 | 54.215 | 48.355 | 63.280 | 51.010 | 1.641678 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — eval_oos_detectors.py (PID 6931) vms_mb | MB | 4 | 397.988 | 339.422 | 463.961 | 386.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6936) rss_mb | MB | 1 | 1.387 | 1.387 | 1.387 | 1.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 6936) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6937) rss_mb | MB | 1 | 21.211 | 21.211 | 21.211 | 21.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 6937) vms_mb | MB | 1 | 25.840 | 25.840 | 25.840 | 25.840 | n/a | n/a |
| sleep (PID 6943) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6943) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6943) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6943) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6943) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6943) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 6946) CPU | percent | 5 | 163.898 | 148.713 | 170.399 | 148.713 | 8.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 6946) rss_mb | MB | 6 | 197.158 | 122.336 | 276.141 | 168.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 6946) main thread run-queue wait | percent | 5 | 54.543 | 45.131 | 64.381 | 54.336 | 2.751782 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 6946) vms_mb | MB | 6 | 417.373 | 344.348 | 495.754 | 388.211 | n/a | n/a |
| sleep (PID 6958) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6958) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6958) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6958) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6958) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6958) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6978) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6978) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6978) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6978) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6978) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6978) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6980) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6980) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6980) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6980) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6980) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6980) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6986) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6986) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6986) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6986) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6986) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6986) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6992) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6992) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6992) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6992) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6992) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6992) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 6998) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 6998) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6998) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 6998) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 6998) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 6998) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7017) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7017) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7017) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7017) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7017) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7017) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_l18_and_reg.py (PID 7021) CPU | percent | 29 | 173.265 | 152.570 | 178.843 | 169.656 | 50.640000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_l18_and_reg.py (PID 7021) rss_mb | MB | 30 | 216.787 | 113.941 | 320.684 | 320.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_l18_and_reg.py (PID 7021) main thread run-queue wait | percent | 29 | 57.325 | 47.918 | 79.294 | 52.550 | 16.755475 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_l18_and_reg.py (PID 7021) vms_mb | MB | 30 | 436.859 | 344.770 | 540.559 | 540.559 | n/a | n/a |
| sleep (PID 7036) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7036) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7036) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7036) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7036) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7036) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7039) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7039) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7039) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7039) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7039) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7039) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7041) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7041) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7041) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7041) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7041) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7041) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7054) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7054) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7054) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7054) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7054) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7054) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7073) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7073) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7073) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7073) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7073) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7073) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_l22_digits.py (PID 7077) CPU | percent | 1 | 134.165 | 134.165 | 134.165 | 134.165 | 1.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_l22_digits.py (PID 7077) rss_mb | MB | 2 | 596.488 | 62.578 | 1130.398 | 1130.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_l22_digits.py (PID 7077) main thread run-queue wait | percent | 1 | 17.418 | 17.418 | 17.418 | 17.418 | 0.175265 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_l22_digits.py (PID 7077) vms_mb | MB | 2 | 811.453 | 272.129 | 1350.777 | 1350.777 | n/a | n/a |
| sleep (PID 7090) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7090) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7090) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7090) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7090) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7090) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7092) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7092) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7092) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7092) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7092) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7092) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7093) rss_mb | MB | 1 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7093) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7094) rss_mb | MB | 1 | 7.109 | 7.109 | 7.109 | 7.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7094) vms_mb | MB | 1 | 11.660 | 11.660 | 11.660 | 11.660 | n/a | n/a |
| sleep (PID 7106) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7106) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7106) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7106) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7106) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7106) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_2digit.py (PID 7122) rss_mb | MB | 1 | 1545.391 | 1545.391 | 1545.391 | 1545.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_2digit.py (PID 7122) vms_mb | MB | 1 | 1739.719 | 1739.719 | 1739.719 | 1739.719 | n/a | n/a |
| sleep (PID 7134) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7134) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7134) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7134) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7134) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7134) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7354) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7354) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7354) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7354) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7354) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7354) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7359) CPU | percent | 38 | 173.658 | 122.346 | 180.426 | 177.777 | 66.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7359) rss_mb | MB | 39 | 2321.333 | 105.988 | 4032.359 | 2337.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7359) main thread run-queue wait | percent | 38 | 50.098 | 17.811 | 64.573 | 50.380 | 19.189824 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7359) vms_mb | MB | 39 | 2552.481 | 298.766 | 4493.957 | 2554.023 | n/a | n/a |
| sleep (PID 7375) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7375) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7375) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7375) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7375) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7375) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7381) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7381) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7381) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7381) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7381) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7381) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7391) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7391) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7392) rss_mb | MB | 1 | 16.758 | 16.758 | 16.758 | 16.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7392) vms_mb | MB | 1 | 22.141 | 22.141 | 22.141 | 22.141 | n/a | n/a |
| sleep (PID 7414) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7414) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7414) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7414) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 7414) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7414) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7418) rss_mb | MB | 1 | 1.605 | 1.605 | 1.605 | 1.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7418) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7419) rss_mb | MB | 1 | 14.672 | 14.672 | 14.672 | 14.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7419) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sleep (PID 7431) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7431) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7431) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7431) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7431) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7431) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7529) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7529) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7529) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7529) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7529) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7529) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_unedited_details.py (PID 7537) CPU | percent | 4 | 159.195 | 153.013 | 162.595 | 158.664 | 6.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_unedited_details.py (PID 7537) rss_mb | MB | 5 | 162.227 | 124.316 | 201.805 | 200.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_unedited_details.py (PID 7537) main thread run-queue wait | percent | 4 | 57.300 | 49.974 | 59.947 | 59.726 | 2.313790 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_unedited_details.py (PID 7537) vms_mb | MB | 5 | 384.411 | 344.719 | 432.387 | 419.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7543) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7543) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7544) rss_mb | MB | 1 | 20.367 | 20.367 | 20.367 | 20.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7544) vms_mb | MB | 1 | 25.199 | 25.199 | 25.199 | 25.199 | n/a | n/a |
| sleep (PID 7550) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7550) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7550) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7550) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7550) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7550) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7552) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7552) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7552) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7552) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7552) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7552) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7553) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7553) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7554) rss_mb | MB | 1 | 21.723 | 21.723 | 21.723 | 21.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7554) vms_mb | MB | 1 | 27.039 | 27.039 | 27.039 | 27.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_heads_and_gclause.py (PID 7560) CPU | percent | 5 | 163.912 | 157.772 | 169.009 | 160.078 | 8.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_heads_and_gclause.py (PID 7560) rss_mb | MB | 6 | 174.200 | 18.629 | 290.945 | 290.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_heads_and_gclause.py (PID 7560) main thread run-queue wait | percent | 5 | 44.592 | 35.626 | 60.549 | 38.992 | 2.255356 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_heads_and_gclause.py (PID 7560) vms_mb | MB | 6 | 389.207 | 210.289 | 509.953 | 509.953 | n/a | n/a |
| sleep (PID 7572) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7572) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7572) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7572) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7572) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7572) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 7589) CPU | percent | 2 | 123.661 | 101.223 | 146.099 | 146.099 | 2.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 7589) rss_mb | MB | 3 | 790.382 | 7.215 | 1211.340 | 1152.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 7589) main thread run-queue wait | percent | 2 | 31.077 | 6.691 | 55.463 | 55.463 | 0.625475 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_guess_copy.py (PID 7589) vms_mb | MB | 3 | 1043.007 | 11.789 | 1743.078 | 1374.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7593) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7593) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7594) rss_mb | MB | 1 | 10.516 | 10.516 | 10.516 | 10.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7594) vms_mb | MB | 1 | 15.117 | 15.117 | 15.117 | 15.117 | n/a | n/a |
| sleep (PID 7601) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7601) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7601) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7601) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7601) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7601) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7618) rss_mb | MB | 1 | 1.582 | 1.582 | 1.582 | 1.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7618) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7619) rss_mb | MB | 1 | 20.848 | 20.848 | 20.848 | 20.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7619) vms_mb | MB | 1 | 25.836 | 25.836 | 25.836 | 25.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 7721) rss_mb | MB | 1 | 160.051 | 160.051 | 160.051 | 160.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 7721) vms_mb | MB | 1 | 769.887 | 769.887 | 769.887 | 769.887 | n/a | n/a |
| sleep (PID 7732) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7732) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7732) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7732) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7732) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7732) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7734) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7734) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7734) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7734) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7734) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7734) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 7738) rss_mb | MB | 1 | 83.066 | 83.066 | 83.066 | 83.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 7738) vms_mb | MB | 1 | 304.020 | 304.020 | 304.020 | 304.020 | n/a | n/a |
| sleep (PID 7750) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7750) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7750) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7750) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 7750) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7750) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7752) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7752) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7752) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7752) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7752) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7752) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_b14_head_symmetry.py (PID 7761) CPU | percent | 8 | 173.065 | 161.081 | 178.035 | 169.995 | 13.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_b14_head_symmetry.py (PID 7761) rss_mb | MB | 9 | 2038.725 | 1153.102 | 2489.793 | 2231.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_b14_head_symmetry.py (PID 7761) main thread run-queue wait | percent | 8 | 53.644 | 35.917 | 65.944 | 42.851 | 4.317738 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_b14_head_symmetry.py (PID 7761) vms_mb | MB | 9 | 2488.615 | 1740.324 | 4383.273 | 2449.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7766) rss_mb | MB | 1 | 1.598 | 1.598 | 1.598 | 1.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7766) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7767) rss_mb | MB | 1 | 7.691 | 7.691 | 7.691 | 7.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7767) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sleep (PID 7773) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7773) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7773) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7773) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 7773) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7773) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7870) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7870) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7870) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7870) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7870) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7870) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7871) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 7871) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7872) rss_mb | MB | 1 | 20.359 | 20.359 | 20.359 | 20.359 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 7872) vms_mb | MB | 1 | 25.188 | 25.188 | 25.188 | 25.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7879) CPU | percent | 27 | 171.843 | 125.275 | 180.368 | 176.974 | 46.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7879) rss_mb | MB | 28 | 1960.554 | 14.773 | 3753.492 | 2375.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7879) main thread run-queue wait | percent | 27 | 52.699 | 25.469 | 75.729 | 49.925 | 14.349986 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7879) vms_mb | MB | 28 | 2222.521 | 209.172 | 4532.156 | 2592.152 | n/a | n/a |
| sleep (PID 7884) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7884) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7884) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7884) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7884) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7884) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7916) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7916) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7916) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7916) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7916) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7916) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7918) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7918) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7918) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7918) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7918) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7918) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 7927) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 7927) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7927) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 7927) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 7927) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 7927) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7953) CPU | percent | 27 | 170.838 | 126.307 | 181.322 | 179.236 | 46.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7953) rss_mb | MB | 28 | 1912.663 | 14.605 | 2376.195 | 2376.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7953) main thread run-queue wait | percent | 27 | 52.247 | 18.409 | 63.667 | 58.193 | 14.217662 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_and_audit_adapter.py (PID 7953) vms_mb | MB | 28 | 2148.152 | 209.211 | 2592.844 | 2592.844 | n/a | n/a |
| sleep (PID 8042) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8042) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8042) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8042) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8042) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8042) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8043) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8043) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 8044) rss_mb | MB | 1 | 15.672 | 15.672 | 15.672 | 15.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 8044) vms_mb | MB | 1 | 20.500 | 20.500 | 20.500 | 20.500 | n/a | n/a |
| sleep (PID 8052) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8052) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8052) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8052) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8052) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8052) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 8058) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8058) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8058) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8058) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8058) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8058) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8059) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 8059) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 8060) rss_mb | MB | 1 | 9.609 | 9.609 | 9.609 | 9.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 8060) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sleep (PID 8071) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8071) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8071) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8071) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8071) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8071) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 8083) CPU | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 8083) io read MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8083) io write MB/s | MB/s | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 8083) rss_mb | MB | 48 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 8083) main thread run-queue wait | percent | 47 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 8083) vms_mb | MB | 48 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| docker inspect (PID 8123) rss_mb | MB | 1 | 30.219 | 30.219 | 30.219 | 30.219 | n/a | n/a |
| docker inspect (PID 8123) vms_mb | MB | 1 | 1907.832 | 1907.832 | 1907.832 | 1907.832 | n/a | n/a |
| docker commit (PID 8140) CPU | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 8140) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8140) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8140) rss_mb | MB | 23 | 28.621 | 0.000 | 29.922 | 0.000 | n/a | n/a |
| docker commit (PID 8140) main thread run-queue wait | percent | 22 | 0.002 | 0.000 | 0.038 | 0.038 | 0.000382 run-queue seconds | n/a |
| docker commit (PID 8140) vms_mb | MB | 23 | 1824.412 | 0.000 | 1907.340 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 CPU | percent | 10341 | 55.111 | 0.000 | 218.497 | 0.037 | 5734.322654 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 10341 | 2.676 | 0.000 | 50.839 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 10341 | 3.499 | 0.000 | 74.045 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io_psi_full_pct | percent of wall time stalled | 10341 | 0.009 | 0.000 | 20.325 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io_psi_some_pct | percent of wall time stalled | 10341 | 0.010 | 0.000 | 20.325 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io read MB/s | MB/s | 10341 | 0.021 | 0.000 | 30.417 | 0.000 | 221.324219 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io write MB/s | MB/s | 10341 | 0.034 | 0.000 | 6.299 | 0.000 | 356.863281 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory | MB | 10342 | 406.778 | 35.227 | 4560.008 | 298.488 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory_psi_full_pct | percent of wall time stalled | 10341 | 0.003 | 0.000 | 6.715 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory_psi_some_pct | percent of wall time stalled | 10341 | 0.003 | 0.000 | 6.715 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 net rx MB/s | MB/s | 10341 | 0.000 | 0.000 | 0.007 | 0.000 | 0.414234 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 net tx MB/s | MB/s | 10341 | 0.000 | 0.000 | 0.036 | 0.000 | 2.683685 MB | n/a |
| workload total CPU | percent | 10348 | 2.527 | 1.504 | 116.666 | 2.061 | 263.289064 CPU seconds | n/a |
| workload total memory | MB | 10349 | 9020.232 | 8178.359 | 10082.281 | 9078.070 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
