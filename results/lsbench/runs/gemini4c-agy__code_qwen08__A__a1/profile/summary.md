# agprof summary

- Duration: **10140.797 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **130 calls**, 130 succeeded, 0 failed, 0 interrupted, n/a reported retries, 9297.124 s total wait
- Tools: **185/185 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **1123817** at 1.972 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 10133468.009 / 10133468.009 ms |
| LLM latency p50 / p95 | 32061.753 / 228700.504 ms |
| LLM TTFT p50 / p95 | 20328.573 / 218599.339 ms |
| LLM input / output tokens | 15982499 / 189399 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 130 total, 130 succeeded, 0 failed, 0 interrupted |
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
| edit_file | 8/8 | 8 | 0 | 0 | n/a | n/a |
| mcp__agency__attention | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 9/9 | 9 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 12/12 | 12 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 10/10 | 10 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 7/7 | 7 | 0 | 0 | n/a | n/a |
| read_file | 39/39 | 39 | 0 | 0 | n/a | n/a |
| run_command | 74/74 | 74 | 0 | 0 | n/a | n/a |
| write_file | 17/17 | 17 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 3.499% | 175.147% | 355.378 s | 6201.980 MB | 7786.684 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| tail | 9352 | sandbox_agent_lsb-antigravity_0000_0000 | 10072 | 0.003% | 0.995% | 0.260 s | 1.508 MB | 1.508 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| lsb_grid_worker | 9041 |  | 10079 | 0.000% | 0.000% | 0.000 s | 3.324 MB | 3.324 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 9441 | sandbox_agent_lsb-antigravity_0000_0000 | 10072 | 43.643% | 95.362% | 4421.510 s | 105.811 MB | 134.906 MB | 970.153 MB | 973.188 MB | n/a MB | n/a MB |
| python | 9095 |  | 10079 | 0.000% | 0.000% | 0.000 s | 12.188 MB | 12.188 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9065 |  | 16 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 9320 | sandbox_agent_lsb-antigravity_0000_0000 | 10072 | 0.002% | 0.995% | 0.200 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python | 9201 |  | 10079 | 0.040% | 3.976% | 4.060 s | 45.309 MB | 45.559 MB | 131.213 MB | 131.707 MB | 0.003906 MB | 0.351562 MB |
| python3 | 9447 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 62.117% | 62.117% | 0.630 s | 44.502 MB | 58.539 MB | 52.023 MB | 66.449 MB | n/a MB | n/a MB |
| python | 9050 |  | 10079 | 1.519% | 173.787% | 154.170 s | 2909.141 MB | 4226.051 MB | 15835.931 MB | 18544.914 MB | 3.511719 MB | 1936.417969 MB |
| vllm | 9056 |  | 10079 | 0.144% | 6.948% | 14.660 s | 1804.422 MB | 1804.793 MB | 11035.578 MB | 11044.496 MB | 0.000000 MB | 0.089844 MB |
| lsb_guard.sh | 9062 |  | 10079 | 0.001% | 0.995% | 0.090 s | 3.379 MB | 3.379 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 9096 |  | 10079 | 1.771% | 53.452% | 179.860 s | 2321.754 MB | 2322.043 MB | 21204.299 MB | 21204.438 MB | 0.000000 MB | 0.066406 MB |
| antigravity | 9464 | sandbox_agent_lsb-antigravity_0000_0000 | 10045 | 1.858% | 25.784% | 187.700 s | 271.884 MB | 314.465 MB | 2225.083 MB | 2273.207 MB | n/a MB | n/a MB |
| sleep | 9486 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9489 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9559 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 9567 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9568 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.574 MB | 21.574 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| python3 | 9580 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.188 MB | 20.188 MB | 212.074 MB | 212.074 MB | n/a MB | n/a MB |
| bash | 9576 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.691 MB | 2.691 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 9668 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9766 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9768 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 9770 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.250 MB | 20.250 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| sh | 9769 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.512 MB | 1.512 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 9781 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9783 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9785 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9883 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9885 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 9887 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.293 MB | 18.293 MB | 24.223 MB | 24.223 MB | n/a MB | n/a MB |
| sh | 9886 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 9903 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9905 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 9907 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10066 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10079 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10081 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10083 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10097 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10197 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10199 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10231 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10233 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10312 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10333 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10335 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10349 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10351 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10431 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10453 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10494 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 10496 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.840 MB | 20.840 MB | 25.840 MB | 25.840 MB | n/a MB | n/a MB |
| sh | 10495 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 10504 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 10525 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.316 MB | 19.316 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| sh | 10524 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 10532 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10555 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10671 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 10673 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.637 MB | 7.637 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sh | 10672 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10684 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.344 MB | 11.344 MB | 15.129 MB | 15.129 MB | n/a MB | n/a MB |
| sh | 10696 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10697 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.844 MB | 20.844 MB | 25.582 MB | 25.582 MB | n/a MB | n/a MB |
| sleep | 10703 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10705 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10707 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10731 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 10854 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.195 MB | 8.195 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 10853 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10876 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.426 MB | 20.426 MB | 25.195 MB | 25.195 MB | n/a MB | n/a MB |
| sh | 10875 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 10883 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10886 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10900 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10902 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 10922 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 10950 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 10951 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.332 MB | 15.332 MB | 20.398 MB | 20.398 MB | n/a MB | n/a MB |
| sleep | 10958 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 10983 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| sleep | 10990 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 10996 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| sleep | 10992 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11017 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.906 MB | 19.906 MB | 24.938 MB | 24.938 MB | n/a MB | n/a MB |
| sh | 11016 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11035 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11065 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11083 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11084 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.098 MB | 21.098 MB | 25.715 MB | 25.715 MB | n/a MB | n/a MB |
| sh | 11097 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11098 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.598 MB | 7.598 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| sleep | 11197 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11199 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11201 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11225 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11226 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.656 MB | 17.656 MB | 23.012 MB | 23.012 MB | n/a MB | n/a MB |
| sleep | 11261 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11273 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11294 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.188 MB | 20.188 MB | 24.945 MB | 24.945 MB | n/a MB | n/a MB |
| sh | 11293 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11306 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.477 MB | 7.477 MB | 11.930 MB | 11.930 MB | n/a MB | n/a MB |
| sleep | 11315 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11405 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| pgrep | 11409 |  | 1 | n/a% | n/a% | n/a s | 3.305 MB | 3.305 MB | 10.102 MB | 10.102 MB | n/a MB | n/a MB |
| sleep | 11410 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11418 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11421 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11443 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11448 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11468 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11469 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.750 MB | 16.750 MB | 22.141 MB | 22.141 MB | n/a MB | n/a MB |
| sleep | 11483 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11485 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11487 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11507 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11509 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11511 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11513 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11515 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11536 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11538 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11550 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11551 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.703 MB | 20.703 MB | 25.453 MB | 25.453 MB | n/a MB | n/a MB |
| sleep | 11559 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11561 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11589 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11613 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11614 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.715 MB | 14.715 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| python3 | 11616 | sandbox_agent_lsb-antigravity_0000_0000 | 14 | 177.200% | 180.432% | 23.200 s | 73.693 MB | 86.527 MB | 1959.075 MB | 1972.000 MB | n/a MB | n/a MB |
| sleep | 11622 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11630 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11631 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.551 MB | 18.551 MB | 24.223 MB | 24.223 MB | n/a MB | n/a MB |
| sleep | 11660 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 11667 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11668 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.195 MB | 16.195 MB | 21.848 MB | 21.848 MB | n/a MB | n/a MB |
| python3 | 11677 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.188 MB | 19.188 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| sh | 11676 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11703 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11714 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11719 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11747 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.363 MB | 21.363 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 11746 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11768 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11771 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.426 MB | 20.426 MB | 25.328 MB | 25.328 MB | n/a MB | n/a MB |
| sh | 11770 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 11791 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 11792 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.418 MB | 10.418 MB | 15.117 MB | 15.117 MB | n/a MB | n/a MB |
| sleep | 11803 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11809 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.184 MB | 9.184 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 11808 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11826 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11828 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11830 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11850 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11863 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11865 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11867 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11869 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 11896 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.207 MB | 9.207 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sh | 11895 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 11907 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11910 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11912 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 11916 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.668 MB | 2.668 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| sleep | 11926 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11928 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 11948 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12110 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12133 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.441 MB | 1.441 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12134 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.762 MB | 18.762 MB | 24.559 MB | 24.559 MB | n/a MB | n/a MB |
| sleep | 12172 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12185 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12187 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12222 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12225 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12241 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12243 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12245 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12269 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.379 MB | 1.379 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| sh | 12268 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.406 MB | 1.406 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12270 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12288 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| sh | 12287 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.609 MB | 1.609 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12297 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12299 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12300 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12301 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.289 MB | 10.289 MB | 15.062 MB | 15.062 MB | n/a MB | n/a MB |
| sh | 12310 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12311 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.664 MB | 20.664 MB | 25.582 MB | 25.582 MB | n/a MB | n/a MB |
| sleep | 12318 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12320 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12341 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.277 MB | 20.277 MB | 25.066 MB | 25.066 MB | n/a MB | n/a MB |
| sh | 12340 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12351 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.234 MB | 8.234 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| sh | 12350 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12361 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12364 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12372 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.637 MB | 18.637 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| sh | 12371 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12390 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.527 MB | 20.527 MB | 25.312 MB | 25.312 MB | n/a MB | n/a MB |
| sh | 12389 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12394 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.957 MB | 7.957 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 12393 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12392 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12404 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12405 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.496 MB | 21.496 MB | 27.055 MB | 27.055 MB | n/a MB | n/a MB |
| python3 | 12414 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 125.469% | 153.729% | 2.530 s | 899.029 MB | 1407.078 MB | 1105.846 MB | 1629.559 MB | n/a MB | n/a MB |
| bash | 12413 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.562 MB | 2.562 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 12419 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12430 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.605 MB | 21.605 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 12429 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12434 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 132.691% | 150.156% | 2.680 s | 966.268 MB | 1407.160 MB | 1178.772 MB | 1629.566 MB | n/a MB | n/a MB |
| bash | 12433 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.594 MB | 2.594 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 12465 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12485 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12487 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.047 MB | 10.047 MB | 13.844 MB | 13.844 MB | n/a MB | n/a MB |
| sh | 12486 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12495 | sandbox_agent_lsb-antigravity_0000_0000 | 7 | 157.270% | 181.870% | 9.500 s | 1339.890 MB | 1746.613 MB | 1556.805 MB | 1961.027 MB | n/a MB | n/a MB |
| sh | 12499 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.590 MB | 1.590 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12500 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.793 MB | 15.793 MB | 20.500 MB | 20.500 MB | n/a MB | n/a MB |
| sleep | 12506 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12511 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 12513 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12514 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12515 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.453 MB | 10.453 MB | 15.117 MB | 15.117 MB | n/a MB | n/a MB |
| sleep | 12538 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12570 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12571 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.941 MB | 14.941 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| sleep | 12585 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12588 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.148 MB | 19.148 MB | 24.801 MB | 24.801 MB | n/a MB | n/a MB |
| sh | 12587 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12595 | sandbox_agent_lsb-antigravity_0000_0000 | 37 | 169.269% | 184.380% | 61.410 s | 329.574 MB | 400.801 MB | 551.253 MB | 614.227 MB | n/a MB | n/a MB |
| sh | 12603 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12604 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 3.966% | 3.966% | 0.040 s | 10.615 MB | 14.258 MB | 15.873 MB | 20.086 MB | n/a MB | n/a MB |
| python3 | 12607 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.438 MB | 18.438 MB | 24.172 MB | 24.172 MB | n/a MB | n/a MB |
| sleep | 12609 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12606 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 12614 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12615 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.695 MB | 15.695 MB | 20.535 MB | 20.535 MB | n/a MB | n/a MB |
| sh | 12618 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12619 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.836 MB | 16.836 MB | 22.141 MB | 22.141 MB | n/a MB | n/a MB |
| bash | 12650 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 12651 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 99.748% | 100.394% | 5.020 s | 153.057 MB | 289.043 MB | 162.673 MB | 299.086 MB | n/a MB | n/a MB |
| sleep | 12654 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12662 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.883 MB | 15.883 MB | 20.535 MB | 20.535 MB | n/a MB | n/a MB |
| sh | 12661 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12692 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12697 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 99.946% | 100.344% | 5.030 s | 151.025 MB | 209.074 MB | 160.637 MB | 215.070 MB | n/a MB | n/a MB |
| bash | 12696 | sandbox_agent_lsb-antigravity_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.617 MB | 2.617 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| sleep | 12706 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12738 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12739 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.719 MB | 10.719 MB | 15.301 MB | 15.301 MB | n/a MB | n/a MB |
| antigravity | 12749 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 290.348 MB | 290.348 MB | 2271.289 MB | 2271.289 MB | n/a MB | n/a MB |
| sleep | 12762 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12784 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.191 MB | 9.191 MB | 13.297 MB | 13.297 MB | n/a MB | n/a MB |
| bash | 12783 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.617 MB | 2.617 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| sleep | 12806 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12807 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 12808 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.258 MB | 21.258 MB | 25.832 MB | 25.832 MB | n/a MB | n/a MB |
| sleep | 12837 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 12848 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.023 MB | 1.023 MB | 2.402 MB | 2.402 MB | n/a MB | n/a MB |
| sleep | 12868 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 12874 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.672 MB | 20.672 MB | 25.445 MB | 25.445 MB | n/a MB | n/a MB |
| sh | 12873 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 12892 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13070 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.574 MB | 21.574 MB | 26.988 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 13069 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13090 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.543 MB | 20.543 MB | 25.328 MB | 25.328 MB | n/a MB | n/a MB |
| sh | 13089 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.559 MB | 1.559 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 13097 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.590 MB | 1.590 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13098 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.711 MB | 14.711 MB | 20.086 MB | 20.086 MB | n/a MB | n/a MB |
| sleep | 13105 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 13114 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.289 MB | 1.289 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13115 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.945 MB | 8.945 MB | 13.551 MB | 13.551 MB | n/a MB | n/a MB |
| sleep | 13125 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 13132 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13133 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.750 MB | 7.750 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python3 | 13137 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.816 MB | 9.816 MB | 13.680 MB | 13.680 MB | n/a MB | n/a MB |
| sh | 13136 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.531 MB | 1.531 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 13145 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13153 | sandbox_agent_lsb-antigravity_0000_0000 | 15 | 168.493% | 180.888% | 23.780 s | 1385.139 MB | 1550.809 MB | 1639.400 MB | 1766.125 MB | n/a MB | n/a MB |
| sleep | 13165 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13171 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13275 | sandbox_agent_lsb-antigravity_0000_0000 | 41 | 171.220% | 184.850% | 69.060 s | 1444.660 MB | 1501.230 MB | 1677.366 MB | 1716.406 MB | n/a MB | n/a MB |
| sleep | 13286 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13288 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.980 MB | 17.980 MB | 23.172 MB | 23.172 MB | n/a MB | n/a MB |
| sh | 13287 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 13295 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.609 MB | 1.609 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13300 | sandbox_agent_lsb-antigravity_0000_0000 | 52 | 170.444% | 183.821% | 87.610 s | 1443.702 MB | 1575.227 MB | 1666.041 MB | 1790.137 MB | n/a MB | n/a MB |
| bash | 13299 | sandbox_agent_lsb-antigravity_0000_0000 | 52 | 0.000% | 0.000% | 0.000 s | 2.785 MB | 2.785 MB | 3.988 MB | 3.988 MB | n/a MB | n/a MB |
| sleep | 13309 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13313 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.609 MB | 1.609 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13319 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13443 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13449 | sandbox_agent_lsb-antigravity_0000_0000 | 72 | 171.681% | 184.927% | 122.840 s | 1519.442 MB | 1666.914 MB | 1742.059 MB | 1881.188 MB | n/a MB | n/a MB |
| bash | 13448 | sandbox_agent_lsb-antigravity_0000_0000 | 72 | 0.000% | 0.000% | 0.000 s | 2.781 MB | 2.781 MB | 3.996 MB | 3.996 MB | n/a MB | n/a MB |
| sleep | 13459 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13468 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13472 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 133.196% | 161.084% | 2.680 s | 755.969 MB | 1142.492 MB | 968.454 MB | 1364.031 MB | n/a MB | n/a MB |
| bash | 13471 | sandbox_agent_lsb-antigravity_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.715 MB | 3.855 MB | 3.855 MB | n/a MB | n/a MB |
| sleep | 13484 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13489 | sandbox_agent_lsb-antigravity_0000_0000 | 120 | 170.807% | 186.867% | 204.860 s | 429.749 MB | 464.367 MB | 652.359 MB | 679.262 MB | n/a MB | n/a MB |
| bash | 13488 | sandbox_agent_lsb-antigravity_0000_0000 | 120 | 0.000% | 0.000% | 0.000 s | 2.781 MB | 2.781 MB | 3.855 MB | 3.855 MB | n/a MB | n/a MB |
| sleep | 13494 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13601 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13612 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 13616 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.660 MB | 2.660 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 13617 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 126.991% | 126.991% | 1.280 s | 569.848 MB | 1111.730 MB | 780.953 MB | 1333.652 MB | n/a MB | n/a MB |
| sleep | 13628 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13634 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.602 MB | 13.602 MB | 207.324 MB | 207.324 MB | n/a MB | n/a MB |
| bash | 13633 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.969 MB | 2.969 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| sleep | 13645 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13647 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13746 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13748 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13750 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13752 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sh | 13755 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 13756 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.488 MB | 19.488 MB | 24.934 MB | 24.934 MB | n/a MB | n/a MB |
| python3 | 13761 | sandbox_agent_lsb-antigravity_0000_0000 | 177 | 170.856% | 181.346% | 302.990 s | 1446.538 MB | 1547.449 MB | 1676.329 MB | 1761.496 MB | n/a MB | n/a MB |
| sleep | 13771 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13867 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13872 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13882 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13884 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 13886 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 13910 | sandbox_agent_lsb-antigravity_0000_0000 | 2 | 163.935% | 163.935% | 1.650 s | 51.396 MB | 88.145 MB | 258.363 MB | 307.676 MB | n/a MB | n/a MB |
| sleep | 13926 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 14067 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 14080 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 14082 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.680 MB | 4.680 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| sh | 14081 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.523 MB | 1.523 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 14090 | sandbox_agent_lsb-antigravity_0000_0000 | 26 | 172.411% | 182.759% | 43.470 s | 1154.082 MB | 1754.789 MB | 1370.618 MB | 1970.320 MB | n/a MB | n/a MB |
| sleep | 14103 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 14109 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 14136 | sandbox_agent_lsb-antigravity_0000_0000 | 171 | 172.849% | 185.087% | 296.260 s | 1444.883 MB | 1547.531 MB | 1673.366 MB | 1761.496 MB | n/a MB | n/a MB |
| bash | 14135 | sandbox_agent_lsb-antigravity_0000_0000 | 197 | 0.000% | 0.000% | 0.000 s | 2.809 MB | 2.809 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| sleep | 14145 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 14227 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 14229 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 14230 | sandbox_agent_lsb-antigravity_0000_0000 | 26 | 173.942% | 180.158% | 43.800 s | 1116.803 MB | 1847.469 MB | 1343.717 MB | 2093.949 MB | n/a MB | n/a MB |
| sh | 14236 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.402 MB | 1.402 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 14237 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.965 MB | 15.965 MB | 20.602 MB | 20.602 MB | n/a MB | n/a MB |
| sleep | 14243 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 14245 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.703 MB | 7.703 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| sh | 14244 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.496 MB | 1.496 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 14256 |  | 42 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 14274 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.188 MB | 19.188 MB | 24.680 MB | 24.680 MB | n/a MB | n/a MB |
| sh | 14273 | sandbox_agent_lsb-antigravity_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.355 MB | 1.355 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| docker | 14283 |  | 1 | n/a% | n/a% | n/a s | 23.391 MB | 23.391 MB | 1698.438 MB | 1698.438 MB | n/a MB | n/a MB |
| docker | 14309 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.438 MB | 30.438 MB | 1843.512 MB | 1843.512 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.933% | 100.000% | 11902.302 MB | 13066.000 MB | 29.366 W | 74.046 W | 297784.396 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-antigravity_0000_0000 | 59.070% | 217.022% | 5987.077 s | 381.656 MB | 2140.531 MB | 24.609375 MB | 335.562500 MB | 0.452453 MB | 3.138368 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 9208 | 10140.745 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 10133.468 | n/a | n/a | 24.609 | 10133468.009 | 10133468.009 | 10133468.009 |
| engine:execute | 1/1 | 0 | 0 | 10133.467 | 8.006 | 10125.318 | 24.609 | 10133466.506 | 10133466.506 | 10133466.506 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 10106.472 | 0.021 | 10106.451 | 18.345 | 10106471.569 | 10106471.569 | 10106471.569 |
| llm:attempt | 130/130 | 0 | 0 | 9297.124 | 5.701 | 9291.362 | 3.415 | 71516.336 | 32061.753 | 228700.504 |
| tool:run_command | 74/74 | 0 | 0 | 817.467 | n/a | n/a | 11.688 | 11046.858 | 376.596 | 59888.245 |
| tool:mcp__agency__generate | 12/12 | 0 | 0 | 187.267 | n/a | n/a | 0.000 | 15605.607 | 13262.258 | 31447.267 |
| run:container_call | 13/13 | 0 | 0 | 22.985 | 0.002 | 22.983 | 0.000 | 1768.085 | 38.408 | 9036.955 |
| teardown:commit | 1/1 | 0 | 0 | 22.595 | 0.004 | 22.591 | 0.000 | 22595.063 | 22595.063 | 22595.063 |
| sandbox:commit | 1/1 | 0 | 0 | 22.403 | 0.003 | 22.400 | 0.000 | 22402.638 | 22402.638 | 22402.638 |
| checkpoint.total | 1/1 | 0 | 0 | 22.402 | 0.003 | 22.400 | 0.000 | 22402.475 | 22402.475 | 22402.475 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.402 | 0.002 | 22.400 | 0.000 | 22402.333 | 22402.333 | 22402.333 |
| tool:mcp__agency__trace | 7/7 | 0 | 0 | 18.989 | n/a | n/a | 0.000 | 2712.783 | 2107.342 | 5391.711 |
| tool:mcp__agency__token_stats | 1/1 | 0 | 0 | 16.280 | n/a | n/a | 0.000 | 16279.698 | 16279.698 | 16279.698 |
| tool:mcp__agency__logit_lens | 1/1 | 0 | 0 | 10.735 | n/a | n/a | 0.000 | 10734.899 | 10734.899 | 10734.899 |
| tool:read_file | 39/39 | 0 | 0 | 10.413 | n/a | n/a | 0.000 | 267.001 | 211.431 | 277.870 |
| tool:mcp__agency__patch | 10/10 | 0 | 0 | 5.508 | n/a | n/a | 0.000 | 550.791 | 541.226 | 607.367 |
| tool:write_file | 17/17 | 0 | 0 | 5.234 | n/a | n/a | 0.362 | 307.897 | 293.030 | 427.322 |
| syscall:connect | 1307/1307 | 0 | 0 | 4.317 | n/a | n/a | 0.221 | 3.303 | 2.403 | 5.635 |
| tool:mcp__agency__inspect_module_inputs | 2/2 | 0 | 0 | 4.235 | n/a | n/a | 0.000 | 2117.693 | 2117.693 | 2128.470 |
| tool:mcp__agency__attribution | 9/9 | 0 | 0 | 4.124 | n/a | n/a | 0.000 | 458.189 | 395.884 | 711.310 |
| tool:mcp__agency__inspect | 2/2 | 0 | 0 | 4.050 | n/a | n/a | 0.000 | 2025.119 | 2025.119 | 2092.634 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.649 | 0.841 | 2.807 | 6.239 | 3648.976 | 3648.976 | 3648.976 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.649 | 0.841 | 2.807 | 6.239 | 3648.716 | 3648.716 | 3648.716 |
| tool:edit_file | 8/8 | 0 | 0 | 2.702 | n/a | n/a | 0.003 | 337.730 | 326.036 | 409.296 |
| syscall:sendto | 740/740 | 0 | 0 | 1.674 | n/a | n/a | 0.081 | 2.263 | 2.046 | 3.975 |
| syscall:execve | 904/904 | 0 | 0 | 1.157 | n/a | n/a | 0.097 | 1.280 | 1.198 | 1.502 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.579 | n/a | n/a | 0.000 | 579.411 | 579.411 | 579.411 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.448 | n/a | n/a | 0.000 | 447.982 | 447.982 | 447.982 |
| tool:mcp__agency__attention | 1/1 | 0 | 0 | 0.371 | n/a | n/a | 0.000 | 370.981 | 370.981 | 370.981 |
| sandbox:create | 1/1 | 0 | 0 | 0.341 | 0.250 | 0.092 | 0.000 | 341.322 | 341.322 | 341.322 |
| sandbox:start | 1/1 | 0 | 0 | 0.323 | 0.002 | 0.320 | 0.000 | 322.657 | 322.657 | 322.657 |
| runtime.container_create | 1/1 | 0 | 0 | 0.323 | 0.002 | 0.320 | 0.000 | 322.528 | 322.528 | 322.528 |
| sandbox:stop | 1/1 | 0 | 0 | 0.192 | 0.001 | 0.191 | 0.000 | 192.167 | 192.167 | 192.167 |
| agency:services_close | 1/1 | 0 | 0 | 0.188 | 0.001 | 0.187 | 0.007 | 187.898 | 187.898 | 187.898 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.087 | 0.087 | 0.000 | 0.003 | 87.255 | 87.255 | 87.255 |
| agency:services_start | 1/1 | 0 | 0 | 0.071 | 0.040 | 0.031 | 0.000 | 71.166 | 71.166 | 71.166 |
| run:detect | 1/1 | 0 | 0 | 0.054 | 0.001 | 0.053 | 0.000 | 53.942 | 53.942 | 53.942 |
| agent:create | 1/1 | 0 | 0 | 0.036 | 0.007 | 0.029 | 0.000 | 36.301 | 36.301 | 36.301 |
| syscall:bind | 4/4 | 0 | 0 | 0.009 | n/a | n/a | 0.004 | 2.253 | 2.232 | 2.549 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.270 | 1.270 | 1.270 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.077 | 0.069 | 0.138 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.233 | 0.233 | 0.233 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.063 | 0.063 | 0.063 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 10078 | 0.126 | 0.013 | 48.113 | 0.083 | 12.810349 CPU seconds | n/a |
| GPU 0 memory | MB | 10079 | 11902.302 | 11670.000 | 13066.000 | 11934.000 | n/a | n/a |
| GPU 0 power | W | 10079 | 29.366 | 27.415 | 74.046 | 28.450 | n/a | 297784.396 J |
| GPU 0 proc / 9050-660338 / sandbox / ~ / device / GPU-5899ea26-8fb1-67fd-772e-291218e57ba9 memory | MB | 10079 | 3224.215 | 3118.000 | 4386.000 | 3234.000 | n/a | n/a |
| GPU 0 proc / 9050-660338 / sandbox / ~ / device / GPU-5899ea26-8fb1-67fd-772e-291218e57ba9 estimated power | W | 5599 | 0.454 | 0.000 | 61.958 | 0.000 | n/a | n/a |
| GPU 0 proc / 9050-660338 / sandbox / ~ / device / GPU-5899ea26-8fb1-67fd-772e-291218e57ba9 utilization | percent | 5599 | 0.275 | 0.000 | 66.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 9096-662267 / sandbox / ~ / device / GPU-5899ea26-8fb1-67fd-772e-291218e57ba9 memory | MB | 10079 | 8196.087 | 8070.000 | 8218.000 | 8218.000 | n/a | n/a |
| GPU 0 proc / 9096-662267 / sandbox / ~ / device / GPU-5899ea26-8fb1-67fd-772e-291218e57ba9 estimated power | W | 4318 | 2.931 | 0.000 | 72.946 | 0.000 | n/a | n/a |
| GPU 0 proc / 9096-662267 / sandbox / ~ / device / GPU-5899ea26-8fb1-67fd-772e-291218e57ba9 utilization | percent | 4318 | 4.034 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 10079 | 11420.302 | 11188.000 | 12584.000 | 11452.000 | n/a | n/a |
| GPU 0 utilization | percent | 10079 | 1.933 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 10079 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 10078 | 4.966 | 0.062 | 76.865 | 0.217 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 10078 | 15.512 | 0.250 | 62.411 | 0.250 | n/a | n/a |
| host disk_read_mb_s | MB/s | 10078 | 0.166 | 0.000 | 213.764 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 10078 | 0.244 | 0.000 | 249.090 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 10078 | 0.097 | 0.000 | 59.764 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 10078 | 0.099 | 0.000 | 60.690 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 10079 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 10079 | 7195.144 | 6365.301 | 9502.039 | 7634.930 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 10078 | 0.002 | 0.000 | 14.513 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 10078 | 0.002 | 0.000 | 14.535 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 10078 | 0.000 | 0.000 | 0.056 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 10078 | 0.005 | 0.000 | 0.852 | 0.000 | n/a | n/a |
| sleep (PID 10066) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10066) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10066) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10066) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10066) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10066) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10079) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10079) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10079) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10079) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10079) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10079) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10081) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10081) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10081) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10081) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10081) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10081) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10083) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10083) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10083) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10083) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10083) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10083) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10097) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10097) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10097) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10097) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10097) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10097) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10197) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10197) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10197) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10197) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10197) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10197) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10199) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10199) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10199) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10199) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10199) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10199) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10231) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10231) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10231) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10231) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10231) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10231) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10233) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10233) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10233) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10233) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10233) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10233) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10312) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10312) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10312) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10312) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10312) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10312) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10333) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10333) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10333) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10333) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10333) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10333) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10335) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10335) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10335) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10335) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10335) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10335) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10349) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10349) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10349) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10349) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10349) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10349) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10351) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10351) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10351) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10351) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10351) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10351) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10431) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10431) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10431) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10431) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10431) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10431) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10453) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10453) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10453) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10453) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10453) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10453) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10494) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10494) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10494) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10494) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10494) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10494) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10495) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10495) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10496) rss_mb | MB | 1 | 20.840 | 20.840 | 20.840 | 20.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10496) vms_mb | MB | 1 | 25.840 | 25.840 | 25.840 | 25.840 | n/a | n/a |
| sleep (PID 10504) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10504) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10504) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10504) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 10504) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10504) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10524) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10524) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10525) rss_mb | MB | 1 | 19.316 | 19.316 | 19.316 | 19.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10525) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sleep (PID 10532) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10532) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10532) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10532) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10532) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10532) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10555) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10555) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10555) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10555) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10555) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10555) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10671) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10671) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10671) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10671) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10671) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10671) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10672) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10672) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10673) rss_mb | MB | 1 | 7.637 | 7.637 | 7.637 | 7.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10673) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 10684) rss_mb | MB | 1 | 11.344 | 11.344 | 11.344 | 11.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 10684) vms_mb | MB | 1 | 15.129 | 15.129 | 15.129 | 15.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10696) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10696) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10697) rss_mb | MB | 1 | 20.844 | 20.844 | 20.844 | 20.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10697) vms_mb | MB | 1 | 25.582 | 25.582 | 25.582 | 25.582 | n/a | n/a |
| sleep (PID 10703) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10703) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10703) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10703) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10703) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10703) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10705) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10705) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10705) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10705) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10705) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10705) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10707) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10707) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10707) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10707) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10707) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10707) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10731) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10731) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10731) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10731) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10731) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10731) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10853) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10853) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10854) rss_mb | MB | 1 | 8.195 | 8.195 | 8.195 | 8.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10854) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10875) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10875) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10876) rss_mb | MB | 1 | 20.426 | 20.426 | 20.426 | 20.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10876) vms_mb | MB | 1 | 25.195 | 25.195 | 25.195 | 25.195 | n/a | n/a |
| sleep (PID 10883) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10883) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10883) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10883) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10883) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10883) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10886) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10886) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10886) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10886) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10886) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10886) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10900) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10900) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10900) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10900) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10900) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10900) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10902) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10902) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10902) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10902) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10902) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10902) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10922) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10922) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10922) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10922) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10922) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10922) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10950) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10950) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10951) rss_mb | MB | 1 | 15.332 | 15.332 | 15.332 | 15.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 10951) vms_mb | MB | 1 | 20.398 | 20.398 | 20.398 | 20.398 | n/a | n/a |
| sleep (PID 10958) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10958) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10958) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10958) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10958) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10958) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10983) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 10983) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sleep (PID 10990) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10990) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10990) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10990) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10990) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10990) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 10992) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 10992) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10992) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 10992) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 10992) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 10992) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 10996) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 10996) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11016) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11016) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11017) rss_mb | MB | 1 | 19.906 | 19.906 | 19.906 | 19.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11017) vms_mb | MB | 1 | 24.938 | 24.938 | 24.938 | 24.938 | n/a | n/a |
| sleep (PID 11035) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11035) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11035) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11035) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11035) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11035) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11065) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11065) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11065) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11065) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11065) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11065) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11083) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11083) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11084) rss_mb | MB | 1 | 21.098 | 21.098 | 21.098 | 21.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11084) vms_mb | MB | 1 | 25.715 | 25.715 | 25.715 | 25.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11097) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11097) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11098) rss_mb | MB | 1 | 7.598 | 7.598 | 7.598 | 7.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11098) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sleep (PID 11197) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11197) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11197) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11197) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11197) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11197) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11199) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11199) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11199) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11199) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11199) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11199) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11201) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11201) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11201) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11201) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11201) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11201) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11225) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11225) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11226) rss_mb | MB | 1 | 17.656 | 17.656 | 17.656 | 17.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11226) vms_mb | MB | 1 | 23.012 | 23.012 | 23.012 | 23.012 | n/a | n/a |
| sleep (PID 11261) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11261) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11261) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11261) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11261) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11261) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11273) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11273) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11273) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11273) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11273) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11273) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11293) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11293) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11294) rss_mb | MB | 1 | 20.188 | 20.188 | 20.188 | 20.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11294) vms_mb | MB | 1 | 24.945 | 24.945 | 24.945 | 24.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11306) rss_mb | MB | 1 | 7.477 | 7.477 | 7.477 | 7.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 11306) vms_mb | MB | 1 | 11.930 | 11.930 | 11.930 | 11.930 | n/a | n/a |
| sleep (PID 11315) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11315) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11315) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11315) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11315) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11315) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11405) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11405) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11405) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11405) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11405) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11405) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| pgrep (PID 11409) rss_mb | MB | 1 | 3.305 | 3.305 | 3.305 | 3.305 | n/a | n/a |
| pgrep (PID 11409) vms_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sleep (PID 11410) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11410) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11410) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11410) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11410) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11410) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11418) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11418) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11418) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11418) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11418) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11418) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11421) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11421) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11421) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11421) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11421) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11421) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11443) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11443) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11443) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11443) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11443) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11443) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11448) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11448) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11448) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11448) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11448) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11448) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11468) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11468) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11469) rss_mb | MB | 1 | 16.750 | 16.750 | 16.750 | 16.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11469) vms_mb | MB | 1 | 22.141 | 22.141 | 22.141 | 22.141 | n/a | n/a |
| sleep (PID 11483) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11483) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11483) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11483) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11483) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11483) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11485) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11485) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11485) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11485) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11485) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11485) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11487) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11487) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11487) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11487) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11487) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11487) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11507) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11507) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11507) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11507) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11507) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11507) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11509) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11509) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11509) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11509) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11509) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11509) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11511) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11511) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11511) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11511) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11511) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11511) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11513) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11513) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11513) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11513) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11513) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11513) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11515) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11515) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11515) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11515) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11515) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11515) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11536) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11536) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11536) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11536) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 11536) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11536) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11538) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11538) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11538) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11538) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11538) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11538) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11550) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11550) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11551) rss_mb | MB | 1 | 20.703 | 20.703 | 20.703 | 20.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11551) vms_mb | MB | 1 | 25.453 | 25.453 | 25.453 | 25.453 | n/a | n/a |
| sleep (PID 11559) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11559) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11559) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11559) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11559) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11559) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11561) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11561) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11561) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11561) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11561) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11561) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11589) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11589) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11589) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11589) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 11589) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11589) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11613) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11613) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11614) rss_mb | MB | 1 | 14.715 | 14.715 | 14.715 | 14.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11614) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_weights_and_setup.py (PID 11616) CPU | percent | 13 | 177.200 | 171.058 | 180.432 | 180.161 | 23.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_weights_and_setup.py (PID 11616) rss_mb | MB | 14 | 73.693 | 58.703 | 86.527 | 58.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_weights_and_setup.py (PID 11616) main thread run-queue wait | percent | 13 | 63.442 | 49.831 | 74.496 | 72.495 | 8.306509 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — inspect_weights_and_setup.py (PID 11616) vms_mb | MB | 14 | 1959.075 | 1944.000 | 1972.000 | 1944.000 | n/a | n/a |
| sleep (PID 11622) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11622) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11622) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11622) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11622) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11622) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11630) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11630) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11631) rss_mb | MB | 1 | 18.551 | 18.551 | 18.551 | 18.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11631) vms_mb | MB | 1 | 24.223 | 24.223 | 24.223 | 24.223 | n/a | n/a |
| sleep (PID 11660) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11660) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11660) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11660) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11660) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11660) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11667) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11667) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11668) rss_mb | MB | 1 | 16.195 | 16.195 | 16.195 | 16.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11668) vms_mb | MB | 1 | 21.848 | 21.848 | 21.848 | 21.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11676) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11676) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11677) rss_mb | MB | 1 | 19.188 | 19.188 | 19.188 | 19.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11677) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sleep (PID 11703) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11703) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11703) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11703) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11703) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11703) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11714) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11714) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11714) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11714) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11714) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11714) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11719) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11719) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11719) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11719) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11719) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11719) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11746) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11746) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11747) rss_mb | MB | 1 | 21.363 | 21.363 | 21.363 | 21.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11747) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sleep (PID 11768) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11768) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11768) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11768) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11768) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11768) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11770) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11770) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11771) rss_mb | MB | 1 | 20.426 | 20.426 | 20.426 | 20.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11771) vms_mb | MB | 1 | 25.328 | 25.328 | 25.328 | 25.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11791) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11791) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11792) rss_mb | MB | 1 | 10.418 | 10.418 | 10.418 | 10.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11792) vms_mb | MB | 1 | 15.117 | 15.117 | 15.117 | 15.117 | n/a | n/a |
| sleep (PID 11803) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11803) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11803) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11803) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11803) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11803) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11808) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11808) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11809) rss_mb | MB | 1 | 9.184 | 9.184 | 9.184 | 9.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11809) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sleep (PID 11826) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11826) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11826) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11826) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11826) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11826) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11828) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11828) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11828) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11828) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11828) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11828) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11830) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11830) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11830) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11830) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11830) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11830) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11850) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11850) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11850) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11850) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11850) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11850) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11863) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11863) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11863) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11863) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11863) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11863) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11865) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11865) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11865) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11865) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11865) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11865) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11867) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11867) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11867) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11867) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11867) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11867) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11869) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11869) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11869) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11869) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11869) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11869) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11895) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 11895) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11896) rss_mb | MB | 1 | 9.207 | 9.207 | 9.207 | 9.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 11896) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sleep (PID 11907) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11907) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11907) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11907) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11907) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11907) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11910) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11910) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11910) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11910) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11910) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11910) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11912) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11912) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11912) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11912) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11912) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11912) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 11916) rss_mb | MB | 1 | 2.668 | 2.668 | 2.668 | 2.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 11916) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sleep (PID 11926) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11926) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11926) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11926) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11926) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11926) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11928) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11928) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11928) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11928) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11928) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11928) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 11948) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 11948) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11948) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 11948) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 11948) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 11948) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12110) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12110) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12110) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12110) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12110) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12110) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12133) rss_mb | MB | 1 | 1.441 | 1.441 | 1.441 | 1.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12133) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12134) rss_mb | MB | 1 | 18.762 | 18.762 | 18.762 | 18.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12134) vms_mb | MB | 1 | 24.559 | 24.559 | 24.559 | 24.559 | n/a | n/a |
| sleep (PID 12172) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12172) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12172) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12172) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12172) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12172) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12185) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12185) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12185) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12185) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12185) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12185) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12187) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12187) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12187) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12187) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12187) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12187) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12222) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12222) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12222) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12222) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12222) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12222) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12225) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12225) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12225) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12225) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12225) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12225) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12241) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12241) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12241) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12241) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12241) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12241) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12243) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12243) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12243) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12243) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 12243) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12243) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12245) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12245) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12245) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12245) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12245) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12245) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12268) rss_mb | MB | 1 | 1.406 | 1.406 | 1.406 | 1.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12268) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12269) rss_mb | MB | 1 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12269) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sleep (PID 12270) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12270) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12270) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12270) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12270) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12270) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12287) rss_mb | MB | 1 | 1.609 | 1.609 | 1.609 | 1.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12287) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python3 (PID 12288) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python3 (PID 12288) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sleep (PID 12297) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12297) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12297) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12297) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12297) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12297) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12299) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12299) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12299) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12299) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12299) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12299) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12300) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12300) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12301) rss_mb | MB | 1 | 10.289 | 10.289 | 10.289 | 10.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12301) vms_mb | MB | 1 | 15.062 | 15.062 | 15.062 | 15.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12310) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12310) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12311) rss_mb | MB | 1 | 20.664 | 20.664 | 20.664 | 20.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12311) vms_mb | MB | 1 | 25.582 | 25.582 | 25.582 | 25.582 | n/a | n/a |
| sleep (PID 12318) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12318) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12318) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12318) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12318) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12318) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12320) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12320) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12320) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12320) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12320) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12320) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12340) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12340) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12341) rss_mb | MB | 1 | 20.277 | 20.277 | 20.277 | 20.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12341) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12350) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12350) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12351) rss_mb | MB | 1 | 8.234 | 8.234 | 8.234 | 8.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12351) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sleep (PID 12361) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12361) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12361) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12361) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12361) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12361) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12364) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12364) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12364) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12364) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12364) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12364) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12371) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12371) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12372) rss_mb | MB | 1 | 18.637 | 18.637 | 18.637 | 18.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12372) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12389) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12389) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12390) rss_mb | MB | 1 | 20.527 | 20.527 | 20.527 | 20.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12390) vms_mb | MB | 1 | 25.312 | 25.312 | 25.312 | 25.312 | n/a | n/a |
| sleep (PID 12392) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12392) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12392) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12392) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12392) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12392) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12393) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12393) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12394) rss_mb | MB | 1 | 7.957 | 7.957 | 7.957 | 7.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12394) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12404) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12404) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12405) rss_mb | MB | 1 | 21.496 | 21.496 | 21.496 | 21.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12405) vms_mb | MB | 1 | 27.055 | 27.055 | 27.055 | 27.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12413) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12413) rss_mb | MB | 3 | 2.562 | 2.562 | 2.562 | 2.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12413) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12413) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_traces.py (PID 12414) CPU | percent | 2 | 125.469 | 97.209 | 153.729 | 153.729 | 2.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_traces.py (PID 12414) rss_mb | MB | 3 | 899.029 | 23.703 | 1407.078 | 1407.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_traces.py (PID 12414) main thread run-queue wait | percent | 2 | 16.299 | 0.078 | 32.520 | 32.520 | 0.328678 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_traces.py (PID 12414) vms_mb | MB | 3 | 1105.846 | 215.895 | 1629.559 | 1629.559 | n/a | n/a |
| sleep (PID 12419) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12419) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12419) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12419) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12419) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12419) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12429) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12429) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12430) rss_mb | MB | 1 | 21.605 | 21.605 | 21.605 | 21.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12430) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12433) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12433) rss_mb | MB | 3 | 2.594 | 2.594 | 2.594 | 2.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12433) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12433) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_traces.py (PID 12434) CPU | percent | 2 | 132.691 | 115.226 | 150.156 | 150.156 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_traces.py (PID 12434) rss_mb | MB | 3 | 966.268 | 84.895 | 1407.160 | 1407.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_traces.py (PID 12434) main thread run-queue wait | percent | 2 | 17.912 | 9.895 | 25.930 | 25.930 | 0.362091 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_traces.py (PID 12434) vms_mb | MB | 3 | 1178.772 | 277.184 | 1629.566 | 1629.566 | n/a | n/a |
| sleep (PID 12465) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12465) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12465) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12465) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12465) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12465) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12485) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12485) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12485) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12485) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12485) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12485) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12486) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12486) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12487) rss_mb | MB | 1 | 10.047 | 10.047 | 10.047 | 10.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12487) vms_mb | MB | 1 | 13.844 | 13.844 | 13.844 | 13.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_per_item_heads_and_general.py (PID 12495) CPU | percent | 6 | 157.270 | 96.441 | 181.870 | 175.923 | 9.500000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_per_item_heads_and_general.py (PID 12495) rss_mb | MB | 7 | 1339.890 | 14.547 | 1746.613 | 1717.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_per_item_heads_and_general.py (PID 12495) main thread run-queue wait | percent | 6 | 40.379 | 4.405 | 58.614 | 45.969 | 2.439803 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_per_item_heads_and_general.py (PID 12495) vms_mb | MB | 7 | 1556.805 | 208.859 | 1961.027 | 1931.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12499) rss_mb | MB | 1 | 1.590 | 1.590 | 1.590 | 1.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12499) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12500) rss_mb | MB | 1 | 15.793 | 15.793 | 15.793 | 15.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12500) vms_mb | MB | 1 | 20.500 | 20.500 | 20.500 | 20.500 | n/a | n/a |
| sleep (PID 12506) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12506) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12506) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12506) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12506) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12506) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12511) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12511) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12511) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12511) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12511) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12511) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 12513) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12513) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12513) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12513) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12513) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12513) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12514) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12514) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12515) rss_mb | MB | 1 | 10.453 | 10.453 | 10.453 | 10.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12515) vms_mb | MB | 1 | 15.117 | 15.117 | 15.117 | 15.117 | n/a | n/a |
| sleep (PID 12538) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12538) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12538) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12538) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12538) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12538) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12570) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12570) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12571) rss_mb | MB | 1 | 14.941 | 14.941 | 14.941 | 14.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12571) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sleep (PID 12585) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12585) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12585) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12585) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12585) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12585) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12587) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12587) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12588) rss_mb | MB | 1 | 19.148 | 19.148 | 19.148 | 19.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12588) vms_mb | MB | 1 | 24.801 | 24.801 | 24.801 | 24.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_def_pairs_and_l21.py (PID 12595) CPU | percent | 36 | 169.269 | 143.484 | 184.380 | 174.022 | 61.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_def_pairs_and_l21.py (PID 12595) rss_mb | MB | 37 | 329.574 | 20.742 | 400.801 | 400.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_def_pairs_and_l21.py (PID 12595) main thread run-queue wait | percent | 36 | 44.891 | 35.975 | 58.733 | 41.426 | 16.286878 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_def_pairs_and_l21.py (PID 12595) vms_mb | MB | 37 | 551.253 | 212.402 | 614.227 | 614.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12603) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12603) rss_mb | MB | 2 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12603) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12603) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12604) CPU | percent | 1 | 3.966 | 3.966 | 3.966 | 3.966 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12604) rss_mb | MB | 2 | 10.615 | 6.973 | 14.258 | 14.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12604) main thread run-queue wait | percent | 1 | 45.977 | 45.977 | 45.977 | 45.977 | 0.463718 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12604) vms_mb | MB | 2 | 15.873 | 11.660 | 20.086 | 20.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12606) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12606) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12607) rss_mb | MB | 1 | 18.438 | 18.438 | 18.438 | 18.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12607) vms_mb | MB | 1 | 24.172 | 24.172 | 24.172 | 24.172 | n/a | n/a |
| sleep (PID 12609) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12609) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12609) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12609) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12609) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12609) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12614) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12614) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12615) rss_mb | MB | 1 | 15.695 | 15.695 | 15.695 | 15.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12615) vms_mb | MB | 1 | 20.535 | 20.535 | 20.535 | 20.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12618) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12618) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12619) rss_mb | MB | 1 | 16.836 | 16.836 | 16.836 | 16.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12619) vms_mb | MB | 1 | 22.141 | 22.141 | 22.141 | 22.141 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12650) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12650) rss_mb | MB | 6 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12650) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12650) vms_mb | MB | 6 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12651) CPU | percent | 5 | 99.748 | 98.338 | 100.394 | 98.338 | 5.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12651) rss_mb | MB | 6 | 153.057 | 66.480 | 289.043 | 289.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12651) main thread run-queue wait | percent | 5 | 0.244 | 0.002 | 1.157 | 1.157 | 0.012276 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12651) vms_mb | MB | 6 | 162.673 | 72.480 | 299.086 | 299.086 | n/a | n/a |
| sleep (PID 12654) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12654) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12654) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12654) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12654) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12654) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12661) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12661) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12662) rss_mb | MB | 1 | 15.883 | 15.883 | 15.883 | 15.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12662) vms_mb | MB | 1 | 20.535 | 20.535 | 20.535 | 20.535 | n/a | n/a |
| sleep (PID 12692) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12692) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12692) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12692) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12692) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12692) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12696) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12696) rss_mb | MB | 6 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12696) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12696) vms_mb | MB | 6 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12697) CPU | percent | 5 | 99.946 | 99.291 | 100.344 | 99.291 | 5.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12697) rss_mb | MB | 6 | 151.025 | 68.156 | 209.074 | 204.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12697) main thread run-queue wait | percent | 5 | 0.003 | 0.001 | 0.005 | 0.004 | 0.000162 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12697) vms_mb | MB | 6 | 160.637 | 72.465 | 215.070 | 215.070 | n/a | n/a |
| sleep (PID 12706) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12706) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12706) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12706) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12706) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12706) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12738) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12738) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12739) rss_mb | MB | 1 | 10.719 | 10.719 | 10.719 | 10.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12739) vms_mb | MB | 1 | 15.301 | 15.301 | 15.301 | 15.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 12749) rss_mb | MB | 1 | 290.348 | 290.348 | 290.348 | 290.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 12749) vms_mb | MB | 1 | 2271.289 | 2271.289 | 2271.289 | 2271.289 | n/a | n/a |
| sleep (PID 12762) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12762) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12762) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12762) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12762) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12762) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12783) rss_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 12783) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12784) rss_mb | MB | 1 | 9.191 | 9.191 | 9.191 | 9.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 12784) vms_mb | MB | 1 | 13.297 | 13.297 | 13.297 | 13.297 | n/a | n/a |
| sleep (PID 12806) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12806) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12806) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12806) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12806) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12806) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12807) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12807) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12808) rss_mb | MB | 1 | 21.258 | 21.258 | 21.258 | 21.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12808) vms_mb | MB | 1 | 25.832 | 25.832 | 25.832 | 25.832 | n/a | n/a |
| sleep (PID 12837) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12837) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12837) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12837) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12837) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12837) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12848) rss_mb | MB | 1 | 1.023 | 1.023 | 1.023 | 1.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12848) vms_mb | MB | 1 | 2.402 | 2.402 | 2.402 | 2.402 | n/a | n/a |
| sleep (PID 12868) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12868) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12868) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12868) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12868) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12868) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12873) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 12873) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12874) rss_mb | MB | 1 | 20.672 | 20.672 | 20.672 | 20.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 12874) vms_mb | MB | 1 | 25.445 | 25.445 | 25.445 | 25.445 | n/a | n/a |
| sleep (PID 12892) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 12892) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12892) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 12892) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 12892) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 12892) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13069) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13069) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13070) rss_mb | MB | 1 | 21.574 | 21.574 | 21.574 | 21.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13070) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13089) rss_mb | MB | 1 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13089) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13090) rss_mb | MB | 1 | 20.543 | 20.543 | 20.543 | 20.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13090) vms_mb | MB | 1 | 25.328 | 25.328 | 25.328 | 25.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13097) rss_mb | MB | 1 | 1.590 | 1.590 | 1.590 | 1.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13097) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13098) rss_mb | MB | 1 | 14.711 | 14.711 | 14.711 | 14.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13098) vms_mb | MB | 1 | 20.086 | 20.086 | 20.086 | 20.086 | n/a | n/a |
| sleep (PID 13105) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13105) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13105) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13105) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13105) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13105) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13114) rss_mb | MB | 1 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13114) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13115) rss_mb | MB | 1 | 8.945 | 8.945 | 8.945 | 8.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13115) vms_mb | MB | 1 | 13.551 | 13.551 | 13.551 | 13.551 | n/a | n/a |
| sleep (PID 13125) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13125) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13125) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13125) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13125) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13125) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13132) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13132) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13133) rss_mb | MB | 1 | 7.750 | 7.750 | 7.750 | 7.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13133) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13136) rss_mb | MB | 1 | 1.531 | 1.531 | 1.531 | 1.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13136) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13137) rss_mb | MB | 1 | 9.816 | 9.816 | 9.816 | 9.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13137) vms_mb | MB | 1 | 13.680 | 13.680 | 13.680 | 13.680 | n/a | n/a |
| sleep (PID 13145) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13145) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13145) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13145) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13145) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13145) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_new_controls.py (PID 13153) CPU | percent | 14 | 168.493 | 134.899 | 180.888 | 170.624 | 23.780000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_new_controls.py (PID 13153) rss_mb | MB | 15 | 1385.139 | 121.438 | 1550.809 | 1323.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_new_controls.py (PID 13153) main thread run-queue wait | percent | 14 | 43.862 | 28.147 | 60.518 | 60.518 | 6.189918 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — analyze_new_controls.py (PID 13153) vms_mb | MB | 15 | 1639.400 | 785.262 | 1766.125 | 1538.273 | n/a | n/a |
| sleep (PID 13165) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13165) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13165) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13165) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13165) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13165) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13171) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13171) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13171) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13171) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13171) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13171) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_all_components_with_546_body.py (PID 13275) CPU | percent | 40 | 171.220 | 140.037 | 184.850 | 171.349 | 69.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_all_components_with_546_body.py (PID 13275) rss_mb | MB | 41 | 1444.660 | 237.875 | 1501.230 | 1325.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_all_components_with_546_body.py (PID 13275) main thread run-queue wait | percent | 40 | 44.951 | 22.702 | 71.336 | 68.072 | 18.130945 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — check_all_components_with_546_body.py (PID 13275) vms_mb | MB | 41 | 1677.366 | 785.395 | 1716.406 | 1540.008 | n/a | n/a |
| sleep (PID 13286) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13286) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13286) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13286) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13286) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13286) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13287) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13287) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13288) rss_mb | MB | 1 | 17.980 | 17.980 | 17.980 | 17.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13288) vms_mb | MB | 1 | 23.172 | 23.172 | 23.172 | 23.172 | n/a | n/a |
| sleep (PID 13295) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13295) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13295) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13295) rss_mb | MB | 59 | 1.609 | 1.609 | 1.609 | 1.609 | n/a | n/a |
| sleep (PID 13295) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13295) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13299) CPU | percent | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13299) rss_mb | MB | 52 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13299) main thread run-queue wait | percent | 51 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13299) vms_mb | MB | 52 | 3.988 | 3.988 | 3.988 | 3.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13300) CPU | percent | 51 | 170.444 | 136.936 | 183.821 | 169.369 | 87.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13300) rss_mb | MB | 52 | 1443.702 | 57.844 | 1575.227 | 1499.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13300) main thread run-queue wait | percent | 51 | 45.174 | 19.323 | 65.358 | 41.868 | 23.221143 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13300) vms_mb | MB | 52 | 1666.041 | 249.414 | 1790.137 | 1714.523 | n/a | n/a |
| sleep (PID 13309) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13309) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13309) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13309) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 13309) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13309) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13313) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13313) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13313) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13313) rss_mb | MB | 60 | 1.609 | 1.609 | 1.609 | 1.609 | n/a | n/a |
| sleep (PID 13313) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13313) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13319) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13319) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13319) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13319) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13319) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13319) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13443) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13443) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13443) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13443) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 13443) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13443) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13448) CPU | percent | 71 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13448) rss_mb | MB | 72 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13448) main thread run-queue wait | percent | 71 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13448) vms_mb | MB | 72 | 3.996 | 3.996 | 3.996 | 3.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13449) CPU | percent | 71 | 171.681 | 123.221 | 184.927 | 169.959 | 122.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13449) rss_mb | MB | 72 | 1519.442 | 24.582 | 1666.914 | 1666.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13449) main thread run-queue wait | percent | 71 | 44.878 | 11.512 | 61.844 | 50.264 | 32.109451 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13449) vms_mb | MB | 72 | 1742.059 | 216.316 | 1881.188 | 1881.188 | n/a | n/a |
| sleep (PID 13459) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13459) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13459) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13459) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13459) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13459) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13468) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13468) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13468) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13468) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13468) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13468) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13471) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13471) rss_mb | MB | 3 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13471) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13471) vms_mb | MB | 3 | 3.855 | 3.855 | 3.855 | 3.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13472) CPU | percent | 2 | 133.196 | 105.307 | 161.084 | 161.084 | 2.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13472) rss_mb | MB | 3 | 755.969 | 13.867 | 1142.492 | 1142.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13472) main thread run-queue wait | percent | 2 | 34.802 | 9.516 | 60.088 | 60.088 | 0.700086 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13472) vms_mb | MB | 3 | 968.454 | 207.617 | 1364.031 | 1364.031 | n/a | n/a |
| sleep (PID 13484) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13484) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13484) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13484) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13484) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13484) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13488) CPU | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13488) rss_mb | MB | 120 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13488) main thread run-queue wait | percent | 119 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13488) vms_mb | MB | 120 | 3.855 | 3.855 | 3.855 | 3.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13489) CPU | percent | 119 | 170.807 | 154.884 | 186.867 | 168.998 | 204.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13489) rss_mb | MB | 120 | 429.749 | 81.711 | 464.367 | 464.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13489) main thread run-queue wait | percent | 119 | 44.587 | 39.459 | 65.229 | 40.066 | 53.476285 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13489) vms_mb | MB | 120 | 652.359 | 278.855 | 679.262 | 679.262 | n/a | n/a |
| sleep (PID 13494) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13494) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13494) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13494) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13494) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13494) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13601) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13601) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13601) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13601) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13601) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13601) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13612) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13612) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13612) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13612) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13612) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13612) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13616) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13616) rss_mb | MB | 2 | 2.660 | 2.660 | 2.660 | 2.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13616) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13616) vms_mb | MB | 2 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13617) CPU | percent | 1 | 126.991 | 126.991 | 126.991 | 126.991 | 1.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13617) rss_mb | MB | 2 | 569.848 | 27.965 | 1111.730 | 1111.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13617) main thread run-queue wait | percent | 1 | 13.894 | 13.894 | 13.894 | 13.894 | 0.140047 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13617) vms_mb | MB | 2 | 780.953 | 228.254 | 1333.652 | 1333.652 | n/a | n/a |
| sleep (PID 13628) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13628) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13628) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13628) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 13628) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13628) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13633) rss_mb | MB | 1 | 2.969 | 2.969 | 2.969 | 2.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 13633) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13634) rss_mb | MB | 1 | 13.602 | 13.602 | 13.602 | 13.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python stdin (PID 13634) vms_mb | MB | 1 | 207.324 | 207.324 | 207.324 | 207.324 | n/a | n/a |
| sleep (PID 13645) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13645) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13645) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13645) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13645) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13645) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13647) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13647) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13647) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13647) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13647) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13647) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13746) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13746) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13746) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13746) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13746) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13746) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13748) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13748) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13748) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13748) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13748) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13748) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13750) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13750) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13750) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13750) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13750) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13750) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13752) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13752) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13752) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13752) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13752) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13752) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13755) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 13755) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13756) rss_mb | MB | 1 | 19.488 | 19.488 | 19.488 | 19.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 13756) vms_mb | MB | 1 | 24.934 | 24.934 | 24.934 | 24.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 13761) CPU | percent | 176 | 170.856 | 119.932 | 181.346 | 176.987 | 302.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 13761) rss_mb | MB | 177 | 1446.538 | 60.785 | 1547.449 | 1347.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 13761) main thread run-queue wait | percent | 176 | 46.118 | 9.888 | 72.186 | 72.186 | 81.781586 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 13761) vms_mb | MB | 177 | 1676.329 | 253.680 | 1761.496 | 1593.918 | n/a | n/a |
| sleep (PID 13771) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13771) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13771) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13771) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 13771) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13771) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13867) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13867) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13867) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13867) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13867) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13867) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13872) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13872) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13872) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13872) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13872) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13872) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13882) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13882) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13882) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13882) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13882) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13882) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13884) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13884) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13884) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13884) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13884) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13884) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 13886) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13886) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13886) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13886) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13886) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13886) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 13910) CPU | percent | 1 | 163.935 | 163.935 | 163.935 | 163.935 | 1.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 13910) rss_mb | MB | 2 | 51.396 | 14.648 | 88.145 | 88.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 13910) main thread run-queue wait | percent | 1 | 39.832 | 39.832 | 39.832 | 39.832 | 0.400914 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 13910) vms_mb | MB | 2 | 258.363 | 209.051 | 307.676 | 307.676 | n/a | n/a |
| sleep (PID 13926) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 13926) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13926) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 13926) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 13926) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 13926) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 14067) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14067) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14067) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14067) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14067) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14067) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 14080) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14080) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14080) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14080) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14080) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14080) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 14081) rss_mb | MB | 1 | 1.523 | 1.523 | 1.523 | 1.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 14081) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 14082) rss_mb | MB | 1 | 4.680 | 4.680 | 4.680 | 4.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 14082) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 14090) CPU | percent | 25 | 172.411 | 117.006 | 182.759 | 177.007 | 43.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 14090) rss_mb | MB | 26 | 1154.082 | 72.820 | 1754.789 | 1643.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 14090) main thread run-queue wait | percent | 25 | 54.623 | 14.118 | 73.192 | 68.121 | 13.770017 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 14090) vms_mb | MB | 26 | 1370.618 | 297.164 | 1970.320 | 1859.570 | n/a | n/a |
| sleep (PID 14103) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14103) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14103) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14103) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14103) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14103) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 14109) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14109) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14109) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14109) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14109) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14109) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 14135) CPU | percent | 196 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 14135) rss_mb | MB | 197 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 14135) main thread run-queue wait | percent | 196 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 14135) vms_mb | MB | 197 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 14136) CPU | percent | 170 | 172.849 | 108.318 | 185.087 | 175.931 | 296.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 14136) rss_mb | MB | 171 | 1444.883 | 23.164 | 1547.531 | 1327.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 14136) main thread run-queue wait | percent | 170 | 46.117 | 8.630 | 70.137 | 49.342 | 79.041365 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — build_adapter.py (PID 14136) vms_mb | MB | 171 | 1673.366 | 214.805 | 1761.496 | 1593.918 | n/a | n/a |
| sleep (PID 14145) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14145) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14145) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14145) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14145) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14145) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 14227) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14227) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14227) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14227) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14227) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14227) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 14229) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14229) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14229) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14229) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14229) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14229) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 14230) CPU | percent | 25 | 173.942 | 138.175 | 180.158 | 174.921 | 43.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 14230) rss_mb | MB | 26 | 1116.803 | 21.410 | 1847.469 | 1644.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 14230) main thread run-queue wait | percent | 25 | 59.122 | 30.102 | 76.418 | 50.658 | 14.887431 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — verify_adapter.py (PID 14230) vms_mb | MB | 26 | 1343.717 | 212.906 | 2093.949 | 1859.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 14236) rss_mb | MB | 1 | 1.402 | 1.402 | 1.402 | 1.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 14236) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 14237) rss_mb | MB | 1 | 15.965 | 15.965 | 15.965 | 15.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 14237) vms_mb | MB | 1 | 20.602 | 20.602 | 20.602 | 20.602 | n/a | n/a |
| sleep (PID 14243) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14243) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14243) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14243) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14243) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14243) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 14244) rss_mb | MB | 1 | 1.496 | 1.496 | 1.496 | 1.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 14244) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 14245) rss_mb | MB | 1 | 7.703 | 7.703 | 7.703 | 7.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 14245) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sleep (PID 14256) CPU | percent | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 14256) io read MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14256) io write MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 14256) rss_mb | MB | 42 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 14256) main thread run-queue wait | percent | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 14256) vms_mb | MB | 42 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 14273) rss_mb | MB | 1 | 1.355 | 1.355 | 1.355 | 1.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 14273) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 14274) rss_mb | MB | 1 | 19.188 | 19.188 | 19.188 | 19.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 14274) vms_mb | MB | 1 | 24.680 | 24.680 | 24.680 | 24.680 | n/a | n/a |
| docker inspect (PID 14283) rss_mb | MB | 1 | 23.391 | 23.391 | 23.391 | 23.391 | n/a | n/a |
| docker inspect (PID 14283) vms_mb | MB | 1 | 1698.438 | 1698.438 | 1698.438 | 1698.438 | n/a | n/a |
| docker commit (PID 14309) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 14309) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 14309) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 14309) rss_mb | MB | 22 | 30.438 | 30.438 | 30.438 | 30.438 | n/a | n/a |
| docker commit (PID 14309) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 14309) vms_mb | MB | 22 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 9041) CPU | percent | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 9041) io read MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 9041) io write MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 9041) rss_mb | MB | 10079 | 3.324 | 3.324 | 3.324 | 3.324 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 9041) main thread run-queue wait | percent | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 9041) vms_mb | MB | 10079 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9050) CPU | percent | 10078 | 1.519 | 0.000 | 173.787 | 0.995 | 154.170000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 9050) io read MB/s | MB/s | 10078 | 0.000 | 0.000 | 1.783 | 0.000 | 3.511719 MB | n/a |
| Agency harness — python -m lsbench (PID 9050) io write MB/s | MB/s | 10078 | 0.190 | 0.000 | 448.406 | 0.027 | 1936.417969 MB | n/a |
| Agency harness — python -m lsbench (PID 9050) rss_mb | MB | 10079 | 2909.141 | 2177.559 | 4226.051 | 3527.945 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9050) main thread run-queue wait | percent | 10078 | 0.000 | 0.000 | 0.357 | 0.000 | 0.019424 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 9050) vms_mb | MB | 10079 | 15835.931 | 13603.879 | 18544.914 | 16670.730 | n/a | n/a |
| Python — vllm (PID 9056) CPU | percent | 10078 | 0.144 | 0.000 | 6.948 | 0.000 | 14.660000 CPU seconds | n/a |
| Python — vllm (PID 9056) io read MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 9056) io write MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.004 | 0.000 | 0.089844 MB | n/a |
| Python — vllm (PID 9056) rss_mb | MB | 10079 | 1804.422 | 1802.668 | 1804.793 | 1804.789 | n/a | n/a |
| Python — vllm (PID 9056) main thread run-queue wait | percent | 10078 | 0.003 | 0.000 | 0.558 | 0.000 | 0.308376 run-queue seconds | n/a |
| Python — vllm (PID 9056) vms_mb | MB | 10079 | 11035.578 | 10971.477 | 11044.496 | 11044.496 | n/a | n/a |
| bash lsb_guard.sh (PID 9062) CPU | percent | 10078 | 0.001 | 0.000 | 0.995 | 0.000 | 0.090000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 9062) io read MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 9062) io write MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 9062) rss_mb | MB | 10079 | 3.379 | 3.379 | 3.379 | 3.379 | n/a | n/a |
| bash lsb_guard.sh (PID 9062) main thread run-queue wait | percent | 10078 | 0.000 | 0.000 | 0.105 | 0.000 | 0.003664 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 9062) vms_mb | MB | 10079 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sleep (PID 9065) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9065) io read MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9065) io write MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9065) rss_mb | MB | 16 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9065) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9065) vms_mb | MB | 16 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — python -c (PID 9095) CPU | percent | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 9095) io read MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9095) io write MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9095) rss_mb | MB | 10079 | 12.188 | 12.188 | 12.188 | 12.188 | n/a | n/a |
| Python — python -c (PID 9095) main thread run-queue wait | percent | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 9095) vms_mb | MB | 10079 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 9096) CPU | percent | 10078 | 1.771 | 0.000 | 53.452 | 1.990 | 179.860000 CPU seconds | n/a |
| VLLM::EngineCore (PID 9096) io read MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 9096) io write MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.008 | 0.000 | 0.066406 MB | n/a |
| VLLM::EngineCore (PID 9096) rss_mb | MB | 10079 | 2321.754 | 2320.918 | 2322.043 | 2321.902 | n/a | n/a |
| VLLM::EngineCore (PID 9096) main thread run-queue wait | percent | 10078 | 0.000 | 0.000 | 0.307 | 0.000 | 0.044857 run-queue seconds | n/a |
| VLLM::EngineCore (PID 9096) vms_mb | MB | 10079 | 21204.299 | 21203.422 | 21204.438 | 21204.422 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 9201) CPU | percent | 10078 | 0.040 | 0.000 | 3.976 | 0.000 | 4.060000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 9201) io read MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 9201) io write MB/s | MB/s | 10078 | 0.000 | 0.000 | 0.008 | 0.000 | 0.351562 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 9201) rss_mb | MB | 10079 | 45.309 | 43.734 | 45.559 | 45.414 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 9201) main thread run-queue wait | percent | 10078 | 0.001 | 0.000 | 0.328 | 0.000 | 0.087935 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 9201) vms_mb | MB | 10079 | 131.213 | 131.176 | 131.707 | 131.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 9320) CPU | percent | 10071 | 0.002 | 0.000 | 0.995 | 0.000 | 0.200000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 9320) rss_mb | MB | 10072 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 9320) main thread run-queue wait | percent | 10071 | 0.006 | 0.000 | 5.493 | 0.000 | 0.651116 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — docker-init (PID 9320) vms_mb | MB | 10072 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 9352) CPU | percent | 10071 | 0.003 | 0.000 | 0.995 | 0.000 | 0.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 9352) rss_mb | MB | 10072 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 9352) main thread run-queue wait | percent | 10071 | 0.005 | 0.000 | 5.435 | 0.000 | 0.513922 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — tail (PID 9352) vms_mb | MB | 10072 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9441) CPU | percent | 10071 | 43.643 | 0.000 | 95.362 | 0.000 | 4421.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9441) rss_mb | MB | 10072 | 105.811 | 3.188 | 134.906 | 134.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9441) main thread run-queue wait | percent | 10071 | 0.000 | 0.000 | 0.008 | 0.000 | 0.000164 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9441) vms_mb | MB | 10072 | 970.153 | 4.262 | 973.188 | 972.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9447) CPU | percent | 1 | 62.117 | 62.117 | 62.117 | 62.117 | 0.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9447) rss_mb | MB | 2 | 44.502 | 30.465 | 58.539 | 58.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9447) main thread run-queue wait | percent | 1 | 0.006 | 0.006 | 0.006 | 0.006 | 0.000061 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9447) vms_mb | MB | 2 | 52.023 | 37.598 | 66.449 | 66.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 9464) CPU | percent | 10044 | 1.858 | 0.000 | 25.784 | 6.964 | 187.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 9464) rss_mb | MB | 10045 | 271.884 | 224.141 | 314.465 | 310.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 9464) main thread run-queue wait | percent | 10044 | 0.556 | 0.000 | 64.603 | 0.000 | 56.298682 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — antigravity (PID 9464) vms_mb | MB | 10045 | 2225.083 | 1988.711 | 2273.207 | 2270.863 | n/a | n/a |
| sleep (PID 9486) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9486) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9486) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9486) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9486) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9486) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9489) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9489) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9489) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9489) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9489) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9489) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9559) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9559) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9559) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9559) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9559) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9559) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9567) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9567) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9568) rss_mb | MB | 1 | 21.574 | 21.574 | 21.574 | 21.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9568) vms_mb | MB | 1 | 26.988 | 26.988 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9576) rss_mb | MB | 1 | 2.691 | 2.691 | 2.691 | 2.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — bash (PID 9576) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9580) rss_mb | MB | 1 | 20.188 | 20.188 | 20.188 | 20.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — python -c (PID 9580) vms_mb | MB | 1 | 212.074 | 212.074 | 212.074 | 212.074 | n/a | n/a |
| sleep (PID 9668) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9668) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9668) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9668) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9668) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9668) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9766) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9766) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9766) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9766) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9766) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9766) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9768) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9768) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9768) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9768) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9768) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9768) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9769) rss_mb | MB | 1 | 1.512 | 1.512 | 1.512 | 1.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9769) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9770) rss_mb | MB | 1 | 20.250 | 20.250 | 20.250 | 20.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9770) vms_mb | MB | 1 | 25.066 | 25.066 | 25.066 | 25.066 | n/a | n/a |
| sleep (PID 9781) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9781) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9781) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9781) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9781) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9781) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9783) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9783) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9783) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9783) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9783) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9783) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9785) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9785) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9785) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9785) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 9785) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9785) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9883) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9883) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9883) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9883) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9883) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9883) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9885) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9885) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9885) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9885) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9885) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9885) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9886) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — sh (PID 9886) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9887) rss_mb | MB | 1 | 18.293 | 18.293 | 18.293 | 18.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-antigravity_0000_0000 — agpolicy_hook.py (PID 9887) vms_mb | MB | 1 | 24.223 | 24.223 | 24.223 | 24.223 | n/a | n/a |
| sleep (PID 9903) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9903) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9903) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9903) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 9903) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9903) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9905) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9905) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9905) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9905) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 9905) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9905) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 9907) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 9907) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9907) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 9907) rss_mb | MB | 60 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 9907) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 9907) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 CPU | percent | 10071 | 59.070 | 0.000 | 217.022 | 0.000 | 5987.077133 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 10071 | 3.585 | 0.000 | 50.460 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 10071 | 4.753 | 0.000 | 76.171 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io_psi_full_pct | percent of wall time stalled | 10071 | 0.006 | 0.000 | 37.814 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io_psi_some_pct | percent of wall time stalled | 10071 | 0.007 | 0.000 | 37.816 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io read MB/s | MB/s | 10071 | 0.002 | 0.000 | 4.659 | 0.000 | 24.609375 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 io write MB/s | MB/s | 10071 | 0.033 | 0.000 | 6.296 | 0.000 | 335.562500 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory | MB | 10072 | 381.656 | 20.547 | 2140.531 | 146.523 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory_psi_full_pct | percent of wall time stalled | 10071 | 0.002 | 0.000 | 15.782 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 memory_psi_some_pct | percent of wall time stalled | 10071 | 0.002 | 0.000 | 15.782 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 net rx MB/s | MB/s | 10071 | 0.000 | 0.000 | 0.007 | 0.000 | 0.452453 MB | n/a |
| sandbox sandbox_agent_lsb-antigravity_0000_0000 net tx MB/s | MB/s | 10071 | 0.000 | 0.000 | 0.043 | 0.000 | 3.138368 MB | n/a |
| workload total CPU | percent | 10078 | 3.499 | 1.381 | 175.147 | 2.063 | 355.378149 CPU seconds | n/a |
| workload total memory | MB | 10079 | 6201.980 | 5230.559 | 7786.684 | 7296.180 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
