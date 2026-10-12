"""Stage 116: immutable ballot concern and independently authorised review fixture.

This adapter does not grant judicial authority, determine review merits,
or expose sealed votes to reviewers. STRA routing is represented by an outbox.
"""
import sqlite3
from glass_hammer_early_acceptance_110 import ContextualDecision

class ConcernReview(ContextualDecision):
    def __init__(self,path):
        super().__init__(path)
        with self.machine.connection() as db:
            db.execute("CREATE TABLE IF NOT EXISTS concerns116 (concern_id TEXT PRIMARY KEY, decision_id TEXT NOT NULL, steward TEXT NOT NULL, position TEXT NOT NULL, explanation TEXT NOT NULL, evidence_ref TEXT NOT NULL, prior_concern TEXT, event_id TEXT NOT NULL UNIQUE)")
            db.execute("CREATE TABLE IF NOT EXISTS review_outbox116 (concern_id TEXT PRIMARY KEY, decision_id TEXT NOT NULL, review_ground TEXT NOT NULL, route TEXT NOT NULL, state TEXT NOT NULL)")
            db.execute("CREATE TABLE IF NOT EXISTS review_referrals116 (referral_id TEXT PRIMARY KEY, concern_id TEXT NOT NULL UNIQUE, owner TEXT NOT NULL, authority_ref TEXT NOT NULL, state TEXT NOT NULL)")
            db.execute("CREATE TABLE IF NOT EXISTS replacement116 (replacement_id TEXT PRIMARY KEY, original_decision TEXT NOT NULL, referral_id TEXT NOT NULL UNIQUE, excluded_steward TEXT NOT NULL)")
    def record_concern(self,*,concern_id,decision_id,steward,position,explanation,evidence_ref,event_id,prior_concern=None):
        if not all((concern_id,decision_id,steward,position,explanation,evidence_ref,event_id)):return "DENY_INCOMPLETE"
        with self.machine.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                prior=db.execute("SELECT decision_id,steward,position,explanation,evidence_ref FROM concerns116 WHERE concern_id=?",(concern_id,)).fetchone()
                if prior:out="DUPLICATE" if prior==(decision_id,steward,position,explanation,evidence_ref) else "DENY_ID_COLLISION"
                elif db.execute("SELECT 1 FROM concerns116 WHERE event_id=?",(event_id,)).fetchone():out="DENY_EVENT_REUSE"
                elif not (db.execute("SELECT 1 FROM ballots WHERE decision_id=? AND steward=? AND position=?",(decision_id,steward,position)).fetchone() or db.execute("SELECT 1 FROM late_ballots110 WHERE decision_id=? AND steward=? AND position=?",(decision_id,steward,position)).fetchone()):out="DENY_NO_COMMITTED_BALLOT"
                elif prior_concern and not db.execute("SELECT 1 FROM concerns116 WHERE concern_id=? AND decision_id=? AND steward=?",(prior_concern,decision_id,steward)).fetchone():out="DENY_PRIOR_REFERENCE"
                else:
                    db.execute("INSERT INTO concerns116 VALUES (?,?,?,?,?,?,?,?)",(concern_id,decision_id,steward,position,explanation,evidence_ref,prior_concern,event_id))
                    db.execute("INSERT INTO review_outbox116 VALUES (?,?,?,?,?)",(concern_id,decision_id,"STEWARD_SUBSEQUENT_CONCERN","STRA_REVIEW_ROUTING","PENDING"))
                    out="RECORDED"
                db.execute("COMMIT")
                return out
            except Exception:
                db.execute("ROLLBACK")
                raise
    def refer(self,*,referral_id,concern_id,owner,authority_ref,authority_valid):
        if not authority_valid or not owner or not authority_ref:return "DENY_REVIEW_AUTHORITY"
        with self.machine.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                if db.execute("SELECT 1 FROM review_referrals116 WHERE concern_id=?",(concern_id,)).fetchone():out="ALREADY_REFERRED"
                elif not db.execute("SELECT 1 FROM review_outbox116 WHERE concern_id=?",(concern_id,)).fetchone():out="DENY_NO_CONCERN"
                else:
                    db.execute("INSERT INTO review_referrals116 VALUES (?,?,?,?,?)",(referral_id,concern_id,owner,authority_ref,"REFERRED"))
                    db.execute("UPDATE review_outbox116 SET state='REFERRED' WHERE concern_id=?",(concern_id,))
                    out="REFERRED"
                db.execute("COMMIT")
                return out
            except Exception:
                db.execute("ROLLBACK")
                raise
    def propose_replacement(self,*,replacement_id,original_decision,referral_id,excluded_steward,authority_valid):
        if not authority_valid:return "DENY_REPLACEMENT_AUTHORITY"
        with self.machine.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                row=db.execute("SELECT c.decision_id,c.steward FROM review_referrals116 r JOIN concerns116 c ON c.concern_id=r.concern_id WHERE r.referral_id=?",(referral_id,)).fetchone()
                if not row or row!=(original_decision,excluded_steward):out="DENY_REVIEW_BINDING"
                elif replacement_id==original_decision:out="DENY_REUSED_DECISION_ID"
                elif db.execute("SELECT 1 FROM decisions WHERE id=?",(replacement_id,)).fetchone():out="DENY_EXISTING_DECISION_ID"
                elif db.execute("SELECT 1 FROM replacement116 WHERE referral_id=?",(referral_id,)).fetchone():out="ALREADY_PROPOSED"
                else:
                    db.execute("INSERT INTO replacement116 VALUES (?,?,?,?)",(replacement_id,original_decision,referral_id,excluded_steward))
                    out="PROPOSED_ONLY"
                db.execute("COMMIT")
                return out
            except Exception:
                db.execute("ROLLBACK")
                raise
    def history(self,decision_id):
        with self.machine.connection() as db:
            return db.execute("SELECT concern_id,steward,position,explanation,evidence_ref,prior_concern FROM concerns116 WHERE decision_id=? ORDER BY rowid",(decision_id,)).fetchall()
