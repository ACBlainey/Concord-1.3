import os
import tempfile
import unittest
from authority_owner_registry_101 import Request
from glass_hammer_owner_projection_118 import OwnerCheckedProjection

class OwnerProjection118(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.p=OwnerCheckedProjection(os.path.join(self.tmp.name,"decision.sqlite"),os.path.join(self.tmp.name,"owner.sqlite"))
        self.m=self.p.isolated
        self.m.create("D","Question?")
        self.m.vote(decision_id="D",position="P1",steward="S1",choice="F",event_id="V1",eligible=True,context_ok=True)
        self.m.vote(decision_id="D",position="P2",steward="S2",choice="A",event_id="V2",eligible=True,context_ok=True)
        self.m.record_concern(concern_id="C1",decision_id="D",steward="S1",position="P1",explanation="Protected reason",evidence_ref="SECRET",event_id="CE1")
        self.p.owner.issue("G-S2",Request("S2","PROJECT_STEWARD","D","VOTE_CONTEXT_VIEW",1),100,200)
    def tearDown(self):self.tmp.cleanup()
    def view(self,**kw):return self.p.project(decision_id="D",subject="S2",role="STEWARD",grant_ref="G-S2",now=150,revision=1,steward="S2",**kw)
    def test_valid_grant_own_projection(self):
        r=self.view()
        self.assertEqual(r["own_ballots"],[{"position":"P2","choice":"A"}])
    def test_other_ballot_sealed(self):self.assertNotIn("'F'",str(self.view()))
    def test_peer_concern_sealed(self):self.assertNotIn("Protected reason",str(self.view()))
    def test_revoked_grant_denied(self):
        self.p.owner.revoke("G-S2")
        self.assertEqual(self.view()["status"],"DENY_OWNER_GRANT")
    def test_expired_grant_denied(self):
        r=self.p.project(decision_id="D",subject="S2",role="STEWARD",grant_ref="G-S2",now=200,revision=1,steward="S2")
        self.assertEqual(r["status"],"DENY_OWNER_GRANT")
    def test_wrong_revision_denied(self):
        r=self.p.project(decision_id="D",subject="S2",role="STEWARD",grant_ref="G-S2",now=150,revision=2,steward="S2")
        self.assertEqual(r["status"],"DENY_OWNER_GRANT")
    def test_identity_alias_denied(self):
        r=self.p.project(decision_id="D",subject="S2",role="STEWARD",grant_ref="G-S2",now=150,revision=1,steward="S1")
        self.assertEqual(r["status"],"DENY_SUBJECT_BINDING")
    def test_grant_reuse_for_another_decision_denied(self):
        r=self.p.project(decision_id="OTHER",subject="S2",role="STEWARD",grant_ref="G-S2",now=150,revision=1,steward="S2")
        self.assertEqual(r["status"],"DENY_OWNER_GRANT")
    def test_role_escalation_denied(self):
        r=self.p.project(decision_id="D",subject="S2",role="REVIEW_ROUTER",grant_ref="G-S2",now=150,revision=1)
        self.assertEqual(r["status"],"DENY_OWNER_GRANT")
    def test_no_grant_denied(self):
        r=self.p.project(decision_id="D",subject="S2",role="STEWARD",grant_ref="UNKNOWN",now=150,revision=1,steward="S2")
        self.assertEqual(r["status"],"DENY_OWNER_GRANT")
    def test_public_requires_distinct_grant(self):
        r=self.p.project(decision_id="D",subject="PUBLIC",role="PUBLIC",grant_ref="G-S2",now=150,revision=1)
        self.assertEqual(r["status"],"DENY_OWNER_GRANT")
    def test_reviewer_requires_independence(self):
        self.p.owner.issue("G-R",Request("R1","PROJECT_REVIEW_CONCERN","D","REVIEW_EVIDENCE",1),100,200)
        r=self.p.reviewer(decision_id="D",subject="R1",grant_ref="G-R",now=150,revision=1,independence_ref="")
        self.assertEqual(r["status"],"DENY_INDEPENDENCE_EVIDENCE")
    def test_reviewer_independence_grant_checked(self):
        self.p.owner.issue("G-R",Request("R1","PROJECT_REVIEW_CONCERN","D","REVIEW_EVIDENCE",1),100,200)
        r=self.p.reviewer(decision_id="D",subject="R1",grant_ref="G-R",now=150,revision=1,independence_ref="UNKNOWN")
        self.assertEqual(r["status"],"DENY_INDEPENDENCE")
    def test_reviewer_two_grants(self):
        self.p.owner.issue("G-R",Request("R1","PROJECT_REVIEW_CONCERN","D","REVIEW_EVIDENCE",1),100,200)
        self.p.owner.issue("G-I",Request("R1","VERIFY_INDEPENDENT_REVIEWER","D","REVIEW_INDEPENDENCE",1),100,200)
        r=self.p.reviewer(decision_id="D",subject="R1",grant_ref="G-R",now=150,revision=1,independence_ref="G-I")
        self.assertEqual(r["status"],"OK")
        self.assertEqual(r["ballots"],"SEALED_PENDING_SEPARATE_DISCLOSURE_AUTHORITY")
    def test_reviewer_revocation_denies(self):
        self.p.owner.issue("G-R",Request("R1","PROJECT_REVIEW_CONCERN","D","REVIEW_EVIDENCE",1),100,200)
        self.p.owner.issue("G-I",Request("R1","VERIFY_INDEPENDENT_REVIEWER","D","REVIEW_INDEPENDENCE",1),100,200)
        self.p.owner.revoke("G-I")
        r=self.p.reviewer(decision_id="D",subject="R1",grant_ref="G-R",now=150,revision=1,independence_ref="G-I")
        self.assertEqual(r["status"],"DENY_INDEPENDENCE")
    def test_owner_grant_not_ballot_revocation(self):
        before=self.m.status("D")["regular"]
        self.p.owner.revoke("G-S2")
        self.assertEqual(self.m.status("D")["regular"],before)
    def test_no_unrecognised_role(self):
        r=self.p.project(decision_id="D",subject="S2",role="ADMIN",grant_ref="G-S2",now=150,revision=1)
        self.assertEqual(r["status"],"DENY_ROLE")

if __name__=="__main__":unittest.main()
