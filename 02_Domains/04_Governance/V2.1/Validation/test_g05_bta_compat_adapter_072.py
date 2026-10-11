import copy
import unittest
from g05_bta_compat_adapter_072 import read_fixture, project, LEGACY_ONLY, GRADUATED_ONLY, consequentially_complete

class CompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.source = read_fixture()
        self.result = project(self.source)

    def test_original_preserved(self):
        self.assertEqual(self.result["source"], self.source)

    def test_no_source_mutation(self):
        original = copy.deepcopy(self.source)
        project(self.source)
        self.assertEqual(self.source, original)

    def test_all_six_ambiguous_fields_quarantined(self):
        self.assertEqual(set(self.result["unresolved_legacy_fields"]), LEGACY_ONLY)

    def test_no_unsupported_graduated_fields_created(self):
        self.assertFalse(GRADUATED_ONLY & set(self.result["graduated_shared_fields"]))

    def test_review_not_consequence(self):
        self.assertIn("ExternalityReviewRefs", self.result["unresolved_legacy_fields"])
        self.assertNotIn("ExternalConsequenceRefs", self.result["graduated_shared_fields"])

    def test_owner_not_inferred_from_state_system(self):
        self.assertNotIn("ParticipatingOwnerRefs", self.result["graduated_shared_fields"])

    def test_recovery_not_inferred_from_rollback(self):
        self.assertNotIn("RecoveryRefs", self.result["graduated_shared_fields"])

    def test_no_full_completion(self):
        self.assertFalse(consequentially_complete(self.source))

    def test_ambiguous_projection_not_authoritative(self):
        self.assertFalse(self.result["semantics_verified"])

    def test_copy_isolation(self):
        self.result["source"]["TransitionID"] = "CHANGED"
        self.assertEqual(self.source["TransitionID"], "BTA-MRT-003-TX-01")

if __name__ == "__main__":
    unittest.main(verbosity=2)
