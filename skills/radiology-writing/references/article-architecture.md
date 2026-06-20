# Radiology manuscript architecture

## Skeleton (Original Research)
1. **Title** — concrete; population/condition + modality/method + finding or role.
2. **Structured abstract** — Background, Purpose, Materials and Methods, Results, Conclusion.
3. **Summary statement** — one sentence (the main finding).
4. **Key Results** — ≤ 3 items, ≤ 75 words, with summary data.
5. **Abbreviations** list.
6. **Introduction** — stakes → gap → objective/hypothesis.
7. **Materials and Methods** — design/ethics → participants → technique → analysis/readers →
   model/pipeline → statistics.
8. **Results** — flow + characteristics → performance (CIs) → comparisons → validation.
9. **Discussion** — key-finding summary → context → limitations → bounded conclusion.
10. **Tables/Figures** — within limits; patient-flow diagram expected.

## Argument flow by study type
- **Diagnostic accuracy**: clinical question → index test vs reference standard → accuracy
  with CIs at a pre-specified threshold → comparison/limitations. (STARD)
- **Prediction model (AI/ML)**: clinical need → development cohort/pipeline → discrimination
  **and calibration** → external validation → clinical utility (DCA) → bounded use.
  (TRIPOD+AI)
- **Radiomics**: phenotype hypothesis → IBSI pipeline + reproducibility → signature in
  nested CV → external validation → interpretation. (CLEAR/METRICS)
- **Radiogenomics**: imaging phenotype ↔ molecular layer → matched cohort → association/
  integration (FDR) → validation cohort → bounded biological interpretation.

## Paragraph discipline
- One paragraph, one message; first sentence states it; following sentences support in order.
- Keep each claim adjacent to its evidence (number + CI).
- Don't preview all results in the Introduction; don't re-list all results in the Discussion.

## Length & limits
- _Radiology_ enforces word counts, figure/table counts, and a structured-abstract limit.
  **Verify current limits** in the author instructions before finalising; design figures to
  the count (combine panels rather than exceed).
