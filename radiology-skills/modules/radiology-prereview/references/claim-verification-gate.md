# Claim verification gate

Use this reference before submission, after major rewriting, or whenever a manuscript contains important background, novelty, guideline, numerical, or comparison claims.

## Verification modes

| Mode | Use when | Rule |
|---|---|---|
| Search mode | Need to find or verify supporting literature | Search source-of-record databases and verify identifiers |
| Doc-only mode | User supplied a closed evidence packet | Verify only against provided documents; mark outside claims as `CANNOT ASSESS` |
| Visual/table mode | Claim appears in a figure, table, abstract, or Key Results box | Check the plotted/table value against source data or manuscript numbers |

State the mode at the start of the output. Do not blur doc-only verification into internet verification.

## Claim extraction

Break text into atomic claim units. Use stable IDs:

- `BKG-01`: background or disease-burden claim
- `GAP-01`: limitation or unmet-need claim
- `NOV-01`: novelty or "first" claim
- `MET-01`: method/guideline claim
- `NUM-01`: numerical claim, including sample size, AUC, HR, CI, p value, percentage, date
- `CMP-01`: comparison with prior work
- `FIG-01`: figure/table/visual claim
- `BIO-01`: biological or mechanistic interpretation

One sentence can contain several claims.

## Extraction confirmation gate

Use a strict two-pass architecture:

1. **Extraction pass only**: list all claims, types, and locations. Do not verify yet.
2. **Verification pass only**: verify the fixed claim list. Do not add new claims silently.

For long manuscripts, the user does not need to approve every claim before verification, but the extracted list must be preserved in the output so later audits can reproduce what was checked.

## Source hierarchy

Prefer the highest source type that matches the claim:

1. Guidelines, consensus statements, reporting standards, trial registries, dataset records.
2. Original peer-reviewed study with DOI/PMID and accessible metadata.
3. Systematic review/meta-analysis for broad background claims.
4. Preprint only when clearly marked and no peer-reviewed source exists.
5. Secondary citation lists only as leads, not final support.

For imaging-specific claims, prioritize radiology/imaging venues when the claim is about imaging practice. For biology/method claims, broaden appropriately.

## Support status

| Status | Meaning |
|---|---|
| `VERIFIED` | Source directly supports the claim and identifier/metadata are verified |
| `SUPPORTED` | Source supports the claim with minor wording adjustment |
| `PARTIAL` | Source supports only part of the claim or a narrower version |
| `BACKGROUND_ONLY` | Source provides context but not evidence for the specific claim |
| `CONFLICT` | Credible sources disagree |
| `UNSUPPORTED` | No adequate support found/provided |
| `CANNOT_ASSESS` | Verification impossible in current mode or with available access |

If status is not `VERIFIED`, propose a bounded wording change or a missing-input request.

## Numerical precision rules

- Sample sizes, events, dates, scanner counts, centers, AUC, HR, OR, CI, p values, and percentages must match the source or source data.
- Rounding is allowed only if mathematically consistent and the precision is not misleading.
- CI and p value direction must agree with the reported effect.
- Do not convert unadjusted results into adjusted claims.
- Do not cite a training cohort result as external validation.
- Do not cite a correlation as causation or biological mechanism.

## Strict visual/table checks

For abstracts, Key Results, figure legends, graphical abstracts, tables, and slides, use stricter numeric verification:

| Check | Failure |
|---|---|
| Rounding changes clinical interpretation | numerical error |
| CI/p-value copied without cohort label | misleading |
| Internal cohort metric described as external validation | hallucination/unsupported |
| Figure axis or legend implies a different endpoint | visual claim error |
| Table 1 denominator differs from flowchart | consistency error |
| KM/DCA/ROC text reports a value not present in source data | numerical error |

## Two-pass workflow

1. **Pass A: claim extraction**
   - Extract all claim IDs and classify them.
   - Mark whether each claim needs a citation, manuscript data check, figure/table check, or author input.
2. **Pass B: verification**
   - Retrieve or inspect evidence.
   - Verify identifiers.
   - Assign support status.
   - Recommend citation, rewording, deletion, or author input.

## Output table

| Claim ID | Claim text | Claim type | Evidence/source | DOI/PMID/accession | Status | Required action |
|---|---|---|---|---|---|---|
| BKG-01 | ... | background | ... | ... | VERIFIED | cite |
| NOV-01 | ... | novelty | ... | ... | PARTIAL | soften novelty |
| FIG-01 | ... | visual claim | source data / figure | n/a | UNSUPPORTED | correct figure or text |

This gate feeds `radiology-prereview` and should be repeated after major revision.
