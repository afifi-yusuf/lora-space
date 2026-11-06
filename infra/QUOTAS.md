# GPU quota and capacity status

Accounts: AWS `173796169264` (Warply, IAM user `warply-cli`); Azure "Azure subscription 1" (Microsoft for Startups).

## AWS EC2 vCPU quotas (as of 2026-11-06)

| Region | G (L4/L40S/A10G) On-Demand | P (H100) On-Demand | Open requests |
|---|---:|---:|---|
| us-east-1 | 8 | 16 | G → 24: case 179391130400463 |
| us-east-2 | 0 | 16 (approved 2026-11-06) | — |
| us-west-2 | 0 | 16 (approved 2026-11-06) | — |
| eu-north-1 | 0 | 16 (approved 2026-11-06) | — |

Past G requests took 11–14 days; a P request (us-east-1 → 16) took 1 day. Spot quotas for G and P are 0 outside
us-east-1 G (8).

`p5.4xlarge` (1× H100) is offered in us-east-1 (6 AZs), us-east-2, us-west-2, eu-west-2, eu-central-1, eu-north-1,
ap-northeast-1, ap-southeast-2, sa-east-1. H200 is only sold as 8-GPU `p5e/p5en.48xlarge` (192 vCPUs).

**Capacity (2026-11-05):** no on-demand `p5.4xlarge` capacity in any us-east-1 AZ (21+ rounds); no `g6e` capacity in
us-east-1. Capacity Block offer: 1× H100 for 24 h from 2026-11-29, $143.28.

Approval confirmed 2026-11-06 by launch probes: all three regions now return InsufficientInstanceCapacity (not
VcpuLimitExceeded). `infra/launch_retry.sh` covers us-east-1, us-east-2, us-west-2 and eu-north-1 (set `REGIONS`); each
region has DLAMI 20261102, an SSH security group `warply-gpu-ssh` and key pair `warply-gpu`
(local `~/.ssh/warply-gpu-<region>.pem`). **Capacity (2026-11-06 14:55 UTC):** no p5.4xlarge in any of the 16 AZs.

## Azure

All GPU VM families have 0 quota (checked East US, East US 2, West US 3, South Central US). Auto-approval for
`Standard NCadsH100v5 Family vCPUs` → 40 (East US) was declined ("ContactSupport"); the support API needs a paid
plan (subscription is on Developer), so the request is being filed manually in the portal.
