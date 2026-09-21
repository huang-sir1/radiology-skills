# Synthetic-imaging generation study contract

Use this contract when the primary output is a generated radiological image, volume, sequence,
counterfactual, paired modality, lesion insertion or synthetic cohort. If the aim is reconstruction,
denoising or acceleration of an acquired signal for immediate interpretation, use
`reconstruction-enhancement.md` and disclose any generative component there.

## 1. Freeze the purpose and independent unit

| Field | Required specification |
|---|---|
| Generation task | unconditional, conditional, image-to-image, lesion insertion, paired-modality, counterfactual or augmentation |
| Intended use | development/training, method stress test, education, simulation or hypothesis generation |
| Independent unit | real source patient/exam and generated descendants; generated variants from one source remain one family |
| Conditioning inputs | images, masks, labels, reports, clinical variables, prompts and their timing/authority |
| Reference/target | real acquisition, pathology/clinical construct or explicitly no patient-level reference |
| Comparator | real-only development baseline and established augmentation/simulation alternative |
| Primary metric | use-specific fidelity/diversity/task/privacy endpoint with patient-level uncertainty |
| Failure policy | deletion/insertion, label inconsistency, memorisation, rare-group collapse and prohibited use |
| Claim ceiling | technical generation or development-set augmentation unless real untouched evidence supports more |

Generated images are model outputs, not independent patients, measurements or clinical outcomes.
Synthetic samples do not increase the clinical sample size or event count. Record the complete
source-patient-to-output lineage and split every descendant with its source patient.

## 2. Development and evaluation contract

- Use generated data for development/training only unless a separate use is explicitly justified.
- Preserve a real, patient-level, untouched final evaluation set representing the intended
  population, site/protocol shift and decision. Never select generators, prompts, checkpoints,
  filtering rules or downstream models on this final set.
- Compare a **real-only baseline** with the same architecture, tuning budget, evaluation set and
  uncertainty. Also report the marginal contribution of synthetic data across realistic real-data
  fractions when label-efficiency is claimed.
- Generated test data may stress known factors but cannot replace real-patient validation. A
  synthetic-to-synthetic result supports only the declared simulation.
- Keep source, pretraining and evaluation genealogy; audit exact and near duplicates, public-dataset
  aliases and model-pretraining overlap.

## 3. Fidelity, clinical semantics and diversity

Pixel, embedding or distribution metrics such as PSNR, SSIM, FID or visual preference do not by
themselves establish pathology preservation, diagnostic interchangeability, clinical utility,
privacy or absence of memorisation. Match evaluation to the use:

- physical/anatomical consistency and modality-specific quantitative units;
- finding-level presence, location, size and severity with blinded qualified adjudication;
- deletion, insertion, displacement and conditioning-label contradiction rates;
- diversity, mode collapse and coverage of rare but clinically important patterns;
- downstream real-set task performance and calibration, including failure cases and subgroups; and
- stochastic repeatability across seeds/prompts plus rejected/filtered-output accounting.

Reader preference measures realism under that display protocol only. It is not proof that generated
findings correspond to a real patient's biology.

## 4. Privacy and memorisation gate

Freeze a named threat model: protected asset, adversary, access, attacks, controls and success
criterion. Include nearest-neighbour/duplicate retrieval, rare-case copying, membership-inference or
model-inversion testing when relevant; audit prompts, logs, embeddings, hosted-provider retention and
exports. Passing a limited attack suite does not prove anonymity or universal non-memorisation.

Reuse the four-state pretraining-overlap and privacy contract in
`radiology-deep-learning/foundation-model-data-genealogy-and-privacy.md`. Route processing authority,
vendor terms and re-identification risk to `radiology-ethics`.

## 5. Stop gates and claim boundary

Return `STOP_FOR_REPAIR` for source-patient leakage across partitions, tuning on the real final set,
hidden filtering/failures, untracked source lineage, a sample-size claim that counts generated images
as patients, or a clinical/biological claim supported only by synthetic evidence. Return
`PRIVACY_CLAIM_UNRESOLVED` when the threat model is unspecified.

Permitted claim examples:

- “The generator produced images meeting the named technical/finding-level criteria.”
- “Adding the declared synthetic training data changed performance on the untouched real cohort by
  the reported amount relative to the matched real-only baseline.”

Do not claim that synthetic imaging replaces real clinical evidence, adds independent patients,
preserves every pathology, is anonymous, or improves patient outcomes without the corresponding real
clinical, privacy or impact evidence.

## Required return

`purpose/claim card -> real-source genealogy -> independent-unit and split manifest -> generator and
filtering provenance -> real-only comparator -> fidelity/semantic/diversity matrix -> privacy threat
model -> untouched-real evaluation -> failures -> claim ceiling`.

## Primary and official sources

- NIST. [Generative AI Profile (AI 600-1)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).
- NIST. [Adversarial Machine Learning taxonomy (AI 100-2e2025)](https://www.nist.gov/publications/adversarial-machine-learning-taxonomy-and-terminology-attacks-and-mitigations-0).
- Tejani AS, et al. [CLAIM 2024 Update](https://doi.org/10.1148/ryai.240300).

These sources frame reporting and risk controls; they do not validate a particular generator.
