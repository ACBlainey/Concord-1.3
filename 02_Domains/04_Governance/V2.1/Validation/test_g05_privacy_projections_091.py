import unittest
from g05_privacy_projections_091 import public_duty_projection,privileged_duty_projection
from g05_bta_continuity_duties_081 import ContinuityLedger,Duty
from g05_bta_orphan_duties_083 import OrphanRegistry
from g05_bta_duty_succession_082 import SuccessionLedger,Custody
class PrivacyTests(unittest.TestCase):
 def setUp(self):
  self.d=ContinuityLedger();self.d.register(Duty("D1","OLD","TX","SECRET-PERSON","EV"))
  self.o=OrphanRegistry();self.o.detect("D1","OLD","TX","EV","SECRET-PERSON")
  self.s=SuccessionLedger();self.s.register(Custody("D1","OLD",1))
 def public(self):return public_duty_projection("D1",self.d,self.o,self.s)
 def test_public_has_no_beneficiary(self):self.assertNotIn("beneficiary_ref",self.public())
 def test_public_no_secret_string(self):self.assertNotIn("SECRET-PERSON",str(self.public()))
 def test_public_no_owner(self):self.assertNotIn("OLD",str(self.public()))
 def test_public_no_evidence(self):self.assertNotIn("EV",str(self.public()))
 def test_public_no_transition(self):self.assertNotIn("TX",str(self.public()))
 def test_public_obligation_open(self):self.assertTrue(self.public()["obligation_open"])
 def test_public_orphan(self):self.assertTrue(self.public()["orphan_referral_pending"])
 def test_public_review(self):self.assertTrue(self.public()["review_required"])
 def test_no_authority(self):self.assertFalse(self.public()["authority_granted"])
 def test_denied_privileged(self):self.assertEqual(privileged_duty_projection("D1",self.d,self.o),{"access_denied":True})
 def test_privileged_verified(self):self.assertEqual(privileged_duty_projection("D1",self.d,self.o,True)["beneficiary_ref"],"SECRET-PERSON")
 def test_unknown_public(self):self.assertFalse(public_duty_projection("UNKNOWN",self.d,self.o,self.s)["found"])
 def test_unknown_privileged(self):self.assertIsNone(privileged_duty_projection("UNKNOWN",self.d,self.o,True)["beneficiary_ref"])
 def test_missing_custody_review(self):
  del self.s.records["D1"];self.assertTrue(self.public()["review_required"])
 def test_missing_orphan_no_flag_when_consistent(self):
  del self.o.records["D1"];self.assertFalse(self.public()["review_required"])
 def test_closed_obligation(self):
  self.d.close("D1","OLD","CLOSE-EV",True);self.assertFalse(self.public()["obligation_open"])
if __name__=="__main__":unittest.main()
