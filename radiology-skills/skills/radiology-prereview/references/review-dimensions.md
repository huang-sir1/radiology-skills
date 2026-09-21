# Review dimensions

Cover every dimension a methods-literate reviewer checks. For each, record
`Issue | Severity | Location | Guideline/risk | Fix`.

## 1. Design & question
- Clear clinical question, population, endpoint, comparator, intended use.
- Design matches the claim (DTA vs prediction vs radiogenomics).

## 2. Data & cohort
- Source, inclusion/exclusion, flow diagram, real prevalence.
- Patient vs lesion counts; spectrum; single vs multi-center.

## 3. Labels & reference standard
- How the ground truth was established; readers, expertise, blinding, adjudication.
- Label noise / circularity (model predicting the report it learned from).

## 4. Segmentation / annotation
- Reproducibility (ICC/Dice), reader protocol, feature-stability filtering
  (→ radiology-annotation).

## 5. Leakage & partition
- Patient-level split; no overlap; fit-on-training only; no test-set tuning
  (→ radiology-radiomics / radiology-deep-learning audits).

## 6. Parameters, evaluation metrics & methodology
- Values/ranges and units, role and rationale, selection timing/data, search space/budget/objective,
  software/version, freeze point and deviations are traceable.
- Metrics/readouts match the task, independent unit, aggregation, threshold/prevalence and intended
  claim; tuning objectives are not reused as independent evidence without optimism control.
- The method matches the question/estimand, data layer, hierarchy and assumptions; comparators use
  matched cases/splits/preprocessing and fair tuning conditions.
- Decision-bearing parameters have proportionate sensitivity/failure-boundary evidence; advertised
  components have valid ablations/controls where they could change the claim.
- Route a focused design or audit to `radiology-method-evaluation`; freeze its criterion and closure
  evidence as ordinary prereview findings rather than replacing them with a score.

## 7. Statistics
- Estimates with **CIs**; correct tests; **calibration + decision-curve** for clinical models;
  multiplicity control; sample size/EPV (→ radiology-stats).

## 8. Validation
- Internal vs external; honest labelling; per-center/temporal results; performance drop reported.

## 9. Reporting compliance
- Reporting stack selected by study type via radiology-reporting (EQUATOR-family checklists
  such as CLAIM/CLEAR/TRIPOD+AI/STARD) present and complete; IBSI is a reproducibility
  standard, listed separately — not an EQUATOR checklist (→ radiology-reporting).

## 10. Figures & tables
- Table 1; ROC **with** calibration/DCA; flow diagram; failure cases; legends complete;
  interpretability not over-read (→ radiology-figure).

## 11. Claims vs evidence
- Abstract/Key Results/Discussion bounded by data; no "AUC high → clinically usable", no
  "correlation → causation", no unfounded "first/novel".

## 12. Human-subjects authorization
- Treat ethics approval, consent/waiver and data-use authorization as an absolute STOP gate for the
  applicable activity or assurance claim. Consume a `DOCUMENT_VERIFIED`
  `radiology-ethics: human-subjects` receipt with exact document locator, scope and SHA-256; an author
  statement is not closure.

## 13. Data / code sharing
- Audit Data Availability and Code Availability separately: actual repository/access route,
  de-identification, DUA/consent consistency, restrictions and executable access instructions
  (→ radiology-data; radiology-ethics owns authorization consistency).

## 13. Writing & structure
- _Radiology_ shape (Summary statement, Key Results), clarity, limitations honest
  (→ radiology-writing / radiology-polishing).

## Severity rubric
- **Blocker** — likely desk-reject / fatal (leakage, no external validation when required,
  undefined labels, broken stats).
- **Major** — major revision (missing calibration, incomplete reporting, overclaim, weak baseline).
- **Minor** — polish (wording, figure detail, a missing CI).
