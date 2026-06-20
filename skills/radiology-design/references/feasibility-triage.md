# Feasibility triage — can this data support a study?

Decide the **realistic task ceiling** before designing anything. The goal is an honest verdict,
not encouragement.

## Inputs to establish first

| Dimension | Why it gates feasibility |
|---|---|
| Disease + clinical question | Defines the reference standard and the achievable endpoint |
| Modality(ies) | Determines feature/signal availability and harmonisation burden |
| n (patients **and** lesions) | Caps model complexity; lesion-level n ≠ patient-level n |
| Centers / scanners / protocols | Decides whether external/multi-center validation is possible |
| Label source & quality | Pathology > consensus read > single read > report-mined; noisy labels cap ceiling |
| Segmentation masks | Needed for radiomics/segmentation; absence = annotation cost (→ radiology-annotation) |
| Events & follow-up | Prognosis needs event count + mature follow-up, not just patient count |
| Molecular/pathology data | Enables radiogenomics only if **matched** to imaging (same patient/lesion) |
| Time span | Enables temporal validation; flags scanner/protocol drift |

## Task-ceiling heuristics (orientation, not hard cut-offs — confirm power with radiology-stats)

- **Segmentation:** needs high-quality masks; tens of well-annotated cases can pilot, but
  generalisable models need scanner/center diversity.
- **Diagnosis / binary classification:** needs a credible reference standard and adequate cases
  **per class**; artificial 1:1 sampling inflates apparent performance — report real prevalence.
- **Subtyping / staging (multi-class):** each class needs enough cases; rare classes collapse CIs.
- **Prognosis / survival:** driven by **event count** (EPV), not total n; immature follow-up or
  few events ⇒ feasibility/pilot only.
- **Treatment-response / recurrence:** needs defined response criteria, baseline+follow-up
  imaging, and the outcome ascertained the same way across centers.
- **Radiogenomics:** binding constraint is the **matched** imaging∩omics intersection, almost
  always much smaller than either alone (→ radiology-radiogenomics).

## Showstoppers (any one forces "Feasibility study only" or "Not yet")

- No credible reference standard / ground truth for the endpoint.
- No path to external or even temporal validation (single center, single scanner, one period)
  **and** the claim requires generalisability.
- Event count too low for the intended prognostic model (EPV far below threshold).
- Structure that guarantees leakage and cannot be fixed (e.g. same patient's slices unavoidably
  span sets because of how data were collected).
- Labels too noisy or circular (model trained on the report it's meant to replace).

## Verdict format

State exactly one, with a one-line reason and the single most important next action:

- **Feasible as designed** — data supports the intended study; proceed to blueprint.
- **Feasible with changes** — works if you adjust endpoint/scope/validation (name the change).
- **Feasibility study only** — publishable as a pilot/proof-of-concept; do not over-claim.
- **Not yet — collect X first** — name the minimum addition (external cohort, more events,
  pathology labels, masks) that unlocks a real study.

## Anti-patterns to call out

- Choosing the task to fit the algorithm instead of the clinical need.
- Treating lesion count as if it were patient count.
- Assuming "more layers / a foundation model" rescues a cohort that is too small or single-center.
- Planning to mix multi-center data randomly and call the held-out fold "external validation"
  (it is not — see validation-strategy.md).
