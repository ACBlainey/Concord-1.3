import os
import tempfile
import unittest
from glass_hammer_isolation_117 import IsolatedConcernReview

class Isolation117(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.m=IsolatedConcernReview(os.path.join(self.tmp.name,"db.sqlite"))
        self.m.create("D","Question?")
        for p,s,v,e in (("P1","S1","F","V1"),("P2","S2","A","V2")):
            self.m.vote(decision_id="D",position=p,steward=s,choice=v,event_id=e,eligible=True,context_ok=True)
        self.m.record_concern(concern_id="C1",decision_id="D",steward="S1",position="P1",explanation="Concern secret",evidence_ref="SECRET1",event_id="CE1")
    def tearDown(self):self.tmp.cleanup()
    def test_denied_without_verified_authority(self):self.assertEqual(self.m.view("D",role="STEWARD",steward="S2")["status"],"DENY_AUTHORITY")
    def test_steward_own_ballot_only(self):
        r=self.m.view("D",role="STEWARD",steward="S2",authority_verified=True)
        self.assertEqual(r["own_ballots"],[{"position":"P2","choice":"A"}])
        self.assertNotIn("F",str(r))
    def test_steward_cannot_see_peer_concern(self):
        r=self.m.view("D",role="STEWARD",steward="S2",authority_verified=True)
        self.assertNotIn("Concern secret",str(r))
        self.assertNotIn("SECRET1",str(r))
    def test_own_concern_visible(self):
        r=self.m.view("D",role="STEWARD",steward="S1",authority_verified=True)
        self.assertEqual(r["own_concerns"][0]["concern_id"],"C1")
    def test_unknown_steward_sees_no_ballots(self):
        r=self.m.view("D",role="STEWARD",steward="S4",authority_verified=True)
        self.assertEqual(r["own_ballots"],[])
    def test_missing_steward_identity_denied(self):self.assertEqual(self.m.view("D",role="STEWARD",authority_verified=True)["status"],"DENY_IDENTITY")
    def test_public_pending_no_tally(self):
        r=self.m.view("D",role="PUBLIC",authority_verified=True)
        self.assertEqual(r["status"],"PENDING")
        self.assertNotIn("accepted_result",r)
    def test_router_metadata_only(self):
        r=self.m.view("D",role="REVIEW_ROUTER",authority_verified=True)
        self.assertEqual(r["concern_ids"],["C1"])
        self.assertNotIn("Concern secret",str(r))
    def test_router_never_sees_ballot(self):
        r=self.m.view("D",role="REVIEW_ROUTER",authority_verified=True)
        self.assertEqual(r["ballots"],"SEALED")
    def test_reviewer_no_auto_access(self):
        self.assertEqual(self.m.view_reviewer_evidence("D")["status"],"DENY_REVIEW_ACCESS")
    def test_reviewer_requires_independence(self):
        self.assertEqual(self.m.view_reviewer_evidence("D",review_owner_authority_verified=True)["status"],"DENY_REVIEW_ACCESS")
    def test_reviewer_concern_not_ballot(self):
        r=self.m.view_reviewer_evidence("D",review_owner_authority_verified=True,independent_of_stewards=True)
        self.assertEqual(r["status"],"OK")
        self.assertEqual(r["ballots"],"SEALED_PENDING_SEPARATE_DISCLOSURE_AUTHORITY")
    def test_unknown_decision_denied(self):self.assertEqual(self.m.view("X",role="PUBLIC",authority_verified=True)["status"],"DENY_UNKNOWN_DECISION")
    def test_unrecognised_role_denied(self):self.assertEqual(self.m.view("D",role="OBSERVER",authority_verified=True)["status"],"DENY_ROLE")
    def test_steward_cannot_view_result_after_other_votes(self):
        self.m.vote(decision_id="D",position="P3",steward="S3",choice="F",event_id="V3",eligible=True,context_ok=True)
        r=self.m.view("D",role="STEWARD",steward="S1",authority_verified=True)
        self.assertNotIn("accepted_result",r)
    def test_public_closed_seals_votes(self):
        self.m.vote(decision_id="D",position="P3",steward="S3",choice="F",event_id="V3",eligible=True,context_ok=True)
        r=self.m.view("D",role="PUBLIC",authority_verified=True)
        self.assertEqual(r["ballots"],"SEALED")
    def test_view_does_not_change_vote(self):
        before=self.m.status("D")["regular"]
        self.m.view("D",role="STEWARD",steward="S2",authority_verified=True)
        self.assertEqual(before,self.m.status("D")["regular"])

if __name__=="__main__":unittest.main()
