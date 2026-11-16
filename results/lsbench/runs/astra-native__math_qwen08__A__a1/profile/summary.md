# agprof summary

- Duration: **1918.328 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **37 calls**, 37 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1356.597 s total wait
- Tools: **52/52 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **177442** at 1.973 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1918258.814 / 1918258.814 ms |
| LLM latency p50 / p95 | 28677.804 / 89922.776 ms |
| LLM TTFT p50 / p95 | 14734.218 / 27186.724 ms |
| LLM input / output tokens | 3993651 / 55298 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 37 total, 37 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1330.431 / 43799.460 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attribution | 2/2 | 2 | 0 | 0 | 311.593 ms | 311.793 ms |
| bash | 23/23 | 23 | 0 | 0 | 828.124 ms | 3740.248 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 320.275 ms | 320.275 ms |
| generate | 7/7 | 7 | 0 | 0 | 43498.110 ms | 141319.696 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 3499.656 ms | 3499.656 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 222.821 ms | 222.821 ms |
| todowrite | 3/3 | 3 | 0 | 0 | 0.143 ms | 0.186 ms |
| top_activations | 4/4 | 4 | 0 | 0 | 15883.323 ms | 16061.009 ms |
| trace | 9/9 | 9 | 0 | 0 | 10510.156 ms | 15195.239 ms |
| write | 1/1 | 1 | 0 | 0 | 0.416 ms | 0.416 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 16.962% | 313.833% | 326.141 s | 5553.060 MB | 6062.531 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker-init | 5114 | sandbox_agent_lsb-native_0000_0000 | 1906 | 0.003% | 0.995% | 0.050 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 5153 | sandbox_agent_lsb-native_0000_0000 | 1906 | 0.002% | 0.996% | 0.040 s | 1.562 MB | 1.562 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 5254 | sandbox_agent_lsb-native_0000_0000 | 1906 | 2.818% | 90.905% | 54.030 s | 103.092 MB | 108.828 MB | 968.932 MB | 972.898 MB | n/a MB | n/a MB |
| python3 | 5260 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.910% | 99.910% | 1.010 s | 55.996 MB | 82.441 MB | 67.586 MB | 98.148 MB | n/a MB | n/a MB |
| python | 4725 |  | 1906 | 9.050% | 313.119% | 174.130 s | 2659.682 MB | 2973.430 MB | 15992.148 MB | 18015.660 MB | 2.121094 MB | 938.855469 MB |
| python | 4784 |  | 1906 | 0.000% | 0.000% | 0.000 s | 12.336 MB | 12.336 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 4734 |  | 1906 | 0.606% | 4.977% | 11.650 s | 1806.635 MB | 1807.410 MB | 12015.683 MB | 12017.773 MB | 0.003906 MB | 0.078125 MB |
| VLLM::EngineCor | 4785 |  | 1906 | 7.301% | 39.642% | 140.270 s | 2342.012 MB | 2342.188 MB | 21863.603 MB | 21863.836 MB | 0.000000 MB | 0.011719 MB |
| lsb_agency_reru | 4681 |  | 1906 | 0.000% | 0.000% | 0.000 s | 3.379 MB | 3.379 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python3 | 5272 | sandbox_agent_lsb-native_0000_0000 | 1880 | 0.116% | 59.434% | 2.210 s | 72.430 MB | 75.270 MB | 86.895 MB | 89.898 MB | n/a MB | n/a MB |
| bash | 5793 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 5795 | sandbox_agent_lsb-native_0000_0000 | 4 | 148.161% | 173.069% | 4.470 s | 75.439 MB | 100.410 MB | 323.184 MB | 397.926 MB | n/a MB | n/a MB |
| bash | 6072 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.801 MB | 2.801 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6073 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.598 MB | 14.598 MB | 368.465 MB | 368.465 MB | n/a MB | n/a MB |
| bash | 6131 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.039 MB | 3.039 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6135 | sandbox_agent_lsb-native_0000_0000 | 3 | 159.564% | 195.856% | 3.210 s | 483.846 MB | 727.828 MB | 693.490 MB | 986.305 MB | n/a MB | n/a MB |
| bash | 6142 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.949 MB | 2.949 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6143 | sandbox_agent_lsb-native_0000_0000 | 3 | 165.454% | 204.801% | 3.340 s | 356.671 MB | 698.613 MB | 1080.740 MB | 1437.355 MB | n/a MB | n/a MB |
| bash | 6166 | sandbox_agent_lsb-native_0000_0000 | 3 | 90.991% | 129.299% | 1.830 s | 146.971 MB | 272.973 MB | 429.822 MB | 1008.945 MB | n/a MB | n/a MB |
| python | 6168 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 120.082 MB | 120.082 MB | 472.672 MB | 472.672 MB | n/a MB | n/a MB |
| bash | 6191 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.000 MB | 3.000 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6193 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 233.320 MB | 233.320 MB | 972.953 MB | 972.953 MB | n/a MB | n/a MB |
| python | 6201 | sandbox_agent_lsb-native_0000_0000 | 5 | 190.154% | 198.913% | 7.650 s | 614.849 MB | 731.496 MB | 1346.928 MB | 1470.871 MB | n/a MB | n/a MB |
| bash | 6200 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 3.121 MB | 3.121 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 6296 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.004 MB | 3.004 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6297 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 78.117 MB | 78.117 MB | 429.172 MB | 429.172 MB | n/a MB | n/a MB |
| bash | 6343 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.816 MB | 2.816 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6344 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 179.379 MB | 179.379 MB | 885.793 MB | 885.793 MB | n/a MB | n/a MB |
| bash | 6372 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.793 MB | 2.793 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6373 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 181.555 MB | 181.555 MB | 886.953 MB | 886.953 MB | n/a MB | n/a MB |
| python | 6395 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 208.031 MB | 208.031 MB | 489.094 MB | 489.094 MB | n/a MB | n/a MB |
| python | 6433 | sandbox_agent_lsb-native_0000_0000 | 4 | 172.679% | 198.897% | 5.210 s | 451.768 MB | 826.391 MB | 1298.337 MB | 1631.711 MB | n/a MB | n/a MB |
| bash | 6432 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.000 MB | 3.000 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 6502 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 145.539 MB | 145.539 MB | 256.734 MB | 256.734 MB | n/a MB | n/a MB |
| bash | 6499 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.797 MB | 2.797 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| docker | 6577 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.234 MB | 30.234 MB | 2059.773 MB | 2059.773 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 25.034% | 100.000% | 11961.028 MB | 13528.000 MB | 40.441 W | 78.083 W | 77595.103 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 5.419% | 205.572% | 103.928 s | 173.762 MB | 531.781 MB | 28.218750 MB | 8.273438 MB | 0.001045 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4978 | 1918.263 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1918.259 | n/a | n/a | 28.219 | 1918258.814 | 1918258.814 | 1918258.814 |
| sync:result_wait | 1/1 | 0 | 0 | 1918.258 | 0.000 | 1918.258 | 28.219 | 1918258.040 | 1918258.040 | 1918258.040 |
| engine:execute | 1/1 | 0 | 0 | 1918.257 | 2.187 | 1916.070 | 28.219 | 1918257.329 | 1918257.329 | 1918257.329 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1892.504 | 0.003 | 1892.501 | 28.219 | 1892504.426 | 1892504.426 | 1892504.426 |
| turn | 37/37 | 0 | 0 | 1890.086 | n/a | n/a | 28.210 | 51083.402 | 45005.466 | 111085.690 |
| llm:attempt | 37/37 | 0 | 0 | 1356.597 | 4.451 | 1352.144 | 0.475 | 36664.781 | 28677.804 | 89922.776 |
| tool:generate | 7/7 | 0 | 0 | 367.877 | n/a | n/a | 0.046 | 52553.856 | 43498.110 | 141319.696 |
| tool:trace | 9/9 | 0 | 0 | 75.527 | n/a | n/a | 0.000 | 8391.867 | 10510.156 | 15195.239 |
| tool:top_activations | 4/4 | 0 | 0 | 48.073 | n/a | n/a | 0.000 | 12018.195 | 15883.323 | 16061.009 |
| tool:bash | 23/23 | 0 | 0 | 33.766 | n/a | n/a | 27.568 | 1468.100 | 828.124 | 3740.248 |
| process:bash | 23/23 | 1 | 0 | 33.562 | n/a | n/a | 27.559 | 1459.196 | 820.460 | 3731.268 |
| run:container_call | 13/13 | 0 | 0 | 22.487 | 0.002 | 22.484 | 0.000 | 1729.740 | 33.358 | 8851.358 |
| teardown:commit | 1/1 | 0 | 0 | 22.085 | 0.004 | 22.081 | 0.000 | 22085.027 | 22085.027 | 22085.027 |
| sandbox:commit | 1/1 | 0 | 0 | 21.895 | 0.002 | 21.893 | 0.000 | 21895.162 | 21895.162 | 21895.162 |
| checkpoint.total | 1/1 | 0 | 0 | 21.895 | 0.002 | 21.893 | 0.000 | 21894.926 | 21894.926 | 21894.926 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 21.895 | 0.002 | 21.893 | 0.000 | 21894.758 | 21894.758 | 21894.758 |
| tool:logit_lens | 1/1 | 0 | 0 | 3.500 | n/a | n/a | 0.000 | 3499.656 | 3499.656 | 3499.656 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.066 | 0.698 | 2.368 | 0.000 | 3066.297 | 3066.297 | 3066.297 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.066 | 0.698 | 2.368 | 0.000 | 3066.105 | 3066.105 | 3066.105 |
| syscall:sendto | 1091/1091 | 0 | 0 | 2.262 | n/a | n/a | 0.053 | 2.073 | 1.828 | 4.038 |
| syscall:connect | 304/304 | 0 | 0 | 0.628 | n/a | n/a | 0.025 | 2.066 | 1.800 | 4.214 |
| tool:attribution | 2/2 | 0 | 0 | 0.623 | n/a | n/a | 0.000 | 311.593 | 311.593 | 311.793 |
| sandbox:start | 1/1 | 0 | 0 | 0.338 | 0.002 | 0.335 | 0.000 | 337.665 | 337.665 | 337.665 |
| runtime.container_create | 1/1 | 0 | 0 | 0.338 | 0.002 | 0.335 | 0.000 | 337.522 | 337.522 | 337.522 |
| sandbox:create | 1/1 | 0 | 0 | 0.327 | 0.243 | 0.085 | 0.000 | 327.070 | 327.070 | 327.070 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.320 | n/a | n/a | 0.000 | 320.275 | 320.275 | 320.275 |
| tool:submit_output | 1/1 | 0 | 0 | 0.223 | n/a | n/a | 0.000 | 222.821 | 222.821 | 222.821 |
| sandbox:stop | 1/1 | 0 | 0 | 0.190 | 0.002 | 0.188 | 0.000 | 189.556 | 189.556 | 189.556 |
| agency:services_close | 1/1 | 0 | 0 | 0.141 | 0.000 | 0.140 | 0.000 | 140.868 | 140.868 | 140.868 |
| syscall:execve | 92/92 | 0 | 0 | 0.123 | n/a | n/a | 0.009 | 1.341 | 1.146 | 2.164 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.042 | 0.031 | 0.000 | 73.186 | 73.186 | 73.186 |
| agent:create | 1/1 | 0 | 0 | 0.050 | 0.009 | 0.041 | 0.000 | 49.738 | 49.738 | 49.738 |
| run:detect | 1/1 | 0 | 0 | 0.049 | 0.001 | 0.048 | 0.000 | 49.076 | 49.076 | 49.076 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.002 | 0.002 | 0.000 | 0.000 | 1.761 | 1.761 | 1.761 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.230 | 1.230 | 1.230 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.071 | 0.070 | 0.109 |
| tool:todowrite | 3/3 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.157 | 0.143 | 0.186 |
| tool:write | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.416 | 0.416 | 0.416 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.189 | 0.189 | 0.189 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.065 | 0.065 | 0.065 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1905 | 0.433 | 0.032 | 49.016 | 37.524 | 8.290237 CPU seconds | n/a |
| GPU 0 memory | MB | 1906 | 11961.028 | 11670.000 | 13528.000 | 11984.000 | n/a | n/a |
| GPU 0 power | W | 1906 | 40.441 | 27.372 | 78.083 | 28.583 | n/a | 77595.103 J |
| GPU 0 proc / 4725-86942 / sandbox / ~ / device / GPU-f2dcbfb8-339a-77d4-96df-de091d1106da memory | MB | 1906 | 3238.082 | 3118.000 | 4816.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 4725-86942 / sandbox / ~ / device / GPU-f2dcbfb8-339a-77d4-96df-de091d1106da estimated power | W | 1311 | 6.258 | 0.000 | 75.562 | 0.000 | n/a | n/a |
| GPU 0 proc / 4725-86942 / sandbox / ~ / device / GPU-f2dcbfb8-339a-77d4-96df-de091d1106da utilization | percent | 1311 | 8.337 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 4785-88696 / sandbox / ~ / device / GPU-f2dcbfb8-339a-77d4-96df-de091d1106da memory | MB | 1906 | 8240.946 | 8070.000 | 8316.000 | 8316.000 | n/a | n/a |
| GPU 0 proc / 4785-88696 / sandbox / ~ / device / GPU-f2dcbfb8-339a-77d4-96df-de091d1106da estimated power | W | 567 | 44.744 | 0.000 | 72.444 | 0.000 | n/a | n/a |
| GPU 0 proc / 4785-88696 / sandbox / ~ / device / GPU-f2dcbfb8-339a-77d4-96df-de091d1106da utilization | percent | 567 | 61.743 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1906 | 11479.028 | 11188.000 | 13046.000 | 11502.000 | n/a | n/a |
| GPU 0 utilization | percent | 1906 | 25.034 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1906 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1905 | 0.763 | 0.011 | 75.948 | 0.638 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1905 | 2.731 | 0.125 | 39.281 | 3.836 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1905 | 0.870 | 0.000 | 221.619 | 10.698 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1905 | 0.527 | 0.000 | 244.518 | 0.494 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1905 | 0.466 | 0.000 | 94.151 | 16.486 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1905 | 0.467 | 0.000 | 94.565 | 16.504 | n/a | n/a |
| host mem_total_mb | MB | 1906 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 1906 | 6933.053 | 6433.020 | 7484.109 | 7195.809 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1905 | 0.000 | 0.000 | 0.010 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1905 | 0.000 | 0.000 | 0.028 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1905 | 0.003 | 0.000 | 0.254 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1905 | 0.009 | 0.000 | 0.905 | 0.000 | n/a | n/a |
| bash lsb_agency_rerun.sh (PID 4681) CPU | percent | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_agency_rerun.sh (PID 4681) io read MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_agency_rerun.sh (PID 4681) io write MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_agency_rerun.sh (PID 4681) rss_mb | MB | 1906 | 3.379 | 3.379 | 3.379 | 3.379 | n/a | n/a |
| bash lsb_agency_rerun.sh (PID 4681) main thread run-queue wait | percent | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_agency_rerun.sh (PID 4681) vms_mb | MB | 1906 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4725) CPU | percent | 1905 | 9.050 | 0.000 | 313.119 | 0.000 | 174.130000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 4725) io read MB/s | MB/s | 1905 | 0.001 | 0.000 | 1.978 | 0.000 | 2.121094 MB | n/a |
| Agency harness — python -m lsbench (PID 4725) io write MB/s | MB/s | 1905 | 0.488 | 0.015 | 430.273 | 0.023 | 938.855469 MB | n/a |
| Agency harness — python -m lsbench (PID 4725) rss_mb | MB | 1906 | 2659.682 | 2098.047 | 2973.430 | 2973.430 | n/a | n/a |
| Agency harness — python -m lsbench (PID 4725) main thread run-queue wait | percent | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 4725) vms_mb | MB | 1906 | 15992.148 | 14212.883 | 18015.660 | 16419.539 | n/a | n/a |
| Python — vllm (PID 4734) CPU | percent | 1905 | 0.606 | 0.000 | 4.977 | 0.000 | 11.650000 CPU seconds | n/a |
| Python — vllm (PID 4734) io read MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| Python — vllm (PID 4734) io write MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.008 | 0.000 | 0.078125 MB | n/a |
| Python — vllm (PID 4734) rss_mb | MB | 1906 | 1806.635 | 1803.035 | 1807.410 | 1807.410 | n/a | n/a |
| Python — vllm (PID 4734) main thread run-queue wait | percent | 1905 | 0.001 | 0.000 | 0.329 | 0.000 | 0.024576 run-queue seconds | n/a |
| Python — vllm (PID 4734) vms_mb | MB | 1906 | 12015.683 | 11942.754 | 12017.773 | 12017.773 | n/a | n/a |
| Python — python -c (PID 4784) CPU | percent | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 4784) io read MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4784) io write MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 4784) rss_mb | MB | 1906 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| Python — python -c (PID 4784) main thread run-queue wait | percent | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 4784) vms_mb | MB | 1906 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 4785) CPU | percent | 1905 | 7.301 | 0.000 | 39.642 | 0.995 | 140.270000 CPU seconds | n/a |
| VLLM::EngineCore (PID 4785) io read MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 4785) io write MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 4785) rss_mb | MB | 1906 | 2342.012 | 2339.062 | 2342.188 | 2342.188 | n/a | n/a |
| VLLM::EngineCore (PID 4785) main thread run-queue wait | percent | 1905 | 0.001 | 0.000 | 0.020 | 0.000 | 0.015422 run-queue seconds | n/a |
| VLLM::EngineCore (PID 4785) vms_mb | MB | 1906 | 21863.603 | 21859.750 | 21863.836 | 21863.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 5114) CPU | percent | 1905 | 0.003 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 5114) rss_mb | MB | 1906 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 5114) main thread run-queue wait | percent | 1905 | 0.009 | 0.000 | 6.096 | 0.000 | 0.175673 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 5114) vms_mb | MB | 1906 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 5153) CPU | percent | 1905 | 0.002 | 0.000 | 0.996 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 5153) rss_mb | MB | 1906 | 1.562 | 1.562 | 1.562 | 1.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 5153) main thread run-queue wait | percent | 1905 | 0.009 | 0.000 | 5.982 | 0.000 | 0.166331 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 5153) vms_mb | MB | 1906 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5254) CPU | percent | 1905 | 2.818 | 0.000 | 90.905 | 0.000 | 54.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5254) rss_mb | MB | 1906 | 103.092 | 3.164 | 108.828 | 107.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5254) main thread run-queue wait | percent | 1905 | 0.000 | 0.000 | 0.009 | 0.000 | 0.000106 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5254) vms_mb | MB | 1906 | 968.932 | 4.258 | 972.898 | 972.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5260) CPU | percent | 1 | 99.910 | 99.910 | 99.910 | 99.910 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5260) rss_mb | MB | 2 | 55.996 | 29.551 | 82.441 | 82.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5260) main thread run-queue wait | percent | 1 | 0.008 | 0.008 | 0.008 | 0.008 | 0.000081 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 5260) vms_mb | MB | 2 | 67.586 | 37.023 | 98.148 | 98.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 5272) CPU | percent | 1879 | 0.116 | 0.000 | 59.434 | 0.000 | 2.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 5272) rss_mb | MB | 1880 | 72.430 | 30.855 | 75.270 | 74.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 5272) main thread run-queue wait | percent | 1879 | 0.003 | 0.000 | 4.620 | 0.000 | 0.053709 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 5272) vms_mb | MB | 1880 | 86.895 | 36.262 | 89.898 | 88.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5793) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5793) rss_mb | MB | 4 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5793) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 5793) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — weights.py (PID 5795) CPU | percent | 3 | 148.161 | 100.396 | 173.069 | 173.069 | 4.470000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — weights.py (PID 5795) rss_mb | MB | 4 | 75.439 | 24.504 | 100.410 | 98.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — weights.py (PID 5795) main thread run-queue wait | percent | 3 | 25.575 | 7.871 | 40.524 | 28.330 | 0.771573 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — weights.py (PID 5795) vms_mb | MB | 4 | 323.184 | 135.961 | 397.926 | 395.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6072) rss_mb | MB | 1 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6072) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6073) rss_mb | MB | 1 | 14.598 | 14.598 | 14.598 | 14.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6073) vms_mb | MB | 1 | 368.465 | 368.465 | 368.465 | 368.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6131) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6131) rss_mb | MB | 3 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6131) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6131) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mode_analysis.py (PID 6135) CPU | percent | 2 | 159.564 | 123.272 | 195.856 | 195.856 | 3.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mode_analysis.py (PID 6135) rss_mb | MB | 3 | 483.846 | 24.641 | 727.828 | 727.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mode_analysis.py (PID 6135) main thread run-queue wait | percent | 2 | 1.311 | 0.593 | 2.030 | 2.030 | 0.026381 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mode_analysis.py (PID 6135) vms_mb | MB | 3 | 693.490 | 135.859 | 986.305 | 986.305 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6142) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6142) rss_mb | MB | 3 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6142) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6142) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6143) CPU | percent | 2 | 165.454 | 126.108 | 204.801 | 204.801 | 3.340000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6143) rss_mb | MB | 3 | 356.671 | 13.668 | 698.613 | 698.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6143) main thread run-queue wait | percent | 2 | 43.882 | 12.569 | 75.195 | 75.195 | 0.886603 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6143) vms_mb | MB | 3 | 1080.740 | 367.508 | 1437.355 | 1437.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6166) CPU | percent | 2 | 90.991 | 52.683 | 129.299 | 129.299 | 1.830000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6166) rss_mb | MB | 3 | 146.971 | 2.898 | 272.973 | 272.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6166) main thread run-queue wait | percent | 2 | 3.980 | 0.020 | 7.940 | 7.940 | 0.080034 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6166) vms_mb | MB | 3 | 429.822 | 4.215 | 1008.945 | 1008.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — prepare_probes.py (PID 6168) rss_mb | MB | 1 | 120.082 | 120.082 | 120.082 | 120.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — prepare_probes.py (PID 6168) vms_mb | MB | 1 | 472.672 | 472.672 | 472.672 | 472.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6191) rss_mb | MB | 1 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6191) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — transition_analysis.py (PID 6193) rss_mb | MB | 1 | 233.320 | 233.320 | 233.320 | 233.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — transition_analysis.py (PID 6193) vms_mb | MB | 1 | 972.953 | 972.953 | 972.953 | 972.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6200) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6200) rss_mb | MB | 5 | 3.121 | 3.121 | 3.121 | 3.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6200) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6200) vms_mb | MB | 5 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6201) CPU | percent | 4 | 190.154 | 166.959 | 198.913 | 196.866 | 7.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6201) rss_mb | MB | 5 | 614.849 | 168.332 | 731.496 | 711.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6201) main thread run-queue wait | percent | 4 | 68.147 | 48.603 | 75.555 | 73.670 | 2.741525 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6201) vms_mb | MB | 5 | 1346.928 | 871.156 | 1470.871 | 1450.871 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6296) rss_mb | MB | 1 | 3.004 | 3.004 | 3.004 | 3.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6296) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6297) rss_mb | MB | 1 | 78.117 | 78.117 | 78.117 | 78.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6297) vms_mb | MB | 1 | 429.172 | 429.172 | 429.172 | 429.172 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6343) rss_mb | MB | 1 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6343) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6344) rss_mb | MB | 1 | 179.379 | 179.379 | 179.379 | 179.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6344) vms_mb | MB | 1 | 885.793 | 885.793 | 885.793 | 885.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6372) rss_mb | MB | 1 | 2.793 | 2.793 | 2.793 | 2.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6372) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6373) rss_mb | MB | 1 | 181.555 | 181.555 | 181.555 | 181.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6373) vms_mb | MB | 1 | 886.953 | 886.953 | 886.953 | 886.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reconsideration_direction.py (PID 6395) rss_mb | MB | 1 | 208.031 | 208.031 | 208.031 | 208.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — reconsideration_direction.py (PID 6395) vms_mb | MB | 1 | 489.094 | 489.094 | 489.094 | 489.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6432) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6432) rss_mb | MB | 4 | 3.000 | 3.000 | 3.000 | 3.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6432) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6432) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6433) CPU | percent | 3 | 172.679 | 129.241 | 198.897 | 198.897 | 5.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6433) rss_mb | MB | 4 | 451.768 | 26.340 | 826.391 | 826.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6433) main thread run-queue wait | percent | 3 | 54.660 | 14.974 | 75.800 | 75.800 | 1.649129 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 6433) vms_mb | MB | 4 | 1298.337 | 378.387 | 1631.711 | 1591.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6499) rss_mb | MB | 1 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 6499) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 6502) rss_mb | MB | 1 | 145.539 | 145.539 | 145.539 | 145.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 6502) vms_mb | MB | 1 | 256.734 | 256.734 | 256.734 | 256.734 | n/a | n/a |
| docker commit (PID 6577) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6577) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6577) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6577) rss_mb | MB | 22 | 30.234 | 30.234 | 30.234 | 30.234 | n/a | n/a |
| docker commit (PID 6577) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6577) vms_mb | MB | 22 | 2059.773 | 2059.773 | 2059.773 | 2059.773 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 1905 | 5.419 | 0.000 | 205.572 | 0.000 | 103.928195 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1905 | 0.905 | 0.000 | 75.154 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1905 | 0.913 | 0.000 | 75.585 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 1905 | 0.008 | 0.000 | 12.124 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 1905 | 0.008 | 0.000 | 12.124 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 1905 | 0.015 | 0.000 | 21.666 | 0.000 | 28.218750 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 1905 | 0.004 | 0.000 | 5.785 | 0.000 | 8.273438 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 1906 | 173.762 | 20.492 | 531.781 | 130.203 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001045 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 1905 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 1905 | 16.962 | 1.554 | 313.833 | 1.830 | 326.141036 CPU seconds | n/a |
| workload total memory | MB | 1906 | 5553.060 | 4775.262 | 6062.531 | 6062.527 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
