---
name: radiology-ethics
description: "Audit IRB, consent, privacy, IACUC/IBC, biosafety and dual use; not logistics or lab execution."
---

# Research ethics, animal welfare, biosafety and governance

Use this skill as the independent governance entry point for an imaging, radiomics, imaging-omics,
or mechanism project. It handles three reviews that may apply separately or together:

1. `human-subjects` — participants, identifiable records/images, human tissue, consent, privacy and
   sharing;
2. `animal-welfare` — live-animal use, humane care, protocol scope and veterinary oversight;
3. `biosafety-biosecurity` — biological hazards, recombinant or synthetic nucleic-acid work,
   genetic manipulation, potentially infectious material and dual-use screening.

It supports planning, auditing, learner guidance, manuscript/grant drafting and submission handoff.
It does not approve research, replace the responsible committee, make a legal determination or
convert an unresolved governance gap into acceptable manuscript wording.

## Non-negotiable stance

- **The three branches are not substitutes.** One project can require IRB/ethics-committee,
  IACUC/equivalent and IBC/equivalent review in parallel. Approval in one branch does not authorize
  another branch.
- **Current local authority controls.** Committee names, jurisdiction, institutional policy,
  exemptions, approval type, training, permitted facility and responsible owner vary by institution
  and can change. Record the source and verification date; do not freeze a generic rule as local law.
- **Approval facts are author-only facts.** Committee/office, protocol number, decision, dates,
  approved species/materials/procedures/sites, consent status, amendments, containment decision,
  training and incidents must come from supplied records or the named local owner. Use explicit
  placeholders when absent.
- **Unresolved authority is a `STOP` gate.** Do not recommend starting or continuing covered work
  when an applicable approval, registration, exemption determination, local risk assessment,
  trained owner or approved scope is absent, expired, contradicted or unconfirmed.
- **Remain non-operational for hazardous work.** Screen risk and route it to authorized oversight.
  Do not supply pathogen manipulation, evasion, amplification, release, containment-workaround or
  other dangerous experimental instructions. Do not guess a containment level.
- **Writing cannot cure noncompliance.** For work already performed outside documented approval,
  stop submission-ready assurance language and route the discrepancy to the institution. Never
  invent or retroactively imply approval.
- This is research-governance and writing support, **not legal, veterinary or biosafety advice**.

## Choose an operating mode

| Mode | Use when | Required result |
|---|---|---|
| `classify` | the applicable reviews are unclear | branch map, parallel-review dependencies, responsible local owners and immediate STOP conditions |
| `audit` | protocols, letters, Methods or plans are supplied | record-to-claim comparison, scope/date conflicts, evidence states and atomic closure actions |
| `draft` | verified governance facts need manuscript/grant wording | bounded statements with placeholders and a separate author-confirmation list |
| `mentor` | a learner asks what approvals or safeguards are needed | explain why each branch applies, minimum defensible next step and who must decide; no local or hazardous SOP |
| `submission-handoff` | final declarations or response materials are being assembled | approval matrix, exact evidence anchors, unresolved blockers and wording that matches the verified records |

If the user only asks “is ethics covered?”, default to `classify`, not `draft`.

## Route before writing

| Trigger | Route | Default responsible authority |
|---|---|---|
| participants, identifiable images/records, human tissue, prospective interaction, consent, waiver, privacy or data sharing | `human-subjects` | IRB / research ethics committee / equivalent privacy-governance owner |
| live animals, animal imaging, intervention, breeding, tissue collection from study animals or welfare endpoints | `animal-welfare` | IACUC / animal ethics committee / equivalent plus veterinary programme |
| recombinant or synthetic nucleic acids, gene editing, vector use, potentially infectious specimens, biological agents/toxins, genetically modified organisms or environmental-release potential | `biosafety-biosecurity` | IBC / institutional biosafety office / equivalent |
| credible potential for methods, materials, data, models or results to be misused for high-consequence biological harm | `biosafety-biosecurity` plus dual-use escalation | designated institutional review entity, biosecurity officer and funder/regulator where applicable |

Common combined routes include human tissue with infectious potential (`human-subjects` +
`biosafety-biosecurity`), genetically modified animals (`animal-welfare` +
`biosafety-biosecurity`) and human gene-transfer research (`human-subjects` +
`biosafety-biosecurity`). Classify these as parallel obligations; never collapse them into one
approval.

Read [references/ethics-routing-and-stop-gates.md](references/ethics-routing-and-stop-gates.md)
whenever applicability is uncertain, more than one branch may apply, or a STOP decision is possible.

## Evidence states and verdicts

Use only these evidence states:

- `DOCUMENT_VERIFIED` — the supplied record directly supports the field;
- `AUTHOR_REPORTED` — supplied by the author but not document-verified;
- `UNKNOWN_AUTHOR_INPUT_NEEDED` — missing and cannot be inferred;
- `CONFLICTING` — records, dates, scope or manuscript claims disagree;
- `NOT_APPLICABLE_LOCAL_OWNER_CONFIRMED` — non-applicability or exemption was confirmed by the
  authorized local owner; absence of a document is not enough.

Return `PASS`, `CONDITIONAL` or `STOP` per branch and per planned activity. `PASS` means the supplied
record supports the described scope; it is not this skill granting approval. `CONDITIONAL` is for
non-authorizing planning or writing gaps that can be closed before execution/submission. `STOP`
applies when work or an assurance claim would outrun current verified authority.

## Branch resources

| File | Read when |
|---|---|
| [references/approval-consent.md](references/approval-consent.md) | human study design, IRB/ethics review, consent/waiver, multicentre coverage or human-tissue use |
| [references/reidentification-risk.md](references/reidentification-risk.md) | imaging/genomic re-identification and privacy risk |
| [references/governance-sharing.md](references/governance-sharing.md) | consent-to-sharing consistency, DUA and controlled access |
| [references/animal-welfare-review.md](references/animal-welfare-review.md) | animal-review scope, 3Rs, welfare endpoints, veterinary oversight and animal-use writing |
| [references/biosafety-biosecurity-review.md](references/biosafety-biosecurity-review.md) | biological-material, genetic-manipulation, pathogen and dual-use routing; never for operational instructions |

Use [templates/research-ethics-governance-matrix.md](templates/research-ethics-governance-matrix.md)
for each project. Use [templates/local-ethics-oversight-profile.md](templates/local-ethics-oversight-profile.md)
to record current institutional owners and live policy entry points; do not fill either template by
inference.

## Workflow

1. **Inventory the actual activities and artifacts.** Separate planned from completed work; list
   participants/data/tissue, animals, biological materials, genetic manipulation, sites and sharing.
2. **Classify all applicable branches.** Include combined routes and name the local decision owner
   for each. Do not self-declare an exemption.
3. **Build the governance matrix.** Record committee/office, evidence anchor, number, dates,
   approved scope, amendments, training/facility dependencies, owner and evidence state.
4. **Apply branch STOP gates.** Compare the exact planned/performed activity with current approval
   scope, dates and local determination. Treat missing, expired, conflicting or out-of-scope authority
   as STOP for the affected work or assurance claim.
5. **Check cross-branch consistency.** Verify that human consent permits tissue/genomic use and
   sharing; animal and biosafety scopes cover the same model/material/site; amendments and incidents
   are visible; no branch silently substitutes for another.
6. **Verify live local sources.** Capture jurisdiction, institution, policy URL/document/version,
   accessed date and responsible contact role. External guidance is an entry point, not proof of a
   local approval.
7. **Draft or mentor at the evidence ceiling.** Provide exact placeholders and closure questions.
   For hazardous or dual-use concerns, provide only high-level governance routing and pause detailed
   design/dissemination pending authorized review.

## Output contract

1. `Mode and activity inventory`
2. `Branch map` — `human-subjects | animal-welfare | biosafety-biosecurity`, including combined routes
3. `Governance evidence matrix` — source, scope, date, owner and evidence state
4. `PASS / CONDITIONAL / STOP verdicts` — one per branch and planned activity
5. `Atomic closure actions` — issue, criterion, minimum repair, local owner and closure evidence
6. `Drafting package` — only statements supported by supplied evidence; placeholders remain visible
7. `待作者/机构确认` — every author-only fact, conflict, live-policy check and unresolved approval
8. `Safe handoffs` — local IRB/ethics, animal ethics/veterinary, biosafety/biosecurity or legal owner

## Handoffs and boundaries

- De-identification mechanics, repositories and Data/Code Availability -> `radiology-data`.
- Mechanism experiment choice, controls and analysis design -> `radiology-experiment-design`; this
  skill returns authorization gates, not an experimental protocol.
- Cross-scale imaging-omics interpretation -> `radiology-radiogenomics`.
- Statistical design and inference -> `radiology-stats`.
- Reporting-checklist placement -> `radiology-reporting`; final declaration/file checks ->
  `radiology-submission`.
- Legal interpretation, animal clinical care, containment assignment, incident response and
  dangerous/dual-use determinations remain with current authorized local owners.

Continue helping with classification, gap documentation and safe wording after a STOP verdict, but
do not provide instructions that would enable the blocked activity.
