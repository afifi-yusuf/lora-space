# agprof summary

- Duration: **840.112 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **30 calls**, 30 succeeded, 0 failed, 0 interrupted, n/a reported retries, 625.342 s total wait
- Tools: **64/64 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **77472** at 1.988 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 818057.530 / 818057.530 ms |
| LLM latency p50 / p95 | 21721.142 / 35439.796 ms |
| LLM TTFT p50 / p95 | 5696.165 / 6588.548 ms |
| LLM input / output tokens | 4444171 / 97017 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 30 total, 30 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | 1855.057 / 9375.403 ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- native: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "container_asserted"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 22/22 | 22 | 0 | 0 | 1949.962 ms | 6084.608 ms |
| commit_adapter | 1/1 | 1 | 0 | 0 | 304.730 ms | 304.730 ms |
| edit | 2/2 | 2 | 0 | 0 | 0.509 ms | 0.525 ms |
| generate | 13/13 | 13 | 0 | 0 | 5381.079 ms | 11964.690 ms |
| inspect_module_inputs | 2/2 | 2 | 0 | 0 | 1550.184 ms | 1823.531 ms |
| logit_lens | 1/1 | 1 | 0 | 0 | 6967.795 ms | 6967.795 ms |
| patch | 3/3 | 3 | 0 | 0 | 406.955 ms | 419.499 ms |
| submit_output | 1/1 | 1 | 0 | 0 | 211.439 ms | 211.439 ms |
| token_stats | 2/2 | 2 | 0 | 0 | 6449.233 ms | 10424.496 ms |
| top_activations | 2/2 | 2 | 0 | 0 | 5265.590 ms | 5285.286 ms |
| trace | 9/9 | 9 | 0 | 0 | 1556.740 ms | 2029.216 ms |
| write | 6/6 | 6 | 0 | 0 | 0.390 ms | 0.441 ms |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 21.992% | 799.360% | 184.763 s | 11682.587 MB | 12457.504 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vllm | 9124 |  | 834 | 0.456% | 7.934% | 3.830 s | 1804.716 MB | 1804.770 MB | 12011.458 MB | 12012.684 MB | 0.000000 MB | 0.070312 MB |
| lsb_grid_worker | 2151 |  | 834 | 0.000% | 0.000% | 0.000 s | 3.406 MB | 3.406 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 9581 | sandbox_agent_lsb-native_0000_0000 | 812 | 7.209% | 96.341% | 58.890 s | 108.222 MB | 118.355 MB | 965.968 MB | 975.617 MB | n/a MB | n/a MB |
| python3 | 9587 | sandbox_agent_lsb-native_0000_0000 | 2 | 98.923% | 98.923% | 1.000 s | 56.705 MB | 84.086 MB | 67.521 MB | 98.148 MB | n/a MB | n/a MB |
| python | 9115 |  | 834 | 17.015% | 799.192% | 142.950 s | 2633.516 MB | 3442.391 MB | 16300.347 MB | 18200.383 MB | 0.148438 MB | 446.234375 MB |
| VLLM::EngineCor | 9175 |  | 834 | 4.501% | 52.477% | 37.810 s | 2325.768 MB | 2325.891 MB | 21828.756 MB | 21828.785 MB | 0.000000 MB | 0.003906 MB |
| docker-init | 9438 | sandbox_agent_lsb-native_0000_0000 | 812 | 0.002% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python | 9174 |  | 834 | 0.000% | 0.000% | 0.000 s | 12.180 MB | 12.180 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| tail | 9477 | sandbox_agent_lsb-native_0000_0000 | 812 | 0.002% | 0.995% | 0.020 s | 1.559 MB | 1.559 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 9599 | sandbox_agent_lsb-native_0000_0000 | 807 | 0.334% | 58.683% | 2.710 s | 75.531 MB | 81.848 MB | 88.309 MB | 95.254 MB | n/a MB | n/a MB |
| bash | 9692 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.898 MB | 2.898 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 9707 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.602 MB | 7.602 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 9693 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.989% | 1.985% | 0.040 s | 13.548 MB | 13.598 MB | 17.334 MB | 17.391 MB | n/a MB | n/a MB |
| python | 9721 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.129 MB | 12.129 MB | 15.910 MB | 15.910 MB | n/a MB | n/a MB |
| python | 9736 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.023 MB | 11.023 MB | 15.523 MB | 15.523 MB | n/a MB | n/a MB |
| python | 9751 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.855 MB | 7.855 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| python | 9766 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.465 MB | 4.465 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python | 9863 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.387 MB | 0.387 MB | n/a MB | n/a MB |
| python | 9848 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.496% | 0.992% | 0.010 s | 13.590 MB | 13.590 MB | 17.243 MB | 17.270 MB | n/a MB | n/a MB |
| python | 9877 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.258 MB | 12.258 MB | 16.047 MB | 16.047 MB | n/a MB | n/a MB |
| python | 9892 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.918 MB | 9.918 MB | 14.211 MB | 14.211 MB | n/a MB | n/a MB |
| python | 9957 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 93.879 MB | 93.879 MB | 458.668 MB | 458.668 MB | n/a MB | n/a MB |
| bash | 9956 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.910 MB | 2.910 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 9995 | sandbox_agent_lsb-native_0000_0000 | 2 | 177.954% | 177.954% | 1.790 s | 309.061 MB | 471.555 MB | 699.979 MB | 1072.219 MB | n/a MB | n/a MB |
| bash | 9994 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.824 MB | 2.824 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| grep | 10035 | sandbox_agent_lsb-native_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 1.867 MB | 1.867 MB | 3.777 MB | 3.777 MB | n/a MB | n/a MB |
| bash | 10032 | sandbox_agent_lsb-native_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 3.105 MB | 3.105 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10034 | sandbox_agent_lsb-native_0000_0000 | 10 | 0.772% | 1.988% | 0.070 s | 14.242 MB | 14.242 MB | 17.777 MB | 17.777 MB | n/a MB | n/a MB |
| python | 10042 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.656 MB | 10.656 MB | 14.195 MB | 14.195 MB | n/a MB | n/a MB |
| python | 10071 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.902 MB | 1.902 MB | 9.512 MB | 9.512 MB | n/a MB | n/a MB |
| python | 10085 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.750 MB | 9.750 MB | 14.191 MB | 14.191 MB | n/a MB | n/a MB |
| python | 10099 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.590 MB | 11.590 MB | 15.633 MB | 15.633 MB | n/a MB | n/a MB |
| python | 10114 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.809 MB | 8.809 MB | 13.414 MB | 13.414 MB | n/a MB | n/a MB |
| python | 10128 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.164 MB | 12.164 MB | 15.891 MB | 15.891 MB | n/a MB | n/a MB |
| python | 10142 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.656 MB | 13.656 MB | 17.160 MB | 17.160 MB | n/a MB | n/a MB |
| python | 10156 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.645 MB | 13.645 MB | 17.250 MB | 17.250 MB | n/a MB | n/a MB |
| python | 10171 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.016 MB | 10.016 MB | 14.195 MB | 14.195 MB | n/a MB | n/a MB |
| python | 10221 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.512 MB | 13.512 MB | 17.234 MB | 17.234 MB | n/a MB | n/a MB |
| bash | 10220 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.004 MB | 3.004 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10231 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.512 MB | 13.512 MB | 17.234 MB | 17.234 MB | n/a MB | n/a MB |
| python | 10239 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 85.402 MB | 85.402 MB | 437.078 MB | 437.078 MB | n/a MB | n/a MB |
| bash | 10252 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.840 MB | 2.840 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10253 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 514.211 MB | 514.211 MB | 1067.648 MB | 1067.648 MB | n/a MB | n/a MB |
| python | 10289 | sandbox_agent_lsb-native_0000_0000 | 2 | 197.516% | 197.516% | 1.990 s | 205.146 MB | 247.594 MB | 425.178 MB | 460.633 MB | n/a MB | n/a MB |
| bash | 10283 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 3.086 MB | 3.086 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 10313 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.812 MB | 2.812 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10314 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 250.574 MB | 250.574 MB | 465.184 MB | 465.184 MB | n/a MB | n/a MB |
| python | 10326 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 234.953 MB | 234.953 MB | 449.090 MB | 449.090 MB | n/a MB | n/a MB |
| bash | 10325 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.707 MB | 2.707 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| bash | 10336 | sandbox_agent_lsb-native_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.945 MB | 2.945 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10337 | sandbox_agent_lsb-native_0000_0000 | 2 | 145.128% | 145.128% | 1.460 s | 165.000 MB | 308.891 MB | 366.363 MB | 520.566 MB | n/a MB | n/a MB |
| python | 10370 | sandbox_agent_lsb-native_0000_0000 | 3 | 196.362% | 196.803% | 3.950 s | 186.819 MB | 241.055 MB | 400.507 MB | 454.488 MB | n/a MB | n/a MB |
| bash | 10369 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.062 MB | 3.062 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10376 | sandbox_agent_lsb-native_0000_0000 | 4 | 174.378% | 193.960% | 5.260 s | 523.461 MB | 750.832 MB | 742.277 MB | 963.941 MB | n/a MB | n/a MB |
| bash | 10375 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 3.086 MB | 3.086 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10386 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.985% | 1.961% | 0.030 s | 14.199 MB | 14.199 MB | 17.461 MB | 17.461 MB | n/a MB | n/a MB |
| python | 10387 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.098 MB | 11.098 MB | 15.633 MB | 15.633 MB | n/a MB | n/a MB |
| bash | 10385 | sandbox_agent_lsb-native_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.969 MB | 2.969 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10401 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.020 MB | 12.020 MB | 15.762 MB | 15.762 MB | n/a MB | n/a MB |
| python | 10416 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.980 MB | 7.980 MB | 12.922 MB | 12.922 MB | n/a MB | n/a MB |
| python | 10430 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.793 MB | 12.793 MB | 17.066 MB | 17.066 MB | n/a MB | n/a MB |
| python | 10442 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.129 MB | 22.129 MB | 213.613 MB | 213.613 MB | n/a MB | n/a MB |
| bash | 10441 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.129 MB | 3.129 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10455 | sandbox_agent_lsb-native_0000_0000 | 3 | 180.254% | 184.924% | 3.630 s | 240.210 MB | 371.520 MB | 445.368 MB | 582.805 MB | n/a MB | n/a MB |
| bash | 10454 | sandbox_agent_lsb-native_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 3.016 MB | 3.016 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10461 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 220.043 MB | 220.043 MB | 453.355 MB | 453.355 MB | n/a MB | n/a MB |
| bash | 10460 | sandbox_agent_lsb-native_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.910 MB | 2.910 MB | 4.215 MB | 4.215 MB | n/a MB | n/a MB |
| python | 10465 | sandbox_agent_lsb-native_0000_0000 | 5 | 0.746% | 1.989% | 0.030 s | 12.938 MB | 12.938 MB | 16.383 MB | 16.383 MB | n/a MB | n/a MB |
| python | 10468 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.863 MB | 7.863 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 10482 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.293 MB | 10.293 MB | 14.195 MB | 14.195 MB | n/a MB | n/a MB |
| python | 10496 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.121 MB | 12.121 MB | 15.762 MB | 15.762 MB | n/a MB | n/a MB |
| python | 10511 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.492 MB | 5.492 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| python | 10525 | sandbox_agent_lsb-native_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.926 MB | 10.926 MB | 14.344 MB | 14.344 MB | n/a MB | n/a MB |
| docker | 10575 |  | 2 | 0.000% | 0.000% | 0.000 s | 29.734 MB | 29.734 MB | 2060.031 MB | 2060.031 MB | 0.000000 MB | 0.000000 MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10.351% | 100.000% | 11871.237 MB | 12702.000 MB | 34.009 W | 73.971 W | 28522.415 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-native_0000_0000 | 14.894% | 201.462% | 121.652 s | 154.104 MB | 512.141 MB | 0.128906 MB | 1.054688 MB | 0.000788 MB | 0.000080 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 9307 | 840.049 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 818.058 | n/a | n/a | 0.129 | 818057.530 | 818057.530 | 818057.530 |
| engine:execute | 1/1 | 0 | 0 | 818.056 | 1.565 | 816.460 | 0.129 | 818055.715 | 818055.715 | 818055.715 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 812.274 | 0.004 | 812.270 | 0.073 | 812274.120 | 812274.120 | 812274.120 |
| turn | 30/30 | 0 | 0 | 808.616 | n/a | n/a | 0.021 | 26953.857 | 26908.275 | 44306.338 |
| llm:attempt | 30/30 | 0 | 0 | 625.342 | 3.652 | 621.689 | 0.020 | 20844.741 | 21721.142 | 35439.796 |
| tool:generate | 13/13 | 0 | 0 | 76.621 | n/a | n/a | 0.000 | 5893.952 | 5381.079 | 11964.690 |
| tool:bash | 22/22 | 0 | 0 | 53.987 | n/a | n/a | 0.000 | 2453.937 | 1949.962 | 6084.608 |
| process:bash | 22/22 | 2 | 0 | 53.757 | n/a | n/a | 0.000 | 2443.486 | 1941.520 | 6074.613 |
| tool:trace | 9/9 | 0 | 0 | 13.645 | n/a | n/a | 0.000 | 1516.097 | 1556.740 | 2029.216 |
| tool:token_stats | 2/2 | 0 | 0 | 12.898 | n/a | n/a | 0.000 | 6449.233 | 6449.233 | 10424.496 |
| tool:top_activations | 2/2 | 0 | 0 | 10.531 | n/a | n/a | 0.000 | 5265.590 | 5265.590 | 5285.286 |
| tool:logit_lens | 1/1 | 0 | 0 | 6.968 | n/a | n/a | 0.000 | 6967.795 | 6967.795 | 6967.795 |
| tool:inspect_module_inputs | 2/2 | 0 | 0 | 3.100 | n/a | n/a | 0.000 | 1550.184 | 1550.184 | 1823.531 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 3.056 | 0.690 | 2.366 | 0.052 | 3056.140 | 3056.140 | 3056.140 |
| runtime.harness_start | 1/1 | 0 | 0 | 3.056 | 0.690 | 2.366 | 0.052 | 3055.930 | 3055.930 | 3055.930 |
| syscall:sendto | 1291/1291 | 0 | 0 | 2.900 | n/a | n/a | 0.002 | 2.246 | 1.765 | 4.097 |
| run:container_call | 13/13 | 0 | 0 | 2.518 | 0.003 | 2.516 | 0.000 | 193.727 | 35.459 | 858.722 |
| teardown:commit | 1/1 | 0 | 0 | 2.119 | 0.005 | 2.114 | 0.000 | 2119.196 | 2119.196 | 2119.196 |
| sandbox:commit | 1/1 | 0 | 0 | 1.924 | 0.002 | 1.922 | 0.000 | 1924.462 | 1924.462 | 1924.462 |
| checkpoint.total | 1/1 | 0 | 0 | 1.924 | 0.002 | 1.922 | 0.000 | 1924.332 | 1924.332 | 1924.332 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 1.924 | 0.002 | 1.922 | 0.000 | 1924.198 | 1924.198 | 1924.198 |
| tool:patch | 3/3 | 0 | 0 | 1.229 | n/a | n/a | 0.000 | 409.623 | 406.955 | 419.499 |
| syscall:connect | 354/354 | 0 | 0 | 0.724 | n/a | n/a | 0.000 | 2.046 | 1.763 | 3.938 |
| syscall:execve | 477/477 | 0 | 0 | 0.588 | n/a | n/a | 0.000 | 1.232 | 1.165 | 1.597 |
| sandbox:create | 1/1 | 0 | 0 | 0.339 | 0.253 | 0.086 | 0.000 | 339.051 | 339.051 | 339.051 |
| sandbox:start | 1/1 | 0 | 0 | 0.335 | 0.003 | 0.333 | 0.000 | 335.476 | 335.476 | 335.476 |
| runtime.container_create | 1/1 | 0 | 0 | 0.335 | 0.002 | 0.333 | 0.000 | 335.339 | 335.339 | 335.339 |
| tool:commit_adapter | 1/1 | 0 | 0 | 0.305 | n/a | n/a | 0.000 | 304.730 | 304.730 | 304.730 |
| tool:submit_output | 1/1 | 0 | 0 | 0.211 | n/a | n/a | 0.000 | 211.439 | 211.439 | 211.439 |
| sandbox:stop | 1/1 | 0 | 0 | 0.194 | 0.002 | 0.192 | 0.000 | 194.460 | 194.460 | 194.460 |
| agency:services_close | 1/1 | 0 | 0 | 0.103 | 0.000 | 0.102 | 0.000 | 102.742 | 102.742 | 102.742 |
| agency:services_start | 1/1 | 0 | 0 | 0.072 | 0.041 | 0.031 | 0.000 | 72.403 | 72.403 | 72.403 |
| run:detect | 1/1 | 0 | 0 | 0.052 | 0.001 | 0.051 | 0.000 | 51.972 | 51.972 | 51.972 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.008 | 0.040 | 0.000 | 47.635 | 47.635 | 47.635 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.003 | 0.003 | 0.000 | 0.000 | 2.944 | 2.944 | 2.944 |
| tool:write | 6/6 | 0 | 0 | 0.002 | n/a | n/a | 0.000 | 0.397 | 0.390 | 0.441 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.415 | 1.415 | 1.415 |
| tool:edit | 2/2 | 0 | 0 | 0.001 | n/a | n/a | 0.000 | 0.509 | 0.509 | 0.525 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.075 | 0.077 | 0.109 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.236 | 0.236 | 0.236 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.074 | 0.074 | 0.074 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 833 | 0.441 | 0.028 | 153.398 | 0.058 | 3.693770 CPU seconds | n/a |
| GPU 0 memory | MB | 834 | 11871.237 | 11670.000 | 12702.000 | 11906.000 | n/a | n/a |
| GPU 0 power | W | 834 | 34.009 | 27.872 | 73.971 | 28.644 | n/a | 28522.415 J |
| GPU 0 proc / 9115-343153 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 memory | MB | 834 | 3192.998 | 3118.000 | 4018.000 | 3222.000 | n/a | n/a |
| GPU 0 proc / 9115-343153 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 estimated power | W | 491 | 4.401 | 0.000 | 67.583 | 0.000 | n/a | n/a |
| GPU 0 proc / 9115-343153 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 utilization | percent | 491 | 3.354 | 0.000 | 71.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 9175-344938 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 memory | MB | 834 | 8196.240 | 8070.000 | 8202.000 | 8202.000 | n/a | n/a |
| GPU 0 proc / 9175-344938 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 estimated power | W | 342 | 15.213 | 0.000 | 73.971 | 0.000 | n/a | n/a |
| GPU 0 proc / 9175-344938 / sandbox / ~ / device / GPU-06758974-3986-6756-f27a-f7c221e98846 utilization | percent | 342 | 20.649 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 834 | 11389.237 | 11188.000 | 12220.000 | 11424.000 | n/a | n/a |
| GPU 0 utilization | percent | 834 | 10.351 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 834 | 8.000 | 8.000 | 8.000 | 8.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 833 | 1.140 | 0.009 | 49.783 | 0.078 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 833 | 4.514 | 0.000 | 100.000 | 0.125 | n/a | n/a |
| host disk_read_mb_s | MB/s | 833 | 0.000 | 0.000 | 0.148 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 833 | 0.554 | 0.000 | 35.650 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 833 | 0.035 | 0.000 | 3.271 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 833 | 0.035 | 0.000 | 3.282 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 834 | 30878.172 | 30878.172 | 30878.172 | 30878.172 | n/a | n/a |
| host mem_used_mb | MB | 834 | 6943.874 | 6391.453 | 8240.945 | 7004.438 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 833 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 833 | 0.000 | 0.000 | 0.001 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 833 | 0.006 | 0.000 | 0.254 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 833 | 0.031 | 0.000 | 1.533 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10032) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10032) rss_mb | MB | 10 | 3.105 | 3.105 | 3.105 | 3.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10032) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10032) vms_mb | MB | 10 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10034) CPU | percent | 9 | 0.772 | 0.000 | 1.988 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10034) rss_mb | MB | 10 | 14.242 | 14.242 | 14.242 | 14.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10034) main thread run-queue wait | percent | 9 | 0.004 | 0.001 | 0.006 | 0.003 | 0.000329 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10034) vms_mb | MB | 10 | 17.777 | 17.777 | 17.777 | 17.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 10035) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 10035) rss_mb | MB | 10 | 1.867 | 1.867 | 1.867 | 1.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 10035) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — grep (PID 10035) vms_mb | MB | 10 | 3.777 | 3.777 | 3.777 | 3.777 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10042) rss_mb | MB | 1 | 10.656 | 10.656 | 10.656 | 10.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10042) vms_mb | MB | 1 | 14.195 | 14.195 | 14.195 | 14.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10071) rss_mb | MB | 1 | 1.902 | 1.902 | 1.902 | 1.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10071) vms_mb | MB | 1 | 9.512 | 9.512 | 9.512 | 9.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10085) rss_mb | MB | 1 | 9.750 | 9.750 | 9.750 | 9.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10085) vms_mb | MB | 1 | 14.191 | 14.191 | 14.191 | 14.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10099) rss_mb | MB | 1 | 11.590 | 11.590 | 11.590 | 11.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10099) vms_mb | MB | 1 | 15.633 | 15.633 | 15.633 | 15.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10114) rss_mb | MB | 1 | 8.809 | 8.809 | 8.809 | 8.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10114) vms_mb | MB | 1 | 13.414 | 13.414 | 13.414 | 13.414 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10128) rss_mb | MB | 1 | 12.164 | 12.164 | 12.164 | 12.164 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10128) vms_mb | MB | 1 | 15.891 | 15.891 | 15.891 | 15.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10142) rss_mb | MB | 1 | 13.656 | 13.656 | 13.656 | 13.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10142) vms_mb | MB | 1 | 17.160 | 17.160 | 17.160 | 17.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10156) rss_mb | MB | 1 | 13.645 | 13.645 | 13.645 | 13.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10156) vms_mb | MB | 1 | 17.250 | 17.250 | 17.250 | 17.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10171) rss_mb | MB | 1 | 10.016 | 10.016 | 10.016 | 10.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10171) vms_mb | MB | 1 | 14.195 | 14.195 | 14.195 | 14.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10220) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10220) rss_mb | MB | 2 | 3.004 | 3.004 | 3.004 | 3.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10220) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10220) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10221) rss_mb | MB | 1 | 13.512 | 13.512 | 13.512 | 13.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10221) vms_mb | MB | 1 | 17.234 | 17.234 | 17.234 | 17.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10231) rss_mb | MB | 1 | 13.512 | 13.512 | 13.512 | 13.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10231) vms_mb | MB | 1 | 17.234 | 17.234 | 17.234 | 17.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10239) rss_mb | MB | 1 | 85.402 | 85.402 | 85.402 | 85.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10239) vms_mb | MB | 1 | 437.078 | 437.078 | 437.078 | 437.078 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10252) rss_mb | MB | 1 | 2.840 | 2.840 | 2.840 | 2.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10252) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10253) rss_mb | MB | 1 | 514.211 | 514.211 | 514.211 | 514.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10253) vms_mb | MB | 1 | 1067.648 | 1067.648 | 1067.648 | 1067.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10283) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10283) rss_mb | MB | 2 | 3.086 | 3.086 | 3.086 | 3.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10283) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10283) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10289) CPU | percent | 1 | 197.516 | 197.516 | 197.516 | 197.516 | 1.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10289) rss_mb | MB | 2 | 205.146 | 162.699 | 247.594 | 247.594 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10289) main thread run-queue wait | percent | 1 | 51.660 | 51.660 | 51.660 | 51.660 | 0.520485 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10289) vms_mb | MB | 2 | 425.178 | 389.723 | 460.633 | 460.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10313) rss_mb | MB | 1 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10313) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10314) rss_mb | MB | 1 | 250.574 | 250.574 | 250.574 | 250.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10314) vms_mb | MB | 1 | 465.184 | 465.184 | 465.184 | 465.184 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10325) rss_mb | MB | 1 | 2.707 | 2.707 | 2.707 | 2.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10325) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10326) rss_mb | MB | 1 | 234.953 | 234.953 | 234.953 | 234.953 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10326) vms_mb | MB | 1 | 449.090 | 449.090 | 449.090 | 449.090 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10336) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10336) rss_mb | MB | 2 | 2.945 | 2.945 | 2.945 | 2.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10336) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10336) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10337) CPU | percent | 1 | 145.128 | 145.128 | 145.128 | 145.128 | 1.460000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10337) rss_mb | MB | 2 | 165.000 | 21.109 | 308.891 | 308.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10337) main thread run-queue wait | percent | 1 | 21.849 | 21.849 | 21.849 | 21.849 | 0.219799 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10337) vms_mb | MB | 2 | 366.363 | 212.160 | 520.566 | 520.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10369) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10369) rss_mb | MB | 3 | 3.062 | 3.062 | 3.062 | 3.062 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10369) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10369) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — style_edit.py (PID 10370) CPU | percent | 2 | 196.362 | 195.920 | 196.803 | 195.920 | 3.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — style_edit.py (PID 10370) rss_mb | MB | 3 | 186.819 | 120.809 | 241.055 | 241.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — style_edit.py (PID 10370) main thread run-queue wait | percent | 2 | 48.301 | 45.693 | 50.909 | 45.693 | 0.971638 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — style_edit.py (PID 10370) vms_mb | MB | 3 | 400.507 | 334.980 | 454.488 | 454.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10375) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10375) rss_mb | MB | 4 | 3.086 | 3.086 | 3.086 | 3.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10375) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10375) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10376) CPU | percent | 3 | 174.378 | 146.148 | 193.960 | 193.960 | 5.260000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10376) rss_mb | MB | 4 | 523.461 | 20.383 | 750.832 | 750.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10376) main thread run-queue wait | percent | 3 | 40.975 | 25.496 | 51.557 | 51.557 | 1.235947 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10376) vms_mb | MB | 4 | 742.277 | 211.840 | 963.941 | 963.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10385) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10385) rss_mb | MB | 4 | 2.969 | 2.969 | 2.969 | 2.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10385) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10385) vms_mb | MB | 4 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10386) CPU | percent | 3 | 0.985 | 0.000 | 1.961 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10386) rss_mb | MB | 4 | 14.199 | 14.199 | 14.199 | 14.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10386) main thread run-queue wait | percent | 3 | 0.004 | 0.001 | 0.009 | 0.002 | 0.000129 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10386) vms_mb | MB | 4 | 17.461 | 17.461 | 17.461 | 17.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10387) rss_mb | MB | 1 | 11.098 | 11.098 | 11.098 | 11.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10387) vms_mb | MB | 1 | 15.633 | 15.633 | 15.633 | 15.633 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10401) rss_mb | MB | 1 | 12.020 | 12.020 | 12.020 | 12.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10401) vms_mb | MB | 1 | 15.762 | 15.762 | 15.762 | 15.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10416) rss_mb | MB | 1 | 7.980 | 7.980 | 7.980 | 7.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10416) vms_mb | MB | 1 | 12.922 | 12.922 | 12.922 | 12.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10430) rss_mb | MB | 1 | 12.793 | 12.793 | 12.793 | 12.793 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10430) vms_mb | MB | 1 | 17.066 | 17.066 | 17.066 | 17.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10441) rss_mb | MB | 1 | 3.129 | 3.129 | 3.129 | 3.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10441) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10442) rss_mb | MB | 1 | 22.129 | 22.129 | 22.129 | 22.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10442) vms_mb | MB | 1 | 213.613 | 213.613 | 213.613 | 213.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10454) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10454) rss_mb | MB | 3 | 3.016 | 3.016 | 3.016 | 3.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10454) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10454) vms_mb | MB | 3 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 10455) CPU | percent | 2 | 180.254 | 175.584 | 184.924 | 184.924 | 3.630000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 10455) rss_mb | MB | 3 | 240.210 | 24.020 | 371.520 | 371.520 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 10455) main thread run-queue wait | percent | 2 | 37.940 | 37.028 | 38.852 | 37.028 | 0.764084 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — make_adapter.py (PID 10455) vms_mb | MB | 3 | 445.368 | 215.855 | 582.805 | 582.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10460) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10460) rss_mb | MB | 6 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10460) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 10460) vms_mb | MB | 6 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10461) rss_mb | MB | 1 | 220.043 | 220.043 | 220.043 | 220.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10461) vms_mb | MB | 1 | 453.355 | 453.355 | 453.355 | 453.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10465) CPU | percent | 4 | 0.746 | 0.000 | 1.989 | 0.994 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10465) rss_mb | MB | 5 | 12.938 | 12.938 | 12.938 | 12.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10465) main thread run-queue wait | percent | 4 | 0.003 | 0.000 | 0.006 | 0.000 | 0.000131 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 10465) vms_mb | MB | 5 | 16.383 | 16.383 | 16.383 | 16.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10468) rss_mb | MB | 1 | 7.863 | 7.863 | 7.863 | 7.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10468) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10482) rss_mb | MB | 1 | 10.293 | 10.293 | 10.293 | 10.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10482) vms_mb | MB | 1 | 14.195 | 14.195 | 14.195 | 14.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10496) rss_mb | MB | 1 | 12.121 | 12.121 | 12.121 | 12.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10496) vms_mb | MB | 1 | 15.762 | 15.762 | 15.762 | 15.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10511) rss_mb | MB | 1 | 5.492 | 5.492 | 5.492 | 5.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10511) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10525) rss_mb | MB | 1 | 10.926 | 10.926 | 10.926 | 10.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check_extra.py (PID 10525) vms_mb | MB | 1 | 14.344 | 14.344 | 14.344 | 14.344 | n/a | n/a |
| docker commit (PID 10575) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 10575) io read MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 10575) io write MB/s | MB/s | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 10575) rss_mb | MB | 2 | 29.734 | 29.734 | 29.734 | 29.734 | n/a | n/a |
| docker commit (PID 10575) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 10575) vms_mb | MB | 2 | 2060.031 | 2060.031 | 2060.031 | 2060.031 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2151) CPU | percent | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 2151) io read MB/s | MB/s | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2151) io write MB/s | MB/s | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 2151) rss_mb | MB | 834 | 3.406 | 3.406 | 3.406 | 3.406 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 2151) main thread run-queue wait | percent | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 2151) vms_mb | MB | 834 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9115) CPU | percent | 833 | 17.015 | 0.000 | 799.192 | 0.000 | 142.950000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 9115) io read MB/s | MB/s | 833 | 0.000 | 0.000 | 0.124 | 0.000 | 0.148438 MB | n/a |
| Agency harness — python -m lsbench (PID 9115) io write MB/s | MB/s | 833 | 0.531 | 0.015 | 72.805 | 0.023 | 446.234375 MB | n/a |
| Agency harness — python -m lsbench (PID 9115) rss_mb | MB | 834 | 2633.516 | 2051.469 | 3442.391 | 2899.738 | n/a | n/a |
| Agency harness — python -m lsbench (PID 9115) main thread run-queue wait | percent | 833 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000009 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 9115) vms_mb | MB | 834 | 16300.347 | 14148.891 | 18200.383 | 16578.250 | n/a | n/a |
| Python — vllm (PID 9124) CPU | percent | 833 | 0.456 | 0.000 | 7.934 | 0.000 | 3.830000 CPU seconds | n/a |
| Python — vllm (PID 9124) io read MB/s | MB/s | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — vllm (PID 9124) io write MB/s | MB/s | 833 | 0.000 | 0.000 | 0.008 | 0.000 | 0.070312 MB | n/a |
| Python — vllm (PID 9124) rss_mb | MB | 834 | 1804.716 | 1803.270 | 1804.770 | 1804.770 | n/a | n/a |
| Python — vllm (PID 9124) main thread run-queue wait | percent | 833 | 0.001 | 0.000 | 0.113 | 0.001 | 0.006655 run-queue seconds | n/a |
| Python — vllm (PID 9124) vms_mb | MB | 834 | 12011.458 | 11939.664 | 12012.684 | 12012.684 | n/a | n/a |
| Python — python -c (PID 9174) CPU | percent | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 9174) io read MB/s | MB/s | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9174) io write MB/s | MB/s | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 9174) rss_mb | MB | 834 | 12.180 | 12.180 | 12.180 | 12.180 | n/a | n/a |
| Python — python -c (PID 9174) main thread run-queue wait | percent | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 9174) vms_mb | MB | 834 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 9175) CPU | percent | 833 | 4.501 | 0.000 | 52.477 | 0.000 | 37.810000 CPU seconds | n/a |
| VLLM::EngineCore (PID 9175) io read MB/s | MB/s | 833 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 9175) io write MB/s | MB/s | 833 | 0.000 | 0.000 | 0.004 | 0.000 | 0.003906 MB | n/a |
| VLLM::EngineCore (PID 9175) rss_mb | MB | 834 | 2325.768 | 2325.266 | 2325.891 | 2325.891 | n/a | n/a |
| VLLM::EngineCore (PID 9175) main thread run-queue wait | percent | 833 | 0.000 | 0.000 | 0.040 | 0.000 | 0.003782 run-queue seconds | n/a |
| VLLM::EngineCore (PID 9175) vms_mb | MB | 834 | 21828.756 | 21828.637 | 21828.785 | 21828.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 9438) CPU | percent | 811 | 0.002 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 9438) rss_mb | MB | 812 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 9438) main thread run-queue wait | percent | 811 | 0.003 | 0.000 | 2.054 | 0.000 | 0.021743 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — docker-init (PID 9438) vms_mb | MB | 812 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 9477) CPU | percent | 811 | 0.002 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 9477) rss_mb | MB | 812 | 1.559 | 1.559 | 1.559 | 1.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 9477) main thread run-queue wait | percent | 811 | 0.000 | 0.000 | 0.076 | 0.000 | 0.000914 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — tail (PID 9477) vms_mb | MB | 812 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9581) CPU | percent | 811 | 7.209 | 0.000 | 96.341 | 0.000 | 58.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9581) rss_mb | MB | 812 | 108.222 | 3.070 | 118.355 | 112.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9581) main thread run-queue wait | percent | 811 | 0.000 | 0.000 | 0.012 | 0.000 | 0.000160 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9581) vms_mb | MB | 812 | 965.968 | 4.258 | 975.617 | 975.570 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 9587) CPU | percent | 1 | 98.923 | 98.923 | 98.923 | 98.923 | 1.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 9587) rss_mb | MB | 2 | 56.705 | 29.324 | 84.086 | 84.086 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 9587) main thread run-queue wait | percent | 1 | 0.008 | 0.008 | 0.008 | 0.008 | 0.000084 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -c (PID 9587) vms_mb | MB | 2 | 67.521 | 36.895 | 98.148 | 98.148 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9599) CPU | percent | 806 | 0.334 | 0.000 | 58.683 | 5.968 | 2.710000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9599) rss_mb | MB | 807 | 75.531 | 31.332 | 81.848 | 77.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9599) main thread run-queue wait | percent | 806 | 0.008 | 0.000 | 4.135 | 0.002 | 0.067518 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python -m native_harness.cli (PID 9599) vms_mb | MB | 807 | 88.309 | 36.262 | 95.254 | 91.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9692) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9692) rss_mb | MB | 5 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9692) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9692) vms_mb | MB | 5 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9693) CPU | percent | 4 | 0.989 | 0.000 | 1.985 | 0.979 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9693) rss_mb | MB | 5 | 13.548 | 13.473 | 13.598 | 13.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9693) main thread run-queue wait | percent | 4 | 0.004 | 0.002 | 0.006 | 0.004 | 0.000151 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9693) vms_mb | MB | 5 | 17.334 | 17.320 | 17.391 | 17.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9707) rss_mb | MB | 1 | 7.602 | 7.602 | 7.602 | 7.602 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9707) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9721) rss_mb | MB | 1 | 12.129 | 12.129 | 12.129 | 12.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9721) vms_mb | MB | 1 | 15.910 | 15.910 | 15.910 | 15.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9736) rss_mb | MB | 1 | 11.023 | 11.023 | 11.023 | 11.023 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9736) vms_mb | MB | 1 | 15.523 | 15.523 | 15.523 | 15.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9751) rss_mb | MB | 1 | 7.855 | 7.855 | 7.855 | 7.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9751) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9766) rss_mb | MB | 1 | 4.465 | 4.465 | 4.465 | 4.465 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9766) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9848) CPU | percent | 2 | 0.496 | 0.000 | 0.992 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9848) rss_mb | MB | 3 | 13.590 | 13.590 | 13.590 | 13.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9848) main thread run-queue wait | percent | 2 | 0.003 | 0.003 | 0.004 | 0.003 | 0.000069 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9848) vms_mb | MB | 3 | 17.243 | 17.191 | 17.270 | 17.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9863) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9863) vms_mb | MB | 1 | 0.387 | 0.387 | 0.387 | 0.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9877) rss_mb | MB | 1 | 12.258 | 12.258 | 12.258 | 12.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9877) vms_mb | MB | 1 | 16.047 | 16.047 | 16.047 | 16.047 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9892) rss_mb | MB | 1 | 9.918 | 9.918 | 9.918 | 9.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — check.py (PID 9892) vms_mb | MB | 1 | 14.211 | 14.211 | 14.211 | 14.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9956) rss_mb | MB | 1 | 2.910 | 2.910 | 2.910 | 2.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9956) vms_mb | MB | 1 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — study.py (PID 9957) rss_mb | MB | 1 | 93.879 | 93.879 | 93.879 | 93.879 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — study.py (PID 9957) vms_mb | MB | 1 | 458.668 | 458.668 | 458.668 | 458.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9994) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9994) rss_mb | MB | 2 | 2.824 | 2.824 | 2.824 | 2.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9994) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — bash (PID 9994) vms_mb | MB | 2 | 4.215 | 4.215 | 4.215 | 4.215 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 9995) CPU | percent | 1 | 177.954 | 177.954 | 177.954 | 177.954 | 1.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 9995) rss_mb | MB | 2 | 309.061 | 146.566 | 471.555 | 471.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 9995) main thread run-queue wait | percent | 1 | 36.132 | 36.132 | 36.132 | 36.132 | 0.363444 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-native_0000_0000 — python stdin (PID 9995) vms_mb | MB | 2 | 699.979 | 327.738 | 1072.219 | 1072.219 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 CPU | percent | 811 | 14.894 | 0.000 | 201.462 | 0.000 | 121.651754 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 811 | 1.276 | 0.000 | 50.001 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 811 | 1.280 | 0.000 | 50.001 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_full_pct | percent of wall time stalled | 811 | 0.000 | 0.000 | 0.070 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io_psi_some_pct | percent of wall time stalled | 811 | 0.000 | 0.000 | 0.070 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io read MB/s | MB/s | 811 | 0.000 | 0.000 | 0.105 | 0.000 | 0.128906 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 io write MB/s | MB/s | 811 | 0.001 | 0.000 | 0.711 | 0.000 | 1.054688 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory | MB | 812 | 154.104 | 20.191 | 512.141 | 97.902 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_full_pct | percent of wall time stalled | 811 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 memory_psi_some_pct | percent of wall time stalled | 811 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net rx MB/s | MB/s | 811 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000788 MB | n/a |
| sandbox sandbox_agent_lsb-native_0000_0000 net tx MB/s | MB/s | 811 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000080 MB | n/a |
| workload total CPU | percent | 833 | 21.992 | 1.541 | 799.360 | 1.670 | 184.763080 CPU seconds | n/a |
| workload total memory | MB | 834 | 11682.587 | 11071.996 | 12457.504 | 12034.199 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
