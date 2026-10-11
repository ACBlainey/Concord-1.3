import unittest, yaml, pathlib, copy
P=pathlib.Path(__file__).with_name("G05_BTA_Original_MRT003_Fixture_070.yaml")
D=yaml.safe_load(P.read_text(encoding="utf-8"))["BoundedTransitionContract"]
LEGACY={"ParticipatingStateSystemRefs","TransitionEpochOrPhaseRefs","ScopedValidationRefs","ExternalityReviewRefs","ClockTransitionRelationRefs","RollbackOrRecoveryRefs"}
class ContractTests(unittest.TestCase):
    def test_field_count(self): self.assertEqual(len(D),28)
    def test_lossless_data_roundtrip(self): self.assertEqual(yaml.safe_load(yaml.safe_dump(D)),D)
    def test_legacy_keys(self): self.assertTrue(LEGACY.issubset(D))
    def test_no_destination_access(self): self.assertTrue(any(x["DomainTransitionState"]=="DESTINATION_PRIVILEGED_ACCESS_NOT_ACTIVE" for x in D["TransitionStateRefs"]))
    def test_surviving_duty(self): self.assertTrue(any(x["State"]=="ACTIVE" for x in D["SurvivingDutyRefs"]))
    def test_no_full_restoration(self): self.assertTrue(any(x["State"]=="PRIOR_STATE_NOT_RESTORABLE" for x in D["RollbackOrRecoveryRefs"]))
    def test_failed_attempt_preserved(self): self.assertTrue(D["Provenance"]["FailedAttemptRefs"])
    def test_review_not_consequence(self): self.assertNotIn("ExternalConsequenceRefs",D)
    def test_pending_not_complete(self): self.assertTrue(D["PendingStateRefs"] and D["CompletionConditionRefs"])
    def test_mutation_detected(self):
        changed=copy.deepcopy(D)
        changed["Provenance"].pop("FailedAttemptRefs")
        self.assertNotEqual(changed,D)
if __name__=="__main__": unittest.main(verbosity=2)
