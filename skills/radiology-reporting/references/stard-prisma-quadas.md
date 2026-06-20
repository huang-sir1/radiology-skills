# Diagnostic accuracy & evidence synthesis — STARD, PRISMA-DTA, QUADAS-2

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

> **STARD-AI** is in development for AI diagnostic-accuracy studies; until finalised, use
> STARD 2015 + CLAIM 2024 together.

## PRISMA-DTA (2018) — systematic reviews of diagnostic test accuracy
Extension of PRISMA for DTA reviews. Key DTA-specific items beyond PRISMA 2020:
- Structured abstract with DTA-specific content.
- **Eligibility** by population, index test(s), comparator(s)/reference standard, target
  condition.
- Search strategy reproducible; **flow diagram** of records → included studies.
- **Data items** per study (2×2 counts: TP/FP/FN/TN) so accuracy is recomputable.
- **Risk of bias via QUADAS-2** per included study.
- **Synthesis** — bivariate/HSROC models for pooled sensitivity/specificity; heterogeneity
  exploration; **SROC** plot; investigation of threshold effect.
- Certainty of evidence (GRADE for DTA).

## QUADAS-2 — risk of bias & applicability in DTA studies
Four domains, each rated **Low / High / Unclear** for **risk of bias**, and the first three
also for **applicability**:
1. **Patient selection** — consecutive/random? case-control avoided? inappropriate
   exclusions? (spectrum bias)
2. **Index test** — interpreted **blind** to reference standard? threshold **pre-specified**?
3. **Reference standard** — likely to correctly classify? interpreted blind to index test?
4. **Flow & timing** — appropriate interval? all patients got the **same** reference
   standard? all included in analysis?

**QUADAS-C** extends QUADAS-2 for **comparative** accuracy (test A vs test B).

## Output
- STARD: `Item | Status | Location | Fix`.
- DTA review: PRISMA-DTA item table **plus** a per-study QUADAS-2 traffic-light table
  (domains × studies). Hand off the SROC/forest plots to `radiology-figure` and pooling to
  `radiology-stats`.
