---
name: radiology-translation
description: "Design clinical use, reader/impact studies, human factors, deployment and lifecycle evidence."
---

# Clinical Translation, Reader Studies & Prospective Validation

Use this skill to determine which evidence is needed to move from retrospective performance toward
a bounded claim about clinical use. The required design depends on the intended use and estimand: it
may involve threshold/action analysis, a controlled reader study, silent prospective validation,
active impact evaluation, implementation research or production monitoring.

> **Name note:** this skill is **clinical translation** (bench-to-bedside evidence), **not**
> language translation. For Chinese→English manuscript translation/reconstruction →
> `radiology-writing` ([Chinese-author workflow](../radiology-writing/references/chinese-author-workflow.md)).

## Core stance

- **Retrospective AUC ≠ clinical utility.** Discrimination on a curated set says nothing about
  patient benefit. The claim must be earned with utility evidence, not asserted.
- **Define the use scenario first.** Screening, triage, diagnosis, staging, prognosis,
  treatment-response, surveillance, or MDT support — each fixes the output, the threshold, and the
  cost of errors.
- **Reader studies are designed for the estimand.** Choose crossed/partially crossed MRMC,
  sequential, parallel or another justified design; manage order, learning, memory and carryover,
  report reader/case sampling and match inference to the assignment structure (→ radiology-stats).
- **Thresholds map to actions.** Every operating point implies an action and consequence;
  decision-curve analysis models net benefit under explicit threshold/weighting assumptions but
  does not observe patient benefit or cost-effectiveness by itself.
- **Match design to claim.** Temporal, external, controlled-reader, silent prospective, pragmatic,
  quasi-experimental, randomized and monitoring designs answer different questions; there is no
  universal ranking that overrides estimand, bias, setting and feasibility.
- **Translation is multi-axis.** Technical performance, clinical validation, clinical impact,
  regulatory state, economic value, implementation and production monitoring remain separate.
  Never promote one because another axis is strong.
- **Integrity & safety.** Plan only; never claim deployment readiness without the evidence, and
  never give clinical or diagnostic recommendations for individual patients.

## When to use

- "Design a reader study / clinician+AI gain study." / "帮我设计读者研究 / 医生+AI 增益研究。"
- "What does it take to claim clinical utility / move toward deployment?"
- "Plan a prospective / real-world validation." / "前瞻性验证、真实世界验证怎么设计？"
- "Map my model's threshold to a clinical action / net benefit."
- "Where does this sit in the PACS/RIS workflow?"
- "Is this site ready for silent deployment, local acceptance, active rollout, monitoring or
  retirement?" / "Which implementation-science framework and outcomes fit this study?"

## Operating modes

Choose the narrowest mode: `use-scenario`, `reader-study`, `clinical-impact`,
`regulatory-readiness`, `implementation-readiness`, `silent-deployment`,
`site-acceptance`, `implementation-evaluation`, `post-deployment-monitoring`,
`change-control/revalidation`, or `de-implementation/retirement`.

## When to open extra files

| File | Open when |
|---|---|
| [references/use-scenario.md](references/use-scenario.md) | Defining the clinical-use scenario, the model output, and the cost of errors |
| [references/reader-study.md](references/reader-study.md) | MRMC reader-study design: readers, washout, randomisation, with/without AI, outcomes |
| [references/threshold-to-action.md](references/threshold-to-action.md) | Mapping operating points to actions; net-benefit / decision-curve; false-positive/negative consequences |
| [references/prospective-deployment.md](references/prospective-deployment.md) | Prospective/real-world validation design; PACS/RIS integration; monitoring and drift |
| [references/regulatory-and-deployment-readiness.md](references/regulatory-and-deployment-readiness.md) | The user asks about clinical translation, FDA/EU/regulatory readiness, silent deployment, locked/adaptive models, model cards, lifecycle monitoring, or whether a retrospective AI/radiogenomics model can claim clinical use |
| [references/clinical-impact-study-design.md](references/clinical-impact-study-design.md) | Selecting controlled MRMC, sequential reading, silent prospective, pragmatic/cluster randomized, stepped-wedge, interrupted-time-series or active-deployment/RWE designs for the intended claim |
| [references/human-factors-and-implementation.md](references/human-factors-and-implementation.md) | Workflow fit, automation bias, alert burden, usability, training, overrides/abstention, implementation outcomes and sociotechnical failure analysis |
| [references/evidence-state-and-translation-lifecycle.md](references/evidence-state-and-translation-lifecycle.md) | Always when judging maturity/readiness or coordinating T0-T6; separates seven evidence axes and their claim ceilings |
| [references/implementation-science-and-scale-up.md](references/implementation-science-and-scale-up.md) | Selecting CFIR/NASSS, RE-AIM/PRISM, Proctor outcomes, ERIC strategies, hybrid designs, scale-up or de-implementation |
| [references/deployment-interoperability-and-site-acceptance.md](references/deployment-interoperability-and-site-acceptance.md) | DICOM/IHE/PACS/RIS/EHR/worklist integration, output display/identity, failure fallback or end-to-end site acceptance |
| [references/production-monitoring-and-change-control.md](references/production-monitoring-and-change-control.md) | Active deployment monitoring, label-delay blind intervals, incidents/CAPA, change/revalidation, rollback, stop or retirement |
| [references/source-registry.md](references/source-registry.md) | Any rule-bearing regulatory, interoperability, human-factors, reporting or implementation claim; refresh volatile sources for the target context |
| [templates/clinical-translation-state-card.md](templates/clinical-translation-state-card.md) | A durable seven-axis translation state and T0-T6 handoff artifact is requested |
| [templates/production-monitoring-contract.md](templates/production-monitoring-contract.md) | A monitor/release/event/change contract is requested |

## Workflow

1. **Accept or create the clinical-domain lock.** When disease-specific context matters, receive
   from `radiology-clinical-domain` the population/pathway, decision point, intended use,
   reference-standard, treatment-time, subgroup/access, harm and claim-ceiling fields. Return there
   if any clinical fact or changing standard is unresolved; do not manufacture a pathway inside a
   reader-study plan.
2. **Freeze the seven-axis state** (`evidence-state-and-translation-lifecycle.md`) and the exact
   intervention release. Select one current mode and the earliest unsupported decision; do not use a
   single readiness score.
3. **Define the use scenario** (use-scenario.md) — where in the pathway, who acts on the output,
   what the output is (risk score, stratification, mask, heatmap, report aid), error costs.
4. **Set the threshold-to-action map** (threshold-to-action.md) — operating point(s), the action
   each triggers, and net-benefit framing across plausible thresholds.
5. **Select the clinical-impact design** (clinical-impact-study-design.md). Do not use a controlled
   MRMC experiment to claim real-world outcome benefit, or an uncontrolled before–after rollout to
   claim causality.
6. **Design the reader study** (reader-study.md) when reader performance is the estimand — MRMC or
   justified sequential workflow, case sampling, information availability, order/carryover/learning,
   alone vs +AI, abstention/failures and task-matched outcomes.
7. **Map human factors and implementation** (human-factors-and-implementation.md): user roles,
   workstation/context, training, workload, alert/override behavior, automation bias, failure recovery,
   implementation outcomes and equity/access effects.
8. **For implementation evaluation/scale**, open `implementation-science-and-scale-up.md`; select
   frameworks by job, link strategies to determinant evidence and keep implementation outcomes
   separate from clinical outcomes.
9. **For regulatory/deployment framing**, open `regulatory-and-deployment-readiness.md` and
   bound the claim by intended use, model lock/adaptation, human oversight, monitoring, and
   evidence level.
10. **Plan prospective/real-world validation** (prospective-deployment.md) — temporal/prospective/
   RWE design, workflow position, monitoring for drift, failure handling.
11. **For a real local integration or active release**, run
    `deployment-interoperability-and-site-acceptance.md` and/or
    `production-monitoring-and-change-control.md`; preserve identity/display/fallback/site-test,
    denominator/label-delay/CAPA/rollback/retirement evidence.
12. **Bound the claim** — state exactly what level of evidence supports what level of claim;
   route statistics to `radiology-stats` and reporting to `radiology-reporting`.

## Output contract

1. **`Use scenario`** — pathway position, decision-maker, output type, error costs.
2. **`Seven-axis translation state`** — technical, clinical-validation, impact, regulatory,
   economic, implementation and production states; current T0-T6 position, stale evidence and claim ceiling.
3. **`Threshold-to-action map`** — operating point(s) → action; net-benefit/DCA framing.
4. **`Reader-study design`** (if applicable) — readers, washout, randomisation, arms, outcomes,
   statistic (MRMC → radiology-stats).
5. **`Regulatory/deployment readiness`** — intended use, locked/adaptive status, oversight,
   change-control/revalidation, monitoring, and exact items needing live verification.
6. **`Prospective/real-world plan`** — design, workflow integration, monitoring, drift.
7. **`Human-factors/implementation plan`** — users, context, workload, training, alert/override/
   abstention behavior, failure recovery, implementation outcomes and sociotechnical risks.
8. **`Implementation-science contract`** — framework-role map, determinant evidence, strategies,
   implementation/clinical outcomes, adaptation/equity and scale/de-implementation boundary.
9. **`Site-acceptance and production contract`** — when applicable: release, DICOM/IHE/system tests,
   monitoring denominators/thresholds, blind intervals, incidents/CAPA, rollback/revalidation/retirement.
10. **`Evidence-to-claim matrix`** — each supplied design/evidence axis, its supported claim,
   assumptions/biases and prohibited stronger inference; do not force unlike designs onto one ladder.
11. **`Evidence transition register`** — current evidence, next required study/artifact, success
   criterion, owner, and claim unlocked; preserve failures and drift/incident plans.

## Quality bar

A good translation plan names the clinical decision, chooses a design and analysis matched to the
estimand, ties thresholds to actions and explicit assumptions, plans the next decision-bearing
evidence, and never lets retrospective performance masquerade as clinical readiness.

## Maintainer validation

After changing a translation route, scientific boundary, source or template, run
`scripts/validate_translation_skill.ps1`. It checks the independent package, modes, boundaries,
sources, local links and prohibited over-absolute hierarchy language; it is a static contract test,
not evidence that a study, site or regulatory route passed.

## Handoffs

- Disease/pathway, reference-standard, treatment-time, population representativeness and current
  clinical-standard facts ↔ `radiology-clinical-domain`; this skill returns the reader/prospective/
  threshold/deployment design and does not overwrite the supplied clinical lock.
- MRMC / net-benefit / decision-curve statistics → `radiology-stats`.
- Formal economic estimand/model/HTA evidence → `radiology-health-economics`; DCA remains a clinical
  decision-analysis input and is not cost-effectiveness.
- Qualitative determinants/interviews/mixed-method integration →
  `radiology-qualitative-mixed-methods`; operational RACI/site rollout → `radiology-research-ops`.
- Executable release/replay evidence → `radiology-reproducibility`.
- Reader-study reporting, DECIDE-AI / CONSORT-AI for trials → `radiology-reporting`.
- The validation cohort / temporal design → `radiology-design`.
- Reader-study figures, net-benefit plots → `radiology-figure`.
- Reader/utility/deployment tables → `radiology-table`; program state and gate evidence →
  `radiology-pipeline`.
- Plans research and evaluation only; no individual-patient clinical or diagnostic advice.
