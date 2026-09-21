# Where each checklist item lives in a _Radiology_ manuscript

_Radiology_ (RSNA) has a specific manuscript shape. Map checklist items to the section a
reviewer expects them in — items in the "wrong" place read as missing.

## Manuscript skeleton (Original Research)
- **Title** — concise; state modality and that AI/radiomics is used if central.
- **Structured abstract** — Background, Purpose, Materials and Methods, Results, Conclusion
  (report design, cohort sizes/dates, key metrics **with CIs**, and a bounded conclusion).
- **Summary statement** — a **single sentence** capturing the main finding (required).
- **Key Results** — up to **3** results/conclusions, **≤ 75 words**, with summary data; do
  **not** repeat the Summary statement; avoid vague language and abbreviations (these feed
  the visual abstract).
- **Abbreviations** list.
- **Introduction** — background → gap → objective/hypothesis (short).
- **Materials and Methods** — study design + ethics/IRB + registration; participants
  (eligibility, flow) ; imaging technique (scanner, protocol); image analysis / reference
  standard / readers + blinding; model/feature pipeline; **statistical analysis** (software,
  tests, CIs, multiplicity). *This is where most CLAIM/TRIPOD+AI/CLEAR/STARD items live.*
- **Results** — patient flow + characteristics, performance with CIs, validation, comparisons.
- **Discussion** — **first paragraph summarises key findings**, then context, then
  **limitations**, then a bounded conclusion.
- **Tables/Figures** — within journal limits; a patient-flow diagram is expected.

## Mapping cheat-sheet
| Checklist theme | Manuscript home |
|---|---|
| Ethics, registration, design | M&M (first paragraph) |
| Eligibility, flow, cohort dates | M&M + a flow diagram + Results table 1 |
| Acquisition/scanner/protocol | M&M "imaging technique" (+ supplement table) |
| Reference standard, readers, blinding | M&M "image analysis" |
| Split unit, leakage controls | M&M "statistical analysis"/"model development" |
| Preprocessing, discretisation, IBSI, harmonisation | M&M + supplement (parameter file) |
| Metrics, CIs, DeLong, calibration, DCA, multiplicity | M&M "statistical analysis" + Results |
| Performance, external validation | Results + figures (ROC, calibration, DCA) |
| Fairness/subgroup | Results (+ supplement) |
| Limitations, generalisability | Discussion |
| Data/code/model availability | dedicated statement (cross-ref radiology-data) |

## Submission logistics
- Attach the completed primary checklist as a supplemental file; cite it in M&M.
- Register prospective studies; report the trial/registry ID.
- Confirm word limits, figure/table counts, and structured-abstract word limit against the
  **current** _Radiology_ author instructions (they change — verify before submission).
