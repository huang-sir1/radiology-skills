# Guideline router — pick the stack before you audit

Imaging-AI papers almost always need **more than one** guideline: a *reporting* guideline
(what to write) **and** a *quality / risk-of-bias* tool (how good / how biased). Choose the
full stack first, then audit each.

## Step 1 — answer five questions

1. **Is there an AI/ML/DL component?** → CLAIM 2024 is in scope.
2. **Is a prediction model developed and/or validated** (outputs a risk/score/class for an
   individual)? → TRIPOD+AI (reporting) + PROBAST(-AI) (risk of bias).
3. **Are hand-crafted radiomic features used?** → CLEAR (reporting) + METRICS and/or RQS
   (quality) + IBSI (feature reproducibility).
4. **Is the endpoint diagnostic accuracy vs a reference standard?** → STARD 2015.
5. **Is this a systematic review / meta-analysis?** → PRISMA(-DTA) + QUADAS-2 per study.

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

## Step 3 — separate the three jobs

- **Reporting completeness** — CLAIM, TRIPOD+AI, CLEAR, STARD, PRISMA-DTA, STROBE,
  CONSORT-AI. *Did you write down everything a reader needs to reproduce/judge the study?*
- **Methodological quality** — METRICS, RQS/RQS 2.0. *Were the methods themselves good?*
- **Risk of bias** — PROBAST(-AI), QUADAS-2. *Could the design have biased the result?*

Authors often confuse "we scored well on RQS" with "we are unbiased (PROBAST)". They are
different axes. Report the reporting guideline as the backbone; use quality/RoB tools to
strengthen Methods and pre-empt reviewer critiques.

## Step 4 — _Radiology_ submission logistics

- Upload the completed checklist for the primary guideline as a supplemental file.
- Reference the guideline in Methods ("We report this study following the [guideline]
  checklist").
- For trials, register prospectively and report the registry ID.
- See `radiology-submission-map.md` for where each item belongs in the manuscript.

## Edge cases

- **Foundation models / generative AI in imaging** — CLAIM 2024 added items relevant to
  large/generative models; still report data provenance, evaluation, and failure modes.
  Consider emerging guidance (e.g. for generative models) in addition to CLAIM.
- **No model, only feature association (radiogenomics discovery)** — CLEAR + IBSI for the
  imaging side; report multiple-testing control and validation cohort. Don't force
  TRIPOD+AI if no individual-level prediction model is built — but if you report any
  classifier, you do need it.
- **"AI-assisted" workflow / decision support used clinically** — add DECIDE-AI for the
  early live-clinical-evaluation stage.
