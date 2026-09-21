# Multi-axis evidence state and clinical-translation lifecycle

Use this reference whenever a project asks how far an imaging test or AI system has translated.
Never collapse technical performance, clinical validity, clinical impact, authorization, economic
value, implementation and production monitoring into one maturity label.

## 1. Seven independent evidence axes

| Axis | Decision question | Minimum evidence fields | Forbidden inference |
|---|---|---|---|
| technical/analytical performance | does the software/measurement work under specified conditions? | version, inputs, output, test conditions, accuracy/repeatability/failure and uncertainty | technical success is not clinical validity |
| clinical validation | does it perform for the intended population/use? | intended use, representative cohorts, reference/outcome, transport shifts, calibration/subgroups | external validation is not clinical utility |
| clinical utility/impact | does visible use change decisions, workflow, safety, resources or patient outcomes? | frozen intervention/comparator, causal estimand, live exposure, endpoint/harms/fidelity | silent deployment or DCA is not observed benefit |
| regulatory status | what jurisdictional use is authorized and under which exact conditions? | jurisdiction, product/version, intended use, status, official source/date, qualified owner | clearance is not benefit, reimbursement or local activation |
| HTA/economic value | is it valuable/affordable relative to the current pathway? | perspective, comparator, horizon, cost/outcome model, uncertainty, local price/payment evidence | net benefit/DCA is not cost-effectiveness |
| implementation state | can the intervention be adopted, delivered equitably and sustained in context? | determinants, strategy, reach/adoption/fidelity/acceptability/feasibility/cost/sustainment | reporting against StaRI is not successful implementation |
| production monitoring | is the released intervention still available, used, safe and performing? | release bundle, denominators, baseline/window/cadence/threshold, owner/action/CAPA/rollback | no alert is not proof of stable performance when labels are delayed/missing |

Record each as `NOT_ASSESSED`, `PLANNED`, `EVIDENCE_PARTIAL`, `SUPPORTED_FOR_TESTED_SCOPE`,
`FAILED`, `STALE_AFTER_CHANGE` or `NOT_APPLICABLE`. Regulatory state additionally uses the exact
jurisdiction's official vocabulary; never invent a cross-jurisdiction label.

## 2. Optional T0-T6 route

The route is a coordination branch, not a universal linear regulation pathway. Activities can partly
overlap, but no later activity silently repairs an earlier evidence failure.

| Stage | Decision and artifact | Gate |
|---|---|---|
| T0 intended-use/benefit-risk lock | user, population, setting, inputs/output/action, comparator, harms, version and claim | intended use and authority are explicit |
| T1 validation/transport | technical + clinical validation and local transport plan | tested shifts, failures, calibration and subgroups support only the stated scope |
| T2 governance readiness | ethics, regulatory, privacy/security, quality, clinical safety and IT owners | every live jurisdictional/local requirement verified or escalated |
| T3 local acceptance/silent | end-to-end site acceptance plus shadow run without care influence | identity, delivery, fallback, latency, drift and outcome linkage work; no user-impact claim |
| T4 bounded active deployment/impact | frozen release shown to users under approved evaluation | causal/credible clinical-impact and human-factors/fidelity evidence, harms monitored |
| T5 HTA/procurement/scale | economic/implementation evidence and authorized purchasing route | local cost/payment/capacity/equity assumptions verified; no procurement claim by the skill |
| T6 monitor/change/retire | production contract, incidents, CAPA, revalidation, rollback/stop/retire | release remains within evidence/authorization or is bounded, rolled back or retired |

## 3. Imaging release bundle

Treat these as one intervention identity:

`model/algorithm + weights + preprocessing + operating threshold + output object/schema + UI/display +
workflow/worklist position + user instructions/training + integration configuration + fallback +
monitoring configuration`.

A change in threshold, UI, training, integration or fallback can change clinical behavior even when
the model AUC is unchanged. Mark affected impact, implementation and monitoring evidence stale and
reassess the applicable authorization/change-control path.

## 4. Hard boundaries

- multi-center external validation ≠ clinical utility;
- silent/shadow deployment ≠ human-AI interaction evidence;
- regulatory clearance/approval ≠ patient benefit, reimbursement, procurement or local go-live;
- DCA/net benefit ≠ observed benefit or economic evaluation;
- DICOM conformance statement ≠ end-to-end interoperability;
- QIBA/phantom precision ≠ clinical validity;
- PCCP ≠ permission for unbounded self-learning;
- absence of a drift alert ≠ stable performance when reference labels are delayed, missing or
  selectively verified.

Return `seven-axis state matrix -> earliest unsupported decision -> applicable T-stage -> next
evidence artifact/owner -> stale-after-change map -> surviving claim ceiling`.

## Evidence transition register

One row per evidence axis that must move: `axis | current evidence and state | next required
study/artifact | success criterion | owner | claim unlocked | failure and drift/incident plan`.
Preserve failed transitions — a failed study lowers the claim ceiling and is never silently dropped.

## Primary/official sources and status

- IMDRF [N41 SaMD Clinical Evaluation](https://www.imdrf.org/documents/software-medical-device-samd-clinical-evaluation),
  final 2017, official status verified 2026-08-23.
- IMDRF [N88 GMLP](https://www.imdrf.org/documents/good-machine-learning-practice-medical-device-development-guiding-principles),
  final 2025, official status verified 2026-08-23.
- FDA [AI-enabled device lifecycle and marketing-submission recommendations](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-enabled-device-software-functions-lifecycle-management-and-marketing),
  **draft, not for implementation** as verified 2026-08-23.
- FDA [PCCP guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence),
  final August 2025 as verified 2026-08-23.

This is research/evidence planning, not a regulatory, safety, procurement or reimbursement decision.
Current jurisdictional status must be re-verified and accepted by qualified local owners.
