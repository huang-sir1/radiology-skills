# radiology-polishing

**Polish finished imaging-research prose to _Radiology_ (RSNA) house style** — precise,
concise, correctly formatted, American English, no overclaiming. (To draft/restructure new
content, use `radiology-writing`.)

## What it does
- Tightens prose: short sentences, one idea each, filler removed, clear subjects.
- Enforces **statistical reporting**: estimate + 95% CI, exact p-values, correct number/unit
  format, named tests — **without changing any value**.
- Applies American English and abbreviation rules.
- Flags **overclaiming** and unwarranted causal language; calibrates hedging to evidence.

## Reference files
```
references/
├── radiology-house-style.md  voice, tense, American spelling, abbreviations, units
├── stat-reporting.md         p-values, CIs, decimals, %, n, ranges, test names
└── style-guardrails.md       overclaim/causation detection, hedging, forbidden phrasings
```

## Example prompts
- "Polish this Results paragraph for _Radiology_ and fix the stat formatting."
- "Convert to American English and journal style."
- "Is the conclusion overclaiming for a single-center retrospective study?"

## Integrity
Never alters reported numbers, CIs, p-values, or citations; flags suspected errors instead.
Returns clean prose + a short change log. Hands new content to `radiology-writing` and
missing statistics to `radiology-stats`.
