# Slide map, source ledger, and delivery plan

Create the slide map before artifact layout. Add rows rather than compressing multiple claims into one
row. Use stable slide/scene and asset identifiers through all revisions.

## Slide map

| ID | Upstream Claim ID | Narrative job | Message title/question | Claim state | Visible evidence/visual | Evidence-carrier fidelity | Qualifier/uncertainty | Source key | Notes/transition | Target cumulative time | Status |
|---|---|---|---|---|---|---|---|---|---|---:|---|
| S01 | CLM-... | ... | ... | `SOURCE_OBSERVED / ANALYSIS_DERIVED / INTERPRETATION / RECOMMENDATION / PROPOSED` | ... | `NATIVE_EDITABLE / ACCURATE_SOURCE_CROP / GENERATED_ILLUSTRATION_NOT_EVIDENCE / MISSING / UNVERIFIED` | ... | SRC-... | ... | ... | `CORE / CUT_FIRST / BACKUP` |

Use `MISSING — [required item]` or `UNVERIFIED — [required check]` visibly on the slide when an
unresolved dependency is retained. A decisive missing source or value remains a pre-authoring
`STOP`; the placeholder records the blocker but does not waive it.

## Source and transformation ledger

| Source key | Claim/asset | Authority and exact locator | Evidence maturity | Rights/permission | Transformation | Reconciliation | Final slide(s) |
|---|---|---|---|---|---|---|---|
| SRC-001 | ... | DOI/URL/artifact version + page/figure/panel/table/cell | ... | ... | crop/redraw/annotate/none | checked by/date or `NOT_RUN` | S... |

For Creative Commons assets, retain supplied Title, Author, Source, License and indicate changes. For
medical images, link the image passport and de-identification receipt; do not copy PHI into this table.

## Radiology image passport

| Asset ID | Object + modality | Sequence/phase/view | Orientation/laterality + frame/slice | Display mapping | Annotation/reference | Selection state | De-identification | Transform | Rights |
|---|---|---|---|---|---|---|---|---|---|
| IMG-001 | ... | ... | ... | window/level, color map, fusion | ... | representative/prespecified/error case | receipt/status | ... | ... |

## Speaker-note block per core slide

```text
[Talk track]

[Transition]

[Caveat]

[Timing]

[Anticipated question]

[Sources]
- SRC-...
```

## Q&A and cut map

| Trigger/question | Core answer | Backup slide/source | Return slide | If time is short |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Final receipts

| Gate | Status (`PASS / CONDITIONAL / STOP / NOT_RUN`) | Evidence inspected | Remaining issue/owner |
|---|---|---|---|
| Scientific/narrative | ... | ... | ... |
| Privacy/rights | ... | ... | ... |
| Radiology display | ... | ... | ... |
| Render/layout | ... | ... | ... |
| Accessibility Checker | ... | ... | ... |
| Manual title/alt text/reading order/contrast | ... | ... | ... |
| Package/provenance | ... | ... | ... |
| Editable PPTX parity/round-trip | ... | reopened PPTX + fresh render/export + slide map | ... |
| Timed rehearsal | ... | ... | ... |
