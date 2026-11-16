# agprof summary

- Duration: **720.123 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **70 calls**, 70 succeeded, 0 failed, 0 interrupted, n/a reported retries, 576.877 s total wait
- Tools: **108/108 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **74789** at 1.982 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 700376.468 / 700376.468 ms |
| LLM latency p50 / p95 | 6881.969 / 18160.775 ms |
| LLM TTFT p50 / p95 | 1754.874 / 3503.374 ms |
| LLM input / output tokens | 5502078 / 78799 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 70 total, 70 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 419.754 / 2258.450 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| attention | 2/2 | 2 | 0 | 0 | 315.665 ms | 328.615 ms |
| attribution | 1/1 | 1 | 0 | 0 | 317.722 ms | 317.722 ms |
| bash | 32/32 | 32 | 0 | 0 | 1164.791 ms | 3447.909 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 318.861 ms | 318.861 ms |
| generate | 16/16 | 16 | 0 | 0 | 532.711 ms | 991.251 ms |
| inspect | 3/3 | 3 | 0 | 0 | 1883.087 ms | 2224.206 ms |
| inspect_module_inputs | 10/10 | 10 | 0 | 0 | 1645.842 ms | 2293.467 ms |
| patch | 34/34 | 34 | 0 | 0 | 412.478 ms | 422.156 ms |
| read | 8/8 | 8 | 0 | 0 | 0.329 ms | 0.753 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 239.615 ms | 239.615 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 9.804% | 102.065% | 70.541 s | 5506.404 MB | 5736.441 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 3554 |  | 715 | 7.717% | 101.936% | 55.540 s | 2843.453 MB | 3055.512 MB | 15849.802 MB | 16184.809 MB | 3.582031 MB | 511.656250 MB |
| python | 3598 |  | 715 | 0.000% | 0.000% | 0.000 s | 12.195 MB | 12.195 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| lsb_guard.sh | 3565 |  | 715 | 0.000% | 0.000% | 0.000 s | 3.434 MB | 3.434 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 3954 | sandbox_agent_lsb-native_0000_0000 | 696 | 6.981% | 88.361% | 48.890 s | 106.554 MB | 111.070 MB | 964.021 MB | 972.805 MB | n/a MB | n/a MB |
| lsb_grid_worker | 3545 |  | 715 | 0.000% | 0.000% | 0.000 s | 3.387 MB | 3.387 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| sleep | 3568 |  | 16 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| tail | 3864 | sandbox_agent_lsb-native_0000_0000 | 696 | 0.001% | 0.995% | 0.010 s | 1.535 MB | 1.535 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 3960 | sandbox_agent_lsb-native_0000_0000 | 2 | 99.827% | 99.827% | 1.010 s | 53.096 MB | 79.711 MB | 64.223 MB | 94.285 MB | n/a MB | n/a MB |
| docker-init | 3833 | sandbox_agent_lsb-native_0000_0000 | 696 | 0.001% | 0.995% | 0.010 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| vllm | 3559 |  | 715 | 0.207% | 7.903% | 1.490 s | 1783.305 MB | 1783.332 MB | 11022.397 MB | 11024.051 MB | 0.000000 MB | 0.054688 MB |
| VLLM::EngineCor | 3599 |  | 715 | 1.830% | 40.504% | 13.150 s | 2325.531 MB | 2325.594 MB | 21203.732 MB | 21204.082 MB | 0.000000 MB | 0.003906 MB |
| python3 | 3972 | sandbox_agent_lsb-native_0000_0000 | 670 | 0.683% | 64.281% | 4.610 s | 72.170 MB | 73.582 MB | 86.306 MB | 87.887 MB | n/a MB | n/a MB |
| sleep | 4017 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4164 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4275 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.727 MB | 9.727 MB | 13.340 MB | 13.340 MB | n/a MB | n/a MB |
| bash | 4274 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.836 MB | 2.836 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 4300 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| bash | 4327 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.926 MB | 2.926 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4329 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 48.383 MB | 48.383 MB | 269.047 MB | 269.047 MB | n/a MB | n/a MB |
| sleep | 4334 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| sleep | 4395 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4450 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.230 MB | 9.230 MB | 13.477 MB | 13.477 MB | n/a MB | n/a MB |
| sleep | 4461 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4471 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 115.355 MB | 115.355 MB | 333.988 MB | 333.988 MB | n/a MB | n/a MB |
| python | 4487 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 123.258 MB | 123.258 MB | 340.207 MB | 340.207 MB | n/a MB | n/a MB |
| sleep | 4499 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4506 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 873.801 MB | 873.801 MB | 1729.293 MB | 1729.293 MB | n/a MB | n/a MB |
| bash | 4546 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.078 MB | 3.078 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4547 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 25.539 MB | 25.539 MB | 217.207 MB | 217.207 MB | n/a MB | n/a MB |
| python | 4557 | sandbox_agent_lsb-native_0000_0000 | 2 | 107.410% | 107.410% | 1.080 s | 1032.426 MB | 2047.008 MB | 1237.971 MB | 2266.047 MB | n/a MB | n/a MB |
| sleep | 4575 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4661 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.727 MB | 23.727 MB | 215.816 MB | 215.816 MB | n/a MB | n/a MB |
| python | 4671 | sandbox_agent_lsb-native_0000_0000 | 2 | 110.315% | 110.315% | 1.110 s | 1039.762 MB | 2062.031 MB | 1245.998 MB | 2282.070 MB | n/a MB | n/a MB |
| python | 4681 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 63.184 MB | 63.184 MB | 255.059 MB | 255.059 MB | n/a MB | n/a MB |
| python | 4689 | sandbox_agent_lsb-native_0000_0000 | 2 | 145.139% | 145.139% | 1.460 s | 1148.578 MB | 2061.629 MB | 1520.262 MB | 2281.109 MB | n/a MB | n/a MB |
| sleep | 4698 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.617 MB | 1.617 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4701 | sandbox_agent_lsb-native_0000_0000 | 2 | 110.164% | 110.164% | 1.110 s | 1047.229 MB | 2075.957 MB | 1254.117 MB | 2298.117 MB | n/a MB | n/a MB |
| bash | 4714 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.043 MB | 3.043 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4715 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.859 MB | 6.859 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python | 4716 | sandbox_agent_lsb-native_0000_0000 | 2 | 171.680% | 171.680% | 1.730 s | 898.455 MB | 1680.539 MB | 2972.379 MB | 3669.535 MB | n/a MB | n/a MB |
| python | 4730 | sandbox_agent_lsb-native_0000_0000 | 3 | 149.008% | 195.780% | 3.000 s | 1404.833 MB | 2145.590 MB | 1988.169 MB | 3669.453 MB | n/a MB | n/a MB |
| bash | 4728 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.961 MB | 2.961 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| sleep | 4748 |  | 60 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4742 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 132.465 MB | 132.465 MB | 348.695 MB | 348.695 MB | n/a MB | n/a MB |
| bash | 4752 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.918 MB | 2.918 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4754 | sandbox_agent_lsb-native_0000_0000 | 2 | 127.036% | 127.036% | 1.280 s | 1083.561 MB | 2066.094 MB | 1522.746 MB | 2286.090 MB | n/a MB | n/a MB |
| python | 4762 | sandbox_agent_lsb-native_0000_0000 | 2 | 121.031% | 121.031% | 1.220 s | 1041.588 MB | 2058.219 MB | 1249.568 MB | 2281.977 MB | n/a MB | n/a MB |
| bash | 4772 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.883 MB | 2.883 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4774 | sandbox_agent_lsb-native_0000_0000 | 2 | 121.273% | 121.273% | 1.220 s | 1052.473 MB | 2061.727 MB | 1258.875 MB | 2282.109 MB | n/a MB | n/a MB |
| python | 4778 | sandbox_agent_lsb-native_0000_0000 | 2 | 144.958% | 144.958% | 1.460 s | 1251.832 MB | 2058.543 MB | 1520.633 MB | 2281.977 MB | n/a MB | n/a MB |
| python | 4807 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 85.930 MB | 85.930 MB | 304.680 MB | 304.680 MB | n/a MB | n/a MB |
| sleep | 4816 |  | 59 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| python | 4820 | sandbox_agent_lsb-native_0000_0000 | 3 | 134.374% | 173.901% | 2.710 s | 1502.926 MB | 2422.730 MB | 2055.776 MB | 3669.164 MB | n/a MB | n/a MB |
| bash | 4831 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.930 MB | 2.930 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 4833 | sandbox_agent_lsb-native_0000_0000 | 4 | 196.828% | 198.717% | 5.940 s | 115.929 MB | 156.379 MB | 375.900 MB | 409.828 MB | n/a MB | n/a MB |
| pgrep | 4848 |  | 1 | n/a% | n/a% | n/a s | 3.305 MB | 3.305 MB | 10.102 MB | 10.102 MB | n/a MB | n/a MB |
| sleep | 4849 |  | 42 | 0.000% | 0.000% | 0.000 s | 1.621 MB | 1.621 MB | 5.633 MB | 5.633 MB | 0.000000 MB | 0.000000 MB |
| docker | 4879 |  | 21 | 0.000% | 0.000% | 0.000 s | 30.328 MB | 30.328 MB | 1843.520 MB | 1843.520 MB | 0.000000 MB | 0.000000 MB |
| docker | 4930 |  | 1 | n/a% | n/a% | n/a s | 29.059 MB | 29.059 MB | 1771.188 MB | 1771.188 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1.968% | 100.000% | 11886.389 MB | 12010.000 MB | 29.672 W | 74.040 W | 21318.165 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 15.702% | 202.006% | 109.954 s | 233.343 MB | 2780.125 MB | 10.542969 MB | 241.523438 MB | 0.000978 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 3723 | 720.057 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 700.376 | n/a | n/a | 10.543 | 700376.468 | 700376.468 | 700376.468 |
| engine:execute | 1/1 | 0 | 0 | 700.375 | 1.503 | 698.870 | 10.543 | 700374.845 | 700374.845 | 700374.845 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 674.247 | 0.002 | 674.246 | 10.543 | 674247.414 | 674247.414 | 674247.414 |
| turn | 70/70 | 0 | 0 | 671.844 | n/a | n/a | 10.541 | 9597.765 | 8202.281 | 22390.115 |
| llm:attempt | 70/70 | 0 | 0 | 576.877 | 15.345 | 561.529 | 1.289 | 8241.099 | 6881.969 | 18160.775 |
| tool:bash | 32/32 | 0 | 0 | 39.799 | n/a | n/a | 8.990 | 1243.705 | 1164.791 | 3447.909 |
| process:bash | 32/32 | 4 | 0 | 39.464 | n/a | n/a | 8.987 | 1233.261 | 1155.333 | 3439.444 |
| run:container_call | 13/13 | 0 | 0 | 22.760 | 0.002 | 22.758 | 0.000 | 1750.792 | 35.854 | 8959.221 |
| teardown:commit | 1/1 | 0 | 0 | 22.337 | 0.005 | 22.333 | 0.000 | 22337.429 | 22337.429 | 22337.429 |
| sandbox:commit | 1/1 | 0 | 0 | 22.156 | 0.003 | 22.153 | 0.000 | 22156.287 | 22156.287 | 22156.287 |
| checkpoint.total | 1/1 | 0 | 0 | 22.156 | 0.003 | 22.153 | 0.000 | 22156.157 | 22156.157 | 22156.157 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 22.156 | 0.003 | 22.153 | 0.000 | 22156.021 | 22156.021 | 22156.021 |
| tool:inspect_module_inputs | 10/10 | 0 | 0 | 16.598 | n/a | n/a | 0.000 | 1659.825 | 1645.842 | 2293.467 |
| tool:patch | 34/34 | 0 | 0 | 14.065 | n/a | n/a | 0.000 | 413.686 | 412.478 | 422.156 |
| tool:generate | 16/16 | 0 | 0 | 9.896 | n/a | n/a | 0.000 | 618.483 | 532.711 | 991.251 |
| tool:inspect | 3/3 | 0 | 0 | 6.000 | n/a | n/a | 0.000 | 1999.863 | 1883.087 | 2224.206 |
| syscall:sendto | 2495/2495 | 0 | 0 | 5.722 | n/a | n/a | 0.103 | 2.293 | 1.952 | 4.274 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.163 | 0.724 | 2.438 | 0.000 | 3162.630 | 3162.630 | 3162.630 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.162 | 0.724 | 2.438 | 0.000 | 3162.344 | 3162.344 | 3162.344 |
| syscall:connect | 602/602 | 0 | 0 | 1.317 | n/a | n/a | 0.066 | 2.188 | 1.838 | 4.448 |
| tool:attention | 2/2 | 0 | 0 | 0.631 | n/a | n/a | 0.000 | 315.665 | 315.665 | 328.615 |
| sandbox:start | 1/1 | 0 | 0 | 0.356 | 0.002 | 0.354 | 0.000 | 356.396 | 356.396 | 356.396 |
| runtime.container_create | 1/1 | 0 | 0 | 0.356 | 0.002 | 0.354 | 0.000 | 356.235 | 356.235 | 356.235 |
| sandbox:create | 1/1 | 0 | 0 | 0.339 | 0.244 | 0.096 | 0.000 | 339.189 | 339.189 | 339.189 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.319 | n/a | n/a | 0.000 | 318.861 | 318.861 | 318.861 |
| tool:attribution | 1/1 | 0 | 0 | 0.318 | n/a | n/a | 0.000 | 317.722 | 317.722 | 317.722 |
| tool:submit_output | 1/1 | 0 | 0 | 0.240 | n/a | n/a | 0.000 | 239.615 | 239.615 | 239.615 |
| syscall:execve | 132/132 | 0 | 0 | 0.193 | n/a | n/a | 0.056 | 1.465 | 1.185 | 2.964 |
| sandbox:stop | 1/1 | 0 | 0 | 0.181 | 0.001 | 0.179 | 0.000 | 180.906 | 180.906 | 180.906 |
| agency:services_close | 1/1 | 0 | 0 | 0.134 | 0.001 | 0.133 | 0.000 | 133.507 | 133.507 | 133.507 |
| agency:services_start | 1/1 | 0 | 0 | 0.073 | 0.041 | 0.031 | 0.000 | 72.703 | 72.703 | 72.703 |
| run:detect | 1/1 | 0 | 0 | 0.057 | 0.001 | 0.057 | 0.000 | 57.490 | 57.490 | 57.490 |
| agent:create | 1/1 | 0 | 0 | 0.050 | 0.008 | 0.042 | 0.000 | 49.744 | 49.744 | 49.744 |
| tool:read | 8/8 | 0 | 0 | 0.003 | n/a | n/a | 0.000 | 0.417 | 0.329 | 0.753 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.222 | 1.222 | 1.222 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.068 | 0.059 | 0.103 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.772 | 0.772 | 0.772 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.167 | 0.167 | 0.167 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.063 | 0.063 | 0.063 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 714 | 1.007 | 0.040 | 50.658 | 0.073 | 7.234840 CPU seconds | n/a |
| GPU 0 memory | MB | 715 | 11886.389 | 11670.000 | 12010.000 | 11944.000 | n/a | n/a |
| GPU 0 power | W | 715 | 29.672 | 28.150 | 74.040 | 28.371 | n/a | 21318.165 J |
| GPU 0 proc / 3554-79972 / sandbox / ~ / device / GPU-7db7d2a2-1c9b-2757-88f6-523e771e91b1 memory | MB | 715 | 3258.288 | 3118.000 | 3380.000 | 3314.000 | n/a | n/a |
| GPU 0 proc / 3554-79972 / sandbox / ~ / device / GPU-7db7d2a2-1c9b-2757-88f6-523e771e91b1 estimated power | W | 549 | 2.935 | 0.000 | 58.034 | 0.000 | n/a | n/a |
| GPU 0 proc / 3554-79972 / sandbox / ~ / device / GPU-7db7d2a2-1c9b-2757-88f6-523e771e91b1 utilization | percent | 549 | 2.026 | 0.000 | 48.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 3599-81806 / sandbox / ~ / device / GPU-7db7d2a2-1c9b-2757-88f6-523e771e91b1 memory | MB | 715 | 8146.101 | 8070.000 | 8148.000 | 8148.000 | n/a | n/a |
| GPU 0 proc / 3599-81806 / sandbox / ~ / device / GPU-7db7d2a2-1c9b-2757-88f6-523e771e91b1 estimated power | W | 161 | 3.576 | 0.000 | 67.376 | 0.000 | n/a | n/a |
| GPU 0 proc / 3599-81806 / sandbox / ~ / device / GPU-7db7d2a2-1c9b-2757-88f6-523e771e91b1 utilization | percent | 161 | 2.652 | 0.000 | 91.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 715 | 11404.389 | 11188.000 | 11528.000 | 11462.000 | n/a | n/a |
| GPU 0 utilization | percent | 715 | 1.968 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 715 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 714 | 2.006 | 0.039 | 53.852 | 0.226 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 714 | 6.340 | 0.000 | 51.733 | 0.500 | n/a | n/a |
| host disk_read_mb_s | MB/s | 714 | 2.331 | 0.000 | 193.023 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 714 | 1.059 | 0.000 | 79.584 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 714 | 1.067 | 0.000 | 53.982 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 714 | 1.077 | 0.000 | 54.139 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 715 | 15363.539 | 15363.539 | 15363.539 | 15363.539 | n/a | n/a |
| host mem_used_mb | MB | 715 | 7002.481 | 6404.621 | 9806.363 | 6978.828 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 714 | 0.000 | 0.000 | 0.134 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 714 | 0.000 | 0.000 | 0.134 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 714 | 0.032 | 0.000 | 0.137 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 714 | 0.027 | 0.000 | 0.495 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3545) CPU | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 3545) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3545) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3545) rss_mb | MB | 715 | 3.387 | 3.387 | 3.387 | 3.387 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3545) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 3545) vms_mb | MB | 715 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3554) CPU | percent | 714 | 7.717 | 0.000 | 101.936 | 0.000 | 55.540000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 3554) io read MB/s | MB/s | 714 | 0.005 | 0.000 | 1.726 | 0.000 | 3.582031 MB | n/a |
| Agency harness — python -m lsbench (PID 3554) io write MB/s | MB/s | 714 | 0.711 | 0.023 | 34.308 | 0.023 | 511.656250 MB | n/a |
| Agency harness — python -m lsbench (PID 3554) rss_mb | MB | 715 | 2843.453 | 2295.590 | 3055.512 | 3055.512 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3554) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000008 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 3554) vms_mb | MB | 715 | 15849.802 | 13731.879 | 16184.809 | 16097.621 | n/a | n/a |
| Python — vllm (PID 3559) CPU | percent | 714 | 0.207 | 0.000 | 7.903 | 0.000 | 1.490000 CPU seconds | n/a |
| Python — vllm (PID 3559) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 3559) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.008 | 0.000 | 0.054688 MB | n/a |
| Python — vllm (PID 3559) rss_mb | MB | 715 | 1783.305 | 1782.332 | 1783.332 | 1783.332 | n/a | n/a |
| Python — vllm (PID 3559) main thread run-queue wait | percent | 714 | 0.004 | 0.000 | 0.354 | 0.001 | 0.029266 run-queue seconds | n/a |
| Python — vllm (PID 3559) vms_mb | MB | 715 | 11022.397 | 10951.031 | 11024.051 | 11024.051 | n/a | n/a |
| bash lsb_guard.sh (PID 3565) CPU | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_guard.sh (PID 3565) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3565) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_guard.sh (PID 3565) rss_mb | MB | 715 | 3.434 | 3.434 | 3.434 | 3.434 | n/a | n/a |
| bash lsb_guard.sh (PID 3565) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.107 | 0.000 | 0.001166 run-queue seconds | n/a |
| bash lsb_guard.sh (PID 3565) vms_mb | MB | 715 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| sleep (PID 3568) CPU | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 3568) io read MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3568) io write MB/s | MB/s | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 3568) rss_mb | MB | 16 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 3568) main thread run-queue wait | percent | 15 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 3568) vms_mb | MB | 16 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| Python — python -c (PID 3598) CPU | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 3598) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3598) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3598) rss_mb | MB | 715 | 12.195 | 12.195 | 12.195 | 12.195 | n/a | n/a |
| Python — python -c (PID 3598) main thread run-queue wait | percent | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 3598) vms_mb | MB | 715 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 3599) CPU | percent | 714 | 1.830 | 0.000 | 40.504 | 1.991 | 13.150000 CPU seconds | n/a |
| VLLM::EngineCore (PID 3599) io read MB/s | MB/s | 714 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 3599) io write MB/s | MB/s | 714 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 3599) rss_mb | MB | 715 | 2325.531 | 2325.312 | 2325.594 | 2325.594 | n/a | n/a |
| VLLM::EngineCore (PID 3599) main thread run-queue wait | percent | 714 | 0.001 | 0.000 | 0.177 | 0.000 | 0.006561 run-queue seconds | n/a |
| VLLM::EngineCore (PID 3599) vms_mb | MB | 715 | 21203.732 | 21203.082 | 21204.082 | 21204.082 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3833) CPU | percent | 695 | 0.001 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3833) rss_mb | MB | 696 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3833) main thread run-queue wait | percent | 695 | 0.012 | 0.000 | 5.013 | 0.000 | 0.081785 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 3833) vms_mb | MB | 696 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3864) CPU | percent | 695 | 0.001 | 0.000 | 0.995 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3864) rss_mb | MB | 696 | 1.535 | 1.535 | 1.535 | 1.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3864) main thread run-queue wait | percent | 695 | 0.011 | 0.000 | 5.095 | 0.002 | 0.079449 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 3864) vms_mb | MB | 696 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3954) CPU | percent | 695 | 6.981 | 0.000 | 88.361 | 0.000 | 48.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3954) rss_mb | MB | 696 | 106.554 | 3.207 | 111.070 | 108.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3954) main thread run-queue wait | percent | 695 | 0.000 | 0.000 | 0.008 | 0.001 | 0.000158 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 3954) vms_mb | MB | 696 | 964.021 | 4.258 | 972.805 | 972.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3960) CPU | percent | 1 | 99.827 | 99.827 | 99.827 | 99.827 | 1.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3960) rss_mb | MB | 2 | 53.096 | 26.480 | 79.711 | 79.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3960) main thread run-queue wait | percent | 1 | 0.007 | 0.007 | 0.007 | 0.007 | 0.000069 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 3960) vms_mb | MB | 2 | 64.223 | 34.160 | 94.285 | 94.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3972) CPU | percent | 669 | 0.683 | 0.000 | 64.281 | 0.000 | 4.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3972) rss_mb | MB | 670 | 72.170 | 29.094 | 73.582 | 73.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3972) main thread run-queue wait | percent | 669 | 0.050 | 0.000 | 3.228 | 0.000 | 0.339912 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 3972) vms_mb | MB | 670 | 86.306 | 35.754 | 87.887 | 87.430 | n/a | n/a |
| sleep (PID 4017) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4017) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4017) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4017) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4017) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4017) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4164) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4164) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4164) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4164) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4164) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4164) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4274) rss_mb | MB | 1 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4274) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4275) rss_mb | MB | 1 | 9.727 | 9.727 | 9.727 | 9.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4275) vms_mb | MB | 1 | 13.340 | 13.340 | 13.340 | 13.340 | n/a | n/a |
| sleep (PID 4300) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4300) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4300) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4300) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4300) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4300) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4327) rss_mb | MB | 1 | 2.926 | 2.926 | 2.926 | 2.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4327) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_acts.py (PID 4329) rss_mb | MB | 1 | 48.383 | 48.383 | 48.383 | 48.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — analyze_acts.py (PID 4329) vms_mb | MB | 1 | 269.047 | 269.047 | 269.047 | 269.047 | n/a | n/a |
| sleep (PID 4334) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4334) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4334) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4334) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4334) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4334) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sleep (PID 4395) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4395) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4395) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4395) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4395) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4395) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — derive_adapter.py (PID 4450) rss_mb | MB | 1 | 9.230 | 9.230 | 9.230 | 9.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — derive_adapter.py (PID 4450) vms_mb | MB | 1 | 13.477 | 13.477 | 13.477 | 13.477 | n/a | n/a |
| sleep (PID 4461) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4461) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4461) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4461) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4461) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4461) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — compare_maps.py (PID 4471) rss_mb | MB | 1 | 115.355 | 115.355 | 115.355 | 115.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — compare_maps.py (PID 4471) vms_mb | MB | 1 | 333.988 | 333.988 | 333.988 | 333.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — derive_orthogonal.py (PID 4487) rss_mb | MB | 1 | 123.258 | 123.258 | 123.258 | 123.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — derive_orthogonal.py (PID 4487) vms_mb | MB | 1 | 340.207 | 340.207 | 340.207 | 340.207 | n/a | n/a |
| sleep (PID 4499) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4499) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4499) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4499) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4499) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4499) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — head_analysis.py (PID 4506) rss_mb | MB | 1 | 873.801 | 873.801 | 873.801 | 873.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — head_analysis.py (PID 4506) vms_mb | MB | 1 | 1729.293 | 1729.293 | 1729.293 | 1729.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4546) rss_mb | MB | 1 | 3.078 | 3.078 | 3.078 | 3.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4546) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4547) rss_mb | MB | 1 | 25.539 | 25.539 | 25.539 | 25.539 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4547) vms_mb | MB | 1 | 217.207 | 217.207 | 217.207 | 217.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — head_edit_analysis.py (PID 4557) CPU | percent | 1 | 107.410 | 107.410 | 107.410 | 107.410 | 1.080000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — head_edit_analysis.py (PID 4557) rss_mb | MB | 2 | 1032.426 | 17.844 | 2047.008 | 2047.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — head_edit_analysis.py (PID 4557) main thread run-queue wait | percent | 1 | 0.564 | 0.564 | 0.564 | 0.564 | 0.005671 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — head_edit_analysis.py (PID 4557) vms_mb | MB | 2 | 1237.971 | 209.895 | 2266.047 | 2266.047 | n/a | n/a |
| sleep (PID 4575) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4575) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4575) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4575) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4575) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4575) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — content_head_eval.py (PID 4661) rss_mb | MB | 1 | 23.727 | 23.727 | 23.727 | 23.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — content_head_eval.py (PID 4661) vms_mb | MB | 1 | 215.816 | 215.816 | 215.816 | 215.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — global_projector_eval.py (PID 4671) CPU | percent | 1 | 110.315 | 110.315 | 110.315 | 110.315 | 1.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — global_projector_eval.py (PID 4671) rss_mb | MB | 2 | 1039.762 | 17.492 | 2062.031 | 2062.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — global_projector_eval.py (PID 4671) main thread run-queue wait | percent | 1 | 2.044 | 2.044 | 2.044 | 2.044 | 0.020570 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — global_projector_eval.py (PID 4671) vms_mb | MB | 2 | 1245.998 | 209.926 | 2282.070 | 2282.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_projector.py (PID 4681) rss_mb | MB | 1 | 63.184 | 63.184 | 63.184 | 63.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_projector.py (PID 4681) vms_mb | MB | 1 | 255.059 | 255.059 | 255.059 | 255.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_projector.py (PID 4689) CPU | percent | 1 | 145.139 | 145.139 | 145.139 | 145.139 | 1.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_projector.py (PID 4689) rss_mb | MB | 2 | 1148.578 | 235.527 | 2061.629 | 2061.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_projector.py (PID 4689) main thread run-queue wait | percent | 1 | 19.344 | 19.344 | 19.344 | 19.344 | 0.194583 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_projector.py (PID 4689) vms_mb | MB | 2 | 1520.262 | 759.414 | 2281.109 | 2281.109 | n/a | n/a |
| sleep (PID 4698) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4698) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4698) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4698) rss_mb | MB | 59 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sleep (PID 4698) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4698) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_rrr.py (PID 4701) CPU | percent | 1 | 110.164 | 110.164 | 110.164 | 110.164 | 1.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_rrr.py (PID 4701) rss_mb | MB | 2 | 1047.229 | 18.500 | 2075.957 | 2075.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_rrr.py (PID 4701) main thread run-queue wait | percent | 1 | 3.611 | 3.611 | 3.611 | 3.611 | 0.036387 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — wrong_right_rrr.py (PID 4701) vms_mb | MB | 2 | 1254.117 | 210.117 | 2298.117 | 2298.117 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4714) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4714) rss_mb | MB | 3 | 3.043 | 3.043 | 3.043 | 3.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4714) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4714) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4715) rss_mb | MB | 1 | 6.859 | 6.859 | 6.859 | 6.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 4715) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — numeric_rrr_eval.py (PID 4716) CPU | percent | 1 | 171.680 | 171.680 | 171.680 | 171.680 | 1.730000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — numeric_rrr_eval.py (PID 4716) rss_mb | MB | 2 | 898.455 | 116.371 | 1680.539 | 116.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — numeric_rrr_eval.py (PID 4716) main thread run-queue wait | percent | 1 | 47.391 | 47.391 | 47.391 | 47.391 | 0.477553 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — numeric_rrr_eval.py (PID 4716) vms_mb | MB | 2 | 2972.379 | 2275.223 | 3669.535 | 2275.223 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4728) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4728) rss_mb | MB | 3 | 2.961 | 2.961 | 2.961 | 2.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4728) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4728) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — layer15_rrr_eval.py (PID 4730) CPU | percent | 2 | 149.008 | 102.236 | 195.780 | 195.780 | 3.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — layer15_rrr_eval.py (PID 4730) rss_mb | MB | 3 | 1404.833 | 7.625 | 2145.590 | 2061.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — layer15_rrr_eval.py (PID 4730) main thread run-queue wait | percent | 2 | 27.214 | 12.242 | 42.185 | 42.185 | 0.547814 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — layer15_rrr_eval.py (PID 4730) vms_mb | MB | 3 | 1988.169 | 12.918 | 3669.453 | 2282.137 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — conditional_rrr.py (PID 4742) rss_mb | MB | 1 | 132.465 | 132.465 | 132.465 | 132.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — conditional_rrr.py (PID 4742) vms_mb | MB | 1 | 348.695 | 348.695 | 348.695 | 348.695 | n/a | n/a |
| sleep (PID 4748) CPU | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4748) io read MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4748) io write MB/s | MB/s | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4748) rss_mb | MB | 60 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4748) main thread run-queue wait | percent | 59 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4748) vms_mb | MB | 60 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4752) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4752) rss_mb | MB | 2 | 2.918 | 2.918 | 2.918 | 2.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4752) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4752) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_rrr.py (PID 4754) CPU | percent | 1 | 127.036 | 127.036 | 127.036 | 127.036 | 1.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_rrr.py (PID 4754) rss_mb | MB | 2 | 1083.561 | 101.027 | 2066.094 | 2066.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_rrr.py (PID 4754) main thread run-queue wait | percent | 1 | 15.157 | 15.157 | 15.157 | 15.157 | 0.152720 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_rrr.py (PID 4754) vms_mb | MB | 2 | 1522.746 | 759.402 | 2286.090 | 2286.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_numeric.py (PID 4762) CPU | percent | 1 | 121.031 | 121.031 | 121.031 | 121.031 | 1.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_numeric.py (PID 4762) rss_mb | MB | 2 | 1041.588 | 24.957 | 2058.219 | 2058.219 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_numeric.py (PID 4762) main thread run-queue wait | percent | 1 | 9.465 | 9.465 | 9.465 | 9.465 | 0.095411 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_numeric.py (PID 4762) vms_mb | MB | 2 | 1249.568 | 217.160 | 2281.977 | 2281.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4772) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4772) rss_mb | MB | 4 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4772) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4772) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_norm_rrr.py (PID 4774) CPU | percent | 1 | 121.273 | 121.273 | 121.273 | 121.273 | 1.220000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_norm_rrr.py (PID 4774) rss_mb | MB | 2 | 1052.473 | 43.219 | 2061.727 | 2061.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_norm_rrr.py (PID 4774) main thread run-queue wait | percent | 1 | 13.390 | 13.390 | 13.390 | 13.390 | 0.134706 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_norm_rrr.py (PID 4774) vms_mb | MB | 2 | 1258.875 | 235.641 | 2282.109 | 2282.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_norm_numeric.py (PID 4778) CPU | percent | 1 | 144.958 | 144.958 | 144.958 | 144.958 | 1.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_norm_numeric.py (PID 4778) rss_mb | MB | 2 | 1251.832 | 445.121 | 2058.543 | 2058.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_norm_numeric.py (PID 4778) main thread run-queue wait | percent | 1 | 26.854 | 26.854 | 26.854 | 26.854 | 0.270474 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — failure_norm_numeric.py (PID 4778) vms_mb | MB | 2 | 1520.633 | 759.289 | 2281.977 | 2281.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_compare.py (PID 4807) rss_mb | MB | 1 | 85.930 | 85.930 | 85.930 | 85.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — final_compare.py (PID 4807) vms_mb | MB | 1 | 304.680 | 304.680 | 304.680 | 304.680 | n/a | n/a |
| sleep (PID 4816) CPU | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4816) io read MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4816) io write MB/s | MB/s | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4816) rss_mb | MB | 59 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4816) main thread run-queue wait | percent | 58 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4816) vms_mb | MB | 59 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — regularized_rrr.py (PID 4820) CPU | percent | 2 | 134.374 | 94.847 | 173.901 | 173.901 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — regularized_rrr.py (PID 4820) rss_mb | MB | 3 | 1502.926 | 13.793 | 2422.730 | 2072.254 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — regularized_rrr.py (PID 4820) main thread run-queue wait | percent | 2 | 34.869 | 9.570 | 60.167 | 60.167 | 0.702339 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — regularized_rrr.py (PID 4820) vms_mb | MB | 3 | 2055.776 | 207.480 | 3669.164 | 2290.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4831) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4831) rss_mb | MB | 4 | 2.930 | 2.930 | 2.930 | 2.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4831) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 4831) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_verify_adapter.py (PID 4833) CPU | percent | 3 | 196.828 | 194.871 | 198.717 | 194.871 | 5.940000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_verify_adapter.py (PID 4833) rss_mb | MB | 4 | 115.929 | 61.363 | 156.379 | 156.379 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_verify_adapter.py (PID 4833) main thread run-queue wait | percent | 3 | 48.263 | 45.164 | 49.891 | 49.734 | 1.456522 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — build_verify_adapter.py (PID 4833) vms_mb | MB | 4 | 375.900 | 361.828 | 409.828 | 370.117 | n/a | n/a |
| pgrep (PID 4848) rss_mb | MB | 1 | 3.305 | 3.305 | 3.305 | 3.305 | n/a | n/a |
| pgrep (PID 4848) vms_mb | MB | 1 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sleep (PID 4849) CPU | percent | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sleep (PID 4849) io read MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4849) io write MB/s | MB/s | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| sleep (PID 4849) rss_mb | MB | 42 | 1.621 | 1.621 | 1.621 | 1.621 | n/a | n/a |
| sleep (PID 4849) main thread run-queue wait | percent | 41 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sleep (PID 4849) vms_mb | MB | 42 | 5.633 | 5.633 | 5.633 | 5.633 | n/a | n/a |
| docker commit (PID 4879) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 4879) io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4879) io write MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 4879) rss_mb | MB | 21 | 30.328 | 30.328 | 30.328 | 30.328 | n/a | n/a |
| docker commit (PID 4879) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 4879) vms_mb | MB | 21 | 1843.520 | 1843.520 | 1843.520 | 1843.520 | n/a | n/a |
| docker stop (PID 4930) rss_mb | MB | 1 | 29.059 | 29.059 | 29.059 | 29.059 | n/a | n/a |
| docker stop (PID 4930) vms_mb | MB | 1 | 1771.188 | 1771.188 | 1771.188 | 1771.188 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 695 | 15.702 | 0.000 | 202.006 | 0.036 | 109.954128 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 695 | 1.629 | 0.000 | 50.237 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 695 | 1.872 | 0.000 | 52.838 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 695 | 0.003 | 0.000 | 1.176 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 695 | 0.004 | 0.000 | 1.182 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 695 | 0.015 | 0.000 | 6.382 | 0.000 | 10.542969 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 695 | 0.346 | 0.000 | 79.584 | 0.000 | 241.523438 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 696 | 233.343 | 17.605 | 2780.125 | 351.598 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 695 | 0.000 | 0.000 | 0.148 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 695 | 0.000 | 0.000 | 0.148 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000978 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 695 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 714 | 9.804 | 1.473 | 102.065 | 2.025 | 70.540521 CPU seconds | n/a |
| workload total memory | MB | 715 | 5506.404 | 4938.133 | 5736.441 | 5729.859 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
