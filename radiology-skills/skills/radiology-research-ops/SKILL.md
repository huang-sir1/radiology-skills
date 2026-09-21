---
name: radiology-research-ops
description: "Plan/audit sites, RACI, milestones, dependencies, resources, risks and closeout; not scientific design."
---

# Radiology Research Operations

Use this skill to convert an approved or otherwise frozen scientific plan into a traceable operating
system. It owns RACI, dependencies, site readiness, throughput, resource capacity, operational
registers, freezes, pause/termination and closeout. It does not decide the scientific question,
approve research, execute institutional management authority or claim that a plan was actually run.

## Operating modes

| Mode | Use when | Primary result |
|---|---|---|
| `startup` | a protocol or project is preparing to open | operating charter, RACI, critical path and readiness gates |
| `active-control` | recruitment, acquisition, annotation, assays or analysis are under way | status dashboard, variance, forecast, actions and evidence |
| `recovery` | a milestone, site, resource, quality or dependency is failing | root constraint, recovery options, decision deadline and claim consequence |
| `freeze-release` | a cohort, labels, analysis set, model, evidence or manuscript package must be frozen/released | versioned freeze criteria, authorization, manifest and exception ledger |
| `post-award-funder-reporting` | an awarded project has conditions, amendments, annual/interim/final reports or sponsor deliverables | award-term passport, obligation/evidence crosswalk, reporting package state and authorized funder-action handoff |
| `pause-stop-closeout` | the project pauses, terminates or completes | safety/access handoff, preservation, reconciliation, closure and reusable lessons |

For the control model and registers read
[references/operations-control-model.md](references/operations-control-model.md). For multicentre
and modality-specific readiness read
[references/site-readiness-and-imaging-operations.md](references/site-readiness-and-imaging-operations.md).
For risks, changes, freezes and closeout read
[references/risk-change-freeze-and-closeout.md](references/risk-change-freeze-and-closeout.md).
Consult [references/source-registry.md](references/source-registry.md) before policy-facing advice;
clinical-trial sources are quality frameworks only when the project is outside their actual scope.

## Input passport

Record:

`project/study ID | operating mode | scientific protocol/SAP/design digest and owner | study family
and intended claim | sites/modalities/work packages | current approvals/contracts/access evidence |
start/end and decision milestones | staffing/equipment/assays/compute/budget constraints | critical-to-
quality factors | data/annotation/acquisition/analysis freeze states | current risks/issues/deviations |
local accountable roles | artifact locations | authority for any update or external action`.

Scientific design, ethics, contracts, budget approval, site activation and institutional assignments
are author-only or institution-only facts. Use `NOT_EVIDENCED` until the relevant record is inspected.
Advisory work is read-only; do not open a site, alter a schedule, assign personnel, spend funds,
contact collaborators or change a protocol without explicit authority.

## Operational evidence states

Use `PLANNED`, `EVIDENCED_READY`, `ACTIVE`, `AT_RISK`, `BLOCKED`, `FROZEN`, `PAUSED`,
`TERMINATED` or `CLOSED`. A calendar date, verbal assurance, percentage-complete estimate or green
dashboard does not establish readiness. Every state cites a record, owner and checked date.

## Post-award funder-reporting boundary

For `post-award-funder-reporting`, bind one exact award and reporting period:

`funder/mechanism/cycle/award ID | notice and award-term versions | institutional implementation
route | reporting period/deadline/time zone | approved aims/protocol/SAP/budget/timeline versions |
conditions and prior amendments | required fields/files/attachments | actual milestone/deliverable evidence
and exact locators | deviations/issues/risks | ethics/data/sharing/publication states | scientific owner
approvals | institutional/funder action owner`.

Use the current award notice, terms, amendment history, reporting instructions and institutional
research-office route. A prior application, generic funder guide, planned milestone or percent-complete
estimate is not evidence that a deliverable was achieved or accepted.

- **Annual/interim/final reports:** map every funder field and deliverable to a source artifact,
  reporting period, responsible owner and unresolved fact. Research operations assembles and tracks
  the package; the original scientific owner verifies methods, analyses, results and claims.
- **Amendments:** keep a proposed change, authorized amendment and actual protocol/operational
  deviation distinct. Never backdate approval or use a report narrative to normalize an unauthorized
  change. Propagate an approved change or unapproved deviation to every affected scientific artifact.
- **Administrative and financial boundary:** record award/budget/effort/contract states only from
  authoritative records. Do not certify expenditures, effort, compliance, continuation, acceptance
  or institutional/funder approval.
- **External-action boundary:** do not log in, upload, attest, contact the sponsor, request an
  amendment or submit a report without explicit authority. The maximum machine state is
  `HUMAN_INSTITUTIONAL_FUNDER_ACTION_REQUIRED`.

Use `POST_AWARD_REPORT_INCOMPLETE` when fields, sources or owners are missing and
`POST_AWARD_REPORT_BLOCKED` for a known overdue, authorization, compliance, scientific-validity or
unresolved-term blocker. Neither state permits invented completion evidence.

## Required workflow

1. **Accept the scientific lock.** Receive the question, protocol, estimand, measurement/QC,
   statistics, ethics and data-access decisions from their owners. Return unresolved science rather
   than repairing it as project management.
2. **Build the control book.** Define work packages, deliverables, acceptance criteria, dependencies,
   RACI, decision rights and escalation paths. One work package has one accountable role; never
   invent the person or institutional authority.
3. **Compute the critical path and capacity.** Map duration ranges, access lead times, throughput,
   bottlenecks, slack, external dependencies and resource limits. Separate calendar forecast from
   scientific sample-size requirements.
4. **Gate site/workstream readiness.** Verify approvals, agreements, trained roles, equipment,
   acquisition/reconstruction versions, DICOM transfer/de-identification, reference standard,
   annotation, data schema, assay/compute capacity, safety and fallback. Use
   [templates/site-readiness-freeze-register.md](templates/site-readiness-freeze-register.md).
5. **Control execution.** Compare planned and actual recruitment, follow-up, series acceptance,
   annotation, assay and run throughput. Record denominator, time window, evidence and forecast;
   never invent universal green/yellow/red thresholds.
6. **Maintain distinct registers.** Keep future uncertainty (`risk`), present blockage (`issue`),
   authorized choice (`decision`), planned modification (`change`), divergence from the frozen plan
   (`deviation`) and safety/security event (`incident`) separate.
7. **Freeze and release deliberately.** A freeze identifies scope, version, manifest, criteria,
   approver role, time and permitted exceptions. Any post-freeze change creates a new version and
   downstream-staleness handoff; it is not silently overwritten.
8. **Decide recovery, pause or termination.** Tie actions to explicit thresholds and preserved
   claims. A scientifically invalid, unauthorized or unsafe study cannot be rescued by schedule
   compression.
9. **Close out.** Reconcile participants/cases/specimens/images, data, annotations, equipment,
   finances, agreements, access, deviations, incidents, code/results, negative evidence and
   retention/destruction obligations. Use
    [templates/research-operations-control-book.md](templates/research-operations-control-book.md).
10. **When funder reporting applies, build the award-term crosswalk.** Reconcile the current award
    conditions, approved changes, reporting-period evidence and required fields/files. Return every
    scientific statement to its original owner for verification, then stop at
    `HUMAN_INSTITUTIONAL_FUNDER_ACTION_REQUIRED` for portal, attestation, approval or submission.

## Stop and escalation gates

Return `OPS_STOP_AND_ESCALATE` for absent or expired approval/access; participant or staff safety
risk; uncontrolled PHI/security exposure; unqualified critical role; critical-to-quality process
without monitoring; material protocol deviation; unreconciled patient/exam/lesion/site identity;
protected-test or freeze breach; evidence destruction; or a contract/budget/personnel decision that
requires institutional authority.

State the responsible **role** and minimum evidence for release. The skill never activates a site,
authorizes spending, instructs staff to continue blocked work, signs a delegation log, makes an HR or
contracting decision, or declares institutional compliance.

## Output contract

1. `Operations passport and current evidence state`
2. `Work breakdown, RACI and decision-rights map`
3. `Critical path, capacity and dependency forecast` with uncertainty
4. `Site/workstream readiness matrix` and exact blockers
5. `Recruitment/acquisition/annotation/assay/analysis throughput dashboard`
6. `Resource and budget-capacity map` — quantities and constraints, not financial approval
7. `Risk / issue / decision / change / deviation / incident registers`
8. `Freeze/release manifest and exception ledger`
9. `Recovery, pause, termination or closeout decision packet`
10. `Post-award obligation/report/amendment crosswalk` — when applicable, with source versions,
    scientific-owner verification, unresolved blockers and human funder-action gate
11. `Scientific, ethics, data, institutional and pipeline handoffs`

## Handoffs and non-ownership

- Question, estimand, validation and sample-size design -> `radiology-design` /
  `radiology-stats`; acquisition and measurement gate -> `radiology-acquisition-qc`.
- Annotation SOP -> `radiology-annotation`; data identity, de-identification and access ->
  `radiology-data`; approvals and safety governance -> `radiology-ethics`.
- Grant milestones and requested budget narrative -> `radiology-grant`; whole-project scientific
  state and artifact staleness -> `radiology-pipeline`.
- Pre-award call/proposal review, resubmission and final application-package audit ->
  `radiology-grant`. After award, this skill owns obligation, amendment, annual/interim/final report
  and sponsor-deliverable tracking, while methods/results/claims remain with the original scientific
  owner and portal/acceptance authority remains with the institution/funder.
- Silent/active deployment evidence, reader/impact design, site-acceptance criteria and production
  monitoring science -> `radiology-translation`; operations owns the approved plan's RACI, schedule,
  resources, dependencies, escalation and closeout, not its clinical-validity claim.
- The PI, sponsor, institution, site, funder and authorized committees retain personnel, financial,
  contractual, activation, safety, amendment, report-submission, acceptance and termination authority.
