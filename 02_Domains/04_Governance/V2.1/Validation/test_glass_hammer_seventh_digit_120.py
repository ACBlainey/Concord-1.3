import os
import tempfile
import unittest
from glass_hammer_seventh_digit_120 import SeventhDigitDecision,IndependentCaseLock

class SeventhDigit120(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.m=SeventhDigitDecision(os.path.join(self.tmp.name,"decision.sqlite"))
        self.m.create("D","Question?")
        self.lock=IndependentCaseLock({"S1":"111111","S2":"222222","S3":"333333"})
    def tearDown(self):self.tmp.cleanup()
    def vote(self,p,s,c,e):
        return self.m.vote(decision_id="D",position=p,steward=s,choice=c,event_id=e,eligible=True,context_ok=True)
    def test_initial_zero(self):self.assertEqual(self.m.seventh_digit("D"),{"status":"OK","digit":0})
    def test_first_vote_one(self):
        self.vote("P1","S1","F","E1")
        self.assertEqual(self.m.seventh_digit("D")["digit"],1)
    def test_two_votes_two(self):
        self.vote("P1","S1","F","E1");self.vote("P2","S2","A","E2")
        self.assertEqual(self.m.seventh_digit("D")["digit"],2)
    def test_three_votes_three(self):
        for p,s,c,e in (("P1","S1","F","E1"),("P2","S2","A","E2"),("P3","S3","U","E3")):self.vote(p,s,c,e)
        self.assertEqual(self.m.seventh_digit("D")["digit"],3)
    def test_choice_independent(self):
        observed=[]
        for i,choice in enumerate(("F","A","U")):
            d="D"+str(i);self.m.create(d,"Q")
            self.m.vote(decision_id=d,position="P1",steward="S1",choice=choice,event_id="X"+str(i),eligible=True,context_ok=True)
            observed.append(self.m.seventh_digit(d))
        self.assertEqual(observed,[{"status":"OK","digit":1}]*3)
    def test_duplicate_event_no_increment(self):
        self.vote("P1","S1","F","E1");self.vote("P1","S1","F","E1")
        self.assertEqual(self.m.seventh_digit("D")["digit"],1)
    def test_attempted_second_vote_no_increment(self):
        self.vote("P1","S1","F","E1");self.vote("P1","S1","A","E2")
        self.assertEqual(self.m.seventh_digit("D")["digit"],1)
    def test_first_vote_does_not_block_other_locks(self):
        self.vote("P1","S1","F","E1")
        self.assertEqual(self.lock.open_case("S2","222222"),"OPENED")
        self.assertEqual(self.lock.open_case("S3","333333"),"OPENED")
    def test_second_vote_does_not_block_third_lock(self):
        self.vote("P1","S1","F","E1");self.vote("P2","S2","F","E2")
        self.assertEqual(self.lock.open_case("S3","333333"),"OPENED")
    def test_wrong_combination_denied_independent_of_count(self):
        self.vote("P1","S1","F","E1")
        self.assertEqual(self.lock.open_case("S2","WRONG"),"DENY_COMBINATION")
    def test_indicator_failure_does_not_block_lock(self):
        self.assertEqual(self.m.seventh_digit("D",indicator_available=False),{"status":"UNAVAILABLE"})
        self.assertEqual(self.lock.open_case("S2","222222"),"OPENED")
    def test_indicator_failure_does_not_block_vote(self):
        self.m.seventh_digit("D",indicator_available=False)
        self.assertEqual(self.vote("P1","S1","A","E1"),"ACCEPTED")
    def test_indicator_no_vote_contents(self):
        self.vote("P1","S1","F","E1")
        r=self.m.steward_display("D",steward="S2",authority_verified=True)
        self.assertEqual(set(r),{"status","digit"})
    def test_display_denied_without_authority(self):
        self.assertEqual(self.m.steward_display("D",steward="S2")["status"],"DENY_AUTHORITY")
    def test_unknown_decision_denied(self):
        self.assertEqual(self.m.seventh_digit("X")["status"],"DENY_UNKNOWN_DECISION")
    def test_concern_does_not_decrement(self):
        self.vote("P1","S1","F","E1")
        self.m.record_concern(concern_id="C",decision_id="D",steward="S1",position="P1",explanation="Mistake",evidence_ref="REF",event_id="CE")
        self.assertEqual(self.m.seventh_digit("D")["digit"],1)
    def test_early_acceptance_third_vote_count(self):
        self.vote("P1","S1","F","E1");self.vote("P2","S2","F","E2")
        self.assertEqual(self.m.accept("D",early_context_justified=True,basis="TEST"),"EARLY_ACCEPTED")
        self.assertEqual(self.m.seventh_digit("D")["digit"],2)
        self.assertEqual(self.vote("P3","S3","A","E3"),"LATE_RECORDED")
        self.assertEqual(self.m.seventh_digit("D")["digit"],3)
    def test_early_acceptance_does_not_block_third_lock(self):
        self.vote("P1","S1","F","E1");self.vote("P2","S2","F","E2")
        self.m.accept("D",early_context_justified=True,basis="TEST")
        self.assertEqual(self.lock.open_case("S3","333333"),"OPENED")
    def test_lock_does_not_read_vote_database(self):
        self.m.seventh_digit("D",indicator_available=False)
        self.assertEqual(self.lock.open_case("S1","111111"),"OPENED")
        self.assertTrue(self.lock.is_open("S1"))
    def test_reopening_case_no_new_ballot(self):
        self.lock.open_case("S1","111111")
        self.vote("P1","S1","F","E1")
        self.lock.open_case("S1","111111")
        self.assertEqual(self.m.seventh_digit("D")["digit"],1)

if __name__=="__main__":unittest.main()
