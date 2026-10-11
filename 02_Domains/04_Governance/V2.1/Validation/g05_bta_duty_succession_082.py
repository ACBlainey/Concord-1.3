"""Duty succession candidate: transfer custody without extinguishing obligation.

No legal successor designation or constitutional authority is inferred.
"""
from dataclasses import dataclass,field

@dataclass(frozen=True)
class Custody:
    duty_id: str
    custodian: str
    revision: int
    obligation_state: str="OPEN"

@dataclass
class SuccessionLedger:
    records: dict=field(default_factory=dict)
    history: list=field(default_factory=list)
    pending: dict=field(default_factory=dict)

    def register(self,record):
        if record.duty_id in self.records:return False
        self.records[record.duty_id]=record
        self.history.append(("REGISTER",record.duty_id,record.custodian))
        return True

    def propose(self,duty_id,successor,origin_evidence,successor_evidence,expected_revision):
        current=self.records.get(duty_id)
        if not current or current.obligation_state!="OPEN" or duty_id in self.pending:
            return "NOT_ELIGIBLE"
        if not successor or successor==current.custodian or not origin_evidence or not successor_evidence:
            return "EVIDENCE_OR_SUCCESSOR_MISSING"
        if expected_revision!=current.revision:return "STALE"
        self.pending[duty_id]=(successor,origin_evidence,successor_evidence,expected_revision)
        self.history.append(("PROPOSE",duty_id,successor))
        return "PENDING"

    def confirm(self,duty_id,owner_verified,successor_verified):
        proposal=self.pending.get(duty_id)
        if not proposal:return "NO_PROPOSAL"
        current=self.records[duty_id]
        if current.revision!=proposal[3]:return "STALE"
        if not owner_verified or not successor_verified:return "NOT_VERIFIED"
        successor=proposal[0]
        self.records[duty_id]=Custody(duty_id,successor,current.revision+1,current.obligation_state)
        del self.pending[duty_id]
        self.history.append(("TRANSFER",duty_id,current.custodian,successor))
        return "TRANSFERRED"

    def retire_custodian(self,custodian):
        return {"retirement_recorded":True,
                "untransferred_open_duties":[r.duty_id for r in self.records.values()
                    if r.custodian==custodian and r.obligation_state=="OPEN"],
                "obligations_extinguished":False}
