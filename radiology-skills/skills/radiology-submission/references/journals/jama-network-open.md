# JAMA Network Open — submission profile

Snapshot checked: 2026-08-22. Scope: `Original Investigation`. The official page states `Last
Updated: August 17, 2026`.

## Authoritative routes

- `JNO-IFA`: [Instructions for Authors](https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors)
- `JNO-PORTAL`: [Manuscript Submission System](https://manuscripts.jamanetworkopen.com) — capture
  current fields from the actual submission.

## Route facts

- Single-anonymized review; the title page is the first page of the identified main manuscript.
- Main manuscript must be Word, not PDF, with 10–12 point type, double spacing and ragged right. One
  file contains title page, Key Points, abstract, main text, references, legends and tables, with each
  major part starting on a new page. Tables are editable, at the end and not uploaded as images.
- Research title is at most 100 characters. Title page includes authors/degrees/affiliations,
  corresponding-author details and main-text word count.
- Cover letter is recommended, not universally required. It identifies the corresponding author and
  related, overlapping, simultaneous or preprint material.
- Key Points use Question, Findings and Meaning in 75–100 words total. Structured abstract is at most
  350 words and follows the applicable JAMA headings.
- Original Investigation main text is at most 3,000 words; figures plus tables normally at most five;
  references generally 50–75 depending on design.
- Initial figures may be at the main-file end for review or separately uploaded. Do not reject one
  route merely because the guide also documents the other. At revision, each main figure is a
  separate file and its accepted extension follows its *figure type*: graph/plot
  (`AI/EMF/EPS/PDF/WMF/XLS`), flow diagram (`AI/DOCX/EMF/EPS/PDF`), illustration
  (`AI/EPS/JPG/PDF/PSD/TIF`), photograph/clinical image (`EPS/JPG/PSD/TIF`) or line drawing
  (`JPG/PSD/TIF`). Never union these lists into one permissive format rule for every figure.
- A photograph, clinical image, photomicrograph, gel or similar figure containing labels, arrows or
  other markers needs two versions: one with and one without markers. Initial and revision routes use
  separate pair-assertion rules so their figure-type formats are not conflated. The assertion binds
  `marked_item_id`/`unmarked_item_id` and both SHA-256 values under one `figure_pair_id`; a human must
  still verify that image content differs only by the intended markers.
- Supplementary text/eMethods/eTables/eFigures form one numbered Word file with a cover-page contents
  list and manuscript callouts. Spreadsheet-suitable data can be one Excel workbook whose first sheet
  is contents. Protocol and SAP are required as supplement for randomized and nonrandomized trials.
- All research manuscripts need a Data Sharing Statement and the journal's full-data-access and
  responsibility statement naming responsible authors. Reporting route follows declared Study Type.
- Disclose writing-assistance AI in Acknowledgment with tool/platform, version, manufacturer, use date,
  location and purpose. Research use of AI belongs in Methods. Identifiable patient material requires
  the appropriate permission; simple eye masking is not a substitute.

## Stage material matrix

| Stage | Material | Class | Publicly verified format/status |
|---|---|---|---|
| initial | complete main manuscript | required | Word; PDF not accepted as main manuscript |
| initial | cover letter | optional/recommended | do not create a missing-file hard error |
| initial | figures | conditional | embedded at end or separate; use current figure-type branch |
| initial | marked/unmarked image-pair assertion | conditional when labels/arrows/markers exist | path-free receipt cross-links the two separate initial photo files; human equivalence review required |
| initial | supplement | conditional | one Word file; one Excel workbook for spreadsheet-suitable data |
| initial | protocol and SAP | conditional | randomized/nonrandomized clinical trial |
| initial | reporting checklist | conditional | Study Type/EQUATOR branch |
| revision | graph or statistical plot | conditional by figure type | separate AI/EMF/EPS/PDF/WMF/XLS |
| revision | flow diagram | conditional by figure type | separate AI/DOCX/EMF/EPS/PDF |
| revision | illustration | conditional by figure type | separate AI/EPS/JPG/PDF/PSD/TIF |
| revision | photograph or clinical image | conditional by figure type | separate EPS/JPG/PSD/TIF |
| revision | line drawing | conditional by figure type | separate JPG/PSD/TIF |
| revision | marked/unmarked image-pair assertion | conditional when labels/arrows/markers exist | path-free receipt cross-links the two separate revision photo files; human equivalence review required |
| revision | response/clean/marked files | unresolved | exact live portal required for machine closure; decision letter is human-adjudicated |

## Portal-only checks

- Coauthor names/emails/affiliations, Study Type, funding/award, registration, data-sharing questionnaire,
  related manuscripts and system-sent Authorship Forms. Prior peer-review/editorial-comments upload is
  encouraged, not universally mandatory.

## Published exemplars — advisory only

- [AI Workflow, External Validation, and Development in Eye Disease Diagnosis](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2836426) (2025).
- [Efficiency and Quality of Generative AI–Assisted Radiograph Reporting](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2834943) (2025).

Published Key Points and declarations can guide house-style review, but not initial file mechanics.
