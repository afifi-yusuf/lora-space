# agprof summary

- Duration: **690.115 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **25 calls**, 25 succeeded, 0 failed, 0 interrupted, n/a reported retries, 437.453 s total wait
- Tools: **75/75 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **64373** at 1.98 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 681074.383 / 681074.383 ms |
| LLM latency p50 / p95 | 16006.775 / 41759.798 ms |
| LLM TTFT p50 / p95 | 5282.008 / 6805.713 ms |
| LLM input / output tokens | 2165627 / 65669 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 25 total, 25 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 416.836 / 15884.090 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 2/2 | 2 | 0 | 0 | 318.963 ms | 330.168 ms |
| attribution | 2/2 | 2 | 0 | 0 | 319.037 ms | 322.178 ms |
| bash | 16/16 | 16 | 0 | 0 | 946.065 ms | 40599.504 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 362.002 ms | 362.002 ms |
| generate | 6/6 | 6 | 0 | 0 | 577.738 ms | 1116.062 ms |
| get_current_resources | 1/1 | 1 | 0 | 0 | 245.973 ms | 245.973 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 2804.651 ms | 2804.651 ms |
| patch | 35/35 | 35 | 0 | 0 | 414.364 ms | 424.370 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 240.158 ms | 240.158 ms |
| trace | 10/10 | 10 | 0 | 0 | 2102.521 ms | 2512.073 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 7.246% | 101.730% | 49.940 s | 11090.982 MB | 11878.301 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 7816 |  | 685 | 0.147% | 12.926% | 1.010 s | 1804.197 MB | 1804.258 MB | 11044.507 MB | 11046.715 MB | 0.007812 MB | 0.027344 MB |
| VLLM::EngineCor | 7851 |  | 685 | 1.538% | 50.602% | 10.580 s | 2324.508 MB | 2324.512 MB | 21204.117 MB | 21204.117 MB | 0.000000 MB | 0.003906 MB |
| python3 | 8231 | sandbox_agent_lsb-native_0000_0000 | 3 | 58.411% | 66.376% | 1.180 s | 45.661 MB | 81.355 MB | 55.163 MB | 96.543 MB | n/a MB | n/a MB |
| python | 7850 |  | 685 | 0.000% | 0.000% | 0.000 s | 12.207 MB | 12.207 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker-init | 8101 | sandbox_agent_lsb-native_0000_0000 | 676 | 0.003% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 8132 | sandbox_agent_lsb-native_0000_0000 | 676 | 0.001% | 0.995% | 0.010 s | 1.234 MB | 1.234 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python | 7811 |  | 685 | 5.538% | 101.392% | 38.180 s | 3483.976 MB | 4002.125 MB | 16680.186 MB | 17215.418 MB | 0.781250 MB | 1992.398438 MB |
| bash | 8225 | sandbox_agent_lsb-native_0000_0000 | 676 | 6.651% | 83.285% | 45.220 s | 106.400 MB | 113.789 MB | 963.114 MB | 974.250 MB | n/a MB | n/a MB |
| lsb_grid_worker | 2172 |  | 685 | 0.000% | 0.000% | 0.000 s | 3.062 MB | 3.062 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python3 | 8243 | sandbox_agent_lsb-native_0000_0000 | 659 | 0.597% | 44.767% | 3.960 s | 73.414 MB | 76.887 MB | 87.048 MB | 90.469 MB | n/a MB | n/a MB |
| bash | 8397 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.840 MB | 2.840 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8401 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.438 MB | 10.438 MB | 54.867 MB | 54.867 MB | n/a MB | n/a MB |
| python | 8411 | sandbox_agent_lsb-native_0000_0000 | 5 | 126.294% | 188.950% | 5.080 s | 132.882 MB | 299.121 MB | 528.445 MB | 718.582 MB | n/a MB | n/a MB |
| python | 8454 | sandbox_agent_lsb-native_0000_0000 | 35 | 195.389% | 202.896% | 66.890 s | 270.767 MB | 388.602 MB | 713.914 MB | 824.297 MB | n/a MB | n/a MB |
| python | 8729 | sandbox_agent_lsb-native_0000_0000 | 10 | 181.694% | 195.966% | 16.450 s | 202.969 MB | 301.422 MB | 617.756 MB | 742.164 MB | n/a MB | n/a MB |
| python | 8755 | sandbox_agent_lsb-native_0000_0000 | 46 | 189.979% | 201.932% | 86.100 s | 551.169 MB | 842.945 MB | 987.393 MB | 1334.859 MB | n/a MB | n/a MB |
| bash | 8751 | sandbox_agent_lsb-native_0000_0000 | 46 | 0.000% | 0.000% | 0.000 s | 2.992 MB | 2.992 MB | 4.219 MB | 4.219 MB | n/a MB | n/a MB |
| python | 8783 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.934 MB | 18.934 MB | 170.289 MB | 170.289 MB | n/a MB | n/a MB |
| python | 8795 | sandbox_agent_lsb-native_0000_0000 | 39 | 131.056% | 196.917% | 50.090 s | 304.146 MB | 565.625 MB | 721.318 MB | 996.426 MB | n/a MB | n/a MB |
| python | 8811 | sandbox_agent_lsb-native_0000_0000 | 8 | 181.185% | 199.594% | 12.770 s | 447.579 MB | 653.254 MB | 776.866 MB | 1017.328 MB | n/a MB | n/a MB |
| bash | 8809 | sandbox_agent_lsb-native_0000_0000 | 8 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8846 | sandbox_agent_lsb-native_0000_0000 | 31 | 167.968% | 203.588% | 50.760 s | 435.616 MB | 790.590 MB | 869.981 MB | 1274.301 MB | n/a MB | n/a MB |
| bash | 8861 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.066 MB | 3.066 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 8862 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 140.145 MB | 140.145 MB | 477.531 MB | 477.531 MB | n/a MB | n/a MB |
| docker | 8906 |  | 12 | 0.000% | 0.000% | 0.000 s | 30.441 MB | 30.441 MB | 1843.512 MB | 1843.512 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.658% | 98.000% | 11835.632 MB | 11876.000 MB | 28.826 W | 66.793 W | 19838.552 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 51.533% | 213.720% | 350.222 s | 307.721 MB | 1043.398 MB | 68.457031 MB | 1.601562 MB | 0.000874 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 7989 | 690.050 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 681.074 | n/a | n/a | 68.457 | 681074.383 | 681074.383 | 681074.383 |
| engine:execute | 1/1 | 0 | 0 | 681.073 | 1.769 | 679.299 | 68.457 | 681072.681 | 681072.681 | 681072.681 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 663.355 | 0.002 | 663.353 | 33.602 | 663354.852 | 663354.852 | 663354.852 |
| turn | 25/25 | 0 | 0 | 659.786 | n/a | n/a | 32.398 | 26391.441 | 20450.281 | 75661.643 |
| llm:attempt | 25/25 | 0 | 0 | 437.453 | 3.135 | 434.316 | 6.208 | 17498.116 | 16006.775 | 41759.798 |
| tool:bash | 16/16 | 0 | 0 | 177.388 | n/a | n/a | 20.802 | 11086.771 | 946.065 | 40599.504 |
| process:bash | 16/16 | 1 | 0 | 177.172 | n/a | n/a | 20.619 | 11073.234 | 937.250 | 40556.265 |
| tool:trace | 10/10 | 0 | 0 | 17.983 | n/a | n/a | 0.000 | 1798.319 | 2102.521 | 2512.073 |
| tool:patch | 35/35 | 0 | 0 | 14.553 | n/a | n/a | 4.749 | 415.797 | 414.364 | 424.370 |
| run:container_call | 13/13 | 0 | 0 | 13.245 | 0.002 | 13.243 | 0.074 | 1018.862 | 36.366 | 5156.553 |
| teardown:commit | 1/1 | 0 | 0 | 12.796 | 0.004 | 12.792 | 0.074 | 12796.385 | 12796.385 | 12796.385 |
| sandbox:commit | 1/1 | 0 | 0 | 12.623 | 0.002 | 12.621 | 0.074 | 12622.823 | 12622.823 | 12622.823 |
| checkpoint.total | 1/1 | 0 | 0 | 12.623 | 0.002 | 12.621 | 0.074 | 12622.678 | 12622.678 | 12622.678 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 12.623 | 0.002 | 12.621 | 0.074 | 12622.541 | 12622.541 | 12622.541 |
| syscall:sendto | 1831/1831 | 0 | 0 | 4.285 | n/a | n/a | 0.913 | 2.340 | 1.999 | 4.232 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.280 | 0.984 | 3.295 | 34.682 | 4279.663 | 4279.663 | 4279.663 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.279 | 0.984 | 3.295 | 34.681 | 4279.437 | 4279.437 | 4279.437 |
| tool:generate | 6/6 | 0 | 0 | 4.179 | n/a | n/a | 0.000 | 696.543 | 577.738 | 1116.062 |
| tool:logit_lens | 1/1 | 0 | 0 | 2.805 | n/a | n/a | 0.000 | 2804.651 | 2804.651 | 2804.651 |
| syscall:connect | 452/452 | 0 | 0 | 1.051 | n/a | n/a | 0.250 | 2.326 | 1.919 | 4.337 |
| tool:attribution | 2/2 | 0 | 0 | 0.638 | n/a | n/a | 0.000 | 319.037 | 319.037 | 322.178 |
| tool:attention | 2/2 | 0 | 0 | 0.638 | n/a | n/a | 0.000 | 318.963 | 318.963 | 330.168 |
| sandbox:start | 1/1 | 0 | 0 | 0.383 | 0.003 | 0.381 | 0.000 | 383.121 | 383.121 | 383.121 |
| runtime.container_create | 1/1 | 0 | 0 | 0.383 | 0.002 | 0.381 | 0.000 | 382.927 | 382.927 | 382.927 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.362 | n/a | n/a | 0.000 | 362.002 | 362.002 | 362.002 |
| sandbox:create | 1/1 | 0 | 0 | 0.353 | 0.245 | 0.107 | 0.000 | 352.757 | 352.757 | 352.757 |
| tool:get_current_resources | 1/1 | 0 | 0 | 0.246 | n/a | n/a | 0.113 | 245.973 | 245.973 | 245.973 |
| tool:submit_output | 1/1 | 0 | 0 | 0.240 | n/a | n/a | 0.000 | 240.158 | 240.158 | 240.158 |
| sandbox:stop | 1/1 | 0 | 0 | 0.173 | 0.002 | 0.172 | 0.000 | 173.264 | 173.264 | 173.264 |
| agency:services_close | 1/1 | 0 | 0 | 0.124 | 0.000 | 0.124 | 0.012 | 124.065 | 124.065 | 124.065 |
| syscall:execve | 68/68 | 0 | 0 | 0.116 | n/a | n/a | 0.090 | 1.707 | 1.214 | 3.705 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.042 | 0.031 | 0.000 | 73.292 | 73.292 | 73.292 |
| run:detect | 1/1 | 0 | 0 | 0.056 | 0.001 | 0.056 | 0.000 | 56.356 | 56.356 | 56.356 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.008 | 0.040 | 0.000 | 48.280 | 48.280 | 48.280 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 1.458 | 1.458 | 1.458 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.246 | 1.246 | 1.246 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.075 | 0.073 | 0.111 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.179 | 0.179 | 0.179 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.073 | 0.073 | 0.073 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 684 | 0.849 | 0.015 | 78.388 | 0.046 | 5.839353 CPU seconds | n/a |
| GPU 0 memory | MB | 685 | 11835.632 | 11670.000 | 11876.000 | 11844.000 | n/a | n/a |
| GPU 0 power | W | 685 | 28.826 | 27.744 | 66.793 | 27.853 | n/a | 19838.552 J |
| GPU 0 proc / 7811-591244 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 memory | MB | 685 | 3208.403 | 3118.000 | 3246.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 7811-591244 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 estimated power | W | 651 | 2.152 | 0.000 | 50.677 | 0.000 | n/a | n/a |
| GPU 0 proc / 7811-591244 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 utilization | percent | 651 | 1.237 | 0.000 | 46.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 7851-593247 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 memory | MB | 685 | 8145.229 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 7851-593247 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 estimated power | W | 28 | 7.553 | 0.000 | 56.570 | 16.772 | n/a | n/a |
| GPU 0 proc / 7851-593247 / sandbox / ~ / device / GPU-8696a95f-bf2e-3b5f-191a-23678f848762 utilization | percent | 28 | 6.786 | 0.000 | 83.000 | 19.000 | n/a | n/a |
| GPU 0 processes memory | MB | 685 | 11353.632 | 11188.000 | 11394.000 | 11362.000 | n/a | n/a |
| GPU 0 utilization | percent | 685 | 1.658 | 0.000 | 98.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 685 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 684 | 9.016 | 0.013 | 62.516 | 0.265 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 684 | 14.683 | 0.000 | 57.320 | 0.251 | n/a | n/a |
| host disk_read_mb_s | MB/s | 684 | 0.771 | 0.000 | 151.991 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 684 | 2.934 | 0.000 | 184.362 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 684 | 0.884 | 0.000 | 62.396 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 684 | 0.962 | 0.000 | 62.861 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 685 | 15363.539 | 15363.539 | 15363.539 | 15363.539 | n/a | n/a |
| host mem_used_mb | MB | 685 | 7702.333 | 6747.285 | 8543.367 | 7674.996 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 684 | 0.006 | 0.000 | 1.602 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 684 | 0.007 | 0.000 | 1.602 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 684 | 0.006 | 0.000 | 0.254 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 684 | 0.019 | 0.000 | 0.996 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2172) CPU | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2172) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2172) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2172) rss_mb | MB | 685 | 3.062 | 3.062 | 3.062 | 3.062 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2172) main thread run-queue wait | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2172) vms_mb | MB | 685 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 7811) CPU | percent | 684 | 5.538 | 0.000 | 101.392 | 0.996 | 38.180000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 7811) io read MB/s | MB/s | 684 | 0.001 | 0.000 | 0.361 | 0.000 | 0.781250 MB | n/a |
| Agency harness — python -m lsbench (PID 7811) io write MB/s | MB/s | 684 | 2.887 | 0.015 | 327.134 | 0.023 | 1992.398438 MB | n/a |
| Agency harness — python -m lsbench (PID 7811) rss_mb | MB | 685 | 3483.976 | 2545.492 | 4002.125 | 3709.637 | n/a | n/a |
| Agency harness — python -m lsbench (PID 7811) main thread run-queue wait | percent | 684 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000017 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 7811) vms_mb | MB | 685 | 16680.186 | 14116.863 | 17215.418 | 16810.539 | n/a | n/a |
| Python — vllm (PID 7816) CPU | percent | 684 | 0.147 | 0.000 | 12.926 | 0.000 | 1.010000 CPU seconds | n/a |
| Python — vllm (PID 7816) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 7816) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.008 | 0.000 | 0.027344 MB | n/a |
| Python — vllm (PID 7816) rss_mb | MB | 685 | 1804.197 | 1803.383 | 1804.258 | 1804.258 | n/a | n/a |
| Python — vllm (PID 7816) main thread run-queue wait | percent | 684 | 0.005 | 0.000 | 0.517 | 0.000 | 0.035061 run-queue seconds | n/a |
| Python — vllm (PID 7816) vms_mb | MB | 685 | 11044.507 | 10974.695 | 11046.715 | 11046.715 | n/a | n/a |
| Python — python -c (PID 7850) CPU | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 7850) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 7850) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 7850) rss_mb | MB | 685 | 12.207 | 12.207 | 12.207 | 12.207 | n/a | n/a |
| Python — python -c (PID 7850) main thread run-queue wait | percent | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 7850) vms_mb | MB | 685 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 7851) CPU | percent | 684 | 1.538 | 0.000 | 50.602 | 0.996 | 10.580000 CPU seconds | n/a |
| VLLM::EngineCore (PID 7851) io read MB/s | MB/s | 684 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 7851) io write MB/s | MB/s | 684 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 7851) rss_mb | MB | 685 | 2324.508 | 2324.387 | 2324.512 | 2324.512 | n/a | n/a |
| VLLM::EngineCore (PID 7851) main thread run-queue wait | percent | 684 | 0.000 | 0.000 | 0.131 | 0.000 | 0.001757 run-queue seconds | n/a |
| VLLM::EngineCore (PID 7851) vms_mb | MB | 685 | 21204.117 | 21204.117 | 21204.117 | 21204.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 8101) CPU | percent | 675 | 0.003 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 8101) rss_mb | MB | 676 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 8101) main thread run-queue wait | percent | 675 | 0.017 | 0.000 | 5.371 | 0.000 | 0.118396 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 8101) vms_mb | MB | 676 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 8132) CPU | percent | 675 | 0.001 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 8132) rss_mb | MB | 676 | 1.234 | 1.234 | 1.234 | 1.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 8132) main thread run-queue wait | percent | 675 | 0.013 | 0.000 | 5.355 | 0.000 | 0.086169 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 8132) vms_mb | MB | 676 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8225) CPU | percent | 675 | 6.651 | 0.000 | 83.285 | 0.000 | 45.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8225) rss_mb | MB | 676 | 106.400 | 2.992 | 113.789 | 113.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8225) main thread run-queue wait | percent | 675 | 0.000 | 0.000 | 0.006 | 0.000 | 0.000100 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8225) vms_mb | MB | 676 | 963.114 | 4.258 | 974.250 | 974.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8231) CPU | percent | 2 | 58.411 | 50.445 | 66.376 | 66.376 | 1.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8231) rss_mb | MB | 3 | 45.661 | 7.289 | 81.355 | 81.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8231) main thread run-queue wait | percent | 2 | 0.036 | 0.019 | 0.053 | 0.053 | 0.000726 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 8231) vms_mb | MB | 3 | 55.163 | 11.809 | 96.543 | 96.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 8243) CPU | percent | 658 | 0.597 | 0.000 | 44.767 | 0.000 | 3.960000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 8243) rss_mb | MB | 659 | 73.414 | 22.727 | 76.887 | 76.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 8243) main thread run-queue wait | percent | 658 | 0.041 | 0.000 | 5.484 | 0.000 | 0.274148 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 8243) vms_mb | MB | 659 | 87.048 | 29.770 | 90.469 | 89.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8397) rss_mb | MB | 1 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8397) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8401) rss_mb | MB | 1 | 10.438 | 10.438 | 10.438 | 10.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8401) vms_mb | MB | 1 | 54.867 | 54.867 | 54.867 | 54.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diagnose.py (PID 8411) CPU | percent | 4 | 126.294 | 91.430 | 188.950 | 188.950 | 5.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diagnose.py (PID 8411) rss_mb | MB | 5 | 132.882 | 30.012 | 299.121 | 299.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diagnose.py (PID 8411) main thread run-queue wait | percent | 4 | 13.814 | 0.005 | 40.405 | 40.405 | 0.555690 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diagnose.py (PID 8411) vms_mb | MB | 5 | 528.445 | 401.820 | 718.582 | 718.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — roles.py (PID 8454) CPU | percent | 34 | 195.389 | 184.399 | 202.896 | 198.948 | 66.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — roles.py (PID 8454) rss_mb | MB | 35 | 270.767 | 54.930 | 388.602 | 191.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — roles.py (PID 8454) main thread run-queue wait | percent | 34 | 43.085 | 32.921 | 52.055 | 52.055 | 14.750207 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — roles.py (PID 8454) vms_mb | MB | 35 | 713.914 | 440.273 | 824.297 | 625.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 8729) CPU | percent | 9 | 181.694 | 124.076 | 195.966 | 182.978 | 16.450000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 8729) rss_mb | MB | 10 | 202.969 | 15.301 | 301.422 | 205.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 8729) main thread run-queue wait | percent | 9 | 39.445 | 30.956 | 43.359 | 38.290 | 3.571285 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — geometry.py (PID 8729) vms_mb | MB | 10 | 617.756 | 209.383 | 742.164 | 645.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8751) CPU | percent | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8751) rss_mb | MB | 46 | 2.992 | 2.992 | 2.992 | 2.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8751) main thread run-queue wait | percent | 45 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8751) vms_mb | MB | 46 | 4.219 | 4.219 | 4.219 | 4.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — site_compare.py (PID 8755) CPU | percent | 45 | 189.979 | 140.171 | 201.932 | 195.202 | 86.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — site_compare.py (PID 8755) rss_mb | MB | 46 | 551.169 | 26.328 | 842.945 | 293.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — site_compare.py (PID 8755) main thread run-queue wait | percent | 45 | 44.319 | 25.301 | 53.796 | 50.176 | 20.085962 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — site_compare.py (PID 8755) vms_mb | MB | 46 | 987.393 | 218.105 | 1334.859 | 727.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — discourse.py (PID 8783) rss_mb | MB | 1 | 18.934 | 18.934 | 18.934 | 18.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — discourse.py (PID 8783) vms_mb | MB | 1 | 170.289 | 170.289 | 170.289 | 170.289 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design.py (PID 8795) CPU | percent | 38 | 131.056 | 97.427 | 196.917 | 132.256 | 50.090000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design.py (PID 8795) rss_mb | MB | 39 | 304.146 | 10.371 | 565.625 | 306.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design.py (PID 8795) main thread run-queue wait | percent | 38 | 13.427 | 0.002 | 48.267 | 11.600 | 5.132475 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — design.py (PID 8795) vms_mb | MB | 39 | 721.318 | 14.082 | 996.426 | 733.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8809) CPU | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8809) rss_mb | MB | 8 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8809) main thread run-queue wait | percent | 7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8809) vms_mb | MB | 8 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8811) CPU | percent | 7 | 181.185 | 137.184 | 199.594 | 199.594 | 12.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8811) rss_mb | MB | 8 | 447.579 | 20.633 | 653.254 | 639.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8811) main thread run-queue wait | percent | 7 | 27.755 | 17.542 | 32.847 | 31.993 | 1.956408 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8811) vms_mb | MB | 8 | 776.866 | 172.301 | 1017.328 | 1017.328 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 8846) CPU | percent | 30 | 167.968 | 99.396 | 203.588 | 99.396 | 50.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 8846) rss_mb | MB | 31 | 435.616 | 36.152 | 790.590 | 333.438 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 8846) main thread run-queue wait | percent | 30 | 32.570 | 0.005 | 52.472 | 0.005 | 9.844887 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 8846) vms_mb | MB | 31 | 869.981 | 415.648 | 1274.301 | 759.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8861) rss_mb | MB | 1 | 3.066 | 3.066 | 3.066 | 3.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 8861) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8862) rss_mb | MB | 1 | 140.145 | 140.145 | 140.145 | 140.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 8862) vms_mb | MB | 1 | 477.531 | 477.531 | 477.531 | 477.531 | n/a | n/a |
| docker commit (PID 8906) CPU | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 8906) io read MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8906) io write MB/s | MB/s | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8906) rss_mb | MB | 12 | 30.441 | 30.441 | 30.441 | 30.441 | n/a | n/a |
| docker commit (PID 8906) main thread run-queue wait | percent | 11 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 8906) vms_mb | MB | 12 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 675 | 51.533 | 0.000 | 213.720 | 0.000 | 350.221588 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 675 | 8.318 | 0.000 | 50.247 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 675 | 8.842 | 0.000 | 61.774 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 675 | 0.106 | 0.000 | 23.948 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 675 | 0.108 | 0.000 | 23.948 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 675 | 0.101 | 0.000 | 19.670 | 0.000 | 68.457031 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 675 | 0.002 | 0.000 | 0.587 | 0.101 | 1.601562 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 676 | 307.721 | 14.375 | 1043.398 | 176.270 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 675 | 0.006 | 0.000 | 1.736 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 675 | 0.006 | 0.000 | 1.736 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 675 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000874 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 675 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 684 | 7.246 | 1.424 | 101.730 | 1.994 | 49.940357 CPU seconds | n/a |
| workload total memory | MB | 685 | 11090.982 | 9678.555 | 11878.301 | 11362.613 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
