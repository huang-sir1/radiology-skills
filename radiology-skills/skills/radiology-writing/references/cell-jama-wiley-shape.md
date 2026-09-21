# Cell Press, JAMA Network and Advanced/Wiley writing routes

Use this router when the target is Cancer Cell, Cell Reports Medicine, JAMA Network Open or
Advanced Science. These are distinct editorial systems. Do not borrow the Nature-family shape merely
because a published article looks similar, and do not turn a published exemplar into a mandatory
section or file rule.

Current file/package requirements still come from `radiology-submission` and its exact-journal
profile. This reference controls argument and section planning only. Any volatile word, figure,
reference or file limit is `VERIFY_FROM_CURRENT_GUIDE` until the exact target guide is refreshed.

## Cell Press route: Cancer Cell and Cell Reports Medicine

Use a results-led biological/clinical argument:

`brief summary -> exact knowledge gap -> Results subsections that each resolve one question ->
Discussion with competing explanations and limits -> reproducible Methods/resources`

Before final release, open the exact target profile under
`radiology-submission/references/journals/`. Current validated profiles distinguish initial from
final submission and identify target-specific embedded components such as STAR Methods, key
resources, Highlights, graphical abstract and, for Cell Reports Medicine, the limitations section.
Do not assume that a component required by one Cell Press title is required by the other.

Writing rules:

- Begin Results with the biological or clinical question, not the software name.
- Keep donor/patient counts, cell/spot/ROI observations and generated layers visibly separate.
- Give each Results subheading a conclusion that the displayed evidence actually earns.
- In Discussion, test at least one serious biological and one sampling/technical alternative when a
  mechanism is claimed.
- Keep resource, method and availability statements traceable to actual artifacts; never fabricate a
  reagent, accession, code release or experiment to fill a house-style section.
- Draft embedded final-submission components only after the scientific packet is frozen. Their
  presence does not upgrade a `CONDITIONAL` or `STOP` mechanism claim.

If the public guide or live portal cannot establish the exact current shape, return
`VENUE_SHAPE_UNVERIFIED` plus a journal-neutral scientific spine and request the current exact guide;
do not substitute the Nature-family profile.

## JAMA Network Open route

Use a clinically readable IMRaD structure and the exact current
[Instructions for Authors](https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors)
for volatile limits. The front of the manuscript should support the journal's clinical decision
logic:

- **Key Points:** `Question`, `Findings`, `Meaning`; every finding and implication must trace to the
  same frozen Results evidence.
- **Structured abstract:** select the headings required by the actual study design and article type;
  state design, setting, participants/exposure or intervention, main outcome, quantitative results
  with uncertainty and a bounded conclusion.
- **Introduction:** clinical/scientific importance -> exact evidence gap -> objective or hypothesis.
- **Methods/Results:** mirror one another; make cohort flow, independent unit, missingness,
  prespecification, comparisons and sensitivity analyses visible.
- **Discussion:** principal findings -> relation to prior work -> limitations -> restrained
  conclusion. Do not convert prediction or observational association into treatment benefit.

The current upload guide, not this writing router, determines whether figures are embedded or
separate at each stage and which revision image subtype is accepted.

## Advanced Science / Wiley route

Use a broad interdisciplinary argument that remains readable outside radiology or the assay
subfield. Lead with the generalizable scientific advance, then make the method, evidence and boundary
explicit. Do not enforce a detailed house shape, word limit or submission component from memory.

If the exact current Advanced Science author guide is inaccessible or its public portal is a
development placeholder, keep the state `VENUE_SHAPE_UNVERIFIED`. Produce only:

1. a journal-neutral title/abstract and Results-first evidence spine;
2. an explicit list of shape questions to resolve from the current official guide/portal; and
3. a reversible section-allocation map so the manuscript can be conformed after verification.

Wiley's general transfer or author-services pages cannot create an Advanced Science-specific hard
writing or file rule.

## Output addition

For these routes, add:

`venue_route | exact profile checked | verified section elements | VERIFY_FROM_CURRENT_GUIDE |
scientific packet digest | Claim-ID drift ledger`

A completed prose draft is not a package audit. After manuscript, displays, declarations and
supplement stabilize, send the actual upload root to `radiology-submission`.
