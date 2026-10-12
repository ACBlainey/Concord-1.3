"""Durable local restart and concurrent claim tests; no real external effects."""
import tempfile
import unittest
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from decision_acks_durable_096 import DurableDecisionRecovery

class DurableRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.path=Path(self.tmp.name)/"journal.db"
        self.j=DurableDecisionRecovery(self.path)
        self.j.decision("D1","F",True)
    def tearDown(self):self.tmp.cleanup()
    def claim(self,action="A1"):return self.j.claim("D1",action,host_authorised=True)
    def ack(self,**kwargs):
        a=dict(decision_id="D1",action_id="A1",owner="HOST",nonce="N1",revision=1,evidence="RECEIPT",decision="ACK",authenticated=True,scope_verified=True)
        a.update(kwargs);return self.j.ack(**a)
    def test_claim_persists_restart(self):
        self.assertEqual(self.claim(),"CLAIMED")
        self.j=DurableDecisionRecovery(self.path)
        self.assertEqual(self.claim(),"RECONCILE")
    def test_effect_receipt_persists_restart(self):
        self.claim();self.assertEqual(self.j.effect("D1","A1",receipt="HOST-EFFECT"),"DONE")
        self.j=DurableDecisionRecovery(self.path)
        self.assertEqual(self.j.status("D1","A1"),("DONE","HOST-EFFECT"))
        self.assertEqual(self.claim(),"DUPLICATE")
    def test_uncertain_effect_never_blindly_retries(self):
        self.claim();self.assertEqual(self.j.effect("D1","A1"),"UNCERTAIN")
        self.j=DurableDecisionRecovery(self.path)
        self.assertEqual(self.claim(),"RECONCILE")
    def test_lost_ack_after_effect(self):
        self.claim();self.j.effect("D1","A1",receipt="R1")
        self.j=DurableDecisionRecovery(self.path)
        self.assertEqual(self.claim(),"DUPLICATE")
        self.assertEqual(self.ack(),"RECORDED")
    def test_ack_persists_and_replay_idempotent(self):
        self.claim();self.assertEqual(self.ack(),"RECORDED")
        self.j=DurableDecisionRecovery(self.path)
        self.assertEqual(self.ack(),"IDEMPOTENT")
    def test_ack_does_not_prove_effect(self):
        self.claim();self.ack()
        self.assertEqual(self.j.status("D1","A1"),("CLAIMED",None))
    def test_replayed_nonce_different_owner_rejected(self):
        self.claim();self.ack()
        self.assertEqual(self.ack(owner="OTHER"),"REPLAY_CONFLICT")
    def test_conflicting_ack_rejected(self):
        self.claim();self.ack()
        self.assertEqual(self.ack(evidence="DIFFERENT"),"OWNER_CONFLICT")
    def test_wrong_action_ack_rejected(self):
        self.assertEqual(self.ack(action_id="UNKNOWN"),"UNKNOWN_ACTION")
    def test_unverified_ack_rejected(self):
        self.claim();self.assertEqual(self.ack(authenticated=False),"REJECTED")
    def test_no_host_authority_rejected(self):
        self.assertEqual(self.j.claim("D1","A1"),"REJECTED")
    def test_no_result_no_action(self):
        self.j.decision("D2","U",True)
        self.assertEqual(self.j.claim("D2","A1",host_authorised=True),"REJECTED")
    def test_many_simultaneous_claims_one_wins(self):
        with ThreadPoolExecutor(max_workers=8) as pool:
            results=list(pool.map(lambda _:DurableDecisionRecovery(self.path).claim("D1","A1",host_authorised=True),range(40)))
        self.assertEqual(results.count("CLAIMED"),1)
        self.assertEqual(results.count("RECONCILE"),39)
    def test_distinct_actions_survive_restart(self):
        self.claim("A1");self.claim("A2")
        self.j=DurableDecisionRecovery(self.path)
        self.assertEqual(self.j.status("D1","A1")[0],"CLAIMED")
        self.assertEqual(self.j.status("D1","A2")[0],"CLAIMED")
if __name__=="__main__":unittest.main(verbosity=2)
