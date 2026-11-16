# agprof summary

- Duration: **690.111 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **60 calls**, 60 succeeded, 0 failed, 0 interrupted, n/a reported retries, 535.510 s total wait
- Tools: **67/67 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **71573** at 1.98 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 664742.101 / 664742.101 ms |
| LLM latency p50 / p95 | 5015.279 / 32335.902 ms |
| LLM TTFT p50 / p95 | 1847.023 / 3666.545 ms |
| LLM input / output tokens | 6094277 / 70188 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 60 total, 60 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 433.972 / 3996.228 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 27/27 | 27 | 0 | 0 | 421.194 ms | 4096.157 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 312.361 ms | 312.361 ms |
| edit | 2/2 | 2 | 0 | 0 | 0.636 ms | 0.720 ms |
| generate | 5/5 | 5 | 0 | 0 | 3932.604 ms | 5603.914 ms |
| inspect | 1/1 | 1 | 0 | 0 | 3707.370 ms | 3707.370 ms |
| inspect_module_inputs | 1/1 | 1 | 0 | 0 | 3619.039 ms | 3619.039 ms |
| patch | 9/9 | 9 | 0 | 0 | 433.972 ms | 470.761 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 234.955 ms | 234.955 ms |
| todowrite | 2/2 | 2 | 0 | 0 | 0.177 ms | 0.209 ms |
| token_stats | 1/1 | 1 | 0 | 0 | 1917.815 ms | 1917.815 ms |
| trace | 8/8 | 8 | 0 | 0 | 1763.366 ms | 2957.654 ms |
| write | 9/9 | 9 | 0 | 0 | 0.368 ms | 0.534 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 10.182% | 138.042% | 70.186 s | 5895.329 MB | 6373.977 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| VLLM::EngineCor | 3494 |  | 685 | 2.617% | 61.336% | 18.040 s | 2321.145 MB | 2321.250 MB | 21203.379 MB | 21203.379 MB | 0.000000 MB | 0.003906 MB |
| lsb_guard.sh | 3440 |  | 685 | 0.000% | 0.000% | 0.000 s | 3.270 MB | 3.270 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python3 | 3840 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.857% | 99.857% | 1.010 s | 54.473 MB | 82.281 MB | 66.738 MB | 97.996 MB | n/a MB | n/a MB |
| bash | 3834 | sandbox_agent_lsb-native_0000_0000 | 660 | 5.556% | 87.058% | 36.870 s | 102.825 MB | 107.078 MB | 963.532 MB | 972.160 MB | n/a MB | n/a MB |
| lsb_grid_worker | 3420 |  | 685 | 0.000% | 0.000% | 0.000 s | 3.398 MB | 3.398 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| vllm | 3434 |  | 685 | 0.228% | 5.972% | 1.570 s | 1803.829 MB | 1804.203 MB | 11038.633 MB | 11044.496 MB | 0.000000 MB | 0.031250 MB |
| docker-init | 3711 | sandbox_agent_lsb-native_0000_0000 | 660 | 0.003% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python | 3493 |  | 685 | 0.000% | 0.000% | 0.000 s | 12.184 MB | 12.184 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| tail | 3742 | sandbox_agent_lsb-native_0000_0000 | 660 | 0.002% | 0.995% | 0.010 s | 1.566 MB | 1.566 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 3429 |  | 685 | 7.287% | 137.092% | 50.230 s | 3126.820 MB | 3466.480 MB | 16383.709 MB | 17372.906 MB | 4.957031 MB | 799.882812 MB |
| sleep | 3443 |  | 16 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python3 | 3852 | sandbox_agent_lsb-native_0000_0000 | 633 | 0.400% | 60.570% | 2.550 s | 71.881 MB | 74.180 MB | 86.204 MB | 88.102 MB | n/a MB | n/a MB |
| python | 3882 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.320 MB | 14.320 MB | 1874.164 MB | 1874.164 MB | n/a MB | n/a MB |
| bash | 3881 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.781 MB | 2.781 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 3892 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 3927 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.746 MB | 2.746 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3940 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.234 MB | 7.234 MB | 11.785 MB | 11.785 MB | n/a MB | n/a MB |
| python | 3928 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.598 MB | 12.598 MB | 16.016 MB | 16.016 MB | n/a MB | n/a MB |
| sleep | 3958 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 3981 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.727 MB | 2.727 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3982 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.662% | 1.987% | 0.020 s | 12.168 MB | 12.262 MB | 15.781 MB | 15.781 MB | n/a MB | n/a MB |
| python | 3992 | sandbox_agent_lsb-native_0000_0000 | 3 | 99.901% | 100.435% | 2.010 s | 536.812 MB | 927.188 MB | 549.615 MB | 948.637 MB | n/a MB | n/a MB |
| python | 4005 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.660 MB | 7.660 MB | 12.918 MB | 12.918 MB | n/a MB | n/a MB |
| sleep | 4020 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4045 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4060 | sandbox_agent_lsb-native_0000_0000 | 4 | 167.952% | 169.070% | 5.070 s | 99.589 MB | 113.949 MB | 320.858 MB | 335.184 MB | n/a MB | n/a MB |
| bash | 4077 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.938 MB | 2.938 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4078 | sandbox_agent_lsb-native_0000_0000 | 4 | 189.145% | 189.848% | 5.710 s | 124.528 MB | 128.703 MB | 344.606 MB | 348.648 MB | n/a MB | n/a MB |
| sleep | 4086 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4125 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 12.426 MB | 12.426 MB | 15.789 MB | 15.789 MB | n/a MB | n/a MB |
| python | 4135 | sandbox_agent_lsb-native_0000_0000 | 3 | 100.435% | 100.470% | 2.020 s | 436.866 MB | 825.824 MB | 448.467 MB | 842.688 MB | n/a MB | n/a MB |
| python | 4137 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.168 MB | 8.168 MB | 13.020 MB | 13.020 MB | n/a MB | n/a MB |
| sleep | 4163 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4175 | sandbox_agent_lsb-native_0000_0000 | 3 | 98.378% | 98.441% | 1.980 s | 113.331 MB | 116.086 MB | 305.785 MB | 307.270 MB | n/a MB | n/a MB |
| bash | 4174 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.969 MB | 2.969 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4189 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.277 MB | 13.277 MB | 207.391 MB | 207.391 MB | n/a MB | n/a MB |
| bash | 4188 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.891 MB | 2.891 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4203 | sandbox_agent_lsb-native_0000_0000 | 10 | 189.911% | 197.134% | 17.240 s | 146.886 MB | 169.547 MB | 362.717 MB | 385.285 MB | n/a MB | n/a MB |
| bash | 4202 | sandbox_agent_lsb-native_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 4208 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 4235 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.906 MB | 2.906 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4236 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| sleep | 4341 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 4349 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.973 MB | 2.973 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4350 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.539 MB | 18.539 MB | 211.160 MB | 211.160 MB | n/a MB | n/a MB |
| python | 4364 | sandbox_agent_lsb-native_0000_0000 | 2 | 193.445% | 193.445% | 1.950 s | 197.850 MB | 324.066 MB | 406.479 MB | 537.301 MB | n/a MB | n/a MB |
| bash | 4363 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 4383 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4420 | sandbox_agent_lsb-native_0000_0000 | 4 | 183.570% | 197.833% | 5.540 s | 220.431 MB | 303.941 MB | 430.704 MB | 518.500 MB | n/a MB | n/a MB |
| bash | 4419 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.789 MB | 2.789 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 4428 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4469 | sandbox_agent_lsb-native_0000_0000 | 2 | 167.547% | 167.547% | 1.690 s | 194.369 MB | 231.902 MB | 412.865 MB | 453.059 MB | n/a MB | n/a MB |
| bash | 4468 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.949 MB | 2.949 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4491 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 116.367 MB | 116.367 MB | 335.422 MB | 335.422 MB | n/a MB | n/a MB |
| sleep | 4499 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| docker | 4541 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.621 MB | 30.621 MB | 1843.254 MB | 1843.254 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4664 |  | 13 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 4.622% | 100.000% | 12101.892 MB | 12758.000 MB | 30.939 W | 73.123 W | 21301.871 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 15.858% | 205.215% | 105.246 s | 199.350 MB | 1070.457 MB | 3.175781 MB | 90.019531 MB | 0.000978 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 3601 | 690.046 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 664.742 | n/a | n/a | 3.176 | 664742.101 | 664742.101 | 664742.101 |
| engine:execute | 1/1 | 0 | 0 | 664.740 | 1.436 | 663.305 | 3.176 | 664740.486 | 664740.486 | 664740.486 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 638.271 | 0.002 | 638.269 | 3.176 | 638271.054 | 638271.054 | 638271.054 |
| turn | 60/60 | 0 | 0 | 635.379 | n/a | n/a | 3.162 | 10589.658 | 6814.522 | 34754.222 |
| llm:attempt | 60/60 | 0 | 0 | 535.510 | 13.646 | 521.862 | 0.886 | 8925.174 | 5015.279 | 32335.902 |
| tool:bash | 27/27 | 0 | 0 | 43.554 | n/a | n/a | 2.126 | 1613.104 | 421.194 | 4096.157 |
| process:bash | 27/27 | 2 | 0 | 43.255 | n/a | n/a | 2.110 | 1602.030 | 411.748 | 4078.235 |
| run:container_call | 13/13 | 0 | 0 | 23.168 | 0.002 | 23.166 | 0.000 | 1782.161 | 35.805 | 9121.315 |
| teardown:commit | 1/1 | 0 | 0 | 22.747 | 0.004 | 22.743 | 0.000 | 22747.463 | 22747.463 | 22747.463 |
| sandbox:commit | 1/1 | 0 | 0 | 22.570 | 0.002 | 22.568 | 0.000 | 22569.763 | 22569.763 | 22569.763 |
| checkpoint.total | 1/1 | 0 | 0 | 22.570 | 0.002 | 22.568 | 0.000 | 22569.628 | 22569.628 | 22569.628 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.569 | 0.002 | 22.568 | 0.000 | 22569.483 | 22569.483 | 22569.483 |
| tool:generate | 5/5 | 0 | 0 | 20.709 | n/a | n/a | 0.000 | 4141.776 | 3932.604 | 5603.914 |
| tool:trace | 8/8 | 0 | 0 | 16.152 | n/a | n/a | 0.000 | 2019.010 | 1763.366 | 2957.654 |
| tool:patch | 9/9 | 0 | 0 | 3.964 | n/a | n/a | 0.000 | 440.440 | 433.972 | 470.761 |
| tool:inspect | 1/1 | 0 | 0 | 3.707 | n/a | n/a | 0.000 | 3707.370 | 3707.370 | 3707.370 |
| tool:inspect_module_inputs | 1/1 | 0 | 0 | 3.619 | n/a | n/a | 0.000 | 3619.039 | 3619.039 | 3619.039 |
| syscall:sendto | 1349/1349 | 0 | 0 | 3.256 | n/a | n/a | 0.072 | 2.413 | 2.114 | 4.785 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.075 | 0.687 | 2.388 | 0.000 | 3074.991 | 3074.991 | 3074.991 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.075 | 0.687 | 2.388 | 0.000 | 3074.674 | 3074.674 | 3074.674 |
| tool:token_stats | 1/1 | 0 | 0 | 1.918 | n/a | n/a | 0.000 | 1917.815 | 1917.815 | 1917.815 |
| syscall:connect | 328/328 | 0 | 0 | 0.804 | n/a | n/a | 0.021 | 2.451 | 2.127 | 5.013 |
| sandbox:start | 1/1 | 0 | 0 | 0.352 | 0.002 | 0.349 | 0.000 | 351.573 | 351.573 | 351.573 |
| runtime.container_create | 1/1 | 0 | 0 | 0.351 | 0.002 | 0.349 | 0.000 | 351.429 | 351.429 | 351.429 |
| sandbox:create | 1/1 | 0 | 0 | 0.339 | 0.246 | 0.094 | 0.000 | 339.275 | 339.275 | 339.275 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.312 | n/a | n/a | 0.000 | 312.361 | 312.361 | 312.361 |
| syscall:execve | 179/179 | 0 | 0 | 0.240 | n/a | n/a | 0.014 | 1.343 | 1.174 | 2.826 |
| tool:submit_output | 1/1 | 0 | 0 | 0.235 | n/a | n/a | 0.000 | 234.955 | 234.955 | 234.955 |
| agency:services_close | 1/1 | 0 | 0 | 0.178 | 0.001 | 0.177 | 0.000 | 177.821 | 177.821 | 177.821 |
| sandbox:stop | 1/1 | 0 | 0 | 0.177 | 0.002 | 0.176 | 0.000 | 177.455 | 177.455 | 177.455 |
| agency:services_start | 1/1 | 0 | 0 | 0.072 | 0.041 | 0.031 | 0.000 | 72.477 | 72.477 | 72.477 |
| run:detect | 1/1 | 0 | 0 | 0.052 | 0.001 | 0.052 | 0.000 | 52.395 | 52.395 | 52.395 |
| agent:create | 1/1 | 0 | 0 | 0.050 | 0.010 | 0.040 | 0.000 | 49.514 | 49.514 | 49.514 |
| tool:write | 9/9 | 0 | 0 | 0.004 | n/a | n/a | 0.000 | 0.417 | 0.368 | 0.534 |
| tool:edit | 2/2 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.636 | 0.636 | 0.720 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.188 | 1.188 | 1.188 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.072 | 0.079 | 0.095 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.860 | 0.860 | 0.860 |
| tool:todowrite | 2/2 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.177 | 0.177 | 0.209 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.170 | 0.170 | 0.170 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.079 | 0.079 | 0.079 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 684 | 1.169 | 0.039 | 46.348 | 0.085 | 8.050680 CPU seconds | n/a |
| GPU 0 memory | MB | 685 | 12101.892 | 11670.000 | 12758.000 | 11998.000 | n/a | n/a |
| GPU 0 power | W | 685 | 30.939 | 28.336 | 73.123 | 28.519 | n/a | 21301.871 J |
| GPU 0 proc / 3429-83697 / sandbox / ~ / device / GPU-37fda935-706b-7e26-d2bf-d58a17d64021 memory | MB | 685 | 3376.975 | 3118.000 | 3982.000 | 3222.000 | n/a | n/a |
| GPU 0 proc / 3429-83697 / sandbox / ~ / device / GPU-37fda935-706b-7e26-d2bf-d58a17d64021 estimated power | W | 515 | 3.141 | 0.000 | 71.172 | 0.000 | n/a | n/a |
| GPU 0 proc / 3429-83697 / sandbox / ~ / device / GPU-37fda935-706b-7e26-d2bf-d58a17d64021 utilization | percent | 515 | 2.571 | 0.000 | 87.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 3494-85542 / sandbox / ~ / device / GPU-37fda935-706b-7e26-d2bf-d58a17d64021 memory | MB | 685 | 8242.917 | 8070.000 | 8294.000 | 8294.000 | n/a | n/a |
| GPU 0 proc / 3494-85542 / sandbox / ~ / device / GPU-37fda935-706b-7e26-d2bf-d58a17d64021 estimated power | W | 164 | 8.303 | 0.000 | 71.687 | 0.000 | n/a | n/a |
| GPU 0 proc / 3494-85542 / sandbox / ~ / device / GPU-37fda935-706b-7e26-d2bf-d58a17d64021 utilization | percent | 164 | 11.360 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 685 | 11619.892 | 11188.000 | 12276.000 | 11516.000 | n/a | n/a |
| GPU 0 utilization | percent | 685 | 4.622 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 685 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 684 | 2.495 | 0.008 | 54.999 | 0.221 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 684 | 6.462 | 0.000 | 52.463 | 0.000 | n/a | n/a |
| host disk_read_mb_s | MB/s | 684 | 2.389 | 0.000 | 191.193 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 684 | 1.245 | 0.000 | 76.147 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 684 | 1.084 | 0.000 | 65.628 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 684 | 1.094 | 0.000 | 65.867 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 685 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 685 | 7204.132 | 6655.547 | 7991.352 | 7355.668 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 684 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 684 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 684 | 0.028 | 0.000 | 0.150 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 684 | 0.032 | 0.000 | 0.561 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3420) CPU | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 3420) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3420) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3420) rss_mb | MB | 685 | 3.398 | 3.398 | 3.398 | 3.398 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3420) main thread run-queue wait | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 3420) vms_mb | MB | 685 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3429) CPU | percent | 684 | 7.287 | 0.000 | 137.092 | 0.996 | 50.230000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 3429) io read MB/s | MB/s | 684 | 0.007 | 0.000 | 1.703 | 0.000 | 4.957031 MB | n/a |
| Agency harness — python -m lsbench (PID 3429) io write MB/s | MB/s | 684 | 1.159 | 0.015 | 103.888 | 0.023 | 799.882812 MB | n/a |
| Agency harness — python -m lsbench (PID 3429) rss_mb | MB | 685 | 3126.820 | 2538.477 | 3466.480 | 3434.191 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3429) main thread run-queue wait | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 3429) vms_mb | MB | 685 | 16383.709 | 14115.879 | 17372.906 | 16556.504 | n/a | n/a |
| Python — vllm (PID 3434) CPU | percent | 684 | 0.228 | 0.000 | 5.972 | 0.000 | 1.570000 CPU seconds | n/a |
| Python — vllm (PID 3434) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 3434) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.008 | 0.000 | 0.031250 MB | n/a |
| Python — vllm (PID 3434) rss_mb | MB | 685 | 1803.829 | 1802.703 | 1804.203 | 1804.203 | n/a | n/a |
| Python — vllm (PID 3434) main thread run-queue wait | percent | 684 | 0.005 | 0.000 | 0.529 | 0.000 | 0.031794 run-queue seconds | n/a |
| Python — vllm (PID 3434) vms_mb | MB | 685 | 11038.633 | 10971.477 | 11044.496 | 11044.496 | n/a | n/a |
| bash lsb_guard.sh (PID 3440) CPU | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 3440) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3440) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3440) rss_mb | MB | 685 | 3.270 | 3.270 | 3.270 | 3.270 | n/a | n/a |
| bash lsb_guard.sh (PID 3440) main thread run-queue wait | percent | 684 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000017 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 3440) vms_mb | MB | 685 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sleep (PID 3443) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3443) io read MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3443) io write MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3443) rss_mb | MB | 16 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3443) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3443) vms_mb | MB | 16 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — python -c (PID 3493) CPU | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 3493) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3493) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3493) rss_mb | MB | 685 | 12.184 | 12.184 | 12.184 | 12.184 | n/a | n/a |
| Python — python -c (PID 3493) main thread run-queue wait | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 3493) vms_mb | MB | 685 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 3494) CPU | percent | 684 | 2.617 | 0.000 | 61.336 | 1.991 | 18.040000 CPU seconds | n/a |
| VLLM::EngineCore (PID 3494) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 3494) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 3494) rss_mb | MB | 685 | 2321.145 | 2321.125 | 2321.250 | 2321.250 | n/a | n/a |
| VLLM::EngineCore (PID 3494) main thread run-queue wait | percent | 684 | 0.002 | 0.000 | 0.349 | 0.000 | 0.010405 run-queue seconds | n/a |
| VLLM::EngineCore (PID 3494) vms_mb | MB | 685 | 21203.379 | 21203.379 | 21203.379 | 21203.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3711) CPU | percent | 659 | 0.003 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3711) rss_mb | MB | 660 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3711) main thread run-queue wait | percent | 659 | 0.009 | 0.000 | 4.850 | 0.000 | 0.057935 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3711) vms_mb | MB | 660 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3742) CPU | percent | 659 | 0.002 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3742) rss_mb | MB | 660 | 1.566 | 1.566 | 1.566 | 1.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3742) main thread run-queue wait | percent | 659 | 0.008 | 0.000 | 4.834 | 0.000 | 0.052613 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3742) vms_mb | MB | 660 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3834) CPU | percent | 659 | 5.556 | 0.000 | 87.058 | 0.000 | 36.870000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3834) rss_mb | MB | 660 | 102.825 | 3.023 | 107.078 | 106.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3834) main thread run-queue wait | percent | 659 | 0.000 | 0.000 | 0.013 | 0.000 | 0.000196 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3834) vms_mb | MB | 660 | 963.532 | 4.258 | 972.160 | 972.113 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3840) CPU | percent | 1 | 99.857 | 99.857 | 99.857 | 99.857 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3840) rss_mb | MB | 2 | 54.473 | 26.664 | 82.281 | 82.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3840) main thread run-queue wait | percent | 1 | 0.008 | 0.008 | 0.008 | 0.008 | 0.000079 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3840) vms_mb | MB | 2 | 66.738 | 35.480 | 97.996 | 97.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3852) CPU | percent | 632 | 0.400 | 0.000 | 60.570 | 1.982 | 2.550000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3852) rss_mb | MB | 633 | 71.881 | 31.574 | 74.180 | 73.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3852) main thread run-queue wait | percent | 632 | 0.020 | 0.000 | 1.673 | 1.673 | 0.130184 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3852) vms_mb | MB | 633 | 86.204 | 37.547 | 88.102 | 88.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3881) rss_mb | MB | 1 | 2.781 | 2.781 | 2.781 | 2.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3881) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3882) rss_mb | MB | 1 | 14.320 | 14.320 | 14.320 | 14.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3882) vms_mb | MB | 1 | 1874.164 | 1874.164 | 1874.164 | 1874.164 | n/a | n/a |
| sleep (PID 3892) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3892) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3892) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3892) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3892) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3892) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3927) rss_mb | MB | 1 | 2.746 | 2.746 | 2.746 | 2.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3927) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 3928) rss_mb | MB | 1 | 12.598 | 12.598 | 12.598 | 12.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 3928) vms_mb | MB | 1 | 16.016 | 16.016 | 16.016 | 16.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_clean_palindrome.py (PID 3940) rss_mb | MB | 1 | 7.234 | 7.234 | 7.234 | 7.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_clean_palindrome.py (PID 3940) vms_mb | MB | 1 | 11.785 | 11.785 | 11.785 | 11.785 | n/a | n/a |
| sleep (PID 3958) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3958) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3958) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3958) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3958) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3958) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3981) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3981) rss_mb | MB | 4 | 2.727 | 2.727 | 2.727 | 2.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3981) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3981) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 3982) CPU | percent | 3 | 0.662 | 0.000 | 1.987 | 1.987 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 3982) rss_mb | MB | 4 | 12.168 | 12.137 | 12.262 | 12.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 3982) main thread run-queue wait | percent | 3 | 0.001 | 0.000 | 0.004 | 0.004 | 0.000043 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 3982) vms_mb | MB | 4 | 15.781 | 15.781 | 15.781 | 15.781 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_rle.py (PID 3992) CPU | percent | 2 | 99.901 | 99.366 | 100.435 | 100.435 | 2.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_rle.py (PID 3992) rss_mb | MB | 3 | 536.812 | 146.812 | 927.188 | 927.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_rle.py (PID 3992) main thread run-queue wait | percent | 2 | 0.004 | 0.003 | 0.005 | 0.003 | 0.000085 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_rle.py (PID 3992) vms_mb | MB | 3 | 549.615 | 152.434 | 948.637 | 948.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_days_between.py (PID 4005) rss_mb | MB | 1 | 7.660 | 7.660 | 7.660 | 7.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_days_between.py (PID 4005) vms_mb | MB | 1 | 12.918 | 12.918 | 12.918 | 12.918 | n/a | n/a |
| sleep (PID 4020) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4020) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4020) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4020) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4020) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4020) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4045) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4045) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4045) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4045) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4045) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4045) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_local.py (PID 4060) CPU | percent | 3 | 167.952 | 166.980 | 169.070 | 166.980 | 5.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_local.py (PID 4060) rss_mb | MB | 4 | 99.589 | 69.887 | 113.949 | 107.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_local.py (PID 4060) main thread run-queue wait | percent | 3 | 59.486 | 54.995 | 62.160 | 54.995 | 1.795738 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_local.py (PID 4060) vms_mb | MB | 4 | 320.858 | 291.289 | 335.184 | 328.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4077) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4077) rss_mb | MB | 4 | 2.938 | 2.938 | 2.938 | 2.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4077) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4077) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ridge_scan.py (PID 4078) CPU | percent | 3 | 189.145 | 188.788 | 189.848 | 189.848 | 5.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ridge_scan.py (PID 4078) rss_mb | MB | 4 | 124.528 | 114.789 | 128.703 | 128.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ridge_scan.py (PID 4078) main thread run-queue wait | percent | 3 | 55.732 | 51.068 | 58.374 | 51.068 | 1.682481 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — ridge_scan.py (PID 4078) vms_mb | MB | 4 | 344.606 | 335.070 | 348.648 | 348.648 | n/a | n/a |
| sleep (PID 4086) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4086) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4086) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4086) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4086) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4086) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4125) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4125) rss_mb | MB | 4 | 12.426 | 12.426 | 12.426 | 12.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4125) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — evaluate.py (PID 4125) vms_mb | MB | 4 | 15.789 | 15.789 | 15.789 | 15.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_rle.py (PID 4135) CPU | percent | 2 | 100.435 | 100.400 | 100.470 | 100.470 | 2.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_rle.py (PID 4135) rss_mb | MB | 3 | 436.866 | 47.699 | 825.824 | 825.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_rle.py (PID 4135) main thread run-queue wait | percent | 2 | 0.001 | 0.001 | 0.001 | 0.001 | 0.000017 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_rle.py (PID 4135) vms_mb | MB | 3 | 448.467 | 52.570 | 842.688 | 842.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_clean_palindrome.py (PID 4137) rss_mb | MB | 1 | 8.168 | 8.168 | 8.168 | 8.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_clean_palindrome.py (PID 4137) vms_mb | MB | 1 | 13.020 | 13.020 | 13.020 | 13.020 | n/a | n/a |
| sleep (PID 4163) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4163) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4163) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4163) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4163) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4163) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4174) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4174) rss_mb | MB | 3 | 2.969 | 2.969 | 2.969 | 2.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4174) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4174) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4175) CPU | percent | 2 | 98.378 | 98.315 | 98.441 | 98.441 | 1.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4175) rss_mb | MB | 3 | 113.331 | 109.207 | 116.086 | 116.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4175) main thread run-queue wait | percent | 2 | 0.004 | 0.003 | 0.005 | 0.005 | 0.000086 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4175) vms_mb | MB | 3 | 305.785 | 304.090 | 307.270 | 307.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4188) rss_mb | MB | 1 | 2.891 | 2.891 | 2.891 | 2.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4188) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reply_scan.py (PID 4189) rss_mb | MB | 1 | 13.277 | 13.277 | 13.277 | 13.277 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reply_scan.py (PID 4189) vms_mb | MB | 1 | 207.391 | 207.391 | 207.391 | 207.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4202) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4202) rss_mb | MB | 10 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4202) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4202) vms_mb | MB | 10 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reply_scan.py (PID 4203) CPU | percent | 9 | 189.911 | 185.469 | 197.134 | 185.899 | 17.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reply_scan.py (PID 4203) rss_mb | MB | 10 | 146.886 | 79.133 | 169.547 | 162.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reply_scan.py (PID 4203) main thread run-queue wait | percent | 9 | 53.124 | 46.331 | 57.646 | 52.089 | 4.822266 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reply_scan.py (PID 4203) vms_mb | MB | 10 | 362.717 | 296.238 | 385.285 | 378.152 | n/a | n/a |
| sleep (PID 4208) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4208) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4208) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4208) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4208) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4208) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4235) rss_mb | MB | 1 | 2.906 | 2.906 | 2.906 | 2.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4235) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4236) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4236) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sleep (PID 4341) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4341) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4341) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4341) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4341) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4341) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4349) rss_mb | MB | 1 | 2.973 | 2.973 | 2.973 | 2.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4349) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4350) rss_mb | MB | 1 | 18.539 | 18.539 | 18.539 | 18.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4350) vms_mb | MB | 1 | 211.160 | 211.160 | 211.160 | 211.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4363) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4363) rss_mb | MB | 2 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4363) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4363) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_layer_scan.py (PID 4364) CPU | percent | 1 | 193.445 | 193.445 | 193.445 | 193.445 | 1.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_layer_scan.py (PID 4364) rss_mb | MB | 2 | 197.850 | 71.633 | 324.066 | 324.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_layer_scan.py (PID 4364) main thread run-queue wait | percent | 1 | 43.099 | 43.099 | 43.099 | 43.099 | 0.434457 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_layer_scan.py (PID 4364) vms_mb | MB | 2 | 406.479 | 275.656 | 537.301 | 537.301 | n/a | n/a |
| sleep (PID 4383) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4383) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4383) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4383) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4383) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4383) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4419) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4419) rss_mb | MB | 4 | 2.789 | 2.789 | 2.789 | 2.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4419) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4419) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — combined_scan.py (PID 4420) CPU | percent | 3 | 183.570 | 155.053 | 197.833 | 197.824 | 5.540000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — combined_scan.py (PID 4420) rss_mb | MB | 4 | 220.431 | 14.023 | 303.941 | 303.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — combined_scan.py (PID 4420) main thread run-queue wait | percent | 3 | 44.575 | 32.370 | 51.592 | 51.592 | 1.345236 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — combined_scan.py (PID 4420) vms_mb | MB | 4 | 430.704 | 208.668 | 518.500 | 518.500 | n/a | n/a |
| sleep (PID 4428) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4428) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4428) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4428) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4428) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4428) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4468) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4468) rss_mb | MB | 2 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4468) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4468) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_candidate.py (PID 4469) CPU | percent | 1 | 167.547 | 167.547 | 167.547 | 167.547 | 1.690000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_candidate.py (PID 4469) rss_mb | MB | 2 | 194.369 | 156.836 | 231.902 | 231.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_candidate.py (PID 4469) main thread run-queue wait | percent | 1 | 53.913 | 53.913 | 53.913 | 53.913 | 0.543810 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_candidate.py (PID 4469) vms_mb | MB | 2 | 412.865 | 372.672 | 453.059 | 453.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_candidate.py (PID 4491) rss_mb | MB | 1 | 116.367 | 116.367 | 116.367 | 116.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — verify_candidate.py (PID 4491) vms_mb | MB | 1 | 335.422 | 335.422 | 335.422 | 335.422 | n/a | n/a |
| sleep (PID 4499) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4499) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4499) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4499) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4499) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4499) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| docker commit (PID 4541) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4541) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4541) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4541) rss_mb | MB | 22 | 30.621 | 30.621 | 30.621 | 30.621 | n/a | n/a |
| docker commit (PID 4541) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4541) vms_mb | MB | 22 | 1843.254 | 1843.254 | 1843.254 | 1843.254 | n/a | n/a |
| sleep (PID 4664) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4664) io read MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4664) io write MB/s | MB/s | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4664) rss_mb | MB | 13 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4664) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4664) vms_mb | MB | 13 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 659 | 15.858 | 0.000 | 205.215 | 0.000 | 105.245569 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 659 | 2.193 | 0.000 | 50.261 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 659 | 2.411 | 0.000 | 54.276 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 659 | 0.001 | 0.000 | 0.261 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 659 | 0.002 | 0.000 | 0.261 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 659 | 0.005 | 0.000 | 1.103 | 0.000 | 3.175781 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 659 | 0.136 | 0.000 | 71.581 | 0.000 | 90.019531 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 660 | 199.350 | 17.406 | 1070.457 | 187.270 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 659 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 659 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 659 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000978 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 659 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 684 | 10.182 | 1.436 | 138.042 | 2.034 | 70.186152 CPU seconds | n/a |
| workload total memory | MB | 685 | 5895.329 | 5196.906 | 6373.977 | 6363.664 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
