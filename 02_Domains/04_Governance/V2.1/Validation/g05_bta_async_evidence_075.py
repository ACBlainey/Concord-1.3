"""Asynchronous owner evidence ledger, an illustrative BTA boundary fixture.

No constitutional authorisation, clock service, cryptographic identity or network transport
is implemented. A spatial GTP overlap is not an authority hierarchy.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    event_id: str
    transition_id: str
    owner: str
    scope: str
    revision: int
    decision: str
    evidence_ref: str
    area: str

class EvidenceLedger:
    def __init__(self):
        self.events={}
        self.latest={}
        self.collisions=set()
        self.clock_paused=True
        self.emergency_active=set()
        self.surviving_duties=set()

    def ingest(self,event):
        if event.event_id in self.events:
            return "REPLAY" if self.events[event.event_id]==event else "EVENT_ID_CONFLICT"
        if not event.evidence_ref or event.revision<0:
            return "INVALID_EVIDENCE"
        key=(event.owner,event.scope,event.area)
        previous=self.latest.get(key)
        if previous and event.revision<previous.revision:
            return "STALE"
        if previous and event.revision==previous.revision and event.decision!=previous.decision:
            self.collisions.add(key)
            self.events[event.event_id]=event
            return "CONFLICT"
        self.events[event.event_id]=event
        if not previous or event.revision>=previous.revision:
            self.latest[key]=event
        return "ACCEPTED"

    def eligible(self,transition_id,required):
        """Required is a set of exact (owner,scope,area) tuples, not spatial ancestors."""
        for key in required:
            if key in self.collisions:
                return False
            event=self.latest.get(key)
            if not event or event.transition_id!=transition_id or event.decision!="APPROVED":
                return False
        return True

    def activate_emergency(self,area):
        self.emergency_active.add(area)

    def expire_emergency(self,area):
        self.emergency_active.discard(area)
        self.surviving_duties.add((area,"RECOVERY_REVIEW"))
