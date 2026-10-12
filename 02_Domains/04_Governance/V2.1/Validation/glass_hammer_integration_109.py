"""Stage 109: integration adapter, not a Concord production authority service.

The owning ballot state machine consumes the vote; a read-only projection
provides consequence-relevant transitions. No Clock call is required to vote.
A resolved decision is evidence, never permission for host execution.
"""
from dataclasses import dataclass
from glass_hammer_state_108 import BallotMachine

@dataclass(frozen=True)
class DecisionProjection:
    decision_id: str
    state: str
    result: str
    ballots: tuple
    execution_authorised: bool = False

def project(machine: BallotMachine, decision_id):
    state, ballots=machine.snapshot(decision_id)
    if state is None: return None
    return DecisionProjection(decision_id,state,machine.result(decision_id),tuple(ballots))

def crstl_records(machine: BallotMachine, decision_id):
    """Read-only, source-shaped CRSTL projection, not a Clock write or permission."""
    with machine.connection() as db:
        rows=db.execute("SELECT t.event_id,t.position,t.before_state,t.after_state,b.steward,b.choice FROM transitions t JOIN ballots b ON b.event_id=t.event_id WHERE t.decision_id=? ORDER BY t.rowid",(decision_id,)).fetchall()
    return tuple({"transition_id":event,"domain":"Governance","decision_id":decision_id,
                  "position":position,"prior_state":before,"next_state":after,
                  "actor":steward,"choice":choice,"authority_source":"owning_governance_state_machine",
                  "clock_authority":False,"temporal_order_claim":"LOCAL_JOURNAL_ONLY"}
                 for event,position,before,after,steward,choice in rows)

def execution_gate(projection, *, separate_host_authority=False, current_context=False):
    """Even a resolved decision cannot self-authorise an external host action."""
    if projection is None or projection.state!="CLOSED" or projection.result=="U":
        return "DENY_UNRESOLVED"
    if not separate_host_authority or not current_context:
        return "DENY_NO_FRESH_EXECUTION_AUTHORITY"
    return "ELIGIBLE_FOR_HOST_REVALIDATION"
