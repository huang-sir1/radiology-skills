# Scientific deck routing

Read this reference before choosing a narrative. Route by the audience's job, not by the source
document's section order. Select one primary route; list any secondary module explicitly.

## Three routing axes

### Axis 1 — audience outcome

| Audience outcome | Typical route |
|---|---|
| Approve, fund, or authorize a future study | Proposal defense |
| Diagnose an unfinished study and choose the next experiment | Lab meeting |
| Understand one mature contribution within a fixed time | Conference talk |
| Critically appraise an external paper | Journal club |
| Decide whether a project is on course and what intervention is needed | Project review |
| Judge the candidate's defensible original contribution | Thesis/defense |
| Interpret a result set and make a scientific or operational decision | Results deck |

If the user's label conflicts with the requested outcome, route by outcome and mention the mismatch.
For example, a “lab meeting” whose real purpose is a go/no-go milestone decision uses the project-
review route with a lab-meeting discussion module.

### Axis 2 — audience distance

Record the most distant audience that must understand the deck:

- **Same-method specialists** may receive technical abbreviations after one definition.
- **Clinical-domain peers** need the imaging/analysis method translated into clinical consequences.
- **Mixed scientific committee** needs construct, comparator, design, uncertainty, and feasibility
  made explicit; do not rely on local laboratory shorthand.
- **Decision makers or public audience** need stakes and decision consequences without loss of
  uncertainty. Do not replace evidence with promotional language.

The most distant required audience controls first-use definitions and visible context. Technical
detail can move to backup rather than disappear.

### Axis 3 — evidence maturity

| State | What may be shown | Default claim ceiling |
|---|---|---|
| `PLANNED` | rationale, aims, design, assumptions, simulations, prior work | “We propose / will test”; no study result |
| `EXPLORATORY` | provisional analyses with known flexibility | “In this exploratory analysis”; no confirmation or transport claim |
| `INTERIM` | prespecified or frozen partial analysis with incomplete follow-up/enrolment | bounded interim statement; no final efficacy or generalizability claim |
| `FROZEN_INTERNAL` | completed analysis under a frozen plan in represented data | internal result; external performance and clinical utility remain unproven |
| `EXTERNALLY_VALIDATED` | untouched or correctly labelled adapted external evaluation | claim only for represented task, setting, and validation state |
| `PUBLISHED` | source-author claims and reported evidence | faithful report of the publication, not automatic endorsement |
| `MIXED` | several states in one deck | label each claim/slide; the weakest relevant state limits synthesis |

Unpublished does not mean weak, and published does not mean true. Maturity describes what has been
done and frozen, not evidence quality.

## Route 1 — proposal defense or research pitch

**Job:** allow a committee to judge why the proposed research matters and whether it can be done
rigorously by this team under the stated constraints.

**Required upstream artifact:** frozen proposal/grant handoff from `radiology-grant`, including the
exact sponsor/call, review rubric, aims, approach, preliminary evidence, budget/time/resource
constraints, unresolved risks, and claim boundaries. If those are not frozen, stop and return the
content problem to `radiology-grant`.

**Arc:**

1. decision and sponsor-specific review frame
2. important unmet problem and current evidence gap
3. central objective/hypothesis and why now
4. specific aims with non-overlapping success conditions
5. approach mapped to each aim: population/data, imaging chain, reference standard, analysis,
   validation, statistics, and ethics
6. preliminary evidence separated from proposed work
7. rigor, feasibility, team/resources, milestones, risks, alternatives, and stop criteria
8. expected contribution and bounded impact
9. explicit approval/feedback request

Do not use a generic `Significance -> Innovation -> Approach` sequence when the active sponsor has a
different rubric. NIH's current simplified framework is one example—not a universal template—and
groups review under importance, rigor/feasibility, and expertise/resources. Always verify the exact
call and due-date-applicable criteria.

**Decisive slide:** usually an aims-to-evidence-to-decision map, not a decorative vision graphic.

**STOP:** aims conflict with the frozen grant; feasibility has no resource/milestone basis; a proposed
method is narrated as a completed result; or the active review rubric is unknown.

## Route 2 — lab meeting or work-in-progress

**Job:** expose the actual state of the work so collaborators can diagnose problems and choose next
actions. Do not retrofit a clean publication story around unresolved results.

**Arc:**

1. decision/question for this meeting
2. minimum prior context and what changed since the last checkpoint
3. current protocol/analysis state and deviations
4. result or failure evidence, including negative and discordant findings
5. competing explanations and sensitivity checks
6. blocked decisions, options, resource implications, and proposed next experiment
7. named decisions/actions, owners, and evidence needed for closure

Use status titles such as “The external-centre drop remains unexplained” rather than “Our model is
robust” when the cause is unresolved. Keep an appendix with exact parameters, logs, exclusion
details, and failed analyses required for technical discussion.

**STOP:** cherry-picked “best run”; silent protocol drift; post hoc analysis presented as prespecified;
or the deck hides uncertainty needed for the requested decision.

## Route 3 — conference or invited scientific talk

**Job:** communicate one defensible contribution to the meeting audience within the allotted time.

**Arc:**

1. common ground and clinical/scientific tension
2. one main question
3. minimum methods needed to trust the answer
4. one anchor result (“money slide”) with its uncertainty
5. essential supporting/validation evidence
6. bounded interpretation, limitation, implication, and memorable close

Compress background and method inventories before compressing decisive evidence. A short talk is not
a rapid narration of a paper. Preserve one take-home message and keep nonessential sensitivity
analyses or implementation details in backup.

**STOP:** time slot, audience, or organizer/template rules unknown; decisive result cannot be read at
venue scale; or a conference abstract is stronger than the frozen analysis it purports to summarize.

## Route 4 — journal club, paper presentation, or reading conference

**Job:** help the audience understand and critically appraise an external work; distinguish the
authors' conclusion from the presenter's assessment.

**Arc:**

1. citation, clinical/scientific question, and why the paper matters
2. study design and population/data provenance
3. imaging acquisition/measurement and reference-standard chain
4. model/statistical design, data splits, validation, and comparator
5. primary result with uncertainty and denominator
6. calibration/utility/robustness or synthesis evidence as applicable
7. strengths, bias/leakage/reproducibility threats, applicability, and missing evidence
8. `Authors conclude` versus `We can defensibly infer`
9. focused discussion questions and what transfers to the local project

For paper-type subroutes:

| Paper type | Preserve in the evidence arc |
|---|---|
| Diagnostic accuracy | index test, reference standard, threshold, patient flow, accuracy uncertainty |
| Prediction/AI | split hierarchy, preprocessing fit boundary, comparator, calibration, external validation |
| Radiomics | image/segmentation passport, feature extraction/harmonisation, stability, feature-selection boundary |
| Radiogenomics | patient/specimen/time matching, omics layer, multiplicity, association versus mechanism |
| Review/meta-analysis | search/screening, heterogeneity, risk of bias, pooled-estimate applicability |

**STOP:** source is too partial to verify a decisive figure/claim; copied figure context is missing; or
critique is presented as a fact without an evidence or reasoning trail.

## Route 5 — project, milestone, or steering review

**Job:** let responsible people compare current state with the agreed plan and make an intervention,
resourcing, scope, or continuation decision.

**Arc:**

1. review period, agreed objectives, and requested decisions
2. milestone state versus baseline plan
3. delivered evidence, not activity inventory
4. variance: schedule, data, quality, performance, budget/resource, compliance
5. root cause and uncertainty, not only red/amber/green status
6. risk exposure and dependency map
7. options with consequence, owner, date, and evidence for closure
8. next milestone and escalation threshold

Separate `done`, `in progress`, `blocked`, `changed`, and `not verified`. Do not use percentage
complete when the denominator or completion definition is unstable.

**STOP:** current baseline is unknown; activity is substituted for outcome; or a risk is visually
downplayed despite being able to invalidate the scientific claim or ethical authorization.

## Route 6 — thesis, dissertation, or candidacy defense

**Job:** enable examiners to judge whether the candidate understands the problem, made a defensible
original contribution, used rigorous methods, and understands limits and next steps.

**Arc:**

1. thesis question and contribution claim
2. prior-work boundary: what was known, missing, and not done by the candidate
3. chapter/aim map with candidate contribution and collaborators' contribution
4. methods needed to evaluate each claim
5. results and validation in the order needed to support the contribution
6. synthesis across chapters, including contradictions
7. limitations, failed or negative work relevant to validity
8. contribution matrix and future work clearly separated
9. concise closing answer to the thesis question

Keep backup slides for cohort derivation, parameter choices, assumption checks, supplementary
results, contribution/author roles, and likely examiner questions. Future work cannot be counted as
the completed contribution.

**STOP:** authorship/contribution is ambiguous; chapter evidence does not support the global thesis
claim; or confidential/unpublished content has no approved presentation boundary.

## Route 7 — results, analysis, or decision deck

**Job:** make a frozen result set interpretable for a specified scientific, clinical-development, or
operational decision.

**Arc:**

1. decision/question and analysis population
2. analysis contract, estimand/endpoint, and data-quality state
3. primary result with effect/accuracy and uncertainty
4. supporting, subgroup, sensitivity, failure, and missingness evidence
5. alternative explanations and applicability
6. recommendation or next decision, explicitly separated from observed result

The same analysis needs different explanation for statisticians, imaging scientists, clinicians, and
executives. Change context and decision framing, not the numerical result or uncertainty.

**STOP:** result freeze is absent; cohort/denominator or metric definition changes across slides; or
the requested recommendation would exceed the observed evidence.

## Mixed-deck rule

List the composition explicitly, for example:

`Primary: project review | Secondary module: lab-meeting technical diagnosis | Evidence: INTERIM`

Do not concatenate complete routes. Keep the primary route's opening and close, and borrow only the
minimum secondary module required for the decision.

## Sources and rule provenance

- Garner JK, Alley MP. *How the Design of Presentation Slides Affects Audience Comprehension: A
  Case for the Assertion-Evidence Approach*. International Journal of Engineering Education.
  2013;29(6):1564-1579. The experiment supports sentence-message headlines and relevant visual
  evidence over common topic/bullet defaults; it does not prove one structure is optimal for every
  audience or deck job. https://www.ijee.ie/articles/Vol29-6/23_ijee2791ns.pdf
- NIH Office of Dietary Supplements. *Scientifically Speaking: How to Prepare an Effective Talk*.
  Supports audience common ground, a main question, an anchor result, synthesis, and time-aware
  supporting material. Its “two minutes per slide” is an average example, not a universal quota.
  https://ods.od.nih.gov/News/Scientifically_Speaking_How_to_Prepare_an_Effective_Talk.aspx
- Naegle KM. *Ten simple rules for effective presentation slides*. PLOS Computational Biology.
  2021;17:e1009554. Supports one main idea per slide, conclusion-oriented titles, meaningful figures,
  and rehearsal-linked slide scope. https://doi.org/10.1371/journal.pcbi.1009554
- NIH. *Simplified Peer Review Framework*. Current official example of sponsor-specific grant review
  factors for many NIH research project grants due on or after 25 January 2025; applicability must be
  checked against the exact opportunity and date. https://www.grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework
- RSNA. *Faculty and presenter resources*. Use only for the applicable meeting year and presentation
  type; organizer templates and upload rules override generic defaults. https://www.rsna.org/annual-meeting/attendee-resources/faculty-and-presenter-resources
