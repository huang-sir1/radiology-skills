# Statistical reporting & number formatting

Match _Radiology_'s conventions; **never change the underlying values** — only formatting and
completeness (flag if a required element, e.g. a CI, is absent).

## P-values
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
`P < 0.05` → exact P + leading-zero rule; "significant" alone → estimate + CI + P + test;
"0.88" AUC → ".88"; percentage without n → add "(x of y)"; mean without SD → add dispersion.
