"""Stage 117: decision-specific information projections; no host access control.

Projection rules are independent of a caller's requested fields. A steward
never receives other ballots or other stewards' concerns through this adapter.
"""
from glass_hammer_concern_review_116 import ConcernReview

class IsolatedConcernReview(ConcernReview):
    def view(self,decision_id,*,role,steward=None,authority_verified=False):
        if not authority_verified:return {"status":"DENY_AUTHORITY"}
        with self.machine.connection() as db:
            row=db.execute("SELECT state FROM decisions WHERE id=?",(decision_id,)).fetchone()
            if row is None:return {"status":"DENY_UNKNOWN_DECISION"}
            votes=db.execute("SELECT position,steward,choice FROM ballots WHERE decision_id=? UNION ALL SELECT position,steward,choice FROM late_ballots110 WHERE decision_id=?",(decision_id,decision_id)).fetchall()
            concerns=db.execute("SELECT concern_id,steward,position,explanation,evidence_ref FROM concerns116 WHERE decision_id=?",(decision_id,)).fetchall()
            accepted=db.execute("SELECT accepted_result FROM acceptance110 WHERE decision_id=?",(decision_id,)).fetchone()
        if role=="STEWARD":
            if not steward:return {"status":"DENY_IDENTITY"}
            own=[{"position":p,"choice":v} for p,s,v in votes if s==steward]
            own_concerns=[{"concern_id":c,"explanation":x,"evidence_ref":e} for c,s,p,x,e in concerns if s==steward]
            return {"status":"OK","decision_id":decision_id,"own_ballots":own,"own_concerns":own_concerns,"other_ballots":"SEALED","other_concerns":"SEALED"}
        if role=="PUBLIC":
            if row[0]!="CLOSED":return {"status":"PENDING","decision_id":decision_id}
            return {"status":"OK","decision_id":decision_id,"accepted_result":accepted[0] if accepted else None,"ballots":"SEALED","concerns":"SEALED"}
        if role=="REVIEW_ROUTER":
            return {"status":"OK","decision_id":decision_id,"concern_ids":[c for c,s,p,x,e in concerns],"ballots":"SEALED","concern_contents":"SEALED"}
        return {"status":"DENY_ROLE"}
    def view_reviewer_evidence(self,decision_id,*,review_owner_authority_verified=False,independent_of_stewards=False):
        if not review_owner_authority_verified or not independent_of_stewards:return {"status":"DENY_REVIEW_ACCESS"}
        # This is a deliberately separate privileged projection, not a vote.
        with self.machine.connection() as db:
            concerns=db.execute("SELECT concern_id,steward,explanation,evidence_ref FROM concerns116 WHERE decision_id=?",(decision_id,)).fetchall()
        return {"status":"OK","concerns":tuple(concerns),"ballots":"SEALED_PENDING_SEPARATE_DISCLOSURE_AUTHORITY"}
