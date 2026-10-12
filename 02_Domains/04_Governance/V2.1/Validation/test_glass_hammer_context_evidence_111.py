import os
import tempfile
import unittest
from dataclasses import replace
from glass_hammer_context_evidence_111 import ContextEvidence,OwnerSnapshot,EvidenceGatedAcceptance,verify_context

class ContextEvidence111(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.adapter=EvidenceGatedAcceptance(os.path.join(self.tmp.name,"db.sqlite"))
        self.adapter.decision.create("D","Question?")
        for p,s,e in (("P1","S1","E1"),("P2","S2","E2")):
            self.adapter.decision.vote(decision_id="D",position=p,steward=s,choice="F",event_id=e,eligible=True,context_ok=True)
        self.e=ContextEvidence("D","OWNER","REVIEWER","Urgent safety response",3,100,200,"CTX-1","Delay would cause preventable harm","CIVIL_CONTACT_REVIEW")
        self.s=OwnerSnapshot("D",3,150,frozenset({"OWNER"}),frozenset({"OWNER"}),True,True,True,True)
    def tearDown(self):self.tmp.cleanup()
    def test_valid_independent_evidence(self):self.assertEqual(verify_context(self.e,self.s),"VALID")
    def test_valid_acceptance(self):self.assertEqual(self.adapter.accept("D",self.e,self.s),"EARLY_ACCEPTED")
    def test_missing_evidence(self):self.assertEqual(self.adapter.accept("D",None,self.s),"DENY_MISSING_CONTEXT_EVIDENCE")
    def test_wrong_decision(self):self.assertEqual(verify_context(replace(self.e,decision_id="X"),self.s),"DENY_DECISION_BINDING")
    def test_unauthorised_issuer(self):self.assertEqual(verify_context(replace(self.e,issuer="OTHER"),self.s),"DENY_ISSUER")
    def test_unverified_issuer(self):self.assertEqual(verify_context(self.e,replace(self.s,independently_verified_issuers=frozenset())),"DENY_ISSUER")
    def test_self_assertion(self):self.assertEqual(verify_context(replace(self.e,evaluator="OWNER"),self.s),"DENY_SELF_ASSERTION")
    def test_revision_mismatch(self):self.assertEqual(verify_context(replace(self.e,state_revision=2),self.s),"DENY_REVISION")
    def test_revocation(self):self.assertEqual(verify_context(replace(self.e,revoked=True),self.s),"DENY_INCOMPLETE")
    def test_missing_review_route(self):self.assertEqual(verify_context(replace(self.e,review_route=""),self.s),"DENY_INCOMPLETE")
    def test_expiry(self):self.assertEqual(verify_context(self.e,replace(self.s,now=200)),"DENY_EXPIRED")
    def test_future_attestation(self):self.assertEqual(verify_context(self.e,replace(self.s,now=99)),"DENY_EXPIRED")
    def test_stale_context(self):self.assertEqual(verify_context(self.e,replace(self.s,context_still_valid=False)),"DENY_CONTEXT")
    def test_rights_guard(self):self.assertEqual(verify_context(self.e,replace(self.s,rights_guard_ok=False)),"DENY_SAFEGUARDS")
    def test_necessity_guard(self):self.assertEqual(verify_context(self.e,replace(self.s,necessity_guard_ok=False)),"DENY_SAFEGUARDS")
    def test_proportionality_guard(self):self.assertEqual(verify_context(self.e,replace(self.s,proportionality_guard_ok=False)),"DENY_SAFEGUARDS")
    def test_context_not_predefined_category(self):
        e=replace(self.e,purpose="Unforeseen legitimate situation")
        self.assertEqual(verify_context(e,self.s),"VALID")
    def test_late_ballot_after_evidence_acceptance(self):
        self.adapter.accept("D",self.e,self.s)
        x=self.adapter.decision.vote(decision_id="D",position="P3",steward="S3",choice="A",event_id="E3",eligible=True,context_ok=True)
        self.assertEqual(x,"LATE_RECORDED")
        self.assertEqual(self.adapter.decision.status("D")["accepted"],"F")
    def test_result_never_execution_authority(self):
        self.adapter.accept("D",self.e,self.s)
        self.assertFalse(self.adapter.decision.status("D")["execution_authorised"])

if __name__=="__main__":unittest.main()
