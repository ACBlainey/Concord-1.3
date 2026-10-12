import os
import tempfile
import threading
import unittest
from dataclasses import replace
from glass_hammer_atomic_acceptance_112 import AtomicContextualDecision
from glass_hammer_context_evidence_111 import ContextEvidence,OwnerSnapshot

class AtomicAcceptance112(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.path=os.path.join(self.tmp.name,"db.sqlite")
        self.m=AtomicContextualDecision(self.path)
        self.m.create("D","Question?")
        for p,s,e in (("P1","S1","E1"),("P2","S2","E2")):
            self.m.vote(decision_id="D",position=p,steward=s,choice="F",event_id=e,eligible=True,context_ok=True)
        self.e=ContextEvidence("D","OWNER","REVIEWER","Emergency",3,100,200,"REF-3","Urgent","REVIEW")
        self.s=OwnerSnapshot("D",3,150,frozenset({"OWNER"}),frozenset({"OWNER"}),True,True,True,True)
    def tearDown(self):self.tmp.cleanup()
    def context(self,revision=3,**kw):return self.m.set_context("D",revision,**kw)
    def test_valid_atomic_acceptance(self):
        self.context()
        self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"EARLY_ACCEPTED")
    def test_missing_owner_state(self):self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"DENY_NO_OWNER_STATE")
    def test_stale_revision(self):
        self.context(4)
        self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"DENY_STALE_OWNER_STATE")
    def test_revoked_context(self):
        self.context(context_valid=False)
        self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"DENY_OWNER_SAFEGUARDS")
    def test_rights_guard(self):
        self.context(rights_ok=False)
        self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"DENY_OWNER_SAFEGUARDS")
    def test_necessity_guard(self):
        self.context(necessity_ok=False)
        self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"DENY_OWNER_SAFEGUARDS")
    def test_proportionality_guard(self):
        self.context(proportionality_ok=False)
        self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"DENY_OWNER_SAFEGUARDS")
    def test_missing_evidence(self):
        self.context()
        self.assertEqual(self.m.accept_atomic("D",None,self.s),"DENY_MISSING_CONTEXT_EVIDENCE")
    def test_expired_evidence(self):
        self.context()
        self.assertEqual(self.m.accept_atomic("D",self.e,replace(self.s,now=200)),"DENY_EXPIRED")
    def test_wrong_decision_binding(self):
        self.context()
        self.assertEqual(self.m.accept_atomic("D",replace(self.e,decision_id="X"),self.s),"DENY_DECISION_BINDING")
    def test_unverified_issuer(self):
        self.context()
        self.assertEqual(self.m.accept_atomic("D",self.e,replace(self.s,independently_verified_issuers=frozenset())),"DENY_ISSUER")
    def test_provenance_durable(self):
        self.context()
        self.m.accept_atomic("D",self.e,self.s)
        self.assertEqual(self.m.provenance("D"),("REF-3","OWNER","REVIEWER",3,150))
    def test_replay_does_not_create_second_acceptance(self):
        self.context()
        self.m.accept_atomic("D",self.e,self.s)
        self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"ALREADY_ACCEPTED")
    def test_monotonic_owner_revision(self):
        self.context(4)
        self.assertEqual(self.context(3),"DENY_NONMONOTONIC_REVISION")
    def test_changed_context_before_acceptance(self):
        self.context()
        self.context(4,context_valid=False)
        self.assertEqual(self.m.accept_atomic("D",self.e,self.s),"DENY_STALE_OWNER_STATE")
    def test_late_third_still_recorded(self):
        self.context()
        self.m.accept_atomic("D",self.e,self.s)
        self.assertEqual(self.m.vote(decision_id="D",position="P3",steward="S3",choice="A",event_id="E3",eligible=True,context_ok=True),"LATE_RECORDED")
    def test_no_host_authority(self):
        self.context()
        self.m.accept_atomic("D",self.e,self.s)
        self.assertFalse(self.m.status("D")["execution_authorised"])
    def test_competing_acceptance_single_winner(self):
        self.context()
        barrier=threading.Barrier(2)
        results=[]
        def worker():
            m=AtomicContextualDecision(self.path)
            barrier.wait()
            results.append(m.accept_atomic("D",self.e,self.s))
        ts=[threading.Thread(target=worker) for _ in range(2)]
        for t in ts:t.start()
        for t in ts:t.join()
        self.assertCountEqual(results,["EARLY_ACCEPTED","ALREADY_ACCEPTED"])
    def test_unknown_decision(self):
        self.context()
        self.assertEqual(self.m.accept_atomic("UNKNOWN",self.e,self.s),"DENY_DECISION_BINDING")

if __name__=="__main__":unittest.main()
