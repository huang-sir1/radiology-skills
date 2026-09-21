# Equity, stakeholder and participation gate

This is a cross-lifecycle gate, not a substitute specialist. It asks whether the research question,
sample, measurement, analysis, deployment and communication represent the people and workflows to
which the claim will apply.

## Gate passport

Freeze:

`intended population/use setting -> actual recruitment/referral/access path -> stakeholder groups and
decision authority -> imaging burden and harms -> representation/measurement gaps -> equity estimand
and uncertainty -> action threshold -> owner and next review date`.

Distinguish patient/public **involvement**, research **participation** and one-way **engagement**. Their
governance, evidence and reporting are not interchangeable.

## Owner map

| Decision | Unique owner | Gate handoff |
|---|---|---|
| who shaped the question, endpoint, burden, threshold and dissemination | `radiology-design` | PPI/equity decision ledger |
| participant rights, consent/waiver, return of results and authorized data/tissue use | `radiology-ethics` | document-verified authorization receipt |
| cohort coverage, missingness, access, data provenance and controlled sharing | `radiology-data` | lifecycle inventory/access route |
| annotation/reference-standard comparability and reader effects | `radiology-annotation` | subgroup measurement/label audit |
| estimand, interaction, precision, multiplicity and intersectional analysis | `radiology-stats` | analysis/uncertainty plan |
| workflow access, human factors, subgroup harm, monitoring and scale | `radiology-translation` | implementation/monitoring contract |
| delivery responsibilities, site readiness and issue escalation | `radiology-research-ops` | RACI/readiness/risk record |
| funder-facing plan and resourcing | `radiology-grant` | criterion/evidence/budget mapping |
| reporting of involvement/equity | `radiology-reporting` | versioned checklist locations |
| public/patient communication | `radiology-dissemination` | audience/claim/accessibility receipt |

## Imaging-specific minimum audit

Check referral and scanner access, site/vendor/protocol spectrum, radiation/contrast/tracer and repeat
scan burden, pediatric/older/disabled/language needs, incidental findings, privacy acceptability,
reference-standard/label quality across groups, false-positive/false-negative/downstream-test harm,
availability of the clinical action after an alert, and digital/workflow exclusion after deployment.

For every decision-bearing group contrast record the independent unit, denominator, missingness,
measurement equivalence, effect/CI, multiplicity, threshold and action if the criterion fails. Do not
declare fairness from balanced counts, one non-significant interaction, equal AUC alone or a post hoc
dashboard.

## Status and consequences

- `PASS`: target and actual populations are reconciled; involvement/authority is evidenced; planned
  estimands, harms, thresholds and remediation owners are explicit.
- `CONDITIONAL`: a named limitation survives with a narrower population/use claim and repair plan.
- `STOP`: participation/authorization is misrepresented, a vulnerable or excluded group bears
  unassessed material harm, the target population is unsupported by the sample/measurement, or a
  failed equity criterion has no action.
- `NOT_APPLICABLE`: permitted only with a reason tied to the actual claim and use setting.

## Sources

- World Medical Association. [Declaration of Helsinki, 2024](https://www.wma.net/policies-post/wma-declaration-of-helsinki/).
- SPIRIT–CONSORT. [Patient and public involvement item](https://www.consort-spirit.org/item11-patient-publicinvolvement).
- EQUATOR. [GRIPP2](https://www.equator-network.org/reporting-guidelines/gripp2-reporting-checklists-tools-to-improve-reporting-of-patient-and-public-involvement-in-research/).
- FDA. [Good Machine Learning Practice guiding principles](https://www.fda.gov/medical-devices/software-medical-device-samd/good-machine-learning-practice-medical-device-development-guiding-principles).

Sources were checked or routed on 2026-08-23. Re-verify live requirements at protocol, submission and
deployment; a reporting guideline does not prove equity or valid involvement.
