"""Orphaned duty detection and protected referral fixture.

Detection, safeguarding, referral and assumption of custody are distinct.
No authority or legal duty is assigned to the referral destination.
"""
from dataclasses import dataclass,field

@dataclass(frozen=True)
class Orphan:
    duty_id: str
    last_custodian: str
    origin_transition: str
    evidence_ref: str
    protected_beneficiary_ref: str
    state: str="UNASSIGNED"

@dataclass
class OrphanRegistry:
    records: dict=field(default_factory=dict)
    referrals: list=field(default_factory=list)
    events: list=field(default_factory=list)

    def detect(self,duty_id,last_custodian,origin_transition,evidence_ref,beneficiary_ref):
        if not all((duty_id,last_custodian,origin_transition,evidence_ref)):
            return "INSUFFICIENT_PROVENANCE"
        if duty_id in self.records:
            return "ALREADY_RECORDED"
        self.records[duty_id]=Orphan(duty_id,last_custodian,origin_transition,evidence_ref,beneficiary_ref)
        self.events.append(("ORPHAN_DETECTED",duty_id))
        return "RECORDED"

    def refer(self,duty_id,contact_ref,reason):
        if duty_id not in self.records:return "UNKNOWN_DUTY"
        if not contact_ref or not reason:return "INVALID_REFERRAL"
        self.referrals.append((duty_id,contact_ref,reason))
        self.events.append(("REFERRED_FOR_REVIEW",duty_id,contact_ref))
        return "REFERRED_NOT_ASSIGNED"

    def nominate(self,duty_id,candidate,qualification_evidence):
        if duty_id not in self.records:return "UNKNOWN_DUTY"
        if not candidate or not qualification_evidence:return "NOT_QUALIFIED"
        self.events.append(("SUCCESSOR_NOMINATED",duty_id,candidate))
        return "REQUIRES_OWNER_AND_SUCCESSOR_VERIFICATION"

    def status(self,duty_id):
        item=self.records.get(duty_id)
        return {"discoverable":item is not None,"custody_assigned":False,
                "duty_extinguished":False,
                "protected_beneficiary_ref":item.protected_beneficiary_ref if item else None}
