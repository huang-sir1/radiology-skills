# Source authority and live-refresh contract

Use this contract whenever the audit asserts that a file, field, format, limit, form or checklist is
required, allowed or prohibited.

## Authority classes

| Class | What it can establish | What it cannot establish |
|---|---|---|
| `JOURNAL_GUIDE` | Journal- and article-type-specific content, structure, limits and named materials | A logged-in portal's current upload widget unless stated |
| `PORTAL_CURRENT` | The actual file designation, accepted extension, required field or attestation shown for this submission instance | A durable rule for other article types or future submissions |
| `PORTAL_PLACEHOLDER` | Advisory discovery of a publisher or journal workflow endpoint that is visibly incomplete, under development or not the genuine submission instance | Any required field, accepted extension, upload designation or route closure; it is non-authoritative and cannot be promoted to `PORTAL_CURRENT` |
| `OFFICIAL_FORM` | Required fields and file behavior of that exact form/template | That every journal sibling requires the form |
| `PUBLISHER_POLICY` | Cross-journal ethics, data, code, authorship, image or reporting policy | A journal-specific article limit when the journal guide differs |
| `REPORTING_STANDARD` | Checklist content for the matching study design | That the target journal mandates upload of the checklist |
| `PUBLISHED_EXEMPLAR` | Observed house style, section rhythm and display strategy | Submission file type, word limit, required attachment or portal field |
| `SECONDARY_SUMMARY` | Discovery lead only | Any hard compliance decision |

## Conflict resolution

1. Match exact journal, article type and submission stage before comparing rules.
2. For upload mechanics, a captured current portal requirement governs that submission instance.
3. For manuscript content and attachments, a journal-specific guide overrides publisher-family prose.
4. Official article-type pages and named forms refine a general journal guide.
5. Publisher policy remains binding on its declared axis unless the journal explicitly narrows it.
6. Published exemplars and third-party summaries never override an official rule.
7. Record conflicts in parallel. Do not silently choose the more convenient rule.

## Live verification receipt

Every decisive rule records:

`rule_id | journal_id | article_type | stage | applicable_stages | authority_class | page_title | direct_url |
visible_version_or_update | checked_on | requirement | condition | file_type_or_limit | evidence_paraphrase`

`stage` records the rule's primary evidence context. `applicable_stages` is a semicolon-delimited,
explicit allowlist for route reuse (for example, `initial;pre-review`). A route contract may cite a
rule only when its own stage appears in that allowlist; publisher or journal-family similarity does
not justify implicit cross-stage reuse.

Use direct official URLs. A search-result URL is not a source. If a page is dynamic, record the
visible portal label or screenshot locator and session date without exposing credentials or private
manuscript content.

For a `PORTAL_CURRENT` override, the manifest `notes` field must contain this semicolon-delimited
structured receipt:

`portal_capture_sha256=<64-hex>; portal_capture_date=<YYYY-MM-DD>; portal_journal_id=<journal_id>; portal_article_type=<article_type>; portal_stage=<stage>; portal_screen=<screen label>; portal_locator=<concrete capture locator>`

`portal_capture_date` must equal manifest `guide_verified_on`; journal, article type and stage must
match the frozen intake passport. The deterministic auditor checks field presence, syntax, route/date
agreement and internal consistency only. A human must still open the locator and verify that the
capture is genuine, readable, current, from the exact journal and submission instance, and actually
shows the claimed designation or extension. A generic journal page on the same parent domain is not a
portal capture. An Editorial Manager development page is `PORTAL_PLACEHOLDER`, not
`PORTAL_CURRENT`, and cannot resolve a file-type rule.

## Decision-letter boundary

A genuine decision letter is instance-specific editorial evidence after a human verifies journal,
manuscript identity, stage, date and the exact instruction. It is not a live portal and must never be
encoded as `PORTAL_CURRENT`. The deterministic auditor does not authenticate email/PDF provenance and
therefore cannot close a rule directly from a decision letter. Either keep the route `INCOMPLETE`, or
have a maintainer incorporate the adjudicated rule into the bundled evidence/contract and rerun the
validator and regression suite. Record the letter hash and locator in the human report without placing
private correspondence inside the upload root.

## Refresh policy

- For a final upload audit, refresh every decisive journal guide and file-type rule during the task,
  even when a local snapshot exists.
- Treat repository profiles as routing caches and known-question lists, not permanent authority.
- If the official page is unavailable, try another official journal/publisher path or supplied
  current guide. Otherwise mark the affected rule `UNVERIFIED_CURRENT_GUIDE`.
- A hard unverified rule that could change acceptance keeps the package `INCOMPLETE`; it is not a
  warning that can be waived by the model.
- Preserve the checked date and source URL in the manifest so a later audit can detect staleness.

For a same-rule task-local refresh, copy the complete TSV outside the upload root, recheck every
decisive source, and change only `checked_on` and `verification_status`. Pass that copy with
`--evidence`; the auditor compares all substantive fields with the bundled validated registry and
reports both evidence paths and SHA-256 hashes; it also records the immutable bundled route-contract
path and SHA-256 for replay. A changed URL, requirement, condition, article/stage
scope or allowed extension is not a refresh: update the bundled registry and route contract, then run
`scripts/validate_submission_skill.py` before using it for readiness.

## Published-article learning

Use 1–3 recent comparable papers to observe title rhythm, abstract density, section order, figure
architecture, captions and declarations. Label every such inference `OBSERVED_EXEMPLAR`, state the
sample size and study-type match, and keep it advisory. Production layout and published PDF appearance
may differ from files accepted at submission.
