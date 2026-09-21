# Noisy, weak and report-derived label contract

Use this reference when labels come from routine reports, billing/diagnostic codes, NLP/LLM extraction,
heuristics, distant supervision, model-assisted annotation, incomplete follow-up or another process
that is cheaper but less direct than a task-appropriate reference standard.

Weak labels may support development; they do not become clean truth through volume.

## 1. Name the label evidence state

| State | Example | Required boundary |
|---|---|---|
| `DIRECT_REFERENCE` | pathology or prespecified expert/reference process appropriate to the construct | document its own error/timing limits |
| `ADJUDICATED_REFERENCE` | independent reads plus frozen adjudication | preserve component reads and adjudication rule |
| `REPORT_DERIVED` | label extracted from report text | report content/omission/hedging and extraction error both apply |
| `CODE_DERIVED` | ICD/procedure/registry code | billing/selection meaning may differ from clinical construct |
| `RULE_WEAK` | heuristic/keyword/metadata rule | publish rule, conflict/abstention and audit performance |
| `MODEL_PSEUDO` | teacher/model prediction | circularity and correlated error; never primary evaluation truth |
| `HUMAN_MODEL_ASSISTED` | reader edits a prelabel | record model/version and assistance effect |
| `UNVERIFIED` | inferred from absence or incomplete follow-up | not negative; retain uncertainty state |

Each row needs `source_type`, source locator/version, transformation/prompt/code version, confidence or
uncertainty, adjudication state and snapshot digest.

## 2. Define the weak-label mechanism

Before training, state:

- target construct, unit and time window;
- how each source observes or misses it;
- expected false-positive/false-negative and subgroup/site/documentation mechanisms;
- whether errors depend on disease severity, scanner/site, reader, treatment or outcome;
- how conflicting sources are combined and when the system abstains;
- which clean/adjudicated subset remains independent for calibration and final evaluation.

Do not assume label noise is random. Routine reports selectively mention findings; codes reflect care
and reimbursement; follow-up depends on clinical concern; pseudo-label errors follow the teacher.

## 3. Report-derived labels

- Specify report type/version (preliminary/final/addendum), section(s), author role and timestamp relative
  to the image and outcome.
- Preserve negation, uncertainty, conditional language, laterality, anatomy, severity and historical
  versus current findings. “Not mentioned” is neither absent nor assessed.
- Remove templated/copied text and near-duplicate patient reports across partitions; keep longitudinal
  reports with the patient.
- Record NLP/LLM model, checkpoint/API date, exact prompt/rules, retrieval/context, decoding and post-
  processing. Human correction produces a new label state with its own provenance.
- Audit against images plus the defined reference evidence, not only against the same source report.

## 4. Label-function and conflict contract

For every heuristic/model/source, record:

```text
label_function_id -> construct -> inputs -> output/value set -> abstention -> version -> expected
dependency -> development data used -> audited sample -> confusion/error profile -> allowed role
```

- Keep abstentions visible; forcing coverage can increase systematic misclassification.
- Do not treat correlated rules as independent votes. Shared vocabulary, source reports or upstream
  models create dependent errors.
- Freeze rule weights/conflict resolution before protected-reference evaluation.
- If active learning or iterative relabeling uses evaluation errors, move those cases to development
  and reserve a new untouched evaluation set.

## 5. Clean-set design and audit

Create a patient-level, reference-quality set sampled to expose important error mechanisms—not only an
easy random subset. Include normal/positive/indeterminate, subtle/severe, site/modality/protocol,
demographic and report-style strata.

Use it to estimate:

- per-class sensitivity, specificity/precision and abstention/coverage with CIs;
- laterality, negation, uncertainty, temporal and severity errors;
- source/site/subgroup variation and disagreements;
- calibration of probabilistic labels if they are used as probabilities;
- effect of label source on downstream performance in a prespecified sensitivity analysis.

The final model must be evaluated on a clean/adjudicated set independent of weak-label construction and
model/prompt selection. Report both weak-label audit and final task performance.

## 6. Modeling routes and evidence boundaries

Possible routes include exclusion/abstention, probabilistic labels, loss correction, robust training,
co-teaching, positive–unlabeled methods or human review. Select from the stated noise mechanism and
validate against the independent clean set; no method universally “solves” noisy labels.

- Report label-source ablations and performance as clean-label fraction changes.
- Prevent patient/site leakage and keep all label-generation fitting inside development partitions.
- A weak-label model may learn documentation or site behavior rather than imaging pathology; test
  label-source/site prediction and external transport.
- Pseudo-label confidence is model output, not evidence of correctness.

## 7. Stop gates and output

Return `STOP_FOR_REPAIR` when label provenance is missing, report-derived absence is encoded as negative
without justification, the same model/source defines both training and primary evaluation labels,
protected clean cases influenced rule/model selection or patient duplicates cross partitions.

Return:

`construct card -> label-source/mechanism map -> rule/model/prompt manifest -> conflict/abstention policy
-> independent clean-set design -> label audit/error profile -> downstream sensitivity -> claim ceiling
-> deviations`.

Allowed claim: “trained/evaluated using the stated weak-label process and independent reference set.”
Forbidden leap: “large-scale ground truth” or biological/clinical validity based only on report/code/
pseudo-label agreement.

## Primary sources

- Irvin J, et al. [CheXpert](https://arxiv.org/abs/1901.07031) (original report-label uncertainty framework and dataset study).
- Ratner A, et al. [Snorkel](https://doi.org/10.14778/3157794.3157797) (original data-programming system).
- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).

These sources illustrate methods/reporting; they do not validate a new label source. The project must
measure its own label error against the task-specific reference process.
