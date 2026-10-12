"""Provisional G03/G07 event-state fixture. NOT a deployed authority service."""
from dataclasses import dataclass, field

@dataclass
class Decision:
    decision_id: str
    authorised: bool
    positions: dict = field(default_factory=dict)
    steward_ids: set = field(default_factory=set)
    result: str = "U"
    actions: dict = field(default_factory=dict)
    completed: bool = False
    provenance: list = field(default_factory=list)

    def vote(self, position, steward, ballot, *, mandate=True):
        if not self.authorised or not mandate or self.completed:
            return "REJECTED"
        if ballot not in ("F", "A", "U") or position not in ("P1", "P2", "P3"):
            return "REJECTED"
        if position in self.positions:
            return "DUPLICATE" if self.positions[position] == (steward, ballot) else "CONFLICT"
        if steward in self.steward_ids:
            return "REPEATED_STEWARD"
        if self.result != "U":
            self.provenance.append((position, steward, ballot))
            return "PROVENANCE_ONLY"
        self.positions[position] = (steward, ballot)
        self.steward_ids.add(steward)
        votes = [v for _, v in self.positions.values()]
        if votes.count("F") >= 2: self.result = "F"
        if votes.count("A") >= 2: self.result = "A"
        return "ACCEPTED"

    def expanded(self, position, members, ballots, *, mandate=False):
        if not mandate or not self.authorised or self.result != "U" or self.completed:
            return "NO_EXPANSION_AUTHORITY"
        if len(members) != 3 or len(set(members)) != 3 or any(m in self.steward_ids for m in members):
            return "REPEATED_STEWARD"
        if position in self.positions:
            return "CONFLICT"
        if any(v not in ("F", "A", "U") for v in ballots) or len(ballots) != 3:
            return "REJECTED"
        result = "F" if ballots.count("F") >= 2 else "A" if ballots.count("A") >= 2 else "U"
        if result == "U": return "UNRESOLVED"
        status = self.vote(position, "EXPANDED:" + position, result)
        if status == "ACCEPTED": self.steward_ids.update(members)
        return status

    def action(self, action_id, *, host_authorised=False, effect_known=True):
        if self.result == "U" or not host_authorised:
            return "REJECTED"
        if action_id in self.actions:
            return "DUPLICATE" if self.actions[action_id] == "DONE" else "RECONCILE"
        self.actions[action_id] = "DONE" if effect_known else "UNCERTAIN"
        return self.actions[action_id]

    def close(self):
        if self.result == "U": return "UNRESOLVED"
        self.completed = True
        return "CLOSED"
