# Nature Portfolio Reporting Summary & Editorial Policy Checklist

A **separate, additional** disclosure layer required by Nature-portfolio journals (Nature
Medicine, Nature Biomedical Engineering, Nature Communications, npj Digital Medicine, Nature
Machine Intelligence, etc.) for life-sciences (and behavioural/social-science,
ecology/evolution/environmental-science) research. It sits **alongside**, not instead of,
CLAIM/TRIPOD+AI/CLEAR — audit both stacks; they check different things.

## What it is, and when it applies

- The **Reporting Summary** is a structured form completed by the corresponding author,
  covering experimental/analytical design details that are frequently under-reported. It is
  used by editors and reviewers **during assessment** and is **published with the accepted
  article** — treat every field as something a reader will eventually see, not an internal-only
  disclosure.
- The **Editorial Policy Checklist** is a related, separate form some Nature-portfolio journals
  require once a manuscript is sent for review. It is **not sent to reviewers**, but the editors
  must have it before review starts.
- Applies to life-sciences submissions at Nature-portfolio venues (imaging-AI, radiomics, and
  radiogenomics studies are in scope). Verify live whether the specific target journal requires
  it and which current version of the form applies — Nature Portfolio updates the form
  periodically.

## Core disclosure items (map from what this suite already produces)

Most of these fields are answerable directly from work already done in
`radiology-design`/`radiology-stats`/`radiology-reporting` — this file is about **not forgetting
to transcribe it into the Reporting Summary**, not about generating new analysis.

| Reporting Summary asks | Source in this suite |
|---|---|
| Exact sample size (n) per group/condition, as a discrete number + unit | `radiology-design` cohort inventory; Results flow (`radiology-writing/results.md`) |
| Whether measurements are from distinct samples or the same sample measured repeatedly | `radiology-annotation` (repeat-annotation design), `radiology-design` (unit of analysis) |
| Statistical test(s) used, and whether one- or two-sided | `radiology-stats` — name the test explicitly, as already required by `radiology-polishing/stat-reporting.md` |
| Data exclusions and the criterion (pre-specified or post hoc) | `radiology-design/feasibility-triage.md`, patient-flow diagram |
| Replication — whether attempts to replicate succeeded | `radiology-design/validation-strategy.md` (external/temporal/geographic validation) |
| Randomisation — how samples/participants were allocated to groups | Reader studies (`radiology-translation/reader-study.md`); dataset splits (patient-level, `radiology-radiomics`/`radiology-deep-learning` leakage audits) |
| Blinding — who was blinded to what | `radiology-annotation/reader-protocol.md`, `radiology-translation/reader-study.md` |
| Software used for data collection **and** analysis, with version numbers | `radiology-radiomics/feature-extraction.md` (PyRadiomics + version), `radiology-deep-learning/training-protocol.md` (framework + version), `radiology-stats` code blocks |
| Data availability statement, incl. accession codes/identifiers/web links and any restrictions | `radiology-data` |
| Materials/code availability | `radiology-data` — Nature Portfolio treats this as **a condition of publication**, not a courtesy; see `radiology-data/availability-and-fair.md` |

## Field-by-field discipline

- **Never fill a field with an invented value.** If sample size, blinding status, or software
  version is not yet known, mark it as a placeholder/待确认, exactly as the rest of this suite
  already does — the Reporting Summary is published, so a fabricated field is a permanent,
  citable integrity failure.
- **Consistency check**: every number in the Reporting Summary must match the manuscript and
  the Source Data (→ `radiology-figure/nature-figure-spec.md`,
  `figure-set-consistency.md`) — treat it as one more place `figure-set-consistency.md`'s
  cross-validation discipline applies.
- **Statistics fields** must name the exact test and sidedness — reuse the same test name
  already required in `radiology-polishing/stat-reporting.md` (the analysis itself routes to
  `radiology-stats`); do not paraphrase differently in the two places.

## Output

```
Reporting Summary draft:
  Sample size:            [n per group, unit, source]
  Data exclusions:        [criterion, pre-specified Y/N]
  Replication:            [attempted? succeeded? cohort]
  Randomization:          [method, or NA + why]
  Blinding:               [who, to what, or NA + why]
  Statistics & software:  [test(s), one/two-sided, software+version — from radiology-stats]
  Data availability:      [→ radiology-data]
  Materials/code:         [→ radiology-data — condition of publication]
  待确认 (author-only):    [fields only the author can supply]
```

## Handoffs
- Data/code availability wording, accessions, Extended Data vs Source Data → `radiology-data`.
- The statistics fields (test name, sidedness, CI method) → `radiology-stats`.
- Whether this venue currently requires the Reporting Summary / which version → verify live
  (→ `radiology-search`) before finalising.
- CLAIM/TRIPOD+AI/CLEAR item-by-item audit (a separate, complementary stack) → the routing table
  in `guideline-router.md`.
