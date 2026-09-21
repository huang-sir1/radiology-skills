# Visual evidence and radiology-image handling

Use this reference whenever a deck contains scientific figures, tables, medical images, video,
external assets, or data-dependent graphics. A visual is an evidence carrier, not decoration.

## Visual-selection gate

For each proposed visual, answer:

1. Which slide claim does it support?
2. Which source and exact locator authorize the values or pixels?
3. What must remain visible for a technically competent audience to interpret it?
4. What transformation is required for presentation scale?
5. Could that transformation change meaning or hide uncertainty?
6. What privacy, confidentiality, copyright, license, or embargo constraint applies?
7. What text alternative and spoken description makes its evidentiary role accessible?

Remove visuals that cannot answer question 1. Use `STOP` when a decisive visual fails questions 2,
5, or 6 and no compliant substitute exists.

## Evidence-carrier fidelity contract

Freeze two independent classes in the deck brief:

- **Artifact fidelity:** `NATIVE_EDITABLE` when the delivered scientific objects must remain
  editable; `MIXED_EDITABLE_AND_SOURCE_CROPS` when native objects and justified exact source crops
  coexist; `RENDERED_REFERENCE_ONLY` only when the user requested a non-editable reference output
  rather than an editable presentation artifact.
- **Evidence fidelity:** `EVIDENCE_CRITICAL` for decisive results or methods that must survive
  audit; `EVIDENCE_SUPPORTING` for contextual evidence; `EXPLORATORY_STORYBOARD` for a clearly
  labelled planning visual that does not assert a scientific result.

For evidence-critical slides:

- keep numbers, labels, citations, equations, and table cells as native editable text, equations,
  or tables; keep charts/diagrams as editable vectors when the underlying values or geometry are
  available;
- when native reconstruction would introduce error or the authoritative object is an image, use an
  accurate source crop that remains legible, with an exact locator and transformation record;
- reconcile all recreated values, symbols, labels, panel identities, and equations to the source;
- never use image generation or text-to-image rendering to carry data, numerical results, tables,
  equations, citations, medical-image findings, or other scientific evidence. Generated imagery may
  be used only as visibly labelled `GENERATED ILLUSTRATION — NOT EVIDENCE`, with no implication that
  it depicts an observed patient, result, mechanism, or validated workflow;
- show unresolved content on-slide as `MISSING — [item]` or `UNVERIFIED — [item]`. Do not replace it
  with plausible-looking generated content. A decisive missing or unverified dependency is `STOP`;
  a non-decisive bounded placeholder is at most `CONDITIONAL`.

Do not infer `NATIVE_EDITABLE` from a PPTX filename alone: record the class and the allowed source-
crop exceptions. Conversely, a screenshot embedded in an editable container is not itself editable.

## Figure transformation contract

### Prefer the smallest sufficient evidence unit

- Split a dense manuscript multipanel into sequential slides or scenes. Retain original panel letters
  in the source ledger even when only one panel is shown.
- Crop whitespace and irrelevant neighboring panels, not axes, legends, numbers at risk, scale bars,
  uncertainty, acquisition labels, or comparison groups needed for interpretation.
- Increase labels or recreate a chart only from accessible underlying values. Upscaling a screenshot
  does not recover data or permit selective retyping.
- Use progressive reveal only when each stage has a stable interpretation and the final full context
  is shown. Record the reveal as a presentation transformation.

### Preserve the statistical object

Keep or explicitly restate:

- analysis population and denominator;
- endpoint/metric definition and direction;
- units, axis scale, limits, and transforms;
- point estimate and interval or distribution;
- group/reference level and paired/repeated structure;
- time origin, follow-up, censoring, and numbers at risk when applicable;
- threshold and operating point for diagnostic/prediction displays;
- multiplicity or exploratory status when it changes interpretation;
- cohort/split/site and whether evaluation was frozen, external, or adapted.

Never change a truncated axis, log scale, smoothing, binning, normalization, color scale, or reference
line without recording and visibly labelling the change when it can alter interpretation.

### Show data structure, not only a summary

For continuous values in small samples, prefer a distribution or individual observations when
available rather than a bar with mean and error bar. Paired data should preserve pairing. If only a
published summary figure exists, report that limitation instead of fabricating raw-data detail.

### Recreated visual label

Use one of:

- `Reproduced unchanged from [source]`
- `Cropped from [source]; panel/axes/legend preserved`
- `Recreated by presenter from reported source values`
- `Adapted from [source]; changes: ...`
- `Author-generated from frozen analysis [receipt/version]`

“Recreated” must not imply validation against source data. Reconcile every value and report the check.

## Table transformation contract

Main-deck tables should answer a decision, not reproduce an entire paper table at unreadable scale.

1. Preserve the full table in source or backup when needed for audit.
2. Select a decision-relevant slice for the main slide.
3. Keep row/column definitions, denominator, units, missing values, and footnotes that qualify the
   selected cells.
4. Highlight without hiding non-highlighted comparators.
5. Reconcile selected values cell-by-cell with the source.
6. If converting to a chart, specify the transformation and do not infer unavailable uncertainty.

Use `radiology-table` when the task is to design or audit a standalone scientific table; this skill
owns only its slide-level selection and presentation transformation. Use `radiology-figure` for
standalone publication figures or source-data visual analysis; this skill owns how a frozen visual is
used in the deck.

## Radiology image passport

Every decisive medical-image scene needs enough context to prevent false equivalence or
mislocalisation. Record what applies:

| Field | Examples |
|---|---|
| Object | patient/exam/series/reconstruction/frame/slice/lesion/ROI |
| Modality | CT, MR, PET, SPECT, radiography, mammography/DBT, ultrasound |
| Acquisition identity | phase, sequence, tracer/time, view, plane, b-value, contrast state |
| Display identity | window/level or preset, color map, fusion/opacity, inversion, projection |
| Spatial context | orientation markers, laterality, slice location, plane, zoom, scale bar |
| Transformation | crop, resize, interpolation, annotation, registration, fusion, enhancement |
| Annotation | arrow/outline/ROI author, purpose, and reference standard if relevant |
| Evidence state | representative example, prespecified case, error case, selected exemplar, aggregate |
| Source | DICOM/series or figure locator, paper/project version, and permission state |

### Non-negotiable image rules

- Keep laterality/orientation consistent. Do not mirror an image for layout.
- Do not present two sequences, phases, reconstructions, or time points as comparable without their
  identity and any relevant registration or normalization.
- Preserve the lesion/ROI context and label who created or verified an annotation. An arrow is not a
  reference standard.
- Record window/level, color map, fusion, inversion, projection, crop, zoom, interpolation, and
  enhancement when they can affect what is seen.
- If a static slice cannot support a volumetric, dynamic, cine, or stack-dependent claim, use an
  appropriate video/stack presentation when delivery supports it or show a labelled storyboard.
- A “representative image” selected after outcomes were known must be labelled as selected; it does
  not establish prevalence, typicality, or model explanation.
- AI saliency/attention maps are model-derived visualizations, not pathology or causal mechanism.
  Keep the base image and method/context visible and route scientific interpretation to the proper
  imaging-AI owner.

### Grayscale and display boundary

DICOM PS3.14 defines a grayscale display function for consistent perceptual rendition on standardized
display systems. A PowerPoint export, laptop, projector, videoconference stream, or screenshot does
not thereby become a calibrated diagnostic display.

- Preserve the intended grayscale mapping and avoid uncontrolled contrast enhancement.
- Inspect decisive grayscale images on the planned delivery path when feasible, including exported
  file, presenter machine, projector/room or conferencing compression.
- State `DISPLAY_PATH_NOT_VERIFIED` if that path was not tested.
- Treat slides as scientific communication, not a diagnostic workstation. Do not make individual
  patient-care decisions from the deck.

Consult `radiology-acquisition-qc` when acquisition, reconstruction, or display transformations are
scientifically decisive rather than presentational.

## Privacy and confidentiality gate

Before importing any clinical image or video:

1. Confirm authorization and intended audience/publicity state.
2. Inspect DICOM and exported-file metadata; do not assume export removed identifiers.
3. Inspect the pixel region, overlays, captions, headers/footers, thumbnails, filenames, notes,
   embedded objects, and hidden slides for names, IDs, dates, institutions, faces, accession numbers,
   or other identifying information.
4. Apply the appropriate institution-approved de-identification workflow and maintain internally
   consistent pseudonyms only when scientifically required and authorized.
5. Re-render and inspect after de-identification; cropping the visible header alone is not a complete
   confidentiality profile.

**Presentation-software redaction is not de-identification.** A crop, black rectangle, same-color
text, mask, or off-canvas placement inside PowerPoint/Google Slides/Keynote may leave the original
pixels or text recoverable. Before insertion, permanently remove PHI using an authorized safe
capture, PACS overlay suppression/anonymization, or approved image-processing workflow. Before any
public handoff, run the presentation application's permanent cropped/hidden-content removal and
document-inspection/sanitization functions, then inspect slides, notes, hidden slides, embedded media,
and exported PDF again. A successful-looking slideshow view is not evidence that the package is clean.

DICOM's Basic Application Level Confidentiality Profile is designed for special-purpose de-identified
datasets used in teaching/research, but the standard explicitly notes that conformance does not
guarantee confidentiality. Burned-in pixel information and graphics/overlays require specific checks.
Institutional policy and applicable law remain authoritative.

Use `STOP` for any unresolved patient identifier or unapproved confidential content. Do not place
private source material in an external service merely to create a slide.

## Source provenance and rights

Maintain one row per external asset:

| Field | Required entry |
|---|---|
| `asset_id` | stable local identifier |
| `creator/title` | supplied creator and work title, if available |
| `source_locator` | URL/DOI/page/figure/panel or project artifact/version |
| `rights_state` | owned, permission documented, public domain, named license, exception assessed by owner, or unknown |
| `permitted_use` | internal meeting, teaching, conference, public upload, redistribution, or other bounded use |
| `transformation` | unchanged, crop, annotate, recolor, redraw, composite, or other material change |
| `visible_credit` | short credit or source key used on slide/caption |
| `notes_credit` | complete source and license/permission details |

For Creative Commons material, use the supplied Title, Author, Source, and License (TASL) when
available and indicate modifications. Check whether the license permits adaptation and the intended
commercial/public use. For other material, citing the source does not itself grant permission.

If rights are unknown:

- internal review may proceed only under the user's/institution's authorized basis and must retain
  `RIGHTS_UNRESOLVED_INTERNAL_ONLY`;
- public or redistributed delivery is `STOP` until permission/license or an authorized exception is
  documented;
- replace with an original summary visual based on lawful source facts/data when possible, while
  preserving scientific attribution and transformation provenance.

This is operational rights hygiene, not legal advice; the responsible institution/rightsholder makes
the final determination.

## Accessibility contract

For every final deck:

- give each slide a unique programmatic title;
- add meaningful alt text to evidence-bearing images, charts, diagrams, and tables; mark decorative
  elements decorative;
- set a logical reading order and group complex visual elements when appropriate;
- do not encode group/status/uncertainty by color alone; add labels, symbols, line styles, or patterns;
- maintain sufficient contrast and readable type at the planned venue scale;
- use simple tables with headers when a table is necessary;
- caption or otherwise make embedded audio/video accessible;
- use descriptive hyperlinks rather than raw “click here” text;
- run the PowerPoint Accessibility Checker when the artifact and runtime support it, then manually
  inspect because automated checks do not establish complete accessibility.

### Alt-text pattern for a scientific visual

Describe the evidence and its point, not every decorative pixel:

`[Visual type] of [population/object and comparison]. [Axes/modality and key context]. [Main pattern
with uncertainty/qualification]. This supports [bounded slide message].`

For a radiology image, include modality/sequence or view, anatomy, orientation/laterality when
important, annotation meaning, and the relevant finding/limitation. Do not put identifiers or
unsupported diagnosis in alt text.

## Sources and rule provenance

- DICOM PS3.14, current, *Grayscale Standard Display Function*. Establishes the perceptual grayscale
  display function and ambient-light context; it does not certify a general presentation projector as
  diagnostic. https://dicom.nema.org/medical/dicom/current/output/chtml/part14/chapter_7.html
- DICOM PS3.15, current, *Attribute Confidentiality Profiles*. Establishes the de-identification
  profile, the responsibility to remove identifying information, and special handling of burned-in
  pixel information and overlays. https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html
- ACR, RSNA, and SIIM. *Protecting Patient Information in Online Medical Presentations*. Official
  joint guidance that in-application crops and black bars do not permanently remove PHI; source
  images should be safely captured or permanently cleaned before insertion, and the final package
  should be sanitized before public use. https://www.rsna.org/-/media/Files/RSNA/Practice-Tools/RemovingPHI.pdf
- ACR-AAPM-SIIM. *Technical Standard for Electronic Practice of Medical Imaging*. Supports the
  importance of luminance response, ambient lighting, and display-purpose distinctions. Apply the
  current standard and local qualified-physicist/institutional requirements when diagnostic display
  performance is in scope. https://cs.acr.org/-/media/ACR/Files/Practice-Parameters/Elec-Practice-MedImag.pdf
- Weissgerber TL, et al. *Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm*.
  PLOS Biology. 2015;13:e1002128. Supports displaying distributions/individual observations and
  preserving paired structure rather than relying only on summary bars for continuous data.
  https://doi.org/10.1371/journal.pbio.1002128
- Naegle KM. *Ten simple rules for effective presentation slides*. Supports splitting manuscript
  multipanels and explicitly introducing visual evidence. https://doi.org/10.1371/journal.pcbi.1009554
- Microsoft Support. *Make your PowerPoint presentations accessible to people with disabilities*.
  Official guidance for alt text, unique titles, logical reading order, contrast, non-color cues,
  accessible tables/media, and the Accessibility Checker.
  https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities
- Creative Commons. *Recommended practices for attribution*. Supports retaining Title, Author,
  Source, License and indicating adaptations for CC material. https://wiki.creativecommons.org/wiki/Best_practices_for_attribution
- U.S. Copyright Office. *How to Obtain Permission*. Supports treating license/permission as distinct
  from attribution and checking the intended use; local law and institutional policy may differ.
  https://www.copyright.gov/circs/m10.pdf
