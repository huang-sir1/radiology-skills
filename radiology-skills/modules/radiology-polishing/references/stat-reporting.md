# Statistical reporting & number formatting

Match _Radiology_'s conventions (this file's default); **never change the underlying values** —
only formatting and completeness (flag if a required element, e.g. a CI, is absent).

> **These are AMA-style conventions, confirmed correct for _Radiology_ — they are not universal.**
> Nature-portfolio journals do not follow AMA style and commonly report P-values **with** a
> leading zero (`P = 0.03`, not `P = .03`); confirm the exact convention against the specific
> target journal's current style guide before polishing a Nature-family manuscript — do not
> silently apply the _Radiology_ rule below to a Nature submission. Reference style also differs
> (Nature-family: numbered, in citation order → `radiology-citation`/`export-formats.md`; not the
> author–year/AMA-numbered style assumed elsewhere in this file).

## P-values (_Radiology_ / AMA style — confirm before reusing for a non-AMA venue)
- Report **exact** p to two decimals (`P = .03`), or three when near .05 (`P = .047`).
- Use `P < .001` as the floor; don't write `P = .000` or `P = NS`.
- Italic capital **P**; no leading zero (`P = .03`, not `0.03`) — _Radiology_ omits the
  leading zero for quantities that cannot exceed 1 (p-values, proportions).

## Confidence intervals
- Every primary estimate gets a **95% CI**: "AUC, 0.88 (95% CI: 0.84, 0.92)."
- Use a comma (or "to") between bounds consistently; keep the same decimal places as the
  estimate.
- Report the **estimate + CI**, not just "significant."

## Decimals & leading zeros
- No leading zero for values that cannot exceed 1 (p, AUC, sensitivity, proportions): `.88`.
- **Do** use leading zero for values that can exceed 1 (HR 0.85 is wrong → HR can be <1 but
  the quantity scale exceeds 1, so write 0.85). Apply the "cannot exceed 1" rule: AUC/p/
  proportions → no leading zero; measurements/HR/OR/ratios → keep leading zero.
- Match precision to measurement; don't over-report digits (AUC to 2–3 dp; percentages to
  whole or 1 dp).

## Counts, percentages, ranges
- Percentages with the count: "27% (85 of 314)."
- Ranges with units: "tumor size, 1.2–4.8 cm"; IQR or SD stated ("mean, 56 years ± 12 [SD]").
- Specify the dispersion measure (SD vs SE vs IQR vs range) — ambiguity is a reviewer flag.

## Name the test
- State the test for every p: "(P = .004, DeLong test)," "(P = .02, McNemar test)," "(log-rank)."
- Report the software + version in Methods, and the CI method (Wilson/Clopper-Pearson/
  DeLong/bootstrap).

## Common fixes
`P < 0.05` → exact P + leading-zero rule (per the **confirmed target venue's** style, not
assumed); "significant" alone → estimate + CI + P + test; "0.88" AUC → ".88" (_Radiology_-family
only — keep the leading zero if the venue is Nature-family); percentage without n → add
"(x of y)"; mean without SD → add dispersion.

## Before polishing a non-_Radiology_ manuscript
Confirm the target venue first (→ `radiology-journal`). This file's leading-zero and reference
rules are _Radiology_/AMA-specific; applying them to a Nature-family manuscript is itself a
polishing error. When in doubt, flag the formatting choice to the author rather than silently
picking one.
