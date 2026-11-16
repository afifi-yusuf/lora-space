# agprof summary

- Duration: **4892.475 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **104 calls**, 104 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1075.500 s total wait
- Tools: **107/107 completed**, 2 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **472409** at 1.915 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 4892157.546 / 4892157.546 ms |
| LLM latency p50 / p95 | 7004.493 / 28109.263 ms |
| LLM TTFT p50 / p95 | 3744.394 / 23089.833 ms |
| LLM input / output tokens | 416 / 105270 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 104 total, 104 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- claude_code: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 81/81 | 79 | 2 | 0 | n/a | n/a |
| TaskStop | 1/1 | 1 | 0 | 0 | n/a | n/a |
| ToolSearch | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 6/6 | 6 | 0 | 0 | n/a | n/a |
| mcp__agency__get_current_resources | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__token_stats | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__top_activations | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 8/8 | 8 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 10.231% | 158.757% | 496.148 s | 5849.074 MB | 12958.270 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VLLM::EngineCor | 5826 |  | 4749 | 6.021% | 43.617% | 290.100 s | 1044.897 MB | 2340.105 MB | 21241.873 MB | 21242.145 MB | 130.851562 MB | 0.035156 MB |
| lsb_grid_worker | 1960 |  | 4749 | 0.000% | 0.000% | 0.000 s | 3.010 MB | 3.117 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 5786 |  | 4749 | 3.637% | 156.608% | 178.130 s | 1883.313 MB | 7883.449 MB | 16792.738 MB | 24851.941 MB | 626.507812 MB | 12234.687500 MB |
| python | 5825 |  | 4749 | 0.000% | 0.000% | 0.000 s | 6.166 MB | 12.176 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 5791 |  | 4749 | 0.573% | 12.871% | 27.560 s | 720.841 MB | 1797.996 MB | 11041.459 MB | 11043.375 MB | 143.265625 MB | 0.136719 MB |
| docker | 6105 |  | 1 | n/a% | n/a% | n/a s | 30.590 MB | 30.590 MB | 1907.332 MB | 1907.332 MB | n/a MB | n/a MB |
| tail | 6067 | sandbox_agent_lsb-claude_code_0000_0000 | 4746 | 0.002% | 0.995% | 0.110 s | 1.285 MB | 1.285 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 6172 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 66.903% | 66.903% | 0.680 s | 58.262 MB | 70.137 MB | 67.125 MB | 78.727 MB | n/a MB | n/a MB |
| docker-init | 6041 | sandbox_agent_lsb-claude_code_0000_0000 | 4746 | 0.002% | 0.996% | 0.080 s | 0.385 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 6166 | sandbox_agent_lsb-claude_code_0000_0000 | 4746 | 30.776% | 122.403% | 1500.850 s | 87.155 MB | 111.012 MB | 973.470 MB | 978.414 MB | n/a MB | n/a MB |
| claude | 6185 | sandbox_agent_lsb-claude_code_0000_0000 | 4713 | 3.200% | 71.596% | 154.630 s | 262.413 MB | 351.664 MB | 5499.809 MB | 5499.816 MB | n/a MB | n/a MB |
| python3 | 6228 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.867 MB | 11.867 MB | 19.836 MB | 19.836 MB | n/a MB | n/a MB |
| sh | 6227 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 6229 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6230 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.949 MB | 14.949 MB | 20.176 MB | 20.176 MB | n/a MB | n/a MB |
| python3 | 6275 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.434 MB | 20.434 MB | 25.504 MB | 25.504 MB | n/a MB | n/a MB |
| sh | 6274 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 6283 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6284 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.656 MB | 9.656 MB | 13.617 MB | 13.617 MB | n/a MB | n/a MB |
| sh | 6298 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6299 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.027 MB | 16.027 MB | 21.770 MB | 21.770 MB | n/a MB | n/a MB |
| python3 | 6313 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.594 MB | 19.594 MB | 24.742 MB | 24.742 MB | n/a MB | n/a MB |
| sh | 6312 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.586 MB | 1.586 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6376 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.301 MB | 14.301 MB | 209.328 MB | 209.328 MB | n/a MB | n/a MB |
| bash | 6375 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.727 MB | 2.727 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 6415 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6416 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.480 MB | 14.480 MB | 19.887 MB | 19.887 MB | n/a MB | n/a MB |
| python3 | 6426 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.344 MB | 14.344 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| sh | 6425 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.516 MB | 1.516 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 6437 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 6435 | sandbox_agent_lsb-claude_code_0000_0000 | 396 | 0.005% | 0.989% | 0.020 s | 2.727 MB | 2.727 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 6454 | sandbox_agent_lsb-claude_code_0000_0000 | 386 | 0.003% | 0.989% | 0.010 s | 2.930 MB | 2.930 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 6456 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6458 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6461 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6463 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.320 MB | 1.320 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6465 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6467 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6469 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6473 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6471 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6476 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6478 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6480 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6484 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6482 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6487 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6489 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6491 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.285 MB | 1.285 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6495 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6493 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6498 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6501 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6503 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6505 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6507 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.320 MB | 1.320 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6509 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6512 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6514 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6517 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6519 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6539 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6542 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6544 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6549 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6547 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6551 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6553 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.273 MB | 1.273 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6555 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6557 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.320 MB | 1.320 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6559 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.320 MB | 1.320 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6561 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6564 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.277 MB | 1.277 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6566 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6568 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6570 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6572 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.320 MB | 1.320 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6575 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6577 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6582 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6580 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6584 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6587 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6589 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6592 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6594 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6596 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6598 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6600 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6604 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6602 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6606 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6609 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6611 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6616 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6614 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6618 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| python3 | 6630 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.633 MB | 14.633 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| sh | 6629 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 6666 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6667 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.551 MB | 10.551 MB | 14.992 MB | 14.992 MB | n/a MB | n/a MB |
| python3 | 6691 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 519.801 MB | 519.801 MB | 1670.922 MB | 1670.922 MB | n/a MB | n/a MB |
| bash | 6689 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.770 MB | 2.770 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6701 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.051 MB | 15.051 MB | 20.324 MB | 20.324 MB | n/a MB | n/a MB |
| sh | 6700 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6718 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.430 MB | 11.430 MB | 55.086 MB | 55.086 MB | n/a MB | n/a MB |
| bash | 6717 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.715 MB | 2.715 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 6739 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.934 MB | 2.934 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6741 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 120.208% | 140.198% | 2.420 s | 1163.014 MB | 2215.051 MB | 1380.402 MB | 2641.074 MB | n/a MB | n/a MB |
| bash | 6772 | sandbox_agent_lsb-claude_code_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.629 MB | 2.629 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6773 | sandbox_agent_lsb-claude_code_0000_0000 | 11 | 160.963% | 176.559% | 16.240 s | 1594.858 MB | 1953.492 MB | 1819.097 MB | 2173.578 MB | n/a MB | n/a MB |
| bash | 6785 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.730 MB | 2.730 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6786 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 209.477 MB | 209.477 MB | 409.273 MB | 409.273 MB | n/a MB | n/a MB |
| sh | 6801 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6802 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.523 MB | 10.523 MB | 14.992 MB | 14.992 MB | n/a MB | n/a MB |
| bash | 6810 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.949 MB | 2.949 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 6812 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 118.461 MB | 118.461 MB | 124.043 MB | 124.043 MB | n/a MB | n/a MB |
| sh | 6825 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| python3 | 6834 | sandbox_agent_lsb-claude_code_0000_0000 | 300 | 160.061% | 192.615% | 492.470 s | 5108.496 MB | 7140.609 MB | 5450.056 MB | 7378.203 MB | n/a MB | n/a MB |
| bash | 6833 | sandbox_agent_lsb-claude_code_0000_0000 | 300 | 0.000% | 0.000% | 0.000 s | 2.867 MB | 2.867 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| claude | 6842 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 30.223 MB | 204.434 MB | 787.568 MB | 5499.816 MB | n/a MB | n/a MB |
| python3 | 6843 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 2.413% | 3.067% | 0.120 s | 15.740 MB | 21.254 MB | 21.122 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 6857 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.586 MB | 1.586 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6858 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.594% | 3.955% | 0.080 s | 10.423 MB | 18.035 MB | 14.490 MB | 24.148 MB | n/a MB | n/a MB |
| bash | 6860 | sandbox_agent_lsb-claude_code_0000_0000 | 163 | 0.006% | 0.990% | 0.010 s | 2.836 MB | 2.836 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 6861 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6863 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.137 MB | 1.137 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6864 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6865 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6866 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6867 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6868 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6869 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6870 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6871 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6872 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.344 MB | 1.344 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6873 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6874 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.285 MB | 1.285 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6875 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6876 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6877 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6878 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6879 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6880 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6881 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6882 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 6884 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.090 MB | 1.145 MB | 2.825 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 6885 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 6886 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.198 MB | 1.289 MB | 2.825 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 6887 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6906 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6907 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6908 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6909 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6910 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6911 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6912 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6914 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6915 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6916 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6918 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6919 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6920 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6921 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6924 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6925 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6926 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6927 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6928 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6929 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6930 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6931 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6932 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6933 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6935 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 6959 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.777 MB | 2.777 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6960 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 169.723 MB | 169.723 MB | 366.117 MB | 366.117 MB | n/a MB | n/a MB |
| bash | 6992 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.898 MB | 2.898 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6994 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 140.626% | 140.626% | 1.420 s | 544.350 MB | 1034.527 MB | 978.574 MB | 1256.203 MB | n/a MB | n/a MB |
| python3 | 7011 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 159.134% | 172.484% | 9.700 s | 1969.157 MB | 3191.930 MB | 2312.731 MB | 4294.848 MB | n/a MB | n/a MB |
| bash | 7009 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.715 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7032 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 94.324% | 94.324% | 0.950 s | 592.008 MB | 1170.027 MB | 1251.607 MB | 2295.750 MB | n/a MB | n/a MB |
| bash | 7031 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.719 MB | 2.719 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 7047 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.891 MB | 2.891 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 7057 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7058 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.969 MB | 8.969 MB | 13.410 MB | 13.410 MB | n/a MB | n/a MB |
| bash | 7105 | sandbox_agent_lsb-claude_code_0000_0000 | 157 | 0.000% | 0.000% | 0.000 s | 2.906 MB | 2.906 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7106 | sandbox_agent_lsb-claude_code_0000_0000 | 157 | 169.319% | 176.938% | 266.180 s | 1133.224 MB | 1227.086 MB | 1408.837 MB | 1670.953 MB | n/a MB | n/a MB |
| sh | 7113 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.441 MB | 1.441 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7114 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 4.970% | 7.952% | 0.100 s | 14.780 MB | 20.559 MB | 19.714 MB | 25.633 MB | n/a MB | n/a MB |
| python3 | 7120 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 5.962% | 7.954% | 0.120 s | 14.176 MB | 21.391 MB | 19.507 MB | 26.844 MB | n/a MB | n/a MB |
| sh | 7119 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.480 MB | 1.480 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7123 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.164 MB | 8.164 MB | 13.023 MB | 13.023 MB | n/a MB | n/a MB |
| bash | 7122 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.699 MB | 2.699 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7125 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 2.479% | 2.978% | 0.050 s | 14.193 MB | 18.250 MB | 19.296 MB | 24.254 MB | n/a MB | n/a MB |
| sh | 7124 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7196 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.836 MB | 14.836 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| sh | 7195 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7202 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7203 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.348 MB | 20.348 MB | 25.246 MB | 25.246 MB | n/a MB | n/a MB |
| sh | 7214 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.500 MB | 0.500 MB | n/a MB | n/a MB |
| python3 | 7224 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.285 MB | 20.285 MB | 25.246 MB | 25.246 MB | n/a MB | n/a MB |
| sh | 7223 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.520 MB | 1.520 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7230 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.715 MB | 9.715 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| sh | 7229 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.426 MB | 1.426 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7233 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 162.863 MB | 162.863 MB | 356.648 MB | 356.648 MB | n/a MB | n/a MB |
| bash | 7231 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.773 MB | 2.773 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 7243 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 7246 | sandbox_agent_lsb-claude_code_0000_0000 | 600 | 0.008% | 1.989% | 0.050 s | 2.773 MB | 2.773 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7247 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7248 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7249 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7250 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7251 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7252 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7253 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7254 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7256 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7257 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7259 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7260 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7261 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7262 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7263 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7264 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7265 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7266 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7268 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7269 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7285 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7289 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7290 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7291 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7292 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7293 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7294 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.294 MB | 1.352 MB | 2.748 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7295 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7296 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.305 MB | 1.305 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7297 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7298 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7300 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7302 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7303 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7304 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7305 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7306 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7307 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.129 MB | 1.129 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7308 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7309 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7310 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7312 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7313 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7315 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7316 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7317 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7319 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7320 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7321 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7322 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7323 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7324 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7325 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7326 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7327 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7328 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7329 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7330 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7331 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7332 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7333 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7334 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7335 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 0.928 MB | 1.160 MB | 2.035 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7336 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7338 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7339 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7340 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7341 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7342 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7343 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7344 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7345 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7346 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7347 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7348 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7350 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7351 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7352 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7354 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7355 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7374 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7375 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7376 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7377 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7378 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7379 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7380 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7382 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7383 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7384 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7386 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7387 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.215 MB | 1.215 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7388 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7389 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7390 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7391 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7392 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7394 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7395 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7397 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7398 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.344 MB | 1.344 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7399 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7400 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7401 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7402 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7403 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7404 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7405 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7407 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7408 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7409 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7410 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7412 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7413 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7414 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7416 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7417 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7419 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7420 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7421 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7429 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.305 MB | 1.305 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sh | 7435 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.379 MB | 1.379 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7433 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.586 MB | 1.586 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7436 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.684 MB | 13.684 MB | 19.836 MB | 19.836 MB | n/a MB | n/a MB |
| python3 | 7434 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.082 MB | 10.082 MB | 14.992 MB | 14.992 MB | n/a MB | n/a MB |
| python3 | 7463 | sandbox_agent_lsb-claude_code_0000_0000 | 56 | 163.989% | 176.055% | 90.880 s | 4009.729 MB | 5088.520 MB | 4307.056 MB | 6088.367 MB | n/a MB | n/a MB |
| bash | 7461 | sandbox_agent_lsb-claude_code_0000_0000 | 56 | 0.000% | 0.000% | 0.000 s | 3.020 MB | 3.020 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 7478 | sandbox_agent_lsb-claude_code_0000_0000 | 57 | 0.000% | 0.000% | 0.000 s | 2.836 MB | 2.836 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7480 | sandbox_agent_lsb-claude_code_0000_0000 | 57 | 162.899% | 175.196% | 91.880 s | 3945.651 MB | 5157.219 MB | 4198.583 MB | 6027.797 MB | n/a MB | n/a MB |
| python3 | 7515 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 167.070% | 172.826% | 23.580 s | 460.910 MB | 635.945 MB | 672.930 MB | 848.898 MB | n/a MB | n/a MB |
| bash | 7513 | sandbox_agent_lsb-claude_code_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7674 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.484 MB | 21.484 MB | 26.902 MB | 26.902 MB | n/a MB | n/a MB |
| sh | 7673 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7699 | sandbox_agent_lsb-claude_code_0000_0000 | 123 | 155.111% | 178.306% | 191.250 s | 3717.100 MB | 5780.781 MB | 4018.689 MB | 6171.910 MB | n/a MB | n/a MB |
| bash | 7698 | sandbox_agent_lsb-claude_code_0000_0000 | 123 | 0.000% | 0.000% | 0.000 s | 2.762 MB | 2.762 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7860 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7859 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.848 MB | 2.848 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7873 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.586 MB | 21.586 MB | 213.711 MB | 213.711 MB | n/a MB | n/a MB |
| bash | 7872 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.691 MB | 2.691 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 7893 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7894 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.836 MB | 3.836 MB | 9.633 MB | 9.633 MB | n/a MB | n/a MB |
| python3 | 7905 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 86.090% | 86.090% | 0.870 s | 359.414 MB | 700.590 MB | 553.141 MB | 895.160 MB | n/a MB | n/a MB |
| bash | 7904 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.902 MB | 2.902 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 7921 | sandbox_agent_lsb-claude_code_0000_0000 | 88 | 0.000% | 0.000% | 0.000 s | 2.664 MB | 2.664 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7922 | sandbox_agent_lsb-claude_code_0000_0000 | 88 | 168.394% | 179.496% | 147.600 s | 1243.169 MB | 1502.422 MB | 1458.713 MB | 1714.719 MB | n/a MB | n/a MB |
| python3 | 7947 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.828 MB | 18.828 MB | 24.605 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 7945 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7953 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7954 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.699 MB | 14.699 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| python3 | 7961 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 151.757% | 176.709% | 6.110 s | 1564.777 MB | 2656.469 MB | 1816.895 MB | 3038.145 MB | n/a MB | n/a MB |
| bash | 7960 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.883 MB | 2.883 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7974 | sandbox_agent_lsb-claude_code_0000_0000 | 25 | 167.212% | 177.763% | 40.460 s | 1723.082 MB | 2204.652 MB | 1995.728 MB | 2782.266 MB | n/a MB | n/a MB |
| bash | 7973 | sandbox_agent_lsb-claude_code_0000_0000 | 25 | 0.000% | 0.000% | 0.000 s | 2.645 MB | 2.645 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7987 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.031 MB | 8.031 MB | 12.926 MB | 12.926 MB | n/a MB | n/a MB |
| sh | 7986 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 8023 | sandbox_agent_lsb-claude_code_0000_0000 | 210 | 0.000% | 0.000% | 0.000 s | 2.751 MB | 2.805 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8025 | sandbox_agent_lsb-claude_code_0000_0000 | 210 | 81.177% | 179.717% | 174.770 s | 7892.189 MB | 10638.871 MB | 10500.569 MB | 17725.734 MB | n/a MB | n/a MB |
| claude | 8053 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 238.824 MB | 238.824 MB | 5499.816 MB | 5499.816 MB | n/a MB | n/a MB |
| bash | 8069 | sandbox_agent_lsb-claude_code_0000_0000 | 61 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 8070 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8072 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8073 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8075 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8076 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8152 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8153 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8156 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8157 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8158 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8159 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8161 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8162 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sh | 8164 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8165 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.492 MB | 21.492 MB | 26.902 MB | 26.902 MB | n/a MB | n/a MB |
| bash | 8185 | sandbox_agent_lsb-claude_code_0000_0000 | 20 | 0.000% | 0.000% | 0.000 s | 2.855 MB | 2.855 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 8186 | sandbox_agent_lsb-claude_code_0000_0000 | 20 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sh | 8223 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.594 MB | 1.594 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8224 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.953 MB | 16.953 MB | 22.066 MB | 22.066 MB | n/a MB | n/a MB |
| python3 | 8234 | sandbox_agent_lsb-claude_code_0000_0000 | 115 | 165.020% | 176.499% | 189.530 s | 1647.943 MB | 2014.348 MB | 1872.211 MB | 2226.809 MB | n/a MB | n/a MB |
| bash | 8232 | sandbox_agent_lsb-claude_code_0000_0000 | 115 | 0.000% | 0.000% | 0.000 s | 2.832 MB | 2.832 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8254 | sandbox_agent_lsb-claude_code_0000_0000 | 106 | 171.189% | 199.732% | 181.050 s | 1886.250 MB | 2213.594 MB | 2106.888 MB | 2426.035 MB | n/a MB | n/a MB |
| bash | 8253 | sandbox_agent_lsb-claude_code_0000_0000 | 106 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 8279 | sandbox_agent_lsb-claude_code_0000_0000 | 215 | 0.000% | 0.000% | 0.000 s | 2.898 MB | 2.898 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8281 | sandbox_agent_lsb-claude_code_0000_0000 | 215 | 168.816% | 179.269% | 364.130 s | 2183.293 MB | 2393.410 MB | 2404.579 MB | 2605.785 MB | n/a MB | n/a MB |
| python3 | 8319 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 1.973% | 1.983% | 0.040 s | 11.111 MB | 15.449 MB | 15.781 MB | 20.426 MB | n/a MB | n/a MB |
| sh | 8318 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.453 MB | 1.453 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 8327 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.512 MB | 1.512 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8328 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.649% | 2.982% | 0.080 s | 12.562 MB | 18.145 MB | 17.438 MB | 24.148 MB | n/a MB | n/a MB |
| bash | 8329 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.535 MB | 2.535 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 8332 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.617 MB | 18.617 MB | 24.605 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 8331 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.410 MB | 1.410 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 8337 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8338 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.512 MB | 21.512 MB | 26.902 MB | 26.902 MB | n/a MB | n/a MB |
| bash | 8339 | sandbox_agent_lsb-claude_code_0000_0000 | 131 | 0.008% | 0.990% | 0.010 s | 2.652 MB | 2.652 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| claude | 8340 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.578 MB | 2.578 MB | 283.352 MB | 283.352 MB | n/a MB | n/a MB |
| sleep | 8341 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.273 MB | 1.273 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 8342 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.656 MB | 1.656 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 8343 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.238 MB | 1.238 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8345 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8347 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8350 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8353 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8355 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8358 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.246 MB | 1.246 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8360 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8362 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.250 MB | 1.250 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8365 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8367 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.273 MB | 1.273 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8369 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8371 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 8376 | sandbox_agent_lsb-claude_code_0000_0000 | 60 | 0.000% | 0.000% | 0.000 s | 1.258 MB | 1.258 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| python3 | 8430 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.852 MB | 16.852 MB | 22.066 MB | 22.066 MB | n/a MB | n/a MB |
| sh | 8429 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.387 MB | 1.387 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 8474 | sandbox_agent_lsb-claude_code_0000_0000 | 29 | 0.000% | 0.000% | 0.000 s | 2.781 MB | 2.781 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8476 | sandbox_agent_lsb-claude_code_0000_0000 | 29 | 166.657% | 178.493% | 47.010 s | 4746.288 MB | 5181.918 MB | 4984.041 MB | 5394.430 MB | n/a MB | n/a MB |
| python3 | 8513 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.797 MB | 14.797 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| sh | 8512 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.508 MB | 1.508 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 8525 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8526 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.469 MB | 21.469 MB | 26.902 MB | 26.902 MB | n/a MB | n/a MB |
| python3 | 8535 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 692.660 MB | 692.660 MB | 898.449 MB | 898.449 MB | n/a MB | n/a MB |
| bash | 8534 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.672 MB | 2.672 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 8548 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.941 MB | 2.941 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8549 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 128.331% | 128.331% | 1.300 s | 426.777 MB | 832.223 MB | 634.006 MB | 1054.309 MB | n/a MB | n/a MB |
| python3 | 8561 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.535 MB | 7.535 MB | 11.926 MB | 11.926 MB | n/a MB | n/a MB |
| sh | 8560 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8565 | sandbox_agent_lsb-claude_code_0000_0000 | 25 | 170.033% | 174.170% | 41.090 s | 2848.534 MB | 3265.887 MB | 3061.478 MB | 3478.297 MB | n/a MB | n/a MB |
| bash | 8563 | sandbox_agent_lsb-claude_code_0000_0000 | 25 | 0.000% | 0.000% | 0.000 s | 2.988 MB | 2.988 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8579 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.117 MB | 21.117 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| sh | 8578 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.512 MB | 1.512 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 8582 | sandbox_agent_lsb-claude_code_0000_0000 | 147 | 0.000% | 0.000% | 0.000 s | 2.805 MB | 2.805 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8584 | sandbox_agent_lsb-claude_code_0000_0000 | 147 | 169.637% | 177.144% | 249.560 s | 2324.872 MB | 2648.762 MB | 2544.390 MB | 2860.422 MB | n/a MB | n/a MB |
| python3 | 8610 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 8.884% | 8.884% | 0.090 s | 13.033 MB | 18.844 MB | 18.197 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 8609 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.586 MB | 1.586 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8619 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.638% | 3.964% | 0.080 s | 12.281 MB | 18.105 MB | 17.316 MB | 24.098 MB | n/a MB | n/a MB |
| sh | 8618 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.480 MB | 1.480 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 8665 | sandbox_agent_lsb-claude_code_0000_0000 | 66 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8667 | sandbox_agent_lsb-claude_code_0000_0000 | 66 | 162.679% | 174.619% | 106.490 s | 3145.902 MB | 4679.008 MB | 3404.068 MB | 5155.270 MB | n/a MB | n/a MB |
| sh | 8794 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8795 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.902 MB | 8.902 MB | 13.410 MB | 13.410 MB | n/a MB | n/a MB |
| sh | 8862 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.387 MB | 1.387 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8863 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.148 MB | 15.148 MB | 20.324 MB | 20.324 MB | n/a MB | n/a MB |
| python3 | 8875 | sandbox_agent_lsb-claude_code_0000_0000 | 179 | 169.847% | 176.821% | 304.570 s | 2656.373 MB | 3106.863 MB | 2872.013 MB | 3318.137 MB | n/a MB | n/a MB |
| bash | 8873 | sandbox_agent_lsb-claude_code_0000_0000 | 179 | 0.000% | 0.000% | 0.000 s | 2.848 MB | 2.848 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 9126 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 6.944% | 6.944% | 0.070 s | 13.082 MB | 18.496 MB | 18.090 MB | 24.254 MB | n/a MB | n/a MB |
| sh | 9125 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9133 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 3.229% | 6.958% | 0.130 s | 13.730 MB | 21.012 MB | 18.841 MB | 26.840 MB | n/a MB | n/a MB |
| sh | 9132 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.387 MB | 1.387 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sleep | 9138 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 9135 | sandbox_agent_lsb-claude_code_0000_0000 | 46 | 0.000% | 0.000% | 0.000 s | 2.770 MB | 2.770 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 9141 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 9144 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 9147 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.273 MB | 1.273 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 9150 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.250 MB | 2.697 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 9154 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 9157 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.223 MB | 1.223 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 9160 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 9164 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.273 MB | 1.273 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sh | 9183 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9184 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.027 MB | 15.027 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| python3 | 9367 | sandbox_agent_lsb-claude_code_0000_0000 | 39 | 169.529% | 176.378% | 64.900 s | 3633.189 MB | 4358.348 MB | 3851.858 MB | 4569.871 MB | n/a MB | n/a MB |
| bash | 9365 | sandbox_agent_lsb-claude_code_0000_0000 | 39 | 0.000% | 0.000% | 0.000 s | 2.816 MB | 2.816 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9387 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.203 MB | 20.203 MB | 212.223 MB | 212.223 MB | n/a MB | n/a MB |
| bash | 9386 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.758 MB | 2.758 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 9433 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.895 MB | 2.895 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 9434 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 174.786% | 174.786% | 1.770 s | 115.004 MB | 115.703 MB | 333.793 MB | 333.793 MB | n/a MB | n/a MB |
| sh | 9461 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.582 MB | 1.582 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 9462 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.738 MB | 9.738 MB | 14.707 MB | 14.707 MB | n/a MB | n/a MB |
| docker | 9474 |  | 1 | n/a% | n/a% | n/a s | 29.656 MB | 29.656 MB | 1843.520 MB | 1843.520 MB | n/a MB | n/a MB |
| docker | 9491 |  | 24 | 0.000% | 0.000% | 0.000 s | 30.086 MB | 30.086 MB | 1771.516 MB | 1771.516 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 19.187% | 100.000% | 12032.240 MB | 15160.000 MB | 36.752 W | 75.150 W | 178981.036 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-claude_code_0000_0000 | 100.143% | 275.897% | 4834.859 s | 2356.008 MB | 11306.398 MB | 8184.062500 MB | 9309.667969 MB | 8.498790 MB | 0.046544 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 5933 | 4892.408 | interrupted |
| harness:retire | -1 | 6.946 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sync:result_wait | 1/1 | 0 | 0 | 4892.266 | 0.000 | 4892.265 | 8184.062 | 4892265.505 | 4892265.505 | 4892265.505 |
| run:write_lora_adapter | 1/1 | 0 | 0 | 4892.158 | n/a | n/a | 8184.062 | 4892157.546 | 4892157.546 | 4892157.546 |
| engine:execute | 1/1 | 0 | 0 | 4892.153 | 5.339 | 4886.352 | 8184.062 | 4892153.049 | 4892153.049 | 4892153.049 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 4857.001 | 0.024 | 4856.977 | 8166.931 | 4857000.881 | 4857000.881 | 4857000.881 |
| harness:await_cli | 1/1 | 0 | 0 | 4849.666 | n/a | n/a | 8039.437 | 4849665.533 | 4849665.533 | 4849665.533 |
| tool:Bash | 81/81 | 2 | 0 | 3006.772 | n/a | n/a | 7718.139 | 37120.637 | 1270.752 | 131516.207 |
| llm:attempt | 104/104 | 0 | 0 | 1075.500 | 6.546 | 1068.688 | 125.309 | 10341.347 | 7004.493 | 28109.263 |
| tool:mcp__agency__generate | 6/6 | 0 | 0 | 354.723 | n/a | n/a | 5.487 | 59120.583 | 45806.519 | 120242.225 |
| tool:mcp__agency__trace | 8/8 | 0 | 0 | 251.043 | n/a | n/a | 54.283 | 31380.398 | 18831.757 | 92877.356 |
| tool:mcp__agency__top_activations | 1/1 | 0 | 0 | 33.165 | n/a | n/a | 0.131 | 33164.843 | 33164.843 | 33164.843 |
| run:container_call | 13/13 | 0 | 0 | 27.022 | 0.003 | 27.020 | 0.002 | 2078.653 | 60.626 | 10172.944 |
| teardown:commit | 1/1 | 0 | 0 | 25.985 | 0.005 | 25.980 | 0.002 | 25985.316 | 25985.316 | 25985.316 |
| sandbox:commit | 1/1 | 0 | 0 | 25.271 | 0.004 | 25.268 | 0.002 | 25271.473 | 25271.473 | 25271.473 |
| checkpoint.total | 1/1 | 0 | 0 | 25.270 | 0.003 | 25.267 | 0.002 | 25270.036 | 25270.036 | 25270.036 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 25.270 | 0.003 | 25.267 | 0.002 | 25269.822 | 25269.822 | 25269.822 |
| tool:mcp__agency__token_stats | 1/1 | 0 | 0 | 4.963 | n/a | n/a | 0.020 | 4963.310 | 4963.310 | 4963.310 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.942 | 1.059 | 3.883 | 17.033 | 4942.001 | 4942.001 | 4942.001 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.942 | 1.059 | 3.883 | 17.032 | 4941.778 | 4941.778 | 4941.778 |
| syscall:sendto | 831/831 | 0 | 0 | 3.890 | n/a | n/a | 17.963 | 4.681 | 2.124 | 7.546 |
| syscall:execve | 1057/1057 | 0 | 0 | 3.713 | n/a | n/a | 11.827 | 3.513 | 1.444 | 4.906 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 2.783 | 0.031 | 2.752 | 0.006 | 2782.793 | 2782.793 | 2782.793 |
| tool:mcp__agency__inspect_module_inputs | 2/2 | 0 | 0 | 2.717 | n/a | n/a | 0.266 | 1358.425 | 1358.425 | 1988.596 |
| harness:startup_ready | 1/1 | 0 | 0 | 2.015 | n/a | n/a | 60.089 | 2015.030 | 2015.030 | 2015.030 |
| tool:mcp__agency__inspect | 2/2 | 0 | 0 | 1.807 | n/a | n/a | 0.080 | 903.349 | 903.349 | 1115.020 |
| syscall:connect | 311/311 | 0 | 0 | 1.720 | n/a | n/a | 8.869 | 5.530 | 2.201 | 8.634 |
| sandbox:start | 1/1 | 0 | 0 | 0.970 | 0.003 | 0.968 | 0.000 | 970.218 | 970.218 | 970.218 |
| runtime.container_create | 1/1 | 0 | 0 | 0.970 | 0.002 | 0.968 | 0.000 | 970.083 | 970.083 | 970.083 |
| sandbox:create | 1/1 | 0 | 0 | 0.945 | 0.244 | 0.700 | 0.000 | 944.699 | 944.699 | 944.699 |
| sandbox:stop | 1/1 | 0 | 0 | 0.713 | 0.002 | 0.711 | 0.000 | 712.953 | 712.953 | 712.953 |
| tool:ToolSearch | 2/2 | 0 | 0 | 0.664 | n/a | n/a | 1.352 | 331.821 | 331.821 | 450.064 |
| harness:submit | 1/1 | 0 | 0 | 0.609 | n/a | n/a | 7.842 | 609.290 | 609.290 | 609.290 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.576 | n/a | n/a | 0.001 | 575.961 | 575.961 | 575.961 |
| run:detect | 1/1 | 0 | 0 | 0.485 | 0.001 | 0.485 | 0.000 | 485.305 | 485.305 | 485.305 |
| tool:TaskStop | 1/1 | 0 | 0 | 0.352 | n/a | n/a | 1.439 | 352.476 | 352.476 | 352.476 |
| tool:mcp__agency__get_current_resources | 1/1 | 0 | 0 | 0.249 | n/a | n/a | 0.569 | 248.599 | 248.599 | 248.599 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.217 | n/a | n/a | 0.055 | 216.639 | 216.639 | 216.639 |
| agency:services_close | 1/1 | 0 | 0 | 0.153 | 0.003 | 0.150 | 0.000 | 152.719 | 152.719 | 152.719 |
| agency:services_start | 1/1 | 0 | 0 | 0.107 | 0.047 | 0.060 | 0.000 | 106.921 | 106.921 | 106.921 |
| harness:launch | 1/1 | 0 | 0 | 0.053 | n/a | n/a | 4.516 | 52.861 | 52.861 | 52.861 |
| agent:create | 1/1 | 0 | 0 | 0.051 | 0.009 | 0.042 | 0.000 | 50.544 | 50.544 | 50.544 |
| harness:snapshot | 1/1 | 0 | 0 | 0.008 | n/a | n/a | 0.054 | 8.389 | 8.389 | 8.389 |
| syscall:bind | 2/2 | 0 | 0 | 0.003 | n/a | n/a | 0.045 | 1.266 | 1.266 | 1.402 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.216 | 1.216 | 1.216 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.084 | 0.074 | 0.137 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.171 | 0.171 | 0.171 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.052 | 0.052 | 0.052 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 4746 | 0.218 | 0.009 | 44.221 | 26.939 | 10.600332 CPU seconds | n/a |
| GPU 0 memory | MB | 4749 | 12032.240 | 11670.000 | 15160.000 | 12192.000 | n/a | n/a |
| GPU 0 power | W | 4749 | 36.752 | 27.509 | 75.150 | 28.268 | n/a | 178981.036 J |
| GPU 0 proc / 5786-819554 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c memory | MB | 4749 | 3275.049 | 3118.000 | 6402.000 | 3376.000 | n/a | n/a |
| GPU 0 proc / 5786-819554 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c estimated power | W | 3549 | 1.801 | 0.000 | 74.149 | 0.000 | n/a | n/a |
| GPU 0 proc / 5786-819554 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c utilization | percent | 3549 | 2.270 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 5826-821596 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c memory | MB | 4749 | 8275.191 | 8070.000 | 8334.000 | 8334.000 | n/a | n/a |
| GPU 0 proc / 5826-821596 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c estimated power | W | 1069 | 53.691 | 0.000 | 72.423 | 0.000 | n/a | n/a |
| GPU 0 proc / 5826-821596 / sandbox / ~ / device / GPU-a6154c04-2f5a-d81b-cd45-27e2d06a5a3c utilization | percent | 1069 | 74.399 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 4749 | 11550.240 | 11188.000 | 14678.000 | 11710.000 | n/a | n/a |
| GPU 0 utilization | percent | 4749 | 19.187 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 4749 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 4748 | 25.425 | 0.081 | 93.409 | 3.335 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 4748 | 27.786 | 0.404 | 59.453 | 12.887 | n/a | n/a |
| host disk_read_mb_s | MB/s | 4748 | 2.134 | 0.000 | 210.122 | 11.886 | n/a | n/a |
| host disk_write_mb_s | MB/s | 4748 | 5.288 | 0.000 | 363.630 | 10.985 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 4748 | 4.767 | 0.000 | 100.000 | 26.632 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 4748 | 5.147 | 0.000 | 100.000 | 27.730 | n/a | n/a |
| host mem_total_mb | MB | 4749 | 15363.539 | 15363.539 | 15363.539 | 15363.539 | n/a | n/a |
| host mem_used_mb | MB | 4749 | 5236.575 | 2109.594 | 12715.531 | 2473.238 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 4748 | 1.037 | 0.000 | 100.000 | 0.053 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 4748 | 1.082 | 0.000 | 100.000 | 0.060 | n/a | n/a |
| host net_rx_mb_s | MB/s | 4748 | 0.003 | 0.000 | 8.704 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 4748 | 0.009 | 0.000 | 0.856 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1960) CPU | percent | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1960) io read MB/s | MB/s | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1960) io write MB/s | MB/s | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1960) rss_mb | MB | 4749 | 3.010 | 2.992 | 3.117 | 2.992 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1960) main thread run-queue wait | percent | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1960) vms_mb | MB | 4749 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 5786) CPU | percent | 4748 | 3.637 | 0.000 | 156.608 | 2.981 | 178.130000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 5786) io read MB/s | MB/s | 4748 | 0.047 | 0.000 | 17.601 | 0.792 | 626.507812 MB | n/a |
| Agency harness — python -m lsbench (PID 5786) io write MB/s | MB/s | 4748 | 2.526 | 0.000 | 1138.850 | 5.586 | 12234.687500 MB | n/a |
| Agency harness — python -m lsbench (PID 5786) rss_mb | MB | 4749 | 1883.313 | 601.125 | 7883.449 | 1307.707 | n/a | n/a |
| Agency harness — python -m lsbench (PID 5786) main thread run-queue wait | percent | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 5786) vms_mb | MB | 4749 | 16792.738 | 14031.797 | 24851.941 | 17148.637 | n/a | n/a |
| Python — vllm (PID 5791) CPU | percent | 4748 | 0.573 | 0.000 | 12.871 | 0.994 | 27.560000 CPU seconds | n/a |
| Python — vllm (PID 5791) io read MB/s | MB/s | 4748 | 0.030 | 0.000 | 8.509 | 0.000 | 143.265625 MB | n/a |
| Python — vllm (PID 5791) io write MB/s | MB/s | 4748 | 0.000 | 0.000 | 0.008 | 0.000 | 0.136719 MB | n/a |
| Python — vllm (PID 5791) rss_mb | MB | 4749 | 720.841 | 407.809 | 1797.996 | 477.559 | n/a | n/a |
| Python — vllm (PID 5791) main thread run-queue wait | percent | 4748 | 0.018 | 0.000 | 3.208 | 0.000 | 0.870040 run-queue seconds | n/a |
| Python — vllm (PID 5791) vms_mb | MB | 4749 | 11041.459 | 10966.355 | 11043.375 | 11042.375 | n/a | n/a |
| Python — python -c (PID 5825) CPU | percent | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 5825) io read MB/s | MB/s | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 5825) io write MB/s | MB/s | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 5825) rss_mb | MB | 4749 | 6.166 | 4.527 | 12.176 | 4.527 | n/a | n/a |
| Python — python -c (PID 5825) main thread run-queue wait | percent | 4748 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 5825) vms_mb | MB | 4749 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 5826) CPU | percent | 4748 | 6.021 | 0.000 | 43.617 | 0.000 | 290.100000 CPU seconds | n/a |
| VLLM::EngineCore (PID 5826) io read MB/s | MB/s | 4748 | 0.027 | 0.000 | 9.036 | 0.000 | 130.851562 MB | n/a |
| VLLM::EngineCore (PID 5826) io write MB/s | MB/s | 4748 | 0.000 | 0.000 | 0.008 | 0.000 | 0.035156 MB | n/a |
| VLLM::EngineCore (PID 5826) rss_mb | MB | 4749 | 1044.897 | 642.488 | 2340.105 | 707.109 | n/a | n/a |
| VLLM::EngineCore (PID 5826) main thread run-queue wait | percent | 4748 | 0.009 | 0.000 | 8.269 | 0.000 | 0.436618 run-queue seconds | n/a |
| VLLM::EngineCore (PID 5826) vms_mb | MB | 4749 | 21241.873 | 21235.098 | 21242.145 | 21242.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 6041) CPU | percent | 4745 | 0.002 | 0.000 | 0.996 | 0.000 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 6041) rss_mb | MB | 4746 | 0.385 | 0.051 | 0.551 | 0.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 6041) main thread run-queue wait | percent | 4745 | 0.017 | 0.000 | 5.424 | 0.000 | 0.834075 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 6041) vms_mb | MB | 4746 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 6067) CPU | percent | 4745 | 0.002 | 0.000 | 0.995 | 0.000 | 0.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 6067) rss_mb | MB | 4746 | 1.285 | 1.285 | 1.285 | 1.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 6067) main thread run-queue wait | percent | 4745 | 0.016 | 0.000 | 5.349 | 0.000 | 0.796015 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 6067) vms_mb | MB | 4746 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| docker exec (PID 6105) rss_mb | MB | 1 | 30.590 | 30.590 | 30.590 | 30.590 | n/a | n/a |
| docker exec (PID 6105) vms_mb | MB | 1 | 1907.332 | 1907.332 | 1907.332 | 1907.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6166) CPU | percent | 4745 | 30.776 | 0.000 | 122.403 | 0.000 | 1500.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6166) rss_mb | MB | 4746 | 87.155 | 2.949 | 111.012 | 108.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6166) main thread run-queue wait | percent | 4745 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000133 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6166) vms_mb | MB | 4746 | 973.470 | 4.262 | 978.414 | 975.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6172) CPU | percent | 1 | 66.903 | 66.903 | 66.903 | 66.903 | 0.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6172) rss_mb | MB | 2 | 58.262 | 46.387 | 70.137 | 70.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6172) main thread run-queue wait | percent | 1 | 0.016 | 0.016 | 0.016 | 0.016 | 0.000168 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6172) vms_mb | MB | 2 | 67.125 | 55.523 | 78.727 | 78.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6185) CPU | percent | 4712 | 3.200 | 0.000 | 71.596 | 7.961 | 154.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6185) rss_mb | MB | 4713 | 262.413 | 75.762 | 351.664 | 271.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6185) main thread run-queue wait | percent | 4712 | 18.565 | 0.000 | 89.944 | 0.048 | 883.703226 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6185) vms_mb | MB | 4713 | 5499.809 | 5484.793 | 5499.816 | 5499.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6227) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6227) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6228) rss_mb | MB | 1 | 11.867 | 11.867 | 11.867 | 11.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6228) vms_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6229) rss_mb | MB | 1 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6229) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6230) rss_mb | MB | 1 | 14.949 | 14.949 | 14.949 | 14.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6230) vms_mb | MB | 1 | 20.176 | 20.176 | 20.176 | 20.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6274) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6274) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6275) rss_mb | MB | 1 | 20.434 | 20.434 | 20.434 | 20.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6275) vms_mb | MB | 1 | 25.504 | 25.504 | 25.504 | 25.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6283) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6283) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6284) rss_mb | MB | 1 | 9.656 | 9.656 | 9.656 | 9.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6284) vms_mb | MB | 1 | 13.617 | 13.617 | 13.617 | 13.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6298) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6298) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6299) rss_mb | MB | 1 | 16.027 | 16.027 | 16.027 | 16.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6299) vms_mb | MB | 1 | 21.770 | 21.770 | 21.770 | 21.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6312) rss_mb | MB | 1 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6312) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6313) rss_mb | MB | 1 | 19.594 | 19.594 | 19.594 | 19.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6313) vms_mb | MB | 1 | 24.742 | 24.742 | 24.742 | 24.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6375) rss_mb | MB | 1 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6375) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6376) rss_mb | MB | 1 | 14.301 | 14.301 | 14.301 | 14.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6376) vms_mb | MB | 1 | 209.328 | 209.328 | 209.328 | 209.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6415) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6415) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6416) rss_mb | MB | 1 | 14.480 | 14.480 | 14.480 | 14.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6416) vms_mb | MB | 1 | 19.887 | 19.887 | 19.887 | 19.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6425) rss_mb | MB | 1 | 1.516 | 1.516 | 1.516 | 1.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6425) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6426) rss_mb | MB | 1 | 14.344 | 14.344 | 14.344 | 14.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6426) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6435) CPU | percent | 395 | 0.005 | 0.000 | 0.989 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6435) rss_mb | MB | 396 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6435) main thread run-queue wait | percent | 395 | 0.001 | 0.000 | 0.117 | 0.000 | 0.002634 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6435) vms_mb | MB | 396 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6437) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6437) rss_mb | MB | 10 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6437) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6437) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6454) CPU | percent | 385 | 0.003 | 0.000 | 0.989 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6454) rss_mb | MB | 386 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6454) main thread run-queue wait | percent | 385 | 0.001 | 0.000 | 0.233 | 0.000 | 0.003438 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6454) vms_mb | MB | 386 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6456) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6456) rss_mb | MB | 15 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6456) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6456) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6458) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6458) rss_mb | MB | 10 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6458) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6458) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6461) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6461) rss_mb | MB | 14 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6461) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6461) vms_mb | MB | 14 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6463) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6463) rss_mb | MB | 10 | 1.320 | 1.320 | 1.320 | 1.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6463) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6463) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6465) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6465) rss_mb | MB | 9 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6465) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6465) vms_mb | MB | 9 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6467) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6467) rss_mb | MB | 15 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6467) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6467) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6469) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6469) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6469) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6469) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6471) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6471) rss_mb | MB | 15 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6471) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6471) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6473) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6473) rss_mb | MB | 10 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6473) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6473) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6476) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6476) rss_mb | MB | 10 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6476) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6476) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6478) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6478) rss_mb | MB | 15 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6478) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6478) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6480) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6480) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6480) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6480) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6482) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6482) rss_mb | MB | 15 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6482) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6482) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6484) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6484) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6484) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6484) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6487) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6487) rss_mb | MB | 10 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6487) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6487) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6489) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6489) rss_mb | MB | 15 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6489) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6489) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6491) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6491) rss_mb | MB | 10 | 1.285 | 1.285 | 1.285 | 1.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6491) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6491) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6493) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6493) rss_mb | MB | 14 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6493) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6493) vms_mb | MB | 14 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6495) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6495) rss_mb | MB | 10 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6495) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6495) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6498) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6498) rss_mb | MB | 9 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6498) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6498) vms_mb | MB | 9 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6501) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6501) rss_mb | MB | 15 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6501) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6501) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6503) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6503) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6503) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6503) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6505) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6505) rss_mb | MB | 15 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6505) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6505) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6507) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6507) rss_mb | MB | 10 | 1.320 | 1.320 | 1.320 | 1.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6507) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6507) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6509) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6509) rss_mb | MB | 10 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6509) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6509) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6512) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6512) rss_mb | MB | 15 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6512) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6512) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6514) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6514) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6514) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6514) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6517) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6517) rss_mb | MB | 15 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6517) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6517) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6519) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6519) rss_mb | MB | 10 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6519) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6519) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6539) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6539) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6539) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6539) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6542) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6542) rss_mb | MB | 15 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6542) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6542) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6544) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6544) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6544) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6544) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6547) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6547) rss_mb | MB | 15 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6547) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6547) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6549) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6549) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6549) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6549) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6551) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6551) rss_mb | MB | 10 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6551) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6551) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6553) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6553) rss_mb | MB | 14 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6553) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6553) vms_mb | MB | 14 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6555) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6555) rss_mb | MB | 9 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6555) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6555) vms_mb | MB | 9 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6557) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6557) rss_mb | MB | 15 | 1.320 | 1.320 | 1.320 | 1.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6557) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6557) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6559) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6559) rss_mb | MB | 10 | 1.320 | 1.320 | 1.320 | 1.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6559) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6559) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6561) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6561) rss_mb | MB | 10 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6561) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6561) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6564) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6564) rss_mb | MB | 15 | 1.277 | 1.277 | 1.277 | 1.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6564) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6564) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6566) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6566) rss_mb | MB | 10 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6566) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6566) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6568) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6568) rss_mb | MB | 15 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6568) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6568) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6570) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6570) rss_mb | MB | 10 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6570) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6570) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6572) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6572) rss_mb | MB | 10 | 1.320 | 1.320 | 1.320 | 1.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6572) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6572) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6575) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6575) rss_mb | MB | 15 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6575) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6575) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6577) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6577) rss_mb | MB | 10 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6577) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6577) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6580) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6580) rss_mb | MB | 15 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6580) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6580) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6582) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6582) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6582) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6582) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6584) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6584) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6584) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6584) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6587) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6587) rss_mb | MB | 14 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6587) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6587) vms_mb | MB | 14 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6589) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6589) rss_mb | MB | 10 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6589) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6589) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6592) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6592) rss_mb | MB | 15 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6592) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6592) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6594) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6594) rss_mb | MB | 9 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6594) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6594) vms_mb | MB | 9 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6596) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6596) rss_mb | MB | 10 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6596) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6596) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6598) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6598) rss_mb | MB | 15 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6598) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6598) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6600) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6600) rss_mb | MB | 10 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6600) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6600) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6602) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6602) rss_mb | MB | 15 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6602) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6602) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6604) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6604) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6604) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6604) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6606) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6606) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6606) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6606) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6609) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6609) rss_mb | MB | 15 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6609) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6609) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6611) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6611) rss_mb | MB | 10 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6611) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6611) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6614) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6614) rss_mb | MB | 15 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6614) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6614) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6616) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6616) rss_mb | MB | 10 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6616) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6616) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6618) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6618) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6618) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6618) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6629) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6629) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6630) rss_mb | MB | 1 | 14.633 | 14.633 | 14.633 | 14.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6630) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6666) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6666) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6667) rss_mb | MB | 1 | 10.551 | 10.551 | 10.551 | 10.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6667) vms_mb | MB | 1 | 14.992 | 14.992 | 14.992 | 14.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6689) rss_mb | MB | 1 | 2.770 | 2.770 | 2.770 | 2.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6689) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6691) rss_mb | MB | 1 | 519.801 | 519.801 | 519.801 | 519.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6691) vms_mb | MB | 1 | 1670.922 | 1670.922 | 1670.922 | 1670.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6700) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6700) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6701) rss_mb | MB | 1 | 15.051 | 15.051 | 15.051 | 15.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6701) vms_mb | MB | 1 | 20.324 | 20.324 | 20.324 | 20.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6717) rss_mb | MB | 1 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6717) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6718) rss_mb | MB | 1 | 11.430 | 11.430 | 11.430 | 11.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6718) vms_mb | MB | 1 | 55.086 | 55.086 | 55.086 | 55.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6739) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6739) rss_mb | MB | 3 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6739) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6739) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6741) CPU | percent | 2 | 120.208 | 100.219 | 140.198 | 140.198 | 2.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6741) rss_mb | MB | 3 | 1163.014 | 7.602 | 2215.051 | 1266.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6741) main thread run-queue wait | percent | 2 | 18.129 | 8.094 | 28.165 | 28.165 | 0.364830 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6741) vms_mb | MB | 3 | 1380.402 | 11.922 | 2641.074 | 1488.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6772) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6772) rss_mb | MB | 11 | 2.629 | 2.629 | 2.629 | 2.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6772) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6772) vms_mb | MB | 11 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6773) CPU | percent | 10 | 160.963 | 92.048 | 176.559 | 170.999 | 16.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6773) rss_mb | MB | 11 | 1594.858 | 13.789 | 1953.492 | 1953.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6773) main thread run-queue wait | percent | 10 | 49.266 | 10.448 | 73.408 | 55.517 | 4.972754 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6773) vms_mb | MB | 11 | 1819.097 | 207.398 | 2173.578 | 2173.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6785) rss_mb | MB | 1 | 2.730 | 2.730 | 2.730 | 2.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6785) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6786) rss_mb | MB | 1 | 209.477 | 209.477 | 209.477 | 209.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 6786) vms_mb | MB | 1 | 409.273 | 409.273 | 409.273 | 409.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6801) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6801) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6802) rss_mb | MB | 1 | 10.523 | 10.523 | 10.523 | 10.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6802) vms_mb | MB | 1 | 14.992 | 14.992 | 14.992 | 14.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6810) rss_mb | MB | 1 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6810) vms_mb | MB | 1 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6812) rss_mb | MB | 1 | 118.461 | 118.461 | 118.461 | 118.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6812) vms_mb | MB | 1 | 124.043 | 124.043 | 124.043 | 124.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6825) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6825) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6833) CPU | percent | 299 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6833) rss_mb | MB | 300 | 2.867 | 2.867 | 2.867 | 2.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6833) main thread run-queue wait | percent | 299 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6833) vms_mb | MB | 300 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6834) CPU | percent | 299 | 160.061 | 18.118 | 192.615 | 150.186 | 492.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6834) rss_mb | MB | 300 | 5108.496 | 152.262 | 7140.609 | 4398.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6834) main thread run-queue wait | percent | 299 | 51.366 | 0.001 | 78.835 | 63.154 | 157.117911 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6834) vms_mb | MB | 300 | 5450.056 | 348.047 | 7378.203 | 5298.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6842) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6842) rss_mb | MB | 7 | 30.223 | 0.000 | 204.434 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6842) main thread run-queue wait | percent | 6 | 0.048 | 0.000 | 0.196 | 0.000 | 0.004148 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6842) vms_mb | MB | 7 | 787.568 | 0.500 | 5499.816 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6843) CPU | percent | 4 | 2.413 | 1.618 | 3.067 | 3.067 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6843) rss_mb | MB | 5 | 15.740 | 9.055 | 21.254 | 21.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6843) main thread run-queue wait | percent | 4 | 41.003 | 13.765 | 54.990 | 13.765 | 1.829558 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6843) vms_mb | MB | 5 | 21.122 | 13.492 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6857) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6857) rss_mb | MB | 4 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6857) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6857) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6858) CPU | percent | 3 | 2.594 | 0.850 | 3.955 | 2.979 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6858) rss_mb | MB | 4 | 10.423 | 0.000 | 18.035 | 18.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6858) main thread run-queue wait | percent | 3 | 47.142 | 32.820 | 55.253 | 55.253 | 1.482377 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6858) vms_mb | MB | 4 | 14.490 | 0.387 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6860) CPU | percent | 162 | 0.006 | 0.000 | 0.990 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6860) rss_mb | MB | 163 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6860) main thread run-queue wait | percent | 162 | 0.069 | 0.000 | 5.245 | 0.000 | 0.113063 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6860) vms_mb | MB | 163 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6861) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6861) rss_mb | MB | 3 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6861) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6861) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6863) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6863) rss_mb | MB | 3 | 1.137 | 1.137 | 1.137 | 1.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6863) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6863) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6864) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6864) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6864) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6864) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6865) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6865) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6865) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6865) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6866) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6866) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6866) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6866) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6867) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6867) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6867) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6867) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6868) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6868) rss_mb | MB | 3 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6868) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6868) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6869) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6869) rss_mb | MB | 3 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6869) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6869) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6870) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6870) rss_mb | MB | 3 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6870) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6870) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6871) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6871) rss_mb | MB | 3 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6871) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6871) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6872) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6872) rss_mb | MB | 3 | 1.344 | 1.344 | 1.344 | 1.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6872) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6872) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6873) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6873) rss_mb | MB | 3 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6873) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6873) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6874) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6874) rss_mb | MB | 3 | 1.285 | 1.285 | 1.285 | 1.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6874) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6874) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6875) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6875) rss_mb | MB | 3 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6875) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6875) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6876) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6876) rss_mb | MB | 3 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6876) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6876) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6877) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6877) rss_mb | MB | 3 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6877) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6877) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6878) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6878) rss_mb | MB | 3 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6878) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6878) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6879) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6879) rss_mb | MB | 3 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6879) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6879) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6880) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6880) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6880) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6880) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6881) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6881) rss_mb | MB | 3 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6881) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6881) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6882) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6882) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6882) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6882) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6884) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6884) rss_mb | MB | 4 | 1.090 | 0.926 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6884) main thread run-queue wait | percent | 3 | 0.067 | 0.000 | 0.200 | 0.000 | 0.002011 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6884) vms_mb | MB | 4 | 2.825 | 2.441 | 3.977 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6885) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6885) rss_mb | MB | 2 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6885) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6885) vms_mb | MB | 2 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6886) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6886) rss_mb | MB | 4 | 1.198 | 0.926 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6886) main thread run-queue wait | percent | 3 | 0.055 | 0.000 | 0.164 | 0.000 | 0.001654 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6886) vms_mb | MB | 4 | 2.825 | 2.441 | 3.977 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6887) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6887) rss_mb | MB | 3 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6887) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6887) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6906) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6906) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6906) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6906) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6907) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6907) rss_mb | MB | 3 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6907) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6907) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6908) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6908) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6908) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6908) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6909) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6909) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6909) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6909) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6910) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6910) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6910) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6910) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6911) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6911) rss_mb | MB | 3 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6911) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6911) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6912) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6912) rss_mb | MB | 3 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6912) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6912) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6914) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6914) rss_mb | MB | 3 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6914) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6914) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6915) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6915) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6915) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6915) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6916) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6916) rss_mb | MB | 3 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6916) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6916) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6918) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6918) rss_mb | MB | 3 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6918) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6918) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6919) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6919) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6919) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6919) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6920) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6920) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6920) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6920) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6921) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6921) rss_mb | MB | 3 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6921) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6921) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6924) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6924) rss_mb | MB | 3 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6924) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6924) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6925) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6925) rss_mb | MB | 3 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6925) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6925) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6926) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6926) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6926) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6926) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6927) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6927) rss_mb | MB | 3 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6927) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6927) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6928) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6928) rss_mb | MB | 3 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6928) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6928) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6929) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6929) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6929) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6929) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6930) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6930) rss_mb | MB | 3 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6930) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6930) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6931) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6931) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6931) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6931) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6932) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6932) rss_mb | MB | 3 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6932) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6932) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6933) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6933) rss_mb | MB | 3 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6933) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6933) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6935) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6935) rss_mb | MB | 15 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6935) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6935) vms_mb | MB | 15 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6959) rss_mb | MB | 1 | 2.777 | 2.777 | 2.777 | 2.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6959) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6960) rss_mb | MB | 1 | 169.723 | 169.723 | 169.723 | 169.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6960) vms_mb | MB | 1 | 366.117 | 366.117 | 366.117 | 366.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6992) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6992) rss_mb | MB | 2 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6992) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6992) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an1.py (PID 6994) CPU | percent | 1 | 140.626 | 140.626 | 140.626 | 140.626 | 1.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an1.py (PID 6994) rss_mb | MB | 2 | 544.350 | 54.172 | 1034.527 | 1034.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an1.py (PID 6994) main thread run-queue wait | percent | 1 | 24.763 | 24.763 | 24.763 | 24.763 | 0.250052 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an1.py (PID 6994) vms_mb | MB | 2 | 978.574 | 700.945 | 1256.203 | 1256.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7009) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7009) rss_mb | MB | 7 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7009) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7009) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7011) CPU | percent | 6 | 159.134 | 106.017 | 172.484 | 163.074 | 9.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7011) rss_mb | MB | 7 | 1969.157 | 61.988 | 3191.930 | 3191.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7011) main thread run-queue wait | percent | 6 | 42.218 | 2.375 | 53.639 | 45.285 | 2.550691 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7011) vms_mb | MB | 7 | 2312.731 | 255.148 | 4294.848 | 4294.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7031) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7031) rss_mb | MB | 2 | 2.719 | 2.719 | 2.719 | 2.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7031) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7031) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7032) CPU | percent | 1 | 94.324 | 94.324 | 94.324 | 94.324 | 0.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7032) rss_mb | MB | 2 | 592.008 | 13.988 | 1170.027 | 1170.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7032) main thread run-queue wait | percent | 1 | 5.640 | 5.640 | 5.640 | 5.640 | 0.056805 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7032) vms_mb | MB | 2 | 1251.607 | 207.465 | 2295.750 | 2295.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7047) rss_mb | MB | 1 | 2.891 | 2.891 | 2.891 | 2.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7047) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7057) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7057) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7058) rss_mb | MB | 1 | 8.969 | 8.969 | 8.969 | 8.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7058) vms_mb | MB | 1 | 13.410 | 13.410 | 13.410 | 13.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7105) CPU | percent | 156 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7105) rss_mb | MB | 157 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7105) main thread run-queue wait | percent | 156 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7105) vms_mb | MB | 157 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7106) CPU | percent | 156 | 169.319 | 148.127 | 176.938 | 174.000 | 266.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7106) rss_mb | MB | 157 | 1133.224 | 1069.594 | 1227.086 | 1138.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7106) main thread run-queue wait | percent | 156 | 54.722 | 37.520 | 78.345 | 51.358 | 86.011952 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7106) vms_mb | MB | 157 | 1408.837 | 1364.645 | 1670.953 | 1364.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7113) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7113) rss_mb | MB | 3 | 1.441 | 1.441 | 1.441 | 1.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7113) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7113) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7114) CPU | percent | 2 | 4.970 | 1.987 | 7.952 | 7.952 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7114) rss_mb | MB | 3 | 14.780 | 9.164 | 20.559 | 20.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7114) main thread run-queue wait | percent | 2 | 58.719 | 56.501 | 60.937 | 56.501 | 1.181738 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7114) vms_mb | MB | 3 | 19.714 | 13.492 | 25.633 | 25.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7119) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7119) rss_mb | MB | 3 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7119) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7119) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7120) CPU | percent | 2 | 5.962 | 3.970 | 7.954 | 7.954 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7120) rss_mb | MB | 3 | 14.176 | 6.363 | 21.391 | 21.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7120) main thread run-queue wait | percent | 2 | 43.632 | 41.270 | 45.993 | 41.270 | 0.878536 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7120) vms_mb | MB | 3 | 19.507 | 11.660 | 26.844 | 26.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7122) rss_mb | MB | 1 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7122) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 7123) rss_mb | MB | 1 | 8.164 | 8.164 | 8.164 | 8.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 7123) vms_mb | MB | 1 | 13.023 | 13.023 | 13.023 | 13.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7124) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7124) rss_mb | MB | 3 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7124) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7124) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7125) CPU | percent | 2 | 2.479 | 1.980 | 2.978 | 2.978 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7125) rss_mb | MB | 3 | 14.193 | 9.586 | 18.250 | 18.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7125) main thread run-queue wait | percent | 2 | 51.102 | 45.865 | 56.338 | 45.865 | 1.031092 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7125) vms_mb | MB | 3 | 19.296 | 13.617 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7195) rss_mb | MB | 1 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7195) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7196) rss_mb | MB | 1 | 14.836 | 14.836 | 14.836 | 14.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7196) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7202) rss_mb | MB | 1 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7202) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7203) rss_mb | MB | 1 | 20.348 | 20.348 | 20.348 | 20.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7203) vms_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7214) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7214) vms_mb | MB | 1 | 0.500 | 0.500 | 0.500 | 0.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7223) rss_mb | MB | 1 | 1.520 | 1.520 | 1.520 | 1.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7223) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7224) rss_mb | MB | 1 | 20.285 | 20.285 | 20.285 | 20.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7224) vms_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7229) rss_mb | MB | 1 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7229) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7230) rss_mb | MB | 1 | 9.715 | 9.715 | 9.715 | 9.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7230) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7231) rss_mb | MB | 1 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7231) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7233) rss_mb | MB | 1 | 162.863 | 162.863 | 162.863 | 162.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7233) vms_mb | MB | 1 | 356.648 | 356.648 | 356.648 | 356.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7243) rss_mb | MB | 1 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7243) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7246) CPU | percent | 599 | 0.008 | 0.000 | 1.989 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7246) rss_mb | MB | 600 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7246) main thread run-queue wait | percent | 599 | 0.000 | 0.000 | 0.004 | 0.000 | 0.000143 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7246) vms_mb | MB | 600 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7247) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7247) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7247) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7247) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7248) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7248) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7248) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7248) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7249) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7249) rss_mb | MB | 5 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7249) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7249) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7250) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7250) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7250) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7250) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7251) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7251) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7251) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7251) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7252) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7252) rss_mb | MB | 4 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7252) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7252) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7253) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7253) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7253) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7253) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7254) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7254) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7254) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7254) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7256) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7256) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7256) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7256) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7257) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7257) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7257) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7257) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7259) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7259) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7259) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7259) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7260) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7260) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7260) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7260) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7261) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7261) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7261) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7261) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7262) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7262) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7262) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7262) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7263) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7263) rss_mb | MB | 5 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7263) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7263) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7264) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7264) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7264) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7264) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7265) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7265) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7265) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7265) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7266) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7266) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7266) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7266) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7268) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7268) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7268) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7268) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7269) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7269) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7269) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7269) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7285) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7285) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7285) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7285) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7289) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7289) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7289) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7289) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7290) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7290) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7290) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7290) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7291) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7291) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7291) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7291) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7292) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7292) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7292) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7292) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7293) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7293) rss_mb | MB | 4 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7293) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7293) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7294) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7294) rss_mb | MB | 5 | 1.294 | 1.062 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7294) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7294) vms_mb | MB | 5 | 2.748 | 2.441 | 3.977 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7295) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7295) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7295) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7295) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7296) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7296) rss_mb | MB | 5 | 1.305 | 1.305 | 1.305 | 1.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7296) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7296) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7297) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7297) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7297) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7297) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7298) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7298) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7298) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7298) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7300) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7300) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7300) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7300) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7302) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7302) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7302) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7302) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7303) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7303) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7303) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7303) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7304) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7304) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7304) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7304) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7305) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7305) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7305) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7305) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7306) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7306) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7306) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7306) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7307) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7307) rss_mb | MB | 5 | 1.129 | 1.129 | 1.129 | 1.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7307) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7307) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7308) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7308) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7308) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7308) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7309) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7309) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7309) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7309) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7310) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7310) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7310) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7310) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7312) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7312) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7312) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7312) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7313) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7313) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7313) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7313) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7315) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7315) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7315) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7315) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7316) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7316) rss_mb | MB | 5 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7316) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7316) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7317) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7317) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7317) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7317) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7319) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7319) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7319) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7319) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7320) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7320) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7320) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7320) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7321) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7321) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7321) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7321) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7322) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7322) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7322) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7322) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7323) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7323) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7323) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7323) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7324) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7324) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7324) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7324) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7325) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7325) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7325) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7325) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7326) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7326) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7326) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7326) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7327) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7327) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7327) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7327) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7328) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7328) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7328) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7328) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7329) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7329) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7329) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7329) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7330) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7330) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7330) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7330) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7331) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7331) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7331) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7331) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7332) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7332) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7332) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7332) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7333) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7333) rss_mb | MB | 5 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7333) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7333) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7334) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7334) rss_mb | MB | 4 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7334) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7334) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7335) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7335) rss_mb | MB | 5 | 0.928 | 0.000 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7335) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7335) vms_mb | MB | 5 | 2.035 | 0.410 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7336) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7336) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7336) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7336) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7338) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7338) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7338) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7338) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7339) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7339) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7339) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7339) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7340) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7340) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7340) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7340) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7341) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7341) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7341) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7341) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7342) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7342) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7342) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7342) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7343) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7343) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7343) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7343) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7344) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7344) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7344) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7344) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7345) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7345) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7345) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7345) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7346) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7346) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7346) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7346) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7347) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7347) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7347) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7347) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7348) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7348) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7348) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7348) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7350) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7350) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7350) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7350) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7351) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7351) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7351) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7351) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7352) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7352) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7352) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7352) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7354) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7354) rss_mb | MB | 5 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7354) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7354) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7355) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7355) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7355) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7355) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7374) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7374) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7374) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7374) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7375) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7375) rss_mb | MB | 5 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7375) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7375) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7376) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7376) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7376) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7376) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7377) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7377) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7377) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7377) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7378) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7378) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7378) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7378) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7379) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7379) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7379) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7379) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7380) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7380) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7380) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7380) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7382) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7382) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7382) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7382) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7383) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7383) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7383) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7383) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7384) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7384) rss_mb | MB | 5 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7384) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7384) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7386) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7386) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7386) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7386) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7387) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7387) rss_mb | MB | 5 | 1.215 | 1.215 | 1.215 | 1.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7387) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7387) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7388) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7388) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7388) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7388) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7389) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7389) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7389) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7389) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7390) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7390) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7390) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7390) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7391) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7391) rss_mb | MB | 5 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7391) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7391) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7392) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7392) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7392) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7392) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7394) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7394) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7394) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7394) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7395) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7395) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7395) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7395) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7397) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7397) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7397) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7397) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7398) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7398) rss_mb | MB | 5 | 1.344 | 1.344 | 1.344 | 1.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7398) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7398) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7399) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7399) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7399) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7399) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7400) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7400) rss_mb | MB | 5 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7400) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7400) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7401) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7401) rss_mb | MB | 5 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7401) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7401) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7402) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7402) rss_mb | MB | 5 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7402) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7402) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7403) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7403) rss_mb | MB | 5 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7403) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7403) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7404) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7404) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7404) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7404) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7405) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7405) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7405) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7405) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7407) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7407) rss_mb | MB | 4 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7407) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7407) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7408) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7408) rss_mb | MB | 4 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7408) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7408) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7409) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7409) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7409) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7409) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7410) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7410) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7410) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7410) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7412) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7412) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7412) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7412) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7413) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7413) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7413) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7413) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7414) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7414) rss_mb | MB | 5 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7414) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7414) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7416) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7416) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7416) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7416) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7417) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7417) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7417) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7417) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7419) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7419) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7419) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7419) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7420) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7420) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7420) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7420) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7421) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7421) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7421) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7421) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7429) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7429) rss_mb | MB | 4 | 1.305 | 1.305 | 1.305 | 1.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7429) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7429) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7433) rss_mb | MB | 1 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7433) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7434) rss_mb | MB | 1 | 10.082 | 10.082 | 10.082 | 10.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7434) vms_mb | MB | 1 | 14.992 | 14.992 | 14.992 | 14.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7435) rss_mb | MB | 1 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7435) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7436) rss_mb | MB | 1 | 13.684 | 13.684 | 13.684 | 13.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7436) vms_mb | MB | 1 | 19.836 | 19.836 | 19.836 | 19.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7461) CPU | percent | 55 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7461) rss_mb | MB | 56 | 3.020 | 3.020 | 3.020 | 3.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7461) main thread run-queue wait | percent | 55 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7461) vms_mb | MB | 56 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_ds.py (PID 7463) CPU | percent | 55 | 163.989 | 67.625 | 176.055 | 170.035 | 90.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_ds.py (PID 7463) rss_mb | MB | 56 | 4009.729 | 118.062 | 5088.520 | 3222.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_ds.py (PID 7463) main thread run-queue wait | percent | 55 | 50.345 | 0.035 | 74.380 | 71.542 | 27.902410 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_ds.py (PID 7463) vms_mb | MB | 56 | 4307.056 | 311.824 | 6088.367 | 3551.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7478) CPU | percent | 56 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7478) rss_mb | MB | 57 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7478) main thread run-queue wait | percent | 56 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7478) vms_mb | MB | 57 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_ds.py (PID 7480) CPU | percent | 56 | 162.899 | 68.584 | 175.196 | 101.562 | 91.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_ds.py (PID 7480) rss_mb | MB | 57 | 3945.651 | 58.328 | 5157.219 | 1309.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_ds.py (PID 7480) main thread run-queue wait | percent | 56 | 50.245 | 0.039 | 75.246 | 24.344 | 28.336132 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_ds.py (PID 7480) vms_mb | MB | 57 | 4198.583 | 270.414 | 6027.797 | 1531.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7513) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7513) rss_mb | MB | 15 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7513) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7513) vms_mb | MB | 15 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7515) CPU | percent | 14 | 167.070 | 146.869 | 172.826 | 168.695 | 23.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7515) rss_mb | MB | 15 | 460.910 | 13.410 | 635.945 | 325.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7515) main thread run-queue wait | percent | 14 | 49.250 | 38.066 | 74.333 | 52.773 | 6.949880 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7515) vms_mb | MB | 15 | 672.930 | 207.262 | 848.898 | 538.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7673) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7673) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7674) rss_mb | MB | 1 | 21.484 | 21.484 | 21.484 | 21.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7674) vms_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7698) CPU | percent | 122 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7698) rss_mb | MB | 123 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7698) main thread run-queue wait | percent | 122 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7698) vms_mb | MB | 123 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7699) CPU | percent | 122 | 155.111 | 6.860 | 178.306 | 70.217 | 191.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7699) rss_mb | MB | 123 | 3717.100 | 13.199 | 5780.781 | 383.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7699) main thread run-queue wait | percent | 122 | 46.343 | 0.001 | 78.206 | 29.124 | 57.147062 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7699) vms_mb | MB | 123 | 4018.689 | 207.219 | 6171.910 | 606.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7859) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7859) rss_mb | MB | 5 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7859) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7859) vms_mb | MB | 5 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7860) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7860) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7860) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7860) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7872) rss_mb | MB | 1 | 2.691 | 2.691 | 2.691 | 2.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7872) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7873) rss_mb | MB | 1 | 21.586 | 21.586 | 21.586 | 21.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7873) vms_mb | MB | 1 | 213.711 | 213.711 | 213.711 | 213.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7893) rss_mb | MB | 1 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7893) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7894) rss_mb | MB | 1 | 3.836 | 3.836 | 3.836 | 3.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7894) vms_mb | MB | 1 | 9.633 | 9.633 | 9.633 | 9.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7904) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7904) rss_mb | MB | 2 | 2.902 | 2.902 | 2.902 | 2.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7904) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7904) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7905) CPU | percent | 1 | 86.090 | 86.090 | 86.090 | 86.090 | 0.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7905) rss_mb | MB | 2 | 359.414 | 18.238 | 700.590 | 700.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7905) main thread run-queue wait | percent | 1 | 3.475 | 3.475 | 3.475 | 3.475 | 0.035119 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7905) vms_mb | MB | 2 | 553.141 | 211.121 | 895.160 | 895.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7921) CPU | percent | 87 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7921) rss_mb | MB | 88 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7921) main thread run-queue wait | percent | 87 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7921) vms_mb | MB | 88 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7922) CPU | percent | 87 | 168.394 | 146.154 | 179.496 | 164.525 | 147.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7922) rss_mb | MB | 88 | 1243.169 | 113.449 | 1502.422 | 113.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7922) main thread run-queue wait | percent | 87 | 50.761 | 34.687 | 77.442 | 48.118 | 44.491815 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7922) vms_mb | MB | 88 | 1458.713 | 333.211 | 1714.719 | 333.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7945) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7945) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7947) rss_mb | MB | 1 | 18.828 | 18.828 | 18.828 | 18.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7947) vms_mb | MB | 1 | 24.605 | 24.605 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7953) rss_mb | MB | 1 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7953) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7954) rss_mb | MB | 1 | 14.699 | 14.699 | 14.699 | 14.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7954) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7960) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7960) rss_mb | MB | 5 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7960) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7960) vms_mb | MB | 5 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7961) CPU | percent | 4 | 151.757 | 92.346 | 176.709 | 171.118 | 6.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7961) rss_mb | MB | 5 | 1564.777 | 41.855 | 2656.469 | 1771.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7961) main thread run-queue wait | percent | 4 | 35.428 | 0.023 | 49.171 | 49.171 | 1.426204 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7961) vms_mb | MB | 5 | 1816.895 | 253.633 | 3038.145 | 1994.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7973) CPU | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7973) rss_mb | MB | 25 | 2.645 | 2.645 | 2.645 | 2.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7973) main thread run-queue wait | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7973) vms_mb | MB | 25 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7974) CPU | percent | 24 | 167.212 | 115.997 | 177.763 | 171.986 | 40.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7974) rss_mb | MB | 25 | 1723.082 | 229.273 | 2204.652 | 1722.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7974) main thread run-queue wait | percent | 24 | 48.722 | 13.694 | 72.864 | 51.211 | 11.788748 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 7974) vms_mb | MB | 25 | 1995.728 | 840.695 | 2782.266 | 1944.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7986) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7986) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7987) rss_mb | MB | 1 | 8.031 | 8.031 | 8.031 | 8.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7987) vms_mb | MB | 1 | 12.926 | 12.926 | 12.926 | 12.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8023) CPU | percent | 209 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8023) rss_mb | MB | 210 | 2.751 | 2.680 | 2.805 | 2.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8023) main thread run-queue wait | percent | 209 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8023) vms_mb | MB | 210 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_neg.py (PID 8025) CPU | percent | 209 | 81.177 | 0.990 | 179.717 | 1.979 | 174.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_neg.py (PID 8025) rss_mb | MB | 210 | 7892.189 | 217.672 | 10638.871 | 9562.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_neg.py (PID 8025) main thread run-queue wait | percent | 209 | 20.090 | 0.000 | 78.305 | 0.023 | 42.651772 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_neg.py (PID 8025) vms_mb | MB | 210 | 10500.569 | 841.766 | 17725.734 | 17555.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 8053) rss_mb | MB | 1 | 238.824 | 238.824 | 238.824 | 238.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 8053) vms_mb | MB | 1 | 5499.816 | 5499.816 | 5499.816 | 5499.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8069) CPU | percent | 60 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8069) rss_mb | MB | 61 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8069) main thread run-queue wait | percent | 60 | 0.008 | 0.000 | 0.469 | 0.000 | 0.004741 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8069) vms_mb | MB | 61 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8070) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8070) rss_mb | MB | 5 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8070) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8070) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8072) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8072) rss_mb | MB | 5 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8072) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8072) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8073) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8073) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8073) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8073) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8075) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8075) rss_mb | MB | 4 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8075) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8075) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8076) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8076) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8076) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8076) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8152) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8152) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8152) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8152) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8153) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8153) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8153) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8153) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8156) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8156) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8156) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8156) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8157) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8157) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8157) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8157) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8158) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8158) rss_mb | MB | 4 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8158) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8158) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8159) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8159) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8159) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8159) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8161) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8161) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8161) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8161) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8162) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8162) rss_mb | MB | 3 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8162) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8162) vms_mb | MB | 3 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8164) rss_mb | MB | 1 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8164) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8165) rss_mb | MB | 1 | 21.492 | 21.492 | 21.492 | 21.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8165) vms_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8185) CPU | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8185) rss_mb | MB | 20 | 2.855 | 2.855 | 2.855 | 2.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8185) main thread run-queue wait | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8185) vms_mb | MB | 20 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8186) CPU | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8186) rss_mb | MB | 20 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8186) main thread run-queue wait | percent | 19 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8186) vms_mb | MB | 20 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8223) rss_mb | MB | 1 | 1.594 | 1.594 | 1.594 | 1.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8223) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8224) rss_mb | MB | 1 | 16.953 | 16.953 | 16.953 | 16.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8224) vms_mb | MB | 1 | 22.066 | 22.066 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8232) CPU | percent | 114 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8232) rss_mb | MB | 115 | 2.832 | 2.832 | 2.832 | 2.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8232) main thread run-queue wait | percent | 114 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8232) vms_mb | MB | 115 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8234) CPU | percent | 114 | 165.020 | 13.930 | 176.499 | 171.079 | 189.530000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8234) rss_mb | MB | 115 | 1647.943 | 124.137 | 2014.348 | 1085.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8234) main thread run-queue wait | percent | 114 | 51.456 | 0.010 | 80.322 | 51.883 | 59.097041 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8234) vms_mb | MB | 115 | 1872.211 | 333.016 | 2226.809 | 1298.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8253) CPU | percent | 105 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8253) rss_mb | MB | 106 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8253) main thread run-queue wait | percent | 105 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8253) vms_mb | MB | 106 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8254) CPU | percent | 105 | 171.189 | 150.133 | 199.732 | 161.547 | 181.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8254) rss_mb | MB | 106 | 1886.250 | 962.477 | 2213.594 | 1419.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8254) main thread run-queue wait | percent | 105 | 52.499 | 36.723 | 73.985 | 52.899 | 55.518668 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8254) vms_mb | MB | 106 | 2106.888 | 1229.402 | 2426.035 | 1631.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8279) CPU | percent | 214 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8279) rss_mb | MB | 215 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8279) main thread run-queue wait | percent | 214 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8279) vms_mb | MB | 215 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8281) CPU | percent | 214 | 168.816 | 141.247 | 179.269 | 173.842 | 364.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8281) rss_mb | MB | 215 | 2183.293 | 550.617 | 2393.410 | 727.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8281) main thread run-queue wait | percent | 214 | 53.093 | 24.690 | 78.572 | 72.677 | 114.521112 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8281) vms_mb | MB | 215 | 2404.579 | 747.840 | 2605.785 | 939.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8318) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8318) rss_mb | MB | 3 | 1.453 | 1.453 | 1.453 | 1.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8318) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8318) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8319) CPU | percent | 2 | 1.973 | 1.964 | 1.983 | 1.983 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8319) rss_mb | MB | 3 | 11.111 | 7.586 | 15.449 | 15.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8319) main thread run-queue wait | percent | 2 | 62.824 | 60.759 | 64.888 | 60.759 | 1.273574 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8319) vms_mb | MB | 3 | 15.781 | 11.926 | 20.426 | 20.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8327) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8327) rss_mb | MB | 4 | 1.512 | 1.512 | 1.512 | 1.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8327) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8327) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8328) CPU | percent | 3 | 2.649 | 1.983 | 2.982 | 2.982 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8328) rss_mb | MB | 4 | 12.562 | 7.543 | 18.145 | 18.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8328) main thread run-queue wait | percent | 3 | 53.463 | 50.224 | 59.830 | 59.830 | 1.615056 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8328) vms_mb | MB | 4 | 17.438 | 11.926 | 24.148 | 24.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8329) rss_mb | MB | 1 | 2.535 | 2.535 | 2.535 | 2.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8329) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8331) rss_mb | MB | 1 | 1.410 | 1.410 | 1.410 | 1.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8331) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8332) rss_mb | MB | 1 | 18.617 | 18.617 | 18.617 | 18.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8332) vms_mb | MB | 1 | 24.605 | 24.605 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8337) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8337) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8338) rss_mb | MB | 1 | 21.512 | 21.512 | 21.512 | 21.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8338) vms_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8339) CPU | percent | 130 | 0.008 | 0.000 | 0.990 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8339) rss_mb | MB | 131 | 2.652 | 2.652 | 2.652 | 2.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8339) main thread run-queue wait | percent | 130 | 0.108 | 0.000 | 5.505 | 0.000 | 0.141380 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8339) vms_mb | MB | 131 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 8340) rss_mb | MB | 1 | 2.578 | 2.578 | 2.578 | 2.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 8340) vms_mb | MB | 1 | 283.352 | 283.352 | 283.352 | 283.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8341) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8341) rss_mb | MB | 4 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8341) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8341) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8342) rss_mb | MB | 1 | 1.656 | 1.656 | 1.656 | 1.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8342) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8343) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8343) rss_mb | MB | 5 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8343) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8343) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8345) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8345) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8345) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8345) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8347) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8347) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8347) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8347) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8350) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8350) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8350) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8350) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8353) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8353) rss_mb | MB | 5 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8353) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8353) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8355) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8355) rss_mb | MB | 5 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8355) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8355) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8358) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8358) rss_mb | MB | 5 | 1.246 | 1.246 | 1.246 | 1.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8358) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8358) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8360) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8360) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8360) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8360) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8362) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8362) rss_mb | MB | 5 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8362) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8362) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8365) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8365) rss_mb | MB | 5 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8365) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8365) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8367) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8367) rss_mb | MB | 5 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8367) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8367) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8369) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8369) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8369) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8369) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8371) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8371) rss_mb | MB | 5 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8371) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8371) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8376) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8376) rss_mb | MB | 60 | 1.258 | 1.258 | 1.258 | 1.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8376) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 8376) vms_mb | MB | 60 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8429) rss_mb | MB | 1 | 1.387 | 1.387 | 1.387 | 1.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8429) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8430) rss_mb | MB | 1 | 16.852 | 16.852 | 16.852 | 16.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8430) vms_mb | MB | 1 | 22.066 | 22.066 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8474) CPU | percent | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8474) rss_mb | MB | 29 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8474) main thread run-queue wait | percent | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8474) vms_mb | MB | 29 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — make_adapter.py (PID 8476) CPU | percent | 28 | 166.657 | 93.642 | 178.493 | 163.647 | 47.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — make_adapter.py (PID 8476) rss_mb | MB | 29 | 4746.288 | 140.684 | 5181.918 | 3930.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — make_adapter.py (PID 8476) main thread run-queue wait | percent | 28 | 48.703 | 0.012 | 77.291 | 45.712 | 13.736306 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — make_adapter.py (PID 8476) vms_mb | MB | 29 | 4984.041 | 333.973 | 5394.430 | 4143.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8512) rss_mb | MB | 1 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8512) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8513) rss_mb | MB | 1 | 14.797 | 14.797 | 14.797 | 14.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8513) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8525) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8525) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8526) rss_mb | MB | 1 | 21.469 | 21.469 | 21.469 | 21.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8526) vms_mb | MB | 1 | 26.902 | 26.902 | 26.902 | 26.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8534) rss_mb | MB | 1 | 2.672 | 2.672 | 2.672 | 2.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8534) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8535) rss_mb | MB | 1 | 692.660 | 692.660 | 692.660 | 692.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8535) vms_mb | MB | 1 | 898.449 | 898.449 | 898.449 | 898.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8548) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8548) rss_mb | MB | 2 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8548) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8548) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8549) CPU | percent | 1 | 128.331 | 128.331 | 128.331 | 128.331 | 1.300000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8549) rss_mb | MB | 2 | 426.777 | 21.332 | 832.223 | 832.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8549) main thread run-queue wait | percent | 1 | 31.826 | 31.826 | 31.826 | 31.826 | 0.322400 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8549) vms_mb | MB | 2 | 634.006 | 213.703 | 1054.309 | 1054.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8560) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8560) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8561) rss_mb | MB | 1 | 7.535 | 7.535 | 7.535 | 7.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8561) vms_mb | MB | 1 | 11.926 | 11.926 | 11.926 | 11.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8563) CPU | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8563) rss_mb | MB | 25 | 2.988 | 2.988 | 2.988 | 2.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8563) main thread run-queue wait | percent | 24 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8563) vms_mb | MB | 25 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8565) CPU | percent | 24 | 170.033 | 154.664 | 174.170 | 171.980 | 41.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8565) rss_mb | MB | 25 | 2848.534 | 808.977 | 3265.887 | 1383.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8565) main thread run-queue wait | percent | 24 | 57.537 | 32.876 | 73.718 | 55.354 | 13.902857 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8565) vms_mb | MB | 25 | 3061.478 | 1044.867 | 3478.297 | 1595.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8578) rss_mb | MB | 1 | 1.512 | 1.512 | 1.512 | 1.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8578) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8579) rss_mb | MB | 1 | 21.117 | 21.117 | 21.117 | 21.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8579) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8582) CPU | percent | 146 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8582) rss_mb | MB | 147 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8582) main thread run-queue wait | percent | 146 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8582) vms_mb | MB | 147 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8584) CPU | percent | 146 | 169.637 | 139.372 | 177.144 | 170.754 | 249.560000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8584) rss_mb | MB | 147 | 2324.872 | 932.598 | 2648.762 | 1722.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8584) main thread run-queue wait | percent | 146 | 53.386 | 39.364 | 78.625 | 49.737 | 78.541195 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8584) vms_mb | MB | 147 | 2544.390 | 1156.055 | 2860.422 | 1934.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8609) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8609) rss_mb | MB | 2 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8609) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8609) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8610) CPU | percent | 1 | 8.884 | 8.884 | 8.884 | 8.884 | 0.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8610) rss_mb | MB | 2 | 13.033 | 7.223 | 18.844 | 18.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8610) main thread run-queue wait | percent | 1 | 59.551 | 59.551 | 59.551 | 59.551 | 0.603284 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8610) vms_mb | MB | 2 | 18.197 | 11.789 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8618) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8618) rss_mb | MB | 4 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8618) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8618) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8619) CPU | percent | 3 | 2.638 | 1.975 | 3.964 | 3.964 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8619) rss_mb | MB | 4 | 12.281 | 7.000 | 18.105 | 18.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8619) main thread run-queue wait | percent | 3 | 47.806 | 35.370 | 61.465 | 35.370 | 1.451054 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8619) vms_mb | MB | 4 | 17.316 | 11.660 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8665) CPU | percent | 65 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8665) rss_mb | MB | 66 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8665) main thread run-queue wait | percent | 65 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8665) vms_mb | MB | 66 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_neg2.py (PID 8667) CPU | percent | 65 | 162.679 | 103.382 | 174.619 | 170.996 | 106.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_neg2.py (PID 8667) rss_mb | MB | 66 | 3145.902 | 773.508 | 4679.008 | 4603.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_neg2.py (PID 8667) main thread run-queue wait | percent | 65 | 49.766 | 13.719 | 74.558 | 73.577 | 32.575530 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_neg2.py (PID 8667) vms_mb | MB | 66 | 3404.068 | 1556.992 | 5155.270 | 4825.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8794) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8794) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8795) rss_mb | MB | 1 | 8.902 | 8.902 | 8.902 | 8.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8795) vms_mb | MB | 1 | 13.410 | 13.410 | 13.410 | 13.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8862) rss_mb | MB | 1 | 1.387 | 1.387 | 1.387 | 1.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8862) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8863) rss_mb | MB | 1 | 15.148 | 15.148 | 15.148 | 15.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8863) vms_mb | MB | 1 | 20.324 | 20.324 | 20.324 | 20.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8873) CPU | percent | 178 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8873) rss_mb | MB | 179 | 2.848 | 2.848 | 2.848 | 2.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8873) main thread run-queue wait | percent | 178 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8873) vms_mb | MB | 179 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8875) CPU | percent | 178 | 169.847 | 117.670 | 176.821 | 172.246 | 304.570000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8875) rss_mb | MB | 179 | 2656.373 | 13.137 | 3106.863 | 1347.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8875) main thread run-queue wait | percent | 178 | 53.981 | 13.095 | 78.631 | 51.980 | 96.800971 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 8875) vms_mb | MB | 179 | 2872.013 | 207.219 | 3318.137 | 1558.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9125) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9125) rss_mb | MB | 2 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9125) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9125) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9126) CPU | percent | 1 | 6.944 | 6.944 | 6.944 | 6.944 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9126) rss_mb | MB | 2 | 13.082 | 7.668 | 18.496 | 18.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9126) main thread run-queue wait | percent | 1 | 50.358 | 50.358 | 50.358 | 50.358 | 0.507628 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9126) vms_mb | MB | 2 | 18.090 | 11.926 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9132) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9132) rss_mb | MB | 5 | 1.387 | 1.387 | 1.387 | 1.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9132) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9132) vms_mb | MB | 5 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9133) CPU | percent | 4 | 3.229 | 1.984 | 6.958 | 6.958 | 0.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9133) rss_mb | MB | 5 | 13.730 | 7.246 | 21.012 | 21.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9133) main thread run-queue wait | percent | 4 | 56.164 | 47.028 | 61.530 | 47.028 | 2.261421 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9133) vms_mb | MB | 5 | 18.841 | 11.789 | 26.840 | 26.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9135) CPU | percent | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9135) rss_mb | MB | 46 | 2.770 | 2.770 | 2.770 | 2.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9135) main thread run-queue wait | percent | 45 | 0.179 | 0.000 | 4.956 | 0.000 | 0.081012 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9135) vms_mb | MB | 46 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9138) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9138) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9138) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9138) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9141) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9141) rss_mb | MB | 5 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9141) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9141) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9144) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9144) rss_mb | MB | 5 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9144) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9144) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9147) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9147) rss_mb | MB | 5 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9147) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9147) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9150) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9150) rss_mb | MB | 6 | 1.145 | 0.617 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9150) main thread run-queue wait | percent | 5 | 0.030 | 0.000 | 0.151 | 0.000 | 0.001521 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9150) vms_mb | MB | 6 | 2.697 | 2.441 | 3.977 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9154) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9154) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9154) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9154) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9157) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9157) rss_mb | MB | 5 | 1.223 | 1.223 | 1.223 | 1.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9157) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9157) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9160) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9160) rss_mb | MB | 5 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9160) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9160) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9164) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9164) rss_mb | MB | 5 | 1.273 | 1.273 | 1.273 | 1.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9164) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 9164) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9183) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9183) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9184) rss_mb | MB | 1 | 15.027 | 15.027 | 15.027 | 15.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 9184) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9365) CPU | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9365) rss_mb | MB | 39 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9365) main thread run-queue wait | percent | 38 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9365) vms_mb | MB | 39 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_final.py (PID 9367) CPU | percent | 38 | 169.529 | 143.184 | 176.378 | 160.038 | 64.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_final.py (PID 9367) rss_mb | MB | 39 | 3633.189 | 599.734 | 4358.348 | 2544.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_final.py (PID 9367) main thread run-queue wait | percent | 38 | 52.951 | 32.293 | 77.633 | 42.926 | 20.277249 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build_final.py (PID 9367) vms_mb | MB | 39 | 3851.858 | 794.910 | 4569.871 | 2755.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9386) rss_mb | MB | 1 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9386) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9387) rss_mb | MB | 1 | 20.203 | 20.203 | 20.203 | 20.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9387) vms_mb | MB | 1 | 212.223 | 212.223 | 212.223 | 212.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9433) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9433) rss_mb | MB | 2 | 2.895 | 2.895 | 2.895 | 2.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9433) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 9433) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9434) CPU | percent | 1 | 174.786 | 174.786 | 174.786 | 174.786 | 1.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9434) rss_mb | MB | 2 | 115.004 | 114.305 | 115.703 | 115.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9434) main thread run-queue wait | percent | 1 | 49.502 | 49.502 | 49.502 | 49.502 | 0.501284 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 9434) vms_mb | MB | 2 | 333.793 | 333.793 | 333.793 | 333.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9461) rss_mb | MB | 1 | 1.582 | 1.582 | 1.582 | 1.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 9461) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude_lifecycle_hook.py (PID 9462) rss_mb | MB | 1 | 9.738 | 9.738 | 9.738 | 9.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude_lifecycle_hook.py (PID 9462) vms_mb | MB | 1 | 14.707 | 14.707 | 14.707 | 14.707 | n/a | n/a |
| docker inspect (PID 9474) rss_mb | MB | 1 | 29.656 | 29.656 | 29.656 | 29.656 | n/a | n/a |
| docker inspect (PID 9474) vms_mb | MB | 1 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker commit (PID 9491) CPU | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 9491) io read MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 9491) io write MB/s | MB/s | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 9491) rss_mb | MB | 24 | 30.086 | 30.086 | 30.086 | 30.086 | n/a | n/a |
| docker commit (PID 9491) main thread run-queue wait | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 9491) vms_mb | MB | 24 | 1771.516 | 1771.516 | 1771.516 | 1771.516 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 CPU | percent | 4745 | 100.143 | 0.000 | 275.897 | 0.000 | 4834.859491 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 4745 | 18.076 | 0.000 | 66.014 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 4745 | 25.063 | 0.000 | 92.841 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_full_pct | percent of wall time stalled | 4745 | 1.080 | 0.000 | 90.119 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_some_pct | percent of wall time stalled | 4745 | 1.152 | 0.000 | 92.311 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io read MB/s | MB/s | 4745 | 1.646 | 0.000 | 208.999 | 0.000 | 8184.062500 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io write MB/s | MB/s | 4745 | 1.727 | 0.000 | 346.217 | 0.000 | 9309.667969 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory | MB | 4746 | 2356.008 | 66.926 | 11306.398 | 1387.926 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_full_pct | percent of wall time stalled | 4745 | 0.566 | 0.000 | 96.377 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_some_pct | percent of wall time stalled | 4745 | 0.588 | 0.000 | 97.758 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net rx MB/s | MB/s | 4745 | 0.002 | 0.000 | 8.406 | 0.000 | 8.498790 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net tx MB/s | MB/s | 4745 | 0.000 | 0.000 | 0.005 | 0.000 | 0.046544 MB | n/a |
| workload total CPU | percent | 4748 | 10.231 | 1.541 | 158.757 | 15.526 | 496.148451 CPU seconds | n/a |
| workload total memory | MB | 4749 | 5849.074 | 2698.168 | 12958.270 | 4159.719 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
