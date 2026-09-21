# Animal-welfare and protocol-scope review

Use this reference for live-animal imaging, intervention, breeding, longitudinal monitoring or tissue
collection. `IACUC` is a US term; elsewhere use the current animal ethics committee or equivalent.
Local rules may cover species or activities differently, so the named institutional owner decides
applicability.

## 1. Author-supplied facts

Request and evidence-anchor the following without guessing:

- committee/equivalent name, protocol identifier, decision and relevant dates;
- institution/site, responsible investigator and veterinary contact role;
- species/model, source and approved number or range;
- sex, age/life stage and inclusion logic when relevant to welfare or interpretation;
- high-level procedures, imaging/anesthesia category, interventions and tissue collection covered by
  the protocol;
- expected severity/burden category where the local system uses one;
- refinement measures, analgesia/anesthesia plan, monitoring and humane endpoints as approved;
- approved euthanasia method and trained personnel, stated only from the protocol/local SOP;
- housing, transport, acclimation and special-care dependencies where material;
- 3Rs rationale: replacement, reduction and refinement;
- amendments, unexpected outcomes/adverse events, deviations and required reporting/closure;
- reporting framework used, while recognizing that a reporting checklist does not grant approval.

Do not reproduce a detailed animal procedure or veterinary prescription. Link the controlled local SOP
and owner instead.

## 2. Review questions

| Domain | Question | Evidence required | STOP example |
|---|---|---|---|
| applicability | did the authorized local owner determine that animal review applies or not? | committee/office determination | project self-declares exemption |
| scope | do species, site, investigator and all high-level activities match the current protocol? | approval + relevant protocol/amendment section | model or activity is absent from scope |
| period | does approval cover the actual planned/performed dates? | issue/expiry/continuing-review record | work occurred outside the approved period |
| 3Rs | are alternatives, minimum decision-bearing use and refinements documented? | protocol rationale and committee record | avoidable duplication or burden remains unresolved |
| welfare | are monitoring, humane endpoints and veterinary escalation defined locally? | approved protocol/SOP and owner | no approved endpoint or veterinary path |
| competence | are the facility and personnel approved/trained for the covered work? | current local record | unconfirmed facility or training dependency |
| change control | were amendments, deviations and unexpected outcomes handled as required? | amendment/incident record | unreviewed material change or unresolved event |

Scientific randomization, blinding and independently assigned experimental units remain part of
`radiology-experiment-design`; they do not replace welfare review. Conversely, animal approval does
not establish scientific validity.

## 3. Constructive learner guidance

For a learner, return three levels without inventing a protocol:

- **minimum governance route:** identify the local animal ethics/veterinary owner, submit the exact
  model and activity scope, and do not start before the required current decision;
- **stronger route:** align the approved protocol, preregistered design, training records, welfare
  monitoring, adverse-event log and manuscript denominators;
- **resource-limited route:** reduce scientific breadth or defer animal work; do not remove required
  welfare safeguards or conduct work under an unrelated approval.

Explain which scientific question can still be answered if animal work cannot proceed.

## 4. Writing package

Use placeholders until records are supplied:

```text
All animal procedures were reviewed and approved by [IACUC / animal ethics committee / equivalent
full name] at [institution] (protocol [AUTHOR_INPUT_NEEDED], approved [date], valid for the reported
study period). The approved protocol covered [species/model, site and high-level activity scope].
Animal care, monitoring and humane endpoints followed [author-confirmed current institutional or
jurisdictional framework].
```

Report only verified facts relevant to reproducibility and welfare: model/source, biological unit,
allocation/blinding where used, attrition, welfare-related exclusions, adverse events and humane
endpoint implementation. Do not state “all guidelines were followed” without naming the supported
framework and evidence.

For a documented local exemption/non-applicability determination, identify the deciding authority and
record; never write “ethical approval was not required” solely from the study description.

## 5. Cross-branch handoff

- Genetic manipulation, vectors, potentially infectious challenge/material or modified organisms ->
  test `biosafety-biosecurity` in parallel.
- Human-derived material used in an animal model -> test `human-subjects` source/consent governance
  and biosafety applicability in parallel.
- Experimental controls, endpoints, sample size and analysis -> `radiology-experiment-design` and
  `radiology-stats` after governance gates are identified.
