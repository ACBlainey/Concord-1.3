"""Stage 112: single-transaction contextual early acceptance fixture.

The owner-revision check, contextual evidence checks and decision acceptance
occur under one SQLite write transaction. This is NOT cryptographic proof of
the supplied evidence, and does not bind external systems atomically.
"""
from glass_hammer_context_evidence_111 import verify_context
from glass_hammer_early_acceptance_110 import ContextualDecision

class AtomicContextualDecision(ContextualDecision):
    def __init__(self,path):
        super().__init__(path)
        with self.machine.connection() as db:
            db.execute("CREATE TABLE IF NOT EXISTS owner_context112 (decision_id TEXT PRIMARY KEY, revision INTEGER NOT NULL, context_valid INTEGER NOT NULL, rights_ok INTEGER NOT NULL, necessity_ok INTEGER NOT NULL, proportionality_ok INTEGER NOT NULL)")
            db.execute("CREATE TABLE IF NOT EXISTS acceptance_provenance112 (decision_id TEXT PRIMARY KEY, evidence_ref TEXT NOT NULL, issuer TEXT NOT NULL, evaluator TEXT NOT NULL, revision INTEGER NOT NULL, accepted_at INTEGER NOT NULL)")
    def set_context(self,decision_id,revision,*,context_valid=True,rights_ok=True,necessity_ok=True,proportionality_ok=True):
        with self.machine.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                old=db.execute("SELECT revision FROM owner_context112 WHERE decision_id=?",(decision_id,)).fetchone()
                if old and revision<=old[0]:
                    db.execute("COMMIT")
                    return "DENY_NONMONOTONIC_REVISION"
                db.execute("INSERT INTO owner_context112 VALUES (?,?,?,?,?,?) ON CONFLICT(decision_id) DO UPDATE SET revision=excluded.revision,context_valid=excluded.context_valid,rights_ok=excluded.rights_ok,necessity_ok=excluded.necessity_ok,proportionality_ok=excluded.proportionality_ok",
                           (decision_id,revision,int(context_valid),int(rights_ok),int(necessity_ok),int(proportionality_ok)))
                db.execute("COMMIT")
                return "UPDATED"
            except Exception:
                db.execute("ROLLBACK")
                raise
    def accept_atomic(self,decision_id,evidence,snapshot):
        if evidence is None or snapshot is None:return "DENY_MISSING_CONTEXT_EVIDENCE"
        with self.machine.connection() as db:
            db.execute("BEGIN IMMEDIATE")
            try:
                context=db.execute("SELECT revision,context_valid,rights_ok,necessity_ok,proportionality_ok FROM owner_context112 WHERE decision_id=?",(decision_id,)).fetchone()
                if not context:out="DENY_NO_OWNER_STATE"
                elif snapshot.decision_id!=decision_id or evidence.decision_id!=decision_id:out="DENY_DECISION_BINDING"
                elif context[0]!=snapshot.state_revision:out="DENY_STALE_OWNER_STATE"
                elif not all(context[1:]):out="DENY_OWNER_SAFEGUARDS"
                else:
                    checked=verify_context(evidence,snapshot)
                    if checked!="VALID":out=checked
                    elif db.execute("SELECT 1 FROM acceptance110 WHERE decision_id=?",(decision_id,)).fetchone():out="ALREADY_ACCEPTED"
                    else:
                        state=db.execute("SELECT state FROM decisions WHERE id=?",(decision_id,)).fetchone()
                        if not state:out="DENY_UNKNOWN_DECISION"
                        elif state[0]!="OPEN":out="DENY_DECISION_STATE"
                        else:
                            votes=[r[0] for r in db.execute("SELECT choice FROM ballots WHERE decision_id=?",(decision_id,))]
                            result="F" if votes.count("F")>=2 else "A" if votes.count("A")>=2 else "U"
                            if result=="U":out="DENY_UNRESOLVED"
                            else:
                                early=int(len(votes)<3)
                                db.execute("INSERT INTO acceptance110 VALUES (?,?,?,?)",(decision_id,result,evidence.evidence_ref,early))
                                db.execute("INSERT INTO acceptance_provenance112 VALUES (?,?,?,?,?,?)",(decision_id,evidence.evidence_ref,evidence.issuer,evidence.evaluator,context[0],snapshot.now))
                                db.execute("UPDATE decisions SET state='CLOSED' WHERE id=?",(decision_id,))
                                out="EARLY_ACCEPTED" if early else "ACCEPTED"
                db.execute("COMMIT")
                return out
            except Exception:
                db.execute("ROLLBACK")
                raise
    def provenance(self,decision_id):
        with self.machine.connection() as db:
            return db.execute("SELECT evidence_ref,issuer,evaluator,revision,accepted_at FROM acceptance_provenance112 WHERE decision_id=?",(decision_id,)).fetchone()
