# Risk, change, freeze, pause and closeout

Use this reference during active control, recovery, release and project end. Keep operational records
distinct so that a future risk does not masquerade as a current issue and a deviation does not vanish
inside a meeting note.

## 1. Six separate registers

| Register | Meaning | Minimum fields |
|---|---|---|
| risk | uncertain future event | cause-event-effect, probability/uncertainty, impact, trigger, mitigation, contingency, owner |
| issue | present problem | observation/evidence, impact, containment, root-cause status, corrective action, deadline, owner |
| decision | authorized choice | question, evidence/options/criteria, decision owner, rationale, dissent, action and stale artifacts |
| change | proposed/approved modification | old/new, reason, timing, approval route, validation, affected scope/version |
| deviation | actual divergence from frozen protocol/SOP/plan | planned/actual, detection, result awareness, cause, impact, reportability, correction/prevention |
| incident | safety, privacy, security or material operational event | time, affected people/data/system, containment, authorized reporting, investigation owner, recovery |

Do not assign cause, blame or institutional reportability without the authorized owner. `Root cause
unknown` is preferable to a convenient unsupported story.

## 2. Risk-based quality control

Name critical-to-quality factors that can materially affect participant rights/safety or reliability
of results. For each define risk, prevention, detection, evidence, tolerance/decision rule and owner.
Apply proportionate monitoring; do not copy clinical-trial monitoring requirements to a retrospective
or computational project without applicability.

Escalate when a tolerance is crossed. Repeated small deviations can form a systemic issue even when
each alone is minor. Preserve adverse and negative operational evidence.

## 3. Freeze and release contract

A freeze records:

`freeze ID/type | scope | included/excluded IDs | source versions and digests | criteria/tests |
unresolved exceptions | accountable approver role | time | write/access controls | downstream users |
release status | superseding freeze`.

Common freezes: eligibility/cohort, accepted imaging, annotation/reference, data dictionary and data
cut, split, SAP/analysis, model/threshold, primary results, figures/tables, manuscript and archive.

- `FROZEN` means the registered object cannot be silently changed; it does not certify scientific
  validity.
- A post-freeze correction creates an explicit amendment/new freeze, impact analysis and downstream
  staleness record.
- Release requires acceptance evidence, not the planned date or a folder name containing “final.”

## 4. Recovery, pause and termination

For a failed milestone return:

`constraint -> evidence -> options -> time/resource/scientific trade-off -> success/failure criterion
-> decision date -> owner -> downstream impact`.

Pause when authorization, safety, data integrity, critical resources or inference are unresolved but
may be repaired. Terminate when a STOP criterion is met, repair is infeasible, benefit no longer
justifies cost/risk, or the authorized owner decides to end. This skill recommends; the institution,
sponsor and PI decide under their authority.

Preserve participants' follow-up/safety obligations, data custody, contracts, specimens, model/code,
records and communications during pause/termination. Do not abandon open safety or access duties.

## 5. Closeout receipt

Reconcile:

- site and personnel status, delegation/training and unresolved actions;
- screened/enrolled/followed participants and safety/reporting duties;
- examinations/series/lesions, annotations, specimens and assay inventory;
- queries, deviations, incidents, changes and decisions;
- frozen datasets, splits, code/config/results and negative/failure artifacts;
- equipment/material accountability and outstanding vendors/contracts;
- actual-versus-planned resource/cost evidence, without performing institutional finance sign-off;
- data/model access, retention/destruction, repository and reproducibility handoff; and
- publication, correction, authorship and knowledge-reuse responsibilities.

Return `CLOSEOUT_READY`, `CLOSEOUT_CONDITIONAL` or `CLOSEOUT_BLOCKED`. A paper, grant end date or
empty task list does not establish closeout.

