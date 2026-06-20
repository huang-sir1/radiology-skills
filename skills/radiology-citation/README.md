# radiology-citation

**Verified, imaging-journal-scoped citations → one clean reference file (RIS / EndNote /
BibTeX).** Verifies every identifier; never fabricates metadata.

## What it does
- Segments text into citable claims; finds candidates; **verifies DOI/PMID** before
  formatting.
- Scopes/ranks to imaging journals (Radiology, Radiology: AI, RadioGraphics, AJR, European
  Radiology, JACR, …) or broadens for methods/biology claims.
- Grades support (strong / partial / background / limiting).
- Exports a single reference-manager-ready file with verified fields only.

## Reference files
```
references/
├── radiology-journal-scope.md  imaging-journal scope + venue ranking
└── export-formats.md           RIS / ENW / BibTeX field mapping + integrity
```

## Example prompts
- "Find imaging-journal references for this Discussion paragraph and export RIS."
- "Verify these 12 DOIs and give me a clean BibTeX."

## Integrity
Drops/flags unresolved identifiers; never invents DOIs/pages/volumes. Retrieval is handed to
`radiology-search`.
