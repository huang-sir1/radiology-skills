---
name: radiology-ethics
description: "Write compliant, non-overstated Ethics, Informed-Consent, and privacy/governance text for imaging and imaging+omics studies — study-type framing (retrospective, prospective, registered, multi-center), IRB/ethics-committee approval and numbers, consent vs documented waiver, re-identification risk (DICOM metadata, rare-disease small cohorts, genomic data), and the human-subjects governance behind data sharing (HIPAA/GDPR/PIPL, data-use agreements, controlled access). Use when the user mentions ethics, IRB, ethics committee, informed consent, consent waiver, \"伦理\", \"知情同意\", \"隐私\", HIPAA, GDPR, PIPL, data-use agreement, or needs the Ethics/Consent statement for a manuscript or grant. Produces submission-ready statements and a re-identification risk read. Never fabricates approval numbers, dates, or consent status."
---

# Research Ethics, Consent & Privacy

Use this skill to write the **Ethics**, **Informed Consent**, and **privacy/governance** parts of
an imaging (or imaging+omics) manuscript or grant so they are compliant and honestly bounded.
This is the governance counterpart to `radiology-data` (which handles the mechanics of
de-identification, repositories, and availability statements). This skill frames the *human-
subjects* side: approvals, consent, re-identification risk, and what may lawfully be shared.

## Core stance

- **State the approval, don't invent it.** Ethics-committee/IRB name, approval number, and date,
  plus the consent status, come from the author. Use placeholders; never fabricate them.
- **Consent must match the design.** Retrospective studies often have a **documented waiver** of
  consent; prospective studies need consent (and a consent process described). Say which, and on
  what basis the waiver was granted.
- **Re-identification is a spectrum.** DICOM metadata, dates, rare-disease small cohorts, facial
  reconstruction from head imaging, and genomic data each raise risk; address them specifically.
- **Sharing is governed, not automatic.** Imaging may be openly shareable after de-identification;
  genomic/clinical data are often **controlled access**. The Ethics/consent must permit whatever
  the Data Availability statement promises (keep them consistent with `radiology-data`).
- **Jurisdiction matters.** HIPAA (US), GDPR (EU), PIPL (China) and local rules differ; name the
  framework that applies and defer specifics to the institution.
- **Integrity & scope.** This is drafting and risk-flagging support, **not legal advice**;
  approval numbers, consent terms, and DUAs must be confirmed with the institution/IRB.

## When to use

- "Write the Ethics / Informed Consent / privacy statement / 帮我写伦理与知情同意表述。"
- "Retrospective multi-center study — how do I word the consent waiver?"
- "We have genomic + imaging data — what's the re-identification risk and how do I share it?"
- "Which approval/consent text does a grant or _Radiology_ submission need?"
- "Is 'available on reasonable request' acceptable, and what governance must back it?"

## When to open extra files

| File | Open when |
|---|---|
| [references/approval-consent.md](references/approval-consent.md) | Study-type framing, IRB/ethics approval, consent vs waiver, multi-center approvals, registration |
| [references/reidentification-risk.md](references/reidentification-risk.md) | Assessing/мitigating re-identification: DICOM metadata, dates, small cohorts, defacing, genomic data |
| [references/governance-sharing.md](references/governance-sharing.md) | HIPAA/GDPR/PIPL framing, data-use agreements, controlled access, aligning consent ↔ Data Availability |

## Workflow

1. **Classify the study** — retrospective / prospective / registered / multi-center; secondary
   use of existing data; involvement of imaging, clinical records, pathology, genomics.
2. **Establish approvals & consent** (approval-consent.md) — committee, number, date (placeholders
   if unknown), consent obtained vs documented waiver and its basis; per-center approvals.
3. **Assess re-identification risk** (reidentification-risk.md) — what in the data could
   re-identify a participant, and the mitigations (de-id, defacing, aggregation, controlled
   access). Coordinate de-id mechanics with `radiology-data`.
4. **Set governance for sharing** (governance-sharing.md) — what may be public vs controlled vs
   restricted, the applicable framework, DUA needs; ensure it **matches** the Data Availability
   statement.
5. **Draft statements** — Ethics, Informed Consent, and (if needed) a privacy/governance note,
   in submission-ready English, with a 待确认 list of author-only facts.

## Output contract

1. **`Study/ethics classification`** — design, data types, jurisdiction/framework.
2. **`Ethics statement`** — committee, approval number, date (placeholders where unknown).
3. **`Consent statement`** — consent obtained or documented waiver + basis; prospective process
   if applicable.
4. **`Re-identification risk read`** — risks + mitigations; defacing/controlled-access decisions.
5. **`Governance/sharing note`** — what can be shared and how, consistent with `radiology-data`.
6. **`待确认（中文）`** — approval numbers, dates, consent terms, DUA details to confirm with the IRB.

## Quality bar

A good ethics section is specific, consistent with the data-sharing plan, and never claims an
approval, consent, or shareability the study does not actually have. It reads like an
investigator who knows the governance — and flags exactly what only the IRB can confirm.

## Handoffs

- De-identification mechanics, repositories, Data/Code Availability statements → `radiology-data`.
- Controlled-cohort design (dbGaP/EGA), matched imaging+omics governance → `radiology-radiogenomics`.
- Ethics/open-science checklist items (CLAIM/TRIPOD+AI) → `radiology-reporting`.
- Grant ethics/feasibility framing → `radiology-grant`.
- Not legal advice — confirm all approvals, consent, and DUAs with your institution/IRB.
