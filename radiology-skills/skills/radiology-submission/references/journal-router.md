# Journal route registry

The route ID, article type and stage must all resolve before a journal-compliance verdict. These
profiles are verified routing caches, not permanent copies of the author guide. Refresh every
decisive rule from its direct official URL during the final audit and record the receipt in the
manifest.

## Supported routes

| Canonical `journal_id` | Contract article type (exact label) | Human-recognized names; normalize before machine intake | Profile |
|---|---|---|---|
| `radiology` | `Original Research` | Radiology, RSNA Radiology | [journals/radiology.md](journals/radiology.md) |
| `nature-medicine` | `Article` | Nature Medicine, NM | [journals/nature-medicine.md](journals/nature-medicine.md) |
| `nature-communications` | `Article` | Nature Communications, Nat Commun | [journals/nature-communications.md](journals/nature-communications.md) |
| `lancet-digital-health` | `Article` | The Lancet Digital Health, Lancet Digital Health, TLDH | [journals/lancet-digital-health.md](journals/lancet-digital-health.md) |
| `eclinicalmedicine` | `Article` | eClinicalMedicine, EClinicalMedicine, eCM | [journals/eclinicalmedicine.md](journals/eclinicalmedicine.md) |
| `cancer-cell` | `Research Article` | Cancer Cell | [journals/cancer-cell.md](journals/cancer-cell.md) |
| `cell-reports-medicine` | `Research article` | Cell Reports Medicine, CRM | [journals/cell-reports-medicine.md](journals/cell-reports-medicine.md) |
| `npj-digital-medicine` | `Article` | npj Digital Medicine, npj DM | [journals/npj-digital-medicine.md](journals/npj-digital-medicine.md) |
| `npj-precision-oncology` | `Article` | npj Precision Oncology, npj PO | [journals/npj-precision-oncology.md](journals/npj-precision-oncology.md) |
| `advanced-science` | `Research Article` | Advanced Science | [journals/advanced-science.md](journals/advanced-science.md) |
| `jama-network-open` | `Original Investigation` | JAMA Network Open, JNO | [journals/jama-network-open.md](journals/jama-network-open.md) |

Machine-readable evidence is in
[journal-requirements-evidence.tsv](journal-requirements-evidence.tsv). A row marked
`UNVERIFIED_CURRENT` is a question to resolve, never an allowed default.

## Executable contract coverage

The 11 profiles support human journal-specific review, but the deterministic minimum-material
contract is intentionally narrower: one named primary-research article type per journal. Its PASS is
not whole-profile compliance; manuscript-content limits, declarations, visual review, live-portal
mechanics and decision-letter instructions remain additive human gates. Any structural ERROR makes
`route.minimum_material_contract=FAIL`. Unsupported article types or stages receive journal-neutral
inventory/integrity checks only and remain `ROUTE_UNSUPPORTED`/`INCOMPLETE`; a family profile is not a
substitute.

| Stage | Executable journal/article routes |
|---|---|
| initial | all 11 named article types above |
| pre-review | Nature Medicine Article; Nature Communications Article; both npj Article routes |
| revision | all 11 named article types above |
| final-files | Nature Medicine; Nature Communications; Cancer Cell; Cell Reports Medicine; both npj routes |
| transfer | none; actual transfer offer and target portal must be profiled first |

The executable intake resolver does not guess aliases. A human may recognize the names in the table,
but must write the exact canonical `journal_id` and exact article-type label into the intake. For
`transfer`, follow `intake-transfer-and-human-review.md`: authenticate the offer, bind the explicit
target and target portal inventory, then re-profile against the target's `initial` contract. The
resolver returns `TRANSFER_REPROFILE_REQUIRED`, never a static transfer PASS or READY.

Radiology, The Lancet Digital Health, eClinicalMedicine, Advanced Science and JAMA Network Open do
not yet have a public-guide `final-files` contract. This is a published coverage boundary, not an
invitation to reuse another journal's route.

## Routing order

1. Normalize an exact canonical journal ID; do not stop at publisher family.
2. Resolve the journal's own article type. `Article`, `Original Investigation`, `Original Research`
   and `Research Article` are not interchangeable labels.
3. Resolve canonical `initial`, `pre-review`, `revision`, `transfer` or `final-files`. Preserve but
   normalize publisher labels such as acceptance-in-principle and Cell Press final submission.
4. Activate study-design branches: trial, diagnostic accuracy, prediction/AI, observational,
   systematic review, qualitative, biomarker, human/animal research, software or sensitive data.
5. Load current journal page, publisher policy and named form/checklist sources for that exact branch.
6. If the exact live portal adds a requirement, preserve it as `PORTAL_CURRENT` with the structured
   capture hash/date, exact journal/article/stage binding, screen label and concrete locator required
   by `source-authority-and-refresh.md`; never rewrite the general profile as though it applies to all
   submissions. A decision letter is
   reviewed separately and may motivate a validated registry/contract update, but it is never labeled
   `PORTAL_CURRENT` and cannot self-authorize a manifest exception.

## Family-boundary guards

- Nature Portfolio policy can establish shared reporting/data/ethics duties, but Nature Medicine's
  limits and MI-CLAIM-GEN wording do not automatically govern Nature Communications or an npj.
- Lancet-family common patterns do not erase the different form timing, word limits or special EPD
  requirement of The Lancet Digital Health and eClinicalMedicine.
- Cell Press production conventions do not erase Cancer Cell versus Cell Reports Medicine limits or
  the latter's `Limitations of the study` requirement.
- Wiley portfolio guidance cannot supply an Advanced Science-specific file extension or hard limit
  that the current Advanced Science page or portal does not state.
- Published articles only generate `OBSERVED_EXEMPLAR` advice. They can never make a manifest row
  `required`, `conditional` or `portal-only`.

## Fail-closed fallback

If no exact profile resolves, perform only journal-neutral inventory and byte-level checks and return
`TARGET_UNRESOLVED`. If a decisive current rule cannot be refreshed, return
`UNVERIFIED_CURRENT_GUIDE` and keep readiness `INCOMPLETE`.
