"""Experimental atomic decision/action journal for test fixtures only.

No constitutional authority is issued here. In-process lock proves only one-process
linearisation; it is not distributed durability or external-effect exactly-once.
"""
from threading import RLock

class AtomicDecisionJournal:
    def __init__(self, decision_id, authorised):
        self.decision_id = decision_id
        self.authorised = authorised
        self.lock = RLock()
        self.positions = {}
        self.stewards = set()
        self.result = "U"
        self.actions = {}
        self.history = []
        self.completed = False

    def accept_vote(self, decision_id, position, steward, ballot, *, mandate=True):
        with self.lock:
            if decision_id != self.decision_id or not self.authorised or not mandate or self.completed:
                return "REJECTED"
            if position not in ("P1", "P2", "P3") or ballot not in ("F", "A", "U"):
                return "REJECTED"
            if position in self.positions:
                return "DUPLICATE" if self.positions[position] == (steward, ballot) else "CONFLICT"
            if steward in self.stewards:
                return "REPEATED_STEWARD"
            if self.result != "U":
                self.history.append(("LATE_PROVENANCE", position, steward, ballot))
                return "PROVENANCE_ONLY"
            self.positions[position] = (steward, ballot)
            self.stewards.add(steward)
            votes = [v for _, v in self.positions.values()]
            if votes.count("F") >= 2: self.result = "F"
            elif votes.count("A") >= 2: self.result = "A"
            self.history.append(("BALLOT", position, steward, ballot))
            return "ACCEPTED"

    def claim_action(self, decision_id, action_id, *, host_authorised=False):
        with self.lock:
            if decision_id != self.decision_id or self.result == "U" or not host_authorised:
                return "REJECTED"
            if action_id in self.actions:
                return "DUPLICATE" if self.actions[action_id] == "DONE" else "RECONCILE"
            self.actions[action_id] = "CLAIMED"
            return "CLAIMED"

    def record_effect(self, action_id, *, confirmed):
        with self.lock:
            if self.actions.get(action_id) != "CLAIMED":
                return "REJECTED"
            self.actions[action_id] = "DONE" if confirmed else "UNCERTAIN"
            return self.actions[action_id]

    def complete(self):
        with self.lock:
            if self.result == "U": return "UNRESOLVED"
            self.completed = True
            return "CLOSED"
