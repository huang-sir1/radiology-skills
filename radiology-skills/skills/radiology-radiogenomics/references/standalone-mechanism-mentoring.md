# Standalone mechanism research: mentoring, review, interpretation, and writing

Use this module when the scientific question is mechanism-first and does not begin with radiology, radiomics, or an imaging phenotype. It supports bulk RNA, single-cell or single-nucleus RNA, spatial assays, pathology, and perturbation as independent research routes. Do not force an imaging bridge into a mechanism-only request.

## Operating boundary

- A mechanism is a discriminating explanation of how a defined factor changes a biological state or outcome; a pathway label, enrichment score, cell-state name, proximity score, or model attribution is not a mechanism.
- Start from the biological contrast, inferential unit, tissue and time context, not from the fashionable method.
- Review mode locates evidence and judges claims; mentor mode generates bounded options and next actions; combined mode reports what survives review before redesigning the missing link.
- Predictions, mappings, deconvolution, trajectories, communication scores, and virtual perturbations remain computational evidence until tested against scale-compatible observations or interventions.
- Never invent sample access, assay capability, cohort size, effect, validation, citation, or completed experiment.

## Three orthogonal labels

Record all three fields for every material result or proposed evidence item.

1. **Primary evidence state** — use only `measured`, `derived`, `estimated`, `associated`, `predicted`, or `perturbed`.
2. **Modality subtype** — name the actual source, for example `bulk-rna/counts`, `single-cell/snRNA`, `spatial/spot-based`, `pathology/mIF`, or `perturbation/CRISPRi`; never use a generic “omics” label when the assay subtype changes resolution or interpretation.
3. **Claim-link** — use `direct` when the evidence observes the named link at the declared scale, `inferred` when the link depends on a model or biological interpretation, and `proposed` when it is a testable future link.

These labels are independent. A measured transcript can support only an inferred regulatory claim; a perturbed target can still have an inferred link to the clinical phenotype if target engagement or mediation is unresolved.

## Mechanism-first operating sequence

1. Define population or system, exposure or factor, comparator, biological response, time, and inferential unit.
2. State the exact mechanism distinction the study must resolve, not merely the phenomenon it will describe.
3. Build the resource passport and mark each input `known`, `missing`, `working assumption`, or `not applicable`.
4. Separate active measured modalities from external atlases, generated layers, and proposed validation assays.
5. Construct H1, H2, and H3 before choosing the integration method or writing the central claim.
6. Audit identity, assay validity, independence, confounding, multiplicity, and scale before interpreting biology.
7. Select the conservative, standard, or advanced route and state why its information gain justifies its burden.
8. Build a claim-evidence-mechanism ledger using the three labels above and stable claim IDs.
9. Decide each central claim as `PASS`, `CONDITIONAL`, or `STOP`; grade defects separately as `P0`, `P1`, or `P2`.
10. Return an executable next step, failure criterion, claim ceiling, and writing language allowed now.

## Mechanism question tree

Begin with one sentence:

`In [system/population], does [factor/exposure] alter [cell, tissue, or molecular process] over [time] relative to [comparator], through [candidate link], as distinguished from [alternative] by [decisive observation]?`

Expand it into six branches:

- **Phenomenon:** what reproducible state, transition, phenotype, or outcome needs explanation?
- **Source:** which cell, compartment, clone, or tissue structure could generate the signal?
- **Process:** which regulatory, metabolic, signalling, interaction, or structural process is implicated?
- **Direction and time:** what precedes what, and is the proposed link initiation, maintenance, adaptation, or consequence?
- **Alternative:** which composition, injury, treatment, batch, sampling, or reverse-direction explanation could mimic it?
- **Discriminator:** what measurement, control, intervention, rescue, or time series would separate the explanations?

Reject a branch when its decisive test cannot be linked to the proposed claim at the available scale. Preserve the nearest answerable descriptive or associative question rather than decorating an unidentifiable mechanism.

## Resource passport

| Domain | Facts that change the route |
|---|---|
| Biological system | species, disease/model, tissue, compartment, exposure, comparator, endpoint, time |
| Units and nesting | donors, patients, animals, organoids, samples, regions, cells, spots, fields, technical replicates |
| Provenance | patient-to-sample, specimen-to-section, region/coordinate, collection time, treatment interval |
| Bulk RNA | extraction source, strandedness, depth, raw counts, QC, purity/composition, paired design, batch |
| Single-cell | scRNA or snRNA, chemistry, raw matrices, cell/sample QC, ambient RNA, doublets, donor counts |
| Spatial | platform, feature space, spot/cell resolution, section identity, histology, coordinates, segmentation, registration |
| Pathology | specimen, H&E/IHC/mIF/WSI subtype, block/section, preanalytics, marker validity, scan and algorithm QC |
| Perturbation | intervention, assignment, dose/time, target engagement, controls, rescue, phenotype readout |
| External evidence | atlas or public cohort identity, population match, access, role, overlap and independence |
| Analysis | estimand, covariates, multiplicity, missingness, validation split, uncertainty and negative controls |
| Delivery | decision needed, stage, audience, writing section, time/cost constraints, claim target |

Report the matched biological-unit count at every modality intersection. Cell, spot, gene, tile, section, or read counts do not replace donor, patient, animal, or independently assigned experimental-unit counts.

## Modality-specific decision routes

### Bulk RNA

- Use for tissue-level expression, pathway, isoform, co-expression, or response questions when the bulk sample is the correct unit; state whether composition itself is the phenomenon or a confounder.
- Audit RNA quality, library design, raw-count access, normalization, design matrix, batch, repeated measures, tumour purity, multiplicity, and whether signature scoring or deconvolution was validated in context.
- Differential expression or enrichment is `associated`; regulatory direction is usually claim-link `inferred`.
- A mechanism claim needs cell-source resolution or orthogonal tissue evidence plus a discriminating perturbation, temporal observation, or mediation design appropriate to the biological question.

### Single-cell or single-nucleus RNA

- Define donor-level estimands before clustering; distinguish cell discovery from patient-level generalization.
- Audit ambient RNA, doublets, low-quality cells/nuclei, integration, annotation evidence, malignant-cell logic, sample representation, donor-aware differential tests, and unseen-population behaviour.
- Clusters, trajectories, RNA velocity, regulons, and communication scores are `derived` or `estimated`; their mechanistic claim-links remain `inferred` unless supported by temporal, orthogonal, or perturbational evidence.
- Do not treat cells as independent donors or label transfer as direct validation of a state in a new condition.

### Spatial assays

- Define whether the target is localization, gradient, neighbourhood, boundary, niche, cell interaction, or dynamics.
- Audit section provenance, platform resolution, tissue integrity, coordinates, segmentation, transcript assignment, spatial autocorrelation, patient replication, reference mapping, and registration uncertainty.
- A measured spot count can directly locate a transcript at spot scale but cannot directly assign it to a cell; deconvolved cell abundance, reconstructed cells, imputed genes, and communication are `estimated`.
- Co-localization raises plausibility; it does not establish direction, signalling, necessity, or sufficiency.

### Pathology

- Use declared subtypes such as `pathology/H&E`, `pathology/IHC`, `pathology/mIF`, or `pathology/WSI-model`.
- Preserve patient-specimen-block-section-region-field hierarchy and review preanalytics, marker specificity, pathologist definitions, scan quality, segmentation, phenotype rules, batch handling, and blinded assessment.
- Morphology, marker expression, density, neighbourhood, and tissue architecture can supply orthogonal context, but a correlated marker or WSI feature does not by itself prove the proposed molecular mechanism.
- Route detailed pathology-only work to the independent pathology mechanism guidance.

### Perturbation and virtual perturbation

- Distinguish observed intervention from predicted response. An in-silico knockout is `predicted`, not `perturbed`.
- For observed perturbation, record assignment, perturbation efficiency, off-target risk, dose, time, controls, target engagement, phenotype measurement, biological replication, and rescue or orthogonal perturbation.
- Perturbing a gene and observing a transcriptomic shift does not automatically connect it to tissue function or disease outcome; label the remaining cross-scale claim-link `inferred`.
- Require comparison with simple baselines and test generalization across condition, donor, cell type, and out-of-distribution settings before using predicted perturbation to prioritize experiments.

## Cross-modality triangulation

For each proposed bridge record:

`claim_id | source modality subtype | primary evidence state | target layer | claim-link | unit/scale/time | independence | alternative explanation | discriminating test | current verdict | maximum wording`

- Agreement between bulk deconvolution and a single-cell reference is not independent confirmation when the same atlas, genes, or composition assumptions generate both results.
- Spatial localization can validate location while leaving causal direction unresolved.
- Pathology can validate morphology or protein context while leaving target necessity unresolved.
- Perturbation can test necessity or sufficiency only for the manipulated system, dose, time, and measured endpoint.
- Discordance is diagnostic: test platform limits, cell composition, sampling, time, model transfer, and real biology before averaging conflicting layers into one score.

## Conservative, standard, and advanced routes

### Conservative route

Use current measured data to establish a reproducible phenomenon and bounded association. Add sensitivity analysis, negative controls, explicit alternatives, and honest writing. Choose this when matching, sample size, assay access, or intervention capacity cannot support a stronger bridge.

### Standard route

Add one orthogonal modality or cohort that resolves the weakest necessary link, plus sample-aware validation and a predefined discriminating analysis. Prefer this route when it offers the best balance of identifiability, feasibility, time, cost, and reviewer risk.

### Advanced route

Add longitudinal, spatial, lineage, multi-system, or perturbation-and-rescue evidence that tests direction and transportability. Use it only when identity, replication, assay capability, and analysis capacity are credible; do not recommend it merely because it is technologically impressive.

For all three routes report: required inputs, primary evidence state produced, modality subtype, claim-link upgraded, matched n, success criterion, failure criterion, time/cost driver, and claim permitted if the route fails.

## H1/H2/H3 portfolio

- **H1:** the preferred biological mechanism, expressed as a directional and scale-specific chain.
- **H2:** a plausible biological alternative that predicts at least one different observation.
- **H3:** a technical, sampling, composition, treatment, batch, or model-transfer explanation.

For each hypothesis specify supporting observations, contradicting observations, decisive test, expected pattern, and what result would downgrade it. Add more hypotheses only when they change a decision; never use H2/H3 as decorative limitations after selecting H1.

## Gate logic and STOP rescue

Use `P0` for a defect that can invalidate the central result or make the mechanism non-identifiable, `P1` for a major weakness that may be repairable without reversing the bounded claim, and `P2` for clarity or reproducibility.
Use `PASS`, `CONDITIONAL`, and `STOP` for claims or decision gates, not as synonyms for severity.

Immediate STOP examples include broken unit identity, pseudoreplication, perfect condition-batch confounding, generated values reported as measured, association reported as perturbation, or a mechanism claim with no evidence that distinguishes H1 from H2/H3.

When STOP applies, return:

`blocked mechanism -> exact blocking reason -> nearest answerable question -> evidence needed to restore the original question -> wording allowed now -> smallest executable next step -> success/failure criterion`

Preserve valid descriptive, technical, or associative findings. A STOP is a route correction, not a rejection of the entire project.

## Mentoring and decision support

- Teach `principle -> provided/inspected evidence -> consequence -> verdict -> options -> recommendation -> action`.
- Ask at most three questions when the answers would change the estimand, route, validity, or major deliverable.
- Recommend one route and explain why the others lose; do not return an unranked catalogue of methods.
- Separate facts supplied by the learner from inspected artifacts, working assumptions, and mentor-generated ideas.
- Challenge overclaiming directly while showing the nearest viable mechanism question and the evidence that could change the decision.
- For early learners, define unit, contrast, evidence state, claim-link, confounding, and mechanism with one worked decomposition; for advanced learners, prioritize identifiability, transportability, counterfactuals, and falsifiers.

## Writing contract

### Title and abstract

Name the biological system, actual modality subtype, and study type. Use “associated with,” “localized to,” or “predicted” unless the evidence directly supports stronger wording. Do not headline a virtual perturbation as a knockout experiment or an enrichment as pathway activation.

### Methods

Reconstruct biological-unit identity, specimen and time provenance, assay subtype, QC and exclusions, preprocessing, estimand, covariates, multiplicity, validation, software/reference versions, and every generated or mapped layer.

### Results and figures

Lead with claim IDs and effect plus uncertainty, not workflow completion. State donor/patient/experimental-unit n, the primary evidence state, modality subtype, claim-link, validation role, and denominator in every relevant legend. Report negative and discordant evidence that changes H1/H2/H3.

### Discussion and conclusion

Separate observation, interpretation, prediction, and intervention. Discuss H2/H3, scale and time limits, generalizability, unresolved direction, and the shortest evidence upgrade. The conclusion may not exceed the weakest necessary link in the ledger.

## Standard output

1. Route declaration and completed resource passport.
2. One-sentence question and H1/H2/H3 mechanism tree.
3. Evidence ledger using the three orthogonal labels.
4. Severity-ranked findings and claim-level `PASS/CONDITIONAL/STOP` decisions.
5. Conservative, standard, and advanced plans with one recommendation.
6. STOP rescue where applicable, plus immediate action and completion criterion.
7. Claim ceiling and ready-to-use wording for the requested section.
8. Missing inputs marked `AUTHOR_INPUT_NEEDED`; no invented completion claims.

## Final self-check

- Did the route begin from a mechanism distinction rather than a method or imaging phenotype?
- Are primary evidence state, modality subtype, and claim-link recorded separately and consistently?
- Are donor/patient/experimental units distinct from cells, spots, fields, sections, and technical replicates?
- Do H1, H2, and H3 predict discriminating observations?
- Does every stronger verb have scale-compatible evidence, independence, and validation?
- Are P0/P1/P2 separate from PASS/CONDITIONAL/STOP?
- Does each STOP include a viable rescue and wording allowed now?
- Can the learner execute the recommended next step without guessing hidden requirements?
