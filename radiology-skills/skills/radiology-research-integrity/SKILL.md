---
name: radiology-research-integrity
description: "Audit authorship, COI, AI use, selective reporting and artifact integrity; not misconduct adjudication."
---

# Radiology Research Integrity

Use this skill to audit responsible research conduct across proposals, protocols, analyses,
manuscripts, figures, presentations and published records. It owns the **integrity classification
and evidence-preservation packet**. It does not decide whether misconduct occurred, investigate a
person, contact an institution or publisher, or replace an authorized research-integrity process.

## Non-negotiable classification boundary

Use exactly one of these labels for each concern:

- `OBSERVATION` — a directly inspected record, file property, version difference or attributed
  statement, described without motive or accusation;
- `INTEGRITY_SIGNAL` — an evidence-anchored inconsistency or pattern that needs clarification,
  provenance reconstruction or independent review;
- `ALLEGATION` — an attributed assertion that prohibited conduct occurred; preserve who made it,
  when and in what record, but never restate it as fact;
- `INSTITUTIONAL_FINDING` — a document-verified determination issued by an authorized institution,
  funder, regulator, court or publisher. Record its issuer, scope, date, status and exact source.

Do not upgrade one state to another from visual suspicion, model output, similarity software,
anonymous commentary, author silence or persuasive language. Honest error and disagreement remain
possible until the authorized process determines otherwise.

## Choose the mode

| Mode | Use when | Required result |
|---|---|---|
| `triage` | a possible integrity concern is raised with limited material | bounded classification, preservation actions, missing records and safe next owner |
| `authorship-disclosure` | authorship, CRediT, acknowledgements, COI, sponsor role or AI use is disputed or incomplete | versioned contribution/disclosure ledger and unresolved author decisions |
| `provenance-audit` | text, data, code, statistical output, images or figures may not trace to their source | transformation chain, discrepancies, claim impact and repair/escalation gate |
| `publication-correction` | a preprint, article, abstract, repository or deck may require correction, notice or withdrawal | publication-state map and evidence packet for the authorized publisher/institution |
| `institutional-handoff` | an integrity signal or allegation needs formal local handling | minimal factual handoff, preserved records, confidentiality boundary and no verdict |

For the classification and escalation rules read
[references/evidence-states-and-escalation.md](references/evidence-states-and-escalation.md).
For authorship, CRediT, COI, sponsor and AI-use questions read
[references/authorship-disclosure-and-selective-reporting.md](references/authorship-disclosure-and-selective-reporting.md).
For data, text, code, DICOM and figure provenance or publication correction read
[references/provenance-and-publication-record.md](references/provenance-and-publication-record.md).
Use [references/source-registry.md](references/source-registry.md) to verify the authority and
currency of policy-facing claims; local and venue rules still require live verification.

## Input passport

Record before judging:

`request and mode | artifact IDs/versions/digests | study and Claim IDs | public/submitted/private
state | institution/jurisdiction/funder/venue | applicable policy and access date | people and roles
named by supplied records | evidence locators | confidentiality/access constraints | current safety
or publication risk | user authority for any file or external action`.

Unknown identities, intent, authorship eligibility, contribution, consent, approval, provenance or
policy applicability remain `NOT_VERIFIED`. Review is read-only unless the user explicitly requests
an in-scope artifact edit. Never upload confidential manuscripts or evidence to an external service
without authority.

## Required workflow

1. **Freeze the review surface.** Inventory exact versions, preserve originals and hashes where
   available, and separate public records from confidential material. Do not ask the user to alter
   or delete the source record.
2. **Classify, do not accuse.** Write atomic rows as `OBSERVATION`, `INTEGRITY_SIGNAL`, `ALLEGATION`
   or `INSTITUTIONAL_FINDING`; include source, alternative explanations and what would resolve it.
3. **Audit the relevant chain.** Reconcile authorship/contribution/disclosures; protocol and
   registration to analysis and reporting; raw data to derived values; source images/DICOM to
   panels; code/config/run to statistics; preprint to version of record and later notices.
4. **Apply the radiology gate.** Preserve original pixel/DICOM identity and document window/level,
   crop, orientation, laterality, resampling, intensity adjustment, annotation, compositing and AI
   generation/editing. A display transformation is not automatically improper; an undocumented or
   selectively applied transformation is an integrity signal, not a finding.
5. **Assess claim and safety impact.** State which result, participant protection, clinical claim,
   grant, publication or downstream artifact may be affected. Do not infer intent.
6. **Choose repair or escalation.** Ordinary provenance gaps may be repaired with records,
   correction and transparent disclosure. Potential fabrication, falsification, plagiarism,
   retaliation, active participant risk, evidence destruction or a material public-record problem
   triggers `STOP_AND_ESCALATE` to the authorized owner.
7. **Prepare the bounded packet.** Use
   [templates/integrity-audit-report.md](templates/integrity-audit-report.md) and, when relevant,
   [templates/authorship-coi-ai-ledger.md](templates/authorship-coi-ai-ledger.md). Preserve neutral
   language, access controls, provenance and unresolved alternatives.

## Stop and escalation gates

Return `STOP_AND_ESCALATE` when evidence may be destroyed or altered; confidential records cannot be
handled safely; participant, animal or public safety may be affected; a protected test or source
record has been overwritten; a material publication claim is unreliable; retaliation or coercion is
reported; or a formal allegation requires institutional procedure. Name the **role**, not an invented
person: research-integrity officer, institutional counsel, IRB/ethics owner, data-protection owner,
funder or publisher as applicable.

The skill may organize evidence and draft a factual handoff. It must not interview witnesses,
determine intent, declare guilt/innocence, impose sanctions, promise confidentiality beyond the
actual channel, or issue a correction/retraction itself.

## Output contract

1. `Audit scope and passport`
2. `Concern ledger` — stable ID, four-state classification, exact evidence and alternative
   explanations
3. `Authorship/CRediT/COI/sponsor/AI ledger` when applicable
4. `Text-data-code-image provenance map` — source, transformation, output and Claim IDs
5. `Selective-reporting and protocol-to-report comparison`
6. `Radiology display-integrity gate` — original image/DICOM, transformations, laterality and PHI
7. `Claim, participant and public-record impact`
8. `Repair / STOP_AND_ESCALATE decision` — authorized owner and required evidence, never a verdict
9. `Publication-record action options` — correction, retraction or notice remain publisher decisions
10. `Unresolved author/institution inputs and confidentiality limits`

## Handoffs and non-ownership

- Human/animal/biosafety approval, consent and authorized conduct -> `radiology-ethics`.
- DICOM de-identification, data stewardship, access and sharing -> `radiology-data`.
- Statistical validity or selective model evaluation -> `radiology-stats` /
  `radiology-method-evaluation`; whole-manuscript validity -> `radiology-prereview`.
- Citation support and retraction-status checking -> `radiology-citation`; upload package and forms
  -> `radiology-submission`; reviewer response -> `radiology-response`.
- Frozen executable packaging, prespecified tolerance and independent same-input replay ->
  `radiology-reproducibility`; this skill owns neutral classification and escalation when missing,
  altered or selectively reported run evidence creates an integrity signal, not the replay verdict.
- Institution, funder and publisher retain investigative, adjudicative and publication authority.
