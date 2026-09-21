# Mock-review report format

Mirror a real journal review so the author can rehearse the response. Be specific, located, and
fixable.

## Structure

```
SUMMARY ASSESSMENT
  [3–5 sentences: what the study does, its genuine strength, its decisive weakness,
   and the scientific-prereview state.]

P0 / P1 DECISION-BEARING COMMENTS
  [Finding ID]. Source: [artifact SHA-256 + evidence anchor].
     Issue/criterion: [observed defect + governing criterion].
     Claim consequence: [affected Claim IDs + ceiling if unchanged].
     Repair/closure: [minimum repair → skill + observable closure evidence + residual boundary].
  2. ...

MINOR COMMENTS
  1. [Issue] — Location. Fix.
  ...

CLAIMS vs EVIDENCE
  - [Overclaim] → [bounded rewording].

SCIENTIFIC PREREVIEW STATE
  [SCIENTIFIC_PREREVIEW_PASS / SCIENTIFIC_PREREVIEW_CONDITIONAL /
   SCIENTIFIC_PREREVIEW_FAIL] — because [reasons].
  [This is not an all-files submission-package READY verdict.]

CANONICAL PREREVIEW RECEIPT
  [receipt path/version + analysis-lock digest + claim-registry digest + scientific-handoff digest]
  [scientific_prereview_receipt_digest + validator PASS/FAIL]

FIX ORDER (highest leverage first)
  1. [the fix that unlocks the most] → [skill]
  2. ...
```

## Tone & rules

- Numbered, specific, located — never "improve the statistics" without saying which and where.
- Each P0/P1 finding cites the governing criterion, source digest, affected Claim IDs and frozen
  closure evidence a re-review can observe.
- Preserve an immutable `source_review_state` beside the current verification state. Every P0/P1
  sets `required_for_pass=true`; only an explicitly advisory P2 may be nonblocking.
- Separate **fatal** from **cosmetic**; don't bury a Blocker among wording nits.
- Hand back fixes, routed to the producing skill — this is a review *to act on*.
- State the scientific-prereview state honestly; do not reassure past a real P0/P1.

## Optional: target-journal calibration

If a target tier is given, add one line per major comment: *"At [tier], this is
[blocking / expected-revision / acceptable]"* — and route venue choice to `radiology-journal`.
