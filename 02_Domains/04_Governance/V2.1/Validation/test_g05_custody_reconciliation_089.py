import unittest
from dataclasses import replace
from g05_bta_continuity_duties_081 import Duty,ContinuityLedger
from g05_bta_duty_succession_082 import Custody,SuccessionLedger
from g05_bta_orphan_duties_083 import OrphanRegistry
from g05_custody_reconciliation_089 import ReconciliationEvent,reconcile

class ReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.d=ContinuityLedger();self.d.register(Duty("D1","OLD","TX","PRIVATE","EV"))
        self.s=SuccessionLedger();self.s.register(Custody("D1","OLD",1))
        self.o=OrphanRegistry();self.o.detect("D1","OLD","TX","EV","PRIVATE")
        self.s.propose("D1","NEW","OE","SE",1);self.s.confirm("D1",True,True)
        self.e=ReconciliationEvent("EVENT","D1","OLD","NEW",1,2,"OWNER-EV","SUCCESSOR-EV","PROV","TX")
    def check(self,event=None,owner=True,successor=True,provenance=True,revision=1):
        return reconcile(event or self.e,self.d,self.s,self.o,owner,successor,provenance,revision)
    def test_valid_candidate(self):self.assertTrue(self.check()["eligible_for_owner_controlled_projection"])
    def test_no_mutation(self):self.assertFalse(self.check()["mutation_performed"])
    def test_no_authority(self):self.assertFalse(self.check()["authority_granted"])
    def test_no_duty_closure(self):self.assertFalse(self.check()["duty_closed"])
    def test_no_orphan_clear(self):self.assertFalse(self.check()["orphan_cleared"])
    def test_owner_attestation(self):self.assertIn("OWNER_ATTESTATION_REQUIRED",self.check(owner=False)["issues"])
    def test_successor_attestation(self):self.assertIn("SUCCESSOR_ATTESTATION_REQUIRED",self.check(successor=False)["issues"])
    def test_provenance_attestation(self):self.assertIn("PROVENANCE_VERIFICATION_REQUIRED",self.check(provenance=False)["issues"])
    def test_stale_revision(self):self.assertIn("SOURCE_REVISION_NOT_CONFIRMED",self.check(revision=0)["issues"])
    def test_missing_revision(self):self.assertIn("SOURCE_REVISION_NOT_CONFIRMED",self.check(revision=None)["issues"])
    def test_wrong_transition(self):self.assertIn("TRANSITION_PROVENANCE_MISMATCH",self.check(replace(self.e,source_transition_ref="OTHER"))["issues"])
    def test_wrong_successor(self):self.assertIn("SUCCESSION_NOT_COMMITTED",self.check(replace(self.e,proposed_custodian="OTHER"))["issues"])
    def test_wrong_revision(self):self.assertIn("REVISION_MISMATCH",self.check(replace(self.e,new_revision=3))["issues"])
    def test_missing_duty(self):
        del self.d.duties["D1"]
        self.assertIn("SOURCE_RECORD_MISSING",self.check()["issues"])
    def test_incomplete_evidence(self):self.assertIn("INCOMPLETE_EVENT",self.check(replace(self.e,owner_decision_ref=""))["issues"])
    def test_no_change(self):self.assertIn("NO_CUSTODY_CHANGE",self.check(replace(self.e,proposed_custodian="OLD"))["issues"])
    def test_continuity_stays_open(self):
        self.check();self.assertEqual(self.d.duties["D1"].state,"OPEN")
    def test_orphan_stays_unassigned(self):
        self.check();self.assertFalse(self.o.status("D1")["custody_assigned"])
if __name__=="__main__":unittest.main(verbosity=2)
