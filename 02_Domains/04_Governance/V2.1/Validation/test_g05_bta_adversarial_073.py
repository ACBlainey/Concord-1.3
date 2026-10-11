import copy
import unittest
from g05_bta_compat_adapter_072 import read_fixture
from g05_bta_adversarial_073 import audit, consequential_clearance

class AdversarialTests(unittest.TestCase):
    def setUp(self): self.r=read_fixture()
    def check(self,mutate,code):
        r=copy.deepcopy(self.r);mutate(r);self.assertIn(code,audit(r))
    def test_baseline_needs_semantic_review(self):
        self.assertIn("LEGACY_SEMANTIC_MAPPING_UNRESOLVED",audit(self.r))
    def test_missing_identity(self): self.check(lambda r:r.pop("TransitionID"),"IDENTITY_OR_SCOPE_MISSING")
    def test_missing_scope(self): self.check(lambda r:r.pop("Scope"),"IDENTITY_OR_SCOPE_MISSING")
    def test_missing_provenance(self): self.check(lambda r:r.pop("Provenance"),"PROVENANCE_MISSING")
    def test_missing_historical_ref(self): self.check(lambda r:r["Provenance"].pop("HistoricalRef"),"PROVENANCE_MISSING")
    def test_pending_claimed_complete(self): self.check(lambda r:r.update(DeclaredComplete=True),"PENDING_BUT_DECLARED_COMPLETE")
    def test_terminated_claimed_active(self): self.check(lambda r:r.update(DeclaredAuthorityActive=True),"TERMINATED_AUTHORITY_REACTIVATION_CLAIM")
    def test_unresolved_without_protection(self): self.check(lambda r:r.pop("ProtectedUnresolvedStateRefs"),"UNRESOLVED_UNPROTECTED")
    def test_review_and_consequence_conflict(self): self.check(lambda r:r.update(ExternalConsequenceRefs=[{"Ref":"C1"}]),"REVIEW_AND_CONSEQUENCE_REQUIRE_OWNER_RECONCILIATION")
    def test_missing_basis(self): self.check(lambda r:r.pop("TransitionBasisRefs"),"BASIS_MISSING_REVIEW")
    def test_no_authority_granted(self):
        self.assertFalse(consequential_clearance(self.r)["authorised"])
        self.assertFalse(consequential_clearance(self.r)["complete"])
    def test_invalid_object(self): self.assertEqual(audit(None),["RECORD_INVALID"])

if __name__=="__main__":unittest.main(verbosity=2)
