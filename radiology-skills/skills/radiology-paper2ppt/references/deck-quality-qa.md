# Presentation artifact routes and quality assurance

Read this reference only for a real presentation artifact or an audit/repair of an existing deck.
Load and follow the active presentation skill/tool before authoring because its runtime, template,
format, and verification contracts may change. This reference supplies the scientific handoff and QA
requirements; it does not replace the artifact builder.

## Select an artifact scope

Choose exactly one:

| Scope | Output | Presentation runtime |
|---|---|---|
| `PLAN_ONLY` | deck brief, slide map, notes plan, visual/source ledger, QA plan | not required |
| `CREATE` | new PPTX or requested native presentation plus receipts | required before authoring |
| `EDIT` | revised copy or explicitly authorized in-place edit plus receipts | required before mutation |
| `AUDIT` | evidence/layout/accessibility/package findings; no mutation unless separately requested | read/inspect/render capabilities only |

Do not convert `PLAN_ONLY` into file creation merely because a presentation tool is available. Do not
turn `AUDIT` into repair without user authorization. If an artifact was requested but the required
runtime is unavailable, report `ARTIFACT_RUNTIME_BLOCKED`; a content plan may be offered but is not
the requested presentation file.

## Select one visual route

The active presentation skill is authoritative. Preserve these boundaries:

1. **Existing deck or user-designated template/reference:** inspect all relevant slides and the
   master-layout-slide hierarchy; duplicate and edit inherited structures rather than flattening or
   mixing with an unrelated template. A deck supplied only as scientific source material is not
   automatically the visual design reference.
2. **Explicit visual direction without reference deck:** build to the stated brand, style, mood, and
   accessibility constraints without silently substituting a bundled design.
3. **No visual direction:** use the active presentation skill's template-selection/default route.
   Subject matter alone is not a visual-direction choice.
4. **Native Google Slides:** use the active Google Slides route; do not round-trip an existing native
   deck through PowerPoint unless requested.

For edits, preserve the source and export a copy unless the user explicitly requests and authorizes
in-place mutation. Template compliance does not authorize reuse of proprietary assets outside their
permitted context.

## Pre-authoring handoff gate

Do not begin layout until these are frozen:

- deck brief with communication job, audience, duration, evidence state, confidentiality/publicity,
  artifact scope, and claim ceiling;
- slide map with one supported message per slide/scene;
- source and transformation ledger for every external claim/asset;
- planned speaker notes, `[Sources]` blocks, timing, and cut/backup path;
- privacy/rights disposition for all medical images and external media;
- organizer, institution, sponsor, or thesis template rules and their exact version/date.

`STOP` when a decisive message lacks evidence, PHI remains unresolved, a public asset has unresolved
rights, or the source/template contract is contradictory.

## Authoring constraints

- Audience-facing copy serves the audience; keep production notes, timing scaffolds, and talk tracks
  in notes unless explicitly requested on-slide.
- Use one primary message and one main evidence composition per slide. Split before shrinking.
- Follow the active presentation skill's minimum font, title-wrap, layout, visual-source, and
  implementation requirements. User/organizer/template rules override defaults when they remain
  readable and accessible.
- Use images/charts/tables only under the transformation passport in
  `visual-evidence-and-radiology-images.md`.
- Honor the deck brief's artifact/evidence fidelity classes. Keep evidence-critical numbers, tables,
  equations, citations, and data graphics natively editable where source values are available; use
  only accurate source-linked crops for justified exceptions. Do not rasterize them for convenience.
- Do not use a generated image or text-to-image rendering as scientific evidence. Keep
  `MISSING — ...` and `UNVERIFIED — ...` states visibly legible rather than filling or hiding them.
- Put a `[Sources]` block in speaker notes for every external non-trivial claim and external asset.
- Build anticipated-question backup slides deliberately and exclude them from the timed core route.
- Do not use hidden slides as a place to retain PHI, unlicensed assets, stale contradictory results,
  or unapproved confidential content.

## Required QA passes

Report each pass separately. A failure in one pass cannot be converted into a global pass by success
in another.

### 1. Scientific and narrative QA

For every slide:

- message title agrees with the visible evidence, caption, notes, and source;
- claim state and evidence maturity are correct;
- population/cohort/site, denominator, comparison, endpoint/metric, units, time point, uncertainty,
  and reference standard remain consistent;
- proposed, exploratory, interim, frozen, adapted external, and published evidence are not conflated;
- visible caveats travel with the result they qualify;
- the transition advances the primary deck route;
- the close answers the opening without exceeding the claim ceiling.

Cross-deck checks:

- terminology, abbreviations, cohort names, metric direction, color semantics, laterality, and
  modality/sequence/view labels are consistent;
- no better-looking run, image, or subgroup replaces the prespecified/frozen result without labelling;
- main, backup, and notes do not contain mutually incompatible values or claims.

### 2. Radiology privacy and display QA

- Treat these as hard rules: **a PowerPoint crop is not permanent removal; black bars are not de-identification.**
- all inserted clinical assets were permanently de-identified before insertion or were safely
  captured without PHI;
- no PowerPoint crop, black bar, mask, same-color text, or off-canvas object is treated as removal;
- run the applicable permanent cropped/hidden-content removal, document inspection, and final
  sanitization before public delivery;
- inspect slides, notes, comments, hidden slides, embedded objects/media, thumbnails, filenames, and
  exported PDF for identifiers;
- modality/sequence or view, orientation/laterality, frame/slice context, display transform,
  annotation, and image-selection state are preserved where scientifically relevant;
- grayscale images are legible on the tested delivery path; otherwise report
  `DISPLAY_PATH_NOT_VERIFIED`;
- the deck is labelled/handled as scientific communication, not a diagnostic display.

### 3. Render and layout QA

1. Render every final slide from the final artifact, not a stale draft.
2. Inspect a contact sheet for narrative rhythm, visual consistency, repeated silhouettes, density,
   and abrupt section changes.
3. Inspect every slide individually at full size for:
   - unintended overlap, clipping, off-canvas content, broken connectors, or unresolved placeholders;
   - title/banner wrapping, truncated labels, font substitution, and unreadable body/captions;
   - image distortion, blur, bad crop, missing panel/axis/legend/scale bar/number-at-risk;
   - source labels, footers, slide numbers, and color/line/marker consistency;
   - chart/table values and labels matching the source ledger.
4. Fix all unintended overlaps and clipping. Do not dismiss automated overlap warnings without visual
   inspection and a documented intentional-overlap decision.
5. Re-render after every layout repair and inspect the affected slides plus representative neighbors.

Programmatic package checks alone do not detect visual collisions; a contact sheet alone does not
establish full-size legibility.

### 4. Accessibility QA

Run executable checks where supported, and keep the results distinct:

- **PowerPoint Accessibility Checker:** run on the final artifact when Microsoft PowerPoint is
  available; resolve errors/warnings relevant to the delivery or document justified exceptions.
- **Unique descriptive titles:** verify every slide has a unique programmatic title, including a
  hidden title where the visual design intentionally omits visible title text.
- **Alt text:** verify every evidence-bearing image/chart/diagram/table has meaningful reviewed alt
  text; decorative elements are marked decorative. Reject unreviewed auto-generated descriptions.
- **Reading order:** inspect the final object order in the Reading Order pane or equivalent and ensure
  it follows the intended narrative. Group complex elements when appropriate.
- **Non-color encoding and contrast:** inspect color-deficiency/grayscale behavior and text/background
  contrast; labels, line styles, shapes, or patterns carry meaning in addition to color.
- **Tables/media/links:** use simple header-bearing tables; captions/subtitles or equivalent for
  audio/video; descriptive link text.

Automated Accessibility Checker success is not a complete accessibility certificate. If PowerPoint
or the checker was unavailable, report `ACCESSIBILITY_CHECKER_NOT_RUN` while still performing and
reporting manual/programmatic checks that were possible.

### 5. Package and provenance QA

Reopen/inspect the final package and verify:

- file opens; slide count and order match the slide map;
- notes exist where required and every external claim/asset has a `[Sources]` block;
- embedded images/media/fonts/links resolve as intended;
- hidden/backup slides are inventoried and safe;
- no comments, revisions, document properties, cached crops, hidden data, or temp paths leak private
  or irrelevant information;
- source/transformation ledger matches the final asset set;
- the final output path and filename are the ones actually inspected.

### 6. Editable PPTX parity and round-trip QA

Run this gate whenever an editable PPTX is delivered. Reopen the final saved PPTX, create a fresh
render/export from that reopened package, and compare it with the approved slide map, source ledger,
and previously inspected render. Verify at minimum:

- slide count/order, message titles, upstream Claim IDs, notes, and source blocks are unchanged;
- evidence-critical numbers, table cells, equations, axis/legend labels, citations, image crops, and
  qualifiers remain complete and correct;
- objects promised as native editable remain native text, tables, charts, equations, or vectors;
- approved source crops remain the correct assets at usable resolution and are not silently replaced;
- no font substitution, reflow, clipping, broken links/media, missing alt text, or changed reading
  order alters meaning after save/reopen/export.

Use the same application/runtime for the minimum save-reopen-render check. When a second supported
editor or the actual delivery machine is available, test there too and report which path was used;
do not claim cross-application parity when it was not tested. A mismatch in decisive evidence is
`STOP`. If the required runtime cannot perform the check, report `EDITABLE_PPTX_PARITY_NOT_RUN` and
do not call the artifact fully verified.

### 7. Rehearsal and delivery QA

- rehearse aloud in the intended delivery mode against the actual time limit;
- record total time, section cumulative times, Q&A reserve, and whether the cut path was tested;
- verify animations, videos, fonts, links, presenter view, click order, and remote sharing on the
  intended machine/path when applicable;
- test the decisive radiology images on the target display path when feasible;
- confirm backup-slide navigation and return path;
- if the actual speaker did not rehearse, report `REHEARSAL_NOT_RUN`; model-estimated timing is not a
  rehearsal receipt.

## QA receipt

Use `PASS`, `CONDITIONAL`, `STOP`, or `NOT_RUN` independently:

| Gate | Status | Evidence inspected | Remaining issue / owner |
|---|---|---|---|
| Scientific/narrative | ... | slide map + final slides + sources | ... |
| Privacy/rights | ... | source assets + final package + export | ... |
| Radiology display | ... | rendered/exported/target path | ... |
| Render/layout | ... | all slide renders + contact sheet | ... |
| Accessibility | ... | checker/manual title-alt-order-contrast checks | ... |
| Package/provenance | ... | reopened final artifact | ... |
| Editable PPTX parity/round-trip | ... | reopened PPTX + fresh render/export + slide map | ... |
| Timed rehearsal | ... | rehearsal run/record | ... |

Do not issue a single global `PASS` when any required gate is `STOP` or `NOT_RUN`. State exact scope,
for example: `Render/layout PASS; Accessibility Checker NOT_RUN; manual title/alt/order checks PASS;
timed rehearsal NOT_RUN.`

## Sources and rule provenance

- Microsoft Support. *Make your PowerPoint presentations accessible to people with disabilities*.
  Official operational checks for Accessibility Checker, alt text, unique titles, logical reading
  order, contrast, non-color cues, tables, and media.
  https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities
- ACR, RSNA, and SIIM. *Protecting Patient Information in Online Medical Presentations*. Establishes
  that presentation-software crops/black bars are not permanent de-identification and recommends
  safe source capture plus final sanitization. https://www.rsna.org/-/media/Files/RSNA/Practice-Tools/RemovingPHI.pdf
- RSNA. *Faculty and presenter resources*. Organizer-specific templates, upload, and scientific
  presentation requirements must be checked for the applicable year/type.
  https://www.rsna.org/annual-meeting/attendee-resources/faculty-and-presenter-resources
- Naegle KM. *Ten simple rules for effective presentation slides*. Supports one idea/slide,
  conclusion-oriented titles, graphics, and rehearsal-linked scope.
  https://doi.org/10.1371/journal.pcbi.1009554
