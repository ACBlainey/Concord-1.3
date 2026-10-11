import copy, unittest
from g05_bta_compat_adapter_072 import read_fixture
from g05_bta_owner_attestation_074 import OwnerAttestation, assess_transition

class OwnerBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.r=read_fixture()
        self.required=[("OWNER:ACCESS_PERMISSION","destination privileged access"),
                       ("OWNER:RESPONSIBILITY_CONTINUITY","unresolved live obligations")]
        self.rev={(o,s):3 for o,s in self.required}
        self.a=[OwnerAttestation(o,s,self.r["TransitionID"],3,"APPROVED","EV-"+str(i)) for i,(o,s) in enumerate(self.required)]
    def assess(self,r=None,a=None,rev=None):
        return assess_transition(self.r if r is None else r,self.a if a is None else a,self.rev if rev is None else rev,self.required)
    def test_original_pending_blocks(self):self.assertIn("PENDING_CONDITIONS",self.assess()["issues"])
    def test_original_unresolved_blocks(self):self.assertIn("UNRESOLVED_STATE",self.assess()["issues"])
    def test_wrong_transition_id(self):
        a=list(self.a);a[0]=OwnerAttestation(a[0].owner_ref,a[0].scope,"WRONG",3,"APPROVED","EV")
        self.assertTrue(any("MISSING_OR_DUPLICATE" in x for x in self.assess(a=a)["issues"]))
    def test_wrong_scope(self):
        a=list(self.a);a[0]=OwnerAttestation(a[0].owner_ref,"different",self.r["TransitionID"],3,"APPROVED","EV")
        self.assertTrue(any("MISSING_OR_DUPLICATE" in x for x in self.assess(a=a)["issues"]))
    def test_duplicate_owner(self):
        self.assertTrue(any("MISSING_OR_DUPLICATE" in x for x in self.assess(a=self.a+[self.a[0]])["issues"]))
    def test_stale_revision(self):
        rev=dict(self.rev);rev[self.required[0]]=4
        self.assertTrue(any("STALE_OWNER_REVISION" in x for x in self.assess(rev=rev)["issues"]))
    def test_denial(self):
        a=list(self.a);v=a[0];a[0]=OwnerAttestation(v.owner_ref,v.scope,v.transition_id,v.revision,"DENIED",v.evidence_ref)
        self.assertTrue(any("OWNER_NOT_APPROVED" in x for x in self.assess(a=a)["issues"]))
    def test_missing_evidence(self):
        a=list(self.a);v=a[0];a[0]=OwnerAttestation(v.owner_ref,v.scope,v.transition_id,v.revision,"APPROVED","")
        self.assertTrue(any("OWNER_NOT_APPROVED" in x for x in self.assess(a=a)["issues"]))
    def test_owner_scope_isolation(self):
        a=[self.a[0]]
        self.assertTrue(any("OWNER:RESPONSIBILITY_CONTINUITY" in x for x in self.assess(a=a)["issues"]))
    def test_clean_fixture_still_does_not_grant_authority(self):
        r=copy.deepcopy(self.r);r["PendingStateRefs"]=[];r["UncertaintyOrDisputeState"]["State"]="RESOLVED"
        result=self.assess(r=r)
        self.assertTrue(result["eligible_for_owner_review"])
        self.assertFalse(result["authority_granted"])
        self.assertFalse(result["transition_complete"])
if __name__=="__main__":unittest.main(verbosity=2)
