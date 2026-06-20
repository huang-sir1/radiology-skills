# Radiogenomics reviewer playbook

Use this for pre-submission mock review and revision responses. Radiogenomics reviews usually
converge on the same questions.

## Common reviewer concern -> strong response path

| Concern | What the reviewer is testing | Strong response |
|---|---|---|
| Matched cohort is small | Overfitting and false discovery | State matched n, reduce complexity, pre-specify primary analysis, use FDR, validate externally |
| Imaging and tissue may not match | Spatial validity | Add sample-to-image mapping table, timing window, lesion/region relationship, bounded claims |
| Batch drives the association | Scanner/sequencing confounding | Report batch variables, ComBat/covariate models, batch-only sensitivity, association survival |
| No external validation | Generalisability | Freeze signature/model and test independent cohort; if impossible, downgrade claim to discovery |
| Too many tests | False positives | Define test family, apply BH-FDR/q-values, report full results, distinguish primary vs discovery |
| Feature pipeline unreproducible | Radiomics noise | Add IBSI parameters, software versions, segmentation ICC, feature stability, parameter YAML |
| Omics preprocessing unclear | Bioinformatics validity | Add assay-specific QC, normalization, filtering, batch, accession, software versions |
| Mechanistic overclaim | Correlation sold as biology | Reword to association, add pathway/cell/spatial corroboration, state alternative explanations |
| Patient-level leakage | Inflated performance | Confirm patient-level split, train-only preprocessing, nested CV, no sample/slice leakage |
| Missing data/code availability | Reproducibility | Provide accessions/DOIs/restriction wording and code archive where allowed |

## Pre-submission reviewer simulation
Return comments in this structure:

`Severity | Reviewer persona | Manuscript location | Issue | Why it matters | Required fix | Routed skill`

Reviewer personas:
- Imaging methods reviewer.
- Omics/bioinformatics reviewer.
- Biostatistics reviewer.
- Disease/clinical reviewer.
- Data-sharing/reproducibility reviewer.

## Revision response style
- Accept valid criticism quickly and show the concrete change.
- Cite the exact manuscript/supplement location after each change.
- If new analysis was added, report method and result; do not write "performed" without result.
- If a requested external validation is impossible, state why, soften the claim, and add the gap to
  limitations. Do not pretend internal CV is external validation.
- If disagreeing, use scientific reasoning and offer a sensitivity analysis or clarified wording.

## Response templates
External validation missing:
"We agree that independent validation is critical for establishing generalisability. We have now
[added/applied] the frozen [signature/model/association] to [validation cohort], with results
reported in [location]. Where validation was not available for [specific analysis], we have
reframed the result as exploratory and added this limitation in [location]."

Batch confounding:
"We agree that scanner and sequencing batch could confound radiogenomic associations. We added a
batch/covariate table and repeated the primary analysis with [method], preserving the biological
covariate of interest. The association [remained/materially changed]; the revised Results and
sensitivity analysis are reported in [location]."

Spatial mismatch:
"We clarified the relationship between the molecular sample and imaging phenotype in a new
sample-to-image mapping table. Because [coordinates/region] were [available/unavailable], we now
interpret the result as [region-specific/patient-level] and revised the Discussion accordingly."