"""Owner-separated reconciliation acknowledgement journal (prototype, not an authority service)."""
from dataclasses import dataclass,field
@dataclass(frozen=True)
class Acknowledgement:
    event_ref:str
    owner_ref:str
    source_revision:int
    target_revision:int
    evidence_ref:str
    decision:str
    nonce:str

@dataclass
class AcknowledgementJournal:
    expected_owners:tuple
    expected_source_revision:int
    expected_target_revision:int
    event_ref:str
    records:dict=field(default_factory=dict)
    nonces:set=field(default_factory=set)
    conflicts:list=field(default_factory=list)
    def submit(self,ack,authenticated=False,scope_verified=False):
        if ack.event_ref!=self.event_ref:return "EVENT_MISMATCH"
        if ack.owner_ref not in self.expected_owners:return "UNKNOWN_OWNER"
        if not authenticated or not scope_verified:return "UNVERIFIED_OWNER"
        if not ack.evidence_ref or not ack.nonce:return "INCOMPLETE_PROVENANCE"
        if ack.nonce in self.nonces:
            if self.records.get(ack.owner_ref)==ack:return "IDEMPOTENT"
            self.conflicts.append(("REPLAY",ack.owner_ref));return "REPLAY_CONFLICT"
        if ack.owner_ref in self.records:
            self.conflicts.append(("DUPLICATE_OWNER",ack.owner_ref));return "OWNER_CONFLICT"
        if ack.source_revision!=self.expected_source_revision or ack.target_revision!=self.expected_target_revision:
            self.conflicts.append(("REVISION",ack.owner_ref));return "REVISION_CONFLICT"
        if ack.decision not in ("ACK","REJECT"):
            return "INVALID_DECISION"
        self.records[ack.owner_ref]=ack;self.nonces.add(ack.nonce)
        return "RECORDED"
    def status(self):
        missing=sorted(set(self.expected_owners)-set(self.records))
        rejected=sorted(o for o,a in self.records.items() if a.decision=="REJECT")
        agreed=not missing and not rejected and not self.conflicts
        return {"projection_consensus":agreed,"pending_owners":missing,
                "rejected_owners":rejected,"conflicts":list(self.conflicts),
                "authority_granted":False,"duty_closed":False,
                "orphan_cleared":False,"source_mutated":False}
