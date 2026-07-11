# Guideline router — pick the stack before you audit

Imaging-AI papers almost always need **more than one** guideline: a *reporting* guideline
(what to write) **and** a *quality / risk-of-bias* tool (how good / how biased). Choose the
full stack first, then audit each.

## Step 1 — answer six questions

1. **Is there an AI/ML/DL component?** → CLAIM 2024 is in scope.
2. **Is a prediction model developed and/or validated** (outputs a risk/score/class for an
   individual)? → TRIPOD+AI (reporting) + PROBAST(-AI) (risk of bias).
3. **Are hand-crafted radiomic features used?** → CLEAR (reporting) + METRICS and/or RQS
   (quality) + IBSI (feature reproducibility).
4. **Is the endpoint diagnostic accuracy vs a reference standard?** → STARD 2015.
5. **Is this a systematic review / meta-analysis?** → PRISMA(-DTA) + QUADAS-2 per study.
6. **Is the target a Nature-portfolio journal** (Nature Medicine, Nature Biomedical Engineering,
   Nature Communications, npj Digital Medicine, Nature Machine Intelligence, etc.)? → add the
   **Reporting Summary + Editorial Policy Checklist** on top of whichever stack above applies —
   it is a separate disclosure layer, not a substitute for CLAIM/TRIPOD+AI/CLEAR (→
   `nature-reporting-summary.md`).

A "yes" to several is normal. Stack them.

## Step 2 — common stacks

| Real study | Stack |
|---|---|
| DL classifier on CT, internal + external test | CLAIM 2024 + TRIPOD+AI + PROBAST-AI |
| Hand-crafted radiomics signature predicting a mutation | CLEAR + METRICS (or RQS) + IBSI + TRIPOD+AI |
| Radiomics model whose endpoint is sensitivity/specificity for a lesion | CLEAR + IBSI + STARD (+ TRIPOD+AI if a model score is reported) |
| Deep-learning segmentation tool | CLAIM 2024 (segmentation metrics: DSC, HD95, surface metrics) |
| Meta-analysis of CT radiomics for cancer diagnosis | PRISMA-DTA + QUADAS-2 + (RQS to grade primary studies) |
| Prospective reader study with vs. without AI | STARD + MRMC design (see radiology-stats) + (CONSORT-AI if randomised) |
| Radiogenomics: imaging features ↔ RNA-seq | CLEAR + IBSI for imaging; + multi-omics/leakage rules (radiology-radiogenomics); TRIPOD+AI if a predictive model is built |
| Any of the above, submitted to a Nature-portfolio journal | same stack **+ Reporting Summary/Editorial Policy Checklist** (`nature-reporting-summary.md`) **+** FUTURE-AI as the trustworthy/deployable-AI framing where clinical deployment is discussed |

## Step 3 — separate the three jobs

- **Reporting completeness** — CLAIM, TRIPOD+AI, CLEAR, STARD, PRISMA-DTA, STROBE,
  CONSORT-AI. *Did you write down everything a reader needs to reproduce/judge the study?*
- **Methodological quality** — METRICS, RQS/RQS 2.0. *Were the methods themselves good?*
- **Risk of bias** — PROBAST(-AI), QUADAS-2. *Could the design have biased the result?*
- **Trustworthiness / deployability** — FUTURE-AI (Fairness, Universality, Traceability,
  Usability, Robustness, Explainability — 2023/2024 international consensus, healthcare AI).
  *Would this system be safe and fair to actually deploy?* This is a broader lifecycle lens
  (design → development → validation → deployment → monitoring) rather than an item-by-item
  reporting checklist — use it to frame Discussion claims about clinical readiness and to check
  that explainability/robustness/fairness were addressed somewhere in the study, not only in the
  reporting checklist items that happen to touch them (CLAIM/TRIPOD+AI's fairness item is
  narrower). Cross-ref `radiology-deep-learning/interpretability-uncertainty.md` and
  `radiology-translation/prospective-deployment.md` (monitoring/drift already lives there).

Authors often confuse "we scored well on RQS" with "we are unbiased (PROBAST)". They are
different axes. Report the reporting guideline as the backbone; use quality/RoB tools to
strengthen Methods, FUTURE-AI to frame deployability, and pre-empt reviewer critiques.

## Step 4 — submission logistics

**_Radiology_-family:**
- Upload the completed checklist for the primary guideline as a supplemental file.
- Reference the guideline in Methods ("We report this study following the [guideline]
  checklist").
- For trials, register prospectively and report the registry ID.
- See `radiology-submission-map.md` for where each item belongs in the manuscript.

**Nature-portfolio-family** (in addition to the primary reporting-guideline checklist above):
- Complete the **Reporting Summary** (published with the article) and, if requested, the
  **Editorial Policy Checklist** (→ `nature-reporting-summary.md`).
- Plan the **Extended Data / Supplementary Information / Source Data** split
  (→ `radiology-figure/nature-figure-spec.md`, `radiology-data`).
- See `radiology-journal/submission-logistics.md` for the venue-specific pre-flight checklist.

## Edge cases

- **Foundation models / generative AI in imaging** — CLAIM 2024 added items relevant to
  large/generative models; still report data provenance, evaluation, and failure modes.
  Consider emerging guidance (e.g. for generative models) in addition to CLAIM.
- **Foundation models / LLMs used for report generation, structuring, or summarisation** —
  consider **TRIPOD-LLM** (2025 extension, 19 main items/50 sub-items) alongside CLAIM; report
  the prompt/fine-tuning strategy, evaluation against a reference standard, and failure modes
  the same way an imaging model would be audited. Verify this is still the current name/version
  live before citing it in a manuscript.
- **No model, only feature association (radiogenomics discovery)** — CLEAR + IBSI for the
  imaging side; report multiple-testing control and validation cohort. Don't force
  TRIPOD+AI if no individual-level prediction model is built — but if you report any
  classifier, you do need it.
- **"AI-assisted" workflow / decision support used clinically** — add DECIDE-AI for the
  early live-clinical-evaluation stage; add FUTURE-AI framing if deployment/monitoring is
  discussed.
