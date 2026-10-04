# Private Local Evaluation — Revision 002 Focused Regression Test 001 — Result and PMEDG Decision

**Date:** 4 October 2026
**Status:** REGRESSION PASS / READY FOR PORTABLE EXTRACTION TESTING / NOT YET GRADUATED
**Candidate:** Private Local Evaluation (PLE)
**Specification:** Candidate Development Specification 002

## 1. Result

The focused Revision 002 regression passed all twelve adversarial cases.

The evaluator's final decision was:

**PASS REGRESSION / READY FOR PORTABLE EXTRACTION TESTING**

No genuine PLE gap was identified that should block the next PMEDG stage.

This result authorises advancement to portable extraction testing. It does not itself constitute portable extraction, module graduation or canonical adoption.

## 2. Cases passed

Revision 002 preserved its intended boundary under:

1. semantic-family reconstruction;
2. cross-recipient collusion;
3. sensitive query content;
4. audit shadow-database pressure;
5. stale credential reuse;
6. invalidation without source disclosure;
7. aggregation handoff;
8. protected predicate and appeal;
9. weak-proxy semantic laundering;
10. participant-local notification;
11. cumulative-disclosure coarsening;
12. reset abuse.

## 3. Key validated behaviours

The regression confirms that PLE can reason across syntactically different but semantically related queries rather than treating query text as the privacy boundary.

It can account for materially foreseeable recipient groups rather than assuming separate recipients imply separate knowledge.

It protects query content as potentially sensitive information.

It prevents ordinary audit from becoming a central participant-specific result database.

It distinguishes stale from false and requires revalidation for consequential use where current truth is required.

It permits invalidation of a result without disclosure of the confidential source-state change.

It preserves aggregation and due process as explicit external handoffs rather than absorbing them.

It preserves the distinction between a correctly evaluated predicate and the broader substantive proposition an actor may wish to infer.

It supports participant-local notification without central match disclosure.

It preserves disclosure history across time where a reset would otherwise permit reconstruction.

## 4. Residual implementation questions

The evaluator identified no architectural blocker.

Implementation-level work remains, especially:
- operational semantic-family equivalence;
- recipient-group/collusion discovery;
- concrete disclosure-state persistence;
- domain-specific coarsening rules;
- protected audit implementation;
- invalidation signalling.

These are appropriate subjects for portable extraction and implementation testing.

They are not reasons to continue expanding the candidate architecture before extraction.

## 5. PMEDG state

**Source resolution:** PASS

**Internal adversarial transfer:** PASS

**Blind Cross-Instance Test 001:** PASS WITH DEVELOPMENT RESIDUALS

**Candidate Specification 002:** REGRESSION PASS

**Focused Regression Test 001:** PASS

**Portable extraction testing:** AUTHORISED / NEXT STAGE

**Portable module graduation:** NOT YET

**Canonical adoption:** NOT YET

## 6. Extraction objective

The next PMEDG stage should determine whether the architecture can be reduced to a genuinely portable module without depending on hidden Concord context.

The extraction must preserve at minimum:
- Query To Data; Minimum Result From Data;
- query/result/action authority separation;
- query competence separation;
- non-binary uncertainty;
- cumulative disclosure state;
- semantic query-family control;
- cross-recipient composition;
- query privacy;
- audit minimisation;
- freshness/cache semantics;
- result scope;
- external handoffs;
- failure toward bounded uncertainty/refusal.

The portable module must remain usable outside Concord and must not silently import Concord-specific institutions as prerequisites.

## 7. Next action

Extract **Private Local Evaluation — Portable Module Candidate v0.1** and prepare a clean-instance portable-module test package.

The extraction should be tested as a standalone architecture against unfamiliar applications before graduation is considered.
