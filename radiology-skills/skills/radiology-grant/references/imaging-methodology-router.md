# Imaging methodology framework router for grants

Read this after the proposal's intended use, study type and strongest claim are frozen. Reporting
guidelines, appraisal tools and metrology standards reveal missing design functions; they are not
NSFC criteria, mandatory universal checklists or evidence that a project is valid, feasible or
fundable.

## Select by study function

| Study function | Primary framework(s) | Use in a grant | Important exclusion |
|---|---|---|---|
| General medical-imaging AI | CLAIM 2024 update | dataset, reference standard, model, evaluation and transparency completeness | CLAIM states that its update did not expand to radiomics, pathomics or imaging biomarkers; it is not a scoring scale |
| AI diagnostic-accuracy study | STARD-AI 2025 + diagnostic-accuracy design principles | index test, reference standard, threshold, flow, human-AI role and accuracy reporting | use the current version including corrections; reporting completion does not remove verification or spectrum bias |
| Clinical prediction model | TRIPOD+AI 2024 | model purpose, participants, predictors, outcomes, development, validation, performance and transparency | not a causal-inference or diagnostic-accuracy substitute |
| Prediction-model risk of bias/applicability | PROBAST+AI 2025 | population, predictors, outcome and analysis bias challenge | not a drafting template or score promise |
| Early live clinical AI evaluation | DECIDE-AI | workflow integration, user interaction, errors, safety and early clinical performance | reader improvement or workflow speed does not establish patient benefit |
| AI trial protocol/result | SPIRIT-AI / CONSORT-AI | intervention, human-AI interaction, failures, analysis and reporting | apply only when the proposed design is a clinical trial |
| Trustworthy/deployable healthcare AI | FUTURE-AI 2025 | fairness, universality, traceability, usability, robustness and explainability across lifecycle | broad principles do not replace a study-specific estimand or sample-size calculation |
| Generative healthcare AI | MI-CLAIM-GEN 2025 | model/version, prompting, reference construction, human review, hallucination and evaluation | fluent explanations are not biological mechanisms; hosted APIs require data-retention review |
| Radiomics reporting | CLEAR 2023 | acquisition, segmentation, preprocessing, features, modelling and validation reporting | CLAIM alone is insufficient for radiomics |
| Radiomics methodological quality | METRICS 2024 | method-completeness challenge during design | a quality score does not establish validity or fundability |
| Radiomic feature/preprocessing reproducibility | IBSI + 2024 standardized-filter work | definitions, parameters, software benchmarking and test objects | claimed IBSI compatibility still needs versioned benchmark evidence |
| Radiomics translation/readiness | RQS 2.0 (2025) | maturity, QC, harmonization, fairness, explainability and clinical translation challenge | score/readiness level does not establish independent validity |
| PET/SPECT radiomics | EANM/SNMMI guidance | tracer/acquisition/reconstruction and manual-feature nuclear-medicine radiomics | scope is not every deep-learning or non-nuclear study |
| Quantitative imaging biomarker | QIBA metrology + QIBA Profiles + DICOM | measurand, bias, precision, repeatability, protocol and metadata chain | technical conformity does not establish biological or clinical validity |

## Do not route every study to CLAIM

Freeze the dominant claim first:

- diagnostic accuracy → STARD-AI;
- prognostic/diagnostic prediction model → TRIPOD+AI + PROBAST+AI;
- radiomics → CLEAR + IBSI + METRICS, with RQS 2.0 for translation maturity;
- quantitative measurement → QIBA metrology/Profile + DICOM;
- early clinical deployment → DECIDE-AI, and a trial-specific AI extension if applicable;
- generative/report/VLM system → MI-CLAIM-GEN plus task-appropriate diagnostic, prediction or
  deployment framework.

Multiple frameworks may apply, but each must have a named function. Do not paste every checklist
into the proposal.

## Grant extraction card

For the selected frameworks extract only design-relevant functions:

```text
Study function and strongest claim:
Framework, version/correction and access date:
Design functions adopted:
Functions not applicable and why:
Proposal locations:
Unresolved design defect:
Effect on feasibility or claim ceiling:
```

Never write “the project follows CLAIM/STARD-AI/TRIPOD+AI, therefore the design is rigorous.” Report
the actual controls and evidence.

## Cross-framework imaging gates

### Multimodal intersection denominator

For imaging–clinical–pathology–omics studies, effective `n` is the successfully linked intersection
at the same patient/lesion/region/time window, not the sum of modality counts. Report loss and
missingness at every link.

### Aim-level sample-size memo

For every aim record the primary estimand, independent unit, design inputs and sources, plausible
scenarios, expected non-evaluable/loss, development/tuning/test allocation, method/software/version,
required `n` and accessible `n`. Do not use a universal 10-EPV rule or arbitrary AUC/Dice threshold.

### Reference-standard independence

In addition to definition, timing, readers, blinding, adjudication and reliability, audit index-test
blinding, partial/differential verification and incorporation bias. A label derived from the same
image or report is not automatically an independent truth.

### Data and model lineage

Audit dataset aliases, duplicate/near-duplicate examinations, the same patient across centres,
pretraining corpora, foundation-model weights, prompt/RAG data and hosted-API retention. If the model
may have seen the test source during pretraining, do not call the evaluation wholly independent.

### External-independence vector

Record independence separately for patient, centre, time, protocol, vendor, geography/population and
pretraining lineage. External data used for harmonization, recalibration, threshold selection,
fine-tuning or prompt selection are adaptation data; reserve an untouched test or lower the
transport claim.

### Mechanism evidence ladder

`association → independent replication → orthogonal pathology/molecular evidence → spatial or
temporal matching → targeted perturbation → rescue/counterfactual validation`.

Enrichment, correlation, SHAP, attention or heat maps alone do not establish mechanism. A pure
measurement or transport study need not add animal experiments; require higher-rung evidence only
when the proposal makes a mechanism/causal claim.

## Primary framework sources

- CLAIM 2024: https://doi.org/10.1148/ryai.240300
- STARD-AI: https://doi.org/10.1038/s41591-025-03953-8
- TRIPOD+AI: https://doi.org/10.1136/bmj-2023-078378
- PROBAST+AI: https://doi.org/10.1136/bmj-2024-082505
- FUTURE-AI: https://doi.org/10.1136/bmj-2024-081554
- MI-CLAIM-GEN: https://doi.org/10.1038/s41591-024-03470-0
- METRICS: https://pubmed.ncbi.nlm.nih.gov/38228979/
- IBSI standardized filters: https://doi.org/10.1148/radiol.231319
- RQS 2.0: https://doi.org/10.1038/s41571-025-01067-1
- DECIDE-AI: https://doi.org/10.1038/s41591-022-01772-9
- Quantitative-imaging biomarker metrology: https://doi.org/10.1148/radiol.2015142202
- DICOM current standard: https://www.dicomstandard.org/current/
- QIBA Profiles: https://qibawiki.rsna.org/index.php/Profiles

Verify the current framework version and correction status at use.
