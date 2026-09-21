import csv
import io
import re
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCE = SKILL_ROOT / "references" / "dicom-deidentification.md"
COHORT_REFERENCE = SKILL_ROOT / "references" / "cohort-assembly-and-id-reconciliation.md"


class DicomDeidentificationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = REFERENCE.read_text(encoding="utf-8")
        cls.cohort_text = COHORT_REFERENCE.read_text(encoding="utf-8")

    def test_uid_actions_preserve_internal_references(self):
        for code in ("`X`", "`Z`", "`D`", "`K`", "`C`", "`U`"):
            self.assertIn(code, self.text)
        self.assertIn("non-zero UID that is internally consistent", self.text)
        self.assertIn("cross-instance referential consistency", self.text)
        self.assertNotIn("header tags removed (incl. private/UIDs)", self.text)

    def test_arbitrary_pixel_sample_is_not_release_qa(self):
        self.assertIn("entire release surface", self.text)
        self.assertIn("must not replace full automated inventory", self.text)
        self.assertIn("A casual visual sample", self.text)

    def test_deidentification_declaration_is_recorded_but_verified(self):
        self.assertIn("Patient Identity Removed (0012,0062)", self.text)
        self.assertIn("substitute for verification", " ".join(self.text.split()))

    def test_entrypoint_does_not_claim_absolute_pixel_phi_absence(self):
        skill_text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        normalized = " ".join(skill_text.split())
        self.assertIn("closed object/payload/package", normalized)
        self.assertIn("record coverage/exclusions/residual risk", normalized)
        self.assertIn("Do not claim absolute absence of PHI", normalized)
        self.assertNotIn("confirm no pixel PHI", skill_text)

    def test_release_surface_covers_non_pixel_and_package_payloads(self):
        for term in (
            "Structured Report",
            "Presentation State",
            "Encapsulated Document",
            "video/multiframe",
            "Waveform",
            "DICOMDIR",
            "sidecars",
            "application logs",
            "SOP Class UID",
            "Clean Structured Content",
            "Clean Graphics",
            "Clean Descriptors",
            "STOP_RELEASE_SURFACE_UNRESOLVED",
        ):
            self.assertIn(term, self.text)
        self.assertNotIn("## Two surfaces of PHI", self.text)

    def test_release_archive_is_closed_and_reconciled(self):
        self.assertIn("closed release-surface manifest", self.text)
        self.assertIn("archive actually released", self.text)
        self.assertIn("unmanifested files, sidecars or logs fail the gate", self.text)

    def test_destroying_linkage_key_does_not_self_certify_anonymity(self):
        normalized = " ".join(self.text.split())
        self.assertIn("does **not** by itself establish legal or practical anonymity", normalized)
        self.assertIn("de-identified under the named profile", normalized)
        self.assertIn("pseudonymized when a controlled re-linkage path remains", normalized)
        self.assertIn("reidentification-risk.md", self.text)
        self.assertNotIn("destroy it for full anonymisation", self.text)

    def test_defacing_is_not_skull_stripping_or_anonymity(self):
        normalized = " ".join(self.text.split())
        self.assertIn("defacing is not skull stripping", normalized.casefold())
        self.assertIn("not interchangeable with defacing", normalized)
        self.assertIn("Neither operation guarantees anonymity", normalized)
        self.assertIn("task-specific measurement impact", normalized)
        self.assertIn("controlled-access or exclusion fallback", normalized)
        self.assertNotIn("Defacing/skull-stripping", self.text)

    def test_patient_id_is_not_a_universal_join_key(self):
        normalized = " ".join(self.cohort_text.split())
        self.assertIn("not a universal join key", normalized)
        self.assertIn("row grain", normalized)
        self.assertIn("primary/composite key", normalized)
        for key in ("exam_id", "series_id", "lesion_id", "timepoint_id", "reader_id"):
            self.assertIn(key, self.cohort_text)
        self.assertNotIn("Key **every** table by `patient_id` only", self.cohort_text)

    def test_mixed_grain_joins_fail_on_unresolved_cardinality(self):
        normalized = " ".join(self.cohort_text.split())
        for term in (
            "many-to-many",
            "STOP_JOIN_CARDINALITY_UNRESOLVED",
            "row-multiplication factor",
            "do **not** full-outer-join mixed-grain tables on `patient_id` alone",
            "expected cardinality",
        ):
            self.assertIn(term, normalized)

    def test_same_lesion_t2_dwi_masks_preserve_source_space_identity(self):
        key_match = re.search(
            r"one row per mask/target/reader/version in a single reference series\s*\|\s*`([^`]+)`",
            self.cohort_text,
        )
        self.assertIsNotNone(key_match)
        declared_key = tuple(part.strip() for part in key_match.group(1).split("+"))
        common = {
            "patient_id": "P1",
            "exam_id": "E1",
            "lesion_id": "L1",
            "reader_id": "R1",
            "annotation_version": "v1",
        }
        masks = [
            dict(common, series_id="T2", reference_space_id="native-T2", mask_id="M1"),
            dict(common, series_id="DWI", reference_space_id="native-DWI", mask_id="M2"),
        ]
        old_key = tuple(common)
        self.assertEqual(1, len({tuple(row[key] for key in old_key) for row in masks}))
        self.assertEqual(2, len({tuple(row[key] for key in declared_key) for row in masks}))
        for field in ("series_id", "reference_space_id", "mask_id"):
            self.assertIn(field, declared_key)
        normalized = " ".join(self.cohort_text.split())
        self.assertIn("multi-series segmentation", normalized)
        self.assertIn("controlled mask-to-source-object link table", normalized)


class DataGrainAndFollowupContractTests(unittest.TestCase):
    def read(self, name):
        return (SKILL_ROOT / "references" / name).read_text(encoding="utf-8")

    def test_dictionary_abstraction_and_outcome_preserve_full_keys(self):
        for name in (
            "data-dictionary-spec.md",
            "chinese-clinical-text-abstraction.md",
            "outcome-and-followup-data.md",
        ):
            with self.subTest(name=name):
                text = self.read(name)
                self.assertIn("not a universal join key", text)
                self.assertNotIn("sole join key", text)
                self.assertNotIn("is the only join key", text)
                self.assertNotIn("keys on `patient_id` only", text)

    def test_dictionary_example_is_table_scoped_and_rectangular(self):
        text = self.read("data-dictionary-spec.md")
        block = re.search(r"```text\n(.*?)\n```", text, re.DOTALL).group(1)
        rows = list(csv.DictReader(io.StringIO(block)))
        self.assertTrue(rows)
        self.assertTrue(all(None not in row for row in rows))
        keys = [(row["table_id"], row["variable_name"]) for row in rows]
        self.assertEqual(len(keys), len(set(keys)))
        self.assertEqual({"clinical_baseline"}, {key[0] for key in keys})

    def test_reverse_km_uses_the_complete_eligible_analysis_population(self):
        text = " ".join(self.read("outcome-and-followup-data.md").split())
        self.assertIn("using all eligible patients", text)
        self.assertIn("original events are censored and original right-censorings become events", text)
        self.assertIn("Do not restrict the calculation to censored patients", text)
        self.assertNotIn("Median follow-up** among censored patients", text)

    def test_followup_eligibility_does_not_discard_early_events(self):
        text = " ".join(self.read("outcome-and-followup-data.md").split())
        self.assertIn("Do not exclude early deaths or other early events", text)
        self.assertIn("Administrative entry cutoff", text)
        self.assertIn("Landmark question", text)
        self.assertIn("event_type", text)
        self.assertIn("last_known_event_free_date", text)

    def test_outcome_in_imputation_depends_on_inference_or_prediction_context(self):
        text = " ".join(self.read("outcome-and-followup-data.md").split())
        self.assertIn("Association/effect estimation", text)
        self.assertIn("Prediction development and validation", text)
        self.assertIn("Do not use protected validation/test outcomes to impute predictors", text)
        self.assertIn("cannot silently manufacture event-free follow-up", text)


if __name__ == "__main__":
    unittest.main()
