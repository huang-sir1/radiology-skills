# AI/radiogenomics pitfall audit

Use this reference during pre-submission review of radiology AI, radiomics, deep-learning, foundation-model, VLM, or radiogenomics manuscripts.

## High-risk failures

| Pitfall | Reviewer concern | Fix route |
|---|---|---|
| Single-center high AUC | likely optimism and poor generalisability | external/temporal validation or bounded venue/claim |
| Data leakage | patient/slice/timepoint overlap, feature selection before split, test-set tuning | redo split and train-only preprocessing |
| Scanner/site confounding | model learns institution/protocol rather than disease biology | site-aware split, subgroup analysis, harmonisation, sensitivity |
| Weak labels | report-mined/noisy labels used for both training and evaluation | clean reference-standard validation subset |
| AUC-only reporting | no calibration, DCA, failure cases, or clinical operating point | add calibration, net benefit, CIs, error analysis |
| Superficial XAI | heatmaps shown as mechanism | bound language; test stability and ROI/pathology agreement |
| Missing UQ/OOD | model cannot know when to abstain or request review | uncertainty, conformal, OOD, or referral rule |
| Radiomics reproducibility gap | no IBSI parameters, no segmentation reproducibility, no software versions | add IBSI/CLEAR details and stability analyses |
| Radiogenomics matched-n gap | unclear imaging-omics intersection or tissue-image mismatch | matched flow diagram and sample-to-image table |
| Mechanism overclaim | association described as causal biology | add pathway/spatial/pathology support or soften claim |
| Fairness blind spot | no subgroup performance across age/sex/site/scanner/demographics | subgroup analysis and limitation |
| Clinical-readiness overclaim | retrospective model described as deployable | route to reader/silent/prospective evidence |

## Seven-step mitigation check

1. Patient-level, site-aware, and time-aware partitioning.
2. Documented reference standard, acquisition protocol, and label generation chain.
3. IBSI/CLEAR-aligned radiomics or fully specified deep-feature extraction.
4. External testing and subgroup/site/scanner analysis.
5. Calibration, uncertainty, and failure analysis in the main evidence package.
6. Code/model/minimal reproducibility package where sharing is allowed.
7. Reader-assist, silent deployment, or prospective plan before clinical utility claims.

## Output row

```text
Pitfall:
Severity:
Manuscript location:
Why a reviewer will care:
Required fix:
Claim wording if not fixed:
```
