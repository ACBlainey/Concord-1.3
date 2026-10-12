import os
import tempfile
import unittest
from glass_hammer_concern_review_116 import ConcernReview

class ConcernReview116(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.m=ConcernReview(os.path.join(self.tmp.name,"db.sqlite"))
        self.m.create("D","Question?")
        self.m.vote(decision_id="D",position="P1",steward="S1",choice="F",event_id="V1",eligible=True,context_ok=True)
        self.kw=dict(concern_id="C1",decision_id="D",steward="S1",position="P1",explanation="New evidence",evidence_ref="EVID1",event_id="CE1")
    def tearDown(self):self.tmp.cleanup()
    def test_record_concern(self):self.assertEqual(self.m.record_concern(**self.kw),"RECORDED")
    def test_no_ballot_mutation(self):
        before=self.m.status("D")["regular"]
        self.m.record_concern(**self.kw)
        self.assertEqual(self.m.status("D")["regular"],before)
    def test_concern_does_not_revote(self):
        self.m.record_concern(**self.kw)
        self.assertEqual(self.m.vote(decision_id="D",position="P1",steward="S1",choice="A",event_id="V2",eligible=True,context_ok=True),"DENY_CONSUMED")
    def test_uncommitted_steward_denied(self):
        self.assertEqual(self.m.record_concern(**(self.kw|{"steward":"S2"})),"DENY_NO_COMMITTED_BALLOT")
    def test_duplicate_idempotent(self):
        self.m.record_concern(**self.kw)
        self.assertEqual(self.m.record_concern(**self.kw),"DUPLICATE")
    def test_collision_denied(self):
        self.m.record_concern(**self.kw)
        self.assertEqual(self.m.record_concern(**(self.kw|{"explanation":"Different"})),"DENY_ID_COLLISION")
    def test_event_reuse_denied(self):
        self.m.record_concern(**self.kw)
        self.assertEqual(self.m.record_concern(**(self.kw|{"concern_id":"C2"})),"DENY_EVENT_REUSE")
    def test_correction_is_append_only(self):
        self.m.record_concern(**self.kw)
        k=self.kw|{"concern_id":"C2","event_id":"CE2","prior_concern":"C1","explanation":"Corrected"}
        self.assertEqual(self.m.record_concern(**k),"RECORDED")
        self.assertEqual(len(self.m.history("D")),2)
    def test_unknown_prior_denied(self):
        self.assertEqual(self.m.record_concern(**(self.kw|{"prior_concern":"UNKNOWN"})),"DENY_PRIOR_REFERENCE")
    def test_outbox_is_not_review_authority(self):
        self.m.record_concern(**self.kw)
        with self.m.machine.connection() as db:
            self.assertEqual(db.execute("SELECT state FROM review_outbox116 WHERE concern_id='C1'").fetchone()[0],"PENDING")
    def test_referral_denied_without_authority(self):
        self.m.record_concern(**self.kw)
        self.assertEqual(self.m.refer(referral_id="R1",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=False),"DENY_REVIEW_AUTHORITY")
    def test_authorised_referral(self):
        self.m.record_concern(**self.kw)
        self.assertEqual(self.m.refer(referral_id="R1",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True),"REFERRED")
    def test_referral_dedup(self):
        self.m.record_concern(**self.kw)
        self.m.refer(referral_id="R1",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True)
        self.assertEqual(self.m.refer(referral_id="R2",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True),"ALREADY_REFERRED")
    def test_no_concern_no_referral(self):
        self.assertEqual(self.m.refer(referral_id="R1",concern_id="NONE",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True),"DENY_NO_CONCERN")
    def test_replacement_needs_authority(self):
        self.m.record_concern(**self.kw)
        self.m.refer(referral_id="R1",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True)
        self.assertEqual(self.m.propose_replacement(replacement_id="D2",original_decision="D",referral_id="R1",excluded_steward="S1",authority_valid=False),"DENY_REPLACEMENT_AUTHORITY")
    def test_replacement_excludes_original_steward(self):
        self.m.record_concern(**self.kw)
        self.m.refer(referral_id="R1",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True)
        self.assertEqual(self.m.propose_replacement(replacement_id="D2",original_decision="D",referral_id="R1",excluded_steward="S1",authority_valid=True),"PROPOSED_ONLY")
    def test_wrong_exclusion_denied(self):
        self.m.record_concern(**self.kw)
        self.m.refer(referral_id="R1",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True)
        self.assertEqual(self.m.propose_replacement(replacement_id="D2",original_decision="D",referral_id="R1",excluded_steward="S2",authority_valid=True),"DENY_REVIEW_BINDING")
    def test_replacement_cannot_reuse_original_id(self):
        self.m.record_concern(**self.kw)
        self.m.refer(referral_id="R1",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True)
        self.assertEqual(self.m.propose_replacement(replacement_id="D",original_decision="D",referral_id="R1",excluded_steward="S1",authority_valid=True),"DENY_REUSED_DECISION_ID")
    def test_replacement_not_automatically_created(self):
        self.m.record_concern(**self.kw)
        self.m.refer(referral_id="R1",concern_id="C1",owner="JUDICIARY",authority_ref="AUTH",authority_valid=True)
        self.m.propose_replacement(replacement_id="D2",original_decision="D",referral_id="R1",excluded_steward="S1",authority_valid=True)
        with self.m.machine.connection() as db:
            self.assertIsNone(db.execute("SELECT id FROM decisions WHERE id='D2'").fetchone())
    def test_history_persists_restart(self):
        self.m.record_concern(**self.kw)
        again=ConcernReview(os.path.join(self.tmp.name,"db.sqlite"))
        self.assertEqual(len(again.history("D")),1)

if __name__=="__main__":unittest.main()
