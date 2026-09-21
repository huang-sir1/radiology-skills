# Revision-letter writing chain

Use this file after comments are atomized and scientifically adjudicated. It controls how verified
decisions and evidence become an editor-facing response letter; it does not decide whether a reviewer
request is scientifically necessary.

## 1. Build the document in verification order

Write in this order even if the final journal template differs:

1. manuscript title, ID, decision date and revised version identifier;
2. concise editor-facing summary of **completed** material changes;
3. editor instructions (`E-#`) in their original order;
4. Reviewer 1, Reviewer 2, and so on, preserving comment order and stable IDs;
5. each quoted or faithfully paraphrased comment followed by its response block;
6. visible unresolved/author-input items in a working draft;
7. revision verification receipt for the author team; exclude internal audit notes from the submitted
   letter unless the journal requests them.

Write the editor summary last. It may summarize only changes that already close in the ledger.

## 2. Convert one comment into one response block

For every atomic child commitment that requires new work or a manuscript change, populate this
evidence order in the internal drafting record:

`position -> governing reason -> action and method -> actual result -> manuscript consequence ->
exact location -> residual boundary -> artifact fulfillment`

The position is one of `accept`, `partially accept`, `contest`, or `cannot address`. Do not blur these
states with courteous language. If a compound parent contains three obligations, answer all three
child IDs before closing the parent.

### Accept and repair

> We agree that **[governing issue]** was not sufficiently addressed. We therefore **[specific
> action]** using **[method, data unit and comparator]**. **[Actual result, including uncertainty or
> a negative finding.]** We revised **[section/figure/table/supplement and exact location]** to
> **[new bounded claim or reporting change]**. **[Residual boundary, if any.]**

Do not write “we have revised accordingly” without the operation and result.

### Clarify or report existing evidence

> We appreciate that the original presentation did not make **[design/result distinction]**
> reconstructable. **[Evidence]** was part of the original analysis and no new data were collected
> for this response. We now report **[specific detail/result]** in **[exact location]** and have
> clarified **[affected claim]**.

Use “existing analysis clarified” only when versioned artifacts confirm that status. Otherwise call
it a new analysis.

### Partially accept

> We agree with **[valid premise]**, but the requested extension assumes **[unsupported premise or
> broader scope]**. To address the decision-bearing part, we **[feasible action/method]** and found
> **[result]**. We revised **[locations]** and no longer claim **[surrendered claim]**. The remaining
> limitation is **[explicit boundary]**.

The response must make the accepted and unaccepted parts independently inspectable.

### Evidence-based disagreement

> We respectfully disagree that **[requested operation]** is required to establish **[specific
> current claim]**, because **[governing scientific reason, not preference]**. The relevant existing
> evidence is **[versioned artifact/result with location]**. **[If a real ambiguity remains: We added
> clarification or a discriminating sensitivity analysis at location and report its result.]**
> **[If no change is scientifically justified: No new analysis or manuscript change was made; the
> existing evidence and bounded claim already satisfy criterion.]** The supported scope remains
> **[scope]**, with **[residual boundary]**.

Do not write that the reviewer “misunderstood.” Show which manuscript ambiguity allowed the reading
and repair it when feasible. A compromise edit or sensitivity analysis is not a courtesy tax: require
one only when it reduces a real ambiguity or tests a decision-bearing assumption.

### Legitimate no-new-work routes

- `ACKNOWLEDGE_ONLY`: use for praise, summary or a non-actionable observation; create no scientific
  commitment.
- `ANSWER_FROM_EXISTING_RECORD`: answer from a versioned artifact and give its source locator; do not
  imply the analysis was newly performed.
- `CROSS_REFERENCE_ONLY`: point to the stable canonical issue/response ID and state which child
  obligation is answered.
- `NO_CHANGE_JUSTIFIED`: state the governing criterion and existing evidence locator; record
  `N/A—NO_NEW_WORK` and `N/A—NO_MANUSCRIPT_CHANGE_JUSTIFIED` internally rather than fabricating a
  method, result or revised location.

These routes still receive internal verification. They do not require an author-facing closure label.

### Cannot perform the requested experiment or analysis

> We agree that **[requested evidence]** would test **[question]**. We could not perform it because
> **[specific feasibility, validity or interpretability constraint]**. Instead, we **[nearest
> informative control/triangulation]**, which showed **[result]**. We revised **[locations]** to state
> **[lower claim]** and now list **[residual uncertainty]** as a limitation.

Cost or time alone rarely closes a mechanism-bearing request. Explain why the alternative evidence
is interpretable and reduce the claim when the requested evidence remains absent.

### Negative or null result

> We performed **[analysis/experiment]** as requested. The result did not support **[hypothesis]**:
> **[estimate/readout and uncertainty]**. We therefore changed **[claim/model/figure]** in
> **[locations]** and discuss **[interpretation and residual uncertainty]**.

A negative result is not a failed response. Hiding it or preserving the contradicted headline is.

## 3. Keep response prose and manuscript prose distinct

The response paragraph explains the decision and proves the change. The manuscript contains the
scientific content needed by future readers. Do not paste a long rebuttal rationale into Results or
leave a new result only in the letter.

| Response content | Manuscript surface to update |
|---|---|
| new cohort, sample flow, exclusion or mapping | Methods plus flow diagram/table; Results if usable n changes |
| new analysis/model/statistical test | Methods/SAP, Results, affected figure/table/legend and supplement |
| new experiment or validation | Methods, Results, figures/source data and Discussion boundary |
| claim reduction | title, abstract, Results interpretation, Discussion, conclusion, legends and highlights as applicable |
| new code/data/model artifact | availability statement, repository/accession/version and supplement |
| limitation only | Discussion plus every headline claim that depended on the absent evidence |

Quote revised manuscript text only after the final content is stable. After reformatting, refresh all
page and line locations; do not retain stale locators from a previous pagination.

## 4. Handle reviewer interactions

- **Conflicting requests:** state the shared scientific criterion, show why both literal actions cannot
  be applied simultaneously, choose the defensible analysis, provide sensitivity if useful, and ask
  the editor to adjudicate only when the scientific conflict remains material.
- **Repeated comments:** answer fully once, then cross-reference the stable issue ID and location;
  never give subtly different results in duplicate responses.
- **One result answers several comments:** preserve separate IDs and explain which part of the common
  evidence closes each commitment.
- **New concern created by revision:** add a new issue ID, rerun affected scientific gates and disclose
  the changed claim rather than pretending the original closure is untouched.
- **Reviewer asks for absent modality:** adjudicate whether the current claim requires it. Add the
  evidence, lower the claim, or give criterion-based pushback; do not invent expected results.

## 5. Tone rules

- Open with one brief acknowledgment when useful, then move to the scientific criterion.
- Use calm first-person plural; avoid flattery, defensiveness, motives and statements about reviewer
  competence.
- Prefer precise verbs: `added`, `reanalysed`, `validated`, `reported`, `clarified`, `removed`,
  `restricted`, `could not perform`.
- Avoid empty verbs: `addressed`, `improved`, `considered`, `revised accordingly` unless immediately
  followed by the concrete operation.
- Do not oversell compliance. “Reviewer satisfied” is secondary to the independently verifiable
  action and result.
- Preserve uncertainty. Never turn “not significantly different” into equivalence or absence of effect.

## 6. Working draft versus submission-ready letter

| State | Allowed content |
|---|---|
| Planning draft | visible `[AUTHOR_INPUT_NEEDED]`, `[ANALYSIS_PENDING]`, `[RESULT_NEEDED]`, `[LOCATION_PENDING]` placeholders |
| Internal verification draft | real results and provisional locations; open commitment and cross-artifact checks remain visible |
| Submission-ready | no implied-but-unverified action, no missing result, exact final locations, all parent/child commitments classified, residual limitations propagated |

Never delete an unresolved item merely to make the letter look complete. Move it into the author
decision queue and block submission-ready status.

Set `audit_mode: working` or `final`. Working mode may retain visible placeholders. Final mode must
have `unresolved_placeholder_count = 0`; any `[AUTHOR_INPUT_NEEDED]`, `[ANALYSIS_PENDING]`,
`[RESULT_NEEDED]`, `[LOCATION_PENDING]` or unresolved template token forces
`NOT_READY_FOR_SUBMISSION_ASSEMBLY`.

## 7. Editor summary pattern

Keep the opening summary short and material:

> We thank the editor and reviewers for their evaluation. In the revised manuscript, we have
> **[change 1 with scientific purpose]**, **[change 2]**, and **[change 3]**. These revisions
> **[state the resulting claim consequence]**. We also **[important limitation/claim reduction]**.
> A point-by-point response and exact manuscript locations follow.

Do not list every copyedit. Do not say “all concerns were fully addressed” unless the independent
closure audit confirms every required child commitment and no unresolved item remains.

## 8. Final language audit

For each block ask:

1. Can the reader tell whether the author accepts, partly accepts, contests or cannot comply?
2. Is the scientific reason explicit?
3. If work was performed, are method and actual result both present?
4. Can the change be found at the stated location?
5. Does the revised claim match the result and residual limitation?
6. Is every child commitment closed, pending or explicitly declined?
7. Would the paragraph remain persuasive if all courtesy phrases were removed?

If any answer is no, the block is not submission-ready.
