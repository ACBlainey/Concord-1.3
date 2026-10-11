"""G05 integration scenario 088: cross-stage interface assertions, not runtime certification."""
import unittest
from g05_bta_continuity_duties_081 import Duty,ContinuityLedger
from g05_bta_duty_succession_082 import Custody,SuccessionLedger
from g05_bta_orphan_duties_083 import OrphanRegistry
from g05_bta_orphan_protection_084 import ProtectiveMandate,evaluate,expiry_record
from g05_bta_protection_renewal_085 import Renewal,review_renewal
from g05_bta_cumulative_control_086 import Intervention,exposure
from g05_bta_distributed_control_087 import Restriction,audit

class CrossStageScenario(unittest.TestCase):
    def setUp(self):
        self.duties=ContinuityLedger()
        self.duties.register(Duty("D1","OLD","TX1","BENEFICIARY","EV1"))
        self.succession=SuccessionLedger()
        self.succession.register(Custody("D1","OLD",1))
        self.orphans=OrphanRegistry()
        self.orphans.detect("D1","OLD","TX1","EV1","BENEFICIARY")
        self.m=ProtectiveMandate("D1","M1","EMERGENCY-OWNER","PROTECT",("PRESERVE_RECORD",),10,20,"REVIEW1",1)
    def test_recovery_does_not_close_duty(self):
        self.assertEqual(self.duties.recover_function("TX1","RESTORATION")["open_duties"],["D1"])
    def test_retirement_exposes_untransferred_duty(self):
        self.assertEqual(self.succession.retire_custodian("OLD")["untransferred_open_duties"],["D1"])
    def test_referral_cannot_assign_custody(self):
        self.orphans.refer("D1","CIVIL-CONTACT","urgent")
        self.assertFalse(self.orphans.status("D1")["custody_assigned"])
    def test_protection_during_paused_clock_requires_external_authority(self):
        result=evaluate(self.m,"PRESERVE_RECORD",15,1,False,True,True,clock_paused=True)
        self.assertIn("AUTHORITY_NOT_VERIFIED",result["issues"])
        self.assertFalse(result["clock_advanced"])
    def test_protection_expiry_during_clock_pause(self):
        self.assertTrue(expiry_record(self.m,20)["expired"])
        self.assertEqual(self.duties.recover_function("TX1","RESUMPTION")["open_duties"],["D1"])
    def test_renewal_without_independent_review_fails(self):
        renewal=Renewal("D1","M1","M2","EMERGENCY-OWNER","EV2","REV2","NEC","PROP",20,30,2)
        result=review_renewal(self.m,renewal,21,True,2,True,False)
        self.assertIn("INDEPENDENT_REVIEW_REQUIRED",result["issues"])
    def test_cumulative_review_not_authority(self):
        result=exposure([Intervention("M1","BENEFICIARY","C1",10,20),
                         Intervention("M2","BENEFICIARY","C1",20,30)],
                         "BENEFICIARY","C1",10,30,15,15)
        self.assertTrue(result["requires_independent_review"])
        self.assertFalse(result["authority_granted"])
    def test_distributed_review_not_authority(self):
        result=audit([Restriction("M1","BENEFICIARY","C1",10,20,"ACCESS"),
                      Restriction("M2","BENEFICIARY","C2",20,30,"ACCESS")],
                      "BENEFICIARY","ACCESS",10,30,15,2)
        self.assertTrue(result["review_required"])
        self.assertFalse(result["authority_granted"])
    def test_succession_requires_both_attestations(self):
        self.succession.propose("D1","NEW","ORIGIN-EV","SUCCESSOR-EV",1)
        self.assertEqual(self.succession.confirm("D1",True,False),"NOT_VERIFIED")
    def test_succession_and_duty_closure_are_separate_ledgers(self):
        self.succession.propose("D1","NEW","ORIGIN-EV","SUCCESSOR-EV",1)
        self.succession.confirm("D1",True,True)
        self.assertEqual(self.duties.duties["D1"].state,"OPEN")
        self.assertEqual(self.duties.duties["D1"].owner,"OLD")
    def test_orphan_registry_does_not_auto_resolve_after_succession(self):
        self.succession.propose("D1","NEW","ORIGIN-EV","SUCCESSOR-EV",1)
        self.succession.confirm("D1",True,True)
        self.assertFalse(self.orphans.status("D1")["custody_assigned"])
    def test_expired_mandate_not_usable(self):
        result=evaluate(self.m,"PRESERVE_RECORD",20,1,True,True,True)
        self.assertIn("OUTSIDE_OPERATIONAL_WINDOW",result["issues"])
if __name__=="__main__":unittest.main(verbosity=2)
