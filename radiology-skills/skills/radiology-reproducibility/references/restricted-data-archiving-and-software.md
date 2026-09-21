# Restricted Data, Software, Licensing and Archiving

Use for `package-plan` and `archive-handoff`.

## 1. Reproducible does not mean public

Classify each object separately: public, controlled-access, institutional, confidential, PHI,
licensed proprietary, export-controlled or unresolved. Record governing consent, DUA, data-use
certification, repository terms and transfer limits.

A restricted-data replay route may provide:

- dataset/release identifier and access application path;
- privacy-preserving manifest, schema, counts and content checksums where lawful;
- executable code/config/environment;
- an authorised secure compute location;
- synthetic/minimal fixture for installation and schema tests;
- expected output contract and an independent authorised operator.

A synthetic fixture can demonstrate mechanics, schema and smoke-test behaviour. It does not prove
that real-data results replay, preserve performance or retain clinical distributions.

Do not place identifiers, access tokens, secrets, signed URLs, small-cell disclosures, protected
metadata or trained derivatives with unresolved governance in a public manifest.

## 2. Minimum replay package

Use [minimum-replay-package-manifest.md](../templates/minimum-replay-package-manifest.md). Include:

1. CITATION and stable package/release identifier;
2. licence for code and separate rights/conditions for data, weights and third-party assets;
3. immutable source commit/release and dirty patch if applicable;
4. executable entrypoint and example command;
5. resolved configuration and environment/container digest;
6. input schema/manifest, inclusion rule, version and lawful access route;
7. seeds, determinism settings, weights/checkpoints and their identities;
8. expected outputs, tolerance and verification command;
9. run receipt schema and known failure/portability boundaries;
10. archive location, persistent identifier and relation to the article/grant/protocol.

Avoid copying a whole working directory as a package. Exclude caches, secrets, raw restricted data,
unrelated checkpoints and outputs that cannot be redistributed.

## 3. Licences and dependencies

Code, data, model weights, containers, vendor SDKs, fonts and reference assets can have different
licences. Record:

- licence name/version and canonical text/locator;
- copyright/ownership and redistribution/modification conditions;
- dependency lock and material transitive/proprietary components;
- whether a container redistributes software that the source repository merely references;
- incompatibilities or `LICENSE_UNRESOLVED`.

An open repository without an explicit licence does not automatically grant reuse rights. A licence
does not grant data-subject consent or override a DUA.

## 4. Archiving and citation

A mutable branch or repository URL is not an immutable archive. Freeze a release/snapshot with:

- persistent identifier such as a version DOI or another repository-supported PID;
- immutable commit/release and archive checksum;
- rich metadata linking software, data, article, authors/funders and related versions;
- version-specific citation, not only a concept/latest DOI;
- long-term repository and retention state;
- supersession/deprecation relation when repaired.

OCI images use content-addressable descriptors/digests; cite the digest and specification/runtime
context, not only a tag. W3C PROV can structure entity-activity-agent links, but adopting an ontology
does not itself create complete provenance.

## 5. Radiology minimum

- Maintain patient/exam/series/reconstruction/derived-object hierarchy with pseudonymous or hashed
  local keys and an authorised linkage table outside public artifacts.
- Record DICOM/NIfTI object identity, geometry/orientation, series-selection rules and preprocessing.
- Freeze annotation/segmentation, feature-definition, harmonisation and model-weight versions.
- Public sample images must be explicitly authorised and pixel/metadata de-identification verified.
- Vendor reconstruction or closed inference software needs product/version/configuration and
  portability limits; lack of source code narrows the achievable level.

## 6. Release verdict

- `ARCHIVE_READY`: identities, licences, restricted-data route, metadata, PID and replay contract
  are complete for the claimed public/controlled package.
- `ARCHIVE_CONDITIONAL`: a citable public shell is possible, but named objects remain controlled,
  proprietary or non-redistributable with a documented route.
- `STOP_LICENSE_OR_ARCHIVE`: licence conflict, secret/identifier exposure, mutable-only state or
  missing authority prevents release.

Archive readiness does not upgrade the computational evidence level. A perfectly archived package
may remain only `RERUNNABLE`.
