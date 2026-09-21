from __future__ import annotations

import re
import unittest
from pathlib import Path


REFERENCE = Path(__file__).resolve().parents[1] / "references" / "mask-geometry.md"


def geometry_decision(
    *,
    same_patient_exam: bool,
    source_reference_verified: bool,
    same_physical_space: bool,
    same_grid: bool,
    trusted_transform: bool,
    metadata_rewrite_only: bool = False,
) -> str:
    """Executable semantic oracle for the documented geometry gate."""
    if metadata_rewrite_only:
        return "STOP_FOR_REPAIR"
    if not same_patient_exam or not source_reference_verified:
        return "STOP_FOR_REPAIR"
    if same_physical_space:
        return "PASS" if same_grid else "RESAMPLE_CONDITIONAL"
    if trusted_transform:
        return "REGISTER_CONDITIONAL"
    return "STOP_FOR_REPAIR"


class MaskGeometrySemanticTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = REFERENCE.read_text(encoding="utf-8")

    def test_only_same_space_legitimate_grid_change_allows_simple_resampling(self) -> None:
        self.assertEqual(
            geometry_decision(
                same_patient_exam=True,
                source_reference_verified=True,
                same_physical_space=True,
                same_grid=False,
                trusted_transform=False,
            ),
            "RESAMPLE_CONDITIONAL",
        )
        self.assertEqual(
            geometry_decision(
                same_patient_exam=True,
                source_reference_verified=True,
                same_physical_space=False,
                same_grid=False,
                trusted_transform=True,
            ),
            "REGISTER_CONDITIONAL",
        )

    def test_unknown_identity_reference_or_transform_fails_closed(self) -> None:
        cases = [
            dict(same_patient_exam=False, source_reference_verified=True, same_physical_space=True,
                 same_grid=False, trusted_transform=False),
            dict(same_patient_exam=True, source_reference_verified=False, same_physical_space=True,
                 same_grid=False, trusted_transform=False),
            dict(same_patient_exam=True, source_reference_verified=True, same_physical_space=False,
                 same_grid=False, trusted_transform=False),
        ]
        for case in cases:
            with self.subTest(case=case):
                self.assertEqual(geometry_decision(**case), "STOP_FOR_REPAIR")

    def test_metadata_rewrite_never_repairs_alignment(self) -> None:
        self.assertEqual(
            geometry_decision(
                same_patient_exam=True,
                source_reference_verified=True,
                same_physical_space=True,
                same_grid=False,
                trusted_transform=False,
                metadata_rewrite_only=True,
            ),
            "STOP_FOR_REPAIR",
        )

    def test_documented_decision_table_matches_semantic_oracle(self) -> None:
        rows = {}
        for state, verdict in re.findall(
            r"^\| `([A-Z_]+)` \|.*?\| `([^`]+)` \|$", self.text, flags=re.MULTILINE
        ):
            rows[state] = verdict
        self.assertEqual(rows["SAME_SPACE_SAME_GRID"], "PASS")
        self.assertEqual(rows["SAME_SPACE_DIFFERENT_GRID"], "CONDITIONAL")
        self.assertEqual(rows["CROSS_SPACE_TRUSTED_TRANSFORM"], "CONDITIONAL")
        self.assertEqual(rows["IDENTITY_OR_TRANSFORM_UNKNOWN"], "STOP_FOR_REPAIR")
        self.assertEqual(rows["METADATA_REWRITE_ONLY"], "STOP_FOR_REPAIR")

    def test_receipt_and_per_case_qc_cover_required_evidence(self) -> None:
        required = (
            "referenced series/SOP",
            "transform ID/hash",
            "interpolator",
            "pre/post label counts and physical volumes",
            "axial, coronal and sagittal",
            "first/last occupied slices",
            "every transformed or imported case",
        )
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)


if __name__ == "__main__":
    unittest.main()
