# Text, data, code, image and publication-record provenance

Use this reference for a source-to-output audit. Provenance gaps, analytical errors and inappropriate
transformations can make a result unreliable without establishing why the problem occurred.

## 1. Common provenance graph

Bind each claim-bearing output to:

`source artifact and version -> authorized transformation/code/config -> derived artifact -> value,
panel or sentence -> Claim ID -> proposal/manuscript/deck/repository/publication version`.

Record hashes or immutable identifiers when available. A screenshot, copied spreadsheet cell,
visible notebook output or pasted figure is not a complete source record.

## 2. Text and citation provenance

- Map quotations, close paraphrases, reused methods text and translated passages to exact sources and
  permissions where needed.
- Distinguish common methods language from unattributed appropriation; similarity software supplies
  candidates, not a plagiarism finding.
- Check preprint, conference abstract, thesis, registry and version-of-record overlap. Transparent
  prior dissemination is not automatically redundant publication.
- Preserve cited correction, expression-of-concern and retraction status through
  `radiology-citation`; do not silently cite a superseded version.

## 3. Data, code and statistical provenance

- Reconcile patient/exam/lesion/specimen IDs, cohort flow, exclusions, frozen splits and source-result
  values. Inspect only authorized de-identified records.
- Bind code commit/archive, environment, command, config, seed, input manifest, output and test-access
  events. A rerun that differs is an observation requiring diagnosis, not proof of fabrication.
- Distinguish data cleaning, error correction, imputation, harmonization and exclusion. Record who,
  when, rule, scope, before/after counts and whether outcomes were visible.
- Preserve negative, failed and superseded runs when they influenced selection or claims.

## 4. Radiology image-integrity passport

For every questioned panel record:

`source DICOM/derived object | patient-safe research ID | modality/sequence/view/phase | laterality |
slice/frame | window/level or intensity mapping | crop/resample/rotate/flip | annotation/overlay |
composite boundary | enhancement/denoise/AI generation or editing | operator/software/version |
source-to-panel locator | caption disclosure | original preserved`.

Permissible display processing depends on purpose and venue. Routine windowing, cropping,
resampling, annotation or global adjustment is not automatically improper when it preserves meaning,
is applied consistently, is traceable and is disclosed as needed. Treat these as integrity signals:

- undocumented deletion, duplication, splicing or replacement of anatomy;
- inconsistent processing that changes group comparison or lesion visibility;
- left/right flip or laterality mismatch without a declared display convention;
- choosing a favorable slice/phase/ROI while implying prespecified or representative selection;
- synthetic, reconstructed, enhanced or AI-edited content shown as an acquired clinical image;
- burned-in PHI or hidden provenance; or
- loss of the original/source mapping.

Visual similarity, metadata absence or automated image-forensics output alone cannot establish
manipulation or intent. Preserve originals and route material signals for independent review.

## 5. Correction and retraction pathway

Build a publication-state map: protocol/registry, abstract, preprint, accepted manuscript, version of
record, repository, correction, expression of concern, retraction and replacement. For each, record
issuer, date, DOI/version, affected claims and links.

Use publisher records as primary evidence and Crossmark as a corroborating update channel when
available. A missing Crossmark update, a green/unchanged landing page, or one database's silence is
not a clean certificate; reconcile DOI/version identity and inspect the publisher record before
asserting current publication state.

The skill may propose factual options:

- local artifact correction before dissemination;
- transparent manuscript/repository correction;
- institution/publisher notification for a material public-record issue;
- publisher-controlled correction, retraction, replacement or expression of concern.

It must not issue, demand or predict an editorial action. Prepare an evidence packet that distinguishes
honest error, unresolved integrity signal, attributed allegation and institutional finding.
