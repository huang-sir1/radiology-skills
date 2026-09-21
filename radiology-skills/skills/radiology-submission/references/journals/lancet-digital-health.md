# The Lancet Digital Health — submission profile

Snapshot checked: 2026-08-22. Scope: `Article`. The official author PDF is labelled August 2026.
An independent later request returned HTTP 403; the same-day extracted guide facts remain the routing
snapshot, but a future final audit must reacquire the official PDF or keep decisive items incomplete.

## Authoritative routes

- `TLDH-IFA`: [Information for Authors, August 2026](https://www.thelancet.com/pb-assets/Lancet/authors/tldh-info-for-authors.pdf)
- `TLDH-EM-DEV`: [Public Editorial Manager page](https://www.editorialmanager.com/tldigitalhealth) —
  currently says the site is under development and must not be used for a live submission; do not
  treat unauthenticated assumptions as captured fields.

## Route facts

- Single-anonymized review; author identity remains in the manuscript title page.
- Initial inventory includes covering letter; manuscript including tables/panels; figures; Research in
  context for all primary research; DOI and funding statements; relevant in-press papers plus
  acceptance letters; and trial protocol/reporting materials when applicable.
- The guide has an internal timing conflict for the signed author statement form: an initial checklist
  lists it, while later prose says Original Research forms are requested after peer review. Classify
  this timing `PORTAL_ONLY/UNVERIFIED`; do not invent an initial-upload hard failure.
- Article main text at most 3,500 words, or 4,500 for a randomised controlled trial; at most 30
  references. The five-part semi-structured abstract (Background, Methods, Findings, Interpretation,
  Funding) is at most 300 words.
- Research in context has Evidence before this study, Added value of this study and Implications of
  all the available evidence, with no references. Apply its detailed search-date/terms/selection and
  bias description rather than writing generic promotional prose.
- Every research Article includes a Data sharing statement. Activate current design reporting routes,
  including CONSORT 2025, CONSORT-AI/SPIRIT-AI, STARD, STROBE, STREGA or PRISMA as applicable.
- Supplementary material is one PDF with contents and page numbering. Image and media rules in the
  guide are format-specific and should be applied only to the corresponding files.
- Revision requires clean and highlighted manuscripts plus a detailed point-by-point response with
  the cover letter.
- Public guide confirms that the covering letter is entered under `Enter Comments` and the abstract
  is pasted under `Submit Abstract`; the remaining current portal fields require live capture.

## File and material gates

| Stage | Material | Class | Publicly verified format/status |
|---|---|---|---|
| initial | covering letter | portal-only | required content entered in portal `Enter Comments`; do not invent a local file |
| initial | manuscript including tables/panels | required | accepted manuscript extension not stated in public PDF; verify live |
| initial | figures | required/conditional | TIF/JPG ≥300 dpi for raster; editable Word/PPT for flowcharts; AI/EPS/vector PDF/PPT/Word/SVG for vector |
| initial | Research in context | required for primary research | manuscript section, no references |
| initial | author statement form | timing unresolved | guide conflict; exact working portal required for machine closure; decision letter is human-adjudicated |
| initial | trial protocol/checklists/SAP | conditional | trial/design branch |
| initial | Supplementary material | conditional | one PDF, contents and page numbers |
| revision | clean manuscript | required | extension needs exact working portal; decision letter is human-adjudicated |
| revision | highlighted manuscript | required | extension needs exact working portal; decision letter is human-adjudicated |
| revision | point-by-point response | required | accompanies cover letter; exact upload designation is portal-specific |

## Unverified current/portal gates

- Accepted main-manuscript extension, numeric display-item limit, author-form timing conflict, complete
  file designations and metadata fields. A guide/portal conflict keeps that item incomplete.

## Published exemplars — advisory only

- [Multicentre external-validation point-of-care ultrasound video AI study](https://www.sciencedirect.com/science/article/pii/S2589750024002498) (2025).
- [AI integration in breast screening across three countries](https://www.sciencedirect.com/science/article/pii/S2589750024001730) (2024).

The published PDF's section density and display strategy are descriptive, not accepted-file evidence.
