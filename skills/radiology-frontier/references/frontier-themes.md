# Frontier themes and their data prerequisites

A theme is only a frontier *for a given dataset*. For each, the question is not "is it hot?" but
"can this data carry it, and is the gap still open?" Verify currency with live search
(→ radiology-search); treat the list as orientation, not a closed taxonomy.

| Theme | What it is | Data prerequisites | Common failure / when to avoid |
|---|---|---|---|
| **Foundation models / transfer** | Large pretrained imaging (or vision-language) encoders fine-tuned to a task | Enough cases to fine-tune+validate; honest external test | Small single-center data won't show generalisable gain over a strong baseline |
| **Self-supervised pretraining (SSL)** | Pretrain on unlabelled images, fine-tune on few labels | Large unlabelled pool + a labelled downstream set | Claiming SSL benefit without a fair supervised baseline |
| **Vision-language / report-aware** | Link images to radiology reports / text | Paired image–report data, de-identified | Report leakage (model sees the label it should predict) |
| **Multimodal fusion** | Combine imaging + clinical + pathology/molecular + text | Matched modalities on the same patients | Fusion that underperforms the best single modality; missing-modality handling |
| **Longitudinal / delta** | Model change over time (delta-radiomics, growth) | ≥2 timepoints, registrable, consistent protocol | Inconsistent acquisition across timepoints; registration error as "signal" |
| **Weak / semi / noisy-label** | Learn from imperfect labels (report-mined, partial masks) | A clean validation set with trustworthy labels | Evaluating on the same noisy labels used to train |
| **Domain adaptation / harmonisation** | Transport across scanners/sites | Multi-center/scanner data | Calling random-mixed held-out folds "external" |
| **Federated learning** | Multi-center training without sharing data | Real multi-site governance + heterogeneity | Reproducibility and heterogeneity under-reported |
| **Generative (synthesis/augmentation)** | Synthetic images, denoising, super-resolution, harmonisation | Task where synthesis has a defined downstream benefit | Synthetic data inflating performance; no real-data validation |
| **Uncertainty / OOD / safety** | Calibrated confidence, out-of-distribution detection | A defined deployment distribution to test against | Uncertainty reported but never acted on |
| **Interpretability / mechanism** | Saliency, concept attribution, radiogenomics | For mechanism: **matched** imaging+omics (→ radiology-radiogenomics) | Over-interpreting saliency maps as biology |
| **Radiogenomics / imaging-multi-omics** | Imaging phenotype ↔ molecular biology | Matched imaging∩omics intersection (the binding constraint) | Non-matched public omics written up as direct validation |
| **AI + reader / prospective / RWE** | Clinical-utility, reader studies, prospective validation | Reader pool / prospective enrolment path | Retrospective AUC claimed as clinical readiness (→ radiology-translation) |

## Fit test (apply to every candidate)

1. **Prerequisite check** — does the data meet the row's prerequisites? If no → reject or
   downgrade to the version it can support.
2. **Gap check** — is the question still open, or already answered? (verify live).
3. **Bar check** — what validation does a top venue expect for this theme? Can the user reach it?
4. **Increment check** — what is the *specific* advance over the best existing approach, in one
   sentence? If you can't write it, it's not yet a frontier question.

## Hot-but-often-unsuitable (call these out)

- Foundation models / SSL on small single-center cohorts with no external test.
- Multimodal fusion when one modality already explains the outcome.
- Generative augmentation as the headline result with no real-data validation.
- "Explainable AI" panels presented as mechanism without molecular data.
