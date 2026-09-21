# DICOM de-identification

Imaging cannot be shared until the complete release surface has been inventoried, transformed under
an authorised profile and verified. A clean image header does not establish that an accompanying
structured object, embedded document, display object or package artifact is clean.

## Three release surfaces of PHI

1. **DICOM object attributes** — patient name (0010,0010), ID (0010,0020), birth date
   (0010,0030), accession (0008,0050), institution (0008,0080), referring physician,
   study/series dates and times, device serial numbers, private attributes, and linkable UIDs.
   UIDs are not handled by a blanket “delete all” rule: some must be consistently replaced or
   retained under an authorised profile option to preserve DICOM conformance and references.
2. **Embedded/display payloads** — burned-in Pixel Data and overlay planes; Presentation State
   graphics/text; Structured Report Content Sequences; Acquisition Context and Specimen Preparation
   content; Encapsulated Documents such as PDF/CDA; secondary captures, video/multiframe objects,
   Waveform/audio-like payloads, thumbnails and any private or vendor payload that the selected
   de-identifier cannot parse. Head CT/MRI may also retain recognizable facial geometry.
3. **Package/container artifacts** — `DICOMDIR`, file-set labels, archive names, directory and file
   names, CSV/JSON/XML sidecars, conversion manifests, screenshots, thumbnails, export reports,
   exception files, application logs and QA/reviewer notes. These can disclose identity even when
   every DICOM Data Set passes an attribute scan.

Inventory the release at file and DICOM-object level. Record file path, media type, SOP Class UID,
Transfer Syntax UID, payload class, parent/reference links, frame/content count and intended
disposition. Unknown, unsupported or uninspected payloads are
`STOP_RELEASE_SURFACE_UNRESOLVED`; they are excluded or routed to a qualified content-specific
review rather than silently released.

## Standard & profile
- Use the **DICOM PS3.15 Basic Application Level Confidentiality Profile** with appropriate
  options. In addition to any authorised retention options, explicitly decide whether the release
  needs the Clean Pixel Data, Clean Recognizable Visual Features, Clean Graphics, Clean Structured
  Content and Clean Descriptors Options. Applying the Basic Profile alone does not clean every
  payload listed above.
- Encapsulated Document content is opaque to a generic DICOM attribute cleaner. Replace/exclude it
  as required by the selected profile, or use a documented content-specific cleaning and validation
  path; never infer that a PDF/CDA is safe because its enclosing DICOM attributes were cleaned.
- For unsupported Presentation State, SR, waveform, video or private/vendor payloads, fail closed
  until a parser/reviewer can account for their identifiable content and references.
- Appropriate retention options may include Retain Longitudinal Temporal with date **shifting** and
  Retain Patient Characteristics — keep only what research and governance require while removing
  identifiers.
- **Consistent date-shifting** per patient preserves intervals (important for longitudinal/
  follow-up) without real dates.
- Keep any **secure linkage key** separately under the authorised governance route, or destroy it
  only when the approved retention/destruction plan requires that action. Destroying the mapping key
  changes direct re-linkability but does **not** by itself establish legal or practical anonymity:
  recognizable anatomy, rare phenotypes, dates/geography, genomics, public records and cross-table
  linkage may retain re-identification risk. By default describe the output as de-identified under
  the named profile, or pseudonymized when a controlled re-linkage path remains. Use “anonymous” only
  after the applicable jurisdiction, threat model, data combination, residual-risk assessment and
  authorised governance determination support that term; route this determination to
  `radiology-ethics/references/reidentification-risk.md` rather than self-certifying it here.

## Apply profile action codes, not a blanket UID deletion

- Execute the selected PS3.15 profile attribute by attribute. Record the action codes used:
  `X` remove, `Z` zero length, `D` non-zero dummy value, `K` keep, `C` clean, and `U` replace
  with a non-zero UID that is internally consistent across the related set of instances.
- For `U`, use a collision-resistant mapping and preserve Study/Series/SOP/Frame-of-Reference and
  cross-object references consistently throughout the release. Validate the resulting Information
  Object Definitions and referential graph; independently replacing each UID or deleting required
  UIDs can corrupt the dataset.
- The **Retain UIDs Option** is a documented risk-benefit/governance choice, not a default shortcut.
  Original UIDs may enable linkage when an adversary has the source dataset. Retain them only when
  the selected profile option and data-use approval permit it.
- Set `Patient Identity Removed (0012,0062)` and record the de-identification method/profile and
  options using the applicable DICOM attributes. Do not let those declarations substitute for
  verification of the exported objects.

## Recognizable facial features: defacing is not skull stripping

- **Defacing** modifies or removes externally recognizable facial anatomy to reduce reconstruction
  and matching risk. **Skull stripping** segments/removes non-brain tissue for an analysis pipeline;
  it is not interchangeable with defacing and must not be treated as a privacy certificate.
- Neither operation guarantees anonymity or absence of recognizable features. Choose a method from
  the declared recipient/use/threat model, inspect the resulting facial surface or rendered volume,
  and retain a controlled-access or exclusion fallback when residual risk remains.
- Quantify task-specific measurement impact: verify that brain, head-and-neck, orbital, skull,
  scalp, PET attenuation, registration and other relevant ROIs/signals were not materially changed.
  A visually plausible output is not enough. Route the residual re-identification determination to
  `radiology-ethics/references/reidentification-risk.md` and the measurement-sensitivity decision to
  the active imaging/analysis owner.

## Tools
- **CTP (RSNA Clinical Trial Processor)**, **DICOM Library / dcm4che**, **pydicom** scripts,
  **TCIA's de-identification workflow** (if depositing to TCIA — follow their requirements),
  **gdcm**. Verify, don't trust defaults.

## Verification (mandatory)
- Freeze a closed release-surface manifest before QA. Reconcile its object/file counts and hashes
  against the archive actually released; unmanifested files, sidecars or logs fail the gate.
- Re-scan **every exported object's** attributes for residual identifiers and disallowed private
  attributes; audit each UID against the selected action (`U`, `K`, `X/Z/U*`, etc.) and verify
  cross-instance referential consistency.
- Apply payload-specific checks across the **entire release surface**: pixel/OCR/overlay review;
  Clean Graphics verification for display objects; Clean Structured Content verification for SR and
  related sequences; descriptor review; content-specific Encapsulated Document inspection; and an
  explicit rule for video, waveform, private and unknown payloads. Route every high-risk or
  indeterminate object to manual review or exclusion.
- Inspect package/container artifacts independently: archive, directory and file names; `DICOMDIR`;
  sidecars; thumbnails/screenshots; manifests; export/error logs; and QA notes. Do not publish the
  original identity linkage key, source paths or an exception log containing source identifiers.
- For a small release, manually review all human-viewable payloads; for a large release, a documented
  risk-based/statistical manual sample may supplement but must not replace full automated inventory,
  payload-appropriate coverage and targeted review.
- Record tool/version, rules, total object/frame coverage, flagged counts, reviewer disposition,
  excluded/unsupported payloads, package-artifact coverage, false-negative challenge set or
  validation evidence, and residual risk. A casual visual sample cannot support a “release is free
  of PHI” claim.
- Document the method + profile + tools in Methods (CLAIM/ethics).

## Checklist
`profile/options/action codes recorded? · direct/private identifiers removed or cleaned? · UIDs
replaced/retained/removed exactly as authorised and references remain consistent? · dates shifted
consistently? · all SOP Classes/payloads/package artifacts inventoried? · SR/PR/encapsulated
documents/video/waveform/private payloads explicitly handled? · all exported objects received the
applicable attribute/descriptor/structured/graphics/pixel checks? · every unknown/high-risk object
resolved or excluded? · archive names, sidecars, thumbnails and logs checked? · faces defaced where
required and separately distinguished from skull stripping? · task-specific measurement impact
checked? · linkage key handled per IRB? · released archive reconciled to its manifest? · coverage,
tool versions, exclusions, flags and residual risk documented?`

## Authoritative source

- DICOM Standards Committee. [DICOM PS3.15, current edition, Annex E: Attribute Confidentiality
  Profiles](https://dicom.nema.org/medical/dicom/current/output/html/part15.html). The standard is
  versioned; record the edition/date used and recheck the current edition before a live release.
