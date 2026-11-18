# agprof summary

- Duration: **2130.344 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **30 calls**, 30 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1087.277 s total wait
- Tools: **83/83 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **197855** at 1.973 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2127162.261 / 2127162.261 ms |
| LLM latency p50 / p95 | 34218.455 / 75166.175 ms |
| LLM TTFT p50 / p95 | 9431.998 / 11699.650 ms |
| LLM input / output tokens | 5202807 / 95607 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 30 total, 30 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 4859.820 / 46729.696 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attribution | 1/1 | 1 | 0 | 0 | 317.448 ms | 317.448 ms |
| bash | 21/21 | 21 | 0 | 0 | 7153.556 ms | 30253.016 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 334.631 ms | 334.631 ms |
| generate | 25/25 | 25 | 0 | 0 | 14655.355 ms | 75892.354 ms |
| get_current_resources | 1/1 | 1 | 0 | 0 | 229.154 ms | 229.154 ms |
| inspect | 2/2 | 2 | 0 | 0 | 803.649 ms | 839.881 ms |
| inspect_module_inputs | 3/3 | 3 | 0 | 0 | 855.140 ms | 1265.078 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 1927.936 ms | 1927.936 ms |
| patch | 3/3 | 3 | 0 | 0 | 426.954 ms | 437.279 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 230.680 ms | 230.680 ms |
| token_stats | 5/5 | 5 | 0 | 0 | 10540.522 ms | 61481.376 ms |
| trace | 19/19 | 19 | 0 | 0 | 1388.206 ms | 9804.685 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 30.526% | 268.213% | 650.633 s | 10140.393 MB | 12695.191 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 2344 |  | 2116 | 0.000% | 0.000% | 0.000 s | 12.336 MB | 12.336 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 2345 |  | 2116 | 10.517% | 49.506% | 224.400 s | 2329.180 MB | 2329.598 MB | 21862.749 MB | 21862.961 MB | 0.000000 MB | 0.011719 MB |
| lsb_grid_worker | 2203 |  | 2116 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| vllm | 2239 |  | 2116 | 0.954% | 6.939% | 20.360 s | 1788.914 MB | 1789.016 MB | 12024.672 MB | 12025.570 MB | 0.007812 MB | 0.128906 MB |
| docker | 2483 |  | 1 | n/a% | n/a% | n/a s | 29.887 MB | 29.887 MB | 2060.289 MB | 2060.289 MB | n/a MB | n/a MB |
| docker-buildx | 2497 |  | 1 | n/a% | n/a% | n/a s | 40.172 MB | 40.172 MB | 1299.461 MB | 1299.461 MB | n/a MB | n/a MB |
| python | 2212 |  | 2116 | 19.037% | 266.491% | 405.480 s | 2788.012 MB | 4552.156 MB | 15987.084 MB | 19057.152 MB | 169.882812 MB | 5058.589844 MB |
| python3 | 2766 | sandbox_agent_lsb-native_0000_0000 | 3 | 57.193% | 65.671% | 1.150 s | 41.609 MB | 67.984 MB | 49.172 MB | 77.059 MB | n/a MB | n/a MB |
| docker-init | 2612 | sandbox_agent_lsb-native_0000_0000 | 2111 | 0.002% | 0.995% | 0.050 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| tail | 2655 | sandbox_agent_lsb-native_0000_0000 | 2111 | 0.002% | 0.995% | 0.050 s | 1.367 MB | 1.367 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 2760 | sandbox_agent_lsb-native_0000_0000 | 2111 | 3.567% | 88.576% | 75.770 s | 106.312 MB | 116.598 MB | 969.410 MB | 975.699 MB | n/a MB | n/a MB |
| python3 | 2782 | sandbox_agent_lsb-native_0000_0000 | 2084 | 0.190% | 49.746% | 3.980 s | 73.658 MB | 78.969 MB | 88.157 MB | 93.688 MB | n/a MB | n/a MB |
| python | 2924 | sandbox_agent_lsb-native_0000_0000 | 29 | 195.920% | 200.770% | 55.180 s | 128.000 MB | 146.645 MB | 455.790 MB | 474.363 MB | n/a MB | n/a MB |
| bash | 2922 | sandbox_agent_lsb-native_0000_0000 | 29 | 0.000% | 0.000% | 0.000 s | 2.836 MB | 2.836 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3435 | sandbox_agent_lsb-native_0000_0000 | 8 | 190.093% | 196.883% | 13.380 s | 225.496 MB | 273.387 MB | 865.851 MB | 977.160 MB | n/a MB | n/a MB |
| bash | 3445 | sandbox_agent_lsb-native_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 2.969 MB | 2.969 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3446 | sandbox_agent_lsb-native_0000_0000 | 16 | 196.949% | 200.683% | 29.730 s | 239.578 MB | 242.699 MB | 1012.365 MB | 1432.285 MB | n/a MB | n/a MB |
| python | 3451 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 106.953 MB | 106.953 MB | 298.543 MB | 298.543 MB | n/a MB | n/a MB |
| python | 3591 | sandbox_agent_lsb-native_0000_0000 | 32 | 196.873% | 200.714% | 61.400 s | 285.811 MB | 380.336 MB | 1013.833 MB | 1120.070 MB | n/a MB | n/a MB |
| bash | 3590 | sandbox_agent_lsb-native_0000_0000 | 33 | 1.305% | 41.752% | 0.420 s | 6.283 MB | 111.352 MB | 12.073 MB | 263.520 MB | n/a MB | n/a MB |
| python | 3624 | sandbox_agent_lsb-native_0000_0000 | 11 | 159.550% | 194.692% | 16.050 s | 372.851 MB | 575.844 MB | 789.235 MB | 1008.664 MB | n/a MB | n/a MB |
| python | 3664 | sandbox_agent_lsb-native_0000_0000 | 7 | 169.625% | 197.674% | 10.240 s | 253.605 MB | 445.102 MB | 669.090 MB | 846.918 MB | n/a MB | n/a MB |
| python | 3682 | sandbox_agent_lsb-native_0000_0000 | 7 | 169.233% | 181.660% | 10.220 s | 304.397 MB | 454.883 MB | 747.160 MB | 887.430 MB | n/a MB | n/a MB |
| bash | 3681 | sandbox_agent_lsb-native_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 3.070 MB | 3.070 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 3780 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.961 MB | 2.961 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3781 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 35.934 MB | 35.934 MB | 227.742 MB | 227.742 MB | n/a MB | n/a MB |
| python | 3794 | sandbox_agent_lsb-native_0000_0000 | 12 | 164.738% | 200.795% | 18.230 s | 485.042 MB | 684.492 MB | 974.597 MB | 1195.430 MB | n/a MB | n/a MB |
| bash | 3830 | sandbox_agent_lsb-native_0000_0000 | 30 | 0.000% | 0.000% | 0.000 s | 3.051 MB | 3.051 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3831 | sandbox_agent_lsb-native_0000_0000 | 23 | 196.547% | 200.958% | 43.510 s | 238.646 MB | 297.371 MB | 1025.976 MB | 1484.633 MB | n/a MB | n/a MB |
| python | 3837 | sandbox_agent_lsb-native_0000_0000 | 7 | 167.985% | 199.693% | 10.140 s | 442.442 MB | 703.219 MB | 906.423 MB | 1191.168 MB | n/a MB | n/a MB |
| bash | 3853 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3854 | sandbox_agent_lsb-native_0000_0000 | 6 | 171.208% | 206.829% | 8.610 s | 500.839 MB | 727.359 MB | 935.422 MB | 1204.027 MB | n/a MB | n/a MB |
| python | 3912 | sandbox_agent_lsb-native_0000_0000 | 11 | 176.537% | 202.759% | 17.760 s | 482.879 MB | 742.883 MB | 958.260 MB | 1172.297 MB | n/a MB | n/a MB |
| bash | 3926 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.039 MB | 3.039 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 3927 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 89.516 MB | 89.516 MB | 461.398 MB | 461.398 MB | n/a MB | n/a MB |
| python | 3946 | sandbox_agent_lsb-native_0000_0000 | 13 | 177.983% | 204.913% | 21.490 s | 493.309 MB | 743.824 MB | 999.062 MB | 1172.855 MB | n/a MB | n/a MB |
| docker | 4019 |  | 22 | 0.000% | 0.000% | 0.000 s | 30.695 MB | 30.695 MB | 2060.289 MB | 2060.289 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 30.982% | 100.000% | 12024.358 MB | 14004.000 MB | 42.687 W | 77.799 W | 90974.690 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 19.973% | 208.317% | 424.059 s | 262.849 MB | 990.188 MB | 78.328125 MB | 2.765625 MB | 0.001299 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2481 | 2130.277 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2127.162 | n/a | n/a | 78.328 | 2127162.261 | 2127162.261 | 2127162.261 |
| engine:execute | 1/1 | 0 | 0 | 2127.160 | 2.859 | 2124.301 | 78.328 | 2127160.445 | 2127160.445 | 2127160.445 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 2098.521 | 0.004 | 2098.516 | 40.734 | 2098520.929 | 2098520.929 | 2098520.929 |
| turn | 30/30 | 0 | 0 | 2095.161 | n/a | n/a | 39.018 | 69838.700 | 63952.085 | 169930.916 |
| llm:attempt | 30/30 | 0 | 0 | 1087.277 | 4.497 | 1082.779 | 9.709 | 36242.558 | 34218.455 | 75166.175 |
| tool:generate | 25/25 | 0 | 0 | 595.433 | n/a | n/a | 0.149 | 23817.334 | 14655.355 | 75892.354 |
| tool:bash | 21/21 | 0 | 0 | 190.381 | n/a | n/a | 28.589 | 9065.749 | 7153.556 | 30253.016 |
| process:bash | 21/21 | 1 | 0 | 190.177 | n/a | n/a | 28.579 | 9056.030 | 7142.759 | 30242.450 |
| tool:token_stats | 5/5 | 0 | 0 | 140.411 | n/a | n/a | 0.000 | 28082.226 | 10540.522 | 61481.376 |
| tool:trace | 19/19 | 0 | 0 | 68.607 | n/a | n/a | 0.000 | 3610.907 | 1388.206 | 9804.685 |
| run:container_call | 13/13 | 0 | 0 | 22.937 | 0.002 | 22.935 | 0.020 | 1764.407 | 34.619 | 9068.818 |
| teardown:commit | 1/1 | 0 | 0 | 22.319 | 0.004 | 22.314 | 0.020 | 22318.545 | 22318.545 | 22318.545 |
| sandbox:commit | 1/1 | 0 | 0 | 22.152 | 0.002 | 22.149 | 0.020 | 22151.628 | 22151.628 | 22151.628 |
| checkpoint.total | 1/1 | 0 | 0 | 22.151 | 0.002 | 22.149 | 0.020 | 22151.483 | 22151.483 | 22151.483 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.151 | 0.002 | 22.149 | 0.020 | 22151.348 | 22151.348 | 22151.348 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.901 | 1.130 | 3.771 | 37.526 | 4901.491 | 4901.491 | 4901.491 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.901 | 1.130 | 3.771 | 37.526 | 4901.273 | 4901.273 | 4901.273 |
| syscall:sendto | 1979/1979 | 0 | 0 | 4.042 | n/a | n/a | 0.215 | 2.042 | 1.745 | 3.691 |
| tool:inspect_module_inputs | 3/3 | 0 | 0 | 2.931 | n/a | n/a | 0.000 | 976.882 | 855.140 | 1265.078 |
| tool:logit_lens | 1/1 | 0 | 0 | 1.928 | n/a | n/a | 0.025 | 1927.936 | 1927.936 | 1927.936 |
| tool:inspect | 2/2 | 0 | 0 | 1.607 | n/a | n/a | 0.000 | 803.649 | 803.649 | 839.881 |
| tool:patch | 3/3 | 0 | 0 | 1.284 | n/a | n/a | 0.000 | 427.991 | 426.954 | 437.279 |
| syscall:connect | 547/547 | 0 | 0 | 1.114 | n/a | n/a | 0.141 | 2.036 | 1.777 | 3.866 |
| sandbox:create | 1/1 | 0 | 0 | 1.051 | 0.251 | 0.800 | 0.000 | 1050.875 | 1050.875 | 1050.875 |
| run:detect | 1/1 | 0 | 0 | 0.748 | 0.001 | 0.747 | 0.000 | 747.769 | 747.769 | 747.769 |
| sandbox:start | 1/1 | 0 | 0 | 0.551 | 0.003 | 0.548 | 0.000 | 550.930 | 550.930 | 550.930 |
| runtime.container_create | 1/1 | 0 | 0 | 0.551 | 0.002 | 0.548 | 0.000 | 550.779 | 550.779 | 550.779 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.335 | n/a | n/a | 0.000 | 334.631 | 334.631 | 334.631 |
| tool:attribution | 1/1 | 0 | 0 | 0.317 | n/a | n/a | 0.000 | 317.448 | 317.448 | 317.448 |
| tool:submit_output | 1/1 | 0 | 0 | 0.231 | n/a | n/a | 0.000 | 230.680 | 230.680 | 230.680 |
| tool:get_current_resources | 1/1 | 0 | 0 | 0.229 | n/a | n/a | 0.056 | 229.154 | 229.154 | 229.154 |
| sandbox:stop | 1/1 | 0 | 0 | 0.167 | 0.002 | 0.165 | 0.000 | 166.601 | 166.601 | 166.601 |
| agency:services_close | 1/1 | 0 | 0 | 0.154 | 0.000 | 0.154 | 0.011 | 153.947 | 153.947 | 153.947 |
| syscall:execve | 91/91 | 0 | 0 | 0.134 | n/a | n/a | 0.116 | 1.469 | 1.191 | 2.827 |
| agency:services_start | 1/1 | 0 | 0 | 0.108 | 0.045 | 0.064 | 0.000 | 108.334 | 108.334 | 108.334 |
| agent:create | 1/1 | 0 | 0 | 0.052 | 0.009 | 0.042 | 0.000 | 51.591 | 51.591 | 51.591 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.000 | 3.352 | 3.352 | 3.352 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.321 | 1.321 | 1.321 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.075 | 0.080 | 0.104 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.224 | 0.224 | 0.224 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.099 | 0.099 | 0.099 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2114 | 0.399 | 0.033 | 52.202 | 0.211 | 8.492171 CPU seconds | n/a |
| GPU 0 memory | MB | 2116 | 12024.358 | 11670.000 | 14004.000 | 11904.000 | n/a | n/a |
| GPU 0 power | W | 2116 | 42.687 | 28.292 | 77.799 | 28.324 | n/a | 90974.690 J |
| GPU 0 proc / 2212-24466 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb memory | MB | 2116 | 3336.497 | 3118.000 | 5314.000 | 3214.000 | n/a | n/a |
| GPU 0 proc / 2212-24466 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb estimated power | W | 1120 | 7.007 | 0.000 | 76.407 | 0.000 | n/a | n/a |
| GPU 0 proc / 2212-24466 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb utilization | percent | 1120 | 6.459 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 2345-28359 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb memory | MB | 2116 | 8205.861 | 8070.000 | 8208.000 | 8208.000 | n/a | n/a |
| GPU 0 proc / 2345-28359 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb estimated power | W | 966 | 42.323 | 0.000 | 72.386 | 65.144 | n/a | n/a |
| GPU 0 proc / 2345-28359 / sandbox / ~ / device / GPU-cb73f08c-cbd8-863a-bd60-aed0f222a7eb utilization | percent | 966 | 58.542 | 0.000 | 100.000 | 88.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2116 | 11542.358 | 11188.000 | 13522.000 | 11422.000 | n/a | n/a |
| GPU 0 utilization | percent | 2116 | 30.982 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2116 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2115 | 3.809 | 0.011 | 59.447 | 0.127 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2115 | 6.300 | 0.000 | 33.871 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2115 | 0.898 | 0.000 | 207.285 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2115 | 2.445 | 0.000 | 248.710 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2115 | 1.255 | 0.000 | 94.540 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2115 | 1.258 | 0.000 | 94.579 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 2116 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 2116 | 7164.324 | 6312.125 | 9349.992 | 7393.164 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2115 | 0.003 | 0.000 | 0.254 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2115 | 0.014 | 0.000 | 1.764 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2203) CPU | percent | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2203) io read MB/s | MB/s | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2203) io write MB/s | MB/s | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2203) rss_mb | MB | 2116 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2203) main thread run-queue wait | percent | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2203) vms_mb | MB | 2116 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2212) CPU | percent | 2115 | 19.037 | 0.000 | 266.491 | 1.991 | 405.480000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 2212) io read MB/s | MB/s | 2115 | 0.079 | 0.000 | 92.290 | 0.000 | 169.882812 MB | n/a |
| Agency harness — python -m lsbench (PID 2212) io write MB/s | MB/s | 2115 | 2.374 | 0.015 | 755.885 | 0.023 | 5058.589844 MB | n/a |
| Agency harness — python -m lsbench (PID 2212) rss_mb | MB | 2116 | 2788.012 | 1991.953 | 4552.156 | 3209.664 | n/a | n/a |
| Agency harness — python -m lsbench (PID 2212) main thread run-queue wait | percent | 2115 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000017 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 2212) vms_mb | MB | 2116 | 15987.084 | 14062.852 | 19057.152 | 16082.590 | n/a | n/a |
| Python — vllm (PID 2239) CPU | percent | 2115 | 0.954 | 0.000 | 6.939 | 0.995 | 20.360000 CPU seconds | n/a |
| Python — vllm (PID 2239) io read MB/s | MB/s | 2115 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 2239) io write MB/s | MB/s | 2115 | 0.000 | 0.000 | 0.008 | 0.000 | 0.128906 MB | n/a |
| Python — vllm (PID 2239) rss_mb | MB | 2116 | 1788.914 | 1786.348 | 1789.016 | 1789.016 | n/a | n/a |
| Python — vllm (PID 2239) main thread run-queue wait | percent | 2115 | 0.001 | 0.000 | 0.084 | 0.000 | 0.012677 run-queue seconds | n/a |
| Python — vllm (PID 2239) vms_mb | MB | 2116 | 12024.672 | 11951.551 | 12025.570 | 12025.570 | n/a | n/a |
| Python — python -c (PID 2344) CPU | percent | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 2344) io read MB/s | MB/s | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2344) io write MB/s | MB/s | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 2344) rss_mb | MB | 2116 | 12.336 | 12.336 | 12.336 | 12.336 | n/a | n/a |
| Python — python -c (PID 2344) main thread run-queue wait | percent | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 2344) vms_mb | MB | 2116 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 2345) CPU | percent | 2115 | 10.517 | 0.000 | 49.506 | 0.000 | 224.400000 CPU seconds | n/a |
| VLLM::EngineCore (PID 2345) io read MB/s | MB/s | 2115 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 2345) io write MB/s | MB/s | 2115 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 2345) rss_mb | MB | 2116 | 2329.180 | 2326.566 | 2329.598 | 2329.598 | n/a | n/a |
| VLLM::EngineCore (PID 2345) main thread run-queue wait | percent | 2115 | 0.001 | 0.000 | 0.025 | 0.000 | 0.027178 run-queue seconds | n/a |
| VLLM::EngineCore (PID 2345) vms_mb | MB | 2116 | 21862.749 | 21860.633 | 21862.961 | 21862.961 | n/a | n/a |
| docker info (PID 2483) rss_mb | MB | 1 | 29.887 | 29.887 | 29.887 | 29.887 | n/a | n/a |
| docker info (PID 2483) vms_mb | MB | 1 | 2060.289 | 2060.289 | 2060.289 | 2060.289 | n/a | n/a |
| docker-buildx (PID 2497) rss_mb | MB | 1 | 40.172 | 40.172 | 40.172 | 40.172 | n/a | n/a |
| docker-buildx (PID 2497) vms_mb | MB | 1 | 1299.461 | 1299.461 | 1299.461 | 1299.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2612) CPU | percent | 2110 | 0.002 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2612) rss_mb | MB | 2111 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2612) main thread run-queue wait | percent | 2110 | 0.007 | 0.000 | 5.709 | 0.000 | 0.146320 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 2612) vms_mb | MB | 2111 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2655) CPU | percent | 2110 | 0.002 | 0.000 | 0.995 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2655) rss_mb | MB | 2111 | 1.367 | 1.367 | 1.367 | 1.367 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2655) main thread run-queue wait | percent | 2110 | 0.004 | 0.000 | 4.977 | 0.000 | 0.077219 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 2655) vms_mb | MB | 2111 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2760) CPU | percent | 2110 | 3.567 | 0.000 | 88.576 | 0.000 | 75.770000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2760) rss_mb | MB | 2111 | 106.312 | 2.758 | 116.598 | 114.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2760) main thread run-queue wait | percent | 2110 | 0.000 | 0.000 | 0.008 | 0.000 | 0.000102 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2760) vms_mb | MB | 2111 | 969.410 | 4.258 | 975.699 | 973.973 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2766) CPU | percent | 2 | 57.193 | 48.714 | 65.671 | 65.671 | 1.150000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2766) rss_mb | MB | 3 | 41.609 | 10.984 | 67.984 | 67.984 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2766) main thread run-queue wait | percent | 2 | 0.037 | 0.028 | 0.047 | 0.047 | 0.000749 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 2766) vms_mb | MB | 3 | 49.172 | 15.320 | 77.059 | 77.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2782) CPU | percent | 2083 | 0.190 | 0.000 | 49.746 | 0.000 | 3.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2782) rss_mb | MB | 2084 | 73.658 | 30.977 | 78.969 | 77.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2782) main thread run-queue wait | percent | 2083 | 0.002 | 0.000 | 2.454 | 0.000 | 0.035699 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 2782) vms_mb | MB | 2084 | 88.157 | 36.215 | 93.688 | 92.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2922) CPU | percent | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2922) rss_mb | MB | 29 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2922) main thread run-queue wait | percent | 28 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 2922) vms_mb | MB | 29 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — qweights.py (PID 2924) CPU | percent | 28 | 195.920 | 134.173 | 200.770 | 199.864 | 55.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — qweights.py (PID 2924) rss_mb | MB | 29 | 128.000 | 31.215 | 146.645 | 114.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — qweights.py (PID 2924) main thread run-queue wait | percent | 28 | 32.449 | 15.089 | 35.006 | 32.624 | 9.139213 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — qweights.py (PID 2924) vms_mb | MB | 29 | 455.790 | 332.027 | 474.363 | 442.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3435) CPU | percent | 7 | 190.093 | 155.818 | 196.883 | 194.991 | 13.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3435) rss_mb | MB | 8 | 225.496 | 18.781 | 273.387 | 148.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3435) main thread run-queue wait | percent | 7 | 47.147 | 26.694 | 51.513 | 51.513 | 3.318217 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3435) vms_mb | MB | 8 | 865.851 | 211.262 | 977.160 | 852.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3445) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3445) rss_mb | MB | 17 | 2.969 | 2.969 | 2.969 | 2.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3445) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3445) vms_mb | MB | 17 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3446) CPU | percent | 15 | 196.949 | 191.980 | 200.683 | 198.559 | 29.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3446) rss_mb | MB | 16 | 239.578 | 213.578 | 242.699 | 242.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3446) main thread run-queue wait | percent | 15 | 60.749 | 59.540 | 67.055 | 59.780 | 9.170134 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3446) vms_mb | MB | 16 | 1012.365 | 983.781 | 1432.285 | 985.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3451) rss_mb | MB | 1 | 106.953 | 106.953 | 106.953 | 106.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3451) vms_mb | MB | 1 | 298.543 | 298.543 | 298.543 | 298.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3590) CPU | percent | 32 | 1.305 | 0.000 | 41.752 | 41.752 | 0.420000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3590) rss_mb | MB | 33 | 6.283 | 3.000 | 111.352 | 111.352 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3590) main thread run-queue wait | percent | 32 | 0.189 | 0.000 | 6.060 | 6.060 | 0.060965 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3590) vms_mb | MB | 33 | 12.073 | 4.215 | 263.520 | 263.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3591) CPU | percent | 31 | 196.873 | 190.866 | 200.714 | 197.691 | 61.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3591) rss_mb | MB | 32 | 285.811 | 130.270 | 380.336 | 221.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3591) main thread run-queue wait | percent | 31 | 60.605 | 53.970 | 67.446 | 60.411 | 18.901195 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3591) vms_mb | MB | 32 | 1013.833 | 362.684 | 1120.070 | 991.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — signals.py (PID 3624) CPU | percent | 10 | 159.550 | 92.467 | 194.692 | 194.692 | 16.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — signals.py (PID 3624) rss_mb | MB | 11 | 372.851 | 21.426 | 575.844 | 429.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — signals.py (PID 3624) main thread run-queue wait | percent | 10 | 30.577 | 5.162 | 45.296 | 45.296 | 3.075980 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — signals.py (PID 3624) vms_mb | MB | 11 | 789.235 | 212.508 | 1008.664 | 907.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mode.py (PID 3664) CPU | percent | 6 | 169.625 | 149.239 | 197.674 | 167.035 | 10.240000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mode.py (PID 3664) rss_mb | MB | 7 | 253.605 | 113.012 | 445.102 | 237.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mode.py (PID 3664) main thread run-queue wait | percent | 6 | 36.250 | 25.215 | 44.577 | 32.106 | 2.188215 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mode.py (PID 3664) vms_mb | MB | 7 | 669.090 | 492.648 | 846.918 | 664.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3681) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3681) rss_mb | MB | 7 | 3.070 | 3.070 | 3.070 | 3.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3681) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3681) vms_mb | MB | 7 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3682) CPU | percent | 6 | 169.233 | 149.110 | 181.660 | 181.660 | 10.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3682) rss_mb | MB | 7 | 304.397 | 124.082 | 454.883 | 282.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3682) main thread run-queue wait | percent | 6 | 30.710 | 22.108 | 37.011 | 37.011 | 1.854557 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3682) vms_mb | MB | 7 | 747.160 | 506.812 | 887.430 | 791.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3780) rss_mb | MB | 1 | 2.961 | 2.961 | 2.961 | 2.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3780) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3781) rss_mb | MB | 1 | 35.934 | 35.934 | 35.934 | 35.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3781) vms_mb | MB | 1 | 227.742 | 227.742 | 227.742 | 227.742 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mathkeys.py (PID 3794) CPU | percent | 11 | 164.738 | 98.279 | 200.795 | 132.236 | 18.230000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mathkeys.py (PID 3794) rss_mb | MB | 12 | 485.042 | 22.492 | 684.492 | 394.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mathkeys.py (PID 3794) main thread run-queue wait | percent | 11 | 37.689 | 10.152 | 59.588 | 21.198 | 4.170035 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — mathkeys.py (PID 3794) vms_mb | MB | 12 | 974.597 | 254.438 | 1195.430 | 905.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3830) CPU | percent | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3830) rss_mb | MB | 30 | 3.051 | 3.051 | 3.051 | 3.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3830) main thread run-queue wait | percent | 29 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3830) vms_mb | MB | 30 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3831) CPU | percent | 22 | 196.547 | 193.892 | 200.958 | 194.887 | 43.510000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3831) rss_mb | MB | 23 | 238.646 | 159.070 | 297.371 | 165.316 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3831) main thread run-queue wait | percent | 22 | 60.392 | 58.626 | 67.157 | 60.874 | 13.368847 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — diag.py (PID 3831) vms_mb | MB | 23 | 1025.976 | 900.625 | 1484.633 | 907.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3837) CPU | percent | 6 | 167.985 | 104.440 | 199.693 | 194.819 | 10.140000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3837) rss_mb | MB | 7 | 442.442 | 14.215 | 703.219 | 395.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3837) main thread run-queue wait | percent | 6 | 40.145 | 5.716 | 65.265 | 50.636 | 2.423453 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3837) vms_mb | MB | 7 | 906.423 | 248.637 | 1191.168 | 906.430 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3853) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3853) rss_mb | MB | 6 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3853) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3853) vms_mb | MB | 6 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3854) CPU | percent | 5 | 171.208 | 78.542 | 206.829 | 175.954 | 8.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3854) rss_mb | MB | 6 | 500.839 | 116.402 | 727.359 | 394.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3854) main thread run-queue wait | percent | 5 | 35.852 | 1.943 | 45.168 | 45.168 | 1.802999 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3854) vms_mb | MB | 6 | 935.422 | 496.453 | 1204.027 | 826.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 3912) CPU | percent | 10 | 176.537 | 117.310 | 202.759 | 202.759 | 17.760000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 3912) rss_mb | MB | 11 | 482.879 | 167.203 | 742.883 | 586.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 3912) main thread run-queue wait | percent | 10 | 40.169 | 18.683 | 51.305 | 46.634 | 4.040999 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 3912) vms_mb | MB | 11 | 958.260 | 576.824 | 1172.297 | 1016.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3926) rss_mb | MB | 1 | 3.039 | 3.039 | 3.039 | 3.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3926) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3927) rss_mb | MB | 1 | 89.516 | 89.516 | 89.516 | 89.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 3927) vms_mb | MB | 1 | 461.398 | 461.398 | 461.398 | 461.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 3946) CPU | percent | 12 | 177.983 | 141.120 | 204.913 | 196.890 | 21.490000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 3946) rss_mb | MB | 13 | 493.309 | 115.863 | 743.824 | 491.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 3946) main thread run-queue wait | percent | 12 | 42.868 | 23.953 | 61.117 | 49.147 | 5.176084 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_adapter.py (PID 3946) vms_mb | MB | 13 | 999.062 | 495.160 | 1172.855 | 918.852 | n/a | n/a |
| docker commit (PID 4019) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4019) io read MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4019) io write MB/s | MB/s | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4019) rss_mb | MB | 22 | 30.695 | 30.695 | 30.695 | 30.695 | n/a | n/a |
| docker commit (PID 4019) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4019) vms_mb | MB | 22 | 2060.289 | 2060.289 | 2060.289 | 2060.289 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 2110 | 19.973 | 0.000 | 208.317 | 0.000 | 424.059239 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2110 | 3.916 | 0.000 | 59.838 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2110 | 3.918 | 0.000 | 59.838 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 2110 | 0.050 | 0.000 | 38.906 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 2110 | 0.050 | 0.000 | 38.906 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 2110 | 0.037 | 0.000 | 20.027 | 0.000 | 78.328125 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 2110 | 0.001 | 0.000 | 0.758 | 0.000 | 2.765625 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 2111 | 262.849 | 22.227 | 990.188 | 200.996 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2110 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2110 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 2110 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001299 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 2110 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 2115 | 30.526 | 1.279 | 268.213 | 2.122 | 650.632548 CPU seconds | n/a |
| workload total memory | MB | 2116 | 10140.393 | 7911.277 | 12695.191 | 11664.309 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
