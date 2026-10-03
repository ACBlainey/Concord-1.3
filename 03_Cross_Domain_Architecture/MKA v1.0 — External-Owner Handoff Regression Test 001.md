# MKA v1.0 — External-Owner Handoff Regression Test 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Module:** Multi-Key Authority — Portable Module v1.0  
**Status:** POST-GRADUATION REGRESSION TEST / COMPLETE  
**Test target:** `EXTERNAL_OWNER_REQUIRED` and `OUTSIDE_MKA_SCOPE`

# 1. Purpose

Test whether the two interface states added at graduation improve MKA handoff clarity without changing authority semantics or allowing MKA to evade a genuine authority gap.

The test specifically guards against:

1. using `EXTERNAL_OWNER_REQUIRED` as a substitute for `HOLD_MISSING_AUTHORITY`;
2. using `OUTSIDE_MKA_SCOPE` to ignore an authority dimension that materially affects the proposed act;
3. treating an external owner as automatically authoritative;
4. treating handoff as authorisation;
5. treating handoff as successful resolution;
6. absorbing the external owner's function into MKA.

# 2. Core regression rule

> **External Handoff != Authority Creation**

And:

> **External Owner Identification != External Owner Legitimacy**

And:

> **Handoff Complete != Authority Gap Resolved**

# 3. State-selection distinction

Use `EXTERNAL_OWNER_REQUIRED` where:

- the unresolved question is materially relevant;
- MKA identifies that the question belongs to another architecture/domain function;
- a legitimate owner/resolver must supply the missing state or decision before MKA can continue.

Use `OUTSIDE_MKA_SCOPE` where:

- the requested decision itself is not part of MKA's authority-composition function;
- no MKA authority decision is currently being requested.

Continue to use authority-gap states where the problem is actually missing authority:

- `HOLD_MISSING_AUTHORITY`;
- `HOLD_UNKNOWN_AUTHORITY`;
- `HOLD_DISPUTED_AUTHORITY`.

An external-owner reference may accompany one of those states.

# 4. Scenario 1 — Transition completion

A migration is authorised to begin. Source system reports SENT and destination reports NOT_RECEIVED. The caller asks MKA to declare the migration complete.

Result:

`OUTSIDE_MKA_SCOPE`

Transition completion belongs to transition architecture.

If later consequential action depends on completion, MKA may require an externally supplied transition-completion state before authorising that later act.

**PASS**

# 5. Scenario 2 — Runtime configuration

An agent's purchase authority is valid. The caller asks MKA to choose CPU quota and firewall configuration.

Result:

`OUTSIDE_MKA_SCOPE`

Runtime configuration belongs to the runtime owner.

The valid purchase authority remains unaffected.

**PASS**

# 6. Scenario 3 — Context precedence missing

An act crosses two contexts whose precedence relation is not supplied. MKA cannot establish which authority rule applies.

Result:

`EXTERNAL_OWNER_REQUIRED`

plus, where the missing relation makes authority materially unknown:

`HOLD_UNKNOWN_AUTHORITY`

MKA must not invent the precedence relation.

**PASS**

# 7. Scenario 4 — Missing legal authority

A police actor has authority to investigate but no supplied authority to search a protected location.

Incorrect result:

`EXTERNAL_OWNER_REQUIRED` alone.

Correct result:

`HOLD_MISSING_AUTHORITY`

The fact that Law or Judiciary may own the process for obtaining search authority does not make the current defect merely a routing issue.

An `ExternalOwnerRef` may identify the legitimate route for resolving the missing authority.

**PASS**

# 8. Scenario 5 — Disputed authority

Two authority sources conflict and a legitimate resolver is identified.

Result:

`HOLD_DISPUTED_AUTHORITY`

with:

`ExternalOwnerRef = Resolver`

`EXTERNAL_OWNER_REQUIRED` may describe the handoff but must not replace the dispute state.

**PASS**

# 9. Scenario 6 — Unknown participant classification

A proposed act may affect an entity whose protected participant status is unresolved. Identity/standing classification belongs externally.

Result:

`EXTERNAL_OWNER_REQUIRED`

and, if that classification changes required authority:

`HOLD_UNKNOWN_AUTHORITY`

MKA cannot classify participant standing merely to finish its own check.

**PASS**

# 10. Scenario 7 — External owner itself lacks authority

MKA identifies Domain D as the functional owner of a required state. D supplies a decision but the scenario states D lacks legitimate authority to make that decision.

Result:

The returned state does not become valid merely because it came from the expected functional owner.

MKA must distinguish:

- function ownership;
- legitimate authority.

Result remains blocked/unknown according to the missing legitimate basis.

> **Functional Owner != Legitimate Authority Holder By Default**

**PASS**

# 11. Scenario 8 — Handoff without response

MKA hands a required question to a legitimate external owner. No response has yet returned.

Result:

The original unresolved state remains unresolved.

> **Handoff Initiated != Handoff Resolved**

**PASS**

# 12. Scenario 9 — External owner returns valid state

A legitimate external owner supplies the required current state with adequate scope and provenance.

Result:

MKA may resume its own verification using the supplied state.

It does not need to reproduce the external owner's reasoning unless the host requires that evidence for verification.

**PASS**

# 13. Scenario 10 — Attempted scope escape

A system lacks authority for a consequential act and labels the missing authority question `OUTSIDE_MKA_SCOPE` so execution can continue.

Result:

Invalid.

The missing authority is directly inside MKA's verification scope.

`OUTSIDE_MKA_SCOPE` cannot be used to erase a materially required authority dimension.

**PASS**

# 14. Scenario 11 — Clinical validity

MKA is used in a medical allocation system. Whether a treatment remains clinically effective is not MKA-owned.

Result:

`EXTERNAL_OWNER_REQUIRED` for clinical validity.

If the authority to act depends on that predicate, MKA remains pending until a legitimate clinical owner supplies the current state.

MKA does not invent prognosis.

**PASS**

# 15. Scenario 12 — External owner supplies recommendation, not authority state

An external expert says an act is desirable but does not supply the required authority or predicate state.

Result:

No authority is created.

> **External Recommendation != Authority**

**PASS**

# 16. Scenario 13 — CWA handoff

MKA detects that the proposed route may enter a nested protected context, but the contextual classification is unavailable.

Result:

`EXTERNAL_OWNER_REQUIRED` to the context owner.

If classification is material to authority:

`HOLD_UNKNOWN_AUTHORITY`

MKA does not create the context classification.

**PASS**

# 17. Scenario 14 — BTA handoff

A consequential act depends on whether a prior transition completed.

MKA receives no valid completion state.

Result:

`EXTERNAL_OWNER_REQUIRED` to the transition owner and a hold state if completion is an authority predicate.

MKA does not infer completion from initiation.

**PASS**

# 18. Scenario 15 — CBPR handoff

MKA authorises an action within scope. The caller asks whether a recovered runtime may safely retry an action with unknown commit outcome.

Result:

`OUTSIDE_MKA_SCOPE` for retry/commit-recovery mechanics.

If CBPR later proposes a repeated consequential action, that proposed act may return through MKA for current authority verification.

**PASS**

# 19. Scenario 16 — Circular handoff

MKA sends a question to System A. System A sends it back to MKA without supplying new substantive state.

Result:

No resolution.

The system must preserve the unresolved state and expose the circular dependency.

> **Circular Handoff != Resolution**

**PASS**

# 20. Scenario 17 — Multiple external owners

A proposed act requires context classification from CWA-equivalent owner C and transition state from BTA-equivalent owner T.

Result:

MKA may preserve multiple `ExternalOwnerRef` values or a structured collection.

All materially required returned states must be available before a completeness claim relying on them can pass.

**PASS**

# 21. Scenario 18 — Optional external advice

An external system can provide useful but non-material advice. MKA already has complete authority state.

Result:

No mandatory handoff.

> **Useful External Input != Required External Owner**

**PASS**

# 22. Scenario 19 — Low-consequence permission case

Ordinary private permission is sufficient. A host nevertheless has many external governance systems available.

Result:

`PERMISSION_SUFFICIENT`

MKA does not trigger external-owner routing merely because external systems exist.

**PASS**

# 23. Scenario 20 — External owner changes after proposal

At proposal time, Owner A is the legitimate resolver. Before commit, authority transfers legitimately to Owner B.

Result:

The handoff/authority state must be refreshed where material.

A stale Owner A response cannot automatically satisfy a current Owner B-controlled requirement.

**PASS**

# 24. Regression findings

The new vocabulary does not alter the tested authority semantics.

It improves three distinctions:

1. **MKA-owned unresolved authority**;
2. **externally owned prerequisite state**;
3. **questions that are simply outside MKA's function**.

The strongest operational rule is:

> **External-owner routing may accompany an authority hold, but must never erase the hold when the missing external state is necessary to establish authority.**

# 25. Additional invariants

MKA-32 **External Owner Identification != External Owner Legitimacy.**

MKA-33 **Handoff Initiated != Handoff Resolved.**

MKA-34 **Functional Owner != Legitimate Authority Holder By Default.**

MKA-35 **Outside-MKA-Scope != Permission To Ignore A Required Authority Dimension.**

MKA-36 **External Recommendation != Authority.**

MKA-37 **Circular Handoff != Resolution.**

MKA-38 **Useful External Input != Required External Owner.**

# 26. Result

**PASS — NO REGRESSION / INTERFACE CLARIFICATION VALIDATED**

The graduation clarification improves routing while preserving the original frozen kernel's authority semantics.

No v1.0 correction is required.

# 27. Next maturation interface

The highest-value next integration test is:

**MKA + CWA + CBPR + BTA — Live Composition Test 001**

Purpose:

test one consequential act through:

1. contextual classification/permission;
2. authority-space completeness/composition;
3. bounded runtime execution;
4. transition tracking;

while verifying that no architecture silently absorbs another's state or authority.
