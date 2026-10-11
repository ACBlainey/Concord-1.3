import unittest
from g05_bta_continuity_duties_081 import Duty,ContinuityLedger

class ContinuityDutyTests(unittest.TestCase):
    def setUp(self):
        self.l=ContinuityLedger()
        self.d=Duty("D1","HISTORICAL","TX1","PARTICIPANT-A","EV-ORIGIN")
        self.l.register(self.d)
    def test_registered(self):self.assertIn("D1",self.l.duties)
    def test_duplicate(self):self.assertEqual(self.l.register(self.d),"DUPLICATE")
    def test_invalid(self):self.assertEqual(self.l.register(Duty("","O","TX","B","EV")),"INVALID")
    def test_resumption_preserves_duty(self):
        self.assertEqual(self.l.recover_function("TX1","RESUMPTION")["open_duties"],["D1"])
    def test_compensation_preserves_duty(self):
        self.assertEqual(self.l.recover_function("TX1","COMPENSATION")["open_duties"],["D1"])
    def test_reconstruction_preserves_duty(self):
        self.assertEqual(self.l.recover_function("TX1","RECONSTRUCTION")["open_duties"],["D1"])
    def test_restoration_preserves_duty(self):
        self.assertEqual(self.l.recover_function("TX1","RESTORATION")["open_duties"],["D1"])
    def test_wrong_owner(self):self.assertEqual(self.l.close("D1","OTHER","EV",True),"WRONG_OWNER")
    def test_unverified(self):self.assertEqual(self.l.close("D1","HISTORICAL","EV",False),"UNVERIFIED")
    def test_missing_evidence(self):self.assertEqual(self.l.close("D1","HISTORICAL","",True),"UNVERIFIED")
    def test_verified_closure(self):
        self.assertEqual(self.l.close("D1","HISTORICAL","EV-CLOSE",True),"CLOSED")
        self.assertEqual(self.l.recover_function("TX1","RESTORATION")["open_duties"],[])
    def test_closure_audit_history(self):
        self.l.close("D1","HISTORICAL","EV",True)
        self.assertEqual(self.l.events[:2],[("REGISTER","D1"),("CLOSE","D1")])
    def test_no_implicit_discharge(self):
        self.assertFalse(self.l.recover_function("TX1","RESTORATION")["obligations_discharge_inferred"])
    def test_other_transition_isolated(self):
        self.assertEqual(self.l.recover_function("TX2","RESUMPTION")["open_duties"],[])
    def test_unknown_closure(self):self.assertEqual(self.l.close("UNKNOWN","HISTORICAL","EV",True),"UNKNOWN")
if __name__=="__main__":unittest.main(verbosity=2)
