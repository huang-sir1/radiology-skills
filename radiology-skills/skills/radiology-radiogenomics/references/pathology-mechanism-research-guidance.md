# Independent pathology mechanism research: review, design, interpretation, and writing

Use this module for pathology-first mechanism questions that do not require a radiology or radiomics starting point. It covers H&E, immunohistochemistry (IHC), multiplex immunofluorescence (mIF), and digital pathology or whole-slide imaging (WSI) as measurements of tissue architecture, markers, cells, and spatial organization. It does not replace diagnostic sign-out, laboratory assay validation, ethics review, or clinical regulation.

## Scope and claim boundary

- Define the tissue phenomenon and the mechanism distinction before choosing stains, markers, or algorithms.
- Morphology, marker signal, phenotype density, proximity, and WSI patterns can support a tissue explanation; none automatically proves pathway activity, cell function, signalling, temporal order, or causality.
- “Pathology ground truth” is allowed only for a narrowly defined endpoint with an appropriate reference standard, blinded expert annotation or consensus, and declared uncertainty.
- A representative field, one marker, one section, or one high-performing WSI model cannot represent an entire heterogeneous lesion, patient trajectory, or universal biological mechanism without supporting design.
- Preserve the nearest valid morphological, localization, or association claim when a mechanism claim is blocked.

## Evidence-language contract

Record three independent fields for every endpoint and link:

1. **Primary evidence state:** exactly one of `measured`, `derived`, `estimated`, `associated`, `predicted`, or `perturbed`.
2. **Modality subtype:** for example `pathology/H&E`, `pathology/IHC`, `pathology/mIF`, `pathology/WSI-morphology`, or `pathology/WSI-algorithm`.
3. **Claim-link:** `direct` for an observed link at the declared scale, `inferred` for a model- or interpretation-dependent link, and `proposed` for a future testable link.

Use the fields orthogonally:

- Slide pixels, stain signal, or a declared marker readout are `measured` at their assay scale.
- Prespecified scores, counts, densities, ratios, and morphology features calculated from measurements are `derived`.
- Segmentation labels, phenotype classifications, latent embeddings, imputed markers, and model-generated maps are `estimated`.
- Patient-aware relationships between pathology endpoints and a condition or outcome are `associated`.
- A locked WSI model evaluated on unseen patients produces `predicted` evidence for its declared target.
- An observed intervention with assignment, target engagement, controls, and phenotype readout is `perturbed`.
- A measured marker can still have claim-link `inferred` to a cell state, pathway, interaction, or function.

## Pathology question and estimand

Write one sentence:

`In [population/system], does [tissue structure, marker-defined compartment, or spatial organization] differ under [exposure/condition] versus [comparator] at [specimen/region/time], and does it support [mechanism distinction] against [alternative] through [discriminating evidence]?`

Specify population, eligible specimens, exposure/contrast, primary pathology endpoint, denominator, time, independent unit, intended use, and maximum claim before examining group differences. Separate these questions:

- What tissue structure is present and how reproducibly can it be measured?
- Which cell or compartment carries the signal?
- Is the signal localized, enriched, or spatially organized beyond an appropriate null?
- Does the signal precede, accompany, or follow the phenotype of interest?
- Does intervention change the proposed factor and the relevant tissue or functional endpoint?

## Specimen hierarchy and provenance

Write the actual nesting chain and retain every identifier:

`patient/donor or independently assigned unit -> procedure/time -> specimen -> lesion/site -> block -> section -> region/field/tile -> cell/object -> stain or technical repeat`

- Patients, donors, animals, or independently assigned experimental systems determine biological replication.
- Blocks, sections, fields, tiles, and cells improve measurement density but do not create independent patients.
- Record paired/repeated status, tissue source, procedure, anatomical site, orientation, section depth/order, serial-section distance, recuts, tissue loss, exclusions, and all assay-to-assay matching.
- Same block is not identical tissue; serial sections permit approximate regional comparison, not automatic single-cell colocalization.
- Report eligible, available, stained, QC-passing, matched, and analysed independent units separately.

## Pathology resource passport

| Domain | Required facts |
|---|---|
| Question | population/system, exposure, comparator, endpoint, denominator, unit, time, intended claim |
| Sampling | eligibility, availability mechanism, specimen type, lesions, block/section/ROI selection, exclusions |
| Preanalytics | ischaemia, fixation delay/type/duration, decalcification, processing, block/section age, storage |
| H&E | stain/run, section quality, tissue compartments, annotation definitions, reader roles and blinding |
| IHC | target, clone, vendor/catalogue/lot, dilution, retrieval, detection, controls, scoring and threshold |
| mIF | markers/fluorophores, panel order, single-stain controls, unmixing, autofluorescence, spillover, phenotype rules |
| WSI | scanner, objective/effective resolution, pixel size, focus, compression, file conversion, QC and colour handling |
| Algorithm | task, annotation source, split by patient, version, thresholds, uncertainty, held-out performance, failure handling |
| Spatial analysis | coordinate units, tissue mask, compartments, radius/graph rule, edge correction, null model, multiplicity |
| Analysis | estimand, patient-level n, nesting, covariates, missingness, multiplicity, effect/uncertainty, sensitivity |
| Validation | discovery/validation role, overlap, locked procedure, independent cohort/system, orthogonal or perturbational test |

Mark every field `known`, `missing`, `working assumption`, or `not applicable`. Do not infer fixation, blinding, controls, scanner, marker identity, or patient matching from a representative image or filename.

## Preanalytical and selection gate

- Define eligible specimens and the block/section/ROI sampling rule before viewing the target result.
- Record tissue availability and whether it depends on disease severity, treatment, resectability, site, outcome, specimen size, archival age, or the proposed mechanism.
- Prefer systematic, random, or prespecified stratified sampling over visually interesting fields.
- Log warm/cold ischaemia, fixation, processing, decalcification, archive, sectioning, staining, and scanning variables.
- Check balance and overlap of preanalytics across biological groups and sites; adjust or stratify only when the comparison remains identifiable.
- `STOP` the affected biological comparison when condition is perfectly confounded with fixation, staining run, scanner, specimen type, or another unbroken technical factor.
- Missing historical metadata remain unknown; they do not become “standard practice.” Lower the claim and use available quality proxies and sensitivity analyses without pretending they remove the uncertainty.

## H&E route

- Predefine tissue compartments and features: viable tumour, necrosis, fibrosis, vessels, stroma, inflammation, invasive margin, architecture, grade-related morphology, or another operationally defined structure.
- Declare pathologist number, training/calibration, blinding, repeat reads, agreement, adjudication, and whether annotations define the endpoint or only supply algorithm training labels.
- Measure usable tissue area and denominator; distinguish absence from unassessable tissue.
- A morphology annotation is direct for the examined section and definition, but its link to a protein, molecular program, whole-lesion property, or function remains inferred.
- Representative images illustrate the distribution; they do not replace analysis of all eligible units.

## IHC route

- Record target, clone, vendor, catalogue, lot, dilution/concentration, incubation, antigen retrieval, platform, detection chemistry, expected localization, positivity rule, and known limitations.
- Use appropriate positive and negative tissues or compartments, within-run controls, batch-bridging material, and repeat or orthogonal confirmation for unexpected or central weak signals.
- Define compartment, intensity/localization, cell/tissue denominator, scoring rule, threshold origin, and handling of necrosis, pigment, background, edge artefact, and exhausted tissue.
- One marker rarely defines a complex cell state, pathway, activation, treatment sensitivity, or causal driver.
- A threshold optimized against the same outcome is exploratory unless frozen and evaluated on unseen patients.

## mIF route

- Justify the panel by the mechanism distinction; do not maximize marker count without tissue and validation budget.
- Review antibody compatibility, fluorophore balance, staining order, single-stain controls, spectral unmixing, autofluorescence subtraction, spillover, batch bridging, tissue loss, and dynamic range.
- Predefine a phenotype hierarchy with justified combinations of markers, morphology, compartment, and an `ambiguous/unclassified` option; validate it against blinded expert review on held-out representative fields.
- Carry segmentation and phenotype uncertainty into densities and neighbourhood estimates.
- Co-expression or proximity can be direct for the measured panel and spatial rule, but ligand-receptor signalling, interaction direction, activation, and function remain inferred without discriminating evidence.

## WSI and algorithm route

- Inventory folds, tears, chatter, bubbles, debris, pen, coverslip artefact, saturation, uneven illumination, out-of-focus areas, stitching errors, compression, missing levels, and unusable tissue by patient and group.
- Trace scanner, resolution, pixel size, focus policy, colour profile, file format, conversion, and software version.
- Fit colour normalization, segmentation, representation learning, thresholds, and classifiers inside training data; freeze them before patient-level validation and verify that harmonization preserves relevant morphology.
- Split patients, not tiles or fields. Prevent adjacent sections, repeated scans, blocks, or stain variants from crossing training, tuning, and test roles.
- Validate tissue, compartment, nucleus/cell, phenotype, and spatial tasks separately where each affects the endpoint.
- Report task-appropriate performance, calibration where applicable, site/stain shift, uncertainty, hard cases, class imbalance, subgroup behaviour, and downstream sensitivity to segmentation or threshold perturbation.
- Saliency, attention, latent clusters, and embeddings are estimated explanations, not direct tissue mechanisms.

## Patient-level inference

- State the primary patient- or experimental-unit endpoint, aggregation rule, compartment, denominator, and direction.
- Use patient-level summaries or hierarchical/mixed models that preserve sections, ROIs, fields, tiles, and cells within their biological unit; model repeated lesions or procedures explicitly.
- Report independent-unit n before object counts, effect size and interval, patient consistency, influential units, covariates chosen from design/causal reasoning, and missingness or attrition by group.
- Correct the declared family of markers, compartments, phenotypes, radii, regions, features, endpoints, and subgroups.
- A very small p value from thousands of cells does not repair a small number of independent patients.
- Use patient-preserving permutations, cluster-aware bootstrap, or small-sample methods only when their assumptions and resolution are appropriate and stated.

## Spatial and temporal interpretation

- Declare coordinate units, tissue masks, compartment boundaries, radius or graph construction, edge handling, minimum counts, and a spatial null that preserves patient identity and relevant tissue geometry.
- Density, segmentation, tissue area, geometry, and radius can create apparent neighbourhood effects; test these alternatives and multiplicity before interpreting organization.
- Patient-level association permits no finer regional claim than the sampled and mapped tissue supports.
- Cross-sectional sections do not establish temporal order. Record procedure time, exposure/treatment interval, disease stage, and whether material is baseline, on-treatment, post-treatment, recurrent, or autopsy tissue.
- Longitudinal claims require repeated biological units with compatible sampling and an analysis that separates within-unit change from cohort composition and treatment selection.

## Competing explanations and mechanism claim ceiling

Require at least:

- **H1:** preferred tissue/cellular mechanism with source, process, direction, scale, and time.
- **H2:** plausible biological alternative, such as another cell source, injury response, stromal process, composition change, or reverse direction.
- **H3:** technical or sampling alternative involving fixation, staining, block/ROI choice, scanner, segmentation, threshold, density, batch, or selection.

For each, record predicted observation, contradiction, decisive test, primary evidence state, modality subtype, claim-link, and failure criterion. The weakest necessary link sets the ceiling:

- Reproducible morphology or marker presence supports a descriptive statement at the examined scale.
- Patient-aware differences support an association after confounding and multiplicity assessment.
- Spatial concordance supports localization under the declared sampling and null, not signalling or direction.
- A locked WSI model supports prediction in its tested population and platform, not biological causation.
- Mechanistic wording requires evidence that distinguishes H1 from H2/H3; directional or causal wording generally needs temporal or perturbational evidence, target engagement, controls, and preferably orthogonal confirmation or rescue.

## Stage gates and decisions

| Gate | PASS | CONDITIONAL | STOP examples |
|---|---|---|---|
| Question/estimand | endpoint, unit, contrast, time and claim are explicit | bounded exploratory target | undefined post-hoc mechanism |
| Provenance/selection | complete hierarchy and prespecified sampling | transparent availability sampling | wrong/unknown unit or result-selected regions |
| Preanalytics/assay | controlled variables and fit-for-purpose assay | residual uncertainty is sensitivity-tested | condition fully confounded with batch or failed controls |
| Reader/algorithm | blinded reproducible read or locked held-out model | bounded use with known error | outcome-informed labels or test-set tuning |
| Inference | patient-aware model, uncertainty and multiplicity | identifiable but imprecise | cells/tiles treated as independent patients |
| Spatial/time | claim matches sampling, mapping and time | coarser localization only | cross-sectional or unmatched evidence claimed directional |
| Mechanism | alternatives are discriminated at compatible scale | plausible candidate mechanism | marker/proximity/association alone claimed causal |
| Writing/release | all sections match evidence and ceiling | exact wording repair suffices | estimated output reported as measured or validation overstated |

Grade defects separately: `P0` can invalidate a central result or make the claim non-identifiable; `P1` is a major repairable weakness; `P2` improves clarity or reproducibility. Decide claims and gates with `PASS`, `CONDITIONAL`, or `STOP`. Do not convert one system mechanically into the other.

## Validation and STOP rescue

- **Minimum:** blinded review, reproducible endpoint, patient-aware association, negative controls, and sensitivity.
- **Standard:** an orthogonal marker/panel or independent locked cohort that resolves the weakest link.
- **Mechanism-advancing:** longitudinal or perturbation evidence with target engagement, appropriate controls, functional readout, orthogonal confirmation, and rescue where scientifically feasible.

When a central claim is `STOP`, return:

`blocked claim -> exact blocking condition -> nearest valid pathology question -> minimum new evidence -> wording allowed now -> smallest executable repair -> completion criterion`

Do not prescribe “more IHC,” “more cases,” or “AI validation” without naming the endpoint, specimen frame, assay, controls, independent unit, analysis, and claim-link the repair is intended to upgrade.

## Writing contract

### Methods

Report study role, matched hierarchy counts, eligibility and exclusions, sampling rules, specimen/preanalytics, stain and marker details, controls, reader/blinding, scanner and WSI QC, algorithm splits/version/thresholds, endpoint and denominator, patient-level model, multiplicity, missingness, and sensitivity analyses.

### Results

Report eligible through analysed patient counts before cells or tiles; preanalytic and batch balance; effect and interval; patient consistency; reader/algorithm performance and failures; sensitivities; concordant and discordant cases; and each endpoint's primary evidence state, modality subtype, and claim-link.

### Figure legends

State patients, specimens, blocks, sections, ROIs/fields, and cells separately; stain/marker, compartment, scale bar, scanner/resolution, processing, annotation/segmentation rule, threshold, denominator, representative-image rule, independent unit, statistical model, interval, multiplicity, and serial-section status.

### Title, abstract, discussion, and conclusion

Use “associated with,” “localized to,” “marker-positive,” or “algorithm-estimated” when those are the actual results. Do not replace them with “drives,” “mediates,” “activation,” “interaction,” “ground truth,” or “validated mechanism” without the necessary evidence. Discuss H2/H3, preanalytics, tissue coverage, algorithm error, spatial/time boundary, transportability, and the shortest mechanism-upgrading experiment.

## Standard output and final check

Return: question and route; specimen passport; evidence ledger; severity-ranked findings; gate decisions; H1/H2/H3; assay/control and patient-level analysis plan; conservative, standard, and mechanism-advancing validation options; claim ceiling; STOP rescue; ready-to-use writing; and one next executable action.

Before release confirm that every result uses the three orthogonal labels, nesting is preserved, patient-level n is visible, preanalytics and selection are auditable, algorithms are patient-split and locked, spatial/time wording matches the sampling, P0/P1/P2 are distinct from PASS/CONDITIONAL/STOP, and no mechanism verb outruns the weakest link.
