# Parameter, evaluation-metric and methodology assessment

This is the canonical scientific reference owned by `radiology-method-evaluation`. Use it when the
user asks whether a study's parameters or methods are reasonable, requests
a hyperparameter or sensitivity section, wants a methodology-focused manuscript review, or needs to
write the parameter/method-evaluation evidence into a paper. It applies to `imaging-only`,
`mechanism-only` and `imaging-mechanism` work.

This is a scientific-validity audit, not a formatting checklist and not a numerical quality score.
A severe method defect is not cancelled by many well-reported parameters.

## 1. Declare the three objects separately

| Object | Meaning | Core question | Do not confuse it with |
|---|---|---|---|
| Parameter or setting | a value, rule, range or learned choice that configures acquisition, preprocessing, analysis, model fitting or decision-making | Was it defined, justified, selected without leakage, frozen at the right time and tested over a plausible range? | an evaluation metric |
| Evaluation metric or readout | the quantity used to judge data quality, model performance, biological effect, robustness or utility | Does it measure the stated task at the correct unit and threshold, with uncertainty and an interpretable reference? | a tunable objective that was optimized and then reported on the same data |
| Methodology | the design and operations that connect the question, estimand, data, assumptions, analysis and claim | Can this method identify or estimate what the manuscript claims, relative to credible alternatives? | popularity, software availability or fluent Methods prose |

If the user supplies only a manuscript, audit what is reported and mark execution `NOT VERIFIED`.
If raw data, code or logs are supplied and the user asks for computation, verify selected settings and
run proportionate sensitivity checks. Never imply that a reported analysis was rerun when it was not.

## 2. Coverage and judgement vocabulary

For each applicable row report:

- **Coverage:** `APPLICABLE`, `NOT APPLICABLE` or `NOT ASSESSED`.
- **Scientific judgement:** `PASS`, `CONDITIONAL` or `STOP`.
- **Finding severity:** `P0`, `P1` or `P2`, kept separate from the scientific judgement.
- **Evidence state:** `PLANNED`, `AUTHOR_REPORTED`, `PARTLY_VERIFIED`, `VERIFIED` or
  `NOT_ASSESSABLE`.

Do not calculate an aggregate score. One outcome-informed threshold, test-set-tuned hyperparameter or
invalid independent unit can determine the affected claim even when other rows pass.

## 3. Intake and evidence surfaces

Inventory only the materials supplied:

- protocol/SAP and preregistration;
- manuscript Methods, Results, figures, tables and Supplementary Information;
- acquisition or assay protocol, configuration files, parameter tables and software versions;
- code, environment/lock file, random seeds, tuning logs, experiment tracker and model card;
- raw/processed data, split manifest and cohort/sample topology;
- validation results, ablations, robustness plots and failure cases.

Record exact file/version/digest or manuscript locator when available. Missing code or a missing
configuration is an evidence boundary; it is not proof that the method was executed incorrectly.

## 4. Reconstruct the method before judging it

Write the pipeline as ordered decisions:

`question/estimand -> population/specimen and unit -> measurement -> preprocessing -> representation
-> parameter selection -> model/test -> evaluation metric -> validation -> interpretation/claim`.

For every stage ask:

1. What input enters and what output leaves?
2. Which choices are fixed, learned, estimated, derived or selected by a human?
3. When was each choice made and which data/outcomes were visible?
4. Which assumption makes the operation valid?
5. Which later claim depends on it?

If the pipeline cannot be reconstructed, issue a reporting/reproducibility finding before speculating
about the scientific effect of an unknown setting.

## 5. Parameter registry and validity test

Create one row per decision-bearing parameter or linked group:

`Parameter ID | stage | name/unit | value or range | role | source/rationale | chosen when | data visible
| search space/budget | selection objective | validation scope | freeze state | software/version | sensitivity
| affected Claim IDs | judgement`.

### Parameter roles

| Role | Examples | Required evidence |
|---|---|---|
| fixed by protocol or hardware | voxel size, slice thickness, assay chemistry, magnification, dose/time | protocol/source, unit, allowable variation and deviations |
| externally standardized | IBSI discretization convention, validated clinical cutoff, established assay threshold | exact authority/version and applicability to this setting |
| data-derived without outcome | QC distribution rule, unsupervised factor count, image normalization reference | derivation set, rule, stability and avoidance of outcome peeking |
| learned/tuned | regularization, learning rate, feature count, cluster resolution, neighbourhood radius | search space, budget, objective, inner validation and selected value |
| analyst-selected | smoothing, cutoff, inclusion threshold, visualization range | rationale, timing, plausible alternatives and sensitivity |
| downstream decision threshold | positivity cutoff, operating point, clinical action threshold | intended consequence, selection data, uncertainty, freeze and validation |

### Parameter validity questions

- **Definition:** Is the value, unit, reference category and software/version explicit?
- **Rationale:** Is the choice supported by physics, biology, clinical use, external standard, pilot
  work or a declared optimization objective? A package default alone is not a scientific rationale.
- **Timing and isolation:** Was it chosen before viewing the protected validation/test outcome? Were
  QC, imputation, harmonization, feature selection and threshold choices contained within training
  or discovery data?
- **Search integrity:** Are search space, budget, selection metric, stopping rule and inner/outer
  validation scope reported? Comparing many settings and reporting only the winner is selective.
- **Freeze and transport:** Was the chosen pipeline frozen before external/temporal/platform
  validation? State what was refit, recalibrated or reannotated.
- **Sensitivity:** Does the material conclusion persist over scientifically plausible values,
  alternative seeds and reasonable implementations? Test interacting parameters when one-at-a-time
  perturbation would be misleading.
- **Failure boundary:** Identify the value/range where the result, label, ranking, localization,
  significance or claim changes materially.

Do not demand an exhaustive grid for every incidental parameter. Prioritize parameters that can
change cohort inclusion, labels, representation, leakage, the primary estimate, model selection,
spatial identity, mechanism interpretation or clinical action.

## 6. Evaluation-metric validity

For each headline metric or biological readout record:

- task and estimand it is intended to measure;
- independent unit and aggregation level;
- direction and meaningful reference/baseline;
- threshold or operating-point dependence;
- uncertainty interval or resampling unit;
- class prevalence, censoring, missingness or spatial composition dependence;
- whether it was also the tuning objective;
- complementary metric needed to expose a known blind spot;
- affected claim and wording ceiling.

Examples of mismatches include accuracy in a strongly imbalanced cohort without class-specific
performance; AUC used as clinical utility; Dice used as the sole evidence of boundary accuracy;
cell-level p values used for donor-level claims; silhouette score used as proof of biological cell
identity; enrichment score used as pathway activation or mechanism; correlation used as spatial
co-localization; and a tuned metric reported on the same data without optimism control.

## 7. Methodology evaluation chain

### M1 — Question, estimand and design fit

- Is the question answerable with the stated population/system, comparator, endpoint and time?
- Does the design support description, association, prediction, treatment effect, mechanism or
  causality at the claimed level?
- Is the intended use or biological object clear enough to choose a method?

### M2 — Measurement, reference and unit validity

- Do acquisition/assay, annotation/reference standard and QC measure the claimed object?
- Are patient, lesion, block, section, donor, cell/spot, ROI/tile and time hierarchies preserved?
- Are missingness, exclusions, batch/site/platform and treatment timing handled without changing the
  estimand silently?

### M3 — Analytical method and assumptions

- Does the method match data type, distribution, hierarchy, pairing, censoring, sparsity and
  dimensionality?
- Are assumptions stated and examined? If an assumption fails, is the alternative method or claim
  boundary explicit?
- Is analyst flexibility bounded by a protocol, analysis lock, complete result table or sensitivity
  analysis?

### M4 — Comparators, ablations and negative controls

- Is the nearest credible baseline evaluated on matched data, split, tuning budget and metrics?
- Do ablations isolate the advertised component rather than merely show the full pipeline works?
- Are negative controls, spatial nulls, batch controls or rival biological explanations tested when
  they can reproduce the claimed pattern?

### M5 — Validation and transport

- Distinguish internal resampling, held-out internal, temporal, external-site, cross-platform,
  cross-disease/condition and prospective validation.
- State exactly what object was frozen and what distribution changed.
- Report failures, heterogeneity and degradation, not only the average favourable result.

### M6 — Reproducibility and claim compatibility

- Can another team reconstruct cohort flow, sample topology, preprocessing, parameters, software,
  code, seeds, model/checkpoint and evaluation?
- Do Results, figures, tables, legends, supplement and availability statements agree?
- Does the strongest claim remain within the method's identification and validation boundary?

## 8. Scope adapters: decision-bearing examples

| Scope/modality | Parameters and method choices that commonly require explicit evaluation |
|---|---|
| image formation/quantitation | series/phase/sequence acceptance, acquisition/contrast/tracer, reconstruction/postprocessing, quantitative DICOM transforms, artifacts/dose, phantom/test-retest, site qualification and protocol drift; consume the frozen `radiology-acquisition-qc` passport |
| radiomics/imaging analysis | registration, resampling grid/interpolator, discretization/bin width, segmentation perturbation, feature-stability rule, harmonization covariates, feature selection and model/threshold freeze |
| deep imaging/pathology | resolution, crop/patch and magnification, augmentation, architecture/pretraining, loss/optimizer/schedule, class handling, search space/budget, seed/checkpoint, aggregation and operating threshold |
| bulk RNA | sample/gene filtering, normalization, design matrix/contrast, batch/composition handling, dispersion/model family, effect/FDR thresholds, gene-set universe and score/cutoff |
| sc/snRNA | cell/gene/mitochondrial QC, ambient/doublet handling, normalization/HVG, integration, PCs/neighbours/resolution, annotation confidence, pseudobulk unit, trajectory root and communication thresholds |
| spatial | tissue/cell segmentation, QC, coordinate/registration error, deconvolution, smoothing/imputation, domain resolution, neighbourhood radius/k, spatial null, patient/region aggregation and mapping sensitivity |
| multi-omics/fusion | matched intersection, missing-modality policy, scaling, latent dimension/factor number, modality weighting, alignment objective, unimodal/paired ablation and freeze across validation |
| perturbation | assignment threshold, MOI, guide efficiency, dose/time, target-engagement cutoff, off-target rule, control/rescue design and response readout |
| imaging–mechanism | every active modality above plus patient–lesion–region–block–section–cell/time mapping, bridge parameter sensitivity and discordance handling |

Use the active `radiology-acquisition-qc` modality playbook for image-formation and quantitative-
measurement rules, then the downstream domain playbook for analysis choices. Do not import a
parameter requirement from another modality merely because it appeared in a high-impact paper.

## 9. Sensitivity and robustness design

For each decision-bearing parameter choose the smallest analysis that can change the decision:

| Risk | Minimum assessment | Stronger option when justified |
|---|---|---|
| arbitrary cutoff or QC threshold | repeat across a prespecified plausible band; report inclusion and primary-result changes | blinded/frozen rule plus external replication |
| learned hyperparameter | nested or separate validation with declared search space and objective | repeated nested validation or independent tuning cohort |
| cluster/domain/neighbourhood setting | stability of labels, composition and downstream conclusion across plausible settings | consensus/stability analysis plus orthogonal reference |
| stochastic training | multiple declared seeds with distribution of primary metrics and failure cases | external validation across site/platform shifts |
| preprocessing/harmonization | alternate defensible pipeline and preservation of biological/clinical signal | negative-control features and site-aware transport test |
| operating/positivity threshold | performance/readout and consequence across a meaningful threshold range | prospectively fixed threshold tied to clinical/experimental action |
| method-family choice | matched credible alternative and assumption comparison | simulation/known truth or orthogonal measurement |

Report the actual direction, magnitude and claim consequence of sensitivity analyses. “Results were
robust” without the tested range, unit, estimate and location is not closure evidence.

## 10. Writing and display placement

| Location | Required job |
|---|---|
| Methods | name values/ranges, units, parameter role, rationale/source, selection timing and data, search/selection rule, freeze point, software/version and deviations |
| Results | report only decision-bearing sensitivity, metric comparison, ablation and failure results with effect/uncertainty; state whether the primary conclusion changed |
| Figure/table | show parameter–result or method–result relationships when they materially affect interpretation; label unit, range, reference, uncertainty and validation set |
| Supplement/config/code | provide the complete parameter register, search space, configurations, seeds, secondary robustness results and executable provenance |
| Discussion | state dependence on unresolved parameters/method assumptions, transport limit and the nearest claim that remains stable |
| Abstract/title | include no parameter or method superiority claim that depends on a hidden favourable setting or an unmatched comparator |

Do not fill the main text with every software default. Keep the shortest sufficient chain visible and
move reconstructive detail to the supplement/configuration with an exact main-text pointer.

## 11. Constructive finding and output contract

Every decision-bearing finding records:

`Finding ID -> object (parameter/metric/method) -> affected stage and Claim IDs -> coverage and
evidence state -> typed evidence anchor -> observed issue -> governing criterion -> P0/P1/P2 ->
PASS/CONDITIONAL/STOP consequence -> minimum feasible repair -> optional stronger route ->
cost/trade-off -> closure evidence -> writing locations -> residual boundary`.

Return, in this order:

1. audit scope and evidence/coverage receipt;
2. methodology-fit matrix;
3. parameter registry;
4. evaluation-metric/readout matrix;
5. sensitivity and robustness matrix;
6. genuine strengths and atomic findings;
7. Methods/Results/Figure/Supplement/Discussion placement plan;
8. claim-level verdict and the single next decision-bearing action.

Use [the reusable matrix](../templates/parameter-methodology-evaluation-matrix.md) when a durable
artifact helps. Missing material remains `AUTHOR_INPUT_NEEDED`; never invent a parameter, range,
search, metric, assumption, result, software version or validation.
