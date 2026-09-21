# Imaging–mechanism reviewer response playbook

Use this only when a manuscript claims a connection between an imaging phenotype/model and a tissue,
cellular, molecular, spatial, pathology or perturbational mechanism. Apply the imaging and mechanism
checks, then verify the bridge; parallel valid modalities are not automatically a valid connection.

| Reviewer concern | Decision-bearing question | Honest response path |
|---|---|---|
| Small matched cohort | what is the usable matched patient/lesion intersection for this claim? | show modality flow and matched n, reduce complexity/multiplicity, validate or declare discovery-only status |
| Imaging and tissue mismatch | do patient, lesion, region/habitat, biopsy/section, time and treatment align? | add the mapping table and registration/timing evidence; if coordinates are absent, keep the inference patient-level |
| Scanner, site, assay or batch confounding | can technical origin reproduce the cross-modal association? | report joint batch variables, train-only harmonization, covariate/batch-only sensitivity and the resulting change |
| Multimodal advantage | is the gain over the strongest single modality real and fairly estimated? | use matched splits and preprocessing, current single-modality/clinical baselines, paired uncertainty and failure cases |
| Fusion-method contribution | which component earns the claimed advantage? | add applicable ablations/sensitivity tests; do not require algorithmic ablations for a non-method paper |
| Cross-scale mechanism claim | what is directly measured, associated, predicted or perturbed? | expose the evidence-state ledger, serious biological and technical rivals, and the missing discriminating link |
| External validation | was the frozen object tested on an independent cohort/site/platform? | report the independent test and result or narrow to internal discovery; never rename cross-validation as external |
| Spatial/localized claim | does measurement resolution support region/cell localization? | quantify registration/segmentation error and spatial nulls; keep wording at the coarsest supported level |
| Clinical utility/treatment benefit | is there a comparator, calibration, workflow or treatment interaction? | report the applicable evidence or retain prognostic/association wording; no deployment or benefit claim from retrospective AUC alone |

When a request cannot be met, answer with:

`scope and criterion -> why the requested evidence is unavailable/inapplicable -> best feasible
sensitivity or clarification -> exact claim reduction -> revised locations -> residual limitation`.

Do not promise a new molecular assay for an imaging-only claim or an imaging experiment for a
mechanism-only claim. If the authors change scope during revision, return to `radiology-radiogenomics`
and rebuild the scientific packet before drafting the response.

