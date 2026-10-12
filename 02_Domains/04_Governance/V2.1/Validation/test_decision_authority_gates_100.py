import unittest
from dataclasses import replace
from decision_authority_gates_100 import AuthorityEvidence,ActionRequest,validate_at_commit

class GateTests(unittest.TestCase):
    def setUp(self):
        self.request=ActionRequest("host","apply","resource","restore",2)
        self.one=AuthorityEvidence("HOST","host","apply","resource","restore",10,30,2,"host-proof")
        self.two=AuthorityEvidence("RIGHTS","host","apply","resource","restore",10,30,2,"rights-proof")
        self.evidence=[self.one,self.two]
        self.opts=dict(now=20,required_issuers={"HOST","RIGHTS"},verified_issuers={"HOST","RIGHTS"},current_revision=2,context_allowed=True,host_ready=True)
    def gate(self,evidence=None,request=None,**kwargs):
        opts=dict(self.opts);opts.update(kwargs)
        return validate_at_commit(request or self.request,self.evidence if evidence is None else evidence,**opts)
    def test_two_keys_allow(self):self.assertEqual(self.gate(),"ALLOW")
    def test_missing_key_denied(self):self.assertEqual(self.gate([self.one]),"DENY_AUTHORITY")
    def test_unverified_issuer_denied(self):self.assertEqual(self.gate(verified_issuers={"HOST"}),"DENY_AUTHORITY")
    def test_expired_key_denied(self):self.assertEqual(self.gate(now=30),"DENY_AUTHORITY")
    def test_future_key_denied(self):self.assertEqual(self.gate(now=9),"DENY_AUTHORITY")
    def test_revoked_key_denied(self):self.assertEqual(self.gate([self.one,replace(self.two,revoked=True)]),"DENY_AUTHORITY")
    def test_wrong_target_denied(self):self.assertEqual(self.gate([self.one,replace(self.two,target="other")]),"DENY_AUTHORITY")
    def test_wrong_action_denied(self):self.assertEqual(self.gate([self.one,replace(self.two,action="other")]),"DENY_AUTHORITY")
    def test_wrong_purpose_denied(self):self.assertEqual(self.gate([self.one,replace(self.two,purpose="other")]),"DENY_AUTHORITY")
    def test_wrong_subject_denied(self):self.assertEqual(self.gate([self.one,replace(self.two,subject="other")]),"DENY_AUTHORITY")
    def test_wrong_revision_denied(self):self.assertEqual(self.gate(current_revision=3),"DENY_REVISION")
    def test_stale_evidence_revision_denied(self):self.assertEqual(self.gate([self.one,replace(self.two,revision=1)]),"DENY_AUTHORITY")
    def test_context_blocked(self):self.assertEqual(self.gate(context_allowed=False),"DENY_CONTEXT")
    def test_host_not_ready(self):self.assertEqual(self.gate(host_ready=False),"DENY_CONTEXT")
    def test_no_required_issuers(self):self.assertEqual(self.gate(required_issuers=set()),"DENY_NO_AUTHORITY_BASIS")
    def test_missing_evidence_reference(self):self.assertEqual(self.gate([self.one,replace(self.two,evidence_ref="")]),"DENY_AUTHORITY")
    def test_authority_at_proposal_not_at_commit(self):self.assertEqual(self.gate(now=29),"ALLOW");self.assertEqual(self.gate(now=31),"DENY_AUTHORITY")
    def test_extra_unrelated_evidence_no_bypass(self):
        extra=replace(self.one,issuer="UNRELATED")
        self.assertEqual(self.gate([self.one,extra]),"DENY_AUTHORITY")
if __name__=="__main__":unittest.main(verbosity=2)
