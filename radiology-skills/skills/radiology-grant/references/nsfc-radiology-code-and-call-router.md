# NSFC radiology code and call router

Read this when an NSFC proposal uses imaging, AI, radiomics, nuclear medicine, image-guided
intervention, biomedical engineering or a medical clinical programme. This router narrows candidate
codes and call types; only the current annual guide and exact special-call guide can establish the
final route.

## Route the primary scientific claim, not the department

Ask what claim would remain if imaging were removed:

- **Image formation, acquisition, reconstruction, quantitative phenotype, image processing or
  analysis** → first inspect H27.
- **Biomedical device, engineering system or regenerative-medicine construct** → inspect H28 and
  compare with H27.
- **Tumour mechanism, treatment response or tumour clinical translation where imaging is an evidence
  source** → inspect H18 as well as H27/H28.
- **Radiation injury, protection or non-tumour radiation-treatment science** → inspect H29.
  Diagnostic radiology generally returns to H27; tumour radiotherapy generally uses the applicable
  H18 code.

Using an image does not automatically make H27 correct. A hospital department, old funded proposal
or familiar review panel is not evidence of the current code.

## 2026 H27 working snapshot

The 2026 Medicine code page lists:

| Code | Area |
|---|---|
| H2701 | MRI |
| H2702 | X-ray/CT, electron and ion beams |
| H2703 | ultrasound |
| H2704 | nuclear-medicine diagnosis and therapy |
| H2705 | medical optical imaging |
| H2706 | molecular imaging |
| H2707 | bioelectromagnetic imaging |
| H2708 | medical-image processing, analysis and visualization |
| H2709 | medical-imaging big data and artificial intelligence |
| H2710 | interventional medicine and engineering |
| H2711 | new imaging technologies and methods |

This table is a `2026_OFFICIAL_CYCLE_SNAPSHOT`, not a permanent codebook. Re-open the current H-code
page, named programme guide and division notes at use. Old guides in which H18 or H22 had historical
meanings are stale-code evidence and must trigger re-routing.

## Code decision record

```text
Application year:
Programme and special direction:
Primary scientific question and highest claim:
Imaging role: scientific object / measurement / predictor / supporting evidence / intervention
Candidate code 1 + current official definition:
Candidate code 2 + current official definition:
H18/H27/H28/H29 boundary considered:
Current division notes/exclusions:
Host/NSFC confirmation needed:
Route state: VERIFIED_CURRENT / ADMIN_CONDITIONAL / CONFLICTING / NOT_ESTABLISHED
```

Do not choose a code solely to chase a historical descriptive funding ratio.

## Medical clinical programme

Stable programme logic from the Medicine division is:

`clinical observation or diagnostic/treatment bottleneck → key scientific question →
problem-driven basic/clinical/engineering integration → evidence that returns to diagnosis or
treatment value`.

A clinical-effect comparison, software platform or model leaderboard without a basic/applied-basic
scientific question is not enough.

### Published 2024–2026 status

| Cycle | Guide/result snapshot | Boundary |
|---|---|---|
| 2024 | guide planned about 100 projects and about CNY 0.70 million/project; results report 1,811 applications, 1,798 accepted, 130 funded, average CNY 0.66 million; H27 91/91/7 and H28 48/48/4 | clinical programme only |
| 2025 | guide planned about 130 projects and about CNY 0.65 million/project; wording tightened toward a diagnosis/treatment bottleneck and applicant/team practice; results report 1,895/1,890/130, average CNY 0.5895 million; H27 102/101/8 and H28 44/44/6 | clinical programme only |
| 2026 | public clinical-programme index accessed 2026-08-28 lists through 2025; a 2026 exchange meeting shows continuation but not application quota, amount or outline | return `NOT_ESTABLISHED`; never carry forward 2025 parameters |

Historical counts may describe the named clinical programme. They are not ordinary H27/H28 success
rates and do not predict an applicant's funding probability.

## Special-call boundary

Medicine and AI special calls provide direction evidence, not universal thresholds. A call may
require an existing cohort, longitudinal multimodal collection, mechanism mapping, a specific number
of sites, a budget or a performance target. Those parameters stay inside that exact call.

For every special route record:

`call title/identifier | issue and deadline | eligible programme/type | exact direction | special
outline/attachments | quota/budget regime | current/closed status | non-transferable parameters`.

An expired call cannot be `VERIFIED_CURRENT`; use it only as historical strategy context.

## Scientific-question gate for imaging calls

Before code selection, write:

`clinical phenomenon/bottleneck → scientific unknown → image physics/contrast or measurable
phenotype → biological/clinical proposition → matched validation/intervention → bounded value`.

If the chain stops at “build a model/platform/database,” return `STOP_AND_REFRAME`. If imaging is a
surrogate for a mechanism claim without matched pathological, molecular, temporal or perturbational
evidence, lower the claim ceiling.

## Ethics and data routing

- Current Medicine guidance can require ethics documentation for relevant applications; record
  approved/pending/not submitted, never predict approval.
- Pure clinical/imaging/protein/metabolite data are excluded from the current implementation rule's
  definition of human genetic-resource information, but remain sensitive health information subject
  to ethics, privacy and security controls.
- Imaging linked to biospecimens, genes/genomes or linkable human genetic-resource data may trigger
  HGR review.
- A 2026 HGR revision consultation draft is `DRAFT_NONCONTROLLING`, not current law.
- Multicentre, cloud, cross-border and hosted-model routes each require a separate data-flow review.

See [source-registry.md](source-registry.md) for the year-bound code and programme sources.
