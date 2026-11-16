# agprof summary

- Duration: **2022.892 s**
- Runs: **1/1 completed**, 1 succeeded, 0 failed, 0 interrupted
- Completed throughput: **0.000 runs/s**
- LLM: **46 calls**, 46 succeeded, 0 failed, 0 interrupted, n/a reported retries, 1859.880 s total wait
- Tools: **48/49 completed**, 0 failed, 1 interrupted
- Automatic Python calls: **disabled**
- Raw resource samples: **187319** at 1.98 Hz effective (1 Hz configured)
- GPU sampling: **available** (requested)

## Run, LLM, and tool metrics

| Metric | Value |
|---|---:|
| Run latency p50 / p95 | 2022821.138 / 2022821.138 ms |
| LLM latency p50 / p95 | 34622.747 / 97156.220 ms |
| LLM TTFT p50 / p95 | 17345.095 / 21428.804 ms |
| LLM input / output tokens | 4458434 / 76519 |
| LLM output throughput | n/a tokens/s |
| LLM attempts | 46 total, 46 succeeded, 0 failed, 0 interrupted |
| Tool latency p50 / p95 | n/a / n/a ms |

### Tool outcomes


### Coverage

Tool latency percentiles include exact intervals only; other timings are separated in JSON.
Unknown tool outcomes: 0. Missing measurements are not zero.
Resources are sampled; per-process GPU power is estimated. Telemetry is not lossless.
Telemetry errors: {"unmatched_completions": 1}
- codex: {"automatic_functions": "disabled", "llm": "host_observed", "reason": "External harness internals require cooperative events; no transcript timing inference.", "retries": "container_reported", "tools": "admission_completion_boundaries", "turns": "unavailable"}
| Tool | Completed/started | Succeeded | Failed | Interrupted | p50 latency | p95 latency |
|---|---:|---:|---:|---:|---:|---:|
| Bash | 13/14 | 13 | 0 | 1 | n/a | n/a |
| mcp__agency__attention | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__attribution | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__commit_adapter | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__generate | 16/16 | 16 | 0 | 0 | n/a | n/a |
| mcp__agency__get_current_resources | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__inspect | 3/3 | 3 | 0 | 0 | n/a | n/a |
| mcp__agency__logit_lens | 2/2 | 2 | 0 | 0 | n/a | n/a |
| mcp__agency__patch | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__submit_output | 1/1 | 1 | 0 | 0 | n/a | n/a |
| mcp__agency__trace | 3/3 | 3 | 0 | 0 | n/a | n/a |
| update_plan | 5/5 | 5 | 0 | 0 | n/a | n/a |

## Workload aggregate

| CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write |
|---:|---:|---:|---:|---:|---:|---:|
| 5.129% | 101.700% | 103.885 s | 9073.399 MB | 10394.074 MB | n/a MB | n/a MB |

## Per-process metrics

| Process | PID | Sandbox | Samples | CPU avg | CPU peak | CPU time | RSS avg | RSS peak | VMS avg | VMS peak | Disk read | Disk write |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| docker-buildx | 7499 |  | 1 | n/a% | n/a% | n/a s | 30.137 MB | 30.137 MB | 1361.711 MB | 1361.711 MB | n/a MB | n/a MB |
| VLLM::EngineCor | 7379 |  | 2012 | 2.893% | 52.678% | 58.590 s | 2324.504 MB | 2324.613 MB | 21205.011 MB | 21205.184 MB | 0.000000 MB | 0.011719 MB |
| docker | 7489 |  | 1 | n/a% | n/a% | n/a s | 29.293 MB | 29.293 MB | 1915.523 MB | 1915.523 MB | n/a MB | n/a MB |
| python | 7378 |  | 2012 | 0.000% | 0.000% | 0.000 s | 12.148 MB | 12.148 MB | 19.605 MB | 19.605 MB | 0.000000 MB | 0.000000 MB |
| vllm | 7344 |  | 2012 | 0.246% | 6.959% | 4.980 s | 1775.802 MB | 1776.027 MB | 11012.754 MB | 11017.801 MB | 0.007812 MB | 0.066406 MB |
| python | 7339 |  | 2012 | 1.973% | 101.130% | 39.940 s | 3064.579 MB | 4075.824 MB | 16259.190 MB | 18061.473 MB | 71.734375 MB | 1634.484375 MB |
| lsb_grid_worker | 4781 |  | 2012 | 0.000% | 0.000% | 0.000 s | 3.312 MB | 3.312 MB | 7.570 MB | 7.570 MB | 0.000000 MB | 0.000000 MB |
| bash | 7717 | sandbox_agent_lsb-codex_0000_0000 | 2010 | 24.732% | 99.113% | 499.610 s | 112.630 MB | 118.223 MB | 971.354 MB | 977.148 MB | n/a MB | n/a MB |
| tail | 7627 | sandbox_agent_lsb-codex_0000_0000 | 2010 | 0.002% | 0.996% | 0.050 s | 1.250 MB | 1.250 MB | 2.883 MB | 2.883 MB | n/a MB | n/a MB |
| docker-init | 7595 | sandbox_agent_lsb-codex_0000_0000 | 2010 | 0.002% | 0.996% | 0.040 s | 0.551 MB | 0.551 MB | 1.039 MB | 1.039 MB | n/a MB | n/a MB |
| python3 | 7723 | sandbox_agent_lsb-codex_0000_0000 | 2 | 59.654% | 59.654% | 0.600 s | 35.877 MB | 52.297 MB | 43.320 MB | 61.016 MB | n/a MB | n/a MB |
| codex | 7740 | sandbox_agent_lsb-codex_0000_0000 | 1987 | 2.135% | 20.873% | 42.650 s | 139.066 MB | 147.973 MB | 382.750 MB | 490.910 MB | n/a MB | n/a MB |
| git | 7775 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.031 MB | 3.031 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git-remote-http | 7778 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 10.375 MB | 10.375 MB | 93.027 MB | 93.027 MB | n/a MB | n/a MB |
| git | 7770 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.152 MB | 3.152 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git | 7814 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.156 MB | 3.156 MB | 6.812 MB | 6.812 MB | n/a MB | n/a MB |
| git-remote-http | 7815 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.922 MB | 17.922 MB | 100.590 MB | 100.590 MB | n/a MB | n/a MB |
| git | 7813 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.543 MB | 3.543 MB | 14.816 MB | 14.816 MB | n/a MB | n/a MB |
| git | 7818 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.617 MB | 4.617 MB | 8.285 MB | 8.285 MB | n/a MB | n/a MB |
| git | 7831 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 28.934 MB | 28.934 MB | 35.672 MB | 35.672 MB | n/a MB | n/a MB |
| python3 | 7856 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.676 MB | 14.676 MB | 20.016 MB | 20.016 MB | n/a MB | n/a MB |
| python3 | 7921 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.348 MB | 21.348 MB | 27.074 MB | 27.074 MB | n/a MB | n/a MB |
| find | 7933 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.660 MB | 2.660 MB | 4.934 MB | 4.934 MB | n/a MB | n/a MB |
| bash | 7932 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.922 MB | 2.922 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| head | 7934 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 1.449 MB | 1.449 MB | 2.859 MB | 2.859 MB | n/a MB | n/a MB |
| bash | 7951 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.066 MB | 3.066 MB | 4.402 MB | 4.402 MB | n/a MB | n/a MB |
| python | 7962 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.426 MB | 8.426 MB | 13.055 MB | 13.055 MB | n/a MB | n/a MB |
| python | 7953 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.320 MB | 12.320 MB | 16.434 MB | 16.434 MB | n/a MB | n/a MB |
| python3 | 7997 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.855 MB | 8.855 MB | 13.410 MB | 13.410 MB | n/a MB | n/a MB |
| python3 | 8016 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.102 MB | 5.102 MB | 11.512 MB | 11.512 MB | n/a MB | n/a MB |
| python3 | 8039 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.496 MB | 21.496 MB | 27.059 MB | 27.059 MB | n/a MB | n/a MB |
| python3 | 8154 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 14.453 MB | 14.453 MB | 19.887 MB | 19.887 MB | n/a MB | n/a MB |
| bash | 8173 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 0.000 MB | 0.000 MB | 1.617 MB | 1.617 MB | n/a MB | n/a MB |
| python | 8273 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 11.688 MB | 11.688 MB | 15.227 MB | 15.227 MB | n/a MB | n/a MB |
| bash | 8272 | sandbox_agent_lsb-codex_0000_0000 | 6 | 0.000% | 0.000% | 0.000 s | 2.977 MB | 2.977 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python | 8306 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.242 MB | 12.242 MB | 16.348 MB | 16.348 MB | n/a MB | n/a MB |
| python | 8310 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.281 MB | 8.281 MB | 13.051 MB | 13.051 MB | n/a MB | n/a MB |
| python | 8344 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.320 MB | 12.320 MB | 16.348 MB | 16.348 MB | n/a MB | n/a MB |
| python | 8348 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 4.285 MB | 4.285 MB | 10.000 MB | 10.000 MB | n/a MB | n/a MB |
| python | 8376 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 12.445 MB | 12.445 MB | 16.348 MB | 16.348 MB | n/a MB | n/a MB |
| python | 8383 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 5.504 MB | 5.504 MB | 11.641 MB | 11.641 MB | n/a MB | n/a MB |
| python | 8417 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.754 MB | 8.754 MB | 13.211 MB | 13.211 MB | n/a MB | n/a MB |
| python | 8407 | sandbox_agent_lsb-codex_0000_0000 | 2 | 2.980% | 2.980% | 0.030 s | 12.516 MB | 12.613 MB | 16.471 MB | 16.516 MB | n/a MB | n/a MB |
| python | 8454 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 8.961 MB | 8.961 MB | 13.188 MB | 13.188 MB | n/a MB | n/a MB |
| python3 | 8468 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.270 MB | 7.270 MB | 11.789 MB | 11.789 MB | n/a MB | n/a MB |
| python3 | 8523 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.469 MB | 21.469 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python3 | 8567 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 20.926 MB | 20.926 MB | 25.762 MB | 25.762 MB | n/a MB | n/a MB |
| python3 | 8576 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.918 MB | 9.918 MB | 13.664 MB | 13.664 MB | n/a MB | n/a MB |
| python3 | 8578 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.426 MB | 21.426 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| bash | 8591 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.938 MB | 2.938 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python | 8593 | sandbox_agent_lsb-codex_0000_0000 | 2 | 97.180% | 97.180% | 0.980 s | 62.729 MB | 102.641 MB | 174.469 MB | 213.902 MB | n/a MB | n/a MB |
| python3 | 8605 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 17.621 MB | 17.621 MB | 22.938 MB | 22.938 MB | n/a MB | n/a MB |
| python3 | 8617 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 16.621 MB | 16.621 MB | 22.109 MB | 22.109 MB | n/a MB | n/a MB |
| bash | 8681 | sandbox_agent_lsb-codex_0000_0000 | 3 | 0.000% | 0.000% | 0.000 s | 2.836 MB | 2.836 MB | 4.262 MB | 4.262 MB | n/a MB | n/a MB |
| python | 8683 | sandbox_agent_lsb-codex_0000_0000 | 3 | 118.863% | 143.171% | 2.440 s | 272.951 MB | 688.512 MB | 530.201 MB | 966.652 MB | n/a MB | n/a MB |
| python | 8770 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.555 MB | 7.555 MB | 11.918 MB | 11.918 MB | n/a MB | n/a MB |
| bash | 8744 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 2.836 MB | 2.836 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 8801 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 7.391 MB | 7.391 MB | 11.922 MB | 11.922 MB | n/a MB | n/a MB |
| python | 8812 | sandbox_agent_lsb-codex_0000_0000 | 2 | 94.397% | 94.397% | 0.950 s | 77.277 MB | 136.531 MB | 244.566 MB | 359.227 MB | n/a MB | n/a MB |
| bash | 8811 | sandbox_agent_lsb-codex_0000_0000 | 2 | 0.000% | 0.000% | 0.000 s | 2.762 MB | 2.762 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 8825 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 9.191 MB | 9.191 MB | 13.488 MB | 13.488 MB | n/a MB | n/a MB |
| python3 | 8833 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 21.629 MB | 21.629 MB | 26.992 MB | 26.992 MB | n/a MB | n/a MB |
| python | 8855 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 22.297 MB | 22.297 MB | 133.926 MB | 133.926 MB | n/a MB | n/a MB |
| bash | 8854 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 3.125 MB | 3.125 MB | 4.258 MB | 4.258 MB | n/a MB | n/a MB |
| python3 | 8923 | sandbox_agent_lsb-codex_0000_0000 | 1 | n/a% | n/a% | n/a s | 18.562 MB | 18.562 MB | 24.383 MB | 24.383 MB | n/a MB | n/a MB |
| docker | 8996 |  | 19 | 0.000% | 0.000% | 0.000 s | 30.312 MB | 30.312 MB | 1843.270 MB | 1843.270 MB | 0.000000 MB | 0.000000 MB |
| docker | 9046 |  | 1 | n/a% | n/a% | n/a s | 30.359 MB | 30.359 MB | 1843.770 MB | 1843.770 MB | n/a MB | n/a MB |

## GPU metrics

| GPU | Util avg | Util peak | VRAM avg | VRAM peak | Power avg | Power peak | Energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 4.290% | 100.000% | 11986.616 MB | 12590.000 MB | 31.562 W | 74.475 W | 63825.990 J |

## Sandbox metrics

| Sandbox | CPU avg | CPU peak | CPU time | Memory avg | Memory peak | Disk read | Disk write | Net receive | Net transmit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sandbox_agent_lsb-codex_0000_0000 | 28.090% | 182.679% | 567.555 s | 550.063 MB | 1202.559 MB | 217.511719 MB | 359.808594 MB | 24.959245 MB | 1.609874 MB |

## Incomplete spans

| Label | Thread | Elapsed at stop (s) | Outcome |
|---|---:|---:|---|
| orchestrator:scheduler | 7487 | 2022.826 | interrupted |
| tool:Bash | -1 | 326.537 | interrupted |
| harness:retire | -1 | 0.372 | interrupted |

## Span metrics

| Label | Completed/started | Failed | Interrupted | Wall (s) | CPU (s) | Blocked (s) | Disk read (MB) | Mean (ms) | p50 (ms) | p95 (ms) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| run:write_lora_adapter | 1/1 | 0 | 0 | 2022.821 | n/a | n/a | 217.512 | 2022821.138 | 2022821.138 | 2022821.138 |
| sync:result_wait | 1/1 | 0 | 0 | 2022.821 | 0.000 | 2022.820 | 217.512 | 2022820.522 | 2022820.522 | 2022820.522 |
| engine:execute | 1/1 | 0 | 0 | 2022.820 | 2.680 | 2020.137 | 217.512 | 2022819.522 | 2022819.522 | 2022819.522 |
| harness:attempt_rpc | 1/1 | 0 | 0 | 1997.885 | 0.004 | 1997.882 | 173.802 | 1997885.281 | 1997885.281 | 1997885.281 |
| harness:await_cli | 1/1 | 0 | 0 | 1994.406 | n/a | n/a | 51.213 | 1994405.795 | 1994405.795 | 1994405.795 |
| llm:attempt | 46/46 | 0 | 0 | 1859.880 | 7.150 | 1852.725 | 11.996 | 40432.164 | 34622.747 | 97156.220 |
| tool:Bash | 13/14 | 0 | 1 | 439.442 | n/a | n/a | 32.093 | 33803.201 | 807.931 | 141866.608 |
| tool:mcp__agency__generate | 16/16 | 0 | 0 | 85.918 | n/a | n/a | 0.443 | 5369.849 | 4485.568 | 11876.068 |
| run:container_call | 13/13 | 0 | 0 | 19.783 | 0.002 | 19.781 | 0.000 | 1521.767 | 36.146 | 7763.156 |
| teardown:commit | 1/1 | 0 | 0 | 19.307 | 0.004 | 19.303 | 0.000 | 19307.399 | 19307.399 | 19307.399 |
| sandbox:commit | 1/1 | 0 | 0 | 19.104 | 0.002 | 19.101 | 0.000 | 19103.763 | 19103.763 | 19103.763 |
| checkpoint.total | 1/1 | 0 | 0 | 19.104 | 0.002 | 19.101 | 0.000 | 19103.609 | 19103.609 | 19103.609 |
| checkpoint.fs_snapshot | 1/1 | 0 | 0 | 19.103 | 0.002 | 19.101 | 0.000 | 19103.462 | 19103.462 | 19103.462 |
| tool:mcp__agency__trace | 3/3 | 0 | 0 | 8.754 | n/a | n/a | 0.000 | 2917.924 | 3569.585 | 3868.957 |
| sandbox:ensure_daemon | 1/1 | 0 | 0 | 4.183 | 1.019 | 3.164 | 42.494 | 4182.910 | 4182.910 | 4182.910 |
| runtime.harness_start | 1/1 | 0 | 0 | 4.183 | 1.019 | 3.164 | 42.489 | 4182.626 | 4182.626 | 4182.626 |
| tool:mcp__agency__logit_lens | 2/2 | 0 | 0 | 3.935 | n/a | n/a | 0.000 | 1967.262 | 1967.262 | 2000.133 |
| harness:submit | 1/1 | 0 | 0 | 1.412 | n/a | n/a | 30.910 | 1412.083 | 1412.083 | 1412.083 |
| tool:mcp__agency__inspect | 3/3 | 0 | 0 | 1.391 | n/a | n/a | 0.000 | 463.642 | 508.102 | 518.406 |
| harness:startup_ready | 1/1 | 0 | 0 | 1.226 | n/a | n/a | 75.493 | 1225.622 | 1225.622 | 1225.622 |
| syscall:execve | 874/874 | 0 | 0 | 1.214 | n/a | n/a | 6.371 | 1.389 | 1.170 | 2.512 |
| sandbox:create | 1/1 | 0 | 0 | 1.142 | 0.249 | 0.893 | 0.000 | 1141.559 | 1141.559 | 1141.559 |
| syscall:connect | 464/464 | 0 | 0 | 1.093 | n/a | n/a | 5.207 | 2.355 | 2.078 | 4.549 |
| tool:update_plan | 5/5 | 0 | 0 | 0.916 | n/a | n/a | 0.438 | 183.199 | 191.863 | 199.612 |
| syscall:sendto | 356/356 | 0 | 0 | 0.832 | n/a | n/a | 3.553 | 2.336 | 2.137 | 4.180 |
| harness:snapshot | 1/1 | 0 | 0 | 0.791 | n/a | n/a | 0.126 | 791.088 | 791.088 | 791.088 |
| tool:mcp__agency__patch | 1/1 | 0 | 0 | 0.459 | n/a | n/a | 0.000 | 459.143 | 459.143 | 459.143 |
| run:detect | 1/1 | 0 | 0 | 0.439 | 0.001 | 0.439 | 0.000 | 439.456 | 439.456 | 439.456 |
| sandbox:start | 1/1 | 0 | 0 | 0.408 | 0.002 | 0.406 | 0.000 | 408.491 | 408.491 | 408.491 |
| runtime.container_create | 1/1 | 0 | 0 | 0.408 | 0.002 | 0.406 | 0.000 | 408.350 | 408.350 | 408.350 |
| tool:mcp__agency__attention | 1/1 | 0 | 0 | 0.392 | n/a | n/a | 0.000 | 391.520 | 391.520 | 391.520 |
| tool:mcp__agency__commit_adapter | 1/1 | 0 | 0 | 0.326 | n/a | n/a | 0.000 | 325.560 | 325.560 | 325.560 |
| tool:mcp__agency__attribution | 1/1 | 0 | 0 | 0.305 | n/a | n/a | 0.000 | 304.535 | 304.535 | 304.535 |
| tool:mcp__agency__get_current_resources | 1/1 | 0 | 0 | 0.237 | n/a | n/a | 0.000 | 236.571 | 236.571 | 236.571 |
| tool:mcp__agency__submit_output | 1/1 | 0 | 0 | 0.222 | n/a | n/a | 0.000 | 222.041 | 222.041 | 222.041 |
| sandbox:stop | 1/1 | 0 | 0 | 0.203 | 0.002 | 0.202 | 0.000 | 203.395 | 203.395 | 203.395 |
| agency:services_close | 1/1 | 0 | 0 | 0.140 | 0.000 | 0.139 | 0.000 | 139.892 | 139.892 | 139.892 |
| agency:services_start | 1/1 | 0 | 0 | 0.091 | 0.045 | 0.047 | 0.000 | 91.056 | 91.056 | 91.056 |
| harness:launch | 1/1 | 0 | 0 | 0.051 | n/a | n/a | 1.773 | 50.686 | 50.686 | 50.686 |
| agent:create | 1/1 | 0 | 0 | 0.050 | 0.009 | 0.041 | 0.000 | 49.954 | 49.954 | 49.954 |
| syscall:bind | 7/7 | 0 | 0 | 0.019 | n/a | n/a | 0.498 | 2.753 | 3.041 | 3.904 |
| agency:decode_harness_result | 1/1 | 0 | 0 | 0.004 | 0.004 | 0.000 | 0.000 | 3.931 | 3.931 | 3.931 |
| sync:submission | 1/1 | 0 | 0 | 0.001 | 0.000 | 0.001 | 0.000 | 1.229 | 1.229 | 1.229 |
| sync:container | 13/13 | 0 | 0 | 0.001 | 0.001 | 0.000 | 0.000 | 0.069 | 0.062 | 0.109 |
| sync:scheduler_queue | 1/1 | 0 | 0 | 0.000 | n/a | n/a | 0.000 | 0.172 | 0.172 | 0.172 |
| resolve | 1/1 | 0 | 0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.050 | 0.050 |
| harness:retire | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |
| orchestrator:scheduler | 0/1 | 0 | 1 | 0.000 | n/a | n/a | n/a | n/a | n/a | n/a |

## Resource metrics

| Metric | Unit | Samples | Mean | Min | Max | Last | Total | Energy |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| dockerd CPU | percent | 2010 | 0.408 | 0.029 | 53.291 | 53.291 | 8.250512 CPU seconds | n/a |
| GPU 0 memory | MB | 2012 | 11986.616 | 11670.000 | 12590.000 | 12006.000 | n/a | n/a |
| GPU 0 power | W | 2012 | 31.562 | 29.234 | 74.475 | 29.416 | n/a | 63825.990 J |
| GPU 0 proc / 7339-478857 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 memory | MB | 2012 | 3203.693 | 3118.000 | 3770.000 | 3186.000 | n/a | n/a |
| GPU 0 proc / 7339-478857 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 estimated power | W | 1166 | 0.589 | 0.000 | 69.855 | 0.000 | n/a | n/a |
| GPU 0 proc / 7339-478857 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 utilization | percent | 1166 | 0.443 | 0.000 | 87.000 | 0.000 | n/a | n/a |
| GPU 0 proc / 7379-481514 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 memory | MB | 2012 | 8300.923 | 8070.000 | 8338.000 | 8338.000 | n/a | n/a |
| GPU 0 proc / 7379-481514 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 estimated power | W | 826 | 7.125 | 0.000 | 74.475 | 0.000 | n/a | n/a |
| GPU 0 proc / 7379-481514 / sandbox / ~ / device / GPU-76e8db0c-a181-bd83-94a1-6e56e1b444b3 utilization | percent | 826 | 9.533 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| GPU 0 processes memory | MB | 2012 | 11504.616 | 11188.000 | 12108.000 | 11524.000 | n/a | n/a |
| GPU 0 utilization | percent | 2012 | 4.290 | 0.000 | 100.000 | 0.000 | n/a | n/a |
| host cpu_count | CPUs | 2012 | 4.000 | 4.000 | 4.000 | 4.000 | n/a | n/a |
| host cpu_psi_some_pct | percent of wall time stalled | 2011 | 0.620 | 0.115 | 14.209 | 3.920 | n/a | n/a |
| host cpu_util_pct | percent of all host CPUs | 2011 | 8.104 | 2.057 | 50.250 | 16.449 | n/a | n/a |
| host disk_read_mb_s | MB/s | 2011 | 0.734 | 0.000 | 200.979 | 8.676 | n/a | n/a |
| host disk_write_mb_s | MB/s | 2011 | 1.014 | 0.000 | 235.760 | 2.374 | n/a | n/a |
| host io_psi_full_pct | percent of wall time stalled | 2011 | 0.484 | 0.000 | 76.507 | 19.302 | n/a | n/a |
| host io_psi_some_pct | percent of wall time stalled | 2011 | 0.498 | 0.000 | 76.734 | 19.893 | n/a | n/a |
| host mem_total_mb | MB | 2012 | 15363.547 | 15363.547 | 15363.547 | 15363.547 | n/a | n/a |
| host mem_used_mb | MB | 2012 | 7133.419 | 6667.531 | 8171.102 | 7348.523 | n/a | n/a |
| host memory_psi_full_pct | percent of wall time stalled | 2011 | 0.091 | 0.000 | 77.804 | 0.000 | n/a | n/a |
| host memory_psi_some_pct | percent of wall time stalled | 2011 | 0.091 | 0.000 | 78.033 | 0.000 | n/a | n/a |
| host net_rx_mb_s | MB/s | 2011 | 0.017 | 0.000 | 15.872 | 0.000 | n/a | n/a |
| host net_tx_mb_s | MB/s | 2011 | 0.014 | 0.000 | 1.026 | 0.000 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4781) CPU | percent | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| bash lsb_grid_worker.sh (PID 4781) io read MB/s | MB/s | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4781) io write MB/s | MB/s | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| bash lsb_grid_worker.sh (PID 4781) rss_mb | MB | 2012 | 3.312 | 3.312 | 3.312 | 3.312 | n/a | n/a |
| bash lsb_grid_worker.sh (PID 4781) main thread run-queue wait | percent | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| bash lsb_grid_worker.sh (PID 4781) vms_mb | MB | 2012 | 7.570 | 7.570 | 7.570 | 7.570 | n/a | n/a |
| Agency harness — python -m lsbench (PID 7339) CPU | percent | 2011 | 1.973 | 0.000 | 101.130 | 0.995 | 39.940000 CPU seconds | n/a |
| Agency harness — python -m lsbench (PID 7339) io read MB/s | MB/s | 2011 | 0.035 | 0.000 | 67.946 | 0.000 | 71.734375 MB | n/a |
| Agency harness — python -m lsbench (PID 7339) io write MB/s | MB/s | 2011 | 0.807 | 0.016 | 859.685 | 0.023 | 1634.484375 MB | n/a |
| Agency harness — python -m lsbench (PID 7339) rss_mb | MB | 2012 | 3064.579 | 2529.605 | 4075.824 | 3408.621 | n/a | n/a |
| Agency harness — python -m lsbench (PID 7339) main thread run-queue wait | percent | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Agency harness — python -m lsbench (PID 7339) vms_mb | MB | 2012 | 16259.190 | 14094.793 | 18061.473 | 16845.375 | n/a | n/a |
| Python — vllm (PID 7344) CPU | percent | 2011 | 0.246 | 0.000 | 6.959 | 0.000 | 4.980000 CPU seconds | n/a |
| Python — vllm (PID 7344) io read MB/s | MB/s | 2011 | 0.000 | 0.000 | 0.004 | 0.000 | 0.007812 MB | n/a |
| Python — vllm (PID 7344) io write MB/s | MB/s | 2011 | 0.000 | 0.000 | 0.008 | 0.000 | 0.066406 MB | n/a |
| Python — vllm (PID 7344) rss_mb | MB | 2012 | 1775.802 | 1774.402 | 1776.027 | 1776.027 | n/a | n/a |
| Python — vllm (PID 7344) main thread run-queue wait | percent | 2011 | 0.004 | 0.000 | 0.574 | 0.000 | 0.088975 run-queue seconds | n/a |
| Python — vllm (PID 7344) vms_mb | MB | 2012 | 11012.754 | 10945.781 | 11017.801 | 11017.801 | n/a | n/a |
| Python — python -c (PID 7378) CPU | percent | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| Python — python -c (PID 7378) io read MB/s | MB/s | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 7378) io write MB/s | MB/s | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| Python — python -c (PID 7378) rss_mb | MB | 2012 | 12.148 | 12.148 | 12.148 | 12.148 | n/a | n/a |
| Python — python -c (PID 7378) main thread run-queue wait | percent | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| Python — python -c (PID 7378) vms_mb | MB | 2012 | 19.605 | 19.605 | 19.605 | 19.605 | n/a | n/a |
| VLLM::EngineCore (PID 7379) CPU | percent | 2011 | 2.893 | 0.000 | 52.678 | 0.995 | 58.590000 CPU seconds | n/a |
| VLLM::EngineCore (PID 7379) io read MB/s | MB/s | 2011 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| VLLM::EngineCore (PID 7379) io write MB/s | MB/s | 2011 | 0.000 | 0.000 | 0.004 | 0.000 | 0.011719 MB | n/a |
| VLLM::EngineCore (PID 7379) rss_mb | MB | 2012 | 2324.504 | 2324.113 | 2324.613 | 2324.613 | n/a | n/a |
| VLLM::EngineCore (PID 7379) main thread run-queue wait | percent | 2011 | 0.004 | 0.000 | 0.563 | 0.000 | 0.071469 run-queue seconds | n/a |
| VLLM::EngineCore (PID 7379) vms_mb | MB | 2012 | 21205.011 | 21204.168 | 21205.184 | 21205.168 | n/a | n/a |
| docker info (PID 7489) rss_mb | MB | 1 | 29.293 | 29.293 | 29.293 | 29.293 | n/a | n/a |
| docker info (PID 7489) vms_mb | MB | 1 | 1915.523 | 1915.523 | 1915.523 | 1915.523 | n/a | n/a |
| docker-buildx (PID 7499) rss_mb | MB | 1 | 30.137 | 30.137 | 30.137 | 30.137 | n/a | n/a |
| docker-buildx (PID 7499) vms_mb | MB | 1 | 1361.711 | 1361.711 | 1361.711 | 1361.711 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 7595) CPU | percent | 2009 | 0.002 | 0.000 | 0.996 | 0.000 | 0.040000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 7595) rss_mb | MB | 2010 | 0.551 | 0.551 | 0.551 | 0.551 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 7595) main thread run-queue wait | percent | 2009 | 0.000 | 0.000 | 0.004 | 0.000 | 0.000515 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — docker-init (PID 7595) vms_mb | MB | 2010 | 1.039 | 1.039 | 1.039 | 1.039 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7627) CPU | percent | 2009 | 0.002 | 0.000 | 0.996 | 0.000 | 0.050000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7627) rss_mb | MB | 2010 | 1.250 | 1.250 | 1.250 | 1.250 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7627) main thread run-queue wait | percent | 2009 | 0.000 | 0.000 | 0.060 | 0.000 | 0.001144 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — tail (PID 7627) vms_mb | MB | 2010 | 2.883 | 2.883 | 2.883 | 2.883 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7717) CPU | percent | 2009 | 24.732 | 0.000 | 99.113 | 0.000 | 499.610000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7717) rss_mb | MB | 2010 | 112.630 | 2.750 | 118.223 | 114.340 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7717) main thread run-queue wait | percent | 2009 | 0.000 | 0.000 | 0.006 | 0.000 | 0.000108 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7717) vms_mb | MB | 2010 | 971.354 | 4.262 | 977.148 | 973.566 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7723) CPU | percent | 1 | 59.654 | 59.654 | 59.654 | 59.654 | 0.600000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7723) rss_mb | MB | 2 | 35.877 | 19.457 | 52.297 | 52.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7723) main thread run-queue wait | percent | 1 | 0.032 | 0.032 | 0.032 | 0.032 | 0.000318 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7723) vms_mb | MB | 2 | 43.320 | 25.625 | 61.016 | 61.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7740) CPU | percent | 1986 | 2.135 | 0.000 | 20.873 | 4.974 | 42.650000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7740) rss_mb | MB | 1987 | 139.066 | 22.801 | 147.973 | 142.312 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7740) main thread run-queue wait | percent | 1986 | 0.000 | 0.000 | 0.004 | 0.000 | 0.000081 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — codex (PID 7740) vms_mb | MB | 1987 | 382.750 | 310.961 | 490.910 | 392.043 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7770) rss_mb | MB | 1 | 3.152 | 3.152 | 3.152 | 3.152 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7770) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 7775) rss_mb | MB | 1 | 3.031 | 3.031 | 3.031 | 3.031 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 7775) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 7778) rss_mb | MB | 1 | 10.375 | 10.375 | 10.375 | 10.375 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 7778) vms_mb | MB | 1 | 93.027 | 93.027 | 93.027 | 93.027 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7813) rss_mb | MB | 1 | 3.543 | 3.543 | 3.543 | 3.543 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7813) vms_mb | MB | 1 | 14.816 | 14.816 | 14.816 | 14.816 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 7814) rss_mb | MB | 1 | 3.156 | 3.156 | 3.156 | 3.156 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git remote-https (PID 7814) vms_mb | MB | 1 | 6.812 | 6.812 | 6.812 | 6.812 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 7815) rss_mb | MB | 1 | 17.922 | 17.922 | 17.922 | 17.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git-remote-https (PID 7815) vms_mb | MB | 1 | 100.590 | 100.590 | 100.590 | 100.590 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 7818) rss_mb | MB | 1 | 4.617 | 4.617 | 4.617 | 4.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git (PID 7818) vms_mb | MB | 1 | 8.285 | 8.285 | 8.285 | 8.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7831) rss_mb | MB | 1 | 28.934 | 28.934 | 28.934 | 28.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — git safe.bareRepository=explicit (PID 7831) vms_mb | MB | 1 | 35.672 | 35.672 | 35.672 | 35.672 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7856) rss_mb | MB | 1 | 14.676 | 14.676 | 14.676 | 14.676 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7856) vms_mb | MB | 1 | 20.016 | 20.016 | 20.016 | 20.016 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7921) rss_mb | MB | 1 | 21.348 | 21.348 | 21.348 | 21.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7921) vms_mb | MB | 1 | 27.074 | 27.074 | 27.074 | 27.074 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7932) rss_mb | MB | 1 | 2.922 | 2.922 | 2.922 | 2.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7932) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 7933) rss_mb | MB | 1 | 2.660 | 2.660 | 2.660 | 2.660 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — find (PID 7933) vms_mb | MB | 1 | 4.934 | 4.934 | 4.934 | 4.934 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 7934) rss_mb | MB | 1 | 1.449 | 1.449 | 1.449 | 1.449 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — head (PID 7934) vms_mb | MB | 1 | 2.859 | 2.859 | 2.859 | 2.859 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7951) rss_mb | MB | 1 | 3.066 | 3.066 | 3.066 | 3.066 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 7951) vms_mb | MB | 1 | 4.402 | 4.402 | 4.402 | 4.402 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 7953) rss_mb | MB | 1 | 12.320 | 12.320 | 12.320 | 12.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 7953) vms_mb | MB | 1 | 16.434 | 16.434 | 16.434 | 16.434 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7962) rss_mb | MB | 1 | 8.426 | 8.426 | 8.426 | 8.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 7962) vms_mb | MB | 1 | 13.055 | 13.055 | 13.055 | 13.055 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7997) rss_mb | MB | 1 | 8.855 | 8.855 | 8.855 | 8.855 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 7997) vms_mb | MB | 1 | 13.410 | 13.410 | 13.410 | 13.410 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8016) rss_mb | MB | 1 | 5.102 | 5.102 | 5.102 | 5.102 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8016) vms_mb | MB | 1 | 11.512 | 11.512 | 11.512 | 11.512 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8039) rss_mb | MB | 1 | 21.496 | 21.496 | 21.496 | 21.496 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8039) vms_mb | MB | 1 | 27.059 | 27.059 | 27.059 | 27.059 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8154) rss_mb | MB | 1 | 14.453 | 14.453 | 14.453 | 14.453 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8154) vms_mb | MB | 1 | 19.887 | 19.887 | 19.887 | 19.887 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8173) rss_mb | MB | 1 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8173) vms_mb | MB | 1 | 1.617 | 1.617 | 1.617 | 1.617 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8272) CPU | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8272) rss_mb | MB | 6 | 2.977 | 2.977 | 2.977 | 2.977 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8272) main thread run-queue wait | percent | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8272) vms_mb | MB | 6 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8273) rss_mb | MB | 1 | 11.688 | 11.688 | 11.688 | 11.688 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8273) vms_mb | MB | 1 | 15.227 | 15.227 | 15.227 | 15.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8306) rss_mb | MB | 1 | 12.242 | 12.242 | 12.242 | 12.242 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8306) vms_mb | MB | 1 | 16.348 | 16.348 | 16.348 | 16.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8310) rss_mb | MB | 1 | 8.281 | 8.281 | 8.281 | 8.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8310) vms_mb | MB | 1 | 13.051 | 13.051 | 13.051 | 13.051 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8344) rss_mb | MB | 1 | 12.320 | 12.320 | 12.320 | 12.320 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8344) vms_mb | MB | 1 | 16.348 | 16.348 | 16.348 | 16.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8348) rss_mb | MB | 1 | 4.285 | 4.285 | 4.285 | 4.285 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8348) vms_mb | MB | 1 | 10.000 | 10.000 | 10.000 | 10.000 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8376) rss_mb | MB | 1 | 12.445 | 12.445 | 12.445 | 12.445 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8376) vms_mb | MB | 1 | 16.348 | 16.348 | 16.348 | 16.348 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8383) rss_mb | MB | 1 | 5.504 | 5.504 | 5.504 | 5.504 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8383) vms_mb | MB | 1 | 11.641 | 11.641 | 11.641 | 11.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8407) CPU | percent | 1 | 2.980 | 2.980 | 2.980 | 2.980 | 0.030000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8407) rss_mb | MB | 2 | 12.516 | 12.418 | 12.613 | 12.613 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8407) main thread run-queue wait | percent | 1 | 0.005 | 0.005 | 0.005 | 0.005 | 0.000055 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — probes.py (PID 8407) vms_mb | MB | 2 | 16.471 | 16.426 | 16.516 | 16.516 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8417) rss_mb | MB | 1 | 8.754 | 8.754 | 8.754 | 8.754 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8417) vms_mb | MB | 1 | 13.211 | 13.211 | 13.211 | 13.211 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8454) rss_mb | MB | 1 | 8.961 | 8.961 | 8.961 | 8.961 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python -c (PID 8454) vms_mb | MB | 1 | 13.188 | 13.188 | 13.188 | 13.188 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8468) rss_mb | MB | 1 | 7.270 | 7.270 | 7.270 | 7.270 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8468) vms_mb | MB | 1 | 11.789 | 11.789 | 11.789 | 11.789 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8523) rss_mb | MB | 1 | 21.469 | 21.469 | 21.469 | 21.469 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8523) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8567) rss_mb | MB | 1 | 20.926 | 20.926 | 20.926 | 20.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8567) vms_mb | MB | 1 | 25.762 | 25.762 | 25.762 | 25.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8576) rss_mb | MB | 1 | 9.918 | 9.918 | 9.918 | 9.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8576) vms_mb | MB | 1 | 13.664 | 13.664 | 13.664 | 13.664 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8578) rss_mb | MB | 1 | 21.426 | 21.426 | 21.426 | 21.426 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8578) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8591) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8591) rss_mb | MB | 2 | 2.938 | 2.938 | 2.938 | 2.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8591) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8591) vms_mb | MB | 2 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 8593) CPU | percent | 1 | 97.180 | 97.180 | 97.180 | 97.180 | 0.980000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 8593) rss_mb | MB | 2 | 62.729 | 22.816 | 102.641 | 102.641 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 8593) main thread run-queue wait | percent | 1 | 0.046 | 0.046 | 0.046 | 0.046 | 0.000467 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — weights.py (PID 8593) vms_mb | MB | 2 | 174.469 | 135.035 | 213.902 | 213.902 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8605) rss_mb | MB | 1 | 17.621 | 17.621 | 17.621 | 17.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8605) vms_mb | MB | 1 | 22.938 | 22.938 | 22.938 | 22.938 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8617) rss_mb | MB | 1 | 16.621 | 16.621 | 16.621 | 16.621 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8617) vms_mb | MB | 1 | 22.109 | 22.109 | 22.109 | 22.109 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8681) CPU | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8681) rss_mb | MB | 3 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8681) main thread run-queue wait | percent | 2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8681) vms_mb | MB | 3 | 4.262 | 4.262 | 4.262 | 4.262 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — diagnose.py (PID 8683) CPU | percent | 2 | 118.863 | 94.556 | 143.171 | 143.171 | 2.440000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — diagnose.py (PID 8683) rss_mb | MB | 3 | 272.951 | 36.984 | 688.512 | 93.355 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — diagnose.py (PID 8683) main thread run-queue wait | percent | 2 | 10.804 | 10.203 | 11.405 | 10.203 | 0.221270 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — diagnose.py (PID 8683) vms_mb | MB | 3 | 530.201 | 256.668 | 966.652 | 367.281 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8744) rss_mb | MB | 1 | 2.836 | 2.836 | 2.836 | 2.836 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8744) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8770) rss_mb | MB | 1 | 7.555 | 7.555 | 7.555 | 7.555 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8770) vms_mb | MB | 1 | 11.918 | 11.918 | 11.918 | 11.918 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8801) rss_mb | MB | 1 | 7.391 | 7.391 | 7.391 | 7.391 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8801) vms_mb | MB | 1 | 11.922 | 11.922 | 11.922 | 11.922 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8811) CPU | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8811) rss_mb | MB | 2 | 2.762 | 2.762 | 2.762 | 2.762 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8811) main thread run-queue wait | percent | 1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8811) vms_mb | MB | 2 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8812) CPU | percent | 1 | 94.397 | 94.397 | 94.397 | 94.397 | 0.950000 CPU seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8812) rss_mb | MB | 2 | 77.277 | 18.023 | 136.531 | 136.531 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8812) main thread run-queue wait | percent | 1 | 4.248 | 4.248 | 4.248 | 4.248 | 0.042748 run-queue seconds | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8812) vms_mb | MB | 2 | 244.566 | 129.906 | 359.227 | 359.227 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8825) rss_mb | MB | 1 | 9.191 | 9.191 | 9.191 | 9.191 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8825) vms_mb | MB | 1 | 13.488 | 13.488 | 13.488 | 13.488 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8833) rss_mb | MB | 1 | 21.629 | 21.629 | 21.629 | 21.629 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8833) vms_mb | MB | 1 | 26.992 | 26.992 | 26.992 | 26.992 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8854) rss_mb | MB | 1 | 3.125 | 3.125 | 3.125 | 3.125 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — bash (PID 8854) vms_mb | MB | 1 | 4.258 | 4.258 | 4.258 | 4.258 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8855) rss_mb | MB | 1 | 22.297 | 22.297 | 22.297 | 22.297 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — python stdin (PID 8855) vms_mb | MB | 1 | 133.926 | 133.926 | 133.926 | 133.926 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8923) rss_mb | MB | 1 | 18.562 | 18.562 | 18.562 | 18.562 | n/a | n/a |
| sandbox:sandbox_agent_lsb-codex_0000_0000 — agpolicy_hook.py (PID 8923) vms_mb | MB | 1 | 24.383 | 24.383 | 24.383 | 24.383 | n/a | n/a |
| docker commit (PID 8996) CPU | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 CPU seconds | n/a |
| docker commit (PID 8996) io read MB/s | MB/s | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8996) io write MB/s | MB/s | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 MB | n/a |
| docker commit (PID 8996) rss_mb | MB | 19 | 30.312 | 30.312 | 30.312 | 30.312 | n/a | n/a |
| docker commit (PID 8996) main thread run-queue wait | percent | 18 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000000 run-queue seconds | n/a |
| docker commit (PID 8996) vms_mb | MB | 19 | 1843.270 | 1843.270 | 1843.270 | 1843.270 | n/a | n/a |
| docker stop (PID 9046) rss_mb | MB | 1 | 30.359 | 30.359 | 30.359 | 30.359 | n/a | n/a |
| docker stop (PID 9046) vms_mb | MB | 1 | 1843.770 | 1843.770 | 1843.770 | 1843.770 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 CPU | percent | 2009 | 28.090 | 0.000 | 182.679 | 0.000 | 567.555340 CPU seconds | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_full_pct | percent of wall time stalled | 2009 | 0.371 | 0.000 | 11.525 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 cpu_psi_some_pct | percent of wall time stalled | 2009 | 0.385 | 0.000 | 13.611 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_full_pct | percent of wall time stalled | 2009 | 0.057 | 0.000 | 20.137 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io_psi_some_pct | percent of wall time stalled | 2009 | 0.059 | 0.000 | 20.272 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io read MB/s | MB/s | 2009 | 0.108 | 0.000 | 67.922 | 0.000 | 217.511719 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 io write MB/s | MB/s | 2009 | 0.178 | 0.000 | 168.467 | 0.000 | 359.808594 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory | MB | 2010 | 550.063 | 30.527 | 1202.559 | 523.262 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_full_pct | percent of wall time stalled | 2009 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 memory_psi_some_pct | percent of wall time stalled | 2009 | 0.000 | 0.000 | 0.000 | 0.000 | n/a | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net rx MB/s | MB/s | 2009 | 0.012 | 0.000 | 15.348 | 0.000 | 24.959245 MB | n/a |
| sandbox sandbox_agent_lsb-codex_0000_0000 net tx MB/s | MB/s | 2009 | 0.001 | 0.000 | 0.276 | 0.000 | 1.609874 MB | n/a |
| workload total CPU | percent | 2011 | 5.129 | 1.521 | 101.700 | 9.127 | 103.884758 CPU seconds | n/a |
| workload total memory | MB | 2012 | 9073.399 | 8237.508 | 10394.074 | 10108.918 | n/a | n/a |

## GPU lease metrics

_No GPU leases were recorded._
