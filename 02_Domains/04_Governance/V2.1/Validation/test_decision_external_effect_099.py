import tempfile
import unittest
from pathlib import Path
from decision_external_effect_099 import HostLedger,Receiver

class CrashWindowTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();root=Path(self.t.name)
        self.hp=root/"host.db";self.rp=root/"receiver.db"
        self.h=HostLedger(self.hp);self.r=Receiver(self.rp)
        self.r.accept("A","payload",authorised=True)
    def tearDown(self):self.t.cleanup()
    def crash(self):return self.r.execute("A",self.h,host_authorised=True,crash_after_host=True)
    def test_crash_window_host_effect_exists(self):
        self.assertEqual(self.crash(),"SIMULATED_CRASH")
        self.assertEqual(self.r.status("A")[1],"CLAIMED")
        self.assertIsNotNone(self.h.query("A"))
    def test_restart_reconcile(self):
        self.crash();self.r=Receiver(self.rp);self.h=HostLedger(self.hp)
        self.assertEqual(self.r.reconcile("A",self.h,host_status_trusted=True),"RECONCILED")
        self.assertEqual(self.r.status("A")[1],"DONE")
    def test_no_second_effect_after_crash(self):
        self.crash();self.r=Receiver(self.rp)
        self.assertEqual(self.r.execute("A",self.h,host_authorised=True),"DONE")
        self.assertEqual(self.h.apply("A","payload",host_authorised=True)[0],"IDEMPOTENT")
    def test_no_blind_retry_when_uncertain(self):
        self.crash();self.r.mark_uncertain("A")
        self.assertEqual(self.r.execute("A",self.h,host_authorised=True),"RECONCILE")
    def test_unknown_host_absence_not_failure(self):
        self.assertEqual(self.r.reconcile("A",self.h,host_status_trusted=True),"UNCONFIRMED_ABSENCE")
    def test_untrusted_host_status(self):
        self.crash();self.assertEqual(self.r.reconcile("A",self.h),"UNVERIFIED_HOST")
    def test_effect_conflict(self):
        self.h.apply("A","different",host_authorised=True)
        self.assertEqual(self.r.reconcile("A",self.h,host_status_trusted=True),"EFFECT_CONFLICT")
    def test_no_effect_without_host_grant(self):
        self.assertEqual(self.r.execute("A",self.h),"RECONCILE")
        self.assertIsNone(self.h.query("A"))
    def test_duplicate_claim_does_not_change_payload(self):
        self.assertEqual(self.r.accept("A","different",authorised=True),"CONFLICT")
    def test_host_idempotency(self):
        self.assertEqual(self.h.apply("A","payload",host_authorised=True)[0],"APPLIED")
        self.assertEqual(self.h.apply("A","payload",host_authorised=True)[0],"IDEMPOTENT")
    def test_host_conflicting_replay(self):
        self.h.apply("A","payload",host_authorised=True)
        self.assertEqual(self.h.apply("A","different",host_authorised=True)[0],"CONFLICT")
    def test_reconciled_receipt_persists(self):
        self.crash();self.r.reconcile("A",self.h,host_status_trusted=True)
        self.r=Receiver(self.rp)
        self.assertEqual(self.r.status("A")[2],self.h.query("A")[1])
    def test_no_action_unknown(self):
        self.assertEqual(self.r.reconcile("MISSING",self.h,host_status_trusted=True),"UNKNOWN_ACTION")
    def test_successful_path(self):
        self.assertEqual(self.r.execute("A",self.h,host_authorised=True),"DONE")
        self.assertEqual(self.r.status("A")[1],"DONE")
    def test_done_does_not_execute_again(self):
        self.r.execute("A",self.h,host_authorised=True)
        self.assertEqual(self.r.execute("A",self.h,host_authorised=True),"RECONCILE")
    def test_host_grant_not_derived_from_receiver_acceptance(self):
        self.assertIsNone(self.h.query("A"))
if __name__=="__main__":unittest.main(verbosity=2)
