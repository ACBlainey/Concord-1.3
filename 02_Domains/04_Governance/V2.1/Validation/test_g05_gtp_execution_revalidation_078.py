import unittest
from g05_gtp_execution_revalidation_078 import Snapshot,Approval,review_for_execution

class ExecutionRevalidationTests(unittest.TestCase):
    def setUp(self):
        self.snap=Snapshot(2,(("A",4),("B",7)),3,1,5)
        self.ap=[Approval("A",4,"APPROVED","EA"),Approval("B",7,"APPROVED","EB")]
    def runcheck(self,live=None,approvals=None,available=True,valid=True):
        return review_for_execution(self.snap,live or self.snap,self.ap if approvals is None else approvals,{"A","B"},available,valid)
    def test_clean_ready_only(self):
        result=self.runcheck();self.assertTrue(result["ready_for_final_owner_check"])
        self.assertFalse(result["execution_authorised"])
    def test_resource_revision_changed(self):
        s=Snapshot(3,self.snap.owner_revisions,3,1,5)
        self.assertIn("RESOURCE_CHANGED",self.runcheck(s)["issues"])
    def test_dependency_changed(self):
        s=Snapshot(2,self.snap.owner_revisions,4,1,5)
        self.assertIn("DEPENDENCY_CHANGED",self.runcheck(s)["issues"])
    def test_emergency_changed(self):
        s=Snapshot(2,self.snap.owner_revisions,3,2,5)
        self.assertIn("EMERGENCY_CONTEXT_CHANGED",self.runcheck(s)["issues"])
    def test_clock_changed(self):
        s=Snapshot(2,self.snap.owner_revisions,3,1,6)
        self.assertIn("CLOCK_CONTEXT_CHANGED_REVIEW",self.runcheck(s)["issues"])
    def test_owner_revision_changed(self):
        s=Snapshot(2,(("A",5),("B",7)),3,1,5)
        self.assertIn("OWNER_REVISION_STALE:A",self.runcheck(s)["issues"])
    def test_denial(self):
        a=[Approval("A",4,"DENIED","EA"),self.ap[1]]
        self.assertIn("APPROVAL_INVALID:A",self.runcheck(approvals=a)["issues"])
    def test_missing_approval(self):
        self.assertIn("MISSING_OR_DUPLICATE_APPROVAL:B",self.runcheck(approvals=self.ap[:1])["issues"])
    def test_duplicate_approval(self):
        self.assertIn("MISSING_OR_DUPLICATE_APPROVAL:A",self.runcheck(approvals=self.ap+[self.ap[0]])["issues"])
    def test_missing_evidence(self):
        a=[Approval("A",4,"APPROVED",""),self.ap[1]]
        self.assertIn("APPROVAL_INVALID:A",self.runcheck(approvals=a)["issues"])
    def test_resource_unavailable(self):
        self.assertIn("RESOURCE_UNAVAILABLE",self.runcheck(available=False)["issues"])
    def test_invalid_proposal(self):
        self.assertIn("PROPOSAL_NOT_VALIDATED",self.runcheck(valid=False)["issues"])
    def test_extraneous_owner(self):
        a=self.ap+[Approval("C",1,"APPROVED","EC")]
        self.assertIn("EXTRANEOUS_APPROVAL_REVIEW",self.runcheck(approvals=a)["issues"])
if __name__=="__main__":unittest.main(verbosity=2)
