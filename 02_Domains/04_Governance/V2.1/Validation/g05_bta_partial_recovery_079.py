"""Partial-execution and recovery fixture for BTA/GTP integration.

An interruption never implies rollback restored the prior world.
"""
from dataclasses import dataclass,field

@dataclass
class Transition:
    transition_id: str
    state: str="APPROVED_NOT_EXECUTED"
    completed_steps: list=field(default_factory=list)
    failed_steps: list=field(default_factory=list)
    surviving_duties: set=field(default_factory=set)
    owner_review_required: bool=False
    authority_granted: bool=False

    def start(self,revalidated):
        if self.state!="APPROVED_NOT_EXECUTED" or not revalidated:
            return False
        self.state="EXECUTING"
        return True

    def step(self,step_id,success):
        if self.state!="EXECUTING" or step_id in self.completed_steps or step_id in self.failed_steps:
            return False
        if success:
            self.completed_steps.append(step_id)
        else:
            self.failed_steps.append(step_id)
            self.state="INTERRUPTED"
            self.owner_review_required=True
            self.surviving_duties.add("RECOVERY_ASSESSMENT")
        return True

    def interrupt(self,reason):
        if self.state!="EXECUTING":return False
        self.state="INTERRUPTED"
        self.failed_steps.append("INTERRUPTION:"+reason)
        self.owner_review_required=True
        self.surviving_duties.add("RECOVERY_ASSESSMENT")
        return True

    def propose_recovery(self,owner_verified,dependency_revalidated):
        if self.state!="INTERRUPTED" or not owner_verified or not dependency_revalidated:
            return False
        self.state="RECOVERY_PENDING"
        self.owner_review_required=True
        return True

    def record_recovery(self,restoration_evidence):
        if self.state!="RECOVERY_PENDING" or not restoration_evidence:return False
        self.state="RECOVERY_REVIEW"
        return True

    def conclude(self,owner_confirmed,all_duties_resolved):
        if self.state not in ("EXECUTING","RECOVERY_REVIEW"):
            return False
        if not owner_confirmed or not all_duties_resolved or self.failed_steps:
            return False
        self.state="COMPLETED"
        return True
