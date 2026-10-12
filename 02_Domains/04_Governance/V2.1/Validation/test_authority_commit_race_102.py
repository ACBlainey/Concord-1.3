import tempfile
import unittest
from pathlib import Path
from authority_owner_registry_101 import OwnerRegistry,Request
from authority_commit_race_102 import CommitRace

class RevocationRaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();root=Path(self.tmp.name)
        self.req=Request("actor","move","resource","safety",5)
        self.owners={k:OwnerRegistry(root/(k+".db"),k) for k in ("HOST","RIGHTS")}
        for k,v in self.owners.items():v.issue(k+"-G",self.req,10,30)
        self.refs={k:k+"-G" for k in self.owners}
        self.race=CommitRace(self.req,self.owners,self.refs,self.owners)
    def tearDown(self):self.tmp.cleanup()
    def test_ordinary_commit(self):
        self.assertEqual(self.race.run(20),"COMMITTED")
    def test_revoke_before_prepare(self):
        self.owners["HOST"].revoke("HOST-G")
        self.assertEqual(self.race.run(20),"DENIED_AT_PREPARE")
    def test_revoke_during_prepare(self):
        self.assertEqual(self.race.run(20,before_commit=lambda:self.owners["HOST"].revoke("HOST-G")),"DENIED_AT_COMMIT")
    def test_other_owner_revocation(self):
        self.assertEqual(self.race.run(20,before_commit=lambda:self.owners["RIGHTS"].revoke("RIGHTS-G")),"DENIED_AT_COMMIT")
    def test_revocation_survives_restart(self):
        self.owners["HOST"].revoke("HOST-G")
        self.owners["HOST"]=OwnerRegistry(self.owners["HOST"].path,"HOST")
        self.assertEqual(self.race.run(20),"DENIED_AT_PREPARE")
    def test_expiry_before_prepare(self):
        self.assertEqual(self.race.run(30),"DENIED_AT_PREPARE")
    def test_second_attempt_not_committed(self):
        self.race.run(20)
        self.assertEqual(self.race.run(20),"ALREADY_COMMITTED")
    def test_revocation_after_commit_not_retroactive(self):
        self.race.run(20);self.owners["HOST"].revoke("HOST-G")
        self.assertEqual(self.race.run(20),"ALREADY_COMMITTED")
    def test_unfenced_gap_demonstrated(self):
        self.assertEqual(self.race.observed_gap(20,before_effect=lambda:self.owners["HOST"].revoke("HOST-G")),"UNFENCED_EFFECT")
        self.assertEqual(self.race.check(20),"DENY_AUTHORITY")
    def test_gap_not_hidden_by_counter(self):
        self.race.observed_gap(20,before_effect=lambda:self.owners["RIGHTS"].revoke("RIGHTS-G"))
        self.assertEqual(self.race.attempts,1)
        self.assertFalse(self.race.committed)
    def test_two_keys_required(self):
        self.race.required.add("UNKNOWN")
        self.assertEqual(self.race.run(20),"DENIED_AT_PREPARE")
    def test_missing_reference(self):
        self.refs.pop("HOST")
        self.assertEqual(self.race.run(20),"DENIED_AT_PREPARE")
if __name__=="__main__":unittest.main(verbosity=2)
