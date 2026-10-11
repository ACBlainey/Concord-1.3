import unittest
from g05_bta_recovery_outcomes_080 import Outcome,classify

class OutcomeTests(unittest.TestCase):
    def make(self,kind="RESTORATION",**kw):
        d=dict(kind=kind,prior_state_ref="OLD",resulting_state_ref="NEW",evidence_refs=("EV",),
               unresolved_effect_refs=(),owner_reviewed=True,equivalence_verified=(kind=="RESTORATION"),
               surviving_duty_refs=())
        d.update(kw);return Outcome(**d)
    def test_verified_restoration(self):self.assertTrue(classify(self.make())["full_restoration_verified"])
    def test_resumption_not_restoration(self):self.assertFalse(classify(self.make("RESUMPTION"))["full_restoration_verified"])
    def test_compensation_not_restoration(self):self.assertFalse(classify(self.make("COMPENSATION"))["full_restoration_verified"])
    def test_reconstruction_not_restoration(self):self.assertFalse(classify(self.make("RECONSTRUCTION"))["full_restoration_verified"])
    def test_unverified_equivalence(self):
        self.assertIn("RESTORATION_EQUIVALENCE_UNVERIFIED",classify(self.make(equivalence_verified=False))["issues"])
    def test_unresolved_effects(self):
        self.assertIn("UNRESOLVED_EFFECTS_PREVENT_FULL_RESTORATION",classify(self.make(unresolved_effect_refs=("HARM",)))["issues"])
    def test_no_prior_state(self):
        self.assertIn("RESTORATION_EQUIVALENCE_UNVERIFIED",classify(self.make(prior_state_ref=""))["issues"])
    def test_missing_evidence(self):
        self.assertIn("MISSING_EVIDENCE",classify(self.make(evidence_refs=()))["issues"])
    def test_owner_review(self):
        self.assertIn("OWNER_REVIEW_REQUIRED",classify(self.make(owner_reviewed=False))["issues"])
    def test_missing_result(self):
        self.assertIn("RESULTING_STATE_MISSING",classify(self.make(resulting_state_ref=""))["issues"])
    def test_duties_survive(self):
        self.assertTrue(classify(self.make(surviving_duty_refs=("FOLLOWUP",)))["duties_survive"])
    def test_unknown_kind(self):
        self.assertIn("UNKNOWN_OUTCOME",classify(self.make("MAGIC"))["issues"])
    def test_no_authority(self):self.assertFalse(classify(self.make())["authority_granted"])
    def test_false_equivalence_in_compensation(self):
        self.assertIn("EQUIVALENCE_CLAIM_REQUIRES_RECLASSIFICATION",classify(self.make("COMPENSATION",equivalence_verified=True))["issues"])
if __name__=="__main__":unittest.main(verbosity=2)
