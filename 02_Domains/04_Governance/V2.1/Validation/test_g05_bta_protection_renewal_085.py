import unittest
from g05_bta_orphan_protection_084 import ProtectiveMandate
from g05_bta_protection_renewal_085 import Renewal,review_renewal

class RenewalTests(unittest.TestCase):
    def setUp(self):
        self.prior=ProtectiveMandate("D1","M1","OWNER","SCOPE",("SAFEGUARD",),10,20,"REV1",1)
        self.r=Renewal("D1","M1","M2","OWNER","NEW-EV","REV2","NECESSITY","PROPORTIONALITY",20,30,2)
    def check(self,r=None,now=22,owner=True,rev=2,cumulative=True,independent=True):
        return review_renewal(self.prior,r or self.r,now,owner,rev,cumulative,independent)
    def change(self,**kw):
        d=dict(vars(self.r));d.update(kw);return Renewal(**d)
    def test_new_review_candidate(self):self.assertTrue(self.check()["eligible_for_external_approval"])
    def test_no_authority_created(self):self.assertFalse(self.check()["authority_granted"])
    def test_prior_not_extended(self):self.assertFalse(self.check()["prior_mandate_extended"])
    def test_no_custody(self):self.assertFalse(self.check()["permanent_custody_assigned"])
    def test_reused_mandate(self):self.assertIn("NEW_MANDATE_REQUIRED",self.check(self.change(new_mandate_ref="M1"))["issues"])
    def test_wrong_duty(self):self.assertIn("PRIOR_MANDATE_MISMATCH",self.check(self.change(duty_id="D2"))["issues"])
    def test_missing_fresh_evidence(self):self.assertIn("FRESH_JUSTIFICATION_INCOMPLETE",self.check(self.change(new_evidence_ref=""))["issues"])
    def test_missing_necessity(self):self.assertIn("FRESH_JUSTIFICATION_INCOMPLETE",self.check(self.change(necessity_ref=""))["issues"])
    def test_missing_proportionality(self):self.assertIn("FRESH_JUSTIFICATION_INCOMPLETE",self.check(self.change(proportionality_ref=""))["issues"])
    def test_overlap(self):self.assertIn("TEMPORAL_BOUNDARY_INVALID",self.check(self.change(start_tick=19))["issues"])
    def test_invalid_expiry(self):self.assertIn("TEMPORAL_BOUNDARY_INVALID",self.check(self.change(expiry_tick=20))["issues"])
    def test_expired_renewal(self):self.assertIn("RENEWAL_NOT_CURRENT",self.check(now=30)["issues"])
    def test_stale_revision(self):self.assertIn("REVISION_STALE",self.check(rev=3)["issues"])
    def test_owner_unverified(self):self.assertIn("NEW_OWNER_VERIFICATION_REQUIRED",self.check(owner=False)["issues"])
    def test_cumulative_review_missing(self):self.assertIn("CUMULATIVE_EFFECTS_REVIEW_REQUIRED",self.check(cumulative=False)["issues"])
    def test_independent_review_missing(self):self.assertIn("INDEPENDENT_REVIEW_REQUIRED",self.check(independent=False)["issues"])
if __name__=="__main__":unittest.main(verbosity=2)
