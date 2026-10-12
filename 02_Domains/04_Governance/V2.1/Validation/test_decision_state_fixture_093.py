"""Executable fixture checks; do not infer constitutional approval."""
import unittest
from decision_state_fixture_093 import Decision

class DecisionStateFixtureTests(unittest.TestCase):
    def make(self):
        return Decision("D-1", True)
    def decided(self):
        d=self.make()
        self.assertEqual(d.vote("P1","s1","F"),"ACCEPTED")
        self.assertEqual(d.vote("P2","s2","F"),"ACCEPTED")
        return d
    def test_matching_majority_without_third(self):
        d=self.decided(); self.assertEqual(d.result,"F")
    def test_late_third_is_provenance_only(self):
        d=self.decided(); self.assertEqual(d.vote("P3","s3","A"),"PROVENANCE_ONLY");self.assertEqual(d.result,"F")
    def test_duplicate_ballot(self):
        d=self.make();d.vote("P1","s1","F");self.assertEqual(d.vote("P1","s1","F"),"DUPLICATE")
    def test_conflicting_duplicate(self):
        d=self.make();d.vote("P1","s1","F");self.assertEqual(d.vote("P1","s1","A"),"CONFLICT")
    def test_repeat_steward_other_position(self):
        d=self.make();d.vote("P1","s1","F");self.assertEqual(d.vote("P2","s1","A"),"REPEATED_STEWARD")
    def test_unauthorised_decision(self):
        self.assertEqual(Decision("D-2",False).vote("P1","s1","F"),"REJECTED")
    def test_expansion_requires_mandate(self):
        d=self.make();self.assertEqual(d.expanded("P3",["a","b","c"],["F","F","A"]),"NO_EXPANSION_AUTHORITY")
    def test_expanded_constituent_one_position(self):
        d=self.make();d.vote("P1","s1","F");d.vote("P2","s2","A")
        self.assertEqual(d.expanded("P3",["a","b","c"],["A","A","F"],mandate=True),"ACCEPTED")
        self.assertEqual(d.result,"A");self.assertEqual(len(d.positions),3)
    def test_expansion_reused_identity(self):
        d=self.make();d.vote("P1","s1","F")
        self.assertEqual(d.expanded("P3",["s1","b","c"],["A","A","F"],mandate=True),"REPEATED_STEWARD")
    def test_expansion_no_extra_after_majority(self):
        d=self.decided();self.assertEqual(d.expanded("P3",["a","b","c"],["A","A","A"],mandate=True),"NO_EXPANSION_AUTHORITY")
    def test_shadow_not_authorised(self):
        d=self.make();self.assertEqual(d.vote("P1","shadow","F",mandate=False),"REJECTED")
    def test_action_requires_host_authority(self):
        d=self.decided();self.assertEqual(d.action("A1"),"REJECTED")
    def test_action_duplicate_no_repeat(self):
        d=self.decided();self.assertEqual(d.action("A1",host_authorised=True),"DONE")
        self.assertEqual(d.action("A1",host_authorised=True),"DUPLICATE")
    def test_distinct_actions(self):
        d=self.decided();self.assertEqual(d.action("A1",host_authorised=True),"DONE")
        self.assertEqual(d.action("A2",host_authorised=True),"DONE")
    def test_uncertain_effect_not_blindly_retried(self):
        d=self.decided();self.assertEqual(d.action("A1",host_authorised=True,effect_known=False),"UNCERTAIN")
        self.assertEqual(d.action("A1",host_authorised=True),"RECONCILE")
    def test_closed_decision_cannot_vote(self):
        d=self.decided();d.close();self.assertEqual(d.vote("P3","s3","A"),"REJECTED")
    def test_new_decision_is_distinct(self):
        old=self.decided();old.close();new=Decision("D-2",True)
        self.assertEqual(new.vote("P1","s1","A"),"ACCEPTED");self.assertEqual(old.result,"F")
    def test_new_id_without_authority_rejected(self):
        self.assertEqual(Decision("D-2",False).vote("P1","s1","A"),"REJECTED")
    def test_unresolved_cannot_close(self):
        self.assertEqual(self.make().close(),"UNRESOLVED")
    def test_expired_vote_rejected(self):
        self.assertEqual(self.make().vote("P1","s1","F",mandate=False),"REJECTED")

if __name__=="__main__":unittest.main(verbosity=2)
