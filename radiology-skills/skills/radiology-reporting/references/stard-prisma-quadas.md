# Diagnostic accuracy & evidence synthesis — STARD, PRISMA-DTA, QUADAS-3

## STARD 2015 — diagnostic accuracy studies (30 items)
Use when the endpoint is a **test vs a reference standard** (sensitivity/specificity, etc.),
including AI/radiomics used as a diagnostic test.

Item clusters:
- **Title/Abstract/Intro** — identify as a diagnostic-accuracy study; objectives/hypotheses.
- **Methods** — study design (prospective/retrospective) and whether the cut-off was
  **pre-specified**; eligibility and **setting/recruitment** (consecutive? spectrum of
  disease); the **index test** and **reference standard** with rationale, both executed and
  read with **blinding**; flow and timing between tests; **how indeterminate results and
  missing data** were handled; sample-size rationale; statistical methods incl. CIs.
- **Results** — participant flow (a STARD diagram), clinical & demographic characteristics,
  cross-tab of index vs reference results, estimates of accuracy **with 95% CIs**, adverse
  events.
- **Discussion** — limitations incl. **spectrum/selection bias**, applicability.
- **Other** — registration, protocol, funding.

**Highest-yield STARD failures:** non-consecutive/enriched sampling (spectrum bias);
threshold chosen post-hoc on the same data; reference standard applied differentially or not
blinded; no CIs; no flow diagram.

> **STARD-AI** (Sounderajah et al., *Nature Medicine* 2025;31:3283–3289) is now the standard
> for **AI** diagnostic-accuracy studies: its checklist has 40 items total; relative to STARD
> 2015, 4 existing items were modified and 14 new items added. The publisher also describes
> the additions at main-item/subitem granularity as 10 main items comprising 14 subitems—do
> not mix denominators. The changes cover dataset practices (sources, annotation, partitioning),
> the AI index test and its evaluation, algorithmic bias/fairness, and subgroup performance.
> For an AI index test audit against **STARD-AI** (not STARD 2015 alone);
> STARD 2015 remains the base guideline for non-AI tests.

## PRISMA-DTA (2018) — systematic reviews of diagnostic test accuracy
Extension of PRISMA for DTA reviews. Key DTA-specific items beyond PRISMA 2020:
- Structured abstract with DTA-specific content.
- **Eligibility** by population, index test(s), comparator(s)/reference standard, target
  condition.
- Search strategy reproducible; **flow diagram** of records → included studies.
- **Data items** per study (2×2 counts: TP/FP/FN/TN) so accuracy is recomputable.
- **Risk of bias and applicability via QUADAS-3 v1.2** for selected accuracy estimates.
- **Synthesis** — bivariate/HSROC models for pooled sensitivity/specificity; heterogeneity
  exploration; **SROC** plot; investigation of threshold effect.
- Certainty of evidence (GRADE for DTA).

## QUADAS-3 v1.2 — current risk of bias & applicability tool for DTA reviews

Use the current University of Bristol release. QUADAS-3 shifts the assessment from a single
study-level label to the **selected accuracy-estimate level** and comprises six phases:

1. state the systematic-review synthesis question(s), once per review;
2. define the ideal test accuracy trial for each synthesis question, once per review;
3. draw a flow diagram, once per study;
4. identify the accuracy estimates to assess, once per study;
5. assess risk of bias and applicability for each selected estimate; and
6. make an overall judgment for each selected estimate.

Phase 5 has four domains:

1. **Participants** — enrolment design, prospective/retrospective status, sampling and match to the
   intended-use population;
2. **Index Test** — conduct, interpretation, available information and threshold selection;
3. **Target Condition** — definition, reference-standard conduct/interpretation and timing; and
4. **Analysis** — inclusion in the analysed table, missing data, unit of analysis and calculation of
   the selected estimates.

All four domains receive a risk-of-bias judgment; Participants, Index Test and Target Condition also
receive applicability judgments against the synthesis question and ideal trial. Use the current
response/judgment categories from the v1.2 tool rather than copying a legacy QUADAS-2 form.

## QUADAS-C — comparative accuracy companion

For a primary study that compares two or more index tests, assess the ordinary single-test/estimate
questions with **QUADAS-3** and apply **QUADAS-C alongside QUADAS-3** to the within-study test
comparison, following the adaptation in the QUADAS-3 Explanation & Elaboration guidance.

QUADAS-C cannot be used alone. It does not assess indirect comparisons between separate studies and
does not assess applicability. Do not add it merely because a meta-analysis happens to compare pooled
results from different single-test studies.

## QUADAS-2 (legacy only)

QUADAS-2 is superseded by QUADAS-3. Mention or reproduce it only when faithfully documenting a
historical protocol or completed review that actually used the previous tool; label that use
`legacy` and do not present it as the current recommended route.

## Output
- STARD: `Item | Status | Location | Fix | Owner | Closure evidence`.
- DTA review: PRISMA-DTA item table **plus** a QUADAS-3 v1.2 estimate-level table/graphic
  (domains × selected estimates), with a paired QUADAS-C comparison assessment where eligible.
  Hand off the SROC/forest plots to `radiology-figure` and pooling to
  `radiology-stats`.
