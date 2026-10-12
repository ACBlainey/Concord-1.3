"""Stage 120: seventh digit is a count-only, read-only vote projection.

The lock fixture intentionally has no dependency on decision DB, vote count,
vote contents, or indicator availability. Not a physical lock implementation.
"""
import sqlite3
from glass_hammer_isolation_117 import IsolatedConcernReview

class IndependentCaseLock:
    def __init__(self,combinations):
        self._combinations=dict(combinations)
        self._opened=set()
    def open_case(self,steward,combination):
        if steward not in self._combinations:return "DENY_UNKNOWN_STEWARD"
        if combination!=self._combinations[steward]:return "DENY_COMBINATION"
        self._opened.add(steward)
        return "OPENED"
    def is_open(self,steward):return steward in self._opened

class SeventhDigitDecision(IsolatedConcernReview):
    def seventh_digit(self,decision_id,*,indicator_available=True):
        if not indicator_available:return {"status":"UNAVAILABLE"}
        with self.machine.connection() as db:
            db.execute("BEGIN")
            try:
                if db.execute("SELECT 1 FROM decisions WHERE id=?",(decision_id,)).fetchone() is None:
                    return {"status":"DENY_UNKNOWN_DECISION"}
                rows=db.execute("SELECT position FROM ballots WHERE decision_id=? UNION SELECT position FROM late_ballots110 WHERE decision_id=?",(decision_id,decision_id)).fetchall()
                return {"status":"OK","digit":len(rows)}
            finally:
                db.execute("ROLLBACK")
    def steward_display(self,decision_id,*,steward,authority_verified=False,indicator_available=True):
        if not authority_verified or not steward:return {"status":"DENY_AUTHORITY"}
        return self.seventh_digit(decision_id,indicator_available=indicator_available)
