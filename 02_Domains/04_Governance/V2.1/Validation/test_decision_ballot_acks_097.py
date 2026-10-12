import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from decision_ballot_acks_097 import BallotAckJournal

class BallotAckTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory()
        self.path=Path(self.t.name)/"state.sqlite"
        self.j=BallotAckJournal(self.path)
        self.j.create("D",authorised=True)
    def tearDown(self):self.t.cleanup()
    def vote(self,p,s,v):return self.j.vote("D",p,s,v,mandate=True)
    def majority(self):
        self.vote("P1","s1","F");self.vote("P2","s2","F")
    def ack(self,**kw):
        x=dict(decision_id="D",action_id="A",owner="HOST",nonce="N",revision=2,evidence="E",decision="ACK",authenticated=True,scope_verified=True)
        x.update(kw);return self.j.ack(**x)
    def test_majority_persists_restart(self):
        self.majority();self.j=BallotAckJournal(self.path)
        self.assertEqual(self.j.state("D"),(2,"F"))
    def test_vote_replay_after_restart(self):
        self.vote("P1","s1","F");self.j=BallotAckJournal(self.path)
        self.assertEqual(self.vote("P1","s1","F"),"DUPLICATE")
    def test_conflicting_ballot(self):
        self.vote("P1","s1","F")
        self.assertEqual(self.vote("P1","s1","A"),"CONFLICT")
    def test_steward_cannot_vote_twice(self):
        self.vote("P1","s1","F")
        self.assertEqual(self.vote("P2","s1","F"),"REPEATED_STEWARD")
    def test_late_third_no_revision_change(self):
        self.majority()
        self.assertEqual(self.vote("P3","s3","A"),"PROVENANCE_ONLY")
        self.assertEqual(self.j.state("D"),(2,"F"))
    def test_concurrent_ballots_atomic(self):
        with ThreadPoolExecutor(max_workers=2) as pool:
            a=pool.submit(self.vote,"P1","s1","F");b=pool.submit(self.vote,"P2","s2","F")
            self.assertEqual([a.result(),b.result()].count("ACCEPTED"),2)
        self.assertEqual(self.j.state("D"),(2,"F"))
    def test_concurrent_duplicate_ballots(self):
        with ThreadPoolExecutor(max_workers=8) as pool:
            results=list(pool.map(lambda _:self.vote("P1","s1","F"),range(30)))
        self.assertEqual(results.count("ACCEPTED"),1)
    def test_action_requires_matching_revision(self):
        self.majority()
        self.assertEqual(self.j.claim("D","A",host_authorised=True,expected_revision=1),"REJECTED")
        self.assertEqual(self.j.claim("D","A",host_authorised=True,expected_revision=2),"CLAIMED")
    def test_action_restart_no_repeat(self):
        self.majority();self.j.claim("D","A",host_authorised=True,expected_revision=2)
        self.j=BallotAckJournal(self.path)
        self.assertEqual(self.j.claim("D","A",host_authorised=True,expected_revision=2),"RECONCILE")
    def test_ack_revision_mismatch(self):
        self.majority();self.j.claim("D","A",host_authorised=True,expected_revision=2)
        self.assertEqual(self.ack(revision=1),"REVISION_CONFLICT")
    def test_ack_persists_restart(self):
        self.majority();self.j.claim("D","A",host_authorised=True,expected_revision=2)
        self.assertEqual(self.ack(),"RECORDED")
        self.j=BallotAckJournal(self.path)
        self.assertEqual(self.ack(),"IDEMPOTENT")
    def test_ack_does_not_execute_effect(self):
        self.majority();self.j.claim("D","A",host_authorised=True,expected_revision=2)
        self.assertEqual(self.ack(),"RECORDED")
        self.assertEqual(self.j.claim("D","A",host_authorised=True,expected_revision=2),"RECONCILE")
    def test_uncertain_effect_restart(self):
        self.majority();self.j.claim("D","A",host_authorised=True,expected_revision=2)
        self.assertEqual(self.j.effect("D","A"),"UNCERTAIN")
        self.j=BallotAckJournal(self.path)
        self.assertEqual(self.j.claim("D","A",host_authorised=True,expected_revision=2),"RECONCILE")
    def test_done_action_not_reexecuted(self):
        self.majority();self.j.claim("D","A",host_authorised=True,expected_revision=2)
        self.assertEqual(self.j.effect("D","A","HOST-RECEIPT"),"DONE")
        self.j=BallotAckJournal(self.path)
        self.assertEqual(self.j.claim("D","A",host_authorised=True,expected_revision=2),"DUPLICATE")
    def test_ack_unknown_action(self):
        self.assertEqual(self.ack(),"UNKNOWN_ACTION")
    def test_ack_unverified(self):
        self.majority();self.j.claim("D","A",host_authorised=True,expected_revision=2)
        self.assertEqual(self.ack(authenticated=False),"REJECTED")
if __name__=="__main__":unittest.main(verbosity=2)
