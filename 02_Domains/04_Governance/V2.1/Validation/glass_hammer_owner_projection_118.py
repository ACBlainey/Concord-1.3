"""Stage 118: owner-checked projections using Stage 101 grants.

The owner is read independently; the caller cannot set authority_verified.
Fixture-level security only: no authentication, no crypto, no sealed DB service.
"""
from authority_owner_registry_101 import OwnerRegistry, Request
from glass_hammer_isolation_117 import IsolatedConcernReview

class OwnerCheckedProjection:
    def __init__(self,decision_db,owner_db,issuer="PROJECTION_OWNER"):
        self.isolated=IsolatedConcernReview(decision_db)
        self.owner=OwnerRegistry(owner_db,issuer)
    def project(self,*,decision_id,subject,role,grant_ref,now,revision,steward=None):
        if role not in ("STEWARD","PUBLIC","REVIEW_ROUTER"):return {"status":"DENY_ROLE"}
        if role=="STEWARD" and (not steward or subject!=steward):return {"status":"DENY_SUBJECT_BINDING"}
        request=Request(subject,"PROJECT_"+role,decision_id,"VOTE_CONTEXT_VIEW",revision)
        if self.owner.check(grant_ref,request,now)!="VALID":return {"status":"DENY_OWNER_GRANT"}
        return self.isolated.view(decision_id,role=role,steward=steward,authority_verified=True)
    def reviewer(self,*,decision_id,subject,grant_ref,now,revision,independence_ref):
        if not independence_ref:return {"status":"DENY_INDEPENDENCE_EVIDENCE"}
        # Two separately scoped owner-issued grants: access and independence.
        access=Request(subject,"PROJECT_REVIEW_CONCERN",decision_id,"REVIEW_EVIDENCE",revision)
        independence=Request(subject,"VERIFY_INDEPENDENT_REVIEWER",decision_id,"REVIEW_INDEPENDENCE",revision)
        if self.owner.check(grant_ref,access,now)!="VALID":return {"status":"DENY_OWNER_GRANT"}
        if self.owner.check(independence_ref,independence,now)!="VALID":return {"status":"DENY_INDEPENDENCE"}
        # Never give reviewer raw ballots as a side effect of concern access.
        return self.isolated.view_reviewer_evidence(decision_id,review_owner_authority_verified=True,independent_of_stewards=True)
