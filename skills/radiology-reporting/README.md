# radiology-reporting

**Map an imaging study to the right reporting/quality guideline and audit it item-by-item
before it reaches a reviewer.** This is the compliance backbone of `radiology-skills` and
the single highest-leverage skill for getting AI/radiomics papers into _Radiology_.

## What it does

1. **Classifies** the study (task, design, endpoint, model dev/validation).
2. **Routes** it to the correct guideline stack — usually a *reporting* guideline **plus** a
   *quality / risk-of-bias* tool.
3. **Audits** every checklist item: `PRESENT / PARTIAL / MISSING / NA`, with manuscript
   location and a concrete fix.
4. **Prioritises** fixes as `Blocker / Should-fix / Polish`, each tied to the reviewer risk.

## Guidelines covered (current versions)

| Guideline | Version | Scope |
|---|---|---|
| **CLAIM** | 2024 Update (Radiology: AI) | Any medical-imaging AI study |
| **TRIPOD+AI** | 2024 | Diagnostic/prognostic prediction models (regression or ML) |
| **PROBAST / PROBAST-AI** | — | Risk of bias for prediction models |
| **CLEAR** | 2023 (ESR/EuSoMII), 58 items | Radiomics reporting |
| **METRICS** | 2024 (EuSoMII), 30 items / 9 categories | Radiomics methodological quality |
| **RQS / RQS 2.0** | 2017 / 2025 | Radiomics quality score (readiness levels) |
| **IBSI** | — | Standardised radiomic features + image processing |
| **STARD** | 2015, 30 items | Diagnostic-accuracy studies |
| **PRISMA-DTA** | 2018 | DTA systematic reviews |
| **QUADAS-2 / QUADAS-C** | — | Risk of bias in DTA studies |
| **STROBE** | — | Observational studies |
| **CONSORT-AI / SPIRIT-AI** | 2020 | AI trials / protocols |
| **DECIDE-AI** | — | Early-stage clinical evaluation of decision-support AI |

## Reference files

```
references/
├── guideline-router.md          decision tree + how guidelines stack (hybrid studies)
├── claim-2024.md                CLAIM 2024 Update, section-by-section
├── tripod-ai-probast.md         TRIPOD+AI items + PROBAST(-AI) domains
├── clear-metrics-rqs.md         radiomics reporting (CLEAR) + quality (METRICS, RQS/RQS 2.0)
├── ibsi-features.md             IBSI image processing + feature reproducibility
├── stard-prisma-quadas.md       diagnostic accuracy + DTA reviews + risk of bias
└── radiology-submission-map.md  where each item lives in a Radiology manuscript
```

## Example prompts

- "Audit this manuscript against CLAIM 2024 and give me page-referenced gaps."
- "I built a CT radiomics model for IDH status. Which checklists do I need?"
- "Is my feature extraction IBSI-compliant? What must I report?"
- "Fill the TRIPOD+AI abstract checklist for this paper."
- "What's my QUADAS-2 risk-of-bias exposure for this DTA review?"

## Integrity note

The skill never marks an item compliant to be agreeable, and never invents the missing
experiment or metric. It surfaces gaps and hands off drafting to `radiology-writing`,
statistics to `radiology-stats`, and availability wording to `radiology-data`.
