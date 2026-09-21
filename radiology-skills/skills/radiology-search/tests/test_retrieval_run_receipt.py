#!/usr/bin/env python3
"""Executable success/failure regression for retrieval-run receipts."""

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_retrieval_run_receipt.py"
SPEC = importlib.util.spec_from_file_location("validate_retrieval_run_receipt", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RetrievalRunReceiptTests(unittest.TestCase):
    def fixture(self, root: Path) -> dict[str, object]:
        response = root / "pubmed-response.json"
        response.write_text('{"esearchresult":{"idlist":["1"]}}\n', encoding="utf-8")
        corpus = root / "corpus.csv"
        corpus.write_text("record_id,source_id,title\nREC-1,PMID:1,Fixture\n", encoding="utf-8")
        config = {
            "parser": "fixture-parser", "parser_version": "1.0",
            "dedup_order": ["DOI", "PMID", "TITLE"],
            "normalization_rules": ["unicode-nfkc", "casefold-title"],
            "limits": {"retmax": 100},
        }
        payload: dict[str, object] = {
            "schema_version": "1.0", "run_id": "RUN-001", "run_state": "EXECUTED",
            "executed_on": "2026-08-23T12:00:00Z",
            "question_or_protocol_sha256": "a" * 64,
            "execution_identity": {
                "provider": "NCBI", "tool": "E-utilities", "tool_version": "2026-08",
                "system_context_digest": "not-captured",
            },
            "sources": [{
                "source_id": "PubMed", "endpoint": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
                "query": "radiomics[Title/Abstract]", "filters": {"language": "English"},
                "sort": "pub date", "pagination_exhausted": True, "request_count": 1,
                "raw_result_count": 1, "outcome_state": "SUCCESS",
                "response_artifacts": [{"path": response.name, "sha256": MODULE.sha256_file(response)}],
            }],
            "retrieval_config": config, "retrieval_config_sha256": MODULE.digest(config),
            "corpus_manifest": {
                "path": corpus.name, "sha256": MODULE.sha256_file(corpus), "record_count": 1,
            },
            "evidence_contexts": [{
                "record_id": "REC-1", "evidence_level": "ABSTRACT",
                "source_locator": "PMID:1 abstract", "content_sha256": "b" * 64,
                "claim_ids": [],
            }],
            "index_identity": {
                "state": "CURRENT", "corpus_manifest_sha256": MODULE.sha256_file(corpus),
                "retrieval_config_sha256": MODULE.digest(config), "index_sha256": "c" * 64,
            },
            "failures": [], "update_triggers": ["before submission", "query change"],
            "coverage_claim": "COMPLETE_FOR_DECLARED_SOURCES", "receipt_sha256": "",
            "boundary": "Structural retrieval identity only; no scientific support claim.",
        }
        payload["receipt_sha256"] = MODULE.receipt_digest(payload)
        return payload

    def test_complete_hash_bound_receipt_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertEqual([], MODULE.validate(self.fixture(root), root))

    def test_query_and_configuration_tamper_fail(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = self.fixture(root)
            payload["sources"][0]["query"] = "changed query"
            payload["retrieval_config"]["limits"]["retmax"] = 10
            payload["receipt_sha256"] = MODULE.receipt_digest(payload)
            errors = MODULE.validate(payload, root)
            self.assertTrue(any("retrieval_config_sha256 mismatch" in error for error in errors))

    def test_partial_or_rate_limited_run_cannot_claim_complete_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = self.fixture(root)
            payload["run_state"] = "PARTIAL"
            payload["sources"][0]["outcome_state"] = "RATE_LIMITED"
            payload["sources"][0]["pagination_exhausted"] = False
            payload["failures"] = ["PubMed returned HTTP 429"]
            payload["receipt_sha256"] = MODULE.receipt_digest(payload)
            errors = MODULE.validate(payload, root)
            self.assertTrue(any("cannot claim complete coverage" in error for error in errors))
            self.assertTrue(any("requires every declared source" in error for error in errors))

    def test_current_index_must_bind_corpus_and_configuration(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = self.fixture(root)
            payload["index_identity"]["corpus_manifest_sha256"] = "d" * 64
            payload["receipt_sha256"] = MODULE.receipt_digest(payload)
            errors = MODULE.validate(payload, root)
            self.assertTrue(any("CURRENT index corpus digest mismatch" in error for error in errors))

    def test_physical_response_or_corpus_tamper_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            payload = self.fixture(root)
            (root / "pubmed-response.json").write_text("tampered\n", encoding="utf-8")
            (root / "corpus.csv").write_text("tampered\n", encoding="utf-8")
            errors = MODULE.validate(payload, root)
            self.assertTrue(any("response_artifacts" in error and "mismatch" in error for error in errors))
            self.assertTrue(any("corpus_manifest SHA-256 mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
