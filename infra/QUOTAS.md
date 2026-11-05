# GPU quota and capacity status

Accounts: AWS `173796169264` (Warply, IAM user `warply-cli`); Azure "Azure subscription 1" (Microsoft for Startups).

## AWS EC2 vCPU quotas (as of 2026-11-05)

| Region | G (L4/L40S/A10G) On-Demand | P (H100) On-Demand | Open requests |
|---|---:|---:|---|
| us-east-1 | 8 | 16 | G → 24: case 179391130400463 |
| us-east-2 | 0 | 0 | P → 16: case 179391862800892 |
| us-west-2 | 0 | 0 | P → 16: case 179391869300068 |
| eu-north-1 | 0 | 0 | P → 16: case 179391874500384 |

Past G requests took 11–14 days; a P request (us-east-1 → 16) took 1 day. Spot quotas for G and P are 0 outside
us-east-1 G (8).

`p5.4xlarge` (1× H100) is offered in us-east-1 (6 AZs), us-east-2, us-west-2, eu-west-2, eu-central-1, eu-north-1,
ap-northeast-1, ap-southeast-2, sa-east-1. H200 is only sold as 8-GPU `p5e/p5en.48xlarge` (192 vCPUs).

**Capacity (2026-11-05):** no on-demand `p5.4xlarge` capacity in any us-east-1 AZ (21+ rounds); no `g6e` capacity in
us-east-1. Capacity Block offer: 1× H100 for 24 h from 2026-11-29, $143.28.

Launching in a new region needs that region's DLAMI ID, a key pair (`warply-gpu` exists in us-east-1; a
`warply-gpu-us-east-2` key exists locally) and an SSH security group — `infra/launch_retry.sh` is us-east-1 only.

## Azure

All GPU VM families have 0 quota (checked East US, East US 2, West US 3, South Central US). Auto-approval for
`Standard NCadsH100v5 Family vCPUs` → 40 (East US) was declined ("ContactSupport"); the support API needs a paid
plan (subscription is on Developer), so the request is being filed manually in the portal.
