#!/usr/bin/env python3
"""Regression tests for audit_submission_package.py.

The production auditor deliberately requires a real PDF parser, so the test
fixtures use pypdf to create structurally valid baseline PDFs.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import struct
import subprocess
import sys
import tarfile
import tempfile
import unittest
import zipfile
from pathlib import Path

from pypdf import PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject


SCRIPT = Path(__file__).with_name("audit_submission_package.py")
HEADERS = [
    "schema_version", "project_id", "study_scope", "project_state_digest",
    "modality_role_digest", "scientific_handoff_packet_digest",
    "scientific_prereview_receipt_digest", "source_artifact_id", "analysis_lock_digest",
    "claim_registry_digest", "response_package_digest", "item_id", "journal_id",
    "article_type", "submission_stage",
    "study_design", "review_model", "material", "requirement_class", "condition", "rule_id", "authority_class",
    "source_url", "guide_verified_on", "path", "expected_extensions", "version",
    "sha256", "blinded", "tracked_changes_policy", "revision_variant", "status", "technical_qa", "render_qa", "content_gate",
    "anonymization_qa", "crossfile_qa", "owner", "not_applicable_reason", "notes",
]


def make_docx(
    path: Path, *, text: str = "Complete manuscript", tracked: bool = False,
    creator: str = "", macro: bool = False,
) -> None:
    change = "<w:ins><w:r><w:t>changed</w:t></w:r></w:ins>" if tracked else ""
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body><w:p><w:r><w:t>{text}</w:t></w:r>{change}</w:p></w:body></w:document>"
    )
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "[Content_Types].xml",
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Override PartName="/word/document.xml" '
            'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            '</Types>',
        )
        archive.writestr(
            "_rels/.rels",
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" '
            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
            'Target="word/document.xml"/>'
            '</Relationships>',
        )
        archive.writestr("word/document.xml", document)
        if creator:
            archive.writestr(
                "docProps/core.xml",
                '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
                'xmlns:dc="http://purl.org/dc/elements/1.1/">'
                f"<dc:creator>{creator}</dc:creator><cp:lastModifiedBy>{creator}</cp:lastModifiedBy>"
                "</cp:coreProperties>",
            )
        if macro:
            archive.writestr("word/vbaProject.bin", b"macro")


def make_alt_namespace_docx(path: Path, *, utf16_placeholder: bool = False) -> None:
    word_ns = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    text = "TODO add result" if utf16_placeholder else "Complete manuscript"
    document = (
        '<?xml version="1.0" encoding="UTF-16"?>' if utf16_placeholder
        else '<?xml version="1.0" encoding="UTF-8"?>'
    ) + (
        f'<x:document xmlns:x="{word_ns}"><x:body><x:p><x:r><x:t>{text}</x:t></x:r>'
        '<x:ins><x:r><x:t>changed</x:t></x:r></x:ins>'
        '<x:commentRangeStart x:id="0"/></x:p></x:body></x:document>'
    )
    document_bytes = document.encode("utf-16" if utf16_placeholder else "utf-8")
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(
            "[Content_Types].xml",
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Override PartName="/word/document.xml" '
            'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            '</Types>',
        )
        archive.writestr(
            "_rels/.rels",
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" '
            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
            'Target="word/document.xml"/>'
            '</Relationships>',
        )
        archive.writestr("word/document.xml", document_bytes)
        archive.writestr(
            "word/comments.xml",
            f'<q:comments xmlns:q="{word_ns}"><q:comment q:id="0"><q:p/></q:comment></q:comments>',
        )
        archive.writestr(
            "docProps/core.xml",
            '<c:coreProperties xmlns:c="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:d="http://purl.org/dc/elements/1.1/">'
            '<d:creator>Named Author</d:creator><c:lastModifiedBy>Named Author</c:lastModifiedBy>'
            '</c:coreProperties>',
        )


def make_pdf(path: Path, *, width: float = 72, height: float = 72) -> None:
    writer = PdfWriter()
    writer.add_blank_page(width=width, height=height)
    with path.open("wb") as handle:
        writer.write(handle)


def make_pdf_with_xmp_creator(path: Path) -> None:
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    xmp = DecodedStreamObject()
    xmp.set_data(
        b'<?xpacket begin=""?>'
        b'<x:xmpmeta xmlns:x="adobe:ns:meta/">'
        b'<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">'
        b'<rdf:Description xmlns:dc="http://purl.org/dc/elements/1.1/">'
        b'<dc:creator><rdf:Seq><rdf:li>Jane Doe</rdf:li></rdf:Seq></dc:creator>'
        b'</rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'
    )
    xmp.update({NameObject("/Type"): NameObject("/Metadata"), NameObject("/Subtype"): NameObject("/XML")})
    writer.root_object[NameObject("/Metadata")] = writer._add_object(xmp)
    with path.open("wb") as handle:
        writer.write(handle)


def make_pdf_with_escaped_javascript(path: Path) -> None:
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R /OpenAction 4 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 72 72] >>",
        b"<< /S /Java#53cript /J#53 (app.alert\\(1\\)) >>",
    ]
    payload = bytearray(b"%PDF-1.7\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(payload))
        payload.extend(f"{index} 0 obj\n".encode("ascii"))
        payload.extend(obj + b"\nendobj\n")
    xref_offset = len(payload)
    payload.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    payload.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        payload.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    payload.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("ascii")
    )
    path.write_bytes(payload)


def make_unsupported_zip(path: Path) -> None:
    """Create a ZIP whose local and central headers declare method 99."""
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_STORED) as archive:
        archive.writestr("payload.txt", "bounded test payload")
    payload = bytearray(path.read_bytes())
    local = payload.find(b"PK\x03\x04")
    central = payload.find(b"PK\x01\x02")
    if local < 0 or central < 0:
        raise AssertionError("ZIP fixture lacks expected local/central headers")
    struct.pack_into("<H", payload, local + 8, 99)
    struct.pack_into("<H", payload, central + 10, 99)
    path.write_bytes(payload)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def base_row(path: str = "manuscript.docx", sha256: str = "") -> dict[str, str]:
    return {
        "schema_version": "2.5",
        "project_id": "TEST-PROJECT-001",
        "study_scope": "imaging-only",
        "project_state_digest": "d" * 64,
        "modality_role_digest": "e" * 64,
        "scientific_handoff_packet_digest": "f" * 64,
        "scientific_prereview_receipt_digest": "not-applicable",
        "source_artifact_id": "ART-MAIN",
        "analysis_lock_digest": "a" * 64,
        "claim_registry_digest": "b" * 64,
        "response_package_digest": "c" * 64,
        "item_id": "MAIN",
        "journal_id": "radiology",
        "article_type": "Original Research",
        "submission_stage": "initial",
        "study_design": "observational",
        "review_model": "double-anonymized",
        "material": "anonymous main manuscript",
        "requirement_class": "required",
        "condition": "all submissions",
        "rule_id": "RAD-INITIAL-MAIN",
        "authority_class": "JOURNAL_GUIDE",
        "source_url": "https://pubs.rsna.org/page/radiology/author-instructions",
        "guide_verified_on": "2026-08-22",
        "path": path,
        "expected_extensions": ".docx",
        "version": "v1.0",
        "sha256": sha256,
        "blinded": "false",
        "tracked_changes_policy": "prohibited",
        "revision_variant": "not-applicable",
        "status": "ready",
        "technical_qa": "pass",
        "render_qa": "pass",
        "content_gate": "pass",
        "anonymization_qa": "pass",
        "crossfile_qa": "pass",
        "owner": "author",
        "not_applicable_reason": "",
        "notes": "",
    }


def write_manifest(root: Path, rows: list[dict[str, str]]) -> None:
    with (root / "submission-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADERS)
        writer.writeheader()
        writer.writerows(rows)


def conditional_na(rule_id: str, material: str, source_url: str, *, blinded: str = "not-applicable") -> dict[str, str]:
    row = base_row("", "")
    row.update({
        "item_id": rule_id, "material": material, "requirement_class": "conditional",
        "condition": "condition assessed and not met", "rule_id": rule_id,
        "source_url": source_url, "expected_extensions": "", "version": "", "blinded": blinded,
        "tracked_changes_policy": "not-applicable", "status": "not-applicable",
        "technical_qa": "not-applicable", "render_qa": "not-applicable",
        "content_gate": "not-applicable", "anonymization_qa": "not-applicable",
        "crossfile_qa": "not-applicable", "not_applicable_reason": "triggering condition is absent",
        "notes": "; ".join([
            "na_attested_by=corresponding author",
            "na_attested_on=2026-08-22",
            f"na_rule_id={rule_id}",
            "na_basis=triggering condition is absent",
            f"na_decision_locator=private author attestation {rule_id}",
        ]),
    })
    return row


def portal_receipt(
    journal_id: str, article_type: str, stage: str, screen: str, locator: str,
    *, capture_sha256: str = "a" * 64,
) -> str:
    return "; ".join([
        f"portal_capture_sha256={capture_sha256}",
        "portal_capture_date=2026-08-22",
        f"portal_journal_id={journal_id}",
        f"portal_article_type={article_type}",
        f"portal_stage={stage}",
        f"portal_screen={screen}",
        f"portal_locator={locator}",
    ])


def complete_radiology_rows(root: Path) -> list[dict[str, str]]:
    source = "https://pubs.rsna.org/page/radiology/author-instructions"
    files = {
        "MAIN": ("manuscript.docx", "RAD-INITIAL-MAIN", "anonymous main manuscript", "true"),
        "TITLE": ("title-page.docx", "RAD-INITIAL-TITLE", "full title page", "false"),
    }
    rows: list[dict[str, str]] = []
    for item_id, (filename, rule_id, material, blinded) in files.items():
        path = root / filename
        make_docx(path)
        row = base_row(filename, digest(path))
        row.update({"item_id": item_id, "rule_id": rule_id, "material": material, "blinded": blinded})
        rows.append(row)
    cover = base_row("", "")
    cover.update({
        "item_id": "COVER", "rule_id": "RAD-INITIAL-COVER", "material": "cover letter content",
        "requirement_class": "portal-only", "expected_extensions": "", "version": "",
        "blinded": "not-applicable", "tracked_changes_policy": "not-applicable",
        "status": "portal-entry", "technical_qa": "not-applicable", "render_qa": "not-applicable",
        "content_gate": "not-applicable", "anonymization_qa": "not-applicable",
        "crossfile_qa": "not-applicable",
    })
    rows.append(cover)
    rows.append(conditional_na("RAD-INITIAL-FIGURES", "combined figure review file", source, blinded="true"))
    acknowledgment = conditional_na(
        "RAD-ACK-PERM", "acknowledgment and permission forms",
        source,
        blinded="false",
    )
    rows.append(acknowledgment)
    rows.append(conditional_na("RAD-SUPP-DOC", "Supplemental File for Review", source, blinded="true"))
    rows.append(conditional_na("RAD-SUPP-MEDIA", "separate supplemental multimedia", source, blinded="true"))
    checklist_path = root / "reporting-checklist.docx"
    make_docx(checklist_path)
    checklist = base_row(checklist_path.name, digest(checklist_path))
    checklist.update({
        "item_id": "REPORTING", "rule_id": "RAD-REPORTING", "material": "reporting checklist",
        "requirement_class": "conditional", "condition": "observational study activates reporting standard",
        "blinded": "true",
    })
    rows.append(checklist)
    return rows


def complete_jno_rows(root: Path) -> list[dict[str, str]]:
    guide = "https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors"
    manuscript = root / "manuscript.docx"
    make_docx(manuscript)
    main = base_row(manuscript.name, digest(manuscript))
    main.update({
        "journal_id": "jama-network-open", "article_type": "Original Investigation",
        "rule_id": "JNO-MAIN", "material": "main manuscript", "source_url": guide,
        "blinded": "false", "review_model": "single-anonymized",
    })
    rows = [main]
    for rule_id, material in (
        ("JNO-SUPP", "supplement"),
        ("JNO-PROTOCOL", "protocol and SAP"),
        ("JNO-INIT-FIG-GRAPH", "separate initial graph or plot"),
        ("JNO-INIT-FIG-FLOW", "separate initial flow diagram"),
        ("JNO-INIT-FIG-ILLUS", "separate initial illustration"),
        ("JNO-INIT-FIG-PHOTO", "separate initial photographic or clinical image"),
        ("JNO-INIT-FIG-LINE", "separate initial line drawing"),
        ("JNO-INIT-FIG-MARKER-PAIR", "initial marked and unmarked figure-pair assertion"),
    ):
        row = conditional_na(rule_id, material, guide, blinded="false")
        row.update({
            "journal_id": "jama-network-open", "article_type": "Original Investigation",
            "review_model": "single-anonymized",
        })
        rows.append(row)
    checklist_path = root / "reporting-checklist.docx"
    make_docx(checklist_path)
    reporting = base_row(checklist_path.name, digest(checklist_path))
    reporting.update({
        "item_id": "REPORTING", "journal_id": "jama-network-open",
        "article_type": "Original Investigation", "rule_id": "JNO-REPORTING",
        "material": "reporting checklist", "requirement_class": "conditional",
        "condition": "observational study activates reporting standard", "source_url": guide,
        "blinded": "false", "review_model": "single-anonymized",
    })
    rows.append(reporting)
    return rows


def complete_jno_rows_with_marker_pair(root: Path) -> list[dict[str, str]]:
    guide = "https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors"
    rows = [
        row for row in complete_jno_rows(root)
        if row["rule_id"] not in {"JNO-INIT-FIG-PHOTO", "JNO-INIT-FIG-MARKER-PAIR"}
    ]
    marked_path = root / "figure1-marked.pdf"
    unmarked_path = root / "figure1-unmarked.pdf"
    make_pdf(marked_path, width=72)
    make_pdf(unmarked_path, width=73)
    pair_specs = [
        ("PHOTO-MARKED", marked_path),
        ("PHOTO-UNMARKED", unmarked_path),
    ]
    pair_file_rows: list[dict[str, str]] = []
    for item_id, path in pair_specs:
        row = base_row(path.name, digest(path))
        row.update({
            "item_id": item_id, "journal_id": "jama-network-open",
            "article_type": "Original Investigation", "review_model": "single-anonymized",
            "material": "separate initial photographic or clinical image",
            "requirement_class": "conditional",
            "condition": "photograph clinical image radiograph microscopy CT MRI or ultrasound figure is supplied as a separate initial-submission file",
            "rule_id": "JNO-INIT-FIG-PHOTO", "source_url": guide,
            "expected_extensions": ".pdf", "blinded": "false",
        })
        pair_file_rows.append(row)
    assertion = base_row("", "")
    assertion.update({
        "item_id": "PHOTO-PAIR", "journal_id": "jama-network-open",
        "article_type": "Original Investigation", "review_model": "single-anonymized",
        "material": "initial marked and unmarked figure-pair assertion",
        "requirement_class": "conditional",
        "condition": "photograph clinical image photomicrograph gel or similar image contains labels arrows or other markers",
        "rule_id": "JNO-INIT-FIG-MARKER-PAIR", "source_url": guide,
        "expected_extensions": "", "version": "", "blinded": "not-applicable",
        "tracked_changes_policy": "not-applicable", "status": "ready",
        "technical_qa": "not-applicable", "render_qa": "not-applicable",
        "content_gate": "pass", "anonymization_qa": "not-applicable",
        "crossfile_qa": "pass",
        "notes": "; ".join([
            "figure_pair_id=Figure 1",
            "marked_item_id=PHOTO-MARKED",
            "unmarked_item_id=PHOTO-UNMARKED",
            f"marked_sha256={pair_file_rows[0]['sha256']}",
            f"unmarked_sha256={pair_file_rows[1]['sha256']}",
            "pair_review_locator=private rendered pair review Figure 1",
        ]),
    })
    return [*rows, *pair_file_rows, assertion]


def complete_ncom_rows(root: Path) -> list[dict[str, str]]:
    guide = "https://www.nature.com/ncomms/submit/how-to-submit"
    main_path = root / "manuscript.docx"
    cover_path = root / "cover.docx"
    make_docx(main_path)
    make_docx(cover_path)
    main = base_row(main_path.name, digest(main_path))
    main.update({
        "journal_id": "nature-communications", "article_type": "Article",
        "rule_id": "NCOM-INITIAL-MAIN", "material": "combined manuscript",
        "source_url": guide, "blinded": "false", "review_model": "single-anonymized",
    })
    cover = base_row(cover_path.name, digest(cover_path))
    cover.update({
        "item_id": "COVER", "journal_id": "nature-communications", "article_type": "Article",
        "rule_id": "NCOM-COVER", "material": "cover letter", "authority_class": "PORTAL_CURRENT",
        "source_url": "https://mts-ncomms.nature.com/", "expected_extensions": ".docx",
        "blinded": "false", "review_model": "single-anonymized",
        "notes": portal_receipt(
            "nature-communications", "Article", "initial", "Cover Letter upload",
            "private audit receipt NCOM-cover-20260822",
        ),
    })
    rows = [main, cover]
    for rule_id, material in (
        ("NCOM-SI", "Supplementary Information"),
        ("NCOM-RELATED", "related manuscript copy"),
    ):
        row = conditional_na(rule_id, material, guide, blinded="false")
        row.update({
            "journal_id": "nature-communications", "article_type": "Article",
            "review_model": "single-anonymized",
        })
        rows.append(row)
    return rows


def complete_ncom_final_rows(root: Path) -> list[dict[str, str]]:
    source_path = root / "accepted-source.docx"
    make_docx(source_path, text="Title page with complete author and affiliation details")
    source = base_row(source_path.name, digest(source_path))
    source.update({
        "journal_id": "nature-communications", "article_type": "Article",
        "submission_stage": "final-files", "rule_id": "NCOM-FINAL-SOURCE",
        "material": "editable manuscript source",
        "source_url": "https://www.nature.com/ncomms/submit/article",
        "blinded": "false", "review_model": "double-anonymized",
    })
    rows = [source]
    for rule_id, material in (
        ("NCOM-FINAL-VECTOR", "separate final vector figures"),
        ("NCOM-FINAL-RASTER", "separate final raster figures"),
    ):
        row = conditional_na(
            rule_id, material, "https://www.nature.com/ncomms/submit/how-to-submit",
        )
        row.update({
            "journal_id": "nature-communications", "article_type": "Article",
            "submission_stage": "final-files", "review_model": "double-anonymized",
        })
        rows.append(row)
    return rows


def complete_cancer_cell_final_rows(
    root: Path, *, source_mode: str = "word",
) -> list[dict[str, str]]:
    final_guide = "https://www.cell.com/cancer-cell/information-for-authors/final-submission"
    revision_guide = "https://www.cell.com/cancer-cell/information-for-authors/revise-manuscript"
    source_rows: list[dict[str, str]] = []
    if source_mode == "word":
        source_path = root / "accepted-source.docx"
        make_docx(source_path, text="Complete accepted manuscript with STAR Methods")
        source_specs = [(source_path, ".docx", "")]
    elif source_mode == "latex-only":
        source_path = root / "accepted-source.tex"
        source_path.write_text(
            "\\documentclass{article}\\begin{document}Complete accepted manuscript\\end{document}",
            encoding="utf-8",
        )
        source_specs = [(source_path, ".tex", "Complete dependency and compilation crosswalk recorded")]
    elif source_mode == "latex-plus-pdf":
        source_path = root / "accepted-source.tex"
        source_path.write_text(
            "\\documentclass{article}\\begin{document}Complete accepted manuscript\\end{document}",
            encoding="utf-8",
        )
        checked_pdf = root / "accepted-source-checked.pdf"
        make_pdf(checked_pdf)
        source_sha = digest(source_path)
        checked_pdf_sha = digest(checked_pdf)
        shared_receipt = (
            f"latex_source_set_sha256={'b' * 64}; "
            f"latex_dependency_manifest_sha256={'c' * 64}; "
            f"latex_compile_receipt_sha256={'d' * 64}; "
            "latex_dependency_manifest_locator=private dependency manifest CC-latex-20260822; "
            "latex_compile_receipt_locator=private isolated compile receipt CC-latex-20260822"
        )
        source_specs = [
            (
                source_path, ".tex",
                f"latex_checked_pdf_sha256={checked_pdf_sha}; {shared_receipt}",
            ),
            (
                checked_pdf, ".pdf",
                f"latex_source_tex_sha256={source_sha}; {shared_receipt}",
            ),
        ]
    else:
        raise ValueError(f"Unsupported source_mode: {source_mode}")

    for index, (path, extension, notes) in enumerate(source_specs, start=1):
        source = base_row(path.name, digest(path))
        source.update({
            "item_id": f"SOURCE-{index}", "journal_id": "cancer-cell",
            "article_type": "Research Article", "submission_stage": "final-files",
            "review_model": "single-anonymized", "rule_id": "CC-FINAL-SOURCE",
            "material": "editable manuscript source bundle", "source_url": final_guide,
            "expected_extensions": extension, "blinded": "false", "notes": notes,
        })
        source_rows.append(source)

    star = base_row("", "")
    star.update({
        "item_id": "STAR", "journal_id": "cancer-cell", "article_type": "Research Article",
        "submission_stage": "final-files", "review_model": "single-anonymized",
        "material": "STAR Methods", "rule_id": "CC-STAR", "source_url": revision_guide,
        "expected_extensions": "", "version": "", "blinded": "false",
        "tracked_changes_policy": "not-applicable", "status": "ready",
        "technical_qa": "not-applicable", "render_qa": "not-applicable",
        "content_gate": "pass", "anonymization_qa": "not-applicable",
        "crossfile_qa": "pass", "notes": "STAR Methods section in accepted source; section locator verified",
    })

    krt = conditional_na("CC-KRT", "Key Resources Table", revision_guide, blinded="false")
    krt.update({
        "journal_id": "cancer-cell", "article_type": "Research Article",
        "submission_stage": "final-files", "review_model": "single-anonymized",
    })
    figures = conditional_na(
        "CC-FINAL-FIGURES", "separate final main figures", final_guide, blinded="false",
    )
    figures.update({
        "journal_id": "cancer-cell", "article_type": "Research Article",
        "submission_stage": "final-files", "review_model": "single-anonymized",
    })

    graphical_abstract_path = root / "graphical-abstract.pdf"
    highlights_path = root / "highlights.docx"
    make_pdf(graphical_abstract_path)
    make_docx(highlights_path, text="Highlight one. eTOC summary.")
    graphical_abstract = base_row(graphical_abstract_path.name, digest(graphical_abstract_path))
    graphical_abstract.update({
        "item_id": "GA", "journal_id": "cancer-cell", "article_type": "Research Article",
        "submission_stage": "final-files", "review_model": "single-anonymized",
        "material": "graphical abstract", "rule_id": "CC-GA", "source_url": final_guide,
        "expected_extensions": ".pdf", "blinded": "false",
    })
    highlights = base_row(highlights_path.name, digest(highlights_path))
    highlights.update({
        "item_id": "HIGHLIGHTS", "journal_id": "cancer-cell",
        "article_type": "Research Article", "submission_stage": "final-files",
        "review_model": "single-anonymized", "material": "Highlights and eTOC",
        "rule_id": "CC-HIGHLIGHTS", "source_url": final_guide,
        "expected_extensions": ".docx", "blinded": "false",
    })
    return [*source_rows, star, krt, figures, graphical_abstract, highlights]


def write_manifest_with_headers(
    root: Path, rows: list[dict[str, str]], headers: list[str],
) -> None:
    with (root / "submission-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)


def run_audit(
    root: Path, *, scope: str = "upload-root", route_matrix: Path | None = None,
    evidence: Path | None = None,
) -> tuple[int, dict[str, object]]:
    command = [
        sys.executable, str(SCRIPT), str(root), "--submission-mode", "--scope", scope,
        "--as-of", "2026-08-22",
    ]
    if route_matrix is not None:
        command.extend(["--route-matrix", str(route_matrix)])
    if evidence is not None:
        command.extend(["--evidence", str(evidence)])
    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return completed.returncode, json.loads(completed.stdout)


def codes(report: dict[str, object]) -> set[str]:
    return {str(item["code"]) for item in report["findings"]}  # type: ignore[index]


class PackageAuditTests(unittest.TestCase):
    def test_valid_minimal_closed_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_radiology_rows(root))
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertEqual("PASS", report["status"])
            self.assertEqual("INVENTORY_CLOSED", report["inventory"]["coverage"])
            self.assertTrue(any("Minimum-material-contract PASS" in item for item in report["limitations"]))
            self.assertEqual("PASS", report["route"]["minimum_material_contract"])
            self.assertNotIn("closure", report["route"])
            self.assertTrue(report["evidence_registry"]["substance_bound_to_bundled_registry"])
            self.assertEqual(64, len(report["evidence_registry"]["sha256"]))
            self.assertEqual(64, len(report["route_contract_registry"]["sha256"]))
            self.assertFalse(report["route_contract_registry"]["custom_route_matrix_allowed"])
            self.assertEqual("HUMAN_GATES_REQUIRED", report["whole_package_readiness"])

    def test_upstream_foreign_key_receipts_are_exposed_without_authentication_claim(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_radiology_rows(root))
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            provenance = report["upstream_provenance"]
            self.assertEqual(["TEST-PROJECT-001"], provenance["project_id"])
            self.assertEqual(["imaging-only"], provenance["study_scope"])
            self.assertEqual(["d" * 64], provenance["project_state_digest"])
            self.assertEqual(["e" * 64], provenance["modality_role_digest"])
            self.assertEqual(["f" * 64], provenance["scientific_handoff_packet_digest"])
            self.assertEqual(["not-applicable"], provenance["scientific_prereview_receipt_digest"])
            self.assertEqual(["a" * 64], provenance["analysis_lock_digest"])
            self.assertEqual(["b" * 64], provenance["claim_registry_digest"])
            self.assertEqual("NOT_PERFORMED", provenance["authentication"])

    def test_upstream_digest_mismatch_blocks_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            rows[-1]["claim_registry_digest"] = "d" * 64
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("CLAIM_REGISTRY_DIGEST_MIX", codes(report))

    def test_scientific_handoff_package_fields_require_one_consistent_value(self) -> None:
        cases = (
            ("study_scope", "mechanism-only", "STUDY_SCOPE_MIX"),
            ("project_state_digest", "1" * 64, "PROJECT_STATE_DIGEST_MIX"),
            ("modality_role_digest", "2" * 64, "MODALITY_ROLE_DIGEST_MIX"),
            (
                "scientific_handoff_packet_digest", "3" * 64,
                "SCIENTIFIC_HANDOFF_PACKET_DIGEST_MIX",
            ),
            (
                "scientific_prereview_receipt_digest", "4" * 64,
                "SCIENTIFIC_PREREVIEW_RECEIPT_DIGEST_MIX",
            ),
        )
        for field, changed_value, expected_code in cases:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                rows = complete_radiology_rows(root)
                rows[-1][field] = changed_value
                write_manifest(root, rows)
                code, report = run_audit(root)
                self.assertNotEqual(0, code, report)
                self.assertIn(expected_code, codes(report))

    def test_required_scientific_handoff_digests_reject_zero_sha256(self) -> None:
        for field in (
            "project_state_digest", "modality_role_digest", "scientific_handoff_packet_digest",
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                rows = complete_radiology_rows(root)
                for row in rows:
                    row[field] = "0" * 64
                write_manifest(root, rows)
                code, report = run_audit(root)
                self.assertNotEqual(0, code, report)
                self.assertIn("SCIENTIFIC_HANDOFF_DIGEST", codes(report))

    def test_scientific_prereview_receipt_accepts_na_or_nonzero_but_rejects_zero(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            for row in rows:
                row["scientific_prereview_receipt_digest"] = "4" * 64
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertEqual(
                ["4" * 64],
                report["upstream_provenance"]["scientific_prereview_receipt_digest"],
            )
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            for row in rows:
                row["scientific_prereview_receipt_digest"] = "0" * 64
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("SCIENTIFIC_PREREVIEW_RECEIPT_DIGEST", codes(report))

    def test_study_scope_rejects_unknown_value(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            for row in rows:
                row["study_scope"] = "radiogenomics"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("STUDY_SCOPE", codes(report))

    def test_evidence_synthesis_scope_consumes_prereview_without_radiogenomics_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            for row in rows:
                row["study_scope"] = "evidence-synthesis"
                row["study_design"] = "systematic-review-meta-analysis"
                row["scientific_handoff_packet_digest"] = "not-applicable"
                row["scientific_prereview_receipt_digest"] = "4" * 64
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertEqual("PASS", report["status"])
            provenance = report["upstream_provenance"]
            self.assertEqual(["evidence-synthesis"], provenance["study_scope"])
            self.assertEqual(
                ["not-applicable"], provenance["scientific_handoff_packet_digest"],
            )
            self.assertEqual(
                ["4" * 64], provenance["scientific_prereview_receipt_digest"],
            )

    def test_evidence_synthesis_scope_rejects_radiogenomics_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            for row in rows:
                row["study_scope"] = "evidence-synthesis"
                row["study_design"] = "systematic-review-meta-analysis"
                row["scientific_handoff_packet_digest"] = "3" * 64
                row["scientific_prereview_receipt_digest"] = "4" * 64
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("EVIDENCE_SYNTHESIS_HANDOFF", codes(report))

    def test_evidence_synthesis_scope_requires_review_design_and_prereview_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            for row in rows:
                row["study_scope"] = "evidence-synthesis"
                row["scientific_handoff_packet_digest"] = "not-applicable"
                row["scientific_prereview_receipt_digest"] = "not-applicable"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            observed = codes(report)
            self.assertIn("EVIDENCE_SYNTHESIS_PREREVIEW", observed)
            self.assertIn("EVIDENCE_SYNTHESIS_DESIGN", observed)

    def test_physical_file_requires_stable_source_artifact_id(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            rows[0]["source_artifact_id"] = "bad artifact id with spaces"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("SOURCE_ARTIFACT_ID", codes(report))

    def test_valid_single_anonymized_jno_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_jno_rows(root))
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertEqual("PASS", report["status"])
            self.assertEqual(["single-anonymized"], report["route"]["review_model"])

    def test_jno_initial_photo_route_rejects_docx_container(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_jno_rows(root)
            rows = [row for row in rows if row["rule_id"] != "JNO-INIT-FIG-PHOTO"]
            wrong_photo = root / "clinical-image.docx"
            make_docx(wrong_photo, text="A Word container is not an initial clinical image file")
            photo = base_row(wrong_photo.name, digest(wrong_photo))
            photo.update({
                "item_id": "PHOTO", "journal_id": "jama-network-open",
                "article_type": "Original Investigation", "review_model": "single-anonymized",
                "material": "separate initial photographic or clinical image",
                "requirement_class": "conditional",
                "condition": "photograph clinical image radiograph microscopy CT MRI or ultrasound figure is supplied as a separate initial-submission file",
                "rule_id": "JNO-INIT-FIG-PHOTO",
                "source_url": "https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors",
                "expected_extensions": ".docx", "blinded": "false",
            })
            rows.append(photo)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("RULE_EXTENSIONS_MISMATCH", codes(report))

    def test_jno_marked_photo_without_pair_adjudication_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_jno_rows_with_marker_pair(root)
            rows = [row for row in rows if row["rule_id"] != "JNO-INIT-FIG-MARKER-PAIR"]
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            missing_messages = [
                str(item["message"]) for item in report["findings"]
                if item["code"] == "ROUTE_MATERIAL_MISSING"
            ]
            self.assertTrue(
                any("JNO-INIT-FIG-MARKER-PAIR" in message for message in missing_messages),
                report,
            )

    def test_jno_marked_unmarked_pair_receipt_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_jno_rows_with_marker_pair(root))
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertEqual("PASS", report["route"]["minimum_material_contract"])

    def test_jno_pair_assertion_rejects_a_generic_note(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_jno_rows_with_marker_pair(root)
            assertion = next(
                row for row in rows if row["rule_id"] == "JNO-INIT-FIG-MARKER-PAIR"
            )
            assertion["notes"] = "marked and unmarked images reviewed"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ROUTE_FIGURE_PAIR_RECEIPT", codes(report))

    def test_jno_pair_rule_cannot_mix_active_and_not_applicable_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_jno_rows_with_marker_pair(root)
            na_pair = next(
                row for row in complete_jno_rows(root)
                if row["rule_id"] == "JNO-INIT-FIG-MARKER-PAIR"
            )
            rows.append(na_pair)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ROUTE_CONDITIONAL_STATUS_MIX", codes(report))

    def test_ncom_related_manuscript_condition_can_be_adjudicated_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_ncom_rows(root))
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertNotIn("ROUTE_CURRENT_UNRESOLVED", codes(report))

    def test_conditional_na_requires_dated_human_attestation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_ncom_rows(root)
            related = next(row for row in rows if row["rule_id"] == "NCOM-RELATED")
            related["notes"] = "condition reviewed"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("CONDITIONAL_NA_ATTESTATION", codes(report))
            self.assertEqual("FAIL", report["route"]["minimum_material_contract"])

    def test_ncom_named_final_source_is_not_forced_to_remain_double_blinded(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_ncom_final_rows(root))
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertNotIn("DOUBLE_BLIND_FILE", codes(report))

    def test_ncom_word_container_cannot_replace_required_final_raster_tiff(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_ncom_final_rows(root)
            rows = [row for row in rows if row["rule_id"] != "NCOM-FINAL-RASTER"]
            fake_raster = root / "raster-figure.docx"
            make_docx(fake_raster, text="A Word container is not a final raster figure")
            raster = base_row(fake_raster.name, digest(fake_raster))
            raster.update({
                "item_id": "RASTER", "journal_id": "nature-communications",
                "article_type": "Article", "submission_stage": "final-files",
                "review_model": "double-anonymized", "material": "separate final raster figures",
                "requirement_class": "conditional", "condition": "photographic or bitmapped figures exist",
                "rule_id": "NCOM-FINAL-RASTER",
                "source_url": "https://www.nature.com/ncomms/submit/how-to-submit",
                "expected_extensions": ".docx", "blinded": "false",
            })
            rows.append(raster)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("RULE_EXTENSIONS_MISMATCH", codes(report))
            self.assertEqual("FAIL", report["route"]["minimum_material_contract"])

    def test_lancet_raster_route_rejects_flowchart_docx(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            wrong_raster = root / "raster-figure.docx"
            make_docx(wrong_raster, text="Flowchart container mislabeled as a raster figure")
            row = base_row(wrong_raster.name, digest(wrong_raster))
            row.update({
                "item_id": "RASTER", "journal_id": "lancet-digital-health",
                "article_type": "Article", "submission_stage": "initial",
                "review_model": "single-anonymized", "material": "raster figure files",
                "requirement_class": "conditional",
                "condition": "raster photographic or clinical image figure exists",
                "rule_id": "TLDH-FIG-RASTER",
                "source_url": "https://www.thelancet.com/pb-assets/Lancet/authors/tldh-info-for-authors.pdf",
                "expected_extensions": ".docx", "blinded": "false",
            })
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("RULE_EXTENSIONS_MISMATCH", codes(report))
            self.assertEqual("FAIL", report["route"]["minimum_material_contract"])

    def test_cancer_cell_final_word_source_alternative_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_cancer_cell_final_rows(root, source_mode="word"))
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertEqual("PASS", report["route"]["minimum_material_contract"])

    def test_cancer_cell_lone_tex_source_is_incomplete(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_cancer_cell_final_rows(root, source_mode="latex-only"))
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ROUTE_FILE_SET_ALTERNATIVE", codes(report))
            self.assertEqual("FAIL", report["route"]["minimum_material_contract"])

    def test_cancer_cell_tex_plus_checked_pdf_alternative_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_cancer_cell_final_rows(root, source_mode="latex-plus-pdf"))
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertEqual("PASS", report["route"]["minimum_material_contract"])

    def test_cancer_cell_tex_plus_pdf_without_crosslinked_receipts_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_cancer_cell_final_rows(root, source_mode="latex-plus-pdf")
            for row in rows:
                if row["rule_id"] == "CC-FINAL-SOURCE":
                    row["notes"] = "dependency and compilation reviewed"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ROUTE_LATEX_RECEIPT", codes(report))
            self.assertEqual("FAIL", report["route"]["minimum_material_contract"])

    def test_cancer_cell_latex_receipt_rejects_duplicate_keys(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_cancer_cell_final_rows(root, source_mode="latex-plus-pdf")
            source = next(row for row in rows if row["path"].endswith(".tex"))
            source["notes"] += f"; latex_compile_receipt_sha256={'e' * 64}"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ROUTE_LATEX_RECEIPT", codes(report))

    def test_required_embedded_content_cannot_leave_human_gates_open(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_cancer_cell_final_rows(root, source_mode="word")
            star = next(row for row in rows if row["rule_id"] == "CC-STAR")
            star.update({
                "status": "pending-author", "content_gate": "not-checked",
                "crossfile_qa": "not-checked", "notes": "",
            })
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            observed = codes(report)
            self.assertIn("EMBEDDED_ITEM_OPEN", observed)
            self.assertIn("EMBEDDED_LOCATOR", observed)
            self.assertIn("EMBEDDED_QA", observed)
            self.assertEqual("FAIL", report["route"]["minimum_material_contract"])

    def test_custom_evidence_cannot_rewrite_rule_substance(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_radiology_rows(root))
            source = SCRIPT.parents[1] / "references" / "journal-requirements-evidence.tsv"
            custom = root / "evidence.tsv"
            payload = source.read_text(encoding="utf-8")
            custom.write_text(payload.replace(".doc;.docx", ".exe;.docx", 1), encoding="utf-8")
            code, report = run_audit(root, evidence=custom)
            self.assertNotEqual(0, code, report)
            self.assertIn("RULE_REGISTRY", codes(report))

    def test_study_design_other_alone_cannot_bypass_conditional_routes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            for row in rows:
                row["study_design"] = "other"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("STUDY_DESIGN_OTHER_UNRESOLVED", codes(report))

    def test_duplicate_manifest_header_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            write_manifest_with_headers(root, rows, [*HEADERS, "notes"])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertTrue({"DUPLICATE_HEADERS", "HEADERS"} & codes(report), report)

    def test_reordered_manifest_headers_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            reordered = [HEADERS[1], HEADERS[0], *HEADERS[2:]]
            write_manifest_with_headers(root, rows, reordered)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertTrue({"HEADER_ORDER", "HEADERS"} & codes(report), report)

    def test_manifest_row_with_extra_value_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(sha256=digest(manuscript))
            with (root / "submission-manifest.csv").open("w", encoding="utf-8", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(HEADERS)
                writer.writerow([row.get(header, "") for header in HEADERS] + ["hidden-extra-value"])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ROW_WIDTH", codes(report))

    def test_manifest_cannot_self_refresh_registry_date(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            rows[0]["guide_verified_on"] = "2026-08-21"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("RULE_DATE_MISMATCH", codes(report))

    def test_missing_route_required_materials_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(sha256=digest(manuscript))
            row["blinded"] = "true"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("ROUTE_MATERIAL_MISSING", codes(report))

    def test_attachment_set_never_gets_whole_package_ready(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(sha256=digest(manuscript))
            row["blinded"] = "true"
            write_manifest(root, [row])
            _, report = run_audit(root, scope="attachment-set")
            self.assertEqual("ATTACHMENT_SET_CLOSED", report["inventory"]["coverage"])
            self.assertNotIn(report["readiness_hint"], {"READY", "STRUCTURAL_GATES_PASS"})
            self.assertEqual("BLOCKED_STRUCTURAL", report["whole_package_readiness"])
            self.assertIn("ROUTE_MATERIAL_MISSING", codes(report))

    def test_structurally_passing_attachment_set_remains_incomplete_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, complete_radiology_rows(root))
            code, report = run_audit(root, scope="attachment-set")
            self.assertEqual(0, code, report)
            self.assertEqual("PASS", report["status"])
            self.assertEqual("ATTACHMENT_SET_CLOSED", report["inventory"]["coverage"])
            self.assertEqual("INCOMPLETE_SCOPE", report["whole_package_readiness"])
            self.assertNotEqual("READY", report["whole_package_readiness"])

    def test_cross_journal_rule_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(sha256=digest(manuscript))
            row.update({"journal_id": "cancer-cell", "article_type": "Research Article"})
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("RULE_JOURNAL_MISMATCH", codes(report))

    def test_family_proxy_cannot_satisfy_npj_final_figure_rule(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source_file = root / "accepted-source.docx"
            borrowed_file = root / "borrowed-ncom-rule.docx"
            make_docx(source_file)
            make_docx(borrowed_file)
            npj_source = base_row("accepted-source.docx", digest(source_file))
            npj_source.update({
                "journal_id": "npj-digital-medicine", "article_type": "Article",
                "submission_stage": "final-files", "material": "editable manuscript source",
                "rule_id": "NPJDM-FINAL-SOURCE", "source_url":
                "https://www.nature.com/npjdigitalmed/for-authors-and-referees/submisions",
                "expected_extensions": ".docx", "blinded": "false",
            })
            borrowed = base_row("borrowed-ncom-rule.docx", digest(borrowed_file))
            borrowed.update({
                "item_id": "BORROWED", "journal_id": "npj-digital-medicine",
                "article_type": "Article", "submission_stage": "final-files",
                "material": "borrowed sibling rule", "rule_id": "NCOM-FINAL-SOURCE",
                "source_url": "https://www.nature.com/ncomms/submit/article",
                "expected_extensions": ".docx", "blinded": "false",
            })
            write_manifest(root, [npj_source, borrowed])
            _, report = run_audit(root)
            self.assertIn("RULE_JOURNAL_MISMATCH", codes(report))
            self.assertIn("ROUTE_MATERIAL_MISSING", codes(report))

    def test_npj_revision_contract_cannot_omit_figure_portal_adjudication(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            row = base_row("", "")
            row.update({
                "item_id": "REVISION", "journal_id": "npj-digital-medicine",
                "article_type": "Article", "submission_stage": "revision",
                "review_model": "single-anonymized", "material": "revision package",
                "rule_id": "NPJDM-REV-PACKAGE",
                "source_url": "https://www.nature.com/npjdigitalmed/for-authors-and-referees/editorial-process",
                "expected_extensions": "", "version": "", "blinded": "false",
                "tracked_changes_policy": "not-applicable",
                "revision_variant": "not-applicable", "status": "pending-guide",
                "technical_qa": "not-applicable", "render_qa": "not-applicable",
                "content_gate": "not-applicable", "anonymization_qa": "not-applicable",
                "crossfile_qa": "not-applicable",
            })
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            missing_messages = [
                str(item["message"]) for item in report["findings"]
                if item["code"] == "ROUTE_MATERIAL_MISSING"
            ]
            self.assertTrue(
                any("NPJDM-REV-FIGURES" in message for message in missing_messages),
                report,
            )

    def test_cross_stage_rule_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(sha256=digest(manuscript))
            row["submission_stage"] = "revision"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("RULE_STAGE_MISMATCH", codes(report))

    def test_contract_membership_cannot_exempt_cross_stage_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            root = temp_root / "package"
            root.mkdir()
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(manuscript.name, digest(manuscript))
            row.update({
                "material": "clean and marked manuscripts", "rule_id": "RAD-REVISION",
                "submission_stage": "initial", "blinded": "true",
            })
            write_manifest(root, [row])
            route_matrix = temp_root / "cross-stage-route.json"
            route_matrix.write_text(
                json.dumps({
                    "schema_version": "1.0", "routes": [{
                        "journal_id": "radiology", "article_type": "Original Research",
                        "stage": "initial", "requirements": [{
                            "rule_id": "RAD-REVISION", "requirement_class": "required",
                            "item_kind": "file", "blinded": True,
                        }],
                    }],
                }),
                encoding="utf-8",
            )
            code, report = run_audit(root, route_matrix=route_matrix)
            self.assertNotEqual(0, code, report)
            self.assertTrue(
                {"RULE_STAGE_MISMATCH", "ROUTE_CONTRACT_STAGE_MISMATCH", "RULE_REGISTRY"}
                & codes(report),
                report,
            )

    def test_unknown_route_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(sha256=digest(manuscript))
            row["journal_id"] = "radiolgy"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("ROUTE_UNSUPPORTED", codes(report))

    def test_human_facing_qa_cannot_be_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            rows[0].update({"render_qa": "not-applicable", "content_gate": "not-applicable", "crossfile_qa": "not-applicable"})
            write_manifest(root, rows)
            _, report = run_audit(root)
            self.assertIn("QA_NOT_CLOSED", codes(report))

    def test_present_optional_file_requires_all_qa_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            main_path = root / "manuscript.docx"
            cover_path = root / "optional-cover.docx"
            make_docx(main_path)
            make_docx(cover_path)
            guide = "https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors"
            main = base_row("manuscript.docx", digest(main_path))
            main.update({
                "journal_id": "jama-network-open", "article_type": "Original Investigation",
                "rule_id": "JNO-MAIN", "material": "main manuscript", "source_url": guide,
                "blinded": "false",
            })
            rows = [main]
            for rule_id, material in (
                ("JNO-SUPP", "supplement"), ("JNO-PROTOCOL", "protocol and SAP"),
                ("JNO-REPORTING", "reporting checklist"),
            ):
                row = conditional_na(rule_id, material, guide, blinded="false")
                row.update({"journal_id": "jama-network-open", "article_type": "Original Investigation"})
                rows.append(row)
            cover = base_row("optional-cover.docx", digest(cover_path))
            cover.update({
                "item_id": "COVER", "journal_id": "jama-network-open",
                "article_type": "Original Investigation", "material": "cover letter",
                "requirement_class": "optional", "rule_id": "JNO-COVER", "source_url": guide,
                "expected_extensions": ".docx", "blinded": "false", "render_qa": "unavailable",
            })
            rows.append(cover)
            write_manifest(root, rows)
            _, report = run_audit(root)
            self.assertIn("QA_NOT_CLOSED", codes(report))

    def test_present_optional_file_requires_source_backed_extensions(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_jno_rows(root)
            cover_path = root / "optional-cover.docx"
            make_docx(cover_path)
            cover = base_row(cover_path.name, digest(cover_path))
            cover.update({
                "item_id": "COVER", "journal_id": "jama-network-open",
                "article_type": "Original Investigation", "material": "cover letter",
                "requirement_class": "optional", "rule_id": "JNO-COVER",
                "source_url": "https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors",
                "expected_extensions": "", "blinded": "false",
            })
            rows.append(cover)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("EXPECTED_EXTENSIONS", codes(report))

    def test_present_optional_file_cannot_self_declare_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_jno_rows(root)
            cover_path = root / "optional-cover.docx"
            make_docx(cover_path)
            cover = base_row(cover_path.name, digest(cover_path))
            cover.update({
                "item_id": "COVER", "journal_id": "jama-network-open",
                "article_type": "Original Investigation", "material": "cover letter",
                "requirement_class": "optional", "rule_id": "JNO-COVER",
                "source_url": "https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors",
                "expected_extensions": ".docx", "version": "", "blinded": "false",
                "status": "not-applicable", "technical_qa": "not-applicable",
                "render_qa": "not-applicable", "content_gate": "not-applicable",
                "anonymization_qa": "not-applicable", "crossfile_qa": "not-applicable",
            })
            rows.append(cover)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            observed = codes(report)
            self.assertIn("NOT_READY", observed)
            self.assertTrue({"VERSION", "VERSION_MISSING"} & observed, report)
            self.assertIn("QA_NOT_CLOSED", observed)

    def test_missing_required_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_manifest(root, [base_row(sha256="0" * 64)])
            code, report = run_audit(root)
            self.assertNotEqual(0, code)
            self.assertIn("FILE_MISSING", codes(report))

    def test_unmanifested_file_closes_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            (root / "forgotten.txt").write_text("not reviewed", encoding="utf-8")
            write_manifest(root, [base_row(sha256=digest(manuscript))])
            _, report = run_audit(root)
            self.assertIn("UNMANIFESTED_FILE", codes(report))

    def test_extension_signature_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake_pdf = root / "manuscript.pdf"
            fake_pdf.write_text("plain text wearing a PDF extension", encoding="utf-8")
            row = base_row("manuscript.pdf", digest(fake_pdf))
            row["expected_extensions"] = ".pdf"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("SIGNATURE_MISMATCH", codes(report))
            self.assertEqual("INVENTORY_CLOSED", report["inventory"]["coverage"])

    def test_manifest_cannot_expand_official_extension_rule(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.pdf"
            make_pdf(manuscript)
            row = base_row("manuscript.pdf", digest(manuscript))
            row.update({"expected_extensions": ".docx;.pdf", "blinded": "true"})
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("RULE_EXTENSIONS_MISMATCH", codes(report))

    def test_physical_file_with_no_public_extension_rule_needs_portal_capture(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            cover = root / "cover.docx"
            make_docx(cover)
            row = base_row("cover.docx", digest(cover))
            row.update({
                "item_id": "COVER", "journal_id": "cancer-cell",
                "article_type": "Research Article", "material": "cover letter",
                "rule_id": "CC-COVER", "source_url":
                "https://www.cell.com/cancer-cell/information-for-authors/submit-manuscript",
                "expected_extensions": ".docx", "blinded": "false",
            })
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("RULE_FILETYPE_UNRESOLVED", codes(report))

    def test_portal_override_needs_evidence_locator(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            cover = root / "cover.docx"
            make_docx(cover)
            row = base_row("cover.docx", digest(cover))
            row.update({
                "item_id": "COVER", "journal_id": "cancer-cell",
                "article_type": "Research Article", "material": "cover letter",
                "rule_id": "CC-COVER", "authority_class": "PORTAL_CURRENT",
                "source_url": "https://www.editorialmanager.com/cancer-cell/",
                "expected_extensions": ".docx", "blinded": "false", "notes": "",
            })
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("PORTAL_EVIDENCE_LOCATOR", codes(report))
            self.assertIn("PORTAL_EVIDENCE_RECEIPT", codes(report))

    def test_portal_override_rejects_a_generic_self_authored_note(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            cover = root / "cover.docx"
            make_docx(cover)
            row = base_row(cover.name, digest(cover))
            row.update({
                "item_id": "COVER", "journal_id": "cancer-cell",
                "article_type": "Research Article", "material": "cover letter",
                "rule_id": "CC-COVER", "authority_class": "PORTAL_CURRENT",
                "source_url": "https://www.editorialmanager.com/cancer-cell/",
                "expected_extensions": ".docx", "blinded": "false",
                "review_model": "single-anonymized", "notes": "captured",
            })
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("PORTAL_EVIDENCE_RECEIPT", codes(report))

    def test_shared_publisher_portal_cannot_unlock_advanced_science(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            main = base_row(manuscript.name, digest(manuscript))
            main.update({
                "journal_id": "advanced-science", "article_type": "Research Article",
                "material": "manuscript accepted extension", "rule_id": "AS-MAIN-TYPE",
                "authority_class": "PORTAL_CURRENT",
                "source_url": "https://www.editorialmanager.com/cancer-cell/",
                "expected_extensions": ".docx", "blinded": "false",
                "notes": "Captured Cancer Cell portal screen; deliberately wrong target journal",
            })
            checklist = conditional_na(
                "AS-ML-CHECK", "Machine Learning Data Reporting Checklist",
                "https://onlinelibrary.wiley.com/products/journals/data-checklists-chemistry",
                blinded="false",
            )
            checklist.update({
                "journal_id": "advanced-science", "article_type": "Research Article",
                "authority_class": "PUBLISHER_POLICY",
            })
            write_manifest(root, [main, checklist])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertTrue(
                {"PORTAL_SOURCE_ROUTE", "PORTAL_SOURCE_HOST"} & codes(report),
                report,
            )

    def test_required_advanced_main_cannot_become_path_free_portal_item(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            checklist_path = root / "ml-checklist.docx"
            make_docx(checklist_path)
            main = base_row("", "")
            main.update({
                "journal_id": "advanced-science", "article_type": "Research Article",
                "material": "manuscript accepted extension", "requirement_class": "portal-only",
                "rule_id": "AS-MAIN-TYPE", "authority_class": "PORTAL_CURRENT",
                "source_url": "https://www.editorialmanager.com/cancer-cell/",
                "expected_extensions": "", "version": "", "blinded": "not-applicable",
                "tracked_changes_policy": "not-applicable", "status": "portal-entry",
                "technical_qa": "not-applicable", "render_qa": "not-applicable",
                "content_gate": "not-applicable", "anonymization_qa": "not-applicable",
                "crossfile_qa": "not-applicable",
                "notes": "Wrong-journal portal capture used to test fail-closed class binding",
            })
            checklist = base_row(checklist_path.name, digest(checklist_path))
            checklist.update({
                "item_id": "ML", "journal_id": "advanced-science",
                "article_type": "Research Article", "material": "Machine Learning Data Reporting Checklist",
                "requirement_class": "conditional", "condition": "machine-learning research",
                "rule_id": "AS-ML-CHECK", "authority_class": "PUBLISHER_POLICY",
                "source_url": "https://onlinelibrary.wiley.com/products/journals/data-checklists-chemistry",
                "expected_extensions": ".docx", "blinded": "false",
            })
            write_manifest(root, [main, checklist])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            observed = codes(report)
            self.assertIn("ROUTE_CLASS_MISMATCH", observed)

    def test_required_cannot_be_not_applicable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            row = base_row("", "")
            row.update({
                "status": "not-applicable", "technical_qa": "not-applicable",
                "render_qa": "not-applicable", "content_gate": "not-applicable",
                "anonymization_qa": "not-applicable", "crossfile_qa": "not-applicable",
            })
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("REQUIRED_NA", codes(report))

    def test_published_exemplar_cannot_create_hard_rule(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(sha256=digest(manuscript))
            row["authority_class"] = "PUBLISHED_EXEMPLAR"
            row["source_url"] = "https://pubs.rsna.org/doi/10.1148/radiol.240885"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("NONAUTHORITATIVE_HARD_RULE", codes(report))

    def test_pending_guide_cannot_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(sha256=digest(manuscript))
            row["status"] = "pending-guide"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("NOT_READY", codes(report))

    def test_placeholder_and_undeclared_tracked_changes_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript, text="TODO add result", tracked=True)
            rows[0]["sha256"] = digest(manuscript)
            write_manifest(root, rows)
            _, report = run_audit(root)
            observed = codes(report)
            self.assertIn("PLACEHOLDER", observed)
            self.assertIn("DOCX_TRACKED_CHANGES", observed)
            self.assertEqual("FAIL", report["route"]["minimum_material_contract"])

    def test_initial_file_cannot_self_allow_marked_revision(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript, tracked=True)
            rows[0].update({
                "sha256": digest(manuscript),
                "tracked_changes_policy": "allowed-marked-revision",
                "revision_variant": "marked",
            })
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertTrue(
                {"DOCX_TRACKED_CHANGES", "MARKED_REVISION_UNAUTHORIZED", "TRACKED_POLICY_STAGE"}
                & codes(report),
                report,
            )

    def test_revision_contract_requires_distinct_semantic_roles(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows: list[dict[str, str]] = []
            for index in range(3):
                manuscript = root / f"clean-{index}.docx"
                make_docx(manuscript)
                row = base_row(manuscript.name, digest(manuscript))
                row.update({
                    "item_id": f"CLEAN-{index}", "submission_stage": "revision",
                    "material": "revision file", "rule_id": "RAD-REVISION", "blinded": "true",
                    "revision_variant": "clean",
                })
                rows.append(row)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ROUTE_REVISION_VARIANT_MISSING", codes(report))

    def test_required_revision_roles_cannot_share_identical_bytes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "clean.docx"
            make_docx(source)
            payload = source.read_bytes()
            rows: list[dict[str, str]] = []
            for variant in ("clean", "marked", "response"):
                path = root / f"{variant}.docx"
                path.write_bytes(payload)
                row = base_row(path.name, digest(path))
                row.update({
                    "item_id": variant.upper(), "submission_stage": "revision",
                    "material": variant, "rule_id": "RAD-REVISION", "blinded": "true",
                    "revision_variant": variant,
                    "tracked_changes_policy": "allowed-marked-revision" if variant == "marked" else "prohibited",
                })
                rows.append(row)
            source.unlink()
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ROUTE_REVISION_ROLE_DUPLICATE", codes(report))

    def test_blinded_docx_metadata_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript, creator="Named Author")
            row = base_row(sha256=digest(manuscript))
            row["blinded"] = "true"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("BLIND_METADATA", codes(report))

    def test_ooxml_namespace_prefixes_do_not_hide_comments_changes_or_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            manuscript = root / "manuscript.docx"
            make_alt_namespace_docx(manuscript)
            rows[0]["sha256"] = digest(manuscript)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            observed = codes(report)
            self.assertIn("DOCX_COMMENTS", observed)
            self.assertIn("DOCX_TRACKED_CHANGES", observed)
            self.assertIn("BLIND_METADATA", observed)

    def test_utf16_ooxml_placeholder_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            manuscript = root / "manuscript.docx"
            make_alt_namespace_docx(manuscript, utf16_placeholder=True)
            rows[0]["sha256"] = digest(manuscript)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("PLACEHOLDER", codes(report))

    def test_macro_bearing_ooxml_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript, macro=True)
            write_manifest(root, [base_row(sha256=digest(manuscript))])
            _, report = run_audit(root)
            self.assertIn("OFFICE_MACRO", codes(report))

    def test_pdf_without_eof_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.pdf"
            manuscript.write_bytes(b"%PDF-1.7\n1 0 obj\n<<>>\nendobj\n")
            row = base_row("manuscript.pdf", digest(manuscript))
            row["expected_extensions"] = ".pdf"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("PDF_INTEGRITY", codes(report))

    def test_pdf_magic_and_eof_do_not_replace_parser_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.pdf"
            manuscript.write_bytes(b"%PDF-1.7\nnonsense masquerading as objects\n%%EOF\n")
            row = base_row(manuscript.name, digest(manuscript))
            row["expected_extensions"] = ".pdf"
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("PDF_INTEGRITY", codes(report))

    def test_pdf_name_escaping_does_not_hide_javascript(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.pdf"
            make_pdf_with_escaped_javascript(manuscript)
            row = base_row(manuscript.name, digest(manuscript))
            row["expected_extensions"] = ".pdf"
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("PDF_ACTIVE_CONTENT", codes(report))

    def test_pdf_xmp_creator_is_an_identity_surface(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.pdf"
            make_pdf_with_xmp_creator(manuscript)
            row = base_row(manuscript.name, digest(manuscript))
            row.update({"expected_extensions": ".pdf", "blinded": "true"})
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("BLIND_PDF_METADATA", codes(report))

    def test_zip_parent_traversal_member_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive_path = root / "support.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("../outside.txt", "unsafe")
            row = base_row("support.zip", digest(archive_path))
            row["material"] = "supporting data archive"
            row["expected_extensions"] = ".zip"
            write_manifest(root, [row])
            _, report = run_audit(root)
            self.assertIn("ZIP_UNSAFE_PATH", codes(report))

    def test_duplicate_zip_member_blocks_before_ooxml_read(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            manuscript = root / "manuscript.docx"
            with zipfile.ZipFile(manuscript, "a", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr(
                    "word/document.xml",
                    '<x:document xmlns:x="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                    '<x:body><x:p><x:r><x:t>clean shadow</x:t></x:r></x:p></x:body></x:document>',
                )
            rows[0]["sha256"] = digest(manuscript)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("ZIP_DUPLICATE_MEMBER", codes(report))

    def test_backslash_ooxml_member_is_blocked_after_platform_normalization(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            manuscript = root / "manuscript.docx"
            with zipfile.ZipFile(manuscript, "a", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr(
                    "wordXdocument.xml",
                    '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body/></w:document>',
                )
            payload = manuscript.read_bytes()
            self.assertIn(b"wordXdocument.xml", payload)
            manuscript.write_bytes(payload.replace(b"wordXdocument.xml", b"word\\document.xml"))
            rows[0]["sha256"] = digest(manuscript)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            observed = codes(report)
            self.assertTrue(
                {"ZIP_DUPLICATE_MEMBER", "ZIP_UNSAFE_PATH", "ZIP_CANONICAL_COLLISION"} & observed,
                report,
            )

    def test_ooxml_main_part_needs_valid_opc_declarations(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            manuscript = root / "manuscript.docx"
            with zipfile.ZipFile(manuscript, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr(
                    "[Content_Types].xml",
                    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                    '<Override PartName="/word/document.xml" ContentType="application/octet-stream"/>'
                    '</Types>',
                )
                archive.writestr(
                    "_rels/.rels",
                    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                    '<Relationship Id="rId1" '
                    'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
                    'Target="word/document.xml"/></Relationships>',
                )
                archive.writestr(
                    "word/document.xml",
                    '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body/></w:document>',
                )
            rows[0]["sha256"] = digest(manuscript)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("OOXML_STRUCTURE", codes(report))

    def test_portal_only_ready_requires_exact_route_capture(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            cover = next(row for row in rows if row["rule_id"] == "RAD-INITIAL-COVER")
            cover["status"] = "ready"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("PORTAL_READY_UNPROVEN", codes(report))

    def test_unsupported_zip_compression_is_reported_without_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            archive_path = root / "support.zip"
            make_unsupported_zip(archive_path)
            row = base_row(archive_path.name, digest(archive_path))
            row.update({
                "journal_id": "nature-communications", "article_type": "Article",
                "material": "Supplementary Information", "requirement_class": "conditional",
                "condition": "supplementary content exists", "rule_id": "NCOM-SI",
                "source_url": "https://www.nature.com/ncomms/submit/how-to-submit",
                "expected_extensions": ".zip", "blinded": "false",
            })
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertTrue(
                {"ZIP_UNSUPPORTED", "ZIP_INTEGRITY"} & codes(report),
                report,
            )

    def test_text_validation_reads_the_complete_bounded_payload(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            support = root / "support.txt"
            support.write_bytes(b"a" * 2_100_000 + b"\xff")
            row = base_row(support.name, digest(support))
            row.update({
                "journal_id": "nature-communications", "article_type": "Article",
                "material": "Supplementary Information", "requirement_class": "conditional",
                "condition": "supplementary content exists", "rule_id": "NCOM-SI",
                "source_url": "https://www.nature.com/ncomms/submit/how-to-submit",
                "expected_extensions": ".txt", "blinded": "false",
                "review_model": "single-anonymized",
            })
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertTrue({"SIGNATURE_MISMATCH", "TYPE_UNVERIFIED"} & codes(report), report)

    def test_legacy_ole_magic_is_not_treated_as_a_valid_office_document(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.doc"
            manuscript.write_bytes(b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1" + b"\x00" * 2048)
            row = base_row(manuscript.name, digest(manuscript))
            row.update({
                "journal_id": "jama-network-open", "article_type": "Original Investigation",
                "rule_id": "JNO-MAIN", "material": "main manuscript",
                "source_url": "https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors",
                "expected_extensions": ".doc", "blinded": "false",
                "review_model": "single-anonymized",
            })
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("OLE_PARSE_UNAVAILABLE", codes(report))

    def test_unresolved_portal_rule_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            main = base_row(sha256=digest(manuscript))
            portal = base_row("", "")
            portal.update({
                "item_id": "PORTAL", "material": "live author attestation",
                "requirement_class": "portal-only", "rule_id": "PORTAL-RULE",
                "status": "pending-guide", "expected_extensions": "", "version": "",
                "blinded": "not-applicable", "technical_qa": "not-applicable",
                "render_qa": "not-applicable", "content_gate": "not-applicable",
                "anonymization_qa": "not-applicable", "crossfile_qa": "not-applicable",
            })
            write_manifest(root, [main, portal])
            _, report = run_audit(root)
            self.assertIn("PORTAL_GATE_OPEN", codes(report))

    def test_advanced_science_development_portal_cannot_resolve_guide(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            main = base_row("manuscript.docx", digest(manuscript))
            main.update({
                "journal_id": "advanced-science", "article_type": "Research Article",
                "material": "manuscript accepted extension", "rule_id": "AS-MAIN-TYPE",
                "authority_class": "PORTAL_CURRENT",
                "source_url": "https://www.editorialmanager.com/advancedscience/default.aspx",
                "expected_extensions": ".docx", "blinded": "false",
                "notes": "Public page inspected 2026-08-22; it says the site is under development",
            })
            checklist = conditional_na(
                "AS-ML-CHECK", "Machine Learning Data Reporting Checklist",
                "https://onlinelibrary.wiley.com/products/journals/data-checklists-chemistry",
                blinded="false",
            )
            checklist.update({
                "journal_id": "advanced-science", "article_type": "Research Article",
                "authority_class": "PUBLISHER_POLICY",
            })
            write_manifest(root, [main, checklist])
            _, report = run_audit(root)
            observed = codes(report)
            self.assertTrue({"PORTAL_SOURCE_ROUTE", "PORTAL_SOURCE_HOST"} & observed, report)
            self.assertIn("ROUTE_CURRENT_UNRESOLVED", observed)

    def test_portal_placeholder_cannot_create_a_hard_file_rule(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manuscript = root / "manuscript.docx"
            make_docx(manuscript)
            row = base_row(manuscript.name, digest(manuscript))
            row.update({
                "journal_id": "advanced-science", "article_type": "Research Article",
                "material": "manuscript accepted extension", "rule_id": "AS-MAIN-TYPE",
                "authority_class": "PORTAL_PLACEHOLDER",
                "source_url": "https://www.editorialmanager.com/advancedscience/default.aspx",
                "expected_extensions": ".docx", "blinded": "false",
            })
            write_manifest(root, [row])
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("NONAUTHORITATIVE_HARD_RULE", codes(report))

    def test_cancer_cell_initial_does_not_require_revision_or_final_materials(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            main_path = root / "manuscript.docx"
            cover_path = root / "cover.docx"
            doi_path = root / "declaration.pdf"
            make_docx(main_path)
            make_docx(cover_path)
            make_pdf(doi_path)
            guide = "https://www.cell.com/cancer-cell/information-for-authors/submit-manuscript"
            rows: list[dict[str, str]] = []
            for item_id, path, rule_id, material, expected in (
                ("MAIN", main_path, "CC-INITIAL-MAIN", "free-format manuscript", ".docx"),
                ("COVER", cover_path, "CC-COVER", "cover letter", ".docx"),
                ("DOI", doi_path, "CC-DOI", "Declaration of Interests", ".pdf"),
            ):
                row = base_row(path.name, digest(path))
                row.update({
                    "item_id": item_id, "journal_id": "cancer-cell",
                    "article_type": "Research Article", "material": material, "rule_id": rule_id,
                    "source_url": guide, "expected_extensions": expected, "blinded": "false",
                })
                if item_id == "COVER":
                    row.update({
                        "authority_class": "PORTAL_CURRENT",
                        "source_url": "https://www.editorialmanager.com/cancer-cell/",
                        "notes": portal_receipt(
                            "cancer-cell", "Research Article", "initial", "Cover Letter upload",
                            "private audit receipt CC-cover-20260822",
                        ),
                    })
                rows.append(row)
            write_manifest(root, rows)
            _, report = run_audit(root)
            observed = codes(report)
            self.assertNotIn("CC-STAR", json.dumps(report))
            self.assertNotIn("CC-GA", json.dumps(report))
            self.assertNotIn("ROUTE_MATERIAL_MISSING", observed)

    def test_safe_uncompressed_tar_supplement_passes_preflight(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_ncom_rows(root)
            archive_path = root / "supplement.tar"
            payload = b"bounded supplementary data"
            with tarfile.open(archive_path, "w") as archive:
                member = tarfile.TarInfo("tables/table-s1.txt")
                member.size = len(payload)
                archive.addfile(member, io.BytesIO(payload))
            supplement = next(row for row in rows if row["rule_id"] == "NCOM-SI")
            supplement.update({
                "item_id": "SUPPLEMENT", "path": archive_path.name,
                "expected_extensions": ".tar", "version": "v1.0",
                "sha256": digest(archive_path), "status": "ready",
                "technical_qa": "pass", "render_qa": "not-applicable",
                "content_gate": "pass", "anonymization_qa": "not-applicable",
                "crossfile_qa": "pass", "source_artifact_id": "ART-SUPPLEMENT",
                "not_applicable_reason": "", "notes": "",
            })
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertEqual(0, code, report)
            self.assertNotIn("TAR_", " ".join(codes(report)))

    def test_tar_parent_traversal_member_is_blocked_without_extraction(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_ncom_rows(root)
            archive_path = root / "supplement.tar"
            payload = b"must never be extracted"
            with tarfile.open(archive_path, "w") as archive:
                member = tarfile.TarInfo("../escape.txt")
                member.size = len(payload)
                archive.addfile(member, io.BytesIO(payload))
            supplement = next(row for row in rows if row["rule_id"] == "NCOM-SI")
            supplement.update({
                "item_id": "SUPPLEMENT", "path": archive_path.name,
                "expected_extensions": ".tar", "version": "v1.0",
                "sha256": digest(archive_path), "status": "ready",
                "technical_qa": "pass", "render_qa": "not-applicable",
                "content_gate": "pass", "anonymization_qa": "not-applicable",
                "crossfile_qa": "pass", "source_artifact_id": "ART-SUPPLEMENT",
                "not_applicable_reason": "", "notes": "",
            })
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("TAR_UNSAFE_PATH", codes(report))

    def test_duplicate_structured_receipt_key_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_ncom_rows(root)
            cover = next(row for row in rows if row["rule_id"] == "NCOM-COVER")
            cover["notes"] += "; portal_journal_id=evil-journal"
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("PORTAL_EVIDENCE_RECEIPT", codes(report))

    def test_manifest_parent_escape_is_rejected_before_receipt_or_read(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "package"
            root.mkdir()
            outside = base / "outside.csv"
            outside.write_text("secret,outside,manifest\n", encoding="utf-8")
            completed = subprocess.run(
                [
                    sys.executable, str(SCRIPT), str(root), "--submission-mode",
                    "--scope", "upload-root", "--as-of", "2026-08-22",
                    "--manifest", "../outside.csv",
                ],
                check=False, capture_output=True, text=True, encoding="utf-8",
            )
            report = json.loads(completed.stdout)
            self.assertNotEqual(0, completed.returncode, report)
            self.assertIn("MANIFEST_ESCAPE", codes(report))
            self.assertEqual("NOT_VERIFIED", report["manifest_receipt"]["state"])

    def test_ooxml_external_relationship_is_blocked_before_rendering(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            rows = complete_radiology_rows(root)
            main = next(row for row in rows if row["item_id"] == "MAIN")
            path = root / main["path"]
            with zipfile.ZipFile(path, "a", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr(
                    "word/_rels/document.xml.rels",
                    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                    '<Relationship Id="rRemote" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate" '
                    'TargetMode="External" Target="https://tracker.invalid/template.dotm"/>'
                    "</Relationships>",
                )
            main["sha256"] = digest(path)
            write_manifest(root, rows)
            code, report = run_audit(root)
            self.assertNotEqual(0, code, report)
            self.assertIn("OOXML_EXTERNAL_RELATIONSHIP", codes(report))


if __name__ == "__main__":
    unittest.main(verbosity=2)
