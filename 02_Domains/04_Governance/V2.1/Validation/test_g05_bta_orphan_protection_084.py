import unittest
from g05_bta_orphan_protection_084 import ProtectiveMandate,evaluate,expiry_record

class ProtectionTests(unittest.TestCase):
    def setUp(self):
        self.m=ProtectiveMandate("D1","M1","EMERGENCY-OWNER","SAFEGUARD",("PRESERVE_RECORD","PREVENT_IMMEDIATE_HARM"),10,20,"REVIEW1",3)
    def check(self,m=None,action="PRESERVE_RECORD",now=15,revision=3,owner=True,necessary=True,proportionate=True):
        return evaluate(m or self.m,action,now,revision,owner,necessary,proportionate)
    def test_bounded_proposal(self):self.assertTrue(self.check()["eligible_for_external_execution_review"])
    def test_no_created_authority(self):self.assertFalse(self.check()["authority_created"])
    def test_no_succession(self):self.assertFalse(self.check()["permanent_custody_assigned"])
    def test_clock_not_advanced(self):self.assertFalse(self.check()["clock_advanced"])
    def test_action_scope(self):self.assertIn("ACTION_OUT_OF_SCOPE",self.check(action="TAKE_OWNERSHIP")["issues"])
    def test_before_start(self):self.assertIn("OUTSIDE_OPERATIONAL_WINDOW",self.check(now=9)["issues"])
    def test_at_expiry(self):self.assertIn("OUTSIDE_OPERATIONAL_WINDOW",self.check(now=20)["issues"])
    def test_stale_revision(self):self.assertIn("MANDATE_REVISION_STALE",self.check(revision=4)["issues"])
    def test_no_owner_verification(self):self.assertIn("AUTHORITY_NOT_VERIFIED",self.check(owner=False)["issues"])
    def test_necessity(self):self.assertIn("NECESSITY_NOT_VERIFIED",self.check(necessary=False)["issues"])
    def test_proportionality(self):self.assertIn("PROPORTIONALITY_NOT_VERIFIED",self.check(proportionate=False)["issues"])
    def test_expiry_independent_of_clock(self):
        self.assertTrue(expiry_record(self.m,21)["expired"])
        self.assertFalse(self.check()["clock_advanced"])
    def test_surviving_audit(self):self.assertIn("PROTECTIVE_ACTION_AUDIT",expiry_record(self.m,20)["surviving_duties"])
    def test_succession_review_survives(self):self.assertIn("SUCCESSION_REVIEW",expiry_record(self.m,20)["surviving_duties"])
    def test_no_auto_custody_at_expiry(self):self.assertFalse(expiry_record(self.m,20)["permanent_custody_assigned"])
    def test_no_early_expiry(self):self.assertFalse(expiry_record(self.m,19)["expired"])
if __name__=="__main__":unittest.main(verbosity=2)
