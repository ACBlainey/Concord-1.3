import unittest
from g05_reconciliation_acknowledgements_090 import Acknowledgement,AcknowledgementJournal
class JournalTests(unittest.TestCase):
 def setUp(self):
  self.j=AcknowledgementJournal(("CONTINUITY","SUCCESSION","HISTORICAL"),1,2,"EV")
 def a(self,owner="CONTINUITY",**kw):
  d=dict(event_ref="EV",owner_ref=owner,source_revision=1,target_revision=2,evidence_ref="EVID",decision="ACK",nonce="N-"+owner);d.update(kw);return Acknowledgement(**d)
 def send(self,a=None,auth=True,scope=True):return self.j.submit(a or self.a(),auth,scope)
 def test_first_ack(self):self.assertEqual(self.send(),"RECORDED")
 def test_missing_owners(self):self.send();self.assertEqual(len(self.j.status()["pending_owners"]),2)
 def test_all_owners(self):
  for o in self.j.expected_owners:self.send(self.a(o))
  self.assertTrue(self.j.status()["projection_consensus"])
 def test_no_authority(self):self.assertFalse(self.j.status()["authority_granted"])
 def test_no_closure(self):self.assertFalse(self.j.status()["duty_closed"])
 def test_no_orphan_clear(self):self.assertFalse(self.j.status()["orphan_cleared"])
 def test_no_mutation(self):self.assertFalse(self.j.status()["source_mutated"])
 def test_unknown_owner(self):self.assertEqual(self.send(self.a("ATTACKER")),"UNKNOWN_OWNER")
 def test_wrong_event(self):self.assertEqual(self.send(self.a(event_ref="OTHER")),"EVENT_MISMATCH")
 def test_no_authentication(self):self.assertEqual(self.send(auth=False),"UNVERIFIED_OWNER")
 def test_no_scope(self):self.assertEqual(self.send(scope=False),"UNVERIFIED_OWNER")
 def test_missing_evidence(self):self.assertEqual(self.send(self.a(evidence_ref="")),"INCOMPLETE_PROVENANCE")
 def test_stale_source(self):self.assertEqual(self.send(self.a(source_revision=0)),"REVISION_CONFLICT")
 def test_wrong_target(self):self.assertEqual(self.send(self.a(target_revision=3)),"REVISION_CONFLICT")
 def test_idempotent(self):self.send();self.assertEqual(self.send(),"IDEMPOTENT")
 def test_replay_conflict(self):self.send();self.assertEqual(self.send(self.a("SUCCESSION",nonce="N-CONTINUITY")),"REPLAY_CONFLICT")
 def test_owner_conflict(self):self.send();self.assertEqual(self.send(self.a(nonce="NEW",evidence_ref="DIFFERENT")),"OWNER_CONFLICT")
 def test_rejection_blocks(self):
  for o in self.j.expected_owners:self.send(self.a(o,decision="REJECT" if o=="HISTORICAL" else "ACK"))
  self.assertFalse(self.j.status()["projection_consensus"])
 def test_invalid_decision(self):self.assertEqual(self.send(self.a(decision="GRANT")),"INVALID_DECISION")
 def test_no_partial_consensus(self):self.assertFalse(self.j.status()["projection_consensus"])
if __name__=="__main__":unittest.main()
