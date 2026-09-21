# Feasibility and common rejection mechanisms

Feasibility is an evidence chain, not the sentence “the team has a strong foundation.” Run the
imaging-specific checks in `radiology-feasibility-audit.md` for any full proposal.

## Minimum feasibility evidence

| Dimension | Evidence to request | Overclaim to prevent |
|---|---|---|
| Preliminary work | traceable sample/cohort, code/version, output, denominator and limitations | pilot performance proves external utility |
| Data access | per-site counts, time span, modalities, metadata, labels, events, access agreement | “large database” means usable matched data |
| Measurement | series/protocol/reconstruction/QC inventory and drift plan | DICOM availability means comparable quantitative images |
| Reference standard | construction, timing, readers, adjudication and reliability | routine report text is automatically ground truth |
| Statistics | independent units, sample/event/cluster justification and failure assumptions | images/lesions are independent patients |
| Team | named expertise mapped to tasks and effort | publication prestige substitutes for missing expertise |
| Platform | acquisition, annotation, storage, compute, MLOps and external-validation capability | generic “hospital platform” proves execution |
| Ethics/governance | actual status and responsible authority, not predicted approval | planned submission equals authorization |
| Operations | milestones, owners, dependencies, decision rules and fallback | calendar activities equal measurable progress |
| Budget | quantity × unit cost tied to aims | round totals or generic categories establish reasonableness |

Never fabricate, estimate or “complete” preliminary results that the team cannot anchor. A modest,
bounded pilot is stronger than a precise but unauditable claim.

## Common rejection mechanisms

| Mechanism | Symptom | Repair |
|---|---|---|
| Engineering instead of science | “build/optimize a model” is the objective | reframe to a falsifiable knowledge, measurement or clinical-decision question |
| Unverified premise | novelty/gap rests on a few supportive citations | live search, contradiction check and claim-level source anchors |
| Hollow innovation | “first”, “multimodal”, “foundation model” without a consequential increment | identify question/data/measurement/method/validation/mechanism increment and why it matters |
| Open-loop route | method list cannot be traced back to question and inference | map every aim to evidence, analysis, result pattern and claim ceiling |
| Image-formation blindness | protocol, reconstruction, QC and shift are absent | freeze measurement passport; budget QC/harmonisation validation |
| Leakage or pseudoreplication | slice/lesion splits; clustered units analysed as independent | split and analyse at the defensible independent-unit hierarchy |
| Weak ground truth | report-derived or single-reader labels treated as error-free | define construct, timing, readers/adjudication and uncertainty analysis |
| Thin transport plan | one-center retrospective study promises broad deployment | temporal/site/vendor/prospective validation appropriate to the claim |
| No clinical comparator | model performance without standard-of-care or decision context | add intended use, comparator, reader/workflow design and utility endpoint where warranted |
| Decorative contingency | fallback is another model or post hoc subgroup | specify a different valid inference or honest re-scope |
| Budget–design mismatch | annotation, readers, scans, assays or external sites do not reconcile | derive cost from aim quantities and milestones |
| Over-scoping | mechanisms, prediction, prospective deployment and omics in one small project | narrow to the minimum coherent evidence ladder |
| Administrative/scientific conflation | a compliant form is called competitive, or a strong idea is called eligible | issue separate gate verdicts |

## Technical-route closure

```text
need → question → aim → measurement/data → comparator/analysis → result pattern → inference
                         ↓                         ↓
                  QC/dependency              milestone/fallback
                         └────────── risk + budget ──────────┘
```

The route is closed only when failure states are visible. “Successful model training” is not an
endpoint unless the aim is explicitly technical and the success criterion is defensible.

## Live-rule boundary

Eligibility, limit counts, official section names, page/character limits, attachments, deadlines,
budget categories/regime, ethics documents and AI-use requirements vary by call and cycle. Put them
in the call passport with official evidence; otherwise report `NOT_ASSESSABLE` rather than relying
on memory or an older proposal.
