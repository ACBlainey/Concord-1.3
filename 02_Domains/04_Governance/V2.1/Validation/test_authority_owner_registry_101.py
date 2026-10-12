import tempfile
import unittest
from pathlib import Path
from dataclasses import replace
from authority_owner_registry_101 import OwnerRegistry,Request,commit_gate

class OwnerTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();root=Path(self.t.name)
        self.paths={k:root/(k+".db") for k in ("HOST","RIGHTS")}
        self.owners={k:OwnerRegistry(self.paths[k],k) for k in self.paths}
        self.request=Request("participant","act","target","restore",2)
        for k,o in self.owners.items():o.issue(k+"-G",self.request,10,30)
        self.refs={k:k+"-G" for k in self.owners}
        self.opts=dict(now=20,required_issuers={"HOST","RIGHTS"},context_allowed=True,host_ready=True,current_revision=2)
    def tearDown(self):self.t.cleanup()
    def gate(self,**kw):
        opts=dict(self.opts);opts.update(kw)
        return commit_gate(self.request,self.owners,self.refs,**opts)
    def test_valid(self):self.assertEqual(self.gate(),"ALLOW")
    def test_host_revoke(self):
        self.owners["HOST"].revoke("HOST-G");self.assertEqual(self.gate(),"DENY_AUTHORITY")
    def test_rights_revoke(self):
        self.owners["RIGHTS"].revoke("RIGHTS-G");self.assertEqual(self.gate(),"DENY_AUTHORITY")
    def test_revocation_survives_restart(self):
        self.owners["HOST"].revoke("HOST-G")
        self.owners["HOST"]=OwnerRegistry(self.paths["HOST"],"HOST")
        self.assertEqual(self.gate(),"DENY_AUTHORITY")
    def test_revocation_after_prior_allow(self):
        self.assertEqual(self.gate(),"ALLOW")
        self.owners["HOST"].revoke("HOST-G")
        self.assertEqual(self.gate(),"DENY_AUTHORITY")
    def test_missing_owner(self):
        self.owners.pop("RIGHTS");self.assertEqual(self.gate(),"DENY_MISSING_OWNER")
    def test_missing_reference(self):
        self.refs.pop("RIGHTS");self.assertEqual(self.gate(),"DENY_MISSING_OWNER")
    def test_issuer_mismatch(self):
        self.owners["RIGHTS"]=OwnerRegistry(self.paths["RIGHTS"],"OTHER")
        self.assertEqual(self.gate(),"DENY_MISSING_OWNER")
    def test_unknown_reference(self):
        self.refs["HOST"]="UNKNOWN";self.assertEqual(self.gate(),"DENY_AUTHORITY")
    def test_expired(self):self.assertEqual(self.gate(now=30),"DENY_AUTHORITY")
    def test_not_yet_valid(self):self.assertEqual(self.gate(now=9),"DENY_AUTHORITY")
    def test_wrong_revision(self):self.assertEqual(self.gate(current_revision=3),"DENY_REVISION")
    def test_wrong_target(self):
        self.request=replace(self.request,target="other");self.assertEqual(self.gate(),"DENY_AUTHORITY")
    def test_wrong_purpose(self):
        self.request=replace(self.request,purpose="other");self.assertEqual(self.gate(),"DENY_AUTHORITY")
    def test_wrong_subject(self):
        self.request=replace(self.request,subject="other");self.assertEqual(self.gate(),"DENY_AUTHORITY")
    def test_context_denied(self):self.assertEqual(self.gate(context_allowed=False),"DENY_CONTEXT")
    def test_host_not_ready(self):self.assertEqual(self.gate(host_ready=False),"DENY_CONTEXT")
    def test_no_required_issuers(self):self.assertEqual(self.gate(required_issuers=set()),"DENY_NO_AUTHORITY_BASIS")
    def test_invalid_grant_window(self):
        with self.assertRaises(ValueError):self.owners["HOST"].issue("BAD",self.request,30,10)
    def test_duplicate_grant_ref_rejected(self):
        with self.assertRaises(Exception):self.owners["HOST"].issue("HOST-G",self.request,10,30)
if __name__=="__main__":unittest.main(verbosity=2)
