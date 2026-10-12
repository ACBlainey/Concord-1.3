"""ACKS/decision cross-module recovery tests. In-memory only, NOT durable or deployed."""
import unittest
from decision_state_concurrency_094 import AtomicDecisionJournal
from g05_reconciliation_acknowledgements_090 import Acknowledgement, AcknowledgementJournal

class DecisionAcksRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.d=AtomicDecisionJournal("DEC-1",True)
        self.d.accept_vote("DEC-1","P1","S1","F")
        self.d.accept_vote("DEC-1","P2","S2","F")
        self.acks=AcknowledgementJournal(("HOST",),1,2,"DEC-1:A1")
    def ack(self,**changes):
        args=dict(event_ref="DEC-1:A1",owner_ref="HOST",source_revision=1,
                  target_revision=2,evidence_ref="HOST-RECEIPT-1",decision="ACK",nonce="N1")
        args.update(changes)
        return Acknowledgement(**args)
    def test_lost_ack_after_effect_does_not_repeat(self):
        self.assertEqual(self.d.claim_action("DEC-1","A1",host_authorised=True),"CLAIMED")
        self.assertEqual(self.d.record_effect("A1",confirmed=True),"DONE")
        self.assertEqual(self.d.claim_action("DEC-1","A1",host_authorised=True),"DUPLICATE")
        self.assertEqual(self.acks.submit(self.ack(),authenticated=True,scope_verified=True),"RECORDED")
    def test_lost_ack_before_effect_requires_reconciliation(self):
        self.assertEqual(self.d.claim_action("DEC-1","A1",host_authorised=True),"CLAIMED")
        self.assertEqual(self.d.claim_action("DEC-1","A1",host_authorised=True),"RECONCILE")
        self.assertFalse(self.acks.status()["projection_consensus"])
    def test_uncertain_effect_reconnect_not_reexecute(self):
        self.d.claim_action("DEC-1","A1",host_authorised=True)
        self.assertEqual(self.d.record_effect("A1",confirmed=False),"UNCERTAIN")
        self.assertEqual(self.d.claim_action("DEC-1","A1",host_authorised=True),"RECONCILE")
    def test_ack_does_not_grant_authority(self):
        self.assertEqual(self.acks.submit(self.ack(),authenticated=True,scope_verified=True),"RECORDED")
        self.assertFalse(self.acks.status()["authority_granted"])
        self.assertFalse(self.acks.status()["duty_closed"])
    def test_ack_replay_idempotent(self):
        a=self.ack()
        self.assertEqual(self.acks.submit(a,authenticated=True,scope_verified=True),"RECORDED")
        self.assertEqual(self.acks.submit(a,authenticated=True,scope_verified=True),"IDEMPOTENT")
    def test_revision_mismatch_blocks_projection(self):
        self.assertEqual(self.acks.submit(self.ack(source_revision=0),authenticated=True,scope_verified=True),"REVISION_CONFLICT")
        self.assertFalse(self.acks.status()["projection_consensus"])
    def test_wrong_event_ack_rejected(self):
        self.assertEqual(self.acks.submit(self.ack(event_ref="DEC-OTHER:A1"),authenticated=True,scope_verified=True),"EVENT_MISMATCH")
    def test_unauthenticated_ack_rejected(self):
        self.assertEqual(self.acks.submit(self.ack(),authenticated=False,scope_verified=True),"UNVERIFIED_OWNER")
    def test_rejected_ack_not_success(self):
        self.assertEqual(self.acks.submit(self.ack(decision="REJECT"),authenticated=True,scope_verified=True),"RECORDED")
        self.assertFalse(self.acks.status()["projection_consensus"])
    def test_ack_not_proof_of_external_effect(self):
        self.assertEqual(self.acks.submit(self.ack(),authenticated=True,scope_verified=True),"RECORDED")
        self.assertTrue(self.acks.status()["projection_consensus"])
        self.assertNotIn("A1",self.d.actions)  # ACK journal has no physical-effect evidence
if __name__=="__main__":unittest.main(verbosity=2)
