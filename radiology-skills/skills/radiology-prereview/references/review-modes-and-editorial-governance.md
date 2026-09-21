# Review modes and editorial governance

Select the review mode before reading the paper. The same scientific concern can be valid in several
modes, but audience, confidentiality, conflicts, output and authority differ.

## Mode contract

| Mode | User and purpose | Required output | Authority boundary |
|---|---|---|---|
| `author-prereview` | authors repair their own draft before submission | severity-ranked findings, fixes, closure criteria and readiness receipt | may recommend edits; does not predict or make a journal decision |
| `journal-peer-review` | invited confidential review for a journal | comments to authors, confidential comments to editor, declared COI/confidentiality/AI state and recommendation if requested | reviewer advises; editor/journal decides |
| `editorial-synthesis` | synthesize frozen reviewer reports for an authorized editorial task | agreement/disagreement map, decision-bearing issues and proposed editorial rationale | do not fabricate reviews, identities or an official decision |
| `thesis-prereview` | audit a thesis/dissertation and defense readiness | chapter/argument/method/result consistency findings, contribution map, defense questions and closure evidence | institutional degree rules and committee decisions require live local verification |

Default to `author-prereview` for the author's own manuscript. Use `journal-peer-review` only when the
user states a real invited-review context or explicitly asks for that output form. Do not infer editor
authority from a request to "act like an editor."

## Journal-peer-review intake gate

Before processing a confidential manuscript, record:

`journal/role | manuscript ID and version | review criteria/instructions | due date | confidentiality
terms | external-tool/AI policy | author permission if applicable | reviewer relationships/activities |
recusal decision | assistance by trainees/colleagues and journal permission`.

Use states `POLICY_VERIFIED`, `POLICY_UNRESOLVED`, `COI_CLEAR`, `COI_DISCLOSE`, `RECUSE`,
`AI_USE_AUTHORIZED`, `AI_USE_PROHIBITED` and `STOP_CONFIDENTIALITY_UNRESOLVED`.

ICMJE treats submitted manuscripts as privileged confidential communications. Its current
recommendations say reviewers must keep them confidential, disclose relationships that could bias
review, recuse when a conflict exists, request journal permission before using AI to facilitate review,
and avoid uploading a manuscript where confidentiality cannot be assured. The journal's current policy
is controlling. Unknown permission is a stop, not implied consent.

## Reading and output order

1. Freeze the manuscript/version and the journal criteria before review.
2. Declare scope, missing files, COI, confidentiality and AI/tool state before substantive comments.
3. Review contribution, methods, statistics, imaging measurement, validation, reporting and claim
   ceiling against evidence anchors; never search for author identity in a blinded review.
4. Write comments to authors: concise summary, major issues, minor issues and actionable evidence
   requests. Do not expose confidential editor-only content.
5. Write confidential comments to editor separately: COI/ethics/integrity signals, fatal scope issues,
   recommendation/rationale when requested and uncertainty. Do not accuse misconduct or infer intent;
   route signals to the editor/institutional integrity process.
6. Preserve a private review receipt with manuscript digest, policy source/date, declarations and
   output digest; destroy/retain copies according to the journal policy.

A reviewer recommendation is advisory. Never state acceptance/rejection as an official editorial
decision, contact authors outside the journal process, appropriate unpublished ideas/data, fabricate
reviewer identities, or use confidential content for another project.

## Thesis-prereview additions

Audit the thesis-level research question, contribution across chapters, reuse/publication declarations,
method and cohort consistency, cross-chapter values/figures, negative results, limitations, appendices,
data/code/ethics/AI disclosures and defense claims. Route thesis architecture to `radiology-writing`
and the defense deck to `radiology-paper2ppt`. Verify local graduate-school formatting, embargo,
publication and committee rules live; do not generalize one institution's handbook.

## Sources

- ICMJE. [Responsibilities in the Submission and Peer-Review Process](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/responsibilities-in-the-submission-and-peer-peview-process.html)
  (official recommendations accessed 2026-08-23).
- ICMJE. [Use of Artificial Intelligence in Publishing](https://www.icmje.org/recommendations/browse/artificial-intelligence/)
  (official recommendations accessed 2026-08-23).
- COPE. [Ethical Guidelines for Peer Reviewers](https://publicationethics.org/resources/guidelines/cope-ethical-guidelines-peer-reviewers)
  (verify current journal adoption and version before a real review).

This reference governs the review process, not scientific ownership. Domain findings still route to
their specialist, and `radiology-research-integrity` owns evidence preservation/escalation for an
integrity signal without adjudicating misconduct.
