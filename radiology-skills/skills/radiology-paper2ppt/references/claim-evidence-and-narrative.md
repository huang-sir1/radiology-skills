# Claim, evidence, and narrative contract

Use this reference after selecting the primary deck route. It governs what each slide may claim,
how slides form an argument, what belongs in speaker notes, and how duration changes scope.

## Build backward from the audience outcome

Write these four lines before a slide list:

1. `Audience:` the least specialized group that must follow the argument.
2. `Outcome:` the understanding, judgment, approval, decision, or action required.
3. `Central takeaway / decision basis:` one bounded sentence or, for exploratory work, one question.
4. `Decisive evidence:` the minimum observation(s) that can support that takeaway or decision.

Then design the close, decisive scene, and opening before filling the middle. This prevents a deck
from becoming a compressed manuscript or activity chronology.

## Slide claim contract

Every content slide gets one row in the slide map:

| Field | Contract |
|---|---|
| `narrative_job` | One job: orient, pose, explain, compare, show, qualify, decide, or transition |
| `message_title` | A sentence or bounded question/status that states what the audience should take from the slide |
| `claim_state` | `SOURCE_OBSERVED`, `ANALYSIS_DERIVED`, `INTERPRETATION`, `RECOMMENDATION`, or `PROPOSED` |
| `evidence` | The visible observation, image, chart, table slice, design fact, or documented status that supports the title |
| `qualifier` | Population, setting, comparison, time point, uncertainty, evidence maturity, and known caveat |
| `source` | Authoritative locator or project artifact; not merely the previous slide |
| `delivery` | Talk track, transition, timing, and anticipated question |
| `cut_status` | `CORE`, `CUT_FIRST`, or `BACKUP` |

If a row cannot be completed, the slide is not ready for layout. A visual theme cannot repair an
unsupported title.

## Assertion-evidence as a default, not a slogan

For a result, explanation, or argument slide:

1. Put the bounded message in a sentence headline.
2. Place the evidence that makes the statement credible in the main visual field.
3. Label only the evidence the audience needs to interpret the claim.
4. Move procedural narration and secondary detail to speaker notes or backup.

Examples of useful transformations:

| Topic label | Message title |
|---|---|
| `External validation` | `Performance fell at the wholly unseen centre` |
| `Cohort` | `Exclusions removed 38% of eligible examinations` |
| `Limitations` | `Protocol and site remain inseparable in the external cohort` |
| `Future work` | `A prospective reader study is required before workflow claims` |

Do not force a declarative result when the evidence is unresolved:

- `Why did ADC stability fall after the scanner upgrade?` is valid for a lab meeting.
- `The scanner upgrade caused ADC instability` is not valid without evidence isolating that cause.
- `We will test whether scanner upgrade explains the instability` is valid for proposed work.

Topic titles are acceptable for minimal title/agenda/section-divider slides, but a section label does
not count as a scientific message.

## Claim-state ladder

### `SOURCE_OBSERVED`

Report what a paper, protocol, dataset receipt, analysis output, or project record explicitly contains.
Keep source authorship visible: “The authors reported …” is not the presenter's endorsement.

### `ANALYSIS_DERIVED`

Use only when the value or plot is reproducibly derived from named frozen inputs and analysis. Record
the derivation and distinguish exploratory, interim, and final freezes.

### `INTERPRETATION`

State the reasoning link from observation to meaning. Make viable alternatives visible when they
would change the conclusion. Association, discrimination, prediction, and workflow agreement do not
become mechanism, causality, patient benefit, or deployment readiness through confident wording.

### `RECOMMENDATION`

Name the decision owner, alternatives, expected consequence, and residual uncertainty. A result can
inform a recommendation without logically proving it.

### `PROPOSED`

Use future tense. Separate prior evidence, preliminary evidence, simulation, design assumption, and
the result the study will seek. Never render a proposed workflow diagram as evidence that the
workflow already works.

## Evidence maturity labels

Put a short audience-facing label on slides where maturity could be misunderstood:

- `Proposed study`
- `Exploratory, not prespecified`
- `Interim; follow-up incomplete`
- `Frozen internal validation`
- `Untouched external evaluation`
- `External adaptation performed before evaluation`
- `Published result reported by source authors`

An all-deck footer is not required, but ambiguity is not allowed. If different curves/panels have
different maturity, label them individually.

## Scientific uncertainty language

### Visible slide

Show uncertainty where it changes interpretation:

- estimate plus interval rather than a naked performance number;
- distribution or individual observations when summary alone hides important variation;
- denominator and missingness when rates or exclusions matter;
- sensitivity or alternative explanation when the main inference depends on an assumption;
- explicit `not estimated`, `not collected`, or `not yet adjudicated` instead of a blank that looks zero.

### Spoken interpretation

Use calibrated verbs:

| Evidence | Suitable verb | Avoid without stronger evidence |
|---|---|---|
| observed association | associated, co-varied | caused, drove |
| diagnostic discrimination | distinguished in this cohort | diagnoses patients, improves outcomes |
| prediction in frozen validation | predicted under the stated task | generalizes everywhere |
| reader agreement | agreed under this protocol | is correct |
| exploratory imaging-omics link | suggests, motivates validation | reveals mechanism |
| implementation simulation | projects, estimates | demonstrates clinical benefit |

Do not hide every limitation in a final “limitations” slide. Place a decisive caveat with the evidence
it qualifies, then synthesize remaining limitations near the close.

## Narrative continuity

For each adjacent pair, complete: `Because slide N establishes ___, slide N+1 must answer ___`.
If no relationship exists, move, merge, delete, or explicitly transition the slide.

Useful arcs include:

- context -> tension -> question -> method -> evidence -> qualification -> implication;
- agreed plan -> current evidence -> variance -> cause -> options -> decision;
- field claim -> study design -> result -> alternative explanation -> defensible inference;
- review criterion -> proposal evidence -> risk -> mitigation -> requested approval.

An agenda is a navigation aid, not the narrative. Remove repeated previews, recaps, and generic
section summaries that consume time without changing audience understanding.

## Opening and close

### Opening

Within the first substantive scene, establish audience common ground, the problem/question, and why
this presentation is needed now. Avoid long field histories unless the audience needs them to judge
the contribution.

### Close

Resolve the opening according to deck job:

- proposal: why this study should proceed and the requested approval/feedback;
- lab meeting: the unresolved decision, proposed next test, and owner;
- conference: the bounded take-home contribution and implication;
- journal club: what the paper supports, does not support, and what the group should discuss;
- project review: intervention/decision and next evidence checkpoint;
- defense: answer to the thesis question and original contribution;
- results: observed result, interpretation, and decision/recommendation kept distinct.

Do not make a generic “Thank you” slide the scientific close. Contact/acknowledgment/Q&A may follow
after the conclusion remains visible or is readily recoverable.

## Speaker notes contract

Use speaker notes for delivery support. Recommended block per slide:

```text
[Talk track]
What to say in natural spoken language; do not read visible labels verbatim.

[Transition]
Why the next slide follows.

[Caveat]
One claim boundary or alternative explanation that must be spoken.

[Timing]
Target cumulative time or maximum duration for this scene.

[Anticipated question]
Question -> short answer -> backup slide or source.

[Sources]
- claim or asset -> authoritative URL/DOI/project artifact + exact locator
```

Rules:

- Notes may explain evidence but may not introduce a stronger unsupported conclusion.
- Do not expose production instructions, timing scaffolds, or talk tracks on audience-facing slides
  unless the user explicitly requests them.
- Mark speaker-only hypotheses, personal interpretation, unpublished data, and source-author claims.
- Add a `[Sources]` block for every externally sourced non-trivial claim and asset, even when a short
  visible citation is also present.
- For Q&A, point to backup evidence; do not invent an answer to fill a likely question.

## Timing and cut path

Do not impose a fixed slides-per-minute quota. Slide complexity, animation, image interpretation,
audience familiarity, and discussion style change pace. Use these controls instead:

1. Reserve Q&A and handoff time before allocating content time.
2. Give section-level budgets and a target cumulative time in notes.
3. Rehearse aloud in the actual delivery mode; silent reading is not a timing test.
4. Mark `CUT_FIRST` slides that can be skipped without breaking the logic.
5. Place deep technical evidence in `BACKUP`, linked from anticipated questions.
6. Shorten content before accelerating delivery or shrinking visuals.
7. Record `REHEARSAL_NOT_RUN` if rehearsal was not actually performed.

NIH guidance gives two minutes per supporting slide as an illustrative average, while other scientific
presentation guidance often uses approximately one idea/minute. Treat both as planning heuristics;
only timed rehearsal validates this deck for this speaker.

## Sources and rule provenance

- Garner JK, Alley MP. *How the Design of Presentation Slides Affects Audience Comprehension: A
  Case for the Assertion-Evidence Approach*. International Journal of Engineering Education.
  2013;29(6):1564-1579. Controlled presentation content while comparing slide structures; supports
  message headlines and relevant visual evidence, with context-specific limits.
  https://www.ijee.ie/articles/Vol29-6/23_ijee2791ns.pdf
- Naegle KM. *Ten simple rules for effective presentation slides*. PLOS Computational Biology.
  2021;17:e1009554. Supports one idea per slide, conclusion-bearing titles, splitting manuscript
  multipanels, and rehearsal-informed scope. https://doi.org/10.1371/journal.pcbi.1009554
- Bourne PE. *Ten Simple Rules for Making Good Oral Presentations*. PLOS Computational Biology.
  2007;3:e77. Supports audience-first scope, prioritization, rehearsal, and delivery bounded by the
  allotted time. https://doi.org/10.1371/journal.pcbi.0030077
- NIH Office of Dietary Supplements. *Scientifically Speaking: How to Prepare an Effective Talk*.
  Supports common ground, main question, anchor result, image interpretation, take-home synthesis,
  and finishing on time. https://ods.od.nih.gov/News/Scientifically_Speaking_How_to_Prepare_an_Effective_Talk.aspx
