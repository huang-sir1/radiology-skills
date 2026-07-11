# Interpretability, uncertainty, and robustness

RQS 2.0 (2025) formally added fairness and explainability to radiomics quality scoring, and the
FUTURE-AI consensus (Fairness, Universality, Traceability, Usability, Robustness,
Explainability — 118 international experts) now frames what a "trustworthy, deployable" medical
imaging AI system must show across its lifecycle. A model with excellent AUC but no
interpretability, uncertainty, or robustness evidence is under-built for a high-impact venue,
and increasingly for _Radiology_-tier review too. This file covers the three pieces
`architecture-choice.md`/`training-protocol.md` don't: explaining predictions, quantifying
confidence, and testing failure modes — without overclaiming what any of them prove.

## Interpretability / explainability

Pick the method that matches the architecture and **report it as a hypothesis-generating aid,
not proof the model "understands" the anatomy**:

| Method | Fits | Shows | Caution |
|---|---|---|---|
| **Grad-CAM / Grad-CAM++ / Score-CAM** | CNNs | Coarse spatial attribution (where the network weighted its decision) | Resolution is coarse (last conv layer); do not over-read pixel-level precision |
| **Attention maps / attention rollout** | Transformers/ViT, attention-gated models | Which tokens/patches the model attended to | Attention ≠ explanation of causal reasoning — treat as descriptive, not causal |
| **Integrated Gradients / SHAP (on deep or radiomic features)** | Any differentiable model; tabular radiomic-feature models | Feature-level attribution, additive and theoretically grounded (SHAP) | Computationally heavier; correlated features (common in radiomics) can split credit unstably — report on the same feature set used for the primary model |
| **Occlusion / perturbation sensitivity** | Any black-box model | Empirical effect of masking a region on the output | Slow; sensitive to occlusion size/shape choice — state them |
| **Concept-based (e.g. TCAV-style)** | When a clinically meaningful concept (e.g. necrosis fraction) is hypothesised | Whether the model's representation aligns with a named concept | Requires concept-labelled data; still an association, not a proof |

### What to actually report
1. **Method + parameters** (layer used for Grad-CAM, occlusion size, SHAP background set) —
   reproducibility applies here exactly as it does to training (`training-protocol.md`).
2. **Qualitative + quantitative read**: show representative maps (→ `radiology-figure`) **and**,
   where feasible, a quantitative check — e.g. does the attribution overlap the reference-standard
   lesion mask (Dice/IoU between saliency and ground-truth ROI) more than a chance baseline?
3. **Failure-case attributions**, not only successes — an interpretability section that only shows
   flattering examples is a selection-bias red flag reviewers now watch for.
4. **Bounded claim**: "the model's attention concentrated on the enhancing tumour margin in most
   correctly classified cases" is defensible; "the model identified the biological driver" is not
   — calibrate the same way `radiology-polishing/style-guardrails.md` calibrates any other claim.

## Uncertainty quantification

A point prediction without a confidence estimate is unusable for the threshold-to-action framing
in `radiology-translation/threshold-to-action.md` — report one of these, matched to the
architecture and compute budget:

| Method | How | Report |
|---|---|---|
| **MC dropout** | Keep dropout active at inference; run N forward passes (commonly 20–100) | Predictive mean + variance/entropy; N used |
| **Deep ensembles** | Train K independently-seeded models (commonly 5+); combine predictions | Mean + spread across the ensemble; K and seed list |
| **Conformal prediction** | Calibrate a held-out (never test) calibration set to produce prediction sets/intervals with a guaranteed coverage rate | Target coverage (e.g. 90%), empirical coverage on test, the calibration-set split (must respect patient-level partitioning like every other split) |
| **Evidential / distributional heads** | Model outputs distribution parameters directly | Which distribution, and a calibration check (e.g. reliability diagram of predicted vs. empirical coverage) |

- **Calibration of the uncertainty itself must be checked**, not assumed — a reliability diagram
  for the uncertainty estimate is the analogue of the calibration plot already required for point
  predictions (`radiology-stats/model-evaluation.md`); don't conflate the two.
- State whether uncertainty is used downstream (e.g. flag high-uncertainty cases for human review)
  — if so, this is a use-scenario decision (`radiology-translation/use-scenario.md`).

## Robustness & out-of-distribution (OOD) behaviour

- **Perturbation robustness**: test performance under realistic nuisance variation — different
  scanner/vendor, mild noise, small rotation/crop, compression artefact — and report the
  performance **delta**, not just clean-data performance. This is distinct from, and in addition
  to, the external-validation scanner/site testing in `radiology-design/validation-strategy.md`;
  that tests transportability of the *trained* model, this tests sensitivity to *input* nuisance.
- **OOD / failure detection**: does the model (or an added detector) recognise inputs unlike its
  training distribution (wrong body part, wrong modality/sequence, severe artefact) rather than
  silently emitting a confident wrong answer? Report the detection method and its own
  sensitivity/specificity.
- **Adversarial robustness** is usually out of scope for a clinical-research paper unless
  adversarial threat is part of the claim — don't manufacture an adversarial-robustness section
  that isn't relevant to the study's use scenario; state explicitly if it was not evaluated and
  why, rather than silently omitting it.
- **Subgroup/fairness robustness**: pre-specified performance by clinically relevant subgroup
  (scanner, site, demographic variables where ethically and legally appropriate to collect and
  report) — this is also a named TRIPOD+AI item; don't duplicate work, cross-check with
  `radiology-reporting/tripod-ai-probast.md`.

## FUTURE-AI cross-check (use as a Discussion-level frame, not a new checklist to fabricate)

FUTURE-AI is a lifecycle framework, not an item-by-item reporting checklist like CLAIM — use it to
sanity-check that a deployment-facing claim is actually earned:

```
Fairness:        subgroup performance reported? (→ TRIPOD+AI fairness item, radiology-stats)
Universality:     tested across sites/scanners/populations, or scope explicitly bounded?
Traceability:     training data, code, model version documented and available? (→ radiology-data)
Usability:        output format and human-in-the-loop role defined? (→ radiology-translation/use-scenario.md)
Robustness:       perturbation/OOD behaviour reported? (this file)
Explainability:   interpretability method reported, bounded, and not overclaimed? (this file)
```

Mark each honestly — `Not evaluated` is an acceptable, honest answer for a retrospective
development study; the point is surfacing the gap, not pretending deployment-readiness the
evidence doesn't support (same discipline as `radiology-translation`'s claim ladder).

## Reporting sentence

*"Grad-CAM attribution maps, computed from the final convolutional block, concentrated over the
enhancing tumour margin in 87% of correctly classified cases (representative examples and two
failure cases in Figure 4); predictive uncertainty was estimated by a 5-model deep ensemble
(identical architecture, independent seeds), with 90%-target conformal prediction intervals
achieving 89% empirical coverage on the internal test set. Performance under simulated scanner
noise and a held-out out-of-distribution (non-contrast) input set is reported in Table S4."*

## Handoffs
- Architecture/capacity/baseline choice → `radiology-deep-learning/architecture-choice.md`.
- Calibration of the primary point prediction (distinct from uncertainty calibration above) →
  `radiology-stats/model-evaluation.md`.
- Subgroup/fairness statistical testing → `radiology-stats`.
- Deployment claim bounded by this evidence → `radiology-translation/prospective-deployment.md`.
- Figures for saliency maps/uncertainty plots → `radiology-figure`.
- FUTURE-AI/TRIPOD+AI fairness item routing → `radiology-reporting/guideline-router.md`.
