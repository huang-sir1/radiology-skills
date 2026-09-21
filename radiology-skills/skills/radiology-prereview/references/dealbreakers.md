# Dealbreakers — the issues that decide the outcome

Detect these first. Any one can cause desk-reject or major revision. For each: how to spot it,
and the fix to hand back.

| Dealbreaker | How to detect | Fix to hand back |
|---|---|---|
| **Data leakage** | Selection/normalisation/harmonisation on full cohort; augmentation across split; test-set tuning | Re-fit all data-dependent steps inside training; re-run; report honestly (→ radiomics/DL audit) |
| **No patient-level split** | Slice/lesion-level split; same patient in train+test | Re-split at patient level; re-evaluate |
| **No external validation (when the claim needs it)** | Only internal CV; generalisability claimed | Add external/temporal/geographic cohort, or bound the claim to internal (→ radiology-design) |
| **Undefined / circular labels** | Reference standard vague; model learns from the report it replaces | Define ground truth, readers, blinding; remove circularity |
| **Unclear segmentation** | Segmentation provenance or reproducibility evidence cannot support the stated measurement/model claim | Document readers or automated source, adjudication and task-matched agreement/stability analysis; ICC, Dice and feature filtering are not interchangeable or universally required (→ radiology-annotation) |
| **Incomplete statistics** | Missing uncertainty or analysis needed for the actual estimand/claim | Add appropriate CIs and multiplicity handling; calibration applies to predicted probabilities and DCA to a defined decision with defensible thresholds, not every imaging study (→ radiology-stats) |
| **Overclaiming** | "Clinically applicable" from retrospective AUC; "causal"/"first" | Re-word to bounded claims (→ radiology-writing) |
| **Weak/absent baseline** | DL "wins" vs a strawman or nothing | Add a fair, tuned baseline (radiomics/clinical/radiologist) |
| **Prevalence/spectrum mismatch** | Artificial 1:1; enriched cohort claimed as screening | Report real prevalence; bound the setting |
| **Data/code unavailable without reason** | Bare "on request"; no accession | Provide repository/accession or a justified controlled-access route (→ radiology-data) |
| **Ethics inconsistency** | Sharing promise exceeds consent; no approval | Align ethics ↔ availability; supply approval/consent (→ radiology-ethics) |

## Triage rule

1. Scan for the table above **before** detailed review.
2. If a Blocker exists, say so up front — cosmetic comments are secondary until it's resolved.
3. Pair every Blocker with the concrete fix and the skill that produces it.
