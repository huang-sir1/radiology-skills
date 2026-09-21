---
name: radiology-table
description: "Create/audit editable publication tables with source reconciliation; not figures or statistical inference."
---

# Radiology Publication Tables

Build tables as scientific evidence, not decorative summaries. Each table should answer one
question, expose the correct denominator and uncertainty, and remain traceable to analysis output.

## Core stance

- **Shell before formatting.** Define the population, row variables, column groups, estimand,
  precision, and footnotes before filling cells.
- **One canonical value.** Reconcile values to source output or the `radiology-pipeline`
  `reported_values.csv`; do not retype numbers from prose.
- **Denominators stay visible.** State cohort n, events, missingness, and subgroup denominators.
- **Reference levels are explicit.** Regression and subgroup tables name reference categories.
- **Estimate plus uncertainty.** Report effect estimate with 95% CI; use exact p values under the
  target venue's policy.
- **Editable and inspectable.** Prefer DOCX/XLSX/LaTeX for editing plus CSV/source data for audit.
- **No false polish.** A visually clean table with inconsistent counts or unsupported precision fails.

## When to open extra files

| File | Open when |
|---|---|
| [references/table-archetypes.md](references/table-archetypes.md) | Choosing Table 1, performance, regression, feature, reader, radiogenomics, ablation, or supplement structure |
| [references/survival-and-model-tables.md](references/survival-and-model-tables.md) | Cox/KM/prognostic, logistic, nomogram, time-dependent metrics, calibration, DCA, or feature-weight tables |
| [references/table-style-and-qa.md](references/table-style-and-qa.md) | Applying target-journal style, fitting wide/long tables, footnotes, pagination, export, and final visual QA |

## Workflow

Choose `advisory`, `audit` or `create-edit` from the request. Advisory work returns an inline plan;
audit checks existing tables and reports supported findings without rewriting them. Steps 5–7 apply
to authorized creation/editing; do not export a replacement merely because a table was reviewed.

1. **Classify the table.** Identify its scientific question, target venue, main/supplement role,
   population, cohort(s), endpoint, timepoint, and source artifact.
2. **Write the table contract.** Use the asset `assets/table-spec.template.csv` for a table set,
   or state: `This table should let the reader compare/estimate [question] in [population] using
   [estimand], with [uncertainty and boundary].`
3. **Choose the archetype** from `table-archetypes.md`; define row order and columns before values.
4. **Reconcile inputs.** Check cohort flow, source-data file, statistical output, and canonical value
   keys. Mark missing/contradictory values; never infer them.
5. **Populate with one display policy.** Use consistent decimals, units, CI notation, p-value style,
   missing-data display, and reference labels. Keep exact source values in machine-readable output.
6. **Write title and footnotes.** Define population, abbreviations, tests, summary statistics,
   reference categories, multiplicity adjustment, missingness, and simulation status.
7. **Export.** For actual DOCX/XLSX/LaTeX artifacts, load the relevant document or spreadsheet
   skill/tool. Also preserve a CSV/source-data version when feasible.
8. **Audit.** Open `table-style-and-qa.md`; render or preview the final editable table, inspect page
   width and breaks, and cross-check values against figures and manuscript text.

## Output contract

Return the applicable subset: a bounded question needs its answer; audit needs findings, evidence
locations and the checks actually performed. Completed files and export QA apply only when files
were requested and produced. Missing analysis output does not block review of visible structure.

1. **`Table plan`** - table ID, question, cohort, estimand, source, main/supplement role.
2. **`Table shell`** - ordered rows, columns, group headings, reference levels, and footnote plan.
3. **`Completed table`** - only supplied/computed values; placeholders remain explicit.
4. **`Editable files`** - DOCX/XLSX/LaTeX as requested, plus CSV/source data where feasible.
5. **`Value crosswalk`** - cell/row to value key and source location for primary results.
6. **`QA report`** - denominator, CI/p-value, reference, missingness, abbreviation, width,
   pagination, simulation, and cross-artifact checks.
7. **`Author input needed`** - unresolved facts or outputs only the author/analyst can supply.

## Handoffs

- Statistical method and computed results -> `radiology-stats`.
- Radiomics feature selection/coefficient provenance -> `radiology-radiomics`.
- Deep-learning performance/ablation/fairness outputs -> `radiology-deep-learning`.
- Imaging-omics associations/pathways/cell composition -> `radiology-radiogenomics`.
- Figure-table value reconciliation -> `radiology-figure` / `radiology-pipeline`.
- Reuse or simplify a frozen table for a scientific presentation -> `radiology-paper2ppt` with
  canonical value keys, denominator/uncertainty context and editable source.
- Table callouts and legends in manuscript prose -> `radiology-writing` / `radiology-polishing`.
- Reporting checklist and final package -> `radiology-reporting` / `radiology-submission`.
