# Human factors and implementation for imaging systems

Use this reference to design how people interact with an imaging/AI system and how it is introduced,
maintained and withdrawn in real practice. Usability is not cosmetic: interface, timing, authority,
workload and organizational context can reverse an algorithm's apparent benefit.

This reference supports research planning; formal device usability/regulatory work requires the
qualified local human-factors, safety, clinical-engineering and regulatory owners.

## 1. Define users, environment and safety-critical work

Build a use specification:

| Field | Required specification |
|---|---|
| Users | role, specialty, experience, training, accessibility/language and permissions |
| Patients/cases | intended and excluded populations, urgency, prevalence/spectrum and vulnerable groups |
| Environment | PACS/RIS/EHR/worklist, workstation/mobile, lighting/noise/interruptions, remote/on-call context |
| Task/moment | before, during or after interpretation; screening, triage, diagnosis, reporting, planning or monitoring |
| Information | image/series, priors, indication, model output, uncertainty, explanation and unavailable inputs |
| Authority | who decides/signs, override, escalation and fallback |
| Critical harm | missed/delayed finding, wrong action, unnecessary test, privacy/security or access inequity |

Observe the existing workflow before redesigning it. A diagram made only from developer assumptions is
not a workflow analysis.

## 2. Task and use-error analysis

Decompose the path:

`case acquisition -> input availability -> model execution -> output delivery -> noticing ->
interpretation -> action/override -> communication -> follow-up -> monitoring`.

For each step record user, prerequisite, expected action, time pressure, failure, detectability, harm,
control and evidence. Include:

- wrong patient/exam/series, laterality or stale prior;
- missing/corrupt input, downtime, latency and OOD/abstention;
- false positive/negative, miscalibration and misleading explanation;
- alert fatigue, distraction, automation bias, anchoring and complacency;
- over-reliance by novice users and deskilling/loss of independent search;
- override friction, ambiguous responsibility and silent fallback;
- copied/generated report error and failure of critical-result communication;
- subgroup/access differences and inaccessible UI/training.

Risk priority is not a universal numeric cutoff. Preserve severity, probability/exposure, detectability,
controls, residual risk and owner under the applicable local safety process.

## 3. Interface and information contract

- Show intended use, output meaning, operating point and action—not only a score.
- Make unavailable inputs, low confidence/abstention, failure and version visible with an actionable
  fallback.
- Avoid visual precision the measurement/model does not support. Explanations/saliency are hypotheses
  about model behavior, not proof of causal reasoning or image truth.
- Preserve source image access and the user's ability to inspect independently before/after assistance
  according to the tested workflow.
- Design alerts by consequence and workflow capacity; more sensitivity can cause workload harm.
- Log exposure, output, user action, edit, override/reason, timing, failure and final decision with
  privacy/access controls.
- Define what users are prohibited from doing and how the system prevents or detects it.

## 4. Formative evaluation

Iterate before a confirmatory/live study using representative users, cases and environments:

1. contextual inquiry/work observation;
2. cognitive walkthrough and use-error analysis;
3. low- then high-fidelity prototype testing;
4. think-aloud/debrief focused on causes, not user blame;
5. simulated normal, rare, failure, time-pressure and recovery cases;
6. design revision with traceability from finding to control and retest.

Record recruitment, user profile, tasks, scripts, prototype/version, findings, severity, changes and
residual issues. Small formative samples discover failure modes; they do not estimate population rates.

## 5. Confirmatory human-performance evaluation

Freeze system/UI/training, user groups, critical tasks, use scenarios, endpoint, success criterion and
analysis before testing. Use realistic clinical information, interruptions, prevalence and time
constraints. Assess independent users who were not the design team.

Measure:

- task success and critical use errors with denominators;
- accuracy/safety impact including correct-to-incorrect changes after assistance;
- time to notice/interpret/act and recovery from failure;
- understanding of output, uncertainty, abstention and limitations;
- workload/trust/acceptability as secondary measures tied to behavior;
- variation by experience, site, accessibility and intended subgroup.

Self-reported satisfaction alone does not establish safe/effective use. A controlled lab/reader study
does not establish live implementation.

## 6. Implementation strategy and fidelity

Predefine local readiness, champions/owners, integration/testing, user training/competency, staged
rollout, support, downtime/rollback, incident response and update communication. Measure:

- reach: eligible users/cases actually exposed;
- adoption and time to competent use;
- fidelity: output available/opened/used as intended;
- overrides, workarounds and reasons;
- feasibility, latency, workload and resource displacement;
- maintenance, drift, training decay and staff turnover;
- equity/access and unintended exclusion;
- sustainability and withdrawal criteria.

Implementation outcomes describe delivery. Clinical impact still needs the corresponding causal study
design.

## 7. Automation bias and learning effects

- Include plausible high-confidence wrong outputs and no-output/abstention cases under ethical,
  approved simulation or retrospective reader conditions.
- Capture unaided and aided decision paths where the design allows, not only final accuracy.
- Randomize/counterbalance order and manage washout/carryover. Sequential assistance differs from two
  independent reads.
- Test whether training communicates failure boundaries and whether users retain independent review.
- Monitor acceptance/override conditional on model correctness, confidence and case difficulty.
- Longitudinally assess behavior after novelty fades; a one-session improvement may not persist.

## 8. Monitoring and change control

Maintain versioned links among model, threshold, UI, training, integration and intended use. Monitor
availability, latency, input shift, calibration/performance, subgroup errors, alerts, overrides,
critical incidents and user feedback. Define investigation, corrective action, rollback and revalidation
triggers.

A UI, threshold, workflow position, training or model update can change human behavior even when AUC is
unchanged. Treat material changes as a new intervention state.

## 9. Stop gates and output

Return `STOP_FOR_REPAIR` when intended users/tasks/environment are undefined, a safety-critical failure
has no detectable fallback, output exposure/action cannot be logged, confirmatory testing uses only
developers, or live clinical claims rely only on satisfaction/usability scores. Escalate unresolved
patient-safety, privacy, security and regulatory issues.

Return:

`use specification -> workflow/task analysis -> use-error/harm-control register -> interface/information
contract -> formative evidence -> confirmatory human-performance plan -> implementation/fidelity plan
-> monitoring/change control -> residual risk and claim ceiling`.

## Primary and official sources

- FDA. [Applying Human Factors and Usability Engineering to Medical Devices](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/applying-human-factors-and-usability-engineering-medical-devices).
- Vasey B, et al. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9).
- NIST. [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).
- FDA. [Predetermined Change Control Plan guidance for AI-enabled device software functions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence).

Standards, guidance and jurisdictional applicability change; verify current official requirements before
formal usability validation or deployment.
