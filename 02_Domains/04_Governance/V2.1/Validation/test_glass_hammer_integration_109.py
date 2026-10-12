import os
import tempfile
import unittest
from glass_hammer_state_108 import BallotMachine
from glass_hammer_integration_109 import project,crstl_records,execution_gate

class Integration109(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.path=os.path.join(self.tmp.name,"test.sqlite")
        self.m=BallotMachine(self.path)
        self.m.create("D1","Question?")
    def tearDown(self): self.tmp.cleanup()
    def vote(self,p="P1",s="S1",v="F",e="E1",**kw):
        return self.m.submit(decision_id="D1",position=p,steward=s,choice=v,event_id=e,expected_state="OPEN",eligible=True,context_ok=True,**kw)
    def test_unresolved_is_not_execution_authority(self):
        self.vote()
        self.assertEqual(execution_gate(project(self.m,"D1"),separate_host_authority=True,current_context=True),"DENY_UNRESOLVED")
    def test_resolved_is_not_execution_authority(self):
        self.vote()
        self.vote("P2","S2","F","E2")
        self.assertEqual(execution_gate(project(self.m,"D1")),"DENY_NO_FRESH_EXECUTION_AUTHORITY")
    def test_fresh_host_guard_only_enters_revalidation(self):
        self.vote()
        self.vote("P2","S2","F","E2")
        self.assertEqual(execution_gate(project(self.m,"D1"),separate_host_authority=True,current_context=True),"ELIGIBLE_FOR_HOST_REVALIDATION")
    def test_context_absent_denies_host(self):
        self.vote()
        self.vote("P2","S2","F","E2")
        self.assertEqual(execution_gate(project(self.m,"D1"),separate_host_authority=True),"DENY_NO_FRESH_EXECUTION_AUTHORITY")
    def test_clock_projection_not_needed_for_ballot(self):
        self.assertEqual(self.vote(),"ACCEPTED")
        self.assertEqual(len(crstl_records(self.m,"D1")),1)
    def test_projection_not_clock_authority(self):
        self.vote()
        self.assertFalse(crstl_records(self.m,"D1")[0]["clock_authority"])
    def test_crstl_projection_is_read_only(self):
        self.vote()
        a=self.m.snapshot("D1")
        crstl_records(self.m,"D1")
        self.assertEqual(a,self.m.snapshot("D1"))
    def test_local_order_not_global_clock(self):
        self.vote()
        self.vote("P2","S2","F","E2")
        self.assertTrue(all(x["temporal_order_claim"]=="LOCAL_JOURNAL_ONLY" for x in crstl_records(self.m,"D1")))
    def test_unique_ballot_provenance(self):
        self.vote()
        self.vote("P2","S2","A","E2")
        x=crstl_records(self.m,"D1")
        self.assertEqual({r["transition_id"] for r in x},{"E1","E2"})
        self.assertEqual({r["position"] for r in x},{"P1","P2"})
    def test_unknown_decision_no_authority(self):
        self.assertIsNone(project(self.m,"NONE"))
        self.assertEqual(execution_gate(project(self.m,"NONE")),"DENY_UNRESOLVED")
    def test_unresolved_three_ballots(self):
        self.vote(v="U")
        self.vote("P2","S2","F","E2")
        self.vote("P3","S3","A","E3")
        p=project(self.m,"D1")
        self.assertEqual((p.state,p.result),("CLOSED","U"))
        self.assertEqual(execution_gate(p,separate_host_authority=True,current_context=True),"DENY_UNRESOLVED")
    def test_restart_projection(self):
        self.vote()
        m2=BallotMachine(self.path)
        self.assertEqual(len(crstl_records(m2,"D1")),1)
    def test_replay_does_not_add_transition(self):
        self.vote()
        self.vote(e="E1")
        self.vote(e="E2")
        self.assertEqual(len(crstl_records(self.m,"D1")),1)
    def test_independent_decisions(self):
        self.m.create("D2","Other?")
        self.vote()
        self.assertEqual(len(crstl_records(self.m,"D2")),0)
    def test_negative_result_not_positive_execution(self):
        self.vote(v="A")
        self.vote("P2","S2","A","E2")
        self.assertEqual(project(self.m,"D1").result,"A")
        self.assertEqual(execution_gate(project(self.m,"D1")),"DENY_NO_FRESH_EXECUTION_AUTHORITY")

if __name__=="__main__":unittest.main()
