# agprof summary

- Duration: **15510.976 s**
- Runs: **0/1 completed**, 0 succeeded, 0 failed, 1 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **122 calls**, 122 succeeded, 0 failed, 0 interrupted, n/a reported retries, 13209.284 s total wait
- Tools: **143/144 completed**, 0 failed, 1 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **1539735** at 1.972 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | n/a / n/a ms |
| LLM latency p50 / p95 | 59755.444 / 323050.307 ms |
| LLM TTFT p50 / p95 | 44739.256 / 305594.701 ms |
| LLM input / output tokens | 11119072 / 145131 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 122 total, 122 succeeded, 0 failed, 0 interrupted |
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
| bash | 100/101 | 100 | 0 | 1 | n/a | n/a |
| edit | 2/2 | 2 | 0 | 0 | n/a | n/a |
| read | 30/30 | 30 | 0 | 0 | n/a | n/a |
| todowrite | 8/8 | 8 | 0 | 0 | n/a | n/a |
| write | 3/3 | 3 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 11.200% | 181.400% | 1742.752 s | 9153.835 MB | 11195.289 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lsb_grid_worker | 1733 |  | 15420 | 0.000% | 0.000% | 0.000 s | 3.340 MB | 3.340 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| python | 2009 |  | 15420 | 0.027% | 3.981% | 4.220 s | 44.887 MB | 45.168 MB | 131.222 MB | 131.715 MB | 0.000000 MB | 0.410156 MB |
| VLLM::EngineCor | 1789 |  | 15420 | 3.268% | 42.531% | 508.380 s | 2330.152 MB | 2331.770 MB | 21241.534 MB | 21243.039 MB | 0.000000 MB | 0.101562 MB |
| python | 1742 |  | 15420 | 7.634% | 179.748% | 1188.030 s | 3122.349 MB | 5077.445 MB | 16061.450 MB | 20841.672 MB | 165.113281 MB | 832.226562 MB |
| python | 1788 |  | 15420 | 0.000% | 0.000% | 0.000 s | 12.199 MB | 12.199 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| docker | 2017 |  | 1 | n/a% | n/a% | n/a s | 30.551 MB | 30.551 MB | 1843.270 MB | 1843.270 MB | n/a MB | n/a MB |
| vllm | 1754 |  | 15420 | 0.269% | 7.909% | 41.920 s | 1791.134 MB | 1792.484 MB | 11046.462 MB | 11060.492 MB | 0.007812 MB | 0.179688 MB |
| docker-init | 2124 | sandbox_agent_lsb-opencode_0000_0000 | 15419 | 0.002% | 0.996% | 0.320 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| bash | 2248 | sandbox_agent_lsb-opencode_0000_0000 | 15419 | 31.242% | 99.287% | 4845.850 s | 111.653 MB | 116.738 MB | 902.110 MB | 903.637 MB | n/a MB | n/a MB |
| tail | 2158 | sandbox_agent_lsb-opencode_0000_0000 | 15419 | 0.002% | 0.996% | 0.380 s | 1.301 MB | 1.301 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| python3 | 2254 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 55.159% | 59.690% | 1.110 s | 49.257 MB | 78.820 MB | 59.523 MB | 94.422 MB | n/a MB | n/a MB |
| opencode | 2262 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.582 MB | 17.582 MB | 6358.133 MB | 6358.133 MB | n/a MB | n/a MB |
| opencode | 2276 | sandbox_agent_lsb-opencode_0000_0000 | 15414 | 2.837% | 126.017% | 439.930 s | 712.780 MB | 982.660 MB | 16631.659 MB | 16731.152 MB | n/a MB | n/a MB |
| python3 | 2775 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 6.340 MB | 6.340 MB | 11.656 MB | 11.656 MB | n/a MB | n/a MB |
| python3 | 3042 | sandbox_agent_lsb-opencode_0000_0000 | 521 | 0.002% | 0.989% | 0.010 s | 21.699 MB | 21.699 MB | 27.918 MB | 27.918 MB | n/a MB | n/a MB |
| python3 | 3262 | sandbox_agent_lsb-opencode_0000_0000 | 493 | 0.000% | 0.000% | 0.000 s | 21.582 MB | 21.582 MB | 26.695 MB | 26.695 MB | n/a MB | n/a MB |
| python3 | 3483 | sandbox_agent_lsb-opencode_0000_0000 | 83 | 0.000% | 0.000% | 0.000 s | 21.297 MB | 21.297 MB | 26.621 MB | 26.621 MB | n/a MB | n/a MB |
| bash | 3482 | sandbox_agent_lsb-opencode_0000_0000 | 83 | 0.000% | 0.000% | 0.000 s | 2.898 MB | 2.898 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 3650 | sandbox_agent_lsb-opencode_0000_0000 | 300 | 0.000% | 0.000% | 0.000 s | 20.938 MB | 20.938 MB | 26.652 MB | 26.652 MB | n/a MB | n/a MB |
| bash | 3649 | sandbox_agent_lsb-opencode_0000_0000 | 300 | 0.000% | 0.000% | 0.000 s | 2.891 MB | 2.891 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 3993 | sandbox_agent_lsb-opencode_0000_0000 | 40 | 0.000% | 0.000% | 0.000 s | 2.586 MB | 2.586 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 3994 | sandbox_agent_lsb-opencode_0000_0000 | 40 | 0.000% | 0.000% | 0.000 s | 21.348 MB | 21.348 MB | 26.785 MB | 26.785 MB | n/a MB | n/a MB |
| bash | 4079 | sandbox_agent_lsb-opencode_0000_0000 | 109 | 0.000% | 0.000% | 0.000 s | 2.734 MB | 2.734 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4080 | sandbox_agent_lsb-opencode_0000_0000 | 109 | 0.000% | 0.000% | 0.000 s | 20.816 MB | 20.816 MB | 26.660 MB | 26.660 MB | n/a MB | n/a MB |
| python3 | 4216 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 1.391% | 6.955% | 0.070 s | 18.872 MB | 20.887 MB | 24.424 MB | 26.672 MB | n/a MB | n/a MB |
| bash | 4215 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.816 MB | 2.816 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4231 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 1.986% | 9.932% | 0.100 s | 18.780 MB | 21.125 MB | 24.148 MB | 26.621 MB | n/a MB | n/a MB |
| bash | 4230 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.891 MB | 2.891 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4282 | sandbox_agent_lsb-opencode_0000_0000 | 19 | 0.000% | 0.000% | 0.000 s | 36.621 MB | 36.621 MB | 43.297 MB | 43.297 MB | n/a MB | n/a MB |
| bash | 4281 | sandbox_agent_lsb-opencode_0000_0000 | 19 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 4400 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.898 MB | 2.898 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4401 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 34.195 MB | 34.195 MB | 228.551 MB | 228.551 MB | n/a MB | n/a MB |
| python3 | 4437 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.809 MB | 17.809 MB | 209.895 MB | 209.895 MB | n/a MB | n/a MB |
| bash | 4436 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.758 MB | 2.758 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 4452 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.895 MB | 2.895 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4453 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.457 MB | 20.457 MB | 212.258 MB | 212.258 MB | n/a MB | n/a MB |
| python3 | 4469 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.445 MB | 9.445 MB | 13.410 MB | 13.410 MB | n/a MB | n/a MB |
| bash | 4468 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.812 MB | 2.812 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4619 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 45.914 MB | 45.914 MB | 52.055 MB | 52.055 MB | n/a MB | n/a MB |
| bash | 4618 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.695 MB | 2.695 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4652 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 38.281 MB | 38.281 MB | 44.730 MB | 44.730 MB | n/a MB | n/a MB |
| bash | 4651 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.688 MB | 2.688 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| bash | 4748 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 0.000% | 0.000% | 0.000 s | 3.059 MB | 3.059 MB | 3.996 MB | 3.996 MB | n/a MB | n/a MB |
| python3 | 4749 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 0.000% | 0.000% | 0.000 s | 24.457 MB | 24.457 MB | 29.723 MB | 29.723 MB | n/a MB | n/a MB |
| bash | 4795 | sandbox_agent_lsb-opencode_0000_0000 | 41 | 0.000% | 0.000% | 0.000 s | 2.977 MB | 2.977 MB | 3.988 MB | 3.988 MB | n/a MB | n/a MB |
| python3 | 4796 | sandbox_agent_lsb-opencode_0000_0000 | 41 | 0.617% | 24.686% | 0.250 s | 38.014 MB | 38.801 MB | 231.480 MB | 232.199 MB | n/a MB | n/a MB |
| python3 | 4831 | sandbox_agent_lsb-opencode_0000_0000 | 8 | 170.008% | 174.037% | 11.970 s | 1364.587 MB | 1557.660 MB | 2605.047 MB | 2948.875 MB | n/a MB | n/a MB |
| bash | 4830 | sandbox_agent_lsb-opencode_0000_0000 | 9 | 0.000% | 0.000% | 0.000 s | 2.859 MB | 2.859 MB | 3.855 MB | 3.855 MB | n/a MB | n/a MB |
| bash | 4867 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.625 MB | 2.625 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 4868 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 174.706% | 179.083% | 8.790 s | 65.616 MB | 66.074 MB | 288.917 MB | 290.242 MB | n/a MB | n/a MB |
| python3 | 4888 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 1.738% | 5.964% | 0.070 s | 21.226 MB | 22.785 MB | 26.716 MB | 28.348 MB | n/a MB | n/a MB |
| bash | 4887 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.758 MB | 2.758 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 4901 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 2.586 MB | 2.586 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 4902 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 22.898 MB | 22.898 MB | 28.156 MB | 28.156 MB | n/a MB | n/a MB |
| bash | 4920 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.664 MB | 2.664 MB | 3.855 MB | 3.855 MB | n/a MB | n/a MB |
| python3 | 4921 | sandbox_agent_lsb-opencode_0000_0000 | 2 | 37.555% | 37.555% | 0.380 s | 821.857 MB | 1607.207 MB | 1607.771 MB | 2985.109 MB | n/a MB | n/a MB |
| python3 | 4957 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 1566.230 MB | 1566.230 MB | 2938.070 MB | 2938.070 MB | n/a MB | n/a MB |
| bash | 4956 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.648 MB | 2.648 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 4984 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.000 MB | 0.000 MB | n/a MB | n/a MB |
| python3 | 5136 | sandbox_agent_lsb-opencode_0000_0000 | 51 | 0.000% | 0.000% | 0.000 s | 21.672 MB | 21.672 MB | 26.809 MB | 26.809 MB | n/a MB | n/a MB |
| bash | 5135 | sandbox_agent_lsb-opencode_0000_0000 | 51 | 0.000% | 0.000% | 0.000 s | 2.609 MB | 2.609 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5222 | sandbox_agent_lsb-opencode_0000_0000 | 18 | 0.000% | 0.000% | 0.000 s | 22.374 MB | 22.438 MB | 27.656 MB | 27.762 MB | n/a MB | n/a MB |
| bash | 5221 | sandbox_agent_lsb-opencode_0000_0000 | 18 | 0.000% | 0.000% | 0.000 s | 2.785 MB | 2.785 MB | 3.988 MB | 3.988 MB | n/a MB | n/a MB |
| bash | 5239 | sandbox_agent_lsb-opencode_0000_0000 | 40 | 0.000% | 0.000% | 0.000 s | 2.797 MB | 2.797 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5240 | sandbox_agent_lsb-opencode_0000_0000 | 40 | 174.552% | 179.600% | 68.520 s | 91.496 MB | 91.547 MB | 313.194 MB | 313.199 MB | n/a MB | n/a MB |
| python3 | 5380 | sandbox_agent_lsb-opencode_0000_0000 | 57 | 173.517% | 180.725% | 97.880 s | 91.511 MB | 92.914 MB | 311.934 MB | 313.797 MB | n/a MB | n/a MB |
| bash | 5379 | sandbox_agent_lsb-opencode_0000_0000 | 57 | 0.000% | 0.000% | 0.000 s | 2.715 MB | 2.715 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 5450 | sandbox_agent_lsb-opencode_0000_0000 | 90 | 0.000% | 0.000% | 0.000 s | 2.770 MB | 2.770 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| mkdir | 5451 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 0.461 MB | 0.461 MB | n/a MB | n/a MB |
| python3 | 5452 | sandbox_agent_lsb-opencode_0000_0000 | 89 | 0.011% | 0.990% | 0.010 s | 100.094 MB | 100.094 MB | 322.809 MB | 322.809 MB | n/a MB | n/a MB |
| bash | 5524 | sandbox_agent_lsb-opencode_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 2.656 MB | 2.656 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5525 | sandbox_agent_lsb-opencode_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 23.785 MB | 23.785 MB | 29.074 MB | 29.074 MB | n/a MB | n/a MB |
| python3 | 5542 | sandbox_agent_lsb-opencode_0000_0000 | 76 | 173.461% | 177.024% | 131.020 s | 104.883 MB | 104.949 MB | 324.492 MB | 324.492 MB | n/a MB | n/a MB |
| bash | 5541 | sandbox_agent_lsb-opencode_0000_0000 | 76 | 0.000% | 0.000% | 0.000 s | 2.617 MB | 2.617 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 5587 | sandbox_agent_lsb-opencode_0000_0000 | 36 | 0.000% | 0.000% | 0.000 s | 2.691 MB | 2.691 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5588 | sandbox_agent_lsb-opencode_0000_0000 | 36 | 0.000% | 0.000% | 0.000 s | 59.500 MB | 59.500 MB | 281.605 MB | 281.605 MB | n/a MB | n/a MB |
| bash | 5620 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.691 MB | 2.691 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5621 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 162.056% | 174.197% | 3.270 s | 1777.534 MB | 1875.168 MB | 3158.453 MB | 3266.008 MB | n/a MB | n/a MB |
| bash | 5653 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 0.000% | 0.000% | 0.000 s | 2.555 MB | 2.555 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5654 | sandbox_agent_lsb-opencode_0000_0000 | 13 | 172.537% | 174.681% | 20.840 s | 100.837 MB | 100.848 MB | 324.398 MB | 324.398 MB | n/a MB | n/a MB |
| python3 | 5675 | sandbox_agent_lsb-opencode_0000_0000 | 24 | 44.548% | 171.988% | 10.310 s | 99.684 MB | 101.930 MB | 325.516 MB | 327.695 MB | n/a MB | n/a MB |
| bash | 5674 | sandbox_agent_lsb-opencode_0000_0000 | 24 | 0.000% | 0.000% | 0.000 s | 2.949 MB | 2.949 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 5696 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.678 MB | 2.711 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5697 | sandbox_agent_lsb-opencode_0000_0000 | 4 | 0.000% | 0.000% | 0.000 s | 22.703 MB | 22.703 MB | 28.281 MB | 28.281 MB | n/a MB | n/a MB |
| bash | 5710 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.566 MB | 2.566 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5711 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 21.199 MB | 21.199 MB | 26.969 MB | 26.969 MB | n/a MB | n/a MB |
| bash | 5721 | sandbox_agent_lsb-opencode_0000_0000 | 34 | 0.000% | 0.000% | 0.000 s | 2.898 MB | 2.898 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5722 | sandbox_agent_lsb-opencode_0000_0000 | 34 | 0.000% | 0.000% | 0.000 s | 21.574 MB | 21.574 MB | 27.035 MB | 27.035 MB | n/a MB | n/a MB |
| bash | 5787 | sandbox_agent_lsb-opencode_0000_0000 | 11 | 0.000% | 0.000% | 0.000 s | 2.605 MB | 2.605 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5788 | sandbox_agent_lsb-opencode_0000_0000 | 11 | 174.733% | 177.234% | 17.610 s | 108.920 MB | 112.766 MB | 332.497 MB | 336.203 MB | n/a MB | n/a MB |
| bash | 5837 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.828 MB | 2.828 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5838 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 153.970% | 174.458% | 6.210 s | 1458.990 MB | 1872.992 MB | 2572.666 MB | 3264.566 MB | n/a MB | n/a MB |
| bash | 5853 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.617 MB | 2.617 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5854 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 164.185% | 177.210% | 9.930 s | 1612.624 MB | 1878.391 MB | 2832.528 MB | 3269.738 MB | n/a MB | n/a MB |
| bash | 5868 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.672 MB | 2.672 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5869 | sandbox_agent_lsb-opencode_0000_0000 | 3 | 143.103% | 175.155% | 2.890 s | 1252.056 MB | 1871.012 MB | 2243.780 MB | 3261.887 MB | n/a MB | n/a MB |
| bash | 5883 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 2.664 MB | 2.664 MB | 3.848 MB | 3.848 MB | n/a MB | n/a MB |
| python3 | 5884 | sandbox_agent_lsb-opencode_0000_0000 | 5 | 0.000% | 0.000% | 0.000 s | 22.801 MB | 22.801 MB | 28.332 MB | 28.332 MB | n/a MB | n/a MB |
| python3 | 5917 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 163.156% | 175.203% | 9.860 s | 1608.533 MB | 1875.645 MB | 2801.979 MB | 3267.543 MB | n/a MB | n/a MB |
| bash | 5916 | sandbox_agent_lsb-opencode_0000_0000 | 7 | 0.000% | 0.000% | 0.000 s | 2.637 MB | 2.637 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| bash | 5937 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.684 MB | 2.684 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 5938 | sandbox_agent_lsb-opencode_0000_0000 | 6 | 159.451% | 174.387% | 8.040 s | 1570.874 MB | 1882.672 MB | 2762.740 MB | 3274.508 MB | n/a MB | n/a MB |
| bash | 6014 | sandbox_agent_lsb-opencode_0000_0000 | 22 | 0.000% | 0.000% | 0.000 s | 2.684 MB | 2.684 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 6015 | sandbox_agent_lsb-opencode_0000_0000 | 22 | 26.541% | 172.883% | 5.610 s | 1907.233 MB | 2284.750 MB | 3307.343 MB | 3832.750 MB | n/a MB | n/a MB |
| bash | 6037 | sandbox_agent_lsb-opencode_0000_0000 | 10 | 0.000% | 0.000% | 0.000 s | 2.621 MB | 2.621 MB | 3.852 MB | 3.852 MB | n/a MB | n/a MB |
| python3 | 6038 | sandbox_agent_lsb-opencode_0000_0000 | 10 | 169.799% | 175.807% | 15.400 s | 1741.757 MB | 2146.746 MB | 3248.654 MB | 4065.480 MB | n/a MB | n/a MB |
| bash | 6102 | sandbox_agent_lsb-opencode_0000_0000 | 15 | 0.000% | 0.000% | 0.000 s | 2.680 MB | 2.680 MB | 3.988 MB | 3.988 MB | n/a MB | n/a MB |
| python3 | 6103 | sandbox_agent_lsb-opencode_0000_0000 | 15 | 170.280% | 176.516% | 24.010 s | 1589.070 MB | 1929.371 MB | 2894.927 MB | 3396.539 MB | n/a MB | n/a MB |
| python3 | 6156 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 279.590 MB | 279.590 MB | 2863.086 MB | 2863.086 MB | n/a MB | n/a MB |
| bash | 6155 | sandbox_agent_lsb-opencode_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.887 MB | 2.887 MB | 3.992 MB | 3.992 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 9.827% | 100.000% | 11938.522 MB | 14968.000 MB | 31.775 W | 79.578 W | 493200.575 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-opencode_0000_0000 | 37.252% | 208.945% | 5778.587 s | 1140.645 MB | 2857.766 MB | 167.507812 MB | 314.613281 MB | 26.857862 MB | 0.509185 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 2015 | 15510.912 | interrupted |
| run0:write_lora_adapter:agent_lsb-opencode_0000 | -1 | 15510.911 | interrupted |
| engine:execute | 2016 | 15510.909 | interrupted |
| harness:attempt_rpc | 2261 | 15505.116 | interrupted |
| harness:await_cli | -1 | 15486.794 | interrupted |
| tool:bash | -1 | 0.736 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| llm:attempt | 122/122 | 0 | 0 | 13209.284 | 4.713 | 13204.569 | 9.400 | 108272.820 | 59755.444 | 323050.307 |
| tool:bash | 100/101 | 0 | 1 | 2252.902 | n/a | n/a | 11.266 | 22529.021 | 420.221 | 84905.199 |
| harness:startup_ready | 1/1 | 0 | 0 | 16.234 | n/a | n/a | 61.183 | 16234.461 | 16234.461 | 16234.461 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.671 | 1.073 | 3.598 | 52.545 | 4671.135 | 4671.135 | 4671.135 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.671 | 1.073 | 3.598 | 52.541 | 4670.905 | 4670.905 | 4670.905 |
| tool:read | 30/30 | 0 | 0 | 2.897 | n/a | n/a | 9.319 | 96.552 | 79.695 | 199.272 |
| syscall:sendto | 885/885 | 0 | 0 | 1.913 | n/a | n/a | 0.552 | 2.162 | 1.736 | 4.336 |
| syscall:connect | 504/504 | 0 | 0 | 1.176 | n/a | n/a | 0.686 | 2.332 | 2.061 | 4.482 |
| harness:submit | 1/1 | 0 | 0 | 1.007 | n/a | n/a | 0.004 | 1007.411 | 1007.411 | 1007.411 |
| sandbox:create | 1/1 | 0 | 0 | 1.007 | 0.244 | 0.762 | 0.000 | 1006.733 | 1006.733 | 1006.733 |
| run:detect | 1/1 | 0 | 0 | 0.711 | 0.001 | 0.711 | 0.000 | 711.254 | 711.254 | 711.254 |
| run:container_call | 6/6 | 0 | 0 | 0.612 | 0.001 | 0.611 | 0.000 | 102.023 | 53.837 | 307.747 |
| sandbox:start | 1/1 | 0 | 0 | 0.541 | 0.002 | 0.539 | 0.000 | 540.822 | 540.822 | 540.822 |
| runtime.container_create | 1/1 | 0 | 0 | 0.541 | 0.002 | 0.539 | 0.000 | 540.684 | 540.684 | 540.684 |
| tool:write | 3/3 | 0 | 0 | 0.456 | n/a | n/a | 0.069 | 151.911 | 145.594 | 198.245 |
| syscall:execve | 207/207 | 0 | 0 | 0.325 | n/a | n/a | 0.069 | 1.570 | 1.307 | 3.014 |
| tool:todowrite | 8/8 | 0 | 0 | 0.278 | n/a | n/a | 0.000 | 34.789 | 27.257 | 61.701 |
| tool:edit | 2/2 | 0 | 0 | 0.083 | n/a | n/a | 0.000 | 41.329 | 41.329 | 43.944 |
| agency:services_start | 1/1 | 0 | 0 | 0.074 | 0.040 | 0.033 | 0.000 | 73.629 | 73.629 | 73.629 |
| agent:create | 1/1 | 0 | 0 | 0.048 | 0.009 | 0.040 | 0.000 | 48.384 | 48.384 | 48.384 |
| harness:launch | 1/1 | 0 | 0 | 0.046 | n/a | n/a | 1.180 | 46.459 | 46.459 | 46.459 |
| syscall:bind | 11/11 | 0 | 0 | 0.031 | n/a | n/a | 0.100 | 2.797 | 2.352 | 4.478 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.428 | 1.428 | 1.428 |
| sync:container | 6/6 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.070 | 0.076 | 0.085 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.187 | 0.187 | 0.187 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.065 | 0.065 | 0.065 |
| engine:execute | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:attempt_rpc | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| harness:await_cli | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| run:write_lora_adapter | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 15418 | 0.085 | 0.028 | 1.614 | 0.058 | 13.131325 CPU seconds | n/a |
| GPU 0 memory | MB | 15420 | 11938.522 | 11670.000 | 14968.000 | 11908.000 | n/a | n/a |
| GPU 0 power | W | 15420 | 31.775 | 27.092 | 79.578 | 27.273 | n/a | 493200.575 J |
| GPU 0 proc / 1742-3011 / sandbox / ~ / device / GPU-66a04e2d-a439-af99-2276-cdd3659f5c5b memory | MB | 15420 | 3272.729 | 3118.000 | 6278.000 | 3216.000 | n/a | n/a |
| GPU 0 proc / 1742-3011 / sandbox / ~ / device / GPU-66a04e2d-a439-af99-2276-cdd3659f5c5b estimated power | W | 11617 | 2.689 | 0.000 | 78.782 | 0.000 | n/a | n/a |
| GPU 0 proc / 1742-3011 / sandbox / ~ / device / GPU-66a04e2d-a439-af99-2276-cdd3659f5c5b utilization | percent | 11617 | 2.719 | 0.000 | 99.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 1789-6804 / sandbox / ~ / device / GPU-66a04e2d-a439-af99-2276-cdd3659f5c5b memory | MB | 15420 | 8183.792 | 8070.000 | 8210.000 | 8210.000 | n/a | n/a |
| GPU 0 proc / 1789-6804 / sandbox / ~ / device / GPU-66a04e2d-a439-af99-2276-cdd3659f5c5b estimated power | W | 3546 | 23.233 | 0.000 | 72.523 | 0.000 | n/a | n/a |
| GPU 0 proc / 1789-6804 / sandbox / ~ / device / GPU-66a04e2d-a439-af99-2276-cdd3659f5c5b utilization | percent | 3546 | 32.186 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 15420 | 11456.522 | 11188.000 | 14486.000 | 11426.000 | n/a | n/a |
| GPU 0 utilization | percent | 15420 | 9.827 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 15420 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 15419 | 1.815 | 0.084 | 73.087 | 7.576 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 15419 | 11.919 | 6.801 | 59.045 | 27.569 | n/a | n/a |
| host disk_read_mb_s | MB/s | 15419 | 0.024 | 0.000 | 60.177 | 0.000 | n/a | n/a |
| host disk_write_mb_s | MB/s | 15419 | 0.087 | 0.000 | 85.217 | 0.000 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 15419 | 0.016 | 0.000 | 29.063 | 0.000 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 15419 | 0.017 | 0.000 | 29.112 | 0.000 | n/a | n/a |
| host mem_total_mb | MB | 15420 | 15363.535 | 15363.535 | 15363.535 | 15363.535 | n/a | n/a |
| host mem_used_mb | MB | 15420 | 7835.752 | 6808.613 | 10079.262 | 8627.855 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 15419 | 0.000 | 0.000 | 3.139 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 15419 | 0.000 | 0.000 | 3.139 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 15419 | 0.002 | 0.000 | 11.963 | 0.001 | n/a | n/a |
| host net_tx_mb_s | MB/s | 15419 | 0.002 | 0.000 | 0.551 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1733) CPU | percent | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 1733) io read MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1733) io write MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 1733) rss_mb | MB | 15420 | 3.340 | 3.340 | 3.340 | 3.340 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 1733) main thread run-queue wait | percent | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 1733) vms_mb | MB | 15420 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1742) CPU | percent | 15419 | 7.634 | 0.000 | 179.748 | 2.985 | 1188.030000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 1742) io read MB/s | MB/s | 15419 | 0.011 | 0.000 | 91.177 | 0.000 | 165.113281 MB | n/a |
| Agency harness — python -m lsbench (PID 1742) io write MB/s | MB/s | 15419 | 0.054 | 0.000 | 13.651 | 0.556 | 832.226562 MB | n/a |
| Agency harness — python -m lsbench (PID 1742) rss_mb | MB | 15420 | 3122.349 | 2518.891 | 5077.445 | 3687.031 | n/a | n/a |
| Agency harness — python -m lsbench (PID 1742) main thread run-queue wait | percent | 15419 | 0.000 | 0.000 | 0.199 | 0.000 | 0.002626 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 1742) vms_mb | MB | 15420 | 16061.450 | 14095.812 | 20841.672 | 16672.258 | n/a | n/a |
| Python — vllm (PID 1754) CPU | percent | 15419 | 0.269 | 0.000 | 7.909 | 0.000 | 41.920000 CPU seconds | n/a |
| Python — vllm (PID 1754) io read MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 1754) io write MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.008 | 0.000 | 0.179688 MB | n/a |
| Python — vllm (PID 1754) rss_mb | MB | 15420 | 1791.134 | 1786.469 | 1792.484 | 1792.125 | n/a | n/a |
| Python — vllm (PID 1754) main thread run-queue wait | percent | 15419 | 0.008 | 0.000 | 2.822 | 0.001 | 1.179596 run-queue seconds | n/a |
| Python — vllm (PID 1754) vms_mb | MB | 15420 | 11046.462 | 10983.473 | 11060.492 | 11060.492 | n/a | n/a |
| Python — python -c (PID 1788) CPU | percent | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 1788) io read MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1788) io write MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 1788) rss_mb | MB | 15420 | 12.199 | 12.199 | 12.199 | 12.199 | n/a | n/a |
| Python — python -c (PID 1788) main thread run-queue wait | percent | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 1788) vms_mb | MB | 15420 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 1789) CPU | percent | 15419 | 3.268 | 0.000 | 42.531 | 0.995 | 508.380000 CPU seconds | n/a |
| VLLM::EngineCore (PID 1789) io read MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 1789) io write MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.008 | 0.000 | 0.101562 MB | n/a |
| VLLM::EngineCore (PID 1789) rss_mb | MB | 15420 | 2330.152 | 2323.359 | 2331.770 | 2331.645 | n/a | n/a |
| VLLM::EngineCore (PID 1789) main thread run-queue wait | percent | 15419 | 0.002 | 0.000 | 0.380 | 0.000 | 0.241241 run-queue seconds | n/a |
| VLLM::EngineCore (PID 1789) vms_mb | MB | 15420 | 21241.534 | 21235.102 | 21243.039 | 21243.039 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2009) CPU | percent | 15419 | 0.027 | 0.000 | 3.981 | 0.000 | 4.220000 CPU seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2009) io read MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2009) io write MB/s | MB/s | 15419 | 0.000 | 0.000 | 0.008 | 0.004 | 0.410156 MB | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2009) rss_mb | MB | 15420 | 44.887 | 43.598 | 45.168 | 45.043 | n/a | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2009) main thread run-queue wait | percent | 15419 | 0.001 | 0.000 | 2.861 | 0.000 | 0.191212 run-queue seconds | n/a |
| Python — python -m lsbench.vertex_proxy (PID 2009) vms_mb | MB | 15420 | 131.222 | 131.172 | 131.715 | 131.172 | n/a | n/a |
| docker info (PID 2017) rss_mb | MB | 1 | 30.551 | 30.551 | 30.551 | 30.551 | n/a | n/a |
| docker info (PID 2017) vms_mb | MB | 1 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2124) CPU | percent | 15418 | 0.002 | 0.000 | 0.996 | 0.000 | 0.320000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2124) rss_mb | MB | 15419 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2124) main thread run-queue wait | percent | 15418 | 0.002 | 0.000 | 5.361 | 0.000 | 0.301376 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — docker-init (PID 2124) vms_mb | MB | 15419 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2158) CPU | percent | 15418 | 0.002 | 0.000 | 0.996 | 0.000 | 0.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2158) rss_mb | MB | 15419 | 1.301 | 1.301 | 1.301 | 1.301 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2158) main thread run-queue wait | percent | 15418 | 0.002 | 0.000 | 5.548 | 0.000 | 0.291323 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — tail (PID 2158) vms_mb | MB | 15419 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2248) CPU | percent | 15418 | 31.242 | 0.000 | 99.287 | 59.691 | 4845.850000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2248) rss_mb | MB | 15419 | 111.653 | 3.016 | 116.738 | 114.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2248) main thread run-queue wait | percent | 15418 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000099 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 2248) vms_mb | MB | 15419 | 902.110 | 4.262 | 903.637 | 902.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2254) CPU | percent | 2 | 55.159 | 50.627 | 59.690 | 59.690 | 1.110000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2254) rss_mb | MB | 3 | 49.257 | 19.914 | 78.820 | 78.820 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2254) main thread run-queue wait | percent | 2 | 0.032 | 0.023 | 0.040 | 0.040 | 0.000639 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2254) vms_mb | MB | 3 | 59.523 | 25.883 | 94.422 | 94.422 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2262) rss_mb | MB | 1 | 17.582 | 17.582 | 17.582 | 17.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2262) vms_mb | MB | 1 | 6358.133 | 6358.133 | 6358.133 | 6358.133 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2276) CPU | percent | 15413 | 2.837 | 0.000 | 126.017 | 8.954 | 439.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2276) rss_mb | MB | 15414 | 712.780 | 35.980 | 982.660 | 742.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2276) main thread run-queue wait | percent | 15413 | 1.046 | 0.000 | 72.601 | 3.366 | 162.426211 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — opencode (PID 2276) vms_mb | MB | 15414 | 16631.659 | 6358.133 | 16731.152 | 16731.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2775) rss_mb | MB | 1 | 6.340 | 6.340 | 6.340 | 6.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 2775) vms_mb | MB | 1 | 11.656 | 11.656 | 11.656 | 11.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3042) CPU | percent | 520 | 0.002 | 0.000 | 0.989 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3042) rss_mb | MB | 521 | 21.699 | 21.699 | 21.699 | 21.699 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3042) main thread run-queue wait | percent | 520 | 0.000 | 0.000 | 0.005 | 0.000 | 0.000059 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python -c (PID 3042) vms_mb | MB | 521 | 27.918 | 27.918 | 27.918 | 27.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_batch1_clean.py (PID 3262) CPU | percent | 492 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_batch1_clean.py (PID 3262) rss_mb | MB | 493 | 21.582 | 21.582 | 21.582 | 21.582 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_batch1_clean.py (PID 3262) main thread run-queue wait | percent | 492 | 0.000 | 0.000 | 0.042 | 0.000 | 0.000509 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — run_batch1_clean.py (PID 3262) vms_mb | MB | 493 | 26.695 | 26.695 | 26.695 | 26.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3482) CPU | percent | 82 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3482) rss_mb | MB | 83 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3482) main thread run-queue wait | percent | 82 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3482) vms_mb | MB | 83 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3483) CPU | percent | 82 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3483) rss_mb | MB | 83 | 21.297 | 21.297 | 21.297 | 21.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3483) main thread run-queue wait | percent | 82 | 0.000 | 0.000 | 0.001 | 0.000 | 0.000011 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3483) vms_mb | MB | 83 | 26.621 | 26.621 | 26.621 | 26.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3649) CPU | percent | 299 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3649) rss_mb | MB | 300 | 2.891 | 2.891 | 2.891 | 2.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3649) main thread run-queue wait | percent | 299 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3649) vms_mb | MB | 300 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3650) CPU | percent | 299 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3650) rss_mb | MB | 300 | 20.938 | 20.938 | 20.938 | 20.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3650) main thread run-queue wait | percent | 299 | 0.001 | 0.000 | 0.052 | 0.000 | 0.002023 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3650) vms_mb | MB | 300 | 26.652 | 26.652 | 26.652 | 26.652 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3993) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3993) rss_mb | MB | 40 | 2.586 | 2.586 | 2.586 | 2.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3993) main thread run-queue wait | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 3993) vms_mb | MB | 40 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3994) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3994) rss_mb | MB | 40 | 21.348 | 21.348 | 21.348 | 21.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3994) main thread run-queue wait | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 3994) vms_mb | MB | 40 | 26.785 | 26.785 | 26.785 | 26.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4079) CPU | percent | 108 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4079) rss_mb | MB | 109 | 2.734 | 2.734 | 2.734 | 2.734 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4079) main thread run-queue wait | percent | 108 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4079) vms_mb | MB | 109 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4080) CPU | percent | 108 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4080) rss_mb | MB | 109 | 20.816 | 20.816 | 20.816 | 20.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4080) main thread run-queue wait | percent | 108 | 0.000 | 0.000 | 0.020 | 0.000 | 0.000346 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4080) vms_mb | MB | 109 | 26.660 | 26.660 | 26.660 | 26.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4215) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4215) rss_mb | MB | 6 | 2.816 | 2.816 | 2.816 | 2.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4215) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4215) vms_mb | MB | 6 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4216) CPU | percent | 5 | 1.391 | 0.000 | 6.955 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4216) rss_mb | MB | 6 | 18.872 | 8.797 | 20.887 | 20.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4216) main thread run-queue wait | percent | 5 | 0.029 | 0.000 | 0.146 | 0.000 | 0.001467 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4216) vms_mb | MB | 6 | 24.424 | 13.184 | 26.672 | 26.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4230) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4230) rss_mb | MB | 6 | 2.891 | 2.891 | 2.891 | 2.891 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4230) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4230) vms_mb | MB | 6 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4231) CPU | percent | 5 | 1.986 | 0.000 | 9.932 | 0.000 | 0.100000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4231) rss_mb | MB | 6 | 18.780 | 7.055 | 21.125 | 21.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4231) main thread run-queue wait | percent | 5 | 0.106 | 0.000 | 0.372 | 0.000 | 0.005337 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4231) vms_mb | MB | 6 | 24.148 | 11.785 | 26.621 | 26.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4281) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4281) rss_mb | MB | 19 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4281) main thread run-queue wait | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4281) vms_mb | MB | 19 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4282) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4282) rss_mb | MB | 19 | 36.621 | 36.621 | 36.621 | 36.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4282) main thread run-queue wait | percent | 18 | 0.034 | 0.000 | 0.280 | 0.000 | 0.006185 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4282) vms_mb | MB | 19 | 43.297 | 43.297 | 43.297 | 43.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4400) rss_mb | MB | 1 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4400) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4401) rss_mb | MB | 1 | 34.195 | 34.195 | 34.195 | 34.195 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4401) vms_mb | MB | 1 | 228.551 | 228.551 | 228.551 | 228.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4436) rss_mb | MB | 1 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4436) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4437) rss_mb | MB | 1 | 17.809 | 17.809 | 17.809 | 17.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4437) vms_mb | MB | 1 | 209.895 | 209.895 | 209.895 | 209.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4452) rss_mb | MB | 1 | 2.895 | 2.895 | 2.895 | 2.895 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4452) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4453) rss_mb | MB | 1 | 20.457 | 20.457 | 20.457 | 20.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4453) vms_mb | MB | 1 | 212.258 | 212.258 | 212.258 | 212.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4468) rss_mb | MB | 1 | 2.812 | 2.812 | 2.812 | 2.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4468) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4469) rss_mb | MB | 1 | 9.445 | 9.445 | 9.445 | 9.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4469) vms_mb | MB | 1 | 13.410 | 13.410 | 13.410 | 13.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4618) rss_mb | MB | 1 | 2.695 | 2.695 | 2.695 | 2.695 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4618) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4619) rss_mb | MB | 1 | 45.914 | 45.914 | 45.914 | 45.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4619) vms_mb | MB | 1 | 52.055 | 52.055 | 52.055 | 52.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4651) rss_mb | MB | 1 | 2.688 | 2.688 | 2.688 | 2.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4651) vms_mb | MB | 1 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4652) rss_mb | MB | 1 | 38.281 | 38.281 | 38.281 | 38.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4652) vms_mb | MB | 1 | 44.730 | 44.730 | 44.730 | 44.730 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4748) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4748) rss_mb | MB | 13 | 3.059 | 3.059 | 3.059 | 3.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4748) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4748) vms_mb | MB | 13 | 3.996 | 3.996 | 3.996 | 3.996 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4749) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4749) rss_mb | MB | 13 | 24.457 | 24.457 | 24.457 | 24.457 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4749) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4749) vms_mb | MB | 13 | 29.723 | 29.723 | 29.723 | 29.723 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4795) CPU | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4795) rss_mb | MB | 41 | 2.977 | 2.977 | 2.977 | 2.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4795) main thread run-queue wait | percent | 40 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4795) vms_mb | MB | 41 | 3.988 | 3.988 | 3.988 | 3.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4796) CPU | percent | 40 | 0.617 | 0.000 | 24.686 | 0.000 | 0.250000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4796) rss_mb | MB | 41 | 38.014 | 14.551 | 38.801 | 38.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4796) main thread run-queue wait | percent | 40 | 0.114 | 0.000 | 4.412 | 0.000 | 0.046283 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4796) vms_mb | MB | 41 | 231.480 | 209.066 | 232.199 | 232.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4830) CPU | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4830) rss_mb | MB | 9 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4830) main thread run-queue wait | percent | 8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4830) vms_mb | MB | 9 | 3.855 | 3.855 | 3.855 | 3.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4831) CPU | percent | 7 | 170.008 | 154.722 | 174.037 | 173.050 | 11.970000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4831) rss_mb | MB | 8 | 1364.587 | 24.074 | 1557.660 | 1557.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4831) main thread run-queue wait | percent | 7 | 51.237 | 47.221 | 56.196 | 49.739 | 3.607525 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4831) vms_mb | MB | 8 | 2605.047 | 215.941 | 2948.875 | 2948.875 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4867) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4867) rss_mb | MB | 6 | 2.625 | 2.625 | 2.625 | 2.625 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4867) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4867) vms_mb | MB | 6 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4868) CPU | percent | 5 | 174.706 | 172.018 | 179.083 | 174.494 | 8.790000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4868) rss_mb | MB | 6 | 65.616 | 63.824 | 66.074 | 66.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4868) main thread run-queue wait | percent | 5 | 65.730 | 52.767 | 78.003 | 78.003 | 3.307395 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4868) vms_mb | MB | 6 | 288.917 | 286.227 | 290.242 | 290.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4887) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4887) rss_mb | MB | 5 | 2.758 | 2.758 | 2.758 | 2.758 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4887) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4887) vms_mb | MB | 5 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4888) CPU | percent | 4 | 1.738 | 0.000 | 5.964 | 0.000 | 0.070000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4888) rss_mb | MB | 5 | 21.226 | 14.988 | 22.785 | 22.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4888) main thread run-queue wait | percent | 4 | 0.067 | 0.000 | 0.160 | 0.000 | 0.002718 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4888) vms_mb | MB | 5 | 26.716 | 20.188 | 28.348 | 28.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4901) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4901) rss_mb | MB | 4 | 2.586 | 2.586 | 2.586 | 2.586 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4901) main thread run-queue wait | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4901) vms_mb | MB | 4 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4902) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4902) rss_mb | MB | 4 | 22.898 | 22.898 | 22.898 | 22.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4902) main thread run-queue wait | percent | 3 | 0.075 | 0.000 | 0.186 | 0.038 | 0.002273 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4902) vms_mb | MB | 4 | 28.156 | 28.156 | 28.156 | 28.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4920) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4920) rss_mb | MB | 2 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4920) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4920) vms_mb | MB | 2 | 3.855 | 3.855 | 3.855 | 3.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4921) CPU | percent | 1 | 37.555 | 37.555 | 37.555 | 37.555 | 0.380000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4921) rss_mb | MB | 2 | 821.857 | 36.508 | 1607.207 | 1607.207 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4921) main thread run-queue wait | percent | 1 | 0.276 | 0.276 | 0.276 | 0.276 | 0.002794 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4921) vms_mb | MB | 2 | 1607.771 | 230.434 | 2985.109 | 2985.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4956) rss_mb | MB | 1 | 2.648 | 2.648 | 2.648 | 2.648 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4956) vms_mb | MB | 1 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4957) rss_mb | MB | 1 | 1566.230 | 1566.230 | 1566.230 | 1566.230 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 4957) vms_mb | MB | 1 | 2938.070 | 2938.070 | 2938.070 | 2938.070 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4984) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 4984) vms_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5135) CPU | percent | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5135) rss_mb | MB | 51 | 2.609 | 2.609 | 2.609 | 2.609 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5135) main thread run-queue wait | percent | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5135) vms_mb | MB | 51 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5136) CPU | percent | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5136) rss_mb | MB | 51 | 21.672 | 21.672 | 21.672 | 21.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5136) main thread run-queue wait | percent | 50 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5136) vms_mb | MB | 51 | 26.809 | 26.809 | 26.809 | 26.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5221) CPU | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5221) rss_mb | MB | 18 | 2.785 | 2.785 | 2.785 | 2.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5221) main thread run-queue wait | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5221) vms_mb | MB | 18 | 3.988 | 3.988 | 3.988 | 3.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5222) CPU | percent | 17 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5222) rss_mb | MB | 18 | 22.374 | 22.246 | 22.438 | 22.246 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5222) main thread run-queue wait | percent | 17 | 0.015 | 0.000 | 0.240 | 0.000 | 0.002646 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5222) vms_mb | MB | 18 | 27.656 | 27.445 | 27.762 | 27.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5239) CPU | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5239) rss_mb | MB | 40 | 2.797 | 2.797 | 2.797 | 2.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5239) main thread run-queue wait | percent | 39 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5239) vms_mb | MB | 40 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5240) CPU | percent | 39 | 174.552 | 170.994 | 179.600 | 176.058 | 68.520000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5240) rss_mb | MB | 40 | 91.496 | 90.531 | 91.547 | 91.547 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5240) main thread run-queue wait | percent | 39 | 56.082 | 48.902 | 72.780 | 62.712 | 22.015217 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5240) vms_mb | MB | 40 | 313.194 | 312.980 | 313.199 | 313.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5379) CPU | percent | 56 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5379) rss_mb | MB | 57 | 2.715 | 2.715 | 2.715 | 2.715 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5379) main thread run-queue wait | percent | 56 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5379) vms_mb | MB | 57 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5380) CPU | percent | 56 | 173.517 | 143.748 | 180.725 | 174.642 | 97.880000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5380) rss_mb | MB | 57 | 91.511 | 14.109 | 92.914 | 92.914 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5380) main thread run-queue wait | percent | 56 | 56.253 | 48.564 | 79.256 | 73.428 | 31.731698 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5380) vms_mb | MB | 57 | 311.934 | 207.609 | 313.797 | 313.797 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5450) CPU | percent | 89 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5450) rss_mb | MB | 90 | 2.770 | 2.770 | 2.770 | 2.770 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5450) main thread run-queue wait | percent | 89 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5450) vms_mb | MB | 90 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — mkdir (PID 5451) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — mkdir (PID 5451) vms_mb | MB | 1 | 0.461 | 0.461 | 0.461 | 0.461 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5452) CPU | percent | 88 | 0.011 | 0.000 | 0.990 | 0.000 | 0.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5452) rss_mb | MB | 89 | 100.094 | 100.094 | 100.094 | 100.094 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5452) main thread run-queue wait | percent | 88 | 0.009 | 0.000 | 0.215 | 0.000 | 0.007955 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5452) vms_mb | MB | 89 | 322.809 | 322.809 | 322.809 | 322.809 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5524) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5524) rss_mb | MB | 15 | 2.656 | 2.656 | 2.656 | 2.656 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5524) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5524) vms_mb | MB | 15 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5525) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5525) rss_mb | MB | 15 | 23.785 | 23.785 | 23.785 | 23.785 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5525) main thread run-queue wait | percent | 14 | 0.003 | 0.000 | 0.045 | 0.000 | 0.000452 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5525) vms_mb | MB | 15 | 29.074 | 29.074 | 29.074 | 29.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5541) CPU | percent | 75 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5541) rss_mb | MB | 76 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5541) main thread run-queue wait | percent | 75 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5541) vms_mb | MB | 76 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5542) CPU | percent | 75 | 173.461 | 162.047 | 177.024 | 173.562 | 131.020000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5542) rss_mb | MB | 76 | 104.883 | 103.949 | 104.949 | 104.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5542) main thread run-queue wait | percent | 75 | 58.840 | 48.126 | 78.343 | 73.126 | 44.443135 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5542) vms_mb | MB | 76 | 324.492 | 324.492 | 324.492 | 324.492 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5587) CPU | percent | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5587) rss_mb | MB | 36 | 2.691 | 2.691 | 2.691 | 2.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5587) main thread run-queue wait | percent | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5587) vms_mb | MB | 36 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5588) CPU | percent | 35 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5588) rss_mb | MB | 36 | 59.500 | 59.500 | 59.500 | 59.500 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5588) main thread run-queue wait | percent | 35 | 0.003 | 0.000 | 0.091 | 0.000 | 0.000919 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5588) vms_mb | MB | 36 | 281.605 | 281.605 | 281.605 | 281.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5620) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5620) rss_mb | MB | 3 | 2.691 | 2.691 | 2.691 | 2.691 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5620) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5620) vms_mb | MB | 3 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5621) CPU | percent | 2 | 162.056 | 149.915 | 174.197 | 174.197 | 3.270000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5621) rss_mb | MB | 3 | 1777.534 | 1582.266 | 1875.168 | 1875.168 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5621) main thread run-queue wait | percent | 2 | 61.925 | 50.998 | 72.851 | 72.851 | 1.249728 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5621) vms_mb | MB | 3 | 3158.453 | 2943.344 | 3266.008 | 3266.008 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5653) CPU | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5653) rss_mb | MB | 13 | 2.555 | 2.555 | 2.555 | 2.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5653) main thread run-queue wait | percent | 12 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5653) vms_mb | MB | 13 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5654) CPU | percent | 12 | 172.537 | 170.082 | 174.681 | 171.037 | 20.840000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5654) rss_mb | MB | 13 | 100.837 | 100.711 | 100.848 | 100.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5654) main thread run-queue wait | percent | 12 | 70.980 | 49.758 | 74.268 | 49.758 | 8.573204 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5654) vms_mb | MB | 13 | 324.398 | 324.398 | 324.398 | 324.398 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5674) CPU | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5674) rss_mb | MB | 24 | 2.949 | 2.949 | 2.949 | 2.949 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5674) main thread run-queue wait | percent | 23 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5674) vms_mb | MB | 24 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5675) CPU | percent | 23 | 44.548 | 0.000 | 171.988 | 0.000 | 10.310000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5675) rss_mb | MB | 24 | 99.684 | 95.781 | 101.930 | 99.957 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5675) main thread run-queue wait | percent | 23 | 14.711 | 0.000 | 73.302 | 0.000 | 3.404665 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5675) vms_mb | MB | 24 | 325.516 | 321.953 | 327.695 | 325.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5696) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5696) rss_mb | MB | 5 | 2.678 | 2.547 | 2.711 | 2.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5696) main thread run-queue wait | percent | 4 | 0.008 | 0.000 | 0.032 | 0.000 | 0.000327 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5696) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5697) CPU | percent | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5697) rss_mb | MB | 4 | 22.703 | 22.703 | 22.703 | 22.703 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5697) main thread run-queue wait | percent | 3 | 0.037 | 0.000 | 0.110 | 0.000 | 0.001117 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5697) vms_mb | MB | 4 | 28.281 | 28.281 | 28.281 | 28.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5710) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5710) rss_mb | MB | 3 | 2.566 | 2.566 | 2.566 | 2.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5710) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5710) vms_mb | MB | 3 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5711) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5711) rss_mb | MB | 3 | 21.199 | 21.199 | 21.199 | 21.199 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5711) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5711) vms_mb | MB | 3 | 26.969 | 26.969 | 26.969 | 26.969 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5721) CPU | percent | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5721) rss_mb | MB | 34 | 2.898 | 2.898 | 2.898 | 2.898 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5721) main thread run-queue wait | percent | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5721) vms_mb | MB | 34 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5722) CPU | percent | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5722) rss_mb | MB | 34 | 21.574 | 21.574 | 21.574 | 21.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5722) main thread run-queue wait | percent | 33 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5722) vms_mb | MB | 34 | 27.035 | 27.035 | 27.035 | 27.035 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5787) CPU | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5787) rss_mb | MB | 11 | 2.605 | 2.605 | 2.605 | 2.605 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5787) main thread run-queue wait | percent | 10 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5787) vms_mb | MB | 11 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5788) CPU | percent | 10 | 174.733 | 170.997 | 177.234 | 170.997 | 17.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5788) rss_mb | MB | 11 | 108.920 | 106.246 | 112.766 | 112.766 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5788) main thread run-queue wait | percent | 10 | 57.436 | 49.288 | 73.509 | 56.775 | 5.790110 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5788) vms_mb | MB | 11 | 332.497 | 330.379 | 336.203 | 336.203 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5837) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5837) rss_mb | MB | 5 | 2.828 | 2.828 | 2.828 | 2.828 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5837) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5837) vms_mb | MB | 5 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5838) CPU | percent | 4 | 153.970 | 99.192 | 174.458 | 174.458 | 6.210000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5838) rss_mb | MB | 5 | 1458.990 | 9.734 | 1872.992 | 1872.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5838) main thread run-queue wait | percent | 4 | 49.451 | 9.664 | 72.433 | 72.433 | 1.994574 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5838) vms_mb | MB | 5 | 2572.666 | 13.707 | 3264.566 | 3264.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5853) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5853) rss_mb | MB | 7 | 2.617 | 2.617 | 2.617 | 2.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5853) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5853) vms_mb | MB | 7 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5854) CPU | percent | 6 | 164.185 | 125.167 | 177.210 | 171.963 | 9.930000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5854) rss_mb | MB | 7 | 1612.624 | 22.402 | 1878.391 | 1878.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5854) main thread run-queue wait | percent | 6 | 56.019 | 26.973 | 73.582 | 73.582 | 3.387401 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5854) vms_mb | MB | 7 | 2832.528 | 214.242 | 3269.738 | 3269.738 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5868) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5868) rss_mb | MB | 3 | 2.672 | 2.672 | 2.672 | 2.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5868) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5868) vms_mb | MB | 3 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5869) CPU | percent | 2 | 143.103 | 111.052 | 175.155 | 175.155 | 2.890000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5869) rss_mb | MB | 3 | 1252.056 | 14.145 | 1871.012 | 1871.012 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5869) main thread run-queue wait | percent | 2 | 39.301 | 12.336 | 66.266 | 66.266 | 0.794058 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5869) vms_mb | MB | 3 | 2243.780 | 207.566 | 3261.887 | 3261.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5883) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5883) rss_mb | MB | 5 | 2.664 | 2.664 | 2.664 | 2.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5883) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5883) vms_mb | MB | 5 | 3.848 | 3.848 | 3.848 | 3.848 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5884) CPU | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5884) rss_mb | MB | 5 | 22.801 | 22.801 | 22.801 | 22.801 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5884) main thread run-queue wait | percent | 4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5884) vms_mb | MB | 5 | 28.332 | 28.332 | 28.332 | 28.332 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5916) CPU | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5916) rss_mb | MB | 7 | 2.637 | 2.637 | 2.637 | 2.637 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5916) main thread run-queue wait | percent | 6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5916) vms_mb | MB | 7 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5917) CPU | percent | 6 | 163.156 | 112.113 | 175.203 | 173.072 | 9.860000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5917) rss_mb | MB | 7 | 1608.533 | 8.863 | 1875.645 | 1875.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5917) main thread run-queue wait | percent | 6 | 49.802 | 14.227 | 68.119 | 56.856 | 3.009964 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5917) vms_mb | MB | 7 | 2801.979 | 13.574 | 3267.543 | 3267.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5937) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5937) rss_mb | MB | 6 | 2.684 | 2.684 | 2.684 | 2.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5937) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 5937) vms_mb | MB | 6 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5938) CPU | percent | 5 | 159.451 | 111.055 | 174.387 | 172.083 | 8.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5938) rss_mb | MB | 6 | 1570.874 | 14.453 | 1882.672 | 1882.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5938) main thread run-queue wait | percent | 5 | 49.433 | 16.915 | 73.313 | 51.452 | 2.492829 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 5938) vms_mb | MB | 6 | 2762.740 | 208.871 | 3274.508 | 3274.508 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6014) CPU | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6014) rss_mb | MB | 22 | 2.684 | 2.684 | 2.684 | 2.684 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6014) main thread run-queue wait | percent | 21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6014) vms_mb | MB | 22 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6015) CPU | percent | 21 | 26.541 | 0.000 | 172.883 | 0.000 | 5.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6015) rss_mb | MB | 22 | 1907.233 | 1886.434 | 2284.750 | 1889.559 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6015) main thread run-queue wait | percent | 21 | 8.916 | 0.000 | 67.964 | 0.000 | 1.884462 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6015) vms_mb | MB | 22 | 3307.343 | 3278.074 | 3832.750 | 3282.645 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6037) CPU | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6037) rss_mb | MB | 10 | 2.621 | 2.621 | 2.621 | 2.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6037) main thread run-queue wait | percent | 9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6037) vms_mb | MB | 10 | 3.852 | 3.852 | 3.852 | 3.852 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6038) CPU | percent | 9 | 169.799 | 156.722 | 175.807 | 161.130 | 15.400000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6038) rss_mb | MB | 10 | 1741.757 | 1551.410 | 2146.746 | 1776.832 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6038) main thread run-queue wait | percent | 9 | 50.845 | 38.016 | 65.841 | 44.172 | 4.612060 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6038) vms_mb | MB | 10 | 3248.654 | 2939.477 | 4065.480 | 4065.480 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6102) CPU | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6102) rss_mb | MB | 15 | 2.680 | 2.680 | 2.680 | 2.680 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6102) main thread run-queue wait | percent | 14 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6102) vms_mb | MB | 15 | 3.988 | 3.988 | 3.988 | 3.988 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6103) CPU | percent | 14 | 170.280 | 149.805 | 176.516 | 172.023 | 24.010000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6103) rss_mb | MB | 15 | 1589.070 | 15.855 | 1929.371 | 1779.574 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6103) main thread run-queue wait | percent | 14 | 49.900 | 32.393 | 72.423 | 49.580 | 7.035870 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6103) vms_mb | MB | 15 | 2894.927 | 209.102 | 3396.539 | 3154.324 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6155) rss_mb | MB | 1 | 2.887 | 2.887 | 2.887 | 2.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — bash (PID 6155) vms_mb | MB | 1 | 3.992 | 3.992 | 3.992 | 3.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6156) rss_mb | MB | 1 | 279.590 | 279.590 | 279.590 | 279.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-opencode_0000_0000 — python stdin (PID 6156) vms_mb | MB | 1 | 2863.086 | 2863.086 | 2863.086 | 2863.086 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 CPU | percent | 15418 | 37.252 | 24.532 | 208.945 | 104.288 | 5778.586941 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 15418 | 1.213 | 0.027 | 50.374 | 4.491 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 15418 | 1.563 | 0.027 | 72.704 | 7.158 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_full_pct | percent of wall time stalled | 15418 | 0.007 | 0.000 | 36.833 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io_psi_some_pct | percent of wall time stalled | 15418 | 0.007 | 0.000 | 36.833 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io read MB/s | MB/s | 15418 | 0.011 | 0.000 | 29.977 | 0.000 | 167.507812 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 io write MB/s | MB/s | 15418 | 0.020 | 0.000 | 85.217 | 0.000 | 314.613281 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory | MB | 15419 | 1140.645 | 34.176 | 2857.766 | 1391.785 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_full_pct | percent of wall time stalled | 15418 | 0.000 | 0.000 | 3.136 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 memory_psi_some_pct | percent of wall time stalled | 15418 | 0.000 | 0.000 | 3.136 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net rx MB/s | MB/s | 15418 | 0.002 | 0.000 | 11.593 | 0.000 | 26.857862 MB | n/a |
| sandbox sandbox_agent_lsb-opencode_0000_0000 net tx MB/s | MB/s | 15418 | 0.000 | 0.000 | 0.065 | 0.000 | 0.509185 MB | n/a |
| workload total CPU | percent | 15419 | 11.200 | 1.328 | 181.400 | 3.650 | 1742.752237 CPU seconds | n/a |
| workload total memory | MB | 15420 | 9153.835 | 8460.211 | 11195.289 | 9817.508 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
