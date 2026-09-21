# Three-branch routing and STOP gates

Use this reference before drafting whenever the study may cross human-subjects, animal-welfare or
biosafety/biosecurity governance. The goal is to identify the authorized decision owner and the
evidence needed before work or an assurance claim proceeds. It is not a substitute for local review.

## 1. Build an activity inventory

Classify the work actually planned or performed, not the project title. Record only the level of
detail necessary for governance routing:

| Activity class | Minimum facts to request from the author | Potential branch |
|---|---|---|
| human participants/data | interaction, identifiable data/images, records source, sites, dates, secondary use | human-subjects |
| human tissue/cells | source, identifiability, consent/waiver basis, intended analyses and sharing | human-subjects; add biosafety when material risk requires it |
| live animals | species/model, site, high-level intervention/imaging/tissue activities, protocol period | animal-welfare |
| genetic manipulation | host/system, high-level modification class, vector/material class, site | biosafety-biosecurity; add human or animal review according to the system |
| biological material | human/animal source, potentially infectious status, biological-agent/toxin class, transfer and site | biosafety-biosecurity; possibly human/animal review |
| release, transfer or cross-border movement | material/data category and destination, not procedural details | local biosafety, material-transfer, data/privacy and legal owners |
| potentially harmful misuse | whether methods, materials, data, models or results create a credible high-consequence misuse concern | institutional dual-use/biosecurity review |

`UNKNOWN` is a valid inventory value and usually creates `UNKNOWN_AUTHOR_INPUT_NEEDED`; it is never
evidence that a branch is not applicable.

## 2. Parallel-review map

| Project pattern | Reviews to test independently | Non-substitution rule |
|---|---|---|
| retrospective imaging with identifiable records | human-subjects + privacy/data governance | de-identification does not itself establish IRB exemption or waiver |
| human tissue with potentially infectious material | human-subjects + biosafety-biosecurity | consent/IRB does not assign containment or authorize laboratory work |
| genetically modified animal model | animal-welfare + biosafety-biosecurity | IACUC/equivalent approval does not replace IBC/equivalent review |
| prospective human gene-transfer study | human-subjects + biosafety-biosecurity + any current regulatory route | neither branch alone authorizes initiation |
| animal imaging using only an approved unmodified model | animal-welfare; test biosafety applicability locally | absence of a named hazard is not a self-issued biosafety exemption |
| computational life-science model or dataset with credible misuse potential | biosafety-biosecurity/dual-use route | “in silico” is not automatically outside biosecurity review |

Record the local office that decided `NOT_APPLICABLE`; do not infer non-applicability from generic
guidance.

## 3. Evidence sufficiency

For every applicable branch, capture:

- committee/office and responsible contact role;
- approval, registration or determination identifier;
- decision type and version;
- issue, start and expiry/continuing-review dates where applicable;
- approved sites, investigator, species/population, material and high-level activity scope;
- amendment/deviation/incident status;
- linked training, facility or veterinary/biosafety dependencies;
- exact document/page/section or authoritative local record;
- current-policy source and date checked.

These are author-only or institution-only facts. A manuscript sentence, an old protocol, a colleague's
practice or an external web page cannot replace the current local record.

## 4. Verdict logic

### PASS

Use only when the supplied evidence directly supports the described branch, dates, sites and scope.
State that this is an evidence-audit verdict, not a new approval.

### CONDITIONAL

Use for a planning or writing package when a non-authorizing item can be closed before execution or
submission—for example a missing document locator while the author reports a current approval. List
the owner and closure evidence. A `CONDITIONAL` verdict never authorizes work.

### STOP

Apply STOP to the affected activity or assurance claim when any of the following holds:

- an applicable committee/office decision is absent or its status is unknown;
- the record is expired, suspended or not current for the relevant period;
- species, population, site, investigator, material or activity falls outside documented scope;
- a change, deviation or incident requires local review and no closure is documented;
- required training, facility, veterinary or biosafety-owner confirmation is absent;
- records conflict with the Methods, grant, registry or submission declaration;
- dual-use/high-consequence risk is credible or unresolved and designated review has not cleared the
  design or communication plan;
- completed work appears to predate or exceed approval and the author requests wording that implies
  otherwise.

After STOP, provide only: the gap, why it matters, the responsible local owner, the record needed to
close it, safe non-operational questions and the claim/text that must be withheld. Do not propose a
workaround.

## 5. Live-policy verification

Jurisdiction and institutional policy can change. The following are **entry points**, not universal
rules and not evidence of local approval:

- US human-subjects oversight: <https://www.hhs.gov/ohrp/>
- US animal-welfare/IACUC overview: <https://olaw.nih.gov/node/135>
- US recombinant/synthetic nucleic-acid and IBC information: <https://osp.od.nih.gov/policies/biosafety-and-biosecurity-policy/>
- WHO risk-based laboratory biosafety guidance: <https://www.who.int/publications/i/item/9789240011434>

For every use, record `jurisdiction + institution + source/version + accessed date + local owner`.
Check the current authoritative page at the time of the project; do not rely on a policy name or
effective date copied from an older manuscript.

## 6. Safe output boundary

Allowed: applicability questions, committee routing, document/audit matrix, STOP verdict, high-level
risk categories, author placeholders, manuscript wording and responsible-communication handoff.

Not allowed: assigning a containment level by guess, specifying how to engineer or enhance a
pathogen/toxin, optimizing release or evasion, bypassing institutional review, or supplying detailed
procedures that enable a flagged hazardous activity. Route those decisions to the current local
biosafety/biosecurity owner.
