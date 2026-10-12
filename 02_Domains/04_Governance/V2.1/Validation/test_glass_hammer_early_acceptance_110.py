import os
import tempfile
import unittest
from glass_hammer_early_acceptance_110 import ContextualDecision

class ContextualAcceptance110(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.m=ContextualDecision(os.path.join(self.tmp.name,"db.sqlite"))
        self.m.create("D","Question?")
    def tearDown(self):self.tmp.cleanup()
    def vote(self,p="P1",s="S1",v="F",e="E1",**kw):
        return self.m.vote(decision_id="D",position=p,steward=s,choice=v,event_id=e,eligible=True,context_ok=True,**kw)
    def two(self):
        self.vote()
        self.vote("P2","S2","F","E2")
    def test_two_determine_not_accept(self):
        self.two()
        s=self.m.status("D")
        self.assertEqual(s["determined"],"F")
        self.assertIsNone(s["accepted"])
    def test_default_wait(self):
        self.two()
        self.assertEqual(self.m.accept("D"),"WAIT_FOR_THIRD")
    def test_emergency_context_early(self):
        self.two()
        self.assertEqual(self.m.accept("D",early_context_justified=True,basis="EMERGENCY"),"EARLY_ACCEPTED")
    def test_early_requires_basis(self):
        self.two()
        self.assertEqual(self.m.accept("D",early_context_justified=True),"WAIT_FOR_THIRD")
    def test_non_emergency_context_possible(self):
        self.two()
        self.assertEqual(self.m.accept("D",early_context_justified=True,basis="OTHER_JUSTIFIED_CONTEXT"),"EARLY_ACCEPTED")
    def test_third_before_accept(self):
        self.two()
        self.assertEqual(self.vote("P3","S3","A","E3"),"ACCEPTED")
        self.assertEqual(self.m.accept("D"),"ACCEPTED")
    def test_late_third_after_early(self):
        self.two()
        self.m.accept("D",early_context_justified=True,basis="EMERGENCY")
        self.assertEqual(self.vote("P3","S3","A","E3"),"LATE_RECORDED")
        self.assertEqual(self.m.status("D")["accepted"],"F")
    def test_late_third_cannot_reopen(self):
        self.two()
        self.m.accept("D",early_context_justified=True,basis="EMERGENCY")
        self.vote("P3","S3","A","E3")
        self.assertEqual(self.m.accept("D"),"ALREADY_ACCEPTED")
    def test_third_not_consumed_by_early(self):
        self.two()
        self.m.accept("D",early_context_justified=True,basis="EMERGENCY")
        self.assertEqual(len(self.m.status("D")["late"]),0)
    def test_late_duplicate_event(self):
        self.two()
        self.m.accept("D",early_context_justified=True,basis="EMERGENCY")
        self.vote("P3","S3","A","E3")
        self.assertEqual(self.vote("P3","S3","A","E3"),"DUPLICATE")
    def test_late_new_event_cannot_revote(self):
        self.two()
        self.m.accept("D",early_context_justified=True,basis="EMERGENCY")
        self.vote("P3","S3","A","E3")
        self.assertEqual(self.vote("P3","S3","F","E4"),"DENY_CONSUMED")
    def test_late_other_steward_cannot_revote(self):
        self.two()
        self.m.accept("D",early_context_justified=True,basis="EMERGENCY")
        self.vote("P3","S3","A","E3")
        self.assertEqual(self.vote("P3","S4","F","E4"),"DENY_CONSUMED")
    def test_late_requires_current_context(self):
        self.two()
        self.m.accept("D",early_context_justified=True,basis="EMERGENCY")
        self.assertEqual(self.m.vote(decision_id="D",position="P3",steward="S3",choice="A",event_id="E3",eligible=True,context_ok=False),"DENY_CONTEXT")
    def test_no_majority_cannot_accept(self):
        self.vote(v="U")
        self.vote("P2","S2","F","E2")
        self.assertEqual(self.m.accept("D",early_context_justified=True,basis="EMERGENCY"),"DENY_UNRESOLVED")
    def test_early_never_authorises_effect(self):
        self.two()
        self.m.accept("D",early_context_justified=True,basis="EMERGENCY")
        self.assertFalse(self.m.status("D")["execution_authorised"])
    def test_negative_majority_early(self):
        self.vote(v="A")
        self.vote("P2","S2","A","E2")
        self.assertEqual(self.m.accept("D",early_context_justified=True,basis="EMERGENCY"),"EARLY_ACCEPTED")
        self.assertEqual(self.m.status("D")["accepted"],"A")

if __name__=="__main__":unittest.main()
