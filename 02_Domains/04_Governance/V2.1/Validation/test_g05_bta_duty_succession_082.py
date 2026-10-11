import unittest
from g05_bta_duty_succession_082 import Custody,SuccessionLedger

class SuccessionTests(unittest.TestCase):
    def setUp(self):
        self.l=SuccessionLedger();self.l.register(Custody("D1","OLD",1))
    def proposal(self,**kw):
        d=dict(duty_id="D1",successor="NEW",origin_evidence="EO",successor_evidence="EN",expected_revision=1)
        d.update(kw);return self.l.propose(**d)
    def test_register(self):self.assertEqual(self.l.records["D1"].custodian,"OLD")
    def test_duplicate_register(self):self.assertFalse(self.l.register(Custody("D1","OTHER",1)))
    def test_proposal_pending(self):self.assertEqual(self.proposal(),"PENDING")
    def test_no_self_transfer(self):self.assertEqual(self.proposal(successor="OLD"),"EVIDENCE_OR_SUCCESSOR_MISSING")
    def test_no_origin_evidence(self):self.assertEqual(self.proposal(origin_evidence=""),"EVIDENCE_OR_SUCCESSOR_MISSING")
    def test_no_successor_evidence(self):self.assertEqual(self.proposal(successor_evidence=""),"EVIDENCE_OR_SUCCESSOR_MISSING")
    def test_stale_proposal(self):self.assertEqual(self.proposal(expected_revision=0),"STALE")
    def test_no_double_proposal(self):
        self.proposal();self.assertEqual(self.proposal(),"NOT_ELIGIBLE")
    def test_no_unverified_transfer(self):
        self.proposal();self.assertEqual(self.l.confirm("D1",False,True),"NOT_VERIFIED")
    def test_successor_must_verify(self):
        self.proposal();self.assertEqual(self.l.confirm("D1",True,False),"NOT_VERIFIED")
    def test_transfer_preserves_obligation(self):
        self.proposal();self.assertEqual(self.l.confirm("D1",True,True),"TRANSFERRED")
        self.assertEqual(self.l.records["D1"].obligation_state,"OPEN")
    def test_revision_advances(self):
        self.proposal();self.l.confirm("D1",True,True)
        self.assertEqual(self.l.records["D1"].revision,2)
    def test_old_custodian_retirement_preserves_duty(self):
        self.assertEqual(self.l.retire_custodian("OLD")["untransferred_open_duties"],["D1"])
    def test_after_transfer_old_retirement_has_no_untransferred_duty(self):
        self.proposal();self.l.confirm("D1",True,True)
        self.assertEqual(self.l.retire_custodian("OLD")["untransferred_open_duties"],[])
    def test_retirement_never_extinguishes(self):
        self.assertFalse(self.l.retire_custodian("OLD")["obligations_extinguished"])
    def test_history_records_transfer(self):
        self.proposal();self.l.confirm("D1",True,True)
        self.assertEqual(self.l.history[-1],("TRANSFER","D1","OLD","NEW"))
if __name__=="__main__":unittest.main(verbosity=2)
