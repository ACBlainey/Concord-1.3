import unittest
from g05_gtp_resource_collision_076 import Claim
from g05_gtp_reconciliation_077 import Resolution,review_resolution

class ReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.a=Claim("A1","GTP-A","OWNER-A","PUMP-1",4,"MA","EXCLUSIVE","ACTIVE")
        self.b=Claim("B1","GTP-B","OWNER-B","PUMP-1",7,"MB","EXCLUSIVE","ACTIVE")
        self.c=[self.a,self.b]
        self.r=Resolution("R1","PUMP-1",("A1","B1"),("E1",),("OWNER-A","OWNER-B"),8,("SHARED","SHARED"))
    def review(self,r=None,owners=("OWNER-A","OWNER-B"),revision=8):
        return review_resolution(self.c,self.r if r is None else r,owners,revision)
    def test_complete_proposal_reaches_review(self):self.assertTrue(self.review()["ready_for_owner_system_verification"])
    def test_never_automatically_activates(self):self.assertFalse(self.review()["allocation_activated"])
    def test_no_override(self):self.assertFalse(self.review()["mandates_overridden"])
    def test_missing_owner(self):
        r=Resolution("R1","PUMP-1",("A1","B1"),("E1",),("OWNER-A",),8,("SHARED","SHARED"))
        self.assertIn("OWNER_APPROVAL_INCOMPLETE",self.review(r)["issues"])
    def test_missing_claim(self):
        r=Resolution("R1","PUMP-1",("A1",),("E1",),("OWNER-A","OWNER-B"),8,("SHARED","SHARED"))
        self.assertIn("INCOMPLETE_AFFECTED_CLAIMS",self.review(r)["issues"])
    def test_stale_revision(self):self.assertIn("STALE_RESOLUTION",self.review(revision=9)["issues"])
    def test_no_evidence(self):
        r=Resolution("R1","PUMP-1",("A1","B1"),(),("OWNER-A","OWNER-B"),8,("SHARED","SHARED"))
        self.assertIn("RESOLUTION_EVIDENCE_MISSING",self.review(r)["issues"])
    def test_no_proposed_modes(self):
        r=Resolution("R1","PUMP-1",("A1","B1"),("E1",),("OWNER-A","OWNER-B"),8,())
        self.assertIn("PROPOSED_ALLOCATION_INCOMPLETE",self.review(r)["issues"])
    def test_duplicate_claim(self):
        r=Resolution("R1","PUMP-1",("A1","A1"),("E1",),("OWNER-A","OWNER-B"),8,("SHARED","SHARED"))
        self.assertIn("DUPLICATE_CLAIM_REFERENCE",self.review(r)["issues"])
    def test_wrong_resource(self):
        r=Resolution("R1","PUMP-2",("A1","B1"),("E1",),("OWNER-A","OWNER-B"),8,("SHARED","SHARED"))
        self.assertIn("INCOMPLETE_AFFECTED_CLAIMS",self.review(r)["issues"])
if __name__=="__main__":unittest.main(verbosity=2)
