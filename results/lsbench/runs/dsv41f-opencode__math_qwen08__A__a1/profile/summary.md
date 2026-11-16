# agprof summary

- Duration: **1350.164 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.001 runs/s**
- LLM: **114 calls**, 103 succeeded, 11 failed, 0 interrupted, n/a reported retries, 680.985 s total wait
- Tools: **102/102 completed**, 0 failed, 0 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **127889** at 1.966 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 1323990.664 / 1323990.664 ms |
| LLM latency p50 / p95 | 4706.728 / 14932.916 ms |
| LLM TTFT p50 / p95 | 2458.524 / 8469.177 ms |
| LLM input / output tokens | n/a / n/a |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 114 total, 103 succeeded, 11 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {}
- opencode: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| bash | 97/97 | 97 | 0 | 0 | n/a | n/a |
| read | 1/1 | 1 | 0 | 0 | n/a | n/a |
| write | 4/4 | 4 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 21.688% | 177.026% | 292.969 s | 8923.690 MB | 10590.383 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| python | 3715 |  | 1340 | 10.327% | 177.073% | 139.280 s | 3033.698 MB | 4677.227 MB | 16205.809 MB | 20975.715 MB | 169.269531 MB | 277.003906 MB |
| vllm | 3795 |  | 1340 | 0.954% | 4.968% | 12.900 s | 1781.987 MB | 1782.914 MB | 11032.752 MB | 11038.250 MB | 0.007812 MB | 0.078125 MB |
| docker-buildx | 4012 |  | 1 | n/a% | n/a% | n/a s | 42.277 MB | 42.277 MB | 1362.547 MB | 1362.547 MB | n/a MB | n/a MB |
| docker | 4002 |  | 1 | n/a% | n/a% | n/a s | 29.164 MB | 29.164 MB | 1843.512 MB | 1843.512 MB | n/a MB | n/a MB |
| python | 3829 |  | 1340 | 0.000% | 0.000% | 0.000 s | 12.230 MB | 12.230 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| VLLM::EngineCor | 3830 |  | 1340 | 10.384% | 43.588% | 140.390 s | 2327.147 MB | 2328.324 MB | 21240.039 MB | 21241.285 MB | 0.000000 MB | 0.007812 MB |
| lsb_grid_worker | 3417 |  | 1340 | 0.000% | 0.000% | 0.000 s | 3.320 MB | 3.320 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| tail | 4145 | sandbox_agent_lsb-opencode_0000_0000 | 1312 | 0.002% | 0.995% | 0.030 s | 1.293 MB | 1.293 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| bash | 4240 | sandbox_agent_lsb-opencode_0000_0000 | 1312 | 35.920% | 99.483% | 474.430 s | 109.428 MB | 130.707 MB | 897.793 MB | 904.496 MB | n/a MB | n/a MB |
| python3 | 4246 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 63.296% | 67.939% | 1.280 s | 49.288 MB | 81.840 MB | 59.645 MB | 97.996 MB | n/a MB | n/a MB |
| docker-init | 4111 | sandbox_agent_lsb-opencode_0000_0000 | 1312 | 0.002% | 0.995% | 0.020 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| opencode | 4254 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 42.133 MB | 42.133 MB | 6431.145 MB | 6431.145 MB | n/a MB | n/a MB |
| opencode | 4267 | sandbox_agent_lsb-opencode_0000_0000 | 1286 | 5.358% | 123.242% | 69.320 s | 743.824 MB | 890.242 MB | 16618.940 MB | 16819.039 MB | n/a MB | n/a MB |
| bash | 4363 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.801 MB | 2.801 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| find | 4367 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 17.884% | 17.884% | 0.180 s | 2.188 MB | 2.188 MB | 4.412 MB | 4.445 MB | n/a MB | n/a MB |
| grep | 4368 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.445 MB | 1.445 MB | 3.262 MB | 3.262 MB | n/a MB | n/a MB |
| head | 4369 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 1.238 MB | 1.238 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| bash | 4375 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.617 MB | 2.617 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| curl | 4379 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.727 MB | 9.727 MB | 19.133 MB | 19.133 MB | n/a MB | n/a MB |
| head | 4380 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.129 MB | 1.129 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 4438 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.035 MB | 7.035 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| curl | 4448 | sandbox_agent_lsb-opencode_0000_0000 | 84 | 0.000% | 0.000% | 0.000 s | 9.785 MB | 9.785 MB | 19.504 MB | 19.504 MB | n/a MB | n/a MB |
| python3 | 4445 | sandbox_agent_lsb-opencode_0000_0000 | 84 | 0.000% | 0.000% | 0.000 s | 11.598 MB | 11.598 MB | 15.121 MB | 15.121 MB | n/a MB | n/a MB |
| python3 | 4513 | sandbox_agent_lsb-opencode_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 11.387 MB | 11.387 MB | 14.934 MB | 14.934 MB | n/a MB | n/a MB |
| curl | 4516 | sandbox_agent_lsb-opencode_0000_0000 | 17 | 0.000% | 0.000% | 0.000 s | 9.980 MB | 9.980 MB | 19.504 MB | 19.504 MB | n/a MB | n/a MB |
| python3 | 4542 | sandbox_agent_lsb-opencode_0000_0000 | 22 | 0.000% | 0.000% | 0.000 s | 11.664 MB | 11.664 MB | 15.043 MB | 15.043 MB | n/a MB | n/a MB |
| curl | 4545 | sandbox_agent_lsb-opencode_0000_0000 | 22 | 0.000% | 0.000% | 0.000 s | 10.102 MB | 10.102 MB | 19.508 MB | 19.508 MB | n/a MB | n/a MB |
| python3 | 4585 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 51.441 MB | 51.441 MB | 55.551 MB | 55.551 MB | n/a MB | n/a MB |
| python3 | 4592 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.664 MB | 4.664 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python3 | 4597 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 11.039 MB | 11.039 MB | 14.906 MB | 14.906 MB | n/a MB | n/a MB |
| curl | 4600 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 9.977 MB | 9.977 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 4609 | sandbox_agent_lsb-opencode_0000_0000 | 209 | 0.009% | 1.970% | 0.020 s | 11.359 MB | 11.371 MB | 14.933 MB | 14.941 MB | n/a MB | n/a MB |
| curl | 4612 | sandbox_agent_lsb-opencode_0000_0000 | 208 | 0.005% | 0.990% | 0.010 s | 9.855 MB | 9.855 MB | 19.504 MB | 19.504 MB | n/a MB | n/a MB |
| curl | 4682 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 9.969 MB | 9.969 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 4679 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 10.863 MB | 10.863 MB | 14.898 MB | 14.898 MB | n/a MB | n/a MB |
| python3 | 4733 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.020 MB | 11.020 MB | 14.910 MB | 14.910 MB | n/a MB | n/a MB |
| curl | 4736 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.000 MB | 10.000 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 4740 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.504 MB | 18.504 MB | 211.473 MB | 211.473 MB | n/a MB | n/a MB |
| python3 | 4755 | sandbox_agent_lsb-opencode_0000_0000 | 32 | 0.000% | 0.000% | 0.000 s | 11.797 MB | 11.797 MB | 15.039 MB | 15.039 MB | n/a MB | n/a MB |
| curl | 4759 | sandbox_agent_lsb-opencode_0000_0000 | 32 | 0.000% | 0.000% | 0.000 s | 9.770 MB | 9.770 MB | 19.512 MB | 19.512 MB | n/a MB | n/a MB |
| curl | 4790 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.039 MB | 10.039 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 4787 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.957 MB | 10.957 MB | 14.895 MB | 14.895 MB | n/a MB | n/a MB |
| python3 | 4794 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.301 MB | 21.301 MB | 213.523 MB | 213.523 MB | n/a MB | n/a MB |
| python3 | 4805 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 61.020 MB | 61.020 MB | 76.000 MB | 76.000 MB | n/a MB | n/a MB |
| python3 | 4814 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.824 MB | 6.824 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| curl | 4835 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.711 MB | 9.711 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 4831 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.188 MB | 11.188 MB | 14.961 MB | 14.961 MB | n/a MB | n/a MB |
| python3 | 4844 | sandbox_agent_lsb-opencode_0000_0000 | 43 | 0.000% | 0.000% | 0.000 s | 11.723 MB | 11.723 MB | 15.281 MB | 15.281 MB | n/a MB | n/a MB |
| curl | 4847 | sandbox_agent_lsb-opencode_0000_0000 | 43 | 0.000% | 0.000% | 0.000 s | 10.098 MB | 10.098 MB | 19.516 MB | 19.516 MB | n/a MB | n/a MB |
| bash | 4874 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.695 MB | 2.695 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 4876 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.301 MB | 1.301 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 4875 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.383 MB | 18.383 MB | 1876.789 MB | 1876.789 MB | n/a MB | n/a MB |
| python3 | 4920 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 13.746 MB | 13.746 MB | 208.590 MB | 208.590 MB | n/a MB | n/a MB |
| python3 | 4931 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 10.895 MB | 10.895 MB | 14.941 MB | 14.941 MB | n/a MB | n/a MB |
| curl | 4935 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 9.715 MB | 9.715 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 4940 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.805 MB | 10.805 MB | 14.934 MB | 14.934 MB | n/a MB | n/a MB |
| curl | 4943 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.004 MB | 10.004 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| curl | 4950 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.020 MB | 10.020 MB | 19.512 MB | 19.512 MB | n/a MB | n/a MB |
| python3 | 4947 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.770 MB | 10.770 MB | 14.898 MB | 14.898 MB | n/a MB | n/a MB |
| python3 | 4954 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.109 MB | 8.109 MB | 13.031 MB | 13.031 MB | n/a MB | n/a MB |
| python3 | 4961 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.965 MB | 10.965 MB | 14.930 MB | 14.930 MB | n/a MB | n/a MB |
| curl | 4964 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.055 MB | 10.055 MB | 19.391 MB | 19.391 MB | n/a MB | n/a MB |
| python3 | 4970 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 10.766 MB | 10.766 MB | 14.918 MB | 14.918 MB | n/a MB | n/a MB |
| curl | 4975 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.945 MB | 9.945 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| curl | 4976 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.898 MB | 9.898 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 4987 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 23.160 MB | 23.160 MB | 215.617 MB | 215.617 MB | n/a MB | n/a MB |
| python3 | 4998 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 648.977 MB | 648.977 MB | 1680.699 MB | 1680.699 MB | n/a MB | n/a MB |
| python3 | 5006 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.719 MB | 22.719 MB | 215.473 MB | 215.473 MB | n/a MB | n/a MB |
| python3 | 5044 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 61.234 MB | 61.234 MB | 269.105 MB | 269.105 MB | n/a MB | n/a MB |
| python3 | 5059 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 109.199% | 109.199% | 1.100 s | 604.932 MB | 1083.590 MB | 1003.811 MB | 1306.668 MB | n/a MB | n/a MB |
| python3 | 5074 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.473 MB | 21.473 MB | 213.762 MB | 213.762 MB | n/a MB | n/a MB |
| python3 | 5092 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 992.848 MB | 992.848 MB | 1672.598 MB | 1672.598 MB | n/a MB | n/a MB |
| curl | 5109 | sandbox_agent_lsb-opencode_0000_0000 | 45 | 0.000% | 0.000% | 0.000 s | 10.094 MB | 10.094 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 5105 | sandbox_agent_lsb-opencode_0000_0000 | 45 | 0.000% | 0.000% | 0.000 s | 10.750 MB | 10.750 MB | 14.898 MB | 14.898 MB | n/a MB | n/a MB |
| curl | 5149 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 9.707 MB | 9.707 MB | 19.500 MB | 19.500 MB | n/a MB | n/a MB |
| python3 | 5146 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 10.996 MB | 10.996 MB | 14.934 MB | 14.934 MB | n/a MB | n/a MB |
| python3 | 5155 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1399.789 MB | 1399.789 MB | 2155.867 MB | 2155.867 MB | n/a MB | n/a MB |
| python3 | 5163 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 101.721% | 106.233% | 3.070 s | 815.513 MB | 1105.922 MB | 1030.604 MB | 1328.762 MB | n/a MB | n/a MB |
| python3 | 5188 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1359.477 MB | 1359.477 MB | 1670.875 MB | 1670.875 MB | n/a MB | n/a MB |
| python3 | 5215 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 89.519% | 89.519% | 0.900 s | 530.926 MB | 1044.535 MB | 722.992 MB | 1236.238 MB | n/a MB | n/a MB |
| python3 | 5228 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 98.287% | 98.287% | 0.990 s | 514.359 MB | 1021.285 MB | 620.996 MB | 1230.203 MB | n/a MB | n/a MB |
| python3 | 5899 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 91.481% | 91.481% | 0.920 s | 536.039 MB | 1058.957 MB | 728.865 MB | 1250.566 MB | n/a MB | n/a MB |
| bash | 5908 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.805 MB | 2.805 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| head | 5911 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.129 MB | 1.129 MB | 2.449 MB | 2.449 MB | n/a MB | n/a MB |
| python3 | 5910 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1479.344 MB | 1479.344 MB | 1670.875 MB | 1670.875 MB | n/a MB | n/a MB |
| python3 | 5925 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 115.367% | 115.367% | 1.160 s | 760.930 MB | 1091.797 MB | 1008.713 MB | 1314.680 MB | n/a MB | n/a MB |
| docker | 6016 |  | 21 | 0.000% | 0.000% | 0.000 s | 30.230 MB | 30.230 MB | 1843.512 MB | 1843.512 MB | 0.000000 MB | 0.000000 MB |
| docker | 6067 |  | 1 | n/a% | n/a% | n/a s | 30.812 MB | 30.812 MB | 1771.516 MB | 1771.516 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 31.944% | 100.000% | 12043.615 MB | 15072.000 MB | 42.312 W | 73.403 W | 57139.218 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-opencode_0000_0000 | 43.712% | 190.627% | 577.273 s | 1178.429 MB | 2743.484 MB | 184.187500 MB | 265.757812 MB | 24.511883 MB | 0.515311 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 4000 | 1350.099 | interrupted |
| harness:retire | -1 | 0.295 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 1323.991 | n/a | n/a | 184.188 | 1323990.664 | 1323990.664 | 1323990.664 |
| engine:execute | 1/1 | 0 | 0 | 1323.989 | 2.313 | 1321.675 | 184.188 | 1323989.240 | 1323989.240 | 1323989.240 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1296.492 | 0.005 | 1296.487 | 128.706 | 1296491.867 | 1296491.867 | 1296491.867 |
| harness:await_cli | 1/1 | 0 | 0 | 1276.969 | n/a | n/a | 38.892 | 1276968.827 | 1276968.827 | 1276968.827 |
| llm:attempt | 114/114 | 11 | 0 | 680.985 | 12.378 | 668.603 | 19.206 | 5973.552 | 4706.728 | 14932.916 |
| tool:bash | 97/97 | 0 | 0 | 529.254 | n/a | n/a | 17.560 | 5456.224 | 374.912 | 24420.757 |
| run:container_call | 13/13 | 0 | 0 | 22.315 | 0.002 | 22.312 | 0.190 | 1716.523 | 37.403 | 8791.156 |
| teardown:commit | 1/1 | 0 | 0 | 21.707 | 0.004 | 21.703 | 0.191 | 21707.494 | 21707.494 | 21707.494 |
| sandbox:commit | 1/1 | 0 | 0 | 21.480 | 0.002 | 21.478 | 0.191 | 21479.890 | 21479.890 | 21479.890 |
| checkpoint.total | 1/1 | 0 | 0 | 21.480 | 0.002 | 21.478 | 0.191 | 21479.763 | 21479.763 | 21479.763 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 21.480 | 0.002 | 21.478 | 0.191 | 21479.626 | 21479.626 | 21479.626 |
| harness:startup_ready | 1/1 | 0 | 0 | 17.059 | n/a | n/a | 55.807 | 17059.352 | 17059.352 | 17059.352 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.445 | 1.050 | 3.395 | 53.894 | 4445.248 | 4445.248 | 4445.248 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.445 | 1.050 | 3.395 | 53.889 | 4445.013 | 4445.013 | 4445.013 |
| syscall:connect | 569/569 | 0 | 0 | 1.208 | n/a | n/a | 0.594 | 2.123 | 1.722 | 4.378 |
| syscall:sendto | 554/554 | 0 | 0 | 1.100 | n/a | n/a | 0.327 | 1.986 | 1.620 | 3.952 |
| sandbox:create | 1/1 | 0 | 0 | 1.043 | 0.242 | 0.801 | 0.000 | 1042.699 | 1042.699 | 1042.699 |
| harness:submit | 1/1 | 0 | 0 | 1.009 | n/a | n/a | 5.924 | 1008.619 | 1008.619 | 1008.619 |
| run:detect | 1/1 | 0 | 0 | 0.748 | 0.001 | 0.748 | 0.000 | 748.421 | 748.421 | 748.421 |
| syscall:execve | 405/405 | 0 | 0 | 0.680 | n/a | n/a | 0.523 | 1.678 | 1.278 | 2.834 |
| sandbox:start | 1/1 | 0 | 0 | 0.540 | 0.002 | 0.538 | 0.000 | 540.417 | 540.417 | 540.417 |
| runtime.container_create | 1/1 | 0 | 0 | 0.540 | 0.002 | 0.538 | 0.000 | 540.276 | 540.276 | 540.276 |
| sandbox:stop | 1/1 | 0 | 0 | 0.227 | 0.001 | 0.226 | 0.000 | 227.234 | 227.234 | 227.234 |
| agency:services_close | 1/1 | 0 | 0 | 0.132 | 0.001 | 0.130 | 0.056 | 131.659 | 131.659 | 131.659 |
| tool:write | 4/4 | 0 | 0 | 0.128 | n/a | n/a | 0.014 | 31.971 | 32.352 | 42.109 |
| agency:services_start | 1/1 | 0 | 0 | 0.092 | 0.043 | 0.049 | 0.000 | 91.923 | 91.923 | 91.923 |
| agent:create | 1/1 | 0 | 0 | 0.049 | 0.008 | 0.041 | 0.000 | 49.339 | 49.339 | 49.339 |
| harness:launch | 1/1 | 0 | 0 | 0.048 | n/a | n/a | 0.840 | 47.558 | 47.558 | 47.558 |
| harness:snapshot | 1/1 | 0 | 0 | 0.047 | n/a | n/a | 0.020 | 47.049 | 47.049 | 47.049 |
| tool:read | 1/1 | 0 | 0 | 0.044 | n/a | n/a | 0.000 | 44.244 | 44.244 | 44.244 |
| syscall:bind | 7/7 | 0 | 0 | 0.018 | n/a | n/a | 0.074 | 2.559 | 1.920 | 5.228 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.007 | 0.007 | 0.000 | 0.003 | 7.382 | 7.382 | 7.382 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.221 | 1.221 | 1.221 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.067 | 0.064 | 0.089 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.167 | 0.167 | 0.167 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.058 | 0.058 | 0.058 |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 1338 | 0.656 | 0.027 | 72.995 | 0.033 | 8.828741 CPU seconds | n/a |
| GPU 0 memory | MB | 1340 | 12043.615 | 11670.000 | 15072.000 | 11972.000 | n/a | n/a |
| GPU 0 power | W | 1340 | 42.312 | 27.540 | 73.403 | 27.606 | n/a | 57139.218 J |
| GPU 0 proc / 3715-377580 / sandbox / ~ / device / GPU-d9df2440-f9d1-0a3a-94a1-ed4bddbf35bf memory | MB | 1340 | 3306.930 | 3118.000 | 6306.000 | 3206.000 | n/a | n/a |
| GPU 0 proc / 3715-377580 / sandbox / ~ / device / GPU-d9df2440-f9d1-0a3a-94a1-ed4bddbf35bf estimated power | W | 789 | 3.726 | 0.000 | 71.602 | 0.000 | n/a | n/a |
| GPU 0 proc / 3715-377580 / sandbox / ~ / device / GPU-d9df2440-f9d1-0a3a-94a1-ed4bddbf35bf utilization | percent | 789 | 2.582 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 3830-381066 / sandbox / ~ / device / GPU-d9df2440-f9d1-0a3a-94a1-ed4bddbf35bf memory | MB | 1340 | 8254.685 | 8070.000 | 8284.000 | 8284.000 | n/a | n/a |
| GPU 0 proc / 3830-381066 / sandbox / ~ / device / GPU-d9df2440-f9d1-0a3a-94a1-ed4bddbf35bf estimated power | W | 524 | 53.363 | 0.000 | 72.200 | 0.000 | n/a | n/a |
| GPU 0 proc / 3830-381066 / sandbox / ~ / device / GPU-d9df2440-f9d1-0a3a-94a1-ed4bddbf35bf utilization | percent | 524 | 73.878 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 1340 | 11561.615 | 11188.000 | 14590.000 | 11490.000 | n/a | n/a |
| GPU 0 utilization | percent | 1340 | 31.944 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 1340 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 1339 | 0.957 | 0.084 | 19.424 | 0.223 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 1339 | 16.305 | 0.000 | 64.912 | 0.000 | n/a | n/a |
| host disk_read_mb_s | MB/s | 1339 | 1.601 | 0.000 | 215.813 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 1339 | 0.732 | 0.000 | 117.781 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 1339 | 1.541 | 0.000 | 72.729 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 1339 | 1.607 | 0.000 | 74.370 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 1340 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 1340 | 7732.257 | 6754.984 | 9515.355 | 7230.961 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 1339 | 0.001 | 0.000 | 0.329 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 1339 | 0.001 | 0.000 | 0.336 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 1339 | 0.046 | 0.000 | 13.218 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 1339 | 0.019 | 0.000 | 0.369 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3417) CPU | percent | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 3417) io read MB/s | MB/s | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3417) io write MB/s | MB/s | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 3417) rss_mb | MB | 1340 | 3.320 | 3.320 | 3.320 | 3.320 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 3417) main thread run-queue wait | percent | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 3417) vms_mb | MB | 1340 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3715) CPU | percent | 1339 | 10.327 | 0.000 | 177.073 | 0.000 | 139.280000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 3715) io read MB/s | MB/s | 1339 | 0.125 | 0.000 | 93.245 | 0.000 | 169.269531 MB | n/a |
| Agency harness — python -m lsbench (PID 3715) io write MB/s | MB/s | 1339 | 0.205 | 0.015 | 31.917 | 0.039 | 277.003906 MB | n/a |
| Agency harness — python -m lsbench (PID 3715) rss_mb | MB | 1340 | 3033.698 | 2494.793 | 4677.227 | 3247.887 | n/a | n/a |
| Agency harness — python -m lsbench (PID 3715) main thread run-queue wait | percent | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 3715) vms_mb | MB | 1340 | 16205.809 | 14030.879 | 20975.715 | 16408.738 | n/a | n/a |
| Python — vllm (PID 3795) CPU | percent | 1339 | 0.954 | 0.000 | 4.968 | 0.000 | 12.900000 CPU seconds | n/a |
| Python — vllm (PID 3795) io read MB/s | MB/s | 1339 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 3795) io write MB/s | MB/s | 1339 | 0.000 | 0.000 | 0.008 | 0.000 | 0.078125 MB | n/a |
| Python — vllm (PID 3795) rss_mb | MB | 1340 | 1781.987 | 1778.367 | 1782.914 | 1782.914 | n/a | n/a |
| Python — vllm (PID 3795) main thread run-queue wait | percent | 1339 | 0.014 | 0.000 | 0.736 | 0.001 | 0.183691 run-queue seconds | n/a |
| Python — vllm (PID 3795) vms_mb | MB | 1340 | 11032.752 | 10963.230 | 11038.250 | 11038.250 | n/a | n/a |
| Python — python -c (PID 3829) CPU | percent | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 3829) io read MB/s | MB/s | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3829) io write MB/s | MB/s | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 3829) rss_mb | MB | 1340 | 12.230 | 12.230 | 12.230 | 12.230 | n/a | n/a |
| Python — python -c (PID 3829) main thread run-queue wait | percent | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 3829) vms_mb | MB | 1340 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 3830) CPU | percent | 1339 | 10.384 | 0.000 | 43.588 | 0.996 | 140.390000 CPU seconds | n/a |
| VLLM::EngineCore (PID 3830) io read MB/s | MB/s | 1339 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 3830) io write MB/s | MB/s | 1339 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| VLLM::EngineCore (PID 3830) rss_mb | MB | 1340 | 2327.147 | 2323.449 | 2328.324 | 2328.324 | n/a | n/a |
| VLLM::EngineCore (PID 3830) main thread run-queue wait | percent | 1339 | 0.009 | 0.000 | 0.453 | 0.000 | 0.125172 run-queue seconds | n/a |
| VLLM::EngineCore (PID 3830) vms_mb | MB | 1340 | 21240.039 | 21236.227 | 21241.285 | 21241.285 | n/a | n/a |
| docker info (PID 4002) rss_mb | MB | 1 | 29.164 | 29.164 | 29.164 | 29.164 | n/a | n/a |
| docker info (PID 4002) vms_mb | MB | 1 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| docker-buildx (PID 4012) rss_mb | MB | 1 | 42.277 | 42.277 | 42.277 | 42.277 | n/a | n/a |
| docker-buildx (PID 4012) vms_mb | MB | 1 | 1362.547 | 1362.547 | 1362.547 | 1362.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 4111) CPU | percent | 1311 | 0.002 | 0.000 | 0.995 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 4111) rss_mb | MB | 1312 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 4111) main thread run-queue wait | percent | 1311 | 0.004 | 0.000 | 4.685 | 0.000 | 0.050398 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 4111) vms_mb | MB | 1312 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 4145) CPU | percent | 1311 | 0.002 | 0.000 | 0.995 | 0.000 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 4145) rss_mb | MB | 1312 | 1.293 | 1.293 | 1.293 | 1.293 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 4145) main thread run-queue wait | percent | 1311 | 0.001 | 0.000 | 1.084 | 0.000 | 0.017158 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 4145) vms_mb | MB | 1312 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4240) CPU | percent | 1311 | 35.920 | 0.000 | 99.483 | 0.000 | 474.430000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4240) rss_mb | MB | 1312 | 109.428 | 2.910 | 130.707 | 130.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4240) main thread run-queue wait | percent | 1311 | 0.000 | 0.000 | 0.004 | 0.000 | 0.000083 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4240) vms_mb | MB | 1312 | 897.793 | 4.262 | 904.496 | 904.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4246) CPU | percent | 2 | 63.296 | 58.652 | 67.939 | 67.939 | 1.280000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4246) rss_mb | MB | 3 | 49.288 | 16.488 | 81.840 | 81.840 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4246) main thread run-queue wait | percent | 2 | 0.022 | 0.018 | 0.026 | 0.018 | 0.000448 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4246) vms_mb | MB | 3 | 59.645 | 22.539 | 97.996 | 97.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 4254) rss_mb | MB | 1 | 42.133 | 42.133 | 42.133 | 42.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 4254) vms_mb | MB | 1 | 6431.145 | 6431.145 | 6431.145 | 6431.145 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 4267) CPU | percent | 1285 | 5.358 | 0.942 | 123.242 | 12.933 | 69.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 4267) rss_mb | MB | 1286 | 743.824 | 54.816 | 890.242 | 788.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 4267) main thread run-queue wait | percent | 1285 | 0.379 | 0.001 | 15.809 | 0.015 | 4.900637 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 4267) vms_mb | MB | 1286 | 16618.940 | 6431.648 | 16819.039 | 16819.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4363) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4363) rss_mb | MB | 2 | 2.801 | 2.801 | 2.801 | 2.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4363) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4363) vms_mb | MB | 2 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — find (PID 4367) CPU | percent | 1 | 17.884 | 17.884 | 17.884 | 17.884 | 0.180000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — find (PID 4367) rss_mb | MB | 2 | 2.188 | 2.188 | 2.188 | 2.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — find (PID 4367) main thread run-queue wait | percent | 1 | 0.066 | 0.066 | 0.066 | 0.066 | 0.000659 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — find (PID 4367) vms_mb | MB | 2 | 4.412 | 4.379 | 4.445 | 4.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 4368) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 4368) rss_mb | MB | 2 | 1.445 | 1.445 | 1.445 | 1.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 4368) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — grep (PID 4368) vms_mb | MB | 2 | 3.262 | 3.262 | 3.262 | 3.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 4369) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 4369) rss_mb | MB | 2 | 1.238 | 1.238 | 1.238 | 1.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 4369) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 4369) vms_mb | MB | 2 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4375) rss_mb | MB | 1 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4375) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4379) rss_mb | MB | 1 | 9.727 | 9.727 | 9.727 | 9.727 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4379) vms_mb | MB | 1 | 19.133 | 19.133 | 19.133 | 19.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 4380) rss_mb | MB | 1 | 1.129 | 1.129 | 1.129 | 1.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 4380) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — mcp.py (PID 4438) rss_mb | MB | 1 | 7.035 | 7.035 | 7.035 | 7.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — mcp.py (PID 4438) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4445) CPU | percent | 83 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4445) rss_mb | MB | 84 | 11.598 | 11.598 | 11.598 | 11.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4445) main thread run-queue wait | percent | 83 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4445) vms_mb | MB | 84 | 15.121 | 15.121 | 15.121 | 15.121 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4448) CPU | percent | 83 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4448) rss_mb | MB | 84 | 9.785 | 9.785 | 9.785 | 9.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4448) main thread run-queue wait | percent | 83 | 0.002 | 0.000 | 0.116 | 0.000 | 0.001357 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4448) vms_mb | MB | 84 | 19.504 | 19.504 | 19.504 | 19.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4513) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4513) rss_mb | MB | 17 | 11.387 | 11.387 | 11.387 | 11.387 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4513) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4513) vms_mb | MB | 17 | 14.934 | 14.934 | 14.934 | 14.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4516) CPU | percent | 16 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4516) rss_mb | MB | 17 | 9.980 | 9.980 | 9.980 | 9.980 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4516) main thread run-queue wait | percent | 16 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000041 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4516) vms_mb | MB | 17 | 19.504 | 19.504 | 19.504 | 19.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4542) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4542) rss_mb | MB | 22 | 11.664 | 11.664 | 11.664 | 11.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4542) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4542) vms_mb | MB | 22 | 15.043 | 15.043 | 15.043 | 15.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4545) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4545) rss_mb | MB | 22 | 10.102 | 10.102 | 10.102 | 10.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4545) main thread run-queue wait | percent | 21 | 0.002 | 0.000 | 0.035 | 0.000 | 0.000382 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4545) vms_mb | MB | 22 | 19.508 | 19.508 | 19.508 | 19.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4585) rss_mb | MB | 1 | 51.441 | 51.441 | 51.441 | 51.441 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4585) vms_mb | MB | 1 | 55.551 | 55.551 | 55.551 | 55.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4592) rss_mb | MB | 1 | 4.664 | 4.664 | 4.664 | 4.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4592) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4597) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4597) rss_mb | MB | 5 | 11.039 | 11.039 | 11.039 | 11.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4597) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4597) vms_mb | MB | 5 | 14.906 | 14.906 | 14.906 | 14.906 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4600) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4600) rss_mb | MB | 5 | 9.977 | 9.977 | 9.977 | 9.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4600) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000015 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4600) vms_mb | MB | 5 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4609) CPU | percent | 208 | 0.009 | 0.000 | 1.970 | 0.000 | 0.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4609) rss_mb | MB | 209 | 11.359 | 8.910 | 11.371 | 11.371 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4609) main thread run-queue wait | percent | 208 | 0.000 | 0.000 | 0.007 | 0.000 | 0.000071 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4609) vms_mb | MB | 209 | 14.933 | 13.199 | 14.941 | 14.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4612) CPU | percent | 207 | 0.005 | 0.000 | 0.990 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4612) rss_mb | MB | 208 | 9.855 | 9.855 | 9.855 | 9.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4612) main thread run-queue wait | percent | 207 | 0.002 | 0.000 | 0.209 | 0.000 | 0.003515 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4612) vms_mb | MB | 208 | 19.504 | 19.504 | 19.504 | 19.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4679) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4679) rss_mb | MB | 9 | 10.863 | 10.863 | 10.863 | 10.863 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4679) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4679) vms_mb | MB | 9 | 14.898 | 14.898 | 14.898 | 14.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4682) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4682) rss_mb | MB | 9 | 9.969 | 9.969 | 9.969 | 9.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4682) main thread run-queue wait | percent | 8 | 0.006 | 0.000 | 0.039 | 0.000 | 0.000446 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4682) vms_mb | MB | 9 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4733) rss_mb | MB | 1 | 11.020 | 11.020 | 11.020 | 11.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4733) vms_mb | MB | 1 | 14.910 | 14.910 | 14.910 | 14.910 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4736) rss_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4736) vms_mb | MB | 1 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4740) rss_mb | MB | 1 | 18.504 | 18.504 | 18.504 | 18.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4740) vms_mb | MB | 1 | 211.473 | 211.473 | 211.473 | 211.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4755) CPU | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4755) rss_mb | MB | 32 | 11.797 | 11.797 | 11.797 | 11.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4755) main thread run-queue wait | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4755) vms_mb | MB | 32 | 15.039 | 15.039 | 15.039 | 15.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4759) CPU | percent | 31 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4759) rss_mb | MB | 32 | 9.770 | 9.770 | 9.770 | 9.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4759) main thread run-queue wait | percent | 31 | 0.001 | 0.000 | 0.031 | 0.000 | 0.000371 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4759) vms_mb | MB | 32 | 19.512 | 19.512 | 19.512 | 19.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4787) rss_mb | MB | 1 | 10.957 | 10.957 | 10.957 | 10.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4787) vms_mb | MB | 1 | 14.895 | 14.895 | 14.895 | 14.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4790) rss_mb | MB | 1 | 10.039 | 10.039 | 10.039 | 10.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4790) vms_mb | MB | 1 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4794) rss_mb | MB | 1 | 21.301 | 21.301 | 21.301 | 21.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4794) vms_mb | MB | 1 | 213.523 | 213.523 | 213.523 | 213.523 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — attr.py (PID 4805) rss_mb | MB | 1 | 61.020 | 61.020 | 61.020 | 61.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — attr.py (PID 4805) vms_mb | MB | 1 | 76.000 | 76.000 | 76.000 | 76.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — attr.py (PID 4814) rss_mb | MB | 1 | 6.824 | 6.824 | 6.824 | 6.824 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — attr.py (PID 4814) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — attr.py (PID 4831) rss_mb | MB | 1 | 11.188 | 11.188 | 11.188 | 11.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — attr.py (PID 4831) vms_mb | MB | 1 | 14.961 | 14.961 | 14.961 | 14.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4835) rss_mb | MB | 1 | 9.711 | 9.711 | 9.711 | 9.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4835) vms_mb | MB | 1 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4844) CPU | percent | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4844) rss_mb | MB | 43 | 11.723 | 11.723 | 11.723 | 11.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4844) main thread run-queue wait | percent | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4844) vms_mb | MB | 43 | 15.281 | 15.281 | 15.281 | 15.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4847) CPU | percent | 42 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4847) rss_mb | MB | 43 | 10.098 | 10.098 | 10.098 | 10.098 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4847) main thread run-queue wait | percent | 42 | 0.000 | 0.000 | 0.002 | 0.000 | 0.000095 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4847) vms_mb | MB | 43 | 19.516 | 19.516 | 19.516 | 19.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4874) rss_mb | MB | 1 | 2.695 | 2.695 | 2.695 | 2.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4874) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4875) rss_mb | MB | 1 | 18.383 | 18.383 | 18.383 | 18.383 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4875) vms_mb | MB | 1 | 1876.789 | 1876.789 | 1876.789 | 1876.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 4876) rss_mb | MB | 1 | 1.301 | 1.301 | 1.301 | 1.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 4876) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4920) rss_mb | MB | 1 | 13.746 | 13.746 | 13.746 | 13.746 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4920) vms_mb | MB | 1 | 208.590 | 208.590 | 208.590 | 208.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4931) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4931) rss_mb | MB | 5 | 10.895 | 10.895 | 10.895 | 10.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4931) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4931) vms_mb | MB | 5 | 14.941 | 14.941 | 14.941 | 14.941 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4935) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4935) rss_mb | MB | 5 | 9.715 | 9.715 | 9.715 | 9.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4935) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000004 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4935) vms_mb | MB | 5 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4940) rss_mb | MB | 1 | 10.805 | 10.805 | 10.805 | 10.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4940) vms_mb | MB | 1 | 14.934 | 14.934 | 14.934 | 14.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4943) rss_mb | MB | 1 | 10.004 | 10.004 | 10.004 | 10.004 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4943) vms_mb | MB | 1 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4947) rss_mb | MB | 1 | 10.770 | 10.770 | 10.770 | 10.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4947) vms_mb | MB | 1 | 14.898 | 14.898 | 14.898 | 14.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4950) rss_mb | MB | 1 | 10.020 | 10.020 | 10.020 | 10.020 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4950) vms_mb | MB | 1 | 19.512 | 19.512 | 19.512 | 19.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4954) rss_mb | MB | 1 | 8.109 | 8.109 | 8.109 | 8.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4954) vms_mb | MB | 1 | 13.031 | 13.031 | 13.031 | 13.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4961) rss_mb | MB | 1 | 10.965 | 10.965 | 10.965 | 10.965 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4961) vms_mb | MB | 1 | 14.930 | 14.930 | 14.930 | 14.930 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4964) rss_mb | MB | 1 | 10.055 | 10.055 | 10.055 | 10.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4964) vms_mb | MB | 1 | 19.391 | 19.391 | 19.391 | 19.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4970) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4970) rss_mb | MB | 2 | 10.766 | 10.766 | 10.766 | 10.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4970) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4970) vms_mb | MB | 2 | 14.918 | 14.918 | 14.918 | 14.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4975) rss_mb | MB | 1 | 9.945 | 9.945 | 9.945 | 9.945 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4975) vms_mb | MB | 1 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4976) rss_mb | MB | 1 | 9.898 | 9.898 | 9.898 | 9.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 4976) vms_mb | MB | 1 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4987) rss_mb | MB | 1 | 23.160 | 23.160 | 23.160 | 23.160 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4987) vms_mb | MB | 1 | 215.617 | 215.617 | 215.617 | 215.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4998) rss_mb | MB | 1 | 648.977 | 648.977 | 648.977 | 648.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 4998) vms_mb | MB | 1 | 1680.699 | 1680.699 | 1680.699 | 1680.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5006) rss_mb | MB | 1 | 22.719 | 22.719 | 22.719 | 22.719 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5006) vms_mb | MB | 1 | 215.473 | 215.473 | 215.473 | 215.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5044) rss_mb | MB | 1 | 61.234 | 61.234 | 61.234 | 61.234 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5044) vms_mb | MB | 1 | 269.105 | 269.105 | 269.105 | 269.105 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5059) CPU | percent | 1 | 109.199 | 109.199 | 109.199 | 109.199 | 1.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5059) rss_mb | MB | 2 | 604.932 | 126.273 | 1083.590 | 1083.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5059) main thread run-queue wait | percent | 1 | 9.204 | 9.204 | 9.204 | 9.204 | 0.092720 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5059) vms_mb | MB | 2 | 1003.811 | 700.953 | 1306.668 | 1306.668 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5074) rss_mb | MB | 1 | 21.473 | 21.473 | 21.473 | 21.473 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5074) vms_mb | MB | 1 | 213.762 | 213.762 | 213.762 | 213.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5092) rss_mb | MB | 1 | 992.848 | 992.848 | 992.848 | 992.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5092) vms_mb | MB | 1 | 1672.598 | 1672.598 | 1672.598 | 1672.598 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5105) CPU | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5105) rss_mb | MB | 45 | 10.750 | 10.750 | 10.750 | 10.750 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5105) main thread run-queue wait | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5105) vms_mb | MB | 45 | 14.898 | 14.898 | 14.898 | 14.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 5109) CPU | percent | 44 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 5109) rss_mb | MB | 45 | 10.094 | 10.094 | 10.094 | 10.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 5109) main thread run-queue wait | percent | 44 | 0.024 | 0.000 | 0.252 | 0.000 | 0.010529 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 5109) vms_mb | MB | 45 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5146) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5146) rss_mb | MB | 6 | 10.996 | 10.996 | 10.996 | 10.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5146) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5146) vms_mb | MB | 6 | 14.934 | 14.934 | 14.934 | 14.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 5149) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 5149) rss_mb | MB | 6 | 9.707 | 9.707 | 9.707 | 9.707 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 5149) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000010 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — curl (PID 5149) vms_mb | MB | 6 | 19.500 | 19.500 | 19.500 | 19.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5155) rss_mb | MB | 1 | 1399.789 | 1399.789 | 1399.789 | 1399.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5155) vms_mb | MB | 1 | 2155.867 | 2155.867 | 2155.867 | 2155.867 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5163) CPU | percent | 3 | 101.721 | 99.453 | 106.233 | 99.453 | 3.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5163) rss_mb | MB | 4 | 815.513 | 18.254 | 1105.922 | 1104.309 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5163) main thread run-queue wait | percent | 3 | 2.718 | 0.002 | 8.149 | 0.003 | 0.082131 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5163) vms_mb | MB | 4 | 1030.604 | 210.035 | 1328.762 | 1326.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 5188) rss_mb | MB | 1 | 1359.477 | 1359.477 | 1359.477 | 1359.477 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 5188) vms_mb | MB | 1 | 1670.875 | 1670.875 | 1670.875 | 1670.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5215) CPU | percent | 1 | 89.519 | 89.519 | 89.519 | 89.519 | 0.900000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5215) rss_mb | MB | 2 | 530.926 | 17.316 | 1044.535 | 1044.535 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5215) main thread run-queue wait | percent | 1 | 2.307 | 2.307 | 2.307 | 2.307 | 0.023193 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5215) vms_mb | MB | 2 | 722.992 | 209.746 | 1236.238 | 1236.238 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5228) CPU | percent | 1 | 98.287 | 98.287 | 98.287 | 98.287 | 0.990000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5228) rss_mb | MB | 2 | 514.359 | 7.434 | 1021.285 | 1021.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5228) main thread run-queue wait | percent | 1 | 3.768 | 3.768 | 3.768 | 3.768 | 0.037955 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5228) vms_mb | MB | 2 | 620.996 | 11.789 | 1230.203 | 1230.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5899) CPU | percent | 1 | 91.481 | 91.481 | 91.481 | 91.481 | 0.920000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5899) rss_mb | MB | 2 | 536.039 | 13.121 | 1058.957 | 1058.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5899) main thread run-queue wait | percent | 1 | 5.197 | 5.197 | 5.197 | 5.197 | 0.052268 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5899) vms_mb | MB | 2 | 728.865 | 207.164 | 1250.566 | 1250.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5908) rss_mb | MB | 1 | 2.805 | 2.805 | 2.805 | 2.805 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5908) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 5910) rss_mb | MB | 1 | 1479.344 | 1479.344 | 1479.344 | 1479.344 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — build_adapter.py (PID 5910) vms_mb | MB | 1 | 1670.875 | 1670.875 | 1670.875 | 1670.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 5911) rss_mb | MB | 1 | 1.129 | 1.129 | 1.129 | 1.129 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — head (PID 5911) vms_mb | MB | 1 | 2.449 | 2.449 | 2.449 | 2.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5925) CPU | percent | 1 | 115.367 | 115.367 | 115.367 | 115.367 | 1.160000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5925) rss_mb | MB | 2 | 760.930 | 430.062 | 1091.797 | 1091.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5925) main thread run-queue wait | percent | 1 | 15.953 | 15.953 | 15.953 | 15.953 | 0.160410 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 5925) vms_mb | MB | 2 | 1008.713 | 702.746 | 1314.680 | 1314.680 | n/a | n/a |
| docker commit (PID 6016) CPU | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 6016) io read MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6016) io write MB/s | MB/s | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 6016) rss_mb | MB | 21 | 30.230 | 30.230 | 30.230 | 30.230 | n/a | n/a |
| docker commit (PID 6016) main thread run-queue wait | percent | 20 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 6016) vms_mb | MB | 21 | 1843.512 | 1843.512 | 1843.512 | 1843.512 | n/a | n/a |
| docker stop (PID 6067) rss_mb | MB | 1 | 30.812 | 30.812 | 30.812 | 30.812 | n/a | n/a |
| docker stop (PID 6067) vms_mb | MB | 1 | 1771.516 | 1771.516 | 1771.516 | 1771.516 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 CPU | percent | 1311 | 43.712 | 0.000 | 190.627 | 0.000 | 577.273277 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 1311 | 0.551 | 0.000 | 12.507 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 1311 | 0.700 | 0.000 | 18.913 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_full_pct | percent of wall time stalled | 1311 | 0.085 | 0.000 | 24.988 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_some_pct | percent of wall time stalled | 1311 | 0.086 | 0.000 | 25.155 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io read MB/s | MB/s | 1311 | 0.140 | 0.000 | 37.732 | 0.000 | 184.187500 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io write MB/s | MB/s | 1311 | 0.202 | 0.000 | 68.801 | 0.000 | 265.757812 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory | MB | 1312 | 1178.429 | 28.410 | 2743.484 | 376.137 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_full_pct | percent of wall time stalled | 1311 | 0.000 | 0.000 | 0.042 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_some_pct | percent of wall time stalled | 1311 | 0.000 | 0.000 | 0.042 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net rx MB/s | MB/s | 1311 | 0.019 | 0.000 | 12.863 | 0.000 | 24.511883 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net tx MB/s | MB/s | 1311 | 0.000 | 0.000 | 0.093 | 0.000 | 0.515311 MB | n/a |
| workload total CPU | percent | 1339 | 21.688 | 1.396 | 177.026 | 2.029 | 292.969049 CPU seconds | n/a |
| workload total memory | MB | 1340 | 8923.690 | 8342.211 | 10590.383 | 9189.312 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
