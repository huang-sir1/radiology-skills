# Human-subjects ethics approval & informed consent

Match the consent model to the design; report the approval honestly with author-supplied facts.
`IRB` and `ethics committee` are examples, not universal names. Applicability, exemption, waiver,
approval type and continuing-review requirements must be confirmed under the current jurisdictional
and institutional process. Do not self-declare that retrospective, public, de-identified or secondary
data fall outside review.

## Study-type → consent model

| Design | Typical consent model | What to state |
|---|---|---|
| **Retrospective, existing data** | Often a **documented waiver** of informed consent | The committee granted a waiver; the basis (minimal risk, impracticable to obtain, de-identified) |
| **Prospective** | Usually informed consent; exceptions require the actual authorized determination | The consent process, who consented, language/version, or the exact applicable exception |
| **Registered trial** | Consent + trial registration | Registry + ID; SPIRIT/CONSORT context (→ radiology-reporting) |
| **Multi-center** | Approval at each site or a recognised lead-site/central IRB | Which model; per-center numbers or the central approval |
| **Secondary use of public data** | Source consent/DUA plus the secondary investigator's applicable local determination | Cite source governance and the actual local approval, exemption or non-human-subjects determination; public availability alone establishes none of these |

## Match the statement to the actual decision type

First distinguish `APPROVED`, `EXEMPT_DETERMINATION`, `NOT_HUMAN_SUBJECTS_DETERMINATION`
and `UNKNOWN`. These are recorded decision types, not permissions issued by this skill.

- For approved human research, name the approving body, actual identifier/date where issued,
  approved scope and consent status. Separate waiver of consent from waiver of written
  documentation; one does not imply the other.
- For an exemption or a determination that the activity does not involve human subjects under the
  applicable framework, name the responsible local authority, exact decision type, scope, date and
  identifier if issued. Report `NOT_ISSUED` if the record has no identifier; do not invent a study
  approval number, consent waiver or approving committee.
- For multicentre work, report the actual local or central/reliance model and coverage. A valid
  central/reliance arrangement need not have separate local approval numbers at every site.
- Report source-dataset governance, secondary-use restrictions and privacy controls separately.
  Original dataset approval does not automatically cover every downstream use.
- For applicable human research, report Helsinki adherence only if supported by the actual conduct
  and relevant record. Do not insert it as a substitute for the applicable decision.

An absent required determination remains `UNKNOWN_AUTHOR_INPUT_NEEDED`; a documented exemption or
non-human-subjects decision must not be treated as a missing approval merely because its number or
wording differs from an approved-study template.

## Placeholders (never fabricate)

Choose a template only after the decision type is verified. For approved research, use explicit
placeholders the author fills, e.g.:

```
This [retrospective] study was approved by the [Institutional Review Board / Ethics Committee
of <institution>] (approval no. [XXX], [date]). [Written informed consent was obtained from all
participants. / The requirement for informed consent was waived by the committee owing to the
[retrospective, minimal-risk] design and the use of de-identified data.]
```

For a documented determination, use the record's exact term:

```
The [authorized local body] determined that [the defined secondary-use activity] was
[exempt under the stated framework / not human-subjects research under the stated framework]
([determination identifier, if issued], [date]). The analysis used [source/version] under
[documented access and reuse conditions].
```

Do not describe this determination as full approval or a consent waiver unless the record says so.

## Multi-center wording

*"The study was approved by the ethics committee of the lead institution ([name], no. [XXX]) and
by the local committees of each participating center; the requirement for informed consent was
waived at all sites given the retrospective design."* (Confirm the actual model per site.)

## Common problems

- Stating "consent obtained" for a retrospective registry where a waiver actually applied (or
  vice versa) — must match reality.
- Omitting a site's actual approval or documented central/reliance coverage.
- Claiming Helsinki adherence without a supported applicable governance determination or conduct.
- Approval number/date invented to fill the template — never do this; flag as 待确认.

## Human-subjects STOP gate

Return `STOP` for the affected activity or assurance wording when the responsible local decision is
missing, expired, conflicting, outside the population/site/data/tissue/activity scope, or when consent/
waiver and intended use or sharing disagree. Work already performed outside documented authority
cannot be repaired by retrospective wording; route it to the institution. Use
[ethics-routing-and-stop-gates.md](ethics-routing-and-stop-gates.md) when animal or biosafety review
may also apply.

## Primary scope reference

[OHRP, Coded Private Information or Biospecimens Used in Research (2018)](https://www.hhs.gov/ohrp/coded-private-information-or-biospecimens-used-research.html)
(accessed 2026-09-04) distinguishes secondary research that does not involve human subjects from
exempt human-subjects research under the US HHS framework. This distinction illustrates why the
actual decision type controls wording; it is not a declaration that another jurisdiction or local
institution follows the same rules.
