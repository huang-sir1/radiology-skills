# Simulation and teaching-data contract

Use simulation only after the user explicitly authorizes synthetic data or result-like artifacts for
the current task. Saying that the work is for teaching, asking for mentoring, or having missing inputs
is not simulation authorization. Offer a conceptual explanation, schematic example or placeholder
template when authorization is absent. Simulation may fill an authorized teaching gap; it may not
impersonate a real study.

Record `simulation_authorized=true`, the authorized scope, intended learning objective and whether
files may be created. Authorization for one toy example does not authorize a full synthetic project
or edits to a real project record.

## Provenance states

| State | Meaning | Submission eligibility |
|---|---|---|
| `real` | Supplied or computed from real study data | Eligible only after all gates pass |
| `simulated` | Entire dataset/result is synthetic | Teaching/demo only |
| `mixed` | Real and synthetic artifacts coexist | Ineligible until separated and audited |

## Required labels

For simulated or mixed projects:

- set `data_provenance` and `teaching_only` in `project_state.json`;
- set simulated value rows to `verified_status=simulated`;
- set simulated claims to `status=simulated` and `submission_eligible=false`;
- put `Simulated data for teaching; not clinical evidence` in every relevant figure caption,
  table footnote, abstract/demo page, and exported report;
- keep simulated files in a clearly named path such as `teaching_simulation/`;
- never invent IRB numbers, patient identifiers, accessions, citations, or real institutions.

## Simulation design

When generating teaching data:

1. State the learning objective and which patterns the simulation should demonstrate.
2. Define the synthetic data-generating process, sample size, event/censoring mechanism,
   missingness, correlations, and train/test structure.
3. Use plausible ranges without copying a real cohort or claiming clinical realism.
4. Preserve patient-level structure and analysis hygiene so the pipeline teaches correct practice.
5. Record the random seed and generator version.
6. Include at least one limitation showing where the simulation is intentionally simplified.

## Conversion to a real project

Do not overwrite simulated artifacts in place. Initialize a real-data branch/project record,
replace every simulated value and claim, and rerun all gates. Style/layout templates may be reused;
results, legends, conclusions, and source-data links may not.
