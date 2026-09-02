---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-11
title: Source commit, build environment, run inventory, and execution-gate manifest
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Source identity

| Field | Value |
| --- | --- |
| repository URL/identity | PENDING |
| immutable source commit | PENDING |
| source tree clean | NOT RUN |
| submodule/lockfile hashes | PENDING |
| build command | PENDING |
| test command | PENDING |
| executable SHA-256 | PENDING |

# Build and runtime environment

Record OS image and kernel, architecture, CPU model/flags, compiler and linker versions/flags, math and RNG library versions, dependency lockfile, container/image digest, environment variables affecting numerics, threading/MPI settings, filesystem/endian assumptions, and floating-point mode. Every value and supporting file hash is PENDING.

# Frozen execution inventory

The machine-readable inventory must include every Stage A–C row and, at minimum: stage, model, representation, ensemble, P1/P2/P3 point, L, exact J, exact h_6, chain bank, eight-chain count, seed tuple digest, thermalization, production length, measurement cadence, expected core-hours, output URI, and parent hashes. It must include Q2 `L={48,64,96,128,160,192}` and Q3 `h_6={-0.005,-0.0025,0,+0.0025,+0.005}` without omission.

| Inventory field | Value |
| --- | --- |
| inventory URI | PENDING |
| H_Inventory | PENDING |
| row count | PENDING |
| duplicate-key check | NOT RUN |
| missing-grid check | NOT RUN |
| no-selective-removal check | NOT RUN |

# Resource forecast

| Gate | Value |
| --- | --- |
| `C_max` | 20,000 physical CPU core-hours |
| `C_forecast` | PENDING |
| required forecast ceiling | `C_forecast<=14,000` |
| reserve | PENDING; must be at least 6,000 |
| row-for-row reconciliation | NOT RUN |
| H_Pilot | PENDING |
| H_Forecast | PENDING |

# A.10 artifact manifest

The byte counts and hashes below identify the current scaffold files only. They are not completion hashes and must be replaced when evidence populates a file.

| ID | Filename | Required final state | Current state | Byte count | SHA-256 |
| --- | --- | --- | --- | --- | --- |
| A10-01 | `01_appendix_a_canonical_text.md` | FROZEN | NOT RUN | 1888 | `5ec95b8b836ad418e12f21d75354d6aca28390725cf790800c1315c16028be88` |
| A10-02 | `02_frozen_geometry_specification.md` | FROZEN | NOT RUN | 2165 | `3af79a57f873e99d583236e3a9a22495f55798436a1dbb1297f7c4f6da57a800` |
| A10-03 | `03_transition_acceptance_table.md` | FROZEN | NOT RUN | 3017 | `2c7f1449b9e14bb73747cde19a575b98a1549d6c767217a999ad464d63e5ccef` |
| A10-04 | `04_algebra_invariant_test_report.md` | PASS | NOT RUN | 1940 | `71ea55ab770c95c458633c21d705a8e5dce13ee2af2f9953da0f1e5e7c202b02` |
| A10-05 | `05_small_volume_enumeration_and_tail_certificate.md` | PASS | NOT RUN | 2231 | `5fb3cb3695dc06ce237d6b063c624aeb1c045b07cf288bb85528527ad5af84a1` |
| A10-06 | `06_eight_sector_transform_table.md` | PASS | NOT RUN | 1907 | `01b734f430bfcf960a55d6806923e5583de9008928d0508939a8bd8dce6227fc` |
| A10-07 | `07_partition_ratio_validation_report.md` | PASS | NOT RUN | 2237 | `51e4e161b115cc8bef4afc72ed239c07c43fd91b159f5cf9dcbcd58ccd40ead4` |
| A10-08 | `08_detailed_balance_reachability_report.md` | PASS | NOT RUN | 2257 | `c148167a789719cdd70100fa489dddb809bf54b10be452b136fc37afefdc3418` |
| A10-09 | `09_blind_mixing_roundtrip_pilot_report.md` | PASS | NOT RUN | 3197 | `64e78a82ca305d0b8817480c99852a4337ddb4bfb07c8ec09911e424b667e53c` |
| A10-10 | `10_ckt_axial_mapping_comparator_report.md` | PASS | NOT RUN | 2082 | `cf7936002692b3f5d2a81a355cb62fa00300eee9f73698ecb90c9a9b13a4ffba` |
| A10-11 | `11_source_commit_build_environment_manifest.md` | FROZEN | NOT RUN | PENDING | PENDING |

# Provenance chain

`H_Theory -> H_Protocol -> H_AppA -> H_AppB -> H_AppBAmend -> H_Inventory -> H_Pilot -> H_Forecast -> H_Execution`

| Node | Hash | Parent(s) verified | State |
| --- | --- | --- | --- |
| H_Theory | PENDING | NOT RUN | PENDING |
| H_Protocol | PENDING | NOT RUN | PENDING |
| H_AppA | PENDING | NOT RUN | PENDING |
| H_AppB | PENDING | NOT RUN | PENDING |
| H_AppBAmend/null amendment | PENDING | NOT RUN | PENDING |
| H_Inventory | PENDING | NOT RUN | PENDING |
| H_Pilot | PENDING | NOT RUN | PENDING |
| H_Forecast | PENDING | NOT RUN | PENDING |
| H_Execution | FORBIDDEN_WHILE_PENDING | NOT RUN | BLOCKED |

# Final gate evaluation

Set `status: FROZEN` only after source/build fields contain no `PENDING`, the complete inventory and forecast reconcile and pass, artifacts A10-01 through A10-10 have their required final states and rehash correctly, and the full lineage verifies. A missing field, dirty/unidentified source, environment gap, inventory omission, forecast above 14,000, artifact failure, or hash mismatch is `FAIL — EXECUTION MANIFEST INCOMPLETE`; `H_Execution` must not be created.

Current result: `BLOCKED — SCAFFOLD ONLY; VALIDATION NOT RUN`.
