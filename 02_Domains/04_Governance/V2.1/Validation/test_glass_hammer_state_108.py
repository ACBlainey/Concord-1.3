"""Fixture-only adversarial validation of context-guarded ballot consumption."""
import os
import tempfile
import threading
import unittest
from glass_hammer_state_108 import BallotMachine


class GlassHammerTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.path=os.path.join(self.tmp.name,"ballots.sqlite")
        self.m=BallotMachine(self.path)
        self.m.create("D1","Approve proposal?")
    def tearDown(self): self.tmp.cleanup()
    def vote(self, **kwargs):
        args=dict(decision_id="D1",position="P1",steward="S1",choice="F",event_id="E1",expected_state="OPEN",eligible=True,context_ok=True)
        args.update(kwargs)
        return self.m.submit(**args)
    def test_first_vote(self): self.assertEqual(self.vote(),"ACCEPTED")
    def test_no_eligibility(self): self.assertEqual(self.vote(eligible=False),"DENY_ELIGIBILITY")
    def test_no_context(self): self.assertEqual(self.vote(context_ok=False),"DENY_CONTEXT")
    def test_wrong_state(self): self.assertEqual(self.vote(expected_state="CLOSED"),"DENY_STATE")
    def test_bad_choice(self): self.assertEqual(self.vote(choice="X"),"DENY_INPUT")
    def test_unknown_decision(self): self.assertEqual(self.vote(decision_id="MISSING"),"DENY_UNKNOWN_DECISION")
    def test_same_event_replay(self):
        self.vote()
        self.assertEqual(self.vote(),"DUPLICATE")
        self.assertEqual(len(self.m.snapshot("D1")[1]),1)
    def test_replay_new_id(self):
        self.vote()
        self.assertEqual(self.vote(event_id="E2"),"DENY_CONSUMED")
    def test_replay_other_steward_same_position(self):
        self.vote()
        self.assertEqual(self.vote(event_id="E2",steward="S2"),"DENY_CONSUMED")
    def test_event_collision(self):
        self.vote()
        self.assertEqual(self.vote(event_id="E1",position="P2",steward="S2"),"DENY_EVENT_COLLISION")
    def test_steward_cannot_take_two_positions(self):
        self.vote()
        self.assertEqual(self.vote(event_id="E2",position="P2"),"DENY_REPEATED_STEWARD")
    def test_two_matching_resolves(self):
        self.vote()
        self.assertEqual(self.vote(position="P2",steward="S2",event_id="E2"),"ACCEPTED")
        self.assertEqual(self.m.result("D1"),"F")
        self.assertEqual(self.vote(position="P3",steward="S3",event_id="E3"),"DENY_STATE")
    def test_abstain_not_majority(self):
        self.vote(choice="U")
        self.vote(position="P2",steward="S2",event_id="E2",choice="F")
        self.vote(position="P3",steward="S3",event_id="E3",choice="A")
        self.assertEqual(self.m.result("D1"),"U")
        self.assertEqual(self.m.snapshot("D1")[0],"CLOSED")
    def test_restart_persists_consumption(self):
        self.vote()
        m2=BallotMachine(self.path)
        self.assertEqual(m2.submit(decision_id="D1",position="P1",steward="S1",choice="F",event_id="E2",expected_state="OPEN",eligible=True,context_ok=True),"DENY_CONSUMED")
    def test_competing_same_position(self):
        barrier=threading.Barrier(2)
        out=[]
        def worker(i):
            m=BallotMachine(self.path)
            barrier.wait()
            out.append(m.submit(decision_id="D1",position="P1",steward="S"+str(i),choice="F",event_id="E"+str(i),expected_state="OPEN",eligible=True,context_ok=True))
        threads=[threading.Thread(target=worker,args=(i,)) for i in (1,2)]
        for t in threads:t.start()
        for t in threads:t.join()
        self.assertCountEqual(out,["ACCEPTED","DENY_CONSUMED"])
        self.assertEqual(len(self.m.snapshot("D1")[1]),1)
    def test_distinct_decisions_independent(self):
        self.m.create("D2","Another question?")
        self.vote()
        self.assertEqual(self.vote(decision_id="D2",event_id="E2"),"ACCEPTED")


if __name__=="__main__": unittest.main()
