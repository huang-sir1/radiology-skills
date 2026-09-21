# Reader (annotator) protocol

Readers are part of the method. Specify them so the segmentation is reproducible and unbiased.

## What to specify

| Element | Decision | Why it matters |
|---|---|---|
| **Number of readers** | ≥2 for a reproducibility subset (all or a defined sample) | Enables inter-observer ICC/Dice |
| **Seniority** | Years of experience, specialty | Reviewer expects expertise appropriate to task |
| **Blinding** | Blinded to outcome/label and to each other | Prevents outcome-driven contouring bias |
| **Independent vs consensus** | Independent first (for agreement), consensus for the analysis mask | Mixing them hides disagreement |
| **Adjudication** | Senior third reader / rule for resolving disagreement | Defines the final mask provenance |
| **Reference for auto-seg** | Manual reference + human correction protocol | If a model pre-segments, define the QC/edit step |
| **Training/calibration phase** | Shared cases + protocol before the study set | Reduces avoidable variance |
| **Software + version** | Named tool and version | Reproducibility (IBSI/CLEAR) |

## Independent → agreement → consensus (recommended flow)

1. All reproducibility-subset cases segmented **independently** by ≥2 blinded readers.
2. Compute inter-observer agreement (ICC/Dice/HD) and feature stability on this subset
   (→ reproducibility-qc.md).
3. For the analysis cohort, use a **defined** final mask: single trained reader, consensus, or
   adjudicated — stated explicitly.
4. Intra-observer: one reader re-segments a subset after a washout (e.g. ≥2 weeks).

## Common reviewer objections this pre-empts

- "Who segmented, with what experience, blinded to what?"
- "Is the final mask one reader, consensus, or adjudicated?"
- "How was inter-/intra-observer reproducibility measured, and on how many cases?"
- "Were non-reproducible features removed before modelling?"

## Reporting sentence

*"Segmentation used software/version [AUTHOR_INPUT_NEEDED], with reader number, roles and
experience [AUTHOR_INPUT_NEEDED], under independence and blinding conditions
[AUTHOR_INPUT_NEEDED]. The analysis-mask production procedure was [AUTHOR_INPUT_NEEDED]."*

- Only if inter-observer reproducibility was assessed: *"The reproducibility subset size,
  selection method and rationale were [AUTHOR_INPUT_NEEDED]; metrics and specifications were
  [AUTHOR_INPUT_NEEDED]."*
- Only if intra-observer reproducibility was assessed: *"Repeat annotation used reader and
  subset [AUTHOR_INPUT_NEEDED], with repeat-annotation interval [AUTHOR_INPUT_NEEDED]."*

Fill from the annotation protocol and execution records, including deviations. Remove unperformed
branches; unknown reader experience, blinding, sampling or washout details remain unverified, not
inferred from the recommendations above. Do not turn a recommended design into completed Methods.
