import unittest
from g05_bta_async_evidence_075 import Evidence,EvidenceLedger

class AsyncEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.l=EvidenceLedger()
        self.a=Evidence("E1","TX1","OWNER:ACCESS","access",1,"APPROVED","EV1","GTP-A")
    def test_arrival(self):self.assertEqual(self.l.ingest(self.a),"ACCEPTED")
    def test_replay(self):
        self.l.ingest(self.a);self.assertEqual(self.l.ingest(self.a),"REPLAY")
    def test_event_id_conflict(self):
        self.l.ingest(self.a);b=Evidence("E1","TX1","OWNER:ACCESS","access",1,"DENIED","EV2","GTP-A")
        self.assertEqual(self.l.ingest(b),"EVENT_ID_CONFLICT")
    def test_stale(self):
        self.l.ingest(self.a);b=Evidence("E2","TX1","OWNER:ACCESS","access",0,"DENIED","EV2","GTP-A")
        self.assertEqual(self.l.ingest(b),"STALE")
    def test_equal_revision_conflict(self):
        self.l.ingest(self.a);b=Evidence("E2","TX1","OWNER:ACCESS","access",1,"DENIED","EV2","GTP-A")
        self.assertEqual(self.l.ingest(b),"CONFLICT")
        self.assertFalse(self.l.eligible("TX1",{("OWNER:ACCESS","access","GTP-A")}))
    def test_cross_area_not_inferred(self):
        self.l.ingest(self.a)
        self.assertFalse(self.l.eligible("TX1",{("OWNER:ACCESS","access","GTP-B")}))
    def test_other_owner_not_inferred(self):
        self.l.ingest(self.a)
        self.assertFalse(self.l.eligible("TX1",{("OWNER:RESPONSIBILITY","handoff","GTP-A")}))
    def test_correct_exact_owner(self):
        self.l.ingest(self.a)
        self.assertTrue(self.l.eligible("TX1",{("OWNER:ACCESS","access","GTP-A")}))
    def test_wrong_transition(self):
        self.l.ingest(self.a)
        self.assertFalse(self.l.eligible("TX2",{("OWNER:ACCESS","access","GTP-A")}))
    def test_denial(self):
        b=Evidence("E2","TX1","OWNER:ACCESS","access",2,"DENIED","EV2","GTP-A")
        self.l.ingest(b)
        self.assertFalse(self.l.eligible("TX1",{("OWNER:ACCESS","access","GTP-A")}))
    def test_clock_pause_does_not_prevent_expiry(self):
        self.l.activate_emergency("GTP-A");self.l.expire_emergency("GTP-A")
        self.assertTrue(self.l.clock_paused)
        self.assertNotIn("GTP-A",self.l.emergency_active)
        self.assertIn(("GTP-A","RECOVERY_REVIEW"),self.l.surviving_duties)
    def test_independent_area_expiry(self):
        self.l.activate_emergency("GTP-A");self.l.activate_emergency("GTP-B")
        self.l.expire_emergency("GTP-A")
        self.assertIn("GTP-B",self.l.emergency_active)
        self.assertNotIn("GTP-A",self.l.emergency_active)
if __name__=="__main__":unittest.main(verbosity=2)
