---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-01
title: Appendix A canonical text
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_title: Simulation Protocol v0.3
protocol_tab_id: t.0
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
H_Protocol: PENDING
H_AppA: PENDING
byte_count: PENDING
content_sha256: PENDING_AFTER_COMPLETION
created_at_utc: PENDING
completed_at_utc: PENDING
---

# Purpose

Freeze the exact Appendix A source bytes that control every Q2 holonomy, sector, and validation statement. This scaffold is not evidence of a pass.

# Canonical extraction

- Start anchor: `Appendix A — Three-Axis Fixed-Holonomy Sector Construction`.
- End anchor: the final Appendix A execution-gate formula immediately before `Appendix B — Frozen Execution, Blinding, Size-Admissibility, and Provenance Card`.
- Required sections: A.0 through A.10, once each and in order.
- Encoding: UTF-8, LF line endings, final LF, no index annotations or renderer metadata.
- Source identity: native Google Doc ID, tab ID, revision ID, extraction command/version, and byte count must be recorded above.

# Completion record

| Field | Value |
| --- | --- |
| Extracted file | PENDING |
| Start index | PENDING |
| End index | PENDING |
| Section-order check | NOT RUN |
| Suggestions/control check | NOT RUN |
| H_AppA recomputation | NOT RUN |

# Pass rule

Set `status: FROZEN` only if the anchors are unique, A.0–A.10 are complete and ordered, no unresolved suggestion changes the extracted text, the stored bytes rehash to `H_AppA`, and the manifest points to the same document revision. Any missing section, ambiguous anchor, revision mismatch, or hash mismatch is `FAIL — APPENDIX A CANONICAL TEXT NOT FROZEN` and blocks `H_Execution`.
