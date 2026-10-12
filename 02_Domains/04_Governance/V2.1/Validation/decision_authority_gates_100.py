"""Source-shaped CBPR/MKA gate adapter fixture, NOT credential verification.

Independent authority inputs are explicit; the adapter cannot mint them.
Tests temporal expiry, action/target scope, revocation, and current host context.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthorityEvidence:
    issuer: str
    subject: str
    action: str
    target: str
    purpose: str
    valid_from: int
    valid_until: int
    revision: int
    evidence_ref: str
    revoked: bool = False

@dataclass(frozen=True)
class ActionRequest:
    subject: str
    action: str
    target: str
    purpose: str
    decision_revision: int

def validate_at_commit(request, evidence, *, now, required_issuers, verified_issuers, current_revision, context_allowed, host_ready):
    """Return DENY unless every independently required authority key matches.

    verified_issuers is supplied by the fixture, not cryptographically proven.
    """
    if not context_allowed or not host_ready:return "DENY_CONTEXT"
    if request.decision_revision != current_revision:return "DENY_REVISION"
    if not required_issuers:return "DENY_NO_AUTHORITY_BASIS"
    by_issuer={}
    for e in evidence:
        if e.issuer not in required_issuers or e.issuer not in verified_issuers:
            continue
        if e.revoked or not e.evidence_ref or e.valid_from>now or now>=e.valid_until:
            continue
        if (e.subject,e.action,e.target,e.purpose,e.revision)!=(request.subject,request.action,request.target,request.purpose,current_revision):
            continue
        by_issuer[e.issuer]=e
    return "ALLOW" if set(required_issuers).issubset(by_issuer) else "DENY_AUTHORITY"
