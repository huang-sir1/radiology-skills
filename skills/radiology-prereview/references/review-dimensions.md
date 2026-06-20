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

## 6. Statistics
- Estimates with **CIs**; correct tests; **calibration + decision-curve** for clinical models;
  multiplicity control; sample size/EPV (→ radiology-stats).

## 7. Validation
- Internal vs external; honest labelling; per-center/temporal results; performance drop reported.

## 8. Reporting compliance
- Correct EQUATOR stack present and complete (CLAIM/CLEAR/TRIPOD+AI/STARD/IBSI)
  (→ radiology-reporting).

## 9. Figures & tables
- Table 1; ROC **with** calibration/DCA; flow diagram; failure cases; legends complete;
  interpretability not over-read (→ radiology-figure).

## 10. Claims vs evidence
- Abstract/Key Results/Discussion bounded by data; no "AUC high → clinically usable", no
  "correlation → causation", no unfounded "first/novel".

## 11. Data / code / ethics
- Availability statements specific; de-identification; ethics/consent present and consistent
  (→ radiology-data / radiology-ethics).

## 12. Writing & structure
- _Radiology_ shape (Summary statement, Key Results), clarity, limitations honest
  (→ radiology-writing / radiology-polishing).

## Severity rubric
- **Blocker** — likely desk-reject / fatal (leakage, no external validation when required,
  undefined labels, broken stats).
- **Major** — major revision (missing calibration, incomplete reporting, overclaim, weak baseline).
- **Minor** — polish (wording, figure detail, a missing CI).
