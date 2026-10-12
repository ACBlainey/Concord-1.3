"""Threaded adversarial fixture; NOT distributed or production proof."""
import unittest
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from decision_state_concurrency_094 import AtomicDecisionJournal

class ConcurrencyFixtureTests(unittest.TestCase):
    def test_simultaneous_conflicting_votes_one_wins(self):
        d=AtomicDecisionJournal("D1",True);barrier=Barrier(2)
        def submit(ballot):
            barrier.wait()
            return d.accept_vote("D1","P1","s1",ballot)
        with ThreadPoolExecutor(max_workers=2) as pool:
            a=pool.submit(submit,"F");b=pool.submit(submit,"A")
            outcomes={a.result(),b.result()}
        self.assertEqual(outcomes,{"ACCEPTED","CONFLICT"})
        self.assertEqual(len(d.positions),1)
    def test_parallel_matching_positions_fix_result(self):
        d=AtomicDecisionJournal("D1",True);barrier=Barrier(2)
        def submit(p,s):
            barrier.wait()
            return d.accept_vote("D1",p,s,"F")
        with ThreadPoolExecutor(max_workers=2) as pool:
            a=pool.submit(submit,"P1","s1");b=pool.submit(submit,"P2","s2")
            self.assertEqual([a.result(),b.result()].count("ACCEPTED"),2)
        self.assertEqual(d.result,"F")
    def test_many_identical_replays_once(self):
        d=AtomicDecisionJournal("D1",True)
        with ThreadPoolExecutor(max_workers=12) as pool:
            outcomes=list(pool.map(lambda _:d.accept_vote("D1","P1","s1","F"),range(100)))
        self.assertEqual(outcomes.count("ACCEPTED"),1)
        self.assertEqual(outcomes.count("DUPLICATE"),99)
    def test_simultaneous_action_claim_once(self):
        d=AtomicDecisionJournal("D1",True)
        d.accept_vote("D1","P1","s1","F");d.accept_vote("D1","P2","s2","F")
        with ThreadPoolExecutor(max_workers=12) as pool:
            outcomes=list(pool.map(lambda _:d.claim_action("D1","A1",host_authorised=True),range(100)))
        self.assertEqual(outcomes.count("CLAIMED"),1)
        self.assertEqual(outcomes.count("RECONCILE"),99)
    def test_uncertain_action_never_blindly_reclaimed(self):
        d=AtomicDecisionJournal("D1",True)
        d.accept_vote("D1","P1","s1","F");d.accept_vote("D1","P2","s2","F")
        self.assertEqual(d.claim_action("D1","A1",host_authorised=True),"CLAIMED")
        self.assertEqual(d.record_effect("A1",confirmed=False),"UNCERTAIN")
        self.assertEqual(d.claim_action("D1","A1",host_authorised=True),"RECONCILE")
    def test_confirmed_action_duplicate(self):
        d=AtomicDecisionJournal("D1",True)
        d.accept_vote("D1","P1","s1","F");d.accept_vote("D1","P2","s2","F")
        d.claim_action("D1","A1",host_authorised=True)
        self.assertEqual(d.record_effect("A1",confirmed=True),"DONE")
        self.assertEqual(d.claim_action("D1","A1",host_authorised=True),"DUPLICATE")
    def test_wrong_decision_id(self):
        d=AtomicDecisionJournal("D1",True)
        self.assertEqual(d.accept_vote("D2","P1","s1","F"),"REJECTED")
    def test_no_host_authority_action(self):
        d=AtomicDecisionJournal("D1",True)
        d.accept_vote("D1","P1","s1","F");d.accept_vote("D1","P2","s2","F")
        self.assertEqual(d.claim_action("D1","A1"),"REJECTED")
    def test_expired_ballot_mandate(self):
        d=AtomicDecisionJournal("D1",True)
        self.assertEqual(d.accept_vote("D1","P1","s1","F",mandate=False),"REJECTED")
    def test_closed_vote_rejected(self):
        d=AtomicDecisionJournal("D1",True)
        d.accept_vote("D1","P1","s1","F");d.accept_vote("D1","P2","s2","F")
        self.assertEqual(d.complete(),"CLOSED")
        self.assertEqual(d.accept_vote("D1","P3","s3","A"),"REJECTED")

if __name__=="__main__":unittest.main(verbosity=2)
