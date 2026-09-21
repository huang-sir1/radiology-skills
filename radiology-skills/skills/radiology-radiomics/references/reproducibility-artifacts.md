# Radiomics reproducibility artifacts

The manuscript paragraph is not the pipeline. Preserve enough artifacts to rerun and audit it.

## Minimum bundle

| Artifact | Required content |
|---|---|
| Cohort/split manifest | patient IDs or irreversible hashes, cohort role, center, split/fold, exclusion reason |
| Image/mask manifest | image and mask IDs, modality/phase, preprocessing input, geometry QC status |
| Parameter file | resampling, interpolation, normalization, discretization, filters, feature families, software/version |
| Feature dictionary | original IBSI/PyRadiomics name, display name, family, units/transform, source image/filter |
| Feature-count trail | extracted -> QC -> stable -> de-correlated -> selected -> final model, with rule and fit scope |
| Fitted pipeline | imputer/scaler/harmonizer/selector/model objects or exact reconstruction route |
| Signature map | full-precision coefficients/intercept/baseline survival and reproducible score equation |
| Evaluation output | patient-level predictions, outcome, cohort, timepoint, bootstrap/resampling identifiers |
| Environment/run manifest | code commit/version, packages, OS/runtime, seed, command/config, timestamp |
| Deviation log | planned versus executed decisions and sensitivity analyses |

Use stable IDs rather than patient-identifying information in shareable artifacts.

## Fit-scope field

Every data-dependent artifact records where it was fitted:

`fixed a priori`, `training only`, `inner fold`, `outer fold`, `development cohort`, or `external
application only`.

Any imputer, scaler, harmonizer, ICC/stability filter, correlation filter, selector, threshold, or
cut point recorded as fitted on the full dataset fails the leakage gate unless the task is explicitly
descriptive and no validation claim is made.

## Feature naming

Never shorten feature names differently across coefficient table, heatmap, nomogram, equation, and
Methods. Keep one dictionary and one display label. Preserve the original machine name for reruns.

## Count reconciliation

Feature counts must form a continuous trail. If stages overlap or branch, state why; do not present
an impossible arithmetic sequence. Reconcile the trail with flow/pipeline figures and supplementary
feature tables.

