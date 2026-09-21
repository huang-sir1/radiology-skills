# Conference portal finalization

This route owns the final conference/congress portal field and upload-file audit. It does **not**
draft, shorten, scientifically revise, or approve the abstract. Conference-abstract content remains
with `radiology-dissemination`; this route accepts only a frozen abstract artifact and its handoff
receipt.

## 1. Route boundary

Use this branch when the request is to verify the final portal fields, upload designations, file
bytes, declarations, deadline/cycle binding, or hand off a prepared package to an authorized human.
Route abstract argument, audience adaptation, word/character compression, poster content, or meeting
communications back to `radiology-dissemination`. Route a manuscript Abstract to
`radiology-writing`, a meeting slide deck to `radiology-paper2ppt`, and internal meeting minutes to
`radiology-research-ops`.

Never reuse a journal profile, publisher-family rule, prior-year call, accepted abstract, search
snippet, third-party meeting summary, or generic portal landing page as the current meeting contract.
The 11 journal routes and their deterministic auditor remain separate.

## 2. Freeze a conference intake passport

Start from `../assets/conference-portal-intake.template.json`. The exact venue series, submission
cycle and submission type must be repeated in both the current-call and live-portal bindings:

`venue_series_id | submission_cycle | submission_type | current_call_url | portal_url |
call_checked_on | portal_checked_on | submission_deadline | call_capture_sha256 |
call_capture_locator | portal_capture_sha256 | portal_capture_locator`.

The current call must visibly be open for that exact cycle and type. Record the stated deadline with
its UTC offset; a date without the venue timezone cannot close the deadline gate. The portal capture
must show the actual field/file designation for the same venue, cycle and submission type. Machine
checks can verify receipt syntax and internal equality only; an authorized human must authenticate
both captures. If the portal is available only after login, keep its locator private and never store
credentials, cookies, access tokens, author passwords, full session exports, or unnecessary personal
data in the repository or upload root.

Recheck both sources during the finalization task. A missing, closed, stale, future, wrong-cycle,
wrong-type, or unbound call returns `CALL_EVIDENCE_UNVERIFIED`. A portal that cannot be tied to the
exact current instance returns `PORTAL_EVIDENCE_UNVERIFIED`. Neither is a waivable warning.

## 3. Accept only a frozen scientific-content handoff

The intake binds:

`project_id | abstract_artifact_id | abstract_sha256 | dissemination_handoff_sha256 |
claim_registry_digest | analysis_lock_digest | content_owner=radiology-dissemination`.

The handoff must identify the frozen abstract version, source claims, denominators, uncertainty,
limitations, submission category and unresolved scientific decisions. `radiology-submission` may
map that content into verified portal fields, but it must not strengthen causal, diagnostic,
prognostic, clinical-utility, generalisability, novelty, priority, regulatory, or deployment claims.
If a portal field requires new scientific wording rather than a mechanical transfer, return it to
the content owner and invalidate the previous abstract hash after revision.

## 4. Build the field/file manifest

Use `../assets/conference-portal-manifest.template.csv`. One row represents one upload file, portal
field, or portal attestation. Do not store passwords or live credentials and avoid storing private
field values when a controlled locator is sufficient.

- `upload-file`: use a safe relative path inside the author-confirmed upload root, bind the actual
  upload SHA-256, retain the frozen source-artifact receipt, record only the extension allowlist and
  size limit visibly established by the exact current call/portal, verify the real container rather
  than the suffix alone, and complete technical/render/content, privacy and rights review before
  handoff.
- `portal-field`: name the exact portal designation and bind the source artifact/value locator. Keep
  the path and upload digest empty. Values such as title, abstract text, author order, affiliations,
  keywords, presenter, acknowledgments, funding and registration identifiers must reconcile with the
  frozen content and authorized records.
- `portal-attestation`: map the exact statement, authorized human owner and current source. AI-use,
  conflicts, funding, prior presentation/publication, permissions, presenter eligibility, copyright
  or license grants, ethics/consent, and author approval are not facts the model may invent or attest.

Every row records `CURRENT_CALL`, `PORTAL_CURRENT`, or `OFFICIAL_FORM` authority, an official direct
URL, checked date, requirement class/condition, content/version receipts, a non-empty claim boundary,
separate embargo/disclosure/privacy gates and the responsible human. Required or triggered
conditional rows cannot be marked not applicable. Optional omission never cures a conflicting hard
portal rule.

Close the inventory in both directions: every actual upload byte has one manifest row and every
upload-file row resolves to one current file. A field manifest is not proof that a human pasted the
value correctly.

## 5. Independent release boundaries

- **Claim:** portal mapping may preserve or weaken the frozen evidence claim; it may not upgrade it.
- **Embargo:** verify current meeting, journal, sponsor and institutional publicity rules separately.
  Abstract submission, acceptance and public release are different events.
- **Disclosure:** reconcile authorship/presenter approval, conflicts, funding, AI use, prior
  presentation/publication, copyright/license and required attestations. The model never signs.
- **Privacy:** inspect DICOM pixels/metadata, screenshots, filenames, notes, hidden objects, office
  metadata and linked files for PHI or unnecessary personal data. De-identification does not establish
  consent, image-reuse rights or portal authority.
- **Rights:** a citation is not permission. Preserve license/permission/attribution evidence for every
  reused figure, image or third-party element.

Any unresolved package-level gate stays `PORTAL_PACKAGE_BLOCKED`. `NOT_APPLICABLE` is not a machine
shortcut for embargo, disclosure, privacy, rights or author approval.

## 6. Deterministic check and human final action

Run outside the upload root:

```powershell
python scripts/validate_conference_portal_package.py conference-intake.json `
  conference-manifest.csv --package-root C:\author-confirmed-conference-upload-root
```

The checker validates exact schemas, duplicate keys/headers, venue-cycle-type binding, dated live
receipts, deadline timezone, closed inventory, file hashes, source-artifact binding and the five
package gates. It never opens the portal, enters values, clicks attestations, uploads, submits, pays,
withdraws, or grants readiness. Its report always keeps `readiness_granted=false` and
`portal_action_performed=false`.

Its only progression state is `HUMAN_PORTAL_ACTION_REQUIRED`, which means the prepared field/file
map passed the modeled checks and still requires the named authorized human to re-open the live
portal, compare every value and file, make attestations, and perform the final action. Any defect
returns `PORTAL_PACKAGE_BLOCKED`; unresolved live sources use the more specific states above.

After the human submits, preserve the official confirmation identifier/page/email as a private
receipt with time, venue/cycle/type, package inventory digest and final abstract hash. Until an
authorized human authenticates that receipt, do not say `SUBMITTED`, `ACCEPTED`, `PUBLISHED`, or
`EMBARGO CLEARED`. Meeting acceptance is not scientific validation and does not authorize later
journal submission or public reuse.
