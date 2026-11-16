# agprof summary

- Duration: **5010.744 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **82 calls**, 82 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1765.372 s total wait
- Tools: **91/91 completed**, 5 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **490505** at 1.966 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 4996370.909 / 4996370.909 ms |
| LLM latency p50 / p95 | 13168.874 / 74671.611 ms |
| LLM TTFT p50 / p95 | 5694.990 / 43858.681 ms |
| LLM input / output tokens | 180 / 175281 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 82 total, 82 succeeded, 0 failed, 0 interrupted |
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
| Bash | 69/69 | 64 | 5 | 0 | n/a | n/a |
| ToolSearch | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 7/7 | 7 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect_module_inputs | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 10/10 | 10 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 10.388% | 104.689% | 523.448 s | 6831.236 MB | 13415.910 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python3 | 3067 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 99.912% | 99.912% | 1.010 s | 54.279 MB | 82.457 MB | 66.166 MB | 98.152 MB | n/a MB | n/a MB |
| vllm | 2609 |  | 4969 | 0.479% | 9.876% | 24.240 s | 1470.961 MB | 1787.906 MB | 11028.303 MB | 11031.172 MB | 14.011719 MB | 0.121094 MB |
| python | 2604 |  | 4969 | 4.839% | 104.319% | 243.310 s | 2888.754 MB | 6996.465 MB | 16496.474 MB | 23107.656 MB | 246.511719 MB | 11748.507812 MB |
| docker-init | 2938 | sandbox_agent_lsb-claude_code_0000_0000 | 4954 | 0.002% | 0.995% | 0.110 s | 0.233 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 3061 | sandbox_agent_lsb-claude_code_0000_0000 | 4954 | 29.931% | 107.447% | 1494.460 s | 98.193 MB | 106.363 MB | 973.398 MB | 976.785 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 2718 |  | 4969 | 5.067% | 76.185% | 255.690 s | 1970.244 MB | 2342.070 MB | 21242.913 MB | 21243.180 MB | 73.582031 MB | 0.031250 MB |
| python | 2717 |  | 4969 | 0.000% | 0.000% | 0.000 s | 7.494 MB | 12.176 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| lsb_grid_worker | 1695 |  | 4969 | 0.000% | 0.000% | 0.000 s | 1.244 MB | 3.320 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| tail | 2969 | sandbox_agent_lsb-claude_code_0000_0000 | 4954 | 0.003% | 3.880% | 0.220 s | 0.615 MB | 1.570 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| claude | 3080 | sandbox_agent_lsb-claude_code_0000_0000 | 4925 | 2.862% | 63.673% | 142.050 s | 278.772 MB | 333.062 MB | 5499.810 MB | 5499.816 MB | n/a MB | n/a MB |
| python3 | 3126 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.738 MB | 16.738 MB | 22.066 MB | 22.066 MB | n/a MB | n/a MB |
| sh | 3125 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3171 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 25.016 MB | 25.016 MB | 217.531 MB | 217.531 MB | n/a MB | n/a MB |
| bash | 3166 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 3196 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.445 MB | 1.445 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3197 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.621 MB | 20.621 MB | 25.504 MB | 25.504 MB | n/a MB | n/a MB |
| python3 | 3257 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.285 MB | 18.285 MB | 24.098 MB | 24.098 MB | n/a MB | n/a MB |
| sh | 3256 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3267 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.863 MB | 17.863 MB | 209.988 MB | 209.988 MB | n/a MB | n/a MB |
| bash | 3265 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.805 MB | 2.805 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 3282 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.711 MB | 2.711 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 3293 | sandbox_agent_lsb-claude_code_0000_0000 | 367 | 0.005% | 0.990% | 0.020 s | 2.688 MB | 2.688 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 3296 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3507 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.234 MB | 1.234 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3510 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3513 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3516 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3520 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.320 MB | 1.320 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3523 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3527 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3530 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3534 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3537 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3540 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3543 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3546 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3550 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3553 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3556 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3560 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3563 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3567 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3571 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3574 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.277 MB | 1.277 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3578 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3581 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3584 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.285 MB | 1.285 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3588 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3665 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3668 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3671 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.266 MB | 1.266 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3674 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3677 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3699 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3702 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.289 MB | 1.289 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3705 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.242 MB | 1.242 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3709 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.160 MB | 1.160 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3713 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.352 MB | 1.352 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 3717 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.136 MB | 1.262 MB | 2.197 MB | 2.441 MB | n/a MB | n/a MB |
| python3 | 3824 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.516 MB | 18.516 MB | 24.254 MB | 24.254 MB | n/a MB | n/a MB |
| sh | 3823 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.461 MB | 1.461 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 3887 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.340 MB | 1.340 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3888 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.000 MB | 7.000 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| python3 | 3897 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.324 MB | 18.324 MB | 209.930 MB | 209.930 MB | n/a MB | n/a MB |
| bash | 3896 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.809 MB | 2.809 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 3910 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 69.483% | 69.483% | 0.700 s | 190.312 MB | 256.625 MB | 570.566 MB | 666.332 MB | n/a MB | n/a MB |
| bash | 3909 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.699 MB | 2.699 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 3922 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.477 MB | 20.477 MB | 25.246 MB | 25.246 MB | n/a MB | n/a MB |
| sh | 3921 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.492 MB | 1.492 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 3926 | sandbox_agent_lsb-claude_code_0000_0000 | 318 | 151.762% | 178.113% | 485.620 s | 5132.181 MB | 7096.641 MB | 5508.242 MB | 7351.320 MB | n/a MB | n/a MB |
| bash | 3923 | sandbox_agent_lsb-claude_code_0000_0000 | 318 | 0.000% | 0.000% | 0.000 s | 1.025 MB | 2.941 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 4104 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.230 MB | 9.230 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| sh | 4103 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.305 MB | 1.305 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 4116 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4117 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.047 MB | 7.047 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| bash | 4118 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.605 MB | 2.605 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4119 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 131.723 MB | 131.723 MB | 347.105 MB | 347.105 MB | n/a MB | n/a MB |
| python3 | 4136 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.578 MB | 20.578 MB | 212.516 MB | 212.516 MB | n/a MB | n/a MB |
| bash | 4135 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.703 MB | 2.703 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 4176 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.227 MB | 1.227 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4177 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.914 MB | 19.914 MB | 24.988 MB | 24.988 MB | n/a MB | n/a MB |
| python3 | 4188 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 143.852 MB | 143.852 MB | 150.039 MB | 150.039 MB | n/a MB | n/a MB |
| bash | 4185 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.754 MB | 2.754 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| sh | 4212 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4213 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.309 MB | 18.309 MB | 24.254 MB | 24.254 MB | n/a MB | n/a MB |
| python3 | 4218 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 149.086 MB | 149.086 MB | 154.973 MB | 154.973 MB | n/a MB | n/a MB |
| bash | 4216 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.797 MB | 2.797 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 4229 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 102.168% | 102.168% | 1.030 s | 93.682 MB | 173.848 MB | 287.072 MB | 366.746 MB | n/a MB | n/a MB |
| bash | 4228 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.859 MB | 2.859 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4300 | sandbox_agent_lsb-claude_code_0000_0000 | 131 | 149.956% | 179.518% | 198.170 s | 4899.055 MB | 5305.648 MB | 5179.964 MB | 5526.422 MB | n/a MB | n/a MB |
| sh | 4310 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.438 MB | 1.438 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4311 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 7.886% | 7.886% | 0.080 s | 18.359 MB | 20.797 MB | 23.766 MB | 25.762 MB | n/a MB | n/a MB |
| bash | 4344 | sandbox_agent_lsb-claude_code_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 1.504 MB | 2.754 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4345 | sandbox_agent_lsb-claude_code_0000_0000 | 17 | 14.501% | 35.507% | 2.350 s | 871.117 MB | 2193.371 MB | 1253.187 MB | 2640.984 MB | n/a MB | n/a MB |
| sh | 4415 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.375 MB | 1.375 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4416 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.953% | 5.918% | 0.120 s | 12.960 MB | 20.230 MB | 17.733 MB | 25.375 MB | n/a MB | n/a MB |
| sh | 4424 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.348 MB | 1.348 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 4425 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.789 MB | 7.789 MB | 12.926 MB | 12.926 MB | n/a MB | n/a MB |
| bash | 4429 | sandbox_agent_lsb-claude_code_0000_0000 | 44 | 0.000% | 0.000% | 0.000 s | 2.512 MB | 2.660 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 4431 | sandbox_agent_lsb-claude_code_0000_0000 | 44 | 59.790% | 134.630% | 26.260 s | 991.476 MB | 3029.855 MB | 1346.704 MB | 3262.852 MB | n/a MB | n/a MB |
| sh | 5745 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.363 MB | 1.363 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 5746 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 19.910 MB | 19.910 MB | 25.117 MB | 25.117 MB | n/a MB | n/a MB |
| sleep | 6015 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 6012 | sandbox_agent_lsb-claude_code_0000_0000 | 606 | 0.021% | 0.995% | 0.130 s | 2.629 MB | 2.629 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 6040 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6043 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6046 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6053 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6059 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6062 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.238 MB | 1.238 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6065 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6069 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6139 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6142 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6145 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6148 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6151 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6155 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6158 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6161 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6165 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6168 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6171 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6174 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6177 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6180 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6183 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6186 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6189 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6192 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6195 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6199 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6202 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6205 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6208 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6211 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6214 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6217 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6220 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6223 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6243 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6246 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6316 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6320 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6323 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6326 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6329 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6333 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6336 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6339 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6343 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6346 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6349 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6352 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6356 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6359 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6362 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6365 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6368 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6372 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6375 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6380 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6383 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6386 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6390 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6393 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6397 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6400 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| claude | 6403 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.164 MB | 6.164 MB | 1309.664 MB | 1309.664 MB | n/a MB | n/a MB |
| sleep | 6405 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 6474 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.260 MB | 1.297 MB | 2.748 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 6477 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6481 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6484 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6487 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6490 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6494 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6497 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6501 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6505 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6508 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.305 MB | 1.305 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6512 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6515 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6518 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6521 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6524 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6527 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6530 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6533 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6536 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6540 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.172 MB | 1.172 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6543 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6546 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6549 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6552 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6555 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6577 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6629 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6632 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6635 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.230 MB | 1.230 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6638 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6658 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6662 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6665 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6668 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6671 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6674 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6677 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6680 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6683 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6686 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6690 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.227 MB | 1.227 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6693 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6697 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6700 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6703 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6706 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6709 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6712 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6715 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6718 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6721 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6726 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6797 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6806 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 6826 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| python3 | 6834 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.156 MB | 20.156 MB | 25.117 MB | 25.117 MB | n/a MB | n/a MB |
| sh | 6833 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 6838 | sandbox_agent_lsb-claude_code_0000_0000 | 743 | 0.000% | 0.000% | 0.000 s | 2.742 MB | 2.742 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6839 | sandbox_agent_lsb-claude_code_0000_0000 | 743 | 166.078% | 177.281% | 1242.410 s | 5178.046 MB | 5485.402 MB | 5408.745 MB | 5705.055 MB | n/a MB | n/a MB |
| sh | 6851 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.457 MB | 1.457 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6852 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 4.640% | 6.961% | 0.140 s | 13.428 MB | 21.125 MB | 18.521 MB | 26.906 MB | n/a MB | n/a MB |
| python3 | 6856 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 5.953% | 16.895% | 0.360 s | 30.680 MB | 62.398 MB | 223.028 MB | 254.309 MB | n/a MB | n/a MB |
| bash | 6855 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.996 MB | 2.996 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 6861 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 5.931% | 5.931% | 0.060 s | 19.043 MB | 21.426 MB | 24.531 MB | 26.996 MB | n/a MB | n/a MB |
| sh | 6860 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6868 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.651% | 2.983% | 0.080 s | 12.701 MB | 18.273 MB | 17.505 MB | 24.254 MB | n/a MB | n/a MB |
| sh | 6867 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6875 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 7.912% | 7.912% | 0.080 s | 17.766 MB | 20.656 MB | 22.760 MB | 25.504 MB | n/a MB | n/a MB |
| sh | 6874 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.383 MB | 1.383 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 6948 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.465 MB | 1.465 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6949 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 3.977% | 5.968% | 0.080 s | 14.682 MB | 20.246 MB | 19.542 MB | 25.117 MB | n/a MB | n/a MB |
| python3 | 6952 | sandbox_agent_lsb-claude_code_0000_0000 | 58 | 46.670% | 106.404% | 26.860 s | 766.422 MB | 1253.363 MB | 1085.389 MB | 1565.219 MB | n/a MB | n/a MB |
| bash | 6950 | sandbox_agent_lsb-claude_code_0000_0000 | 58 | 0.000% | 0.000% | 0.000 s | 2.984 MB | 2.984 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 6975 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 6976 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 3.461% | 3.961% | 0.070 s | 12.132 MB | 18.527 MB | 17.174 MB | 24.605 MB | n/a MB | n/a MB |
| claude | 6988 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 291.160 MB | 291.160 MB | 5499.816 MB | 5499.816 MB | n/a MB | n/a MB |
| claude | 7067 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 73.670 MB | 290.918 MB | 1376.853 MB | 5499.816 MB | n/a MB | n/a MB |
| python3 | 7068 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 1.951% | 1.987% | 0.040 s | 13.327 MB | 16.887 MB | 18.478 MB | 22.105 MB | n/a MB | n/a MB |
| sleep | 7075 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7072 | sandbox_agent_lsb-claude_code_0000_0000 | 482 | 0.014% | 0.995% | 0.070 s | 2.699 MB | 2.699 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7077 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7079 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7081 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7085 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7087 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7089 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7091 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7093 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7095 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7098 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7100 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7103 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7105 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7107 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7109 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7113 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7115 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7120 | sandbox_agent_lsb-claude_code_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 1.007 MB | 1.156 MB | 2.697 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7122 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7124 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7126 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7129 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7131 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7152 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7264 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7267 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7269 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7272 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7274 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7276 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7278 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7279 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7280 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7282 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7284 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7286 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7288 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7290 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7292 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7295 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7297 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7299 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7318 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.316 MB | 1.316 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7320 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7322 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.172 MB | 1.172 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7324 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7326 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| claude | 7327 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 280.488 MB | 280.488 MB | n/a MB | n/a MB |
| sleep | 7328 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7330 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7331 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7333 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7335 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7404 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7406 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7408 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7410 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7412 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7414 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7416 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.145 MB | 1.145 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7418 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.254 MB | 1.254 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7421 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.332 MB | 1.332 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7422 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7423 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7424 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7425 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7429 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7431 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7433 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7436 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7438 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7440 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7442 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7445 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7448 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7450 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7452 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7454 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7455 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.316 MB | 1.316 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7457 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7459 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7461 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7464 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7466 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.207 MB | 1.207 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7468 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7470 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7472 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7474 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.297 MB | 1.297 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7479 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7481 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.164 MB | 1.164 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7483 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.168 MB | 1.168 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7484 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.504 MB | 1.504 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sleep | 7485 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7487 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.195 MB | 1.195 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7490 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7493 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.336 MB | 1.336 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7495 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7497 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.156 MB | 1.156 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7565 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.332 MB | 1.332 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7568 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.148 MB | 1.148 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sleep | 7571 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.312 MB | 1.312 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| sh | 7579 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.477 MB | 1.477 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7580 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.531 MB | 9.531 MB | 13.484 MB | 13.484 MB | n/a MB | n/a MB |
| bash | 7611 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.820 MB | 2.820 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7613 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.211 MB | 9.211 MB | 13.414 MB | 13.414 MB | n/a MB | n/a MB |
| python3 | 7633 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.223 MB | 20.223 MB | 24.988 MB | 24.988 MB | n/a MB | n/a MB |
| sh | 7632 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.434 MB | 1.434 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7664 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.184 MB | 16.184 MB | 21.770 MB | 21.770 MB | n/a MB | n/a MB |
| sh | 7663 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7686 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.508 MB | 1.508 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7687 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.766 MB | 9.766 MB | 13.617 MB | 13.617 MB | n/a MB | n/a MB |
| bash | 7695 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.957 MB | 2.957 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7697 | sandbox_agent_lsb-claude_code_0000_0000 | 3 | 99.442% | 99.481% | 2.000 s | 152.499 MB | 155.559 MB | 158.160 MB | 161.160 MB | n/a MB | n/a MB |
| sleep | 7740 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.262 MB | 1.262 MB | 2.441 MB | 2.441 MB | n/a MB | n/a MB |
| bash | 7739 | sandbox_agent_lsb-claude_code_0000_0000 | 145 | 0.000% | 0.000% | 0.000 s | 1.508 MB | 1.508 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7741 | sandbox_agent_lsb-claude_code_0000_0000 | 145 | 169.706% | 182.954% | 247.370 s | 4718.477 MB | 5167.738 MB | 4964.914 MB | 5387.215 MB | n/a MB | n/a MB |
| bash | 7737 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.711 MB | 2.711 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7751 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 15.766 MB | 15.766 MB | 20.527 MB | 20.527 MB | n/a MB | n/a MB |
| sh | 7750 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7760 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 7.896% | 7.896% | 0.080 s | 19.002 MB | 21.246 MB | 24.527 MB | 26.988 MB | n/a MB | n/a MB |
| sh | 7759 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.426 MB | 1.426 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7765 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.989% | 0.989% | 0.010 s | 8.174 MB | 9.168 MB | 12.523 MB | 13.258 MB | n/a MB | n/a MB |
| bash | 7764 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.883 MB | 2.883 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 7768 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 2.639% | 3.969% | 0.080 s | 11.375 MB | 18.887 MB | 15.222 MB | 24.605 MB | n/a MB | n/a MB |
| sh | 7767 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.469 MB | 1.469 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7792 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 3.967% | 6.947% | 0.120 s | 13.361 MB | 20.887 MB | 17.882 MB | 25.762 MB | n/a MB | n/a MB |
| sh | 7791 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 1.371 MB | 1.371 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 7814 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 1.484 MB | 1.484 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7815 | sandbox_agent_lsb-claude_code_0000_0000 | 5 | 3.728% | 7.952% | 0.150 s | 13.540 MB | 21.516 MB | 18.759 MB | 27.062 MB | n/a MB | n/a MB |
| sh | 7818 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.480 MB | 1.480 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7819 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.910 MB | 7.910 MB | 12.926 MB | 12.926 MB | n/a MB | n/a MB |
| sh | 7823 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.418 MB | 1.418 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7824 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.918 MB | 7.918 MB | 12.926 MB | 12.926 MB | n/a MB | n/a MB |
| python3 | 7844 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 24.676 MB | 24.676 MB | 216.188 MB | 216.188 MB | n/a MB | n/a MB |
| bash | 7842 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.836 MB | 2.836 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 7859 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.383 MB | 1.383 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7860 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.379 MB | 1.379 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| tail | 7887 | sandbox_agent_lsb-claude_code_0000_0000 | 139 | 0.000% | 0.000% | 0.000 s | 1.219 MB | 1.219 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 7884 | sandbox_agent_lsb-claude_code_0000_0000 | 139 | 0.000% | 0.000% | 0.000 s | 2.773 MB | 2.773 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7886 | sandbox_agent_lsb-claude_code_0000_0000 | 139 | 150.138% | 172.827% | 208.750 s | 807.635 MB | 1079.180 MB | 1049.621 MB | 1334.070 MB | n/a MB | n/a MB |
| python3 | 7925 | sandbox_agent_lsb-claude_code_0000_0000 | 17 | 165.814% | 178.962% | 26.750 s | 589.709 MB | 662.414 MB | 887.634 MB | 974.938 MB | n/a MB | n/a MB |
| bash | 7923 | sandbox_agent_lsb-claude_code_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7932 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.918 MB | 8.918 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| sh | 7931 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.430 MB | 1.430 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 7947 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 98.644% | 103.241% | 2.980 s | 638.112 MB | 1493.164 MB | 954.069 MB | 1716.570 MB | n/a MB | n/a MB |
| bash | 7943 | sandbox_agent_lsb-claude_code_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.934 MB | 2.934 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 7987 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.934 MB | 9.934 MB | 13.773 MB | 13.773 MB | n/a MB | n/a MB |
| sh | 7986 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.480 MB | 1.480 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| sh | 8017 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.586 MB | 1.586 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8018 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.406 MB | 14.406 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| python3 | 8041 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.598 MB | 21.598 MB | 26.996 MB | 26.996 MB | n/a MB | n/a MB |
| sh | 8040 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.480 MB | 1.480 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| bash | 8085 | sandbox_agent_lsb-claude_code_0000_0000 | 176 | 0.000% | 0.000% | 0.000 s | 2.812 MB | 2.812 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8087 | sandbox_agent_lsb-claude_code_0000_0000 | 176 | 170.564% | 182.666% | 301.460 s | 4648.988 MB | 5236.156 MB | 4881.333 MB | 5456.090 MB | n/a MB | n/a MB |
| python3 | 8120 | sandbox_agent_lsb-claude_code_0000_0000 | 100 | 146.814% | 174.374% | 146.400 s | 649.952 MB | 1044.438 MB | 895.826 MB | 1256.641 MB | n/a MB | n/a MB |
| tail | 8121 | sandbox_agent_lsb-claude_code_0000_0000 | 100 | 0.000% | 0.000% | 0.000 s | 1.203 MB | 1.203 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 8118 | sandbox_agent_lsb-claude_code_0000_0000 | 100 | 0.000% | 0.000% | 0.000 s | 2.934 MB | 2.934 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| bash | 8163 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.859 MB | 2.859 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 8165 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 137.618% | 175.248% | 12.480 s | 641.077 MB | 1369.047 MB | 974.609 MB | 1623.328 MB | n/a MB | n/a MB |
| python3 | 8188 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 145.985% | 171.082% | 8.810 s | 1461.185 MB | 2221.734 MB | 1700.764 MB | 2441.727 MB | n/a MB | n/a MB |
| tail | 8189 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 1.238 MB | 1.238 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 8186 | sandbox_agent_lsb-claude_code_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 3.016 MB | 3.016 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8207 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 137.274% | 174.274% | 12.460 s | 1511.033 MB | 1832.277 MB | 1778.063 MB | 2052.531 MB | n/a MB | n/a MB |
| bash | 8205 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.809 MB | 2.809 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| tail | 8208 | sandbox_agent_lsb-claude_code_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.176 MB | 1.176 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python3 | 8226 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 160.578% | 175.488% | 12.940 s | 1213.421 MB | 1500.168 MB | 1471.264 MB | 1700.371 MB | n/a MB | n/a MB |
| bash | 8224 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.941 MB | 2.941 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| tail | 8227 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.098 MB | 1.098 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 8282 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| python3 | 8284 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 162.815% | 172.995% | 11.470 s | 1187.250 MB | 1537.332 MB | 1426.493 MB | 1755.355 MB | n/a MB | n/a MB |
| tail | 8285 | sandbox_agent_lsb-claude_code_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| tail | 8305 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.137 MB | 1.137 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python3 | 8304 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 158.756% | 179.399% | 20.800 s | 2849.140 MB | 3487.098 MB | 3131.534 MB | 4071.059 MB | n/a MB | n/a MB |
| bash | 8302 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 2.949 MB | 2.949 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| sh | 8319 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.527 MB | 1.527 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8320 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.773 MB | 20.773 MB | 25.762 MB | 25.762 MB | n/a MB | n/a MB |
| bash | 8322 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 2.949 MB | 2.949 MB | 3.980 MB | 3.980 MB | n/a MB | n/a MB |
| tail | 8325 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 0.000% | 0.000% | 0.000 s | 1.043 MB | 1.043 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python3 | 8324 | sandbox_agent_lsb-claude_code_0000_0000 | 14 | 163.628% | 174.707% | 21.440 s | 2931.436 MB | 3472.293 MB | 3149.066 MB | 3689.977 MB | n/a MB | n/a MB |
| python3 | 8347 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 286.562 MB | 286.562 MB | 700.926 MB | 700.926 MB | n/a MB | n/a MB |
| tail | 8348 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.039 MB | 1.039 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| bash | 8345 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| date | 8355 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.285 MB | 0.285 MB | 2.395 MB | 2.395 MB | n/a MB | n/a MB |
| sh | 8363 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.512 MB | 1.512 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| python3 | 8364 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.527 MB | 20.527 MB | 25.375 MB | 25.375 MB | n/a MB | n/a MB |
| bash | 8367 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.785 MB | 2.785 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8369 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 20.849% | 40.663% | 1.680 s | 934.451 MB | 1347.332 MB | 1429.953 MB | 1629.867 MB | n/a MB | n/a MB |
| tail | 8370 | sandbox_agent_lsb-claude_code_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 1.180 MB | 1.180 MB | 2.473 MB | 2.473 MB | n/a MB | n/a MB |
| python3 | 8405 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 156.704% | 156.704% | 1.580 s | 711.676 MB | 1392.723 MB | 961.535 MB | 1670.871 MB | n/a MB | n/a MB |
| bash | 8404 | sandbox_agent_lsb-claude_code_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.852 MB | 2.852 MB | 3.977 MB | 3.977 MB | n/a MB | n/a MB |
| python3 | 8427 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.508 MB | 9.508 MB | 13.492 MB | 13.492 MB | n/a MB | n/a MB |
| sh | 8426 | sandbox_agent_lsb-claude_code_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.473 MB | 1.473 MB | 2.531 MB | 2.531 MB | n/a MB | n/a MB |
| docker | 8436 |  | 1 | n/a% | n/a% | n/a s | 8.109 MB | 8.109 MB | 69.133 MB | 69.133 MB | n/a MB | n/a MB |
| docker | 8461 |  | 23 | 0.000% | 0.000% | 0.000 s | 30.594 MB | 30.594 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 17.318% | 100.000% | 12142.429 MB | 14666.000 MB | 36.850 W | 77.582 W | 184723.407 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-claude_code_0000_0000 | 94.318% | 218.508% | 4713.469 s | 3248.065 MB | 8247.977 MB | 8915.167969 MB | 405.078125 MB | 8.503482 MB | 0.051820 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2826 | 5010.681 | interrupted |
| harness:retire | -1 | 2.416 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 4996.371 | n/a | n/a | 8915.168 | 4996370.909 | 4996370.909 | 4996370.909 |
| engine:execute | 1/1 | 0 | 0 | 4996.369 | 4.767 | 4991.200 | 8915.168 | 4996369.444 | 4996369.444 | 4996369.444 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 4968.534 | 0.003 | 4968.531 | 8915.038 | 4968533.845 | 4968533.845 | 4968533.845 |
| harness:await_cli | 1/1 | 0 | 0 | 4963.599 | n/a | n/a | 8909.826 | 4963598.850 | 4963598.850 | 4963598.850 |
| tool:Bash | 69/69 | 5 | 0 | 2529.631 | n/a | n/a | 7987.319 | 36661.325 | 835.189 | 264164.936 |
| llm:attempt | 82/82 | 0 | 0 | 1765.372 | 4.382 | 1760.957 | 789.720 | 21528.924 | 13168.874 | 74671.611 |
| tool:mcp__agency__generate | 7/7 | 0 | 0 | 317.602 | n/a | n/a | 9.443 | 45371.696 | 38351.495 | 104614.249 |
| tool:mcp__agency__trace | 10/10 | 0 | 0 | 232.812 | n/a | n/a | 5.865 | 23281.163 | 11648.860 | 77306.702 |
| run:container_call | 13/13 | 0 | 0 | 24.513 | 0.002 | 24.511 | 0.031 | 1885.651 | 54.131 | 9542.012 |
| teardown:commit | 1/1 | 0 | 0 | 24.090 | 0.004 | 24.085 | 0.031 | 24089.610 | 24089.610 | 24089.610 |
| sandbox:commit | 1/1 | 0 | 0 | 23.840 | 0.002 | 23.837 | 0.031 | 23839.776 | 23839.776 | 23839.776 |
| checkpoint.total | 1/1 | 0 | 0 | 23.840 | 0.002 | 23.837 | 0.031 | 23839.632 | 23839.632 | 23839.632 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 23.839 | 0.002 | 23.837 | 0.031 | 23839.477 | 23839.477 | 23839.477 |
| syscall:execve | 1302/1302 | 0 | 0 | 4.747 | n/a | n/a | 7.534 | 3.646 | 1.388 | 7.605 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.089 | 0.699 | 2.390 | 0.000 | 3089.420 | 3089.420 | 3089.420 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.089 | 0.699 | 2.390 | 0.000 | 3089.123 | 3089.123 | 3089.123 |
| syscall:sendto | 669/669 | 0 | 0 | 2.247 | n/a | n/a | 5.510 | 3.359 | 2.045 | 5.657 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.621 | n/a | n/a | 0.320 | 1620.675 | 1620.675 | 1620.675 |
| syscall:connect | 260/260 | 0 | 0 | 0.929 | n/a | n/a | 2.773 | 3.573 | 2.208 | 6.974 |
| tool:mcp__agency__inspect | 1/1 | 0 | 0 | 0.658 | n/a | n/a | 0.002 | 658.041 | 658.041 | 658.041 |
| harness:submit | 1/1 | 0 | 0 | 0.606 | n/a | n/a | 0.040 | 605.665 | 605.665 | 605.665 |
| tool:mcp__agency__inspect_module_inputs | 1/1 | 0 | 0 | 0.578 | n/a | n/a | 0.001 | 577.819 | 577.819 | 577.819 |
| sandbox:start | 1/1 | 0 | 0 | 0.357 | 0.002 | 0.355 | 0.000 | 356.970 | 356.970 | 356.970 |
| runtime.container_create | 1/1 | 0 | 0 | 0.357 | 0.002 | 0.355 | 0.000 | 356.817 | 356.817 | 356.817 |
| sandbox:create | 1/1 | 0 | 0 | 0.342 | 0.244 | 0.098 | 0.000 | 341.680 | 341.680 | 341.680 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.324 | n/a | n/a | 0.040 | 324.419 | 324.419 | 324.419 |
| sandbox:stop | 1/1 | 0 | 0 | 0.250 | 0.002 | 0.248 | 0.000 | 249.571 | 249.571 | 249.571 |
| tool:ToolSearch | 1/1 | 0 | 0 | 0.237 | n/a | n/a | 0.205 | 236.809 | 236.809 | 236.809 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.197 | n/a | n/a | 0.001 | 196.704 | 196.704 | 196.704 |
| agency:services_close | 1/1 | 0 | 0 | 0.180 | 0.001 | 0.180 | 0.093 | 180.228 | 180.228 | 180.228 |
| agency:services_start | 1/1 | 0 | 0 | 0.071 | 0.040 | 0.030 | 0.000 | 70.521 | 70.521 | 70.521 |
| run:detect | 1/1 | 0 | 0 | 0.060 | 0.001 | 0.060 | 0.000 | 60.341 | 60.341 | 60.341 |
| agent:create | 1/1 | 0 | 0 | 0.047 | 0.007 | 0.040 | 0.000 | 47.301 | 47.301 | 47.301 |
| harness:launch | 1/1 | 0 | 0 | 0.046 | n/a | n/a | 0.000 | 45.774 | 45.774 | 45.774 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.002 | 4.284 | 4.284 | 4.284 |
| harness:snapshot | 1/1 | 0 | 0 | 0.004 | n/a | n/a | 0.021 | 3.819 | 3.819 | 3.819 |
| syscall:bind | 2/2 | 0 | 0 | 0.003 | n/a | n/a | 0.000 | 1.452 | 1.452 | 1.777 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.247 | 1.247 | 1.247 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.077 | 0.073 | 0.113 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.183 | 0.183 | 0.183 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.062 | 0.062 | 0.062 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 4968 | 0.248 | 0.014 | 47.120 | 0.028 | 13.008936 CPU seconds | n/a |
| GPU 0 memory | MB | 4969 | 12142.429 | 11670.000 | 14666.000 | 12316.000 | n/a | n/a |
| GPU 0 power | W | 4969 | 36.850 | 27.542 | 77.582 | 27.700 | n/a | 184723.407 J |
| GPU 0 proc / 2604-99273 / sandbox / ~ / device / GPU-5d7a4c1e-7d9e-b455-b8c3-d52b14304215 memory | MB | 4969 | 3280.889 | 3118.000 | 5812.000 | 3396.000 | n/a | n/a |
| GPU 0 proc / 2604-99273 / sandbox / ~ / device / GPU-5d7a4c1e-7d9e-b455-b8c3-d52b14304215 estimated power | W | 3442 | 3.351 | 0.000 | 77.582 | 0.000 | n/a | n/a |
| GPU 0 proc / 2604-99273 / sandbox / ~ / device / GPU-5d7a4c1e-7d9e-b455-b8c3-d52b14304215 utilization | percent | 3442 | 4.428 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2718-101102 / sandbox / ~ / device / GPU-5d7a4c1e-7d9e-b455-b8c3-d52b14304215 memory | MB | 4969 | 8379.540 | 8070.000 | 8438.000 | 8438.000 | n/a | n/a |
| GPU 0 proc / 2718-101102 / sandbox / ~ / device / GPU-5d7a4c1e-7d9e-b455-b8c3-d52b14304215 estimated power | W | 1440 | 33.952 | 0.000 | 72.320 | 0.000 | n/a | n/a |
| GPU 0 proc / 2718-101102 / sandbox / ~ / device / GPU-5d7a4c1e-7d9e-b455-b8c3-d52b14304215 utilization | percent | 1440 | 47.090 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 4969 | 11660.429 | 11188.000 | 14184.000 | 11834.000 | n/a | n/a |
| GPU 0 utilization | percent | 4969 | 17.318 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 4969 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 4968 | 24.011 | 0.044 | 100.000 | 0.224 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 4968 | 26.349 | 0.000 | 78.780 | 0.251 | n/a | n/a |
| host disk_read_mb_s | MB/s | 4968 | 2.336 | 0.000 | 248.372 | 0.008 | n/a | n/a |
| host disk_write_mb_s | MB/s | 4968 | 2.448 | 0.000 | 244.756 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 4968 | 1.040 | 0.000 | 90.900 | 0.048 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 4968 | 1.255 | 0.000 | 91.661 | 0.048 | n/a | n/a |
| host mem_total_mb | MB | 4969 | 15363.535 | 15363.535 | 15363.535 | 15363.535 | n/a | n/a |
| host mem_used_mb | MB | 4969 | 9013.583 | 6759.461 | 15301.199 | 7488.938 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 4968 | 0.070 | 0.000 | 76.249 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 4968 | 0.076 | 0.000 | 83.433 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 4968 | 0.002 | 0.000 | 8.696 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 4968 | 0.004 | 0.000 | 0.466 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1695) CPU | percent | 4968 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1695) io read MB/s | MB/s | 4968 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1695) io write MB/s | MB/s | 4968 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1695) rss_mb | MB | 4969 | 1.244 | 0.305 | 3.320 | 0.305 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1695) main thread run-queue wait | percent | 4968 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1695) vms_mb | MB | 4969 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2604) CPU | percent | 4968 | 4.839 | 0.000 | 104.319 | 0.995 | 243.310000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2604) io read MB/s | MB/s | 4968 | 0.047 | 0.000 | 55.272 | 0.008 | 246.511719 MB | n/a |
| Agency harness — python -m lsbench (PID 2604) io write MB/s | MB/s | 4968 | 2.324 | 0.012 | 825.094 | 0.051 | 11748.507812 MB | n/a |
| Agency harness — python -m lsbench (PID 2604) rss_mb | MB | 4969 | 2888.754 | 2541.961 | 6996.465 | 3209.707 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2604) main thread run-queue wait | percent | 4968 | 0.000 | 0.000 | 0.456 | 0.000 | 0.008094 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2604) vms_mb | MB | 4969 | 16496.474 | 14125.379 | 23107.656 | 16709.801 | n/a | n/a |
| Python — vllm (PID 2609) CPU | percent | 4968 | 0.479 | 0.000 | 9.876 | 0.000 | 24.240000 CPU seconds | n/a |
| Python — vllm (PID 2609) io read MB/s | MB/s | 4968 | 0.002 | 0.000 | 4.362 | 0.000 | 14.011719 MB | n/a |
| Python — vllm (PID 2609) io write MB/s | MB/s | 4968 | 0.000 | 0.000 | 0.008 | 0.000 | 0.121094 MB | n/a |
| Python — vllm (PID 2609) rss_mb | MB | 4969 | 1470.961 | 1388.867 | 1787.906 | 1398.422 | n/a | n/a |
| Python — vllm (PID 2609) main thread run-queue wait | percent | 4968 | 0.027 | 0.000 | 2.539 | 0.000 | 1.367165 run-queue seconds | n/a |
| Python — vllm (PID 2609) vms_mb | MB | 4969 | 11028.303 | 10954.152 | 11031.172 | 11029.172 | n/a | n/a |
| Python — python -c (PID 2717) CPU | percent | 4968 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2717) io read MB/s | MB/s | 4968 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2717) io write MB/s | MB/s | 4968 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2717) rss_mb | MB | 4969 | 7.494 | 5.875 | 12.176 | 5.875 | n/a | n/a |
| Python — python -c (PID 2717) main thread run-queue wait | percent | 4968 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2717) vms_mb | MB | 4969 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2718) CPU | percent | 4968 | 5.067 | 0.000 | 76.185 | 1.989 | 255.690000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2718) io read MB/s | MB/s | 4968 | 0.011 | 0.000 | 26.412 | 0.000 | 73.582031 MB | n/a |
| VLLM::EngineCore (PID 2718) io write MB/s | MB/s | 4968 | 0.000 | 0.000 | 0.004 | 0.000 | 0.031250 MB | n/a |
| VLLM::EngineCore (PID 2718) rss_mb | MB | 4969 | 1970.244 | 1842.746 | 2342.070 | 1881.730 | n/a | n/a |
| VLLM::EngineCore (PID 2718) main thread run-queue wait | percent | 4968 | 0.137 | 0.000 | 17.661 | 0.000 | 6.916197 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2718) vms_mb | MB | 4969 | 21242.913 | 21236.008 | 21243.180 | 21243.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 2938) CPU | percent | 4953 | 0.002 | 0.000 | 0.995 | 0.000 | 0.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 2938) rss_mb | MB | 4954 | 0.233 | 0.051 | 0.551 | 0.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 2938) main thread run-queue wait | percent | 4953 | 0.017 | 0.000 | 5.413 | 0.000 | 0.841342 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — docker-init (PID 2938) vms_mb | MB | 4954 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 2969) CPU | percent | 4953 | 0.003 | 0.000 | 3.880 | 0.000 | 0.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 2969) rss_mb | MB | 4954 | 0.615 | 0.070 | 1.570 | 0.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 2969) main thread run-queue wait | percent | 4953 | 0.018 | 0.000 | 5.247 | 0.000 | 0.942258 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 2969) vms_mb | MB | 4954 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3061) CPU | percent | 4953 | 29.931 | 0.000 | 107.447 | 0.000 | 1494.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3061) rss_mb | MB | 4954 | 98.193 | 3.055 | 106.363 | 101.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3061) main thread run-queue wait | percent | 4953 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000148 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3061) vms_mb | MB | 4954 | 973.398 | 4.262 | 976.785 | 974.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3067) CPU | percent | 1 | 99.912 | 99.912 | 99.912 | 99.912 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3067) rss_mb | MB | 2 | 54.279 | 26.102 | 82.457 | 82.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3067) main thread run-queue wait | percent | 1 | 0.013 | 0.013 | 0.013 | 0.013 | 0.000130 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3067) vms_mb | MB | 2 | 66.166 | 34.180 | 98.152 | 98.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 3080) CPU | percent | 4924 | 2.862 | 0.000 | 63.673 | 1.991 | 142.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 3080) rss_mb | MB | 4925 | 278.772 | 57.980 | 333.062 | 301.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 3080) main thread run-queue wait | percent | 4924 | 17.848 | 0.002 | 87.578 | 0.013 | 887.060960 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 3080) vms_mb | MB | 4925 | 5499.810 | 5484.289 | 5499.816 | 5499.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3125) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3125) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3126) rss_mb | MB | 1 | 16.738 | 16.738 | 16.738 | 16.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3126) vms_mb | MB | 1 | 22.066 | 22.066 | 22.066 | 22.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3166) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3166) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3171) rss_mb | MB | 1 | 25.016 | 25.016 | 25.016 | 25.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 3171) vms_mb | MB | 1 | 217.531 | 217.531 | 217.531 | 217.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3196) rss_mb | MB | 1 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3196) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3197) rss_mb | MB | 1 | 20.621 | 20.621 | 20.621 | 20.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3197) vms_mb | MB | 1 | 25.504 | 25.504 | 25.504 | 25.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3256) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3256) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3257) rss_mb | MB | 1 | 18.285 | 18.285 | 18.285 | 18.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3257) vms_mb | MB | 1 | 24.098 | 24.098 | 24.098 | 24.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3265) rss_mb | MB | 1 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3265) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 3267) rss_mb | MB | 1 | 17.863 | 17.863 | 17.863 | 17.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 3267) vms_mb | MB | 1 | 209.988 | 209.988 | 209.988 | 209.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3282) rss_mb | MB | 1 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3282) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3293) CPU | percent | 366 | 0.005 | 0.000 | 0.990 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3293) rss_mb | MB | 367 | 2.688 | 2.688 | 2.688 | 2.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3293) main thread run-queue wait | percent | 366 | 0.000 | 0.000 | 0.040 | 0.000 | 0.000653 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3293) vms_mb | MB | 367 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3296) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3296) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3296) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3296) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3507) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3507) rss_mb | MB | 10 | 1.234 | 1.234 | 1.234 | 1.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3507) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3507) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3510) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3510) rss_mb | MB | 10 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3510) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3510) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3513) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3513) rss_mb | MB | 10 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3513) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3513) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3516) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3516) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3516) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3516) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3520) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3520) rss_mb | MB | 10 | 1.320 | 1.320 | 1.320 | 1.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3520) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3520) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3523) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3523) rss_mb | MB | 9 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3523) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3523) vms_mb | MB | 9 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3527) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3527) rss_mb | MB | 10 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3527) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3527) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3530) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3530) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3530) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3530) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3534) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3534) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3534) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3534) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3537) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3537) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3537) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3537) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3540) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3540) rss_mb | MB | 10 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3540) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3540) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3543) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3543) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3543) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3543) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3546) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3546) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3546) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3546) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3550) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3550) rss_mb | MB | 10 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3550) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3550) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3553) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3553) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3553) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3553) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3556) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3556) rss_mb | MB | 9 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3556) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3556) vms_mb | MB | 9 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3560) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3560) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3560) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3560) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3563) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3563) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3563) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3563) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3567) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3567) rss_mb | MB | 10 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3567) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3567) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3571) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3571) rss_mb | MB | 10 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3571) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3571) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3574) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3574) rss_mb | MB | 10 | 1.277 | 1.277 | 1.277 | 1.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3574) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3574) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3578) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3578) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3578) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3578) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3581) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3581) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3581) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3581) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3584) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3584) rss_mb | MB | 10 | 1.285 | 1.285 | 1.285 | 1.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3584) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3584) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3588) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3588) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3588) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3588) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3665) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3665) rss_mb | MB | 9 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3665) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3665) vms_mb | MB | 9 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3668) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3668) rss_mb | MB | 10 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3668) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3668) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3671) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3671) rss_mb | MB | 10 | 1.266 | 1.266 | 1.266 | 1.266 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3671) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3671) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3674) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3674) rss_mb | MB | 10 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3674) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3674) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3677) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3677) rss_mb | MB | 10 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3677) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3677) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3699) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3699) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3699) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3699) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3702) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3702) rss_mb | MB | 10 | 1.289 | 1.289 | 1.289 | 1.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3702) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3702) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3705) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3705) rss_mb | MB | 10 | 1.242 | 1.242 | 1.242 | 1.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3705) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3705) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3709) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3709) rss_mb | MB | 10 | 1.160 | 1.160 | 1.160 | 1.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3709) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3709) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3713) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3713) rss_mb | MB | 10 | 1.352 | 1.352 | 1.352 | 1.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3713) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3713) vms_mb | MB | 10 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3717) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3717) rss_mb | MB | 10 | 1.136 | 0.000 | 1.262 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3717) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 3717) vms_mb | MB | 10 | 2.197 | 0.000 | 2.441 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3823) rss_mb | MB | 1 | 1.461 | 1.461 | 1.461 | 1.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3823) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3824) rss_mb | MB | 1 | 18.516 | 18.516 | 18.516 | 18.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3824) vms_mb | MB | 1 | 24.254 | 24.254 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3887) rss_mb | MB | 1 | 1.340 | 1.340 | 1.340 | 1.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3887) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3888) rss_mb | MB | 1 | 7.000 | 7.000 | 7.000 | 7.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3888) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3896) rss_mb | MB | 1 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3896) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 3897) rss_mb | MB | 1 | 18.324 | 18.324 | 18.324 | 18.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 3897) vms_mb | MB | 1 | 209.930 | 209.930 | 209.930 | 209.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3909) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3909) rss_mb | MB | 2 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3909) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3909) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 3910) CPU | percent | 1 | 69.483 | 69.483 | 69.483 | 69.483 | 0.700000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 3910) rss_mb | MB | 2 | 190.312 | 124.000 | 256.625 | 256.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 3910) main thread run-queue wait | percent | 1 | 0.073 | 0.073 | 0.073 | 0.073 | 0.000732 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 3910) vms_mb | MB | 2 | 570.566 | 474.801 | 666.332 | 474.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3921) rss_mb | MB | 1 | 1.492 | 1.492 | 1.492 | 1.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 3921) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3922) rss_mb | MB | 1 | 20.477 | 20.477 | 20.477 | 20.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 3922) vms_mb | MB | 1 | 25.246 | 25.246 | 25.246 | 25.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3923) CPU | percent | 317 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3923) rss_mb | MB | 318 | 1.025 | 0.941 | 2.941 | 0.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3923) main thread run-queue wait | percent | 317 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 3923) vms_mb | MB | 318 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an0.py (PID 3926) CPU | percent | 317 | 151.762 | 95.482 | 178.113 | 99.388 | 485.620000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an0.py (PID 3926) rss_mb | MB | 318 | 5132.181 | 2251.340 | 7096.641 | 6445.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an0.py (PID 3926) main thread run-queue wait | percent | 317 | 40.738 | 0.001 | 79.718 | 0.002 | 130.393907 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — an0.py (PID 3926) vms_mb | MB | 318 | 5508.242 | 2501.309 | 7351.320 | 7048.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4103) rss_mb | MB | 1 | 1.305 | 1.305 | 1.305 | 1.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4103) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4104) rss_mb | MB | 1 | 9.230 | 9.230 | 9.230 | 9.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4104) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4116) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4116) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4117) rss_mb | MB | 1 | 7.047 | 7.047 | 7.047 | 7.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4117) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4118) rss_mb | MB | 1 | 2.605 | 2.605 | 2.605 | 2.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4118) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4119) rss_mb | MB | 1 | 131.723 | 131.723 | 131.723 | 131.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4119) vms_mb | MB | 1 | 347.105 | 347.105 | 347.105 | 347.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4135) rss_mb | MB | 1 | 2.703 | 2.703 | 2.703 | 2.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4135) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4136) rss_mb | MB | 1 | 20.578 | 20.578 | 20.578 | 20.578 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4136) vms_mb | MB | 1 | 212.516 | 212.516 | 212.516 | 212.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4176) rss_mb | MB | 1 | 1.227 | 1.227 | 1.227 | 1.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4176) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4177) rss_mb | MB | 1 | 19.914 | 19.914 | 19.914 | 19.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4177) vms_mb | MB | 1 | 24.988 | 24.988 | 24.988 | 24.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4185) rss_mb | MB | 1 | 2.754 | 2.754 | 2.754 | 2.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4185) vms_mb | MB | 1 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4188) rss_mb | MB | 1 | 143.852 | 143.852 | 143.852 | 143.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4188) vms_mb | MB | 1 | 150.039 | 150.039 | 150.039 | 150.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4212) rss_mb | MB | 1 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4212) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4213) rss_mb | MB | 1 | 18.309 | 18.309 | 18.309 | 18.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4213) vms_mb | MB | 1 | 24.254 | 24.254 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4216) rss_mb | MB | 1 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4216) vms_mb | MB | 1 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4218) rss_mb | MB | 1 | 149.086 | 149.086 | 149.086 | 149.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4218) vms_mb | MB | 1 | 154.973 | 154.973 | 154.973 | 154.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4228) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4228) rss_mb | MB | 2 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4228) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4228) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4229) CPU | percent | 1 | 102.168 | 102.168 | 102.168 | 102.168 | 1.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4229) rss_mb | MB | 2 | 93.682 | 13.516 | 173.848 | 173.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4229) main thread run-queue wait | percent | 1 | 7.427 | 7.427 | 7.427 | 7.427 | 0.074870 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4229) vms_mb | MB | 2 | 287.072 | 207.398 | 366.746 | 366.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 4300) CPU | percent | 130 | 149.956 | 38.798 | 179.518 | 38.798 | 198.170000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 4300) rss_mb | MB | 131 | 4899.055 | 0.000 | 5305.648 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 4300) main thread run-queue wait | percent | 130 | 58.364 | 2.848 | 88.824 | 15.478 | 77.101784 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 4300) vms_mb | MB | 131 | 5179.964 | 214.066 | 5526.422 | 5526.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4310) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4310) rss_mb | MB | 2 | 1.438 | 1.438 | 1.438 | 1.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4310) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4310) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4311) CPU | percent | 1 | 7.886 | 7.886 | 7.886 | 7.886 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4311) rss_mb | MB | 2 | 18.359 | 15.922 | 20.797 | 20.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4311) main thread run-queue wait | percent | 1 | 65.730 | 65.730 | 65.730 | 65.730 | 0.666758 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4311) vms_mb | MB | 2 | 23.766 | 21.770 | 25.762 | 25.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4344) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4344) rss_mb | MB | 17 | 1.504 | 0.617 | 2.754 | 0.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4344) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4344) vms_mb | MB | 17 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4345) CPU | percent | 16 | 14.501 | 0.991 | 35.507 | 35.507 | 2.350000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4345) rss_mb | MB | 17 | 871.117 | 13.227 | 2193.371 | 102.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4345) main thread run-queue wait | percent | 16 | 57.760 | 39.429 | 74.702 | 65.243 | 9.363707 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4345) vms_mb | MB | 17 | 1253.187 | 207.262 | 2640.984 | 1300.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4415) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4415) rss_mb | MB | 4 | 1.375 | 1.375 | 1.375 | 1.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4415) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4415) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4416) CPU | percent | 3 | 3.953 | 1.974 | 5.918 | 5.918 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4416) rss_mb | MB | 4 | 12.960 | 7.426 | 20.230 | 20.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4416) main thread run-queue wait | percent | 3 | 52.596 | 46.529 | 58.317 | 58.317 | 1.596514 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4416) vms_mb | MB | 4 | 17.733 | 11.926 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4424) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4424) rss_mb | MB | 2 | 1.348 | 1.348 | 1.348 | 1.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4424) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 4424) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4425) rss_mb | MB | 1 | 7.789 | 7.789 | 7.789 | 7.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 4425) vms_mb | MB | 1 | 12.926 | 12.926 | 12.926 | 12.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4429) CPU | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4429) rss_mb | MB | 44 | 2.512 | 0.410 | 2.660 | 0.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4429) main thread run-queue wait | percent | 43 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 4429) vms_mb | MB | 44 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4431) CPU | percent | 43 | 59.790 | 0.995 | 134.630 | 134.630 | 26.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4431) rss_mb | MB | 44 | 991.476 | 7.133 | 3029.855 | 2064.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4431) main thread run-queue wait | percent | 43 | 66.758 | 5.811 | 92.759 | 37.715 | 29.341484 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 4431) vms_mb | MB | 44 | 1346.704 | 11.785 | 3262.852 | 3262.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5745) rss_mb | MB | 1 | 1.363 | 1.363 | 1.363 | 1.363 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 5745) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5746) rss_mb | MB | 1 | 19.910 | 19.910 | 19.910 | 19.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 5746) vms_mb | MB | 1 | 25.117 | 25.117 | 25.117 | 25.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6012) CPU | percent | 605 | 0.021 | 0.000 | 0.995 | 0.000 | 0.130000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6012) rss_mb | MB | 606 | 2.629 | 2.629 | 2.629 | 2.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6012) main thread run-queue wait | percent | 605 | 0.000 | 0.000 | 0.004 | 0.000 | 0.000356 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6012) vms_mb | MB | 606 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6015) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6015) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6015) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6015) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6040) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6040) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6040) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6040) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6043) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6043) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6043) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6043) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6046) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6046) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6046) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6046) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6053) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6053) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6053) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6053) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6059) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6059) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6059) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6059) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6062) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6062) rss_mb | MB | 5 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6062) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6062) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6065) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6065) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6065) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6065) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6069) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6069) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6069) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6069) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6139) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6139) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6139) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6139) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6142) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6142) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6142) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6142) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6145) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6145) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6145) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6145) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6148) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6148) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6148) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6148) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6151) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6151) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6151) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6151) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6155) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6155) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6155) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6155) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6158) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6158) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6158) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6158) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6161) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6161) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6161) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6161) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6165) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6165) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6165) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6165) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6168) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6168) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6168) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6168) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6171) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6171) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6171) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6171) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6174) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6174) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6174) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6174) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6177) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6177) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6177) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6177) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6180) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6180) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6180) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6180) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6183) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6183) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6183) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6183) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6186) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6186) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6186) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6186) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6189) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6189) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6189) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6189) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6192) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6192) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6192) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6192) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6195) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6195) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6195) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6195) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6199) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6199) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6199) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6199) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6202) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6202) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6202) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6202) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6205) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6205) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6205) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6205) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6208) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6208) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6208) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6208) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6211) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6211) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6211) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6211) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6214) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6214) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6214) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6214) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6217) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6217) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6217) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6217) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6220) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6220) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6220) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6220) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6223) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6223) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6223) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6223) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6243) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6243) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6243) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6243) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6246) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6246) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6246) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6246) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6316) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6316) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6316) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6316) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6320) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6320) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6320) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6320) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6323) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6323) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6323) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6323) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6326) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6326) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6326) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6326) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6329) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6329) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6329) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6329) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6333) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6333) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6333) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6333) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6336) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6336) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6336) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6336) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6339) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6339) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6339) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6339) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6343) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6343) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6343) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6343) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6346) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6346) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6346) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6346) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6349) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6349) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6349) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6349) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6352) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6352) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6352) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6352) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6356) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6356) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6356) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6356) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6359) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6359) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6359) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6359) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6362) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6362) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6362) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6362) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6365) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6365) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6365) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6365) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6368) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6368) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6368) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6368) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6372) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6372) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6372) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6372) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6375) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6375) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6375) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6375) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6380) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6380) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6380) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6380) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6383) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6383) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6383) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6383) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6386) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6386) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6386) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6386) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6390) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6390) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6390) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6390) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6393) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6393) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6393) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6393) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6397) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6397) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6397) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6397) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6400) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6400) rss_mb | MB | 4 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6400) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6400) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6403) rss_mb | MB | 1 | 6.164 | 6.164 | 6.164 | 6.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6403) vms_mb | MB | 1 | 1309.664 | 1309.664 | 1309.664 | 1309.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6405) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6405) rss_mb | MB | 4 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6405) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6405) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6474) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6474) rss_mb | MB | 5 | 1.260 | 1.113 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6474) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6474) vms_mb | MB | 5 | 2.748 | 2.441 | 3.977 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6477) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6477) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6477) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6477) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6481) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6481) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6481) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6481) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6484) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6484) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6484) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6484) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6487) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6487) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6487) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6487) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6490) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6490) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6490) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6490) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6494) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6494) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6494) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6494) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6497) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6497) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6497) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6497) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6501) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6501) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6501) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6501) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6505) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6505) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6505) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6505) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6508) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6508) rss_mb | MB | 5 | 1.305 | 1.305 | 1.305 | 1.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6508) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6508) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6512) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6512) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6512) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6512) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6515) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6515) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6515) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6515) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6518) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6518) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6518) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6518) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6521) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6521) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6521) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6521) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6524) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6524) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6524) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6524) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6527) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6527) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6527) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6527) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6530) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6530) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6530) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6530) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6533) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6533) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6533) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6533) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6536) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6536) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6536) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6536) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6540) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6540) rss_mb | MB | 5 | 1.172 | 1.172 | 1.172 | 1.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6540) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6540) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6543) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6543) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6543) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6543) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6546) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6546) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6546) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6546) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6549) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6549) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6549) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6549) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6552) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6552) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6552) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6552) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6555) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6555) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6555) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6555) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6577) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6577) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6577) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6577) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6629) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6629) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6629) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6629) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6632) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6632) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6632) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6632) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6635) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6635) rss_mb | MB | 5 | 1.230 | 1.230 | 1.230 | 1.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6635) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6635) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6638) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6638) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6638) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6638) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6658) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6658) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6658) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6658) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6662) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6662) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6662) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6662) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6665) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6665) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6665) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6665) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6668) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6668) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6668) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6668) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6671) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6671) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6671) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6671) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6674) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6674) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6674) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6674) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6677) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6677) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6677) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6677) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6680) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6680) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6680) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6680) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6683) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6683) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6683) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6683) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6686) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6686) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6686) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6686) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6690) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6690) rss_mb | MB | 5 | 1.227 | 1.227 | 1.227 | 1.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6690) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6690) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6693) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6693) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6693) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6693) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6697) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6697) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6697) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6697) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6700) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6700) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6700) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6700) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6703) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6703) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6703) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6703) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6706) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6706) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6706) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6706) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6709) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6709) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6709) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6709) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6712) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6712) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6712) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6712) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6715) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6715) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6715) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6715) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6718) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6718) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6718) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6718) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6721) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6721) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6721) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6721) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6726) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6726) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6726) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6726) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6797) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6797) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6797) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6797) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6806) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6806) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6806) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6806) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6826) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6826) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6826) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 6826) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6833) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6833) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6834) rss_mb | MB | 1 | 20.156 | 20.156 | 20.156 | 20.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6834) vms_mb | MB | 1 | 25.117 | 25.117 | 25.117 | 25.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6838) CPU | percent | 742 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6838) rss_mb | MB | 743 | 2.742 | 2.742 | 2.742 | 2.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6838) main thread run-queue wait | percent | 742 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6838) vms_mb | MB | 743 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 6839) CPU | percent | 742 | 166.078 | 13.925 | 177.281 | 171.048 | 1242.410000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 6839) rss_mb | MB | 743 | 5178.046 | 25.449 | 5485.402 | 4376.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 6839) main thread run-queue wait | percent | 742 | 56.515 | 0.001 | 88.044 | 53.625 | 422.811523 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 6839) vms_mb | MB | 743 | 5408.745 | 229.367 | 5705.055 | 4595.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6851) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6851) rss_mb | MB | 4 | 1.457 | 1.457 | 1.457 | 1.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6851) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6851) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6852) CPU | percent | 3 | 4.640 | 1.987 | 6.961 | 6.961 | 0.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6852) rss_mb | MB | 4 | 13.428 | 7.133 | 21.125 | 21.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6852) main thread run-queue wait | percent | 3 | 54.856 | 49.340 | 59.816 | 49.340 | 1.655497 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6852) vms_mb | MB | 4 | 18.521 | 11.789 | 26.906 | 26.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6855) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6855) rss_mb | MB | 7 | 2.996 | 2.996 | 2.996 | 2.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6855) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6855) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6856) CPU | percent | 6 | 5.953 | 0.000 | 16.895 | 16.895 | 0.360000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6856) rss_mb | MB | 7 | 30.680 | 13.738 | 62.398 | 62.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6856) main thread run-queue wait | percent | 6 | 45.682 | 20.495 | 65.523 | 62.317 | 2.762394 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python stdin (PID 6856) vms_mb | MB | 7 | 223.028 | 207.430 | 254.309 | 254.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6860) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6860) rss_mb | MB | 2 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6860) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6860) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6861) CPU | percent | 1 | 5.931 | 5.931 | 5.931 | 5.931 | 0.060000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6861) rss_mb | MB | 2 | 19.043 | 16.660 | 21.426 | 21.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6861) main thread run-queue wait | percent | 1 | 60.280 | 60.280 | 60.280 | 60.280 | 0.609803 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6861) vms_mb | MB | 2 | 24.531 | 22.066 | 26.996 | 26.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6867) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6867) rss_mb | MB | 4 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6867) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6867) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6868) CPU | percent | 3 | 2.651 | 1.987 | 2.983 | 2.982 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6868) rss_mb | MB | 4 | 12.701 | 7.664 | 18.273 | 18.273 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6868) main thread run-queue wait | percent | 3 | 59.169 | 55.626 | 61.002 | 60.879 | 1.785835 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6868) vms_mb | MB | 4 | 17.505 | 11.926 | 24.254 | 24.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6874) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6874) rss_mb | MB | 2 | 1.383 | 1.383 | 1.383 | 1.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6874) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6874) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6875) CPU | percent | 1 | 7.912 | 7.912 | 7.912 | 7.912 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6875) rss_mb | MB | 2 | 17.766 | 14.875 | 20.656 | 20.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6875) main thread run-queue wait | percent | 1 | 76.734 | 76.734 | 76.734 | 76.734 | 0.775892 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6875) vms_mb | MB | 2 | 22.760 | 20.016 | 25.504 | 25.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6948) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6948) rss_mb | MB | 3 | 1.465 | 1.465 | 1.465 | 1.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6948) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6948) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6949) CPU | percent | 2 | 3.977 | 1.987 | 5.968 | 5.968 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6949) rss_mb | MB | 3 | 14.682 | 9.309 | 20.246 | 20.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6949) main thread run-queue wait | percent | 2 | 60.123 | 53.919 | 66.328 | 53.919 | 1.209752 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6949) vms_mb | MB | 3 | 19.542 | 13.492 | 25.117 | 25.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6950) CPU | percent | 57 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6950) rss_mb | MB | 58 | 2.984 | 2.984 | 2.984 | 2.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6950) main thread run-queue wait | percent | 57 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 6950) vms_mb | MB | 58 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — probe0.py (PID 6952) CPU | percent | 57 | 46.670 | 0.993 | 106.404 | 61.297 | 26.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — probe0.py (PID 6952) rss_mb | MB | 58 | 766.422 | 19.680 | 1253.363 | 1249.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — probe0.py (PID 6952) main thread run-queue wait | percent | 57 | 68.159 | 37.502 | 82.547 | 73.814 | 39.195318 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — probe0.py (PID 6952) vms_mb | MB | 58 | 1085.389 | 211.938 | 1565.219 | 1517.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6975) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6975) rss_mb | MB | 3 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6975) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 6975) vms_mb | MB | 3 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6976) CPU | percent | 2 | 3.461 | 2.961 | 3.961 | 3.961 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6976) rss_mb | MB | 3 | 12.132 | 7.555 | 18.527 | 18.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6976) main thread run-queue wait | percent | 2 | 42.393 | 37.758 | 47.028 | 37.758 | 0.857805 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 6976) vms_mb | MB | 3 | 17.174 | 11.926 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6988) rss_mb | MB | 1 | 291.160 | 291.160 | 291.160 | 291.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 6988) vms_mb | MB | 1 | 5499.816 | 5499.816 | 5499.816 | 5499.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 7067) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 7067) rss_mb | MB | 4 | 73.670 | 1.254 | 290.918 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 7067) main thread run-queue wait | percent | 3 | 0.193 | 0.000 | 0.578 | 0.000 | 0.005821 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude (PID 7067) vms_mb | MB | 4 | 1376.853 | 2.531 | 5499.816 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7068) CPU | percent | 2 | 1.951 | 1.914 | 1.987 | 1.914 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7068) rss_mb | MB | 3 | 13.327 | 9.027 | 16.887 | 16.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7068) main thread run-queue wait | percent | 2 | 52.476 | 50.578 | 54.375 | 54.375 | 1.077255 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7068) vms_mb | MB | 3 | 18.478 | 13.492 | 22.105 | 22.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7072) CPU | percent | 481 | 0.014 | 0.000 | 0.995 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7072) rss_mb | MB | 482 | 2.699 | 2.699 | 2.699 | 2.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7072) main thread run-queue wait | percent | 481 | 0.206 | 0.000 | 5.834 | 0.000 | 0.999197 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7072) vms_mb | MB | 482 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7075) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7075) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7075) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7075) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7077) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7077) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7077) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7077) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7079) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7079) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7079) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7079) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7081) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7081) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7081) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7081) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7085) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7085) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7085) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7085) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7087) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7087) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7087) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7087) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7089) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7089) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7089) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7089) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7091) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7091) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7091) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7091) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7093) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7093) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7093) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7093) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7095) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7095) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7095) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7095) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7098) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7098) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7098) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7098) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7100) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7100) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7100) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7100) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7103) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7103) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7103) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7103) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7105) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7105) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7105) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7105) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7107) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7107) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7107) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7107) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7109) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7109) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7109) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7109) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7113) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7113) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7113) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7113) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7115) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7115) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7115) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7115) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7120) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7120) rss_mb | MB | 6 | 1.007 | 0.258 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7120) main thread run-queue wait | percent | 5 | 1.045 | 0.000 | 5.224 | 0.000 | 0.052542 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7120) vms_mb | MB | 6 | 2.697 | 2.441 | 3.977 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7122) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7122) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7122) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7122) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7124) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7124) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7124) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7124) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7126) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7126) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7126) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7126) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7129) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7129) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7129) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7129) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7131) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7131) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7131) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7131) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7152) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7152) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7152) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7152) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7264) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7264) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7264) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7264) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7267) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7267) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7267) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7267) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7269) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7269) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7269) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7269) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7272) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7272) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7272) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7272) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7274) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7274) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7274) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7274) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7276) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7276) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7276) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7276) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7278) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7278) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7278) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7278) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7279) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7279) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7280) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7280) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7280) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7280) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7282) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7282) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7282) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7282) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7284) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7284) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7284) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7284) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7286) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7286) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7286) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7286) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7288) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7288) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7288) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7288) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7290) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7290) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7290) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7290) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7292) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7292) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7292) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7292) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7295) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7295) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7295) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7295) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7297) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7297) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7297) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7297) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7299) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7299) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7299) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7299) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7318) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7318) rss_mb | MB | 5 | 1.316 | 1.316 | 1.316 | 1.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7318) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7318) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7320) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7320) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7320) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7320) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7322) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7322) rss_mb | MB | 5 | 1.172 | 1.172 | 1.172 | 1.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7322) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7322) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7324) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7324) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7324) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7324) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7326) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7326) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7326) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7326) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 7327) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 7327) vms_mb | MB | 1 | 280.488 | 280.488 | 280.488 | 280.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7328) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7328) rss_mb | MB | 4 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7328) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7328) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7330) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7330) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7331) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7331) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7331) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7331) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7333) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7333) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7333) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7333) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7335) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7335) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7335) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7335) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7404) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7404) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7404) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7404) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7406) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7406) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7406) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7406) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7408) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7408) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7408) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7408) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7410) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7410) rss_mb | MB | 5 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7410) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7410) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7412) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7412) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7412) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7412) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7414) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7414) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7414) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7414) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7416) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7416) rss_mb | MB | 5 | 1.145 | 1.145 | 1.145 | 1.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7416) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7416) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7418) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7418) rss_mb | MB | 5 | 1.254 | 1.254 | 1.254 | 1.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7418) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7418) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7421) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7421) rss_mb | MB | 5 | 1.332 | 1.332 | 1.332 | 1.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7421) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7421) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 7422) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — ugrep (PID 7422) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7423) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7423) rss_mb | MB | 4 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7423) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7423) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7424) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7424) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7425) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7425) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7425) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7425) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7429) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7429) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7429) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7429) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7431) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7431) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7431) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7431) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7433) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7433) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7433) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7433) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7436) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7436) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7436) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7436) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7438) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7438) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7438) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7438) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7440) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7440) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7440) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7440) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7442) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7442) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7442) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7442) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7445) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7445) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7445) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7445) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7448) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7448) rss_mb | MB | 5 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7448) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7448) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7450) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7450) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7450) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7450) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7452) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7452) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7452) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7452) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7454) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7454) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7455) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7455) rss_mb | MB | 5 | 1.316 | 1.316 | 1.316 | 1.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7455) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7455) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7457) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7457) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7457) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7457) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7459) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7459) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7459) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7459) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7461) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7461) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7461) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7461) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7464) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7464) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7464) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7464) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7466) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7466) rss_mb | MB | 5 | 1.207 | 1.207 | 1.207 | 1.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7466) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7466) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7468) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7468) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7468) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7468) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7470) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7470) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7470) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7470) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7472) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7472) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7472) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7472) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7474) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7474) rss_mb | MB | 5 | 1.297 | 1.297 | 1.297 | 1.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7474) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7474) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7479) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7479) rss_mb | MB | 5 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7479) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7479) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7481) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7481) rss_mb | MB | 5 | 1.164 | 1.164 | 1.164 | 1.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7481) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7481) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7483) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7483) rss_mb | MB | 5 | 1.168 | 1.168 | 1.168 | 1.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7483) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7483) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7484) rss_mb | MB | 1 | 1.504 | 1.504 | 1.504 | 1.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7484) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7485) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7485) rss_mb | MB | 4 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7485) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7485) vms_mb | MB | 4 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7487) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7487) rss_mb | MB | 5 | 1.195 | 1.195 | 1.195 | 1.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7487) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7487) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7490) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7490) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7490) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7490) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7493) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7493) rss_mb | MB | 5 | 1.336 | 1.336 | 1.336 | 1.336 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7493) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7493) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7495) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7495) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7495) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7495) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7497) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7497) rss_mb | MB | 5 | 1.156 | 1.156 | 1.156 | 1.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7497) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7497) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7565) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7565) rss_mb | MB | 5 | 1.332 | 1.332 | 1.332 | 1.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7565) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7565) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7568) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7568) rss_mb | MB | 5 | 1.148 | 1.148 | 1.148 | 1.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7568) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7568) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7571) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7571) rss_mb | MB | 5 | 1.312 | 1.312 | 1.312 | 1.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7571) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7571) vms_mb | MB | 5 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7579) rss_mb | MB | 1 | 1.477 | 1.477 | 1.477 | 1.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7579) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude_lifecycle_hook.py (PID 7580) rss_mb | MB | 1 | 9.531 | 9.531 | 9.531 | 9.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — claude_lifecycle_hook.py (PID 7580) vms_mb | MB | 1 | 13.484 | 13.484 | 13.484 | 13.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7611) rss_mb | MB | 1 | 2.820 | 2.820 | 2.820 | 2.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7611) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps.py (PID 7613) rss_mb | MB | 1 | 9.211 | 9.211 | 9.211 | 9.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — gaps.py (PID 7613) vms_mb | MB | 1 | 13.414 | 13.414 | 13.414 | 13.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7632) rss_mb | MB | 1 | 1.434 | 1.434 | 1.434 | 1.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7632) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7633) rss_mb | MB | 1 | 20.223 | 20.223 | 20.223 | 20.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7633) vms_mb | MB | 1 | 24.988 | 24.988 | 24.988 | 24.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7663) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7663) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7664) rss_mb | MB | 1 | 16.184 | 16.184 | 16.184 | 16.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7664) vms_mb | MB | 1 | 21.770 | 21.770 | 21.770 | 21.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7686) rss_mb | MB | 1 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7686) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7687) rss_mb | MB | 1 | 9.766 | 9.766 | 9.766 | 9.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7687) vms_mb | MB | 1 | 13.617 | 13.617 | 13.617 | 13.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7695) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7695) rss_mb | MB | 3 | 2.957 | 2.957 | 2.957 | 2.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7695) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7695) vms_mb | MB | 3 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — synth.py (PID 7697) CPU | percent | 2 | 99.442 | 99.403 | 99.481 | 99.481 | 2.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — synth.py (PID 7697) rss_mb | MB | 3 | 152.499 | 148.469 | 155.559 | 155.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — synth.py (PID 7697) main thread run-queue wait | percent | 2 | 0.003 | 0.001 | 0.006 | 0.006 | 0.000062 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — synth.py (PID 7697) vms_mb | MB | 3 | 158.160 | 154.160 | 161.160 | 161.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7737) rss_mb | MB | 1 | 2.711 | 2.711 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7737) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7739) CPU | percent | 144 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7739) rss_mb | MB | 145 | 1.508 | 1.508 | 1.508 | 1.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7739) main thread run-queue wait | percent | 144 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7739) vms_mb | MB | 145 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7740) rss_mb | MB | 1 | 1.262 | 1.262 | 1.262 | 1.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sleep (PID 7740) vms_mb | MB | 1 | 2.441 | 2.441 | 2.441 | 2.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 7741) CPU | percent | 144 | 169.706 | 91.414 | 182.954 | 169.051 | 247.370000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 7741) rss_mb | MB | 145 | 4718.477 | 19.031 | 5167.738 | 4377.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 7741) main thread run-queue wait | percent | 144 | 56.214 | 0.030 | 78.324 | 52.777 | 81.932506 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 7741) vms_mb | MB | 145 | 4964.914 | 211.316 | 5387.215 | 4597.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7750) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7750) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7751) rss_mb | MB | 1 | 15.766 | 15.766 | 15.766 | 15.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7751) vms_mb | MB | 1 | 20.527 | 20.527 | 20.527 | 20.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7759) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7759) rss_mb | MB | 2 | 1.426 | 1.426 | 1.426 | 1.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7759) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7759) vms_mb | MB | 2 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7760) CPU | percent | 1 | 7.896 | 7.896 | 7.896 | 7.896 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7760) rss_mb | MB | 2 | 19.002 | 16.758 | 21.246 | 21.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7760) main thread run-queue wait | percent | 1 | 55.260 | 55.260 | 55.260 | 55.260 | 0.559868 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7760) vms_mb | MB | 2 | 24.527 | 22.066 | 26.988 | 26.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7764) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7764) rss_mb | MB | 2 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7764) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7764) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 7765) CPU | percent | 1 | 0.989 | 0.989 | 0.989 | 0.989 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 7765) rss_mb | MB | 2 | 8.174 | 7.180 | 9.168 | 9.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 7765) main thread run-queue wait | percent | 1 | 50.362 | 50.362 | 50.362 | 50.362 | 0.509241 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 7765) vms_mb | MB | 2 | 12.523 | 11.789 | 13.258 | 13.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7767) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7767) rss_mb | MB | 4 | 1.469 | 1.469 | 1.469 | 1.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7767) main thread run-queue wait | percent | 3 | 0.021 | 0.000 | 0.062 | 0.000 | 0.000628 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7767) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7768) CPU | percent | 3 | 2.639 | 1.974 | 3.969 | 3.969 | 0.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7768) rss_mb | MB | 4 | 11.375 | 1.469 | 18.887 | 18.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7768) main thread run-queue wait | percent | 3 | 52.182 | 50.370 | 55.489 | 50.370 | 1.583242 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7768) vms_mb | MB | 4 | 15.222 | 2.531 | 24.605 | 24.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7791) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7791) rss_mb | MB | 4 | 1.371 | 1.371 | 1.371 | 1.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7791) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7791) vms_mb | MB | 4 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7792) CPU | percent | 3 | 3.967 | 1.973 | 6.947 | 6.947 | 0.120000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7792) rss_mb | MB | 4 | 13.361 | 7.605 | 20.887 | 20.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7792) main thread run-queue wait | percent | 3 | 64.690 | 61.154 | 71.717 | 71.717 | 1.958260 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7792) vms_mb | MB | 4 | 17.882 | 11.926 | 25.762 | 25.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7814) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7814) rss_mb | MB | 5 | 1.484 | 1.484 | 1.484 | 1.484 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7814) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7814) vms_mb | MB | 5 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7815) CPU | percent | 4 | 3.728 | 1.988 | 7.952 | 7.952 | 0.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7815) rss_mb | MB | 5 | 13.540 | 4.645 | 21.516 | 21.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7815) main thread run-queue wait | percent | 4 | 54.253 | 50.525 | 59.556 | 59.556 | 2.183004 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7815) vms_mb | MB | 5 | 18.759 | 10.000 | 27.062 | 27.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7818) rss_mb | MB | 1 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7818) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7819) rss_mb | MB | 1 | 7.910 | 7.910 | 7.910 | 7.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7819) vms_mb | MB | 1 | 12.926 | 12.926 | 12.926 | 12.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7823) rss_mb | MB | 1 | 1.418 | 1.418 | 1.418 | 1.418 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7823) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7824) rss_mb | MB | 1 | 7.918 | 7.918 | 7.918 | 7.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7824) vms_mb | MB | 1 | 12.926 | 12.926 | 12.926 | 12.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7842) rss_mb | MB | 1 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7842) vms_mb | MB | 1 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitstat.py (PID 7844) rss_mb | MB | 1 | 24.676 | 24.676 | 24.676 | 24.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitstat.py (PID 7844) vms_mb | MB | 1 | 216.188 | 216.188 | 216.188 | 216.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7859) rss_mb | MB | 1 | 1.383 | 1.383 | 1.383 | 1.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7859) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7860) rss_mb | MB | 1 | 1.379 | 1.379 | 1.379 | 1.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7860) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7884) CPU | percent | 138 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7884) rss_mb | MB | 139 | 2.773 | 2.773 | 2.773 | 2.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7884) main thread run-queue wait | percent | 138 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7884) vms_mb | MB | 139 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 7886) CPU | percent | 138 | 150.138 | 9.930 | 172.827 | 156.987 | 208.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 7886) rss_mb | MB | 139 | 807.635 | 14.016 | 1079.180 | 671.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 7886) main thread run-queue wait | percent | 138 | 44.585 | 0.003 | 57.816 | 49.346 | 61.989149 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys.py (PID 7886) vms_mb | MB | 139 | 1049.621 | 208.582 | 1334.070 | 884.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 7887) CPU | percent | 138 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 7887) rss_mb | MB | 139 | 1.219 | 1.219 | 1.219 | 1.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 7887) main thread run-queue wait | percent | 138 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 7887) vms_mb | MB | 139 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7923) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7923) rss_mb | MB | 17 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7923) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7923) vms_mb | MB | 17 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve.py (PID 7925) CPU | percent | 16 | 165.814 | 153.195 | 178.962 | 168.040 | 26.750000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve.py (PID 7925) rss_mb | MB | 17 | 589.709 | 362.883 | 662.414 | 662.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve.py (PID 7925) main thread run-queue wait | percent | 16 | 50.359 | 38.922 | 73.077 | 68.175 | 8.127776 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve.py (PID 7925) vms_mb | MB | 17 | 887.634 | 579.875 | 974.938 | 974.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7931) rss_mb | MB | 1 | 1.430 | 1.430 | 1.430 | 1.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7931) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7932) rss_mb | MB | 1 | 8.918 | 8.918 | 8.918 | 8.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7932) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7943) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7943) rss_mb | MB | 4 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7943) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 7943) vms_mb | MB | 4 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — val.py (PID 7947) CPU | percent | 3 | 98.644 | 96.279 | 103.241 | 103.241 | 2.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — val.py (PID 7947) rss_mb | MB | 4 | 638.112 | 23.512 | 1493.164 | 580.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — val.py (PID 7947) main thread run-queue wait | percent | 3 | 5.987 | 4.730 | 6.973 | 6.259 | 0.180892 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — val.py (PID 7947) vms_mb | MB | 4 | 954.069 | 215.750 | 1716.570 | 802.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7986) rss_mb | MB | 1 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 7986) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7987) rss_mb | MB | 1 | 9.934 | 9.934 | 9.934 | 9.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 7987) vms_mb | MB | 1 | 13.773 | 13.773 | 13.773 | 13.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8017) rss_mb | MB | 1 | 1.586 | 1.586 | 1.586 | 1.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8017) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8018) rss_mb | MB | 1 | 14.406 | 14.406 | 14.406 | 14.406 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8018) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8040) rss_mb | MB | 1 | 1.480 | 1.480 | 1.480 | 1.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8040) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8041) rss_mb | MB | 1 | 21.598 | 21.598 | 21.598 | 21.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8041) vms_mb | MB | 1 | 26.996 | 26.996 | 26.996 | 26.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8085) CPU | percent | 175 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8085) rss_mb | MB | 176 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8085) main thread run-queue wait | percent | 175 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8085) vms_mb | MB | 176 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 8087) CPU | percent | 175 | 170.564 | 97.386 | 182.666 | 164.222 | 301.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 8087) rss_mb | MB | 176 | 4648.988 | 58.766 | 5236.156 | 3178.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 8087) main thread run-queue wait | percent | 175 | 55.758 | 0.011 | 80.641 | 48.369 | 98.565743 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — build.py (PID 8087) vms_mb | MB | 176 | 4881.333 | 251.574 | 5456.090 | 3398.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8118) CPU | percent | 99 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8118) rss_mb | MB | 100 | 2.934 | 2.934 | 2.934 | 2.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8118) main thread run-queue wait | percent | 99 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8118) vms_mb | MB | 100 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys2.py (PID 8120) CPU | percent | 99 | 146.814 | 12.909 | 174.374 | 168.556 | 146.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys2.py (PID 8120) rss_mb | MB | 100 | 649.952 | 67.543 | 1044.438 | 750.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys2.py (PID 8120) main thread run-queue wait | percent | 99 | 42.070 | 0.014 | 56.448 | 56.448 | 41.951998 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — keys2.py (PID 8120) vms_mb | MB | 100 | 895.826 | 449.500 | 1256.641 | 962.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8121) CPU | percent | 99 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8121) rss_mb | MB | 100 | 1.203 | 1.203 | 1.203 | 1.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8121) main thread run-queue wait | percent | 99 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8121) vms_mb | MB | 100 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8163) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8163) rss_mb | MB | 10 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8163) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8163) vms_mb | MB | 10 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve2.py (PID 8165) CPU | percent | 9 | 137.618 | 87.515 | 175.248 | 113.366 | 12.480000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve2.py (PID 8165) rss_mb | MB | 10 | 641.077 | 24.512 | 1369.047 | 599.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve2.py (PID 8165) main thread run-queue wait | percent | 9 | 31.906 | 7.955 | 50.148 | 19.001 | 2.894078 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — solve2.py (PID 8165) vms_mb | MB | 10 | 974.609 | 216.188 | 1623.328 | 812.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8186) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8186) rss_mb | MB | 7 | 3.016 | 3.016 | 3.016 | 3.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8186) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8186) vms_mb | MB | 7 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitmargin.py (PID 8188) CPU | percent | 6 | 145.985 | 73.506 | 171.082 | 154.092 | 8.810000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitmargin.py (PID 8188) rss_mb | MB | 7 | 1461.185 | 392.426 | 2221.734 | 2221.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitmargin.py (PID 8188) main thread run-queue wait | percent | 6 | 45.087 | 0.019 | 73.695 | 42.163 | 2.720619 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitmargin.py (PID 8188) vms_mb | MB | 7 | 1700.764 | 700.941 | 2441.727 | 2441.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8189) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8189) rss_mb | MB | 7 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8189) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8189) vms_mb | MB | 7 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8205) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8205) rss_mb | MB | 10 | 2.809 | 2.809 | 2.809 | 2.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8205) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8205) vms_mb | MB | 10 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitmargin2.py (PID 8207) CPU | percent | 9 | 137.274 | 66.464 | 174.274 | 118.434 | 12.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitmargin2.py (PID 8207) rss_mb | MB | 10 | 1511.033 | 154.379 | 1832.277 | 1131.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitmargin2.py (PID 8207) main thread run-queue wait | percent | 9 | 40.051 | 0.023 | 64.332 | 32.372 | 3.634974 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — waitmargin2.py (PID 8207) vms_mb | MB | 10 | 1778.063 | 700.910 | 2052.531 | 1395.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8208) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8208) rss_mb | MB | 10 | 1.176 | 1.176 | 1.176 | 1.176 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8208) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8208) vms_mb | MB | 10 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8224) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8224) rss_mb | MB | 9 | 2.941 | 2.941 | 2.941 | 2.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8224) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8224) vms_mb | MB | 9 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs.py (PID 8226) CPU | percent | 8 | 160.578 | 92.374 | 175.488 | 170.014 | 12.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs.py (PID 8226) rss_mb | MB | 9 | 1213.421 | 137.238 | 1500.168 | 1333.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs.py (PID 8226) main thread run-queue wait | percent | 8 | 43.606 | 0.020 | 53.628 | 48.655 | 3.514012 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs.py (PID 8226) vms_mb | MB | 9 | 1471.264 | 701.125 | 1700.371 | 1551.844 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8227) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8227) rss_mb | MB | 9 | 1.098 | 1.098 | 1.098 | 1.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8227) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8227) vms_mb | MB | 9 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8282) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8282) rss_mb | MB | 8 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8282) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8282) vms_mb | MB | 8 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs2.py (PID 8284) CPU | percent | 7 | 162.815 | 140.234 | 172.995 | 164.714 | 11.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs2.py (PID 8284) rss_mb | MB | 8 | 1187.250 | 1065.180 | 1537.332 | 1537.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs2.py (PID 8284) main thread run-queue wait | percent | 7 | 55.569 | 24.056 | 74.080 | 37.448 | 3.913450 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs2.py (PID 8284) vms_mb | MB | 8 | 1426.493 | 1287.141 | 1755.355 | 1755.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8285) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8285) rss_mb | MB | 8 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8285) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8285) vms_mb | MB | 8 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8302) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8302) rss_mb | MB | 14 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8302) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8302) vms_mb | MB | 14 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs3.py (PID 8304) CPU | percent | 13 | 158.756 | 92.409 | 179.399 | 169.937 | 20.800000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs3.py (PID 8304) rss_mb | MB | 14 | 2849.140 | 14.145 | 3487.098 | 3484.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs3.py (PID 8304) main thread run-queue wait | percent | 13 | 42.136 | 0.008 | 55.836 | 52.046 | 5.521119 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs3.py (PID 8304) vms_mb | MB | 14 | 3131.534 | 208.566 | 4071.059 | 3701.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8305) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8305) rss_mb | MB | 14 | 1.137 | 1.137 | 1.137 | 1.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8305) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8305) vms_mb | MB | 14 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8319) rss_mb | MB | 1 | 1.527 | 1.527 | 1.527 | 1.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8319) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8320) rss_mb | MB | 1 | 20.773 | 20.773 | 20.773 | 20.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8320) vms_mb | MB | 1 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8322) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8322) rss_mb | MB | 14 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8322) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8322) vms_mb | MB | 14 | 3.980 | 3.980 | 3.980 | 3.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs4.py (PID 8324) CPU | percent | 13 | 163.628 | 116.284 | 174.707 | 170.026 | 21.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs4.py (PID 8324) rss_mb | MB | 14 | 2931.436 | 1017.234 | 3472.293 | 3472.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs4.py (PID 8324) main thread run-queue wait | percent | 13 | 56.340 | 7.217 | 74.081 | 72.746 | 7.379950 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — dirs4.py (PID 8324) vms_mb | MB | 14 | 3149.066 | 1208.773 | 3689.977 | 3689.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8325) CPU | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8325) rss_mb | MB | 14 | 1.043 | 1.043 | 1.043 | 1.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8325) main thread run-queue wait | percent | 13 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8325) vms_mb | MB | 14 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8345) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8345) rss_mb | MB | 2 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8345) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8345) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — make_adapter.py (PID 8347) rss_mb | MB | 1 | 286.562 | 286.562 | 286.562 | 286.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — make_adapter.py (PID 8347) vms_mb | MB | 1 | 700.926 | 700.926 | 700.926 | 700.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8348) rss_mb | MB | 1 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8348) vms_mb | MB | 1 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — date (PID 8355) rss_mb | MB | 1 | 0.285 | 0.285 | 0.285 | 0.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — date (PID 8355) vms_mb | MB | 1 | 2.395 | 2.395 | 2.395 | 2.395 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8363) rss_mb | MB | 1 | 1.512 | 1.512 | 1.512 | 1.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8363) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8364) rss_mb | MB | 1 | 20.527 | 20.527 | 20.527 | 20.527 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8364) vms_mb | MB | 1 | 25.375 | 25.375 | 25.375 | 25.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8367) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8367) rss_mb | MB | 9 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8367) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8367) vms_mb | MB | 9 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pos0.py (PID 8369) CPU | percent | 8 | 20.849 | 11.918 | 40.663 | 31.777 | 1.680000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pos0.py (PID 8369) rss_mb | MB | 9 | 934.451 | 148.492 | 1347.332 | 1135.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pos0.py (PID 8369) main thread run-queue wait | percent | 8 | 0.032 | 0.013 | 0.055 | 0.055 | 0.002606 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — pos0.py (PID 8369) vms_mb | MB | 9 | 1429.953 | 687.195 | 1629.867 | 1359.773 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8370) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8370) rss_mb | MB | 9 | 1.180 | 1.180 | 1.180 | 1.180 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8370) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — tail (PID 8370) vms_mb | MB | 9 | 2.473 | 2.473 | 2.473 | 2.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8404) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8404) rss_mb | MB | 2 | 2.852 | 2.852 | 2.852 | 2.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8404) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — bash (PID 8404) vms_mb | MB | 2 | 3.977 | 3.977 | 3.977 | 3.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 8405) CPU | percent | 1 | 156.704 | 156.704 | 156.704 | 156.704 | 1.580000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 8405) rss_mb | MB | 2 | 711.676 | 30.629 | 1392.723 | 30.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 8405) main thread run-queue wait | percent | 1 | 27.232 | 27.232 | 27.232 | 27.232 | 0.274567 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — python -c (PID 8405) vms_mb | MB | 2 | 961.535 | 252.199 | 1670.871 | 252.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8426) rss_mb | MB | 1 | 1.473 | 1.473 | 1.473 | 1.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — sh (PID 8426) vms_mb | MB | 1 | 2.531 | 2.531 | 2.531 | 2.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8427) rss_mb | MB | 1 | 9.508 | 9.508 | 9.508 | 9.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-claude_code_0000_0000 — agpolicy_hook.py (PID 8427) vms_mb | MB | 1 | 13.492 | 13.492 | 13.492 | 13.492 | n/a | n/a |
| docker inspect (PID 8436) rss_mb | MB | 1 | 8.109 | 8.109 | 8.109 | 8.109 | n/a | n/a |
| docker inspect (PID 8436) vms_mb | MB | 1 | 69.133 | 69.133 | 69.133 | 69.133 | n/a | n/a |
| docker commit (PID 8461) CPU | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 8461) io read MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8461) io write MB/s | MB/s | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8461) rss_mb | MB | 23 | 30.594 | 30.594 | 30.594 | 30.594 | n/a | n/a |
| docker commit (PID 8461) main thread run-queue wait | percent | 22 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 8461) vms_mb | MB | 23 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 CPU | percent | 4953 | 94.318 | 0.000 | 218.508 | 0.000 | 4713.469418 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 4953 | 16.890 | 0.000 | 51.373 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 4953 | 23.697 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_full_pct | percent of wall time stalled | 4953 | 0.258 | 0.000 | 92.797 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io_psi_some_pct | percent of wall time stalled | 4953 | 0.300 | 0.000 | 92.897 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io read MB/s | MB/s | 4953 | 1.782 | 0.000 | 248.162 | 0.000 | 8915.167969 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 io write MB/s | MB/s | 4953 | 0.081 | 0.000 | 185.832 | 0.000 | 405.078125 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory | MB | 4954 | 3248.065 | 17.539 | 8247.977 | 3715.902 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_full_pct | percent of wall time stalled | 4953 | 0.053 | 0.000 | 43.526 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 memory_psi_some_pct | percent of wall time stalled | 4953 | 0.056 | 0.000 | 45.927 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net rx MB/s | MB/s | 4953 | 0.002 | 0.000 | 8.397 | 0.000 | 8.503482 MB | n/a |
| sandbox sandbox_agent_lsb-claude_code_0000_0000 net tx MB/s | MB/s | 4953 | 0.000 | 0.000 | 0.010 | 0.000 | 0.051820 MB | n/a |
| workload total CPU | percent | 4968 | 10.388 | 1.403 | 104.689 | 2.007 | 523.447545 CPU seconds | n/a |
| workload total memory | MB | 4969 | 6831.236 | 5803.918 | 13415.910 | 6368.098 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
