"""Stage 111: independently attested contextual acceptance, fixture only.

Evidence is a typed assertion supplied by a legitimate owning system. This
fixture does NOT cryptographically verify it, determine jurisdiction, or confer
authority. Fail closed for stale, revoked, unbound or self-issued attestations.
"""
from dataclasses import dataclass
from glass_hammer_early_acceptance_110 import ContextualDecision

@dataclass(frozen=True)
class ContextEvidence:
    decision_id: str
    issuer: str
    evaluator: str
    purpose: str
    state_revision: int
    issued_at: int
    expires_at: int
    evidence_ref: str
    justification: str
    review_route: str
    revoked: bool = False

@dataclass(frozen=True)
class OwnerSnapshot:
    decision_id: str
    state_revision: int
    now: int
    authorised_issuers: frozenset
    independently_verified_issuers: frozenset
    context_still_valid: bool
    rights_guard_ok: bool
    necessity_guard_ok: bool
    proportionality_guard_ok: bool

def verify_context(e: ContextEvidence, s: OwnerSnapshot):
    if e.decision_id!=s.decision_id:return "DENY_DECISION_BINDING"
    if e.issuer not in s.authorised_issuers or e.issuer not in s.independently_verified_issuers:return "DENY_ISSUER"
    if e.evaluator=="" or e.evaluator==e.issuer:return "DENY_SELF_ASSERTION"
    if e.state_revision!=s.state_revision:return "DENY_REVISION"
    if e.revoked or not e.evidence_ref or not e.justification or not e.review_route or not e.purpose:return "DENY_INCOMPLETE"
    if e.issued_at>s.now or s.now>=e.expires_at:return "DENY_EXPIRED"
    if not s.context_still_valid:return "DENY_CONTEXT"
    if not (s.rights_guard_ok and s.necessity_guard_ok and s.proportionality_guard_ok):return "DENY_SAFEGUARDS"
    return "VALID"

class EvidenceGatedAcceptance:
    def __init__(self, path):
        self.decision=ContextualDecision(path)
    def accept(self,decision_id,evidence,snapshot):
        # Source of truth for early acceptance is the owner; this only checks
        # an owner-supplied, independently verified attestation snapshot.
        if evidence is None or snapshot is None:return "DENY_MISSING_CONTEXT_EVIDENCE"
        result=verify_context(evidence,snapshot)
        if result!="VALID":return result
        return self.decision.accept(decision_id,early_context_justified=True,basis=evidence.evidence_ref)
