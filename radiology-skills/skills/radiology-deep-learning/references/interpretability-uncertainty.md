# Interpretability, uncertainty, and robustness

RQS 2.0 (2025) formally added fairness and explainability to radiomics quality scoring, and the
FUTURE-AI consensus (Fairness, Universality, Traceability, Usability, Robustness,
Explainability — 117 international experts (BMJ 2025;388:e081554)) now frames what a "trustworthy, deployable" medical
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
| **Conformal prediction** | Use a prespecified nonconformity score and a calibration set that is separate from fitting and final evaluation | Method, score, alpha, finite-sample quantile rule, calibration-set size, target type (marginal/conditional) and empirical coverage with uncertainty |
| **Evidential / distributional heads** | Model outputs distribution parameters directly | Which distribution, and a calibration check (e.g. reliability diagram of predicted vs. empirical coverage) |

- **Calibration of the uncertainty itself must be checked**, not assumed — a reliability diagram
  for the uncertainty estimate is the analogue of the calibration plot already required for point
  predictions (`radiology-stats/model-evaluation.md`); don't conflate the two.
- State whether uncertainty is used downstream (e.g. flag high-uncertainty cases for human review)
  — if so, this is a use-scenario decision (`radiology-translation/use-scenario.md`).

### Conformal coverage contract

Ordinary split-conformal prediction can provide **finite-sample marginal coverage** only for the
declared method and under its sampling assumptions, commonly exchangeability of calibration and
future examples. It does not provide per-patient, per-class, per-site or other conditional coverage
merely because the nominal level is 90%.

Before using coverage language, freeze and report:

1. the fitting, calibration and final-evaluation partitions, all separated at the patient level;
2. the nonconformity score, alpha, tie/randomisation handling and finite-sample quantile correction;
3. whether the target is marginal, label-conditional, group-conditional or another named coverage
   property, and the theorem/algorithm that supports that target;
4. calibration-set size and empirical final-set coverage, set/interval size and uncertainty overall
   and in clinically relevant predeclared groups; and
5. the action when coverage or efficiency is unacceptable.

Site, time, prevalence, protocol or referral shifts can break ordinary exchangeability. Under such a
shift, report observed transported coverage and the method's explicit shift assumptions; do not carry
the derivation-population guarantee forward by wording alone. Groupwise empirical coverage is an
audit, not proof of individual conditional validity. Use
`COVERAGE_ASSUMPTIONS_UNRESOLVED` when the sampling relation or method is unknown.

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
- **Subgroup/fairness robustness**: pre-specified performance and calibration by clinically relevant
  groups may reveal heterogeneity, but subgroup AUC parity does not establish fairness, equitable
  access, equal error consequences or absence of intersectional harm. Route the full population,
  representation, burden, access, threshold and consequence question to
  `radiology-design/registered-reports-ppi-and-equity.md`, statistical estimation to
  `radiology-stats`, and privacy/protected-attribute authority to `radiology-ethics`.

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

- Only if attribution was evaluated: *"Attribution method and parameters [AUTHOR_INPUT_NEEDED]
  were assessed on evaluation sample and selection rule [AUTHOR_INPUT_NEEDED], yielding findings
  and limitations [AUTHOR_INPUT_NEEDED]."* Add a figure citation only for existing selected
  success/failure examples: *"These examples appear in figure [AUTHOR_INPUT_NEEDED]."*
- Only if predictive uncertainty was evaluated: *"Uncertainty method and configuration
  [AUTHOR_INPUT_NEEDED] yielded calibration results and uncertainty [AUTHOR_INPUT_NEEDED] on
  evaluation partition [AUTHOR_INPUT_NEEDED]."*
- Only if conformal prediction was performed: *"Method, calibration sample, score and alpha
  [AUTHOR_INPUT_NEEDED] targeted coverage property and assumptions [AUTHOR_INPUT_NEEDED]. Observed
  prediction-set/interval coverage and size, with uncertainty, were [AUTHOR_INPUT_NEEDED] in
  evaluation population [AUTHOR_INPUT_NEEDED]."*
- Only if perturbation/OOD behaviour was evaluated: *"Conditions and evaluation design
  [AUTHOR_INPUT_NEEDED] yielded results and uncertainty [AUTHOR_INPUT_NEEDED]."* Add a table/figure
  citation only when that artifact exists: *"Results are reported in [AUTHOR_INPUT_NEEDED]."*

Use only completed analysis records and verified outputs; remove every unperformed branch and
report relevant gaps as not evaluated. Do not invent methods, sample proportions, coverage,
failure-case counts or completed robustness tests from this template. Cite a figure or table only
after verifying that it exists and contains the stated evidence. Empirical coverage does not by
itself establish a conditional or transported guarantee.

## Handoffs
- Architecture/capacity/baseline choice → `radiology-deep-learning/architecture-choice.md`.
- Calibration of the primary point prediction (distinct from uncertainty calibration above) →
  `radiology-stats/model-evaluation.md`.
- Subgroup/fairness statistical estimation → `radiology-stats`; equity estimands, access and affected-
  group decisions → `radiology-design/registered-reports-ppi-and-equity.md`.
- Deployment claim bounded by this evidence → `radiology-translation/prospective-deployment.md`.
- Figures for saliency maps/uncertainty plots → `radiology-figure`.
- FUTURE-AI/TRIPOD+AI fairness item routing → `radiology-reporting/guideline-router.md`.

## Primary sources for the coverage boundary

- Prinster et al. [JAWS-X: Addressing efficiency bottlenecks of conformal prediction under
  distribution shift](https://proceedings.mlr.press/v202/prinster23a.html).
- Gibbs et al. [Conformal prediction with conditional guarantees](https://academic.oup.com/jrsssb/article/87/4/1100/8058684).
- Angelopoulos and Bates. [A gentle introduction to conformal prediction and distribution-free
  uncertainty quantification](https://doi.org/10.48550/arXiv.2107.07511).
