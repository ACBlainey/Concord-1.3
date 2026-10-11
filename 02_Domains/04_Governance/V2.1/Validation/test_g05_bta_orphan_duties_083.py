import unittest
from g05_bta_orphan_duties_083 import OrphanRegistry

class OrphanTests(unittest.TestCase):
    def setUp(self):
        self.r=OrphanRegistry()
        self.r.detect("D1","DEFUNCT-ENTERPRISE","TX1","EV1","PRIVATE-P1")
    def test_detect(self):self.assertTrue(self.r.status("D1")["discoverable"])
    def test_missing_provenance(self):
        self.assertEqual(self.r.detect("D2","OLD","TX2","","P"),"INSUFFICIENT_PROVENANCE")
    def test_duplicate(self):
        self.assertEqual(self.r.detect("D1","OLD","TX1","EV","P"),"ALREADY_RECORDED")
    def test_no_auto_custody(self):self.assertFalse(self.r.status("D1")["custody_assigned"])
    def test_no_extinguishment(self):self.assertFalse(self.r.status("D1")["duty_extinguished"])
    def test_referral(self):
        self.assertEqual(self.r.refer("D1","CIVIL-CONTACT","review"),"REFERRED_NOT_ASSIGNED")
    def test_referral_not_assignment(self):
        self.r.refer("D1","CIVIL-CONTACT","review")
        self.assertFalse(self.r.status("D1")["custody_assigned"])
    def test_unknown_referral(self):self.assertEqual(self.r.refer("D2","CIVIL-CONTACT","review"),"UNKNOWN_DUTY")
    def test_missing_contact(self):self.assertEqual(self.r.refer("D1","","review"),"INVALID_REFERRAL")
    def test_nomination_not_assignment(self):
        self.assertEqual(self.r.nominate("D1","CANDIDATE","QUALIFICATION-EV"),"REQUIRES_OWNER_AND_SUCCESSOR_VERIFICATION")
        self.assertFalse(self.r.status("D1")["custody_assigned"])
    def test_unqualified_nomination(self):self.assertEqual(self.r.nominate("D1","CANDIDATE",""),"NOT_QUALIFIED")
    def test_protected_reference_retained(self):
        self.assertEqual(self.r.status("D1")["protected_beneficiary_ref"],"PRIVATE-P1")
    def test_referral_event_preserved(self):
        self.r.refer("D1","CIVIL-CONTACT","review")
        self.assertIn(("REFERRED_FOR_REVIEW","D1","CIVIL-CONTACT"),self.r.events)
    def test_multiple_referrals_no_hierarchy(self):
        self.r.refer("D1","CONTINUITY","review");self.r.refer("D1","HISTORICAL","provenance")
        self.assertEqual(len(self.r.referrals),2)
        self.assertFalse(self.r.status("D1")["custody_assigned"])
    def test_unknown_status(self):self.assertFalse(self.r.status("UNKNOWN")["discoverable"])
if __name__=="__main__":unittest.main(verbosity=2)
