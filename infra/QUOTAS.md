# GPU quota and capacity status

Accounts: AWS `173796169264` (Warply, IAM user `warply-cli`); Azure "Azure subscription 1" (Microsoft for Startups).

## AWS EC2 vCPU quotas (as of 2026-11-06)

| Region | G (L4/L40S/A10G) On-Demand | P (H100) On-Demand | Open requests |
|---|---:|---:|---|
| us-east-1 | 24 (approved 2026-11-06) | 16 | — |
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

**2026-11-11 (checked in the console; the CLI user cannot read Service Quotas):** G applied values are us-east-1 24
(8 in use), us-east-2 0, us-west-2 0, eu-north-1 0. Filed us-east-1 G 24 -> 48 (pending). Earlier G history in
us-east-1: 48 requested Sep 3 (closed), 8 Oct 8, 24 Nov 5 (granted Nov 6). The same account has Bedrock token quotas
raised for Claude Fable 5.1 (10M TPM) and Opus 5.5 (30M TPM), granted Oct 7: a possible route to Fable.

## Azure

All GPU VM families have 0 quota in every region (re-checked 2026-11-06 via the VM usage and Quota APIs).
Case 2611050010002129 (NCCads H100 v5 → 40 and NDsr H100 v5 → 40, East US; filed 2026-11-05) was **declined**
2026-11-06: Microsoft for Startups subscriptions get no new GPU allocations, with no escalation. The suggested route is
a pay-as-you-go or Enterprise subscription. Note: a 40-vCPU NDsr limit could not start any ND H100 v5 VM anyway (the
smallest, ND96isr, needs 96 vCPUs); only NCC40ads_H100_v5 (1× H100) would fit 40.
