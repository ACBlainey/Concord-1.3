import tempfile
import unittest
from pathlib import Path
from decision_acks_transport_098 import Peer

class TransportRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();root=Path(self.t.name)
        self.sp=root/"sender.db";self.rp=root/"receiver.db"
        self.s=Peer(self.sp,"sender");self.r=Peer(self.rp,"receiver")
        self.s.prepare("E","ACT",2)
    def tearDown(self):self.t.cleanup()
    def deliver(self,**kw):
        args=dict(owner_valid=True,scope_valid=True);args.update(kw)
        return self.r.receive("E","ACT",2,**args)
    def test_lost_delivery(self):
        self.assertEqual(self.s.reconcile("E",self.r),"NOT_RECEIVED")
        self.assertEqual(self.s.status("E")[0],"PENDING")
    def test_lost_acceptance_ack(self):
        self.deliver();self.assertEqual(self.s.reconcile("E",self.r),"ACCEPTED")
    def test_lost_commit_ack(self):
        self.deliver();self.r.commit_effect("E","RECEIPT",host_authorised=True)
        self.assertEqual(self.s.reconcile("E",self.r),"COMMITTED")
    def test_receiver_restart_recovers(self):
        self.deliver();self.r=Peer(self.rp,"receiver")
        self.assertEqual(self.deliver(),"ACCEPTED")
    def test_sender_restart_recovers(self):
        self.deliver();self.s=Peer(self.sp,"sender")
        self.assertEqual(self.s.reconcile("E",self.r),"ACCEPTED")
    def test_effect_once_after_reconnect(self):
        self.deliver();self.assertEqual(self.r.commit_effect("E","R",host_authorised=True),"COMMITTED")
        self.r=Peer(self.rp,"receiver")
        self.assertEqual(self.r.commit_effect("E","R2",host_authorised=True),"REJECTED")
        self.assertEqual(self.r.status("E")[2],"R")
    def test_duplicate_delivery(self):
        self.deliver();self.assertEqual(self.deliver(),"ACCEPTED")
    def test_conflicting_payload(self):
        self.deliver();self.assertEqual(self.r.receive("E","DIFFERENT",2,owner_valid=True,scope_valid=True),"CONFLICT")
    def test_unverified_owner(self):
        self.assertEqual(self.deliver(owner_valid=False),"REJECTED")
    def test_unverified_scope(self):
        self.assertEqual(self.deliver(scope_valid=False),"REJECTED")
    def test_commit_requires_host_grant(self):
        self.deliver();self.assertEqual(self.r.commit_effect("E","R"),"REJECTED")
    def test_commit_requires_accepted_message(self):
        self.assertEqual(self.r.commit_effect("E","R",host_authorised=True),"REJECTED")
    def test_replayed_event_conflicting_revision(self):
        self.deliver();self.assertEqual(self.r.receive("E","ACT",3,owner_valid=True,scope_valid=True),"CONFLICT")
    def test_sender_prepare_conflict(self):
        self.assertEqual(self.s.prepare("E","OTHER",2),"CONFLICT")
    def test_no_inferred_effect_from_acceptance(self):
        self.deliver();self.assertEqual(self.r.status("E"),("ACCEPTED",2,None))
    def test_no_inferred_effect_from_sender_reconcile(self):
        self.deliver();self.s.reconcile("E",self.r)
        self.assertIsNone(self.s.status("E")[2])
if __name__=="__main__":unittest.main(verbosity=2)
