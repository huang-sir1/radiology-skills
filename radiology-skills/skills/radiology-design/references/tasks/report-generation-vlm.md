# Report generation and vision-language-model study contract

Use this contract for image/report-conditioned drafting, impression generation, structured finding
extraction, report correction, visual question answering or other radiology VLM/LLM tasks. Name the
exact task: a model that generates fluent text is not necessarily factually correct, clinically safe or
useful in workflow.

## 1. Freeze the use and information boundary

| Field | Required specification |
|---|---|
| User/workflow | radiologist, trainee, referring clinician or research pipeline; when output is shown |
| Task | draft findings/impression, structured extraction, comparison, QA, retrieval or another fixed task |
| Input | modality/series/views, report text, priors, indication and clinical data available at inference |
| Output | free text, structured fields, answer, ranked evidence or correction suggestion |
| Unit | patient/examination/report; preserve episodes and longitudinal reports together |
| Reference process | original/final report, multi-reader adjudication, pathology/follow-up or task-specific evidence |
| Primary estimand | factual/clinical error rate, completeness, decision effect, time or another patient-level contrast |
| Human authority | review/edit/sign-off, abstention/escalation and prohibited autonomous actions |
| Model state | provider, exact model/checkpoint/API snapshot, prompt/template, retrieval corpus and decoding settings |

Distinguish a report as a **label source** from a reference standard. Reports contain omissions,
hedging, copied text and interpretation; agreement with one report does not prove imaging truth.

## 2. Cohort, privacy and contamination contract

- Define exams through the intended pathway and include normal, subtle, multiple-finding, post-treatment,
  altered-anatomy and poor-quality cases. Report prevalence and report-style/source distribution.
- Split by patient and keep serial exams, reports, addenda, near-duplicate templates and paired modalities
  together. Audit pretraining/fine-tuning/retrieval corpora for test overlap where evidence is available;
  otherwise label contamination risk `NOT_ASSESSABLE`.
- Remove direct identifiers and assess rare-text, dates, accession numbers, burned-in annotations and
  retrieval logs. De-identification does not itself authorize data/model-provider transfer.
- Freeze prompt, system instructions, exemplars, tool/retrieval versions and decoding. Adaptive API
  models require dated snapshots or repeated-drift checks; a brand name alone is not reproducible.
- Prevent label leakage from final impressions, pathology, follow-up or post-decision text unless those
  inputs are available at the intended moment of use.

## 3. Reference and evaluation process

Create a clinically anchored error taxonomy before scoring:

- omitted, invented or contradicted finding;
- wrong anatomy, side, size, severity or temporal comparison;
- negation/uncertainty failure;
- unsupported diagnosis or recommendation;
- missed urgent/critical communication requirement;
- internally inconsistent findings and impression;
- citation/retrieval attribution failure;
- privacy or prohibited-action failure.

Use qualified readers, standardized instructions, blinding, calibration cases, independent review and
adjudication. Preserve individual judgments and disagreement. If reference reports are used, verify a
sample against images and available clinical reference evidence.

## 4. Metric stack

Primary evaluation should be patient/examination-level clinical correctness or error severity with
uncertainty. Add as appropriate:

- finding-level precision/recall with ontology and matching rules;
- omission/commission and critical-error rates;
- laterality, negation, uncertainty and longitudinal-comparison accuracy;
- calibration/selective performance and abstention coverage;
- reader edit distance **and** semantic/clinical change categories;
- time, cognitive workload, acceptance/override and automation-related errors;
- subgroup/site/modality performance and failure-rate denominators.

BLEU, ROUGE, embedding similarity and a model-as-judge score are secondary proxies. They cannot alone
establish clinical correctness. A model judge requires version/prompt, calibration against qualified
human ratings, agreement/error analysis and independence from the system under test.

## 5. Comparators and validation

- Compare with the real baseline: unaided reporting, template/structured-report tool, retrieval-only
  method or prior system—not only another foundation model.
- Freeze development and untouched site/time test sets. Report any local prompt/model adaptation
  separately and evaluate it on a further independent set.
- Stress test absent findings, conflicting priors, incomplete series, unusual terminology, rare disease,
  adversarial/copied text, retrieval failure and provider/API drift.
- A retrospective text benchmark supports benchmark performance only. Reader impact needs a randomized/
  counterbalanced reader study; live workflow and safety need prospective evaluation and monitoring.

## 6. Sample size, stop gates and governance

Plan from the patient-level primary error/contrast, event/finding prevalence, reader/reference
variability, paired design, site/modality strata and desired precision. Sentence/token counts are not n.

Return `STOP_FOR_REPAIR` for patient/report leakage, test prompts tuned on reported test scores, an
untraceable model/API state, PHI transfer without verified authority, model-as-judge-only clinical
claims, missing critical-error denominator or autonomous clinical action outside the approved study.
Escalate unresolved privacy, provider, medical-device and deployment requirements to ethics/governance
and regulatory owners.

## 7. Claim boundary and handoff

- Text similarity -> similarity to the selected references only.
- Human-adjudicated factual performance -> bounded correctness under that cohort/reference process.
- Controlled reader study -> effect under that reading design.
- Prospective deployment study -> workflow/safety effect under that live configuration.

Return: `VLM-use card -> data/privacy/contamination receipt -> model-prompt-retrieval manifest ->
reference/error-taxonomy protocol -> metric/sample-size brief -> human evaluation and stress matrix ->
monitoring/change-control plan -> claim ceiling -> deviations`.

## Primary sources

- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).
- Gallifant J, et al. [TRIPOD-LLM](https://doi.org/10.1038/s41591-024-03425-5).
- Vasey B, et al. [DECIDE-AI](https://doi.org/10.1038/s41591-022-01772-9).

TRIPOD-LLM applies to relevant prediction/diagnosis studies using LLMs; it does not replace CLAIM,
task-specific accuracy/impact design or live regulatory verification.
