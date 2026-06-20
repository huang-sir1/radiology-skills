---
name: radiology-translation
description: "Move a validated imaging model from retrospective performance toward clinical use — design the clinical-use scenario, model outputs, reader (multi-reader multi-case) studies of radiologist-vs-AI-vs-radiologist+AI, decision thresholds tied to actions, net-benefit/decision-curve framing, prospective and real-world validation, and PACS/RIS workflow integration. Use when the user wants a reader study, clinician+AI gain, prospective/real-world validation, deployment plan, \"临床转化/读者研究/前瞻性验证\", or to know what it takes to claim clinical utility. Produces a translation plan with the use scenario, reader-study design, threshold-to-action mapping, and prospective/workflow design. Never lets a retrospective AUC be reported as clinical readiness."
---

# Clinical Translation, Reader Studies & Prospective Validation

Use this skill to turn "the model has good retrospective performance" into "the model helps in
practice." This is the step top journals reward and reviewers demand before any clinical claim:
a defined use scenario, a reader study, thresholds tied to actions, and prospective/real-world
evidence.

## Core stance

- **Retrospective AUC ≠ clinical utility.** Discrimination on a curated set says nothing about
  patient benefit. The claim must be earned with utility evidence, not asserted.
- **Define the use scenario first.** Screening, triage, diagnosis, staging, prognosis,
  treatment-response, surveillance, or MDT support — each fixes the output, the threshold, and the
  cost of errors.
- **Reader studies are designed, not improvised.** MRMC with washout, randomised order,
  radiologist-alone vs radiologist+AI, reader experience reported, and the right statistic
  (→ radiology-stats).
- **Thresholds map to actions.** Every operating point implies a clinical action and a cost of
  false positives/negatives; net-benefit / decision-curve quantifies it.
- **Prospective beats retrospective; real-world beats curated.** Plan temporal/prospective/
  real-world validation and the PACS/RIS workflow position and constraints.
- **Integrity & safety.** Plan only; never claim deployment readiness without the evidence, and
  never give clinical or diagnostic recommendations for individual patients.

## When to use

- "Design a reader study / clinician+AI gain study." / "帮我设计读者研究 / 医生+AI 增益研究。"
- "What does it take to claim clinical utility / move toward deployment?"
- "Plan a prospective / real-world validation." / "前瞻性验证、真实世界验证怎么设计？"
- "Map my model's threshold to a clinical action / net benefit."
- "Where does this sit in the PACS/RIS workflow?"

## When to open extra files

| File | Open when |
|---|---|
| [references/use-scenario.md](references/use-scenario.md) | Defining the clinical-use scenario, the model output, and the cost of errors |
| [references/reader-study.md](references/reader-study.md) | MRMC reader-study design: readers, washout, randomisation, with/without AI, outcomes |
| [references/threshold-to-action.md](references/threshold-to-action.md) | Mapping operating points to actions; net-benefit / decision-curve; false-positive/negative consequences |
| [references/prospective-deployment.md](references/prospective-deployment.md) | Prospective/real-world validation design; PACS/RIS integration; monitoring and drift |

## Workflow

1. **Define the use scenario** (use-scenario.md) — where in the pathway, who acts on the output,
   what the output is (risk score, stratification, mask, heatmap, report aid), error costs.
2. **Set the threshold-to-action map** (threshold-to-action.md) — operating point(s), the action
   each triggers, and net-benefit framing across plausible thresholds.
3. **Design the reader study** (reader-study.md) if clinician impact is claimed — MRMC, washout,
   randomised order, alone vs +AI, reader experience, time/confidence outcomes.
4. **Plan prospective/real-world validation** (prospective-deployment.md) — temporal/prospective/
   RWE design, workflow position, monitoring for drift, failure handling.
5. **Bound the claim** — state exactly what level of evidence supports what level of claim;
   route statistics to `radiology-stats` and reporting to `radiology-reporting`.

## Output contract

1. **`Use scenario`** — pathway position, decision-maker, output type, error costs.
2. **`Threshold-to-action map`** — operating point(s) → action; net-benefit/DCA framing.
3. **`Reader-study design`** (if applicable) — readers, washout, randomisation, arms, outcomes,
   statistic (MRMC → radiology-stats).
4. **`Prospective/real-world plan`** — design, workflow integration, monitoring, drift.
5. **`Claim ladder`** — what each evidence level licenses (retrospective → reader → prospective →
   deployment), with the current honest claim marked.

## Quality bar

A good translation plan names the clinical decision the model serves, designs a reader study a
biostatistician would accept, ties thresholds to actions and net benefit, and plans prospective
evidence — and it never lets a retrospective AUC masquerade as clinical readiness.

## Handoffs

- MRMC / net-benefit / decision-curve statistics → `radiology-stats`.
- Reader-study reporting, DECIDE-AI / CONSORT-AI for trials → `radiology-reporting`.
- The validation cohort / temporal design → `radiology-design`.
- Reader-study figures, net-benefit plots → `radiology-figure`.
- Plans research and evaluation only; no individual-patient clinical or diagnostic advice.
