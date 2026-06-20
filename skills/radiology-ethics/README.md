# radiology-ethics

**Stage 2 — Data & Annotation.** The human-subjects governance counterpart to `radiology-data`:
Ethics, Informed-Consent, and privacy/sharing text that is compliant and honestly bounded.

## What it does

- **Approval & consent** — study-type framing (retrospective/prospective/registered/
  multi-center), IRB/ethics-committee name, number and date (placeholders, never fabricated),
  consent obtained vs documented waiver and its basis, per-center approvals.
- **Re-identification risk read** — DICOM metadata, burned-in pixel PHI, facial reconstruction
  (defacing), dates/ages, small/rare-disease cohorts, and genomic data; mitigations for each.
- **Governance & sharing** — HIPAA/GDPR/PIPL framing, data-use agreements, controlled access,
  and a consistency check so the Ethics text matches the Data Availability promise.
- **Submission-ready statements** + a 待确认 list of author/IRB-only facts.

## Trigger examples

- "帮我写伦理审批、知情同意豁免和隐私表述。"
- "Retrospective multi-center study — how do I word the consent waiver?"
- "We have imaging + genomic data — what's the re-identification risk and how do we share it?"

## Reference files

| File | Use |
|---|---|
| `references/approval-consent.md` | Study-type → consent model; approval statement templates |
| `references/reidentification-risk.md` | Risk sources + mitigations; genomics note |
| `references/governance-sharing.md` | HIPAA/GDPR/PIPL, DUAs, access tiers, consistency check |

## Handoffs

`radiology-data` (de-id mechanics, repositories, availability statements) ·
`radiology-radiogenomics` (controlled genomics) · `radiology-reporting` (open-science items) ·
`radiology-grant` (ethics/feasibility framing).

Drafting and risk-flagging support — **not legal advice**. Confirm all approvals, consent, and
DUAs with your institution/IRB.
