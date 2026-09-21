---
name: radiology-grant
description: "Develop/review radiology grants against a live call, including current NSFC rules, code/call routing, funder criteria and imaging feasibility; not papers or decks. CN: 标书、国自然、基金评审"
---

# Radiology Grant Review and Development

Use this skill for funding proposals, not for manuscript peer review or presentation production.
Treat a grant as a **call-bound argument for a consequential, answerable question and a feasible
research programme**. A polished narrative cannot cure an ineligible application, an unsupported
premise, an underpowered design, or an uncontrolled imaging measurement chain.

## Non-negotiable boundaries

- **Lock the live call before compliance advice.** Record the funder, mechanism, cycle, programme,
  official sources and retrieval date in a [grant call passport](templates/grant-call-passport.md).
  If those cannot be verified, emit `CALL_VERSION_UNRESOLVED`, restrict the review to scientific
  content, and do not claim submission readiness.
- **For NSFC, lock six routing fields.** Record application year, programme/type and subtype,
  science division/office, year-bound application code candidate, research attribute and any
  special call/clinical track. Read
  [nsfc-2024-2026-change-map.md](references/nsfc-2024-2026-change-map.md); current official-source
  conflicts become `CONFLICTING / ADMIN_CONDITIONAL`, never an inferred eligibility answer.
- **Separate two gates.** Administrative acceptance (eligibility, limits, forms, attachments,
  budget regime, ethics/security) is not scientific merit. Passing either gate does not imply
  passing the other.
- **Use the target funder's current criteria.** Do not translate every call into a generic NSFC,
  NIH or numeric rubric. Do not invent scores, weights, deadlines, page limits or eligibility.
- **Evidence before rhetoric.** Preliminary findings must point to real source artifacts. Keep
  verified facts, user attestations, calculations, hypotheses, planned work and missing evidence
  visibly distinct. Never turn planned work into preliminary data.
- **Protect claim ceilings.** Prediction is not measurement, mechanism, causality or clinical
  utility. A model-performance aim cannot silently license any of those stronger claims.
- **Review is read-only by default.** Critique and propose changes; modify the submitted file only
  when the user explicitly requests revision.
- **NSFC generative-AI boundary.** For a live NSFC application, read
  [call-and-compliance-gate.md](references/call-and-compliance-gate.md). The 2026 annual application
  and completion notice permits bounded research-tracking/reference assistance only with human
  verification, applicant responsibility, truthful declaration and marking; it prohibits directly
  generated applications and unverified content. Label AI-assisted text as advisory for applicant
  verification and rewriting; never represent it as applicant-authored or submission-ready.

## Route by task

| User need | Mode and resources | Main output |
|---|---|---|
| Live NSFC rule, year comparison or submission-readiness question | read [nsfc-2024-2026-change-map.md](references/nsfc-2024-2026-change-map.md), [call-and-compliance-gate.md](references/call-and-compliance-gate.md) and [source-registry.md](references/source-registry.md) | six-field current-year lock, exact-source rule map and conflict states |
| NSFC title, abstract, 立项依据, 研究内容, 研究基础 or innovation development | read [nsfc-application-content-playbook.md](references/nsfc-application-content-playbook.md) and [grant-architecture.md](references/grant-architecture.md) | scientific-function map and author decision points, not legacy headings |
| NSFC imaging code, H18/H27/H28/H29 or clinical/special-call choice | read [nsfc-radiology-code-and-call-router.md](references/nsfc-radiology-code-and-call-router.md) | year-bound candidate-code/call record and unresolved confirmation gate |
| Fast fatal-flaw or one-section check | `triage/targeted`; read [review-modes-and-criteria.md](references/review-modes-and-criteria.md) | bounded findings, missing inputs and next gate |
| Whole application review | `full audit`; also read [call-and-compliance-gate.md](references/call-and-compliance-gate.md), [radiology-feasibility-audit.md](references/radiology-feasibility-audit.md), and [evidence-contract-and-stopping-rules.md](references/evidence-contract-and-stopping-rules.md) | criterion-by-criterion report |
| Simulated panel or pre-submission challenge | `mock panel`; read [review-modes-and-criteria.md](references/review-modes-and-criteria.md) | independent views, disagreement record, panel synthesis |
| Response to prior critiques / resubmission | `revision/resubmission`; read [review-modes-and-criteria.md](references/review-modes-and-criteria.md) | critique-to-change matrix and residual risks |
| Final funder-system fields, files and institutional handoff | `funder-package-finalization`; read [call-and-compliance-gate.md](references/call-and-compliance-gate.md) and use the submission contract in [grant-call-passport.md](templates/grant-call-passport.md) | closed field/file/attachment inventory, unresolved blockers and human institutional action gate |
| Develop question, aims or architecture | read [grant-architecture.md](references/grant-architecture.md) and [reframe-and-innovation.md](references/reframe-and-innovation.md) | proposal spine and author decision points |
| Feasibility, milestones, budget or contingency | read [radiology-feasibility-audit.md](references/radiology-feasibility-audit.md) and [feasibility-and-pitfalls.md](references/feasibility-and-pitfalls.md) | aim/milestone/risk register |
| Choose a framework for imaging AI, diagnostic accuracy, prediction, radiomics, generative AI or quantitative imaging | read [imaging-methodology-router.md](references/imaging-methodology-router.md) | task-specific design-function map; no checklist-as-validity claim |
| NIH, ERC, Wellcome or another international route | read [international-grants.md](references/international-grants.md), then verify the named call live | funder-specific mapping; never generic substitution |

Do not load all references for a narrow request.

## Funder-package finalization boundary

Use `funder-package-finalization` only for one exact funder + mechanism + cycle + programme/subcall +
applicant/host configuration. Recheck the live call, amendments, current electronic form/system and
institutional route. Freeze:

`call-passport ID/version | proposal/source versions | field/section/attachment inventory | exact file
locators and hashes where files exist | page/character/format checks | budget/ethics/security/AI-use
handoffs | applicant/co-applicant attestations | institutional steps and deadlines | unresolved
blockers | responsible human role`.

This mode audits a package; it does not log in, paste fields, upload files, attest for an applicant,
confirm institutional eligibility, authorize a budget or press a submission control. Scientific or
budget content that changes during finalization returns to the grant/scientific owner and creates a
new source version before the inventory is rechecked.

Use only these machine states:

- `FUNDER_PACKAGE_INCOMPLETE` — required fields, files, current rules or source versions are missing;
- `FUNDER_PACKAGE_BLOCKED` — a known compliance, authority, confidentiality or unresolved-live-rule
  condition prevents institutional handoff; or
- `HUMAN_INSTITUTIONAL_SUBMISSION_REQUIRED` — the bounded machine audit is complete and every
  remaining portal, attestation, approval and submission action belongs to authorized humans.

`HUMAN_INSTITUTIONAL_SUBMISSION_REQUIRED` is the maximum machine state. Never report `SUBMITTED`,
`ACCEPTED`, `ELIGIBLE_CONFIRMED`, official receipt, funding probability or funder/institutional
approval without the corresponding authoritative external evidence.

## Review workflow

1. **Intake and version lock.** Identify the review mode and material version. Build the call
   passport. Record absent proposal sections instead of inferring them.
2. **Administrative gate.** Check eligibility, application limits, required forms/attachments,
   research category/code, budget route, ethics/security and AI-use rules only against current
   official sources. For NSFC, freeze all six routing fields before any compliance verdict. Preserve
   official-text conflicts instead of resolving them by convenience. Return `ADMIN_PASS`,
   `ADMIN_CONDITIONAL`, `ADMIN_FAIL`, or `ADMIN_NOT_ASSESSABLE` with evidence.
3. **Freeze the proposal spine.** Extract clinical/scientific need → gap → central question →
   hypothesis → aims → expected inference/impact. Flag aims that do not serve the same question.
4. **Apply the funder criteria.** Create one **criterion finding** per material issue: criterion,
   verdict, evidence anchor, consequence, actionable repair and residual uncertainty. Preserve the
   funder's language and scoring model.
5. **Run the radiology gate.** Audit the clinical-phenomenon → image-phenotype → biological/clinical
   proposition bridge; intended use and unit; acquisition/reconstruction; multimodal intersection
   denominator; reference standard; annotation; data/model-lineage leakage; aim-level sample size;
   external-independence vector; statistics; transportability; mechanism evidence; clinical pathway;
   data/compute/ethics; and measurement-to-claim consistency.
6. **Test execution.** Map every aim to personnel, data, dependencies, milestone, decision rule,
   fallback, time and budget. Use the [aim/milestone/risk register](templates/aim-milestone-risk-register.md).
7. **Synthesize without laundering disagreement.** Prioritize fatal compliance defects and
   inference-breaking weaknesses before competitive or editorial improvements. In panel mode,
   retain minority concerns.
8. **Close with a decision boundary.** State what was assessed, what remains unverified, which
   claims are supportable, and whether the next state is `READY_FOR_AUTHOR_REVISION`,
   `READY_FOR_INSTITUTIONAL_CHECK`, `REVIEWABLE_BUT_NOT_READY`, or `STOP_AND_REFRAME`.

## Output contract

For a full review use [grant-review-report.md](templates/grant-review-report.md) and include:

1. `Review scope` — mode, proposal version, sections actually read, target call and limitations.
2. `Call passport status` — current official evidence and unresolved live rules.
3. `Administrative gate` — separate from merit, with no implied funding judgment.
4. `Proposal spine` — question, hypothesis, aims, claim ceiling and logic breaks.
5. `Criterion findings` — `PASS / CONDITIONAL / FAIL / NOT_ASSESSABLE`, each evidence-anchored.
6. `Radiology feasibility gate` — measurement, data, reference standard, analysis and translation.
7. `NSFC code/call and methodology route`, when applicable — year-bound candidate code, clinical or
   special-call boundary, selected design frameworks and explicit non-applicability.
8. `Aim–milestone–risk–budget alignment` — go/no-go logic and scientifically meaningful fallback.
9. `Prioritized revision plan` — P0 compliance, P1 inference-threatening, P2 competitive, P3 editorial.
10. `Evidence and uncertainty ledger` — verified, attested, planned, inferred, missing and stale items.
11. `Readiness boundary` — never a guarantee of eligibility, score, review outcome or funding.

## Handoffs

- Study design and validation → `radiology-design`; acquisition/reconstruction/QC →
  `radiology-acquisition-qc`; ground truth → `radiology-annotation`; data → `radiology-data`.
- Sample size and inference → `radiology-stats` / `radiology-method-evaluation`; clinical
  reader-study design → `radiology-translation` (stats supplies MRMC analysis and sizing);
  ethics and governance → `radiology-ethics`; clinical pathway → `radiology-clinical-domain`.
- Live call, deadline, eligibility or frontier verification → `radiology-search` /
  `radiology-frontier`; project-level provenance → `radiology-pipeline`.
- A frozen, author-approved proposal spine for a defence or pitch deck → `radiology-paper2ppt`.
  This skill does not design slides.
- Award acceptance, post-award conditions, amendments, annual/interim/final technical reporting and
  sponsor deliverable tracking → `radiology-research-ops`; changed scientific content returns to its
  original scientific owner before the funder-facing artifact is refreshed.
- Final portal use, applicant attestations, institutional approvals and submission remain with the
  applicant, host research office and funder. A completed package audit stops at
  `HUMAN_INSTITUTIONAL_SUBMISSION_REQUIRED`.
- This skill does not replace the funder, the host institution's research office, ethics review,
  financial approval or human expert judgment, and never guarantees funding.
