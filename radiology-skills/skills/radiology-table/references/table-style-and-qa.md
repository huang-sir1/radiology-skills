# Table style and QA

## Style contract

Verify the current target guide before final export. Until verified, use a conservative academic shell:

- white background, black text, restrained horizontal rules, no decorative gradients;
- no vertical grid unless the target template requires it;
- sentence-case title and concise, self-contained footnotes;
- align text left, numbers by decimal where supported, and confidence intervals consistently;
- repeat header rows across pages; do not split a variable and its levels across pages when avoidable;
- use abbreviations only when defined below the table;
- avoid color as the only carrier of meaning.

## Numeric policy

Define one policy per table set:

- summary statistics precision by variable type and measurement resolution;
- estimate/CI precision that preserves interpretation;
- exact p values with the target venue's threshold floor;
- percentages with their denominator, especially when missing values differ;
- use an em dash or `NA` only with a footnote that distinguishes not applicable from not measured.

Do not change source values merely to make columns line up. Round only at display time.

## Footnote minimum

Footnotes should identify:

1. population/cohort and unit of analysis;
2. summary statistics and statistical tests;
3. reference categories and covariate adjustment;
4. CI, p-value, and multiplicity methods;
5. missing-data handling;
6. abbreviations;
7. simulation/teaching status when applicable.

## Width and pagination

- Prefer meaningful row groups to tiny text.
- Split a wide table into main and supplementary tables when columns encode different questions.
- Use landscape only when the journal accepts it and splitting would harm interpretation.
- For long tables, repeat headers and keep the title/continued label consistent.
- Inspect the rendered DOCX/PDF or workbook preview; cell text must not clip, wrap incoherently, or overlap.

## Audit checklist

| Check | Pass condition |
|---|---|
| Population | title/footnote states cohort and n |
| Denominators | counts and percentages reconcile with flowchart and Table 1 |
| Values | primary cells trace to source output/value keys |
| Uncertainty | effect/performance estimates have correct CI and cohort |
| Reference levels | every categorical contrast is interpretable |
| Missingness | variable-level missingness or handling is stated |
| Multiplicity | adjusted and unadjusted values are not confused |
| Labels | model, endpoint, timepoint, and units match manuscript/figures |
| Style | guide-specific title, numbering, footnotes, and file format verified |
| Render | no clipping, overflow, orphan header, or unreadably small type |
| Provenance | simulated content is clearly labelled and ineligible for submission |

Use `../scripts/audit_table_csv.py` for structural CSV checks, then visually inspect the editable/rendered
table. Structural validation cannot judge scientific appropriateness.

