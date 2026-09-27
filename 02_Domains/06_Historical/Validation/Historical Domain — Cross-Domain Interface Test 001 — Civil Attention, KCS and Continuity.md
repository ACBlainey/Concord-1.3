# Historical Domain — Cross-Domain Interface Test 001 — Civil Attention, KCS and Continuity

**Project:** The Concord  
**Domain:** Historical  
**Status:** CROSS-DOMAIN INTERFACE TEST / DEVELOPMENT  
**Date:** 25 September 2026  
**Target:** Historical Domain — Formal Domain Specification v0.2  
**Compared systems:** Civil Attention; Knowledge Control System dependency/change-propagation architecture; Continuity Protocol V2  
**Purpose:** Test whether Historical's proposed boundaries survive contact with existing Concord systems rather than merely appearing coherent in isolation.

---

# 1. Test Rule

A boundary is successful when:

1. Historical receives enough information to preserve interpretable past state;
2. the neighbouring system retains its legitimate operational function;
3. neither system silently duplicates the other's authority;
4. state can cross the interface without losing provenance, status, permissions or temporal meaning;
5. later reconstruction can distinguish the live operational state from the archived historical state.

---

# 2. Civil Attention ↔ Historical

Civil Attention defines the participant-facing path:

```text
Participant
→ Common Intake
→ Original Submission Preservation
→ Issue Object
→ Domain Action Objects
→ Domain Examination / Action
→ Domain Status Return
→ Central Resolution Record
→ Participant Feedback / Reviewability
```

Its core rule is:

> **Central Visibility ≠ Central Control.**

Historical has a strongly compatible rule:

> **Historical Custody ≠ Operational Authority.**

These systems therefore share a useful architectural pattern: central legibility without centralised substantive power.

## Interface ownership

Civil Attention owns:

- participant intake;
- provisional classification;
- issue matching;
- routing;
- action ownership visibility;
- current resolution state;
- return path;
- participant feedback.

Historical owns:

- temporal custody of relevant states;
- preservation of submissions and subsequent state transitions where qualified;
- historical provenance;
- reconstruction of what issue existed and how it travelled through the system;
- preservation of later corrections and status history.

## Required handoff objects

Historical should be capable of receiving or referencing:

- original submission;
- Issue ID;
- input class;
- creation time;
- provisional classification history;
- routing history;
- Domain Action Object references;
- status transitions;
- material responses;
- dependencies/review conditions;
- disposition;
- participant-facing feedback state;
- privacy/access state;
- unresolved/reopened state.

## Boundary test

Historical must not decide whether a problem report is valid, whether a petition should succeed, whether a domain action is sufficient, or whether an Issue is operationally resolved.

It may reconstruct those decisions.

### Result CA-H1 — PASS

No authority collision found.

### Important finding CA-H2

Civil Attention's rule:

> **Every Outbound Route Requires a Return Path**

has a Historical analogue:

> **Every consequential state transition should remain reconstructably linked to the state that preceded and followed it.**

The two systems can therefore interoperate naturally through linked Issue/Action/Status objects.

### Important finding CA-H3

Civil Attention explicitly states:

> **Domain Completion ≠ Issue Resolution.**

Historical must preserve this distinction. Archiving a completed Domain Action must not make the parent Issue appear historically resolved if other actions remained open.

### Important finding CA-H4

A participant submission may later prove false, mistaken, malicious, incomplete or insightful.

Historical should preserve:

```text
Submission Existed
≠
Submission Was True
```

This matches the Historical belief/evidence distinction already developed.

---

# 3. KCS ↔ Historical

KCS defines live civilisational knowledge state with provenance, epistemic status, supersession, history, dependencies and change propagation.

Its companion architecture defines:

```text
K(t) = <V, R, P, S, H>
```

and explicitly distinguishes live dependency state from authority.

Historical overlaps heavily with KCS at first glance.

This is therefore a high-risk boundary.

## KCS owns

- current knowledge-object state;
- current epistemic status;
- live dependency representation;
- current materiality/criticality state;
- change-propagation review sets;
- current supersession and compatibility state;
- live dependency freshness/review.

## Historical owns

- temporal custody of previous KCS states where qualified;
- reconstruction of what KCS represented at historical time T;
- preservation of KCS schema/state transitions;
- preservation of past dependency states and their later correction;
- reconstruction of what downstream systems could have known from KCS at time T.

## Core separation

> **KCS tells civilisation what its represented knowledge state currently is.**

> **Historical tells civilisation what that represented knowledge state was, how it changed, and what its historical limits were.**

This is a clean temporal division.

## Boundary test: corrected dependency

At T1 KCS records:

```text
A DEPENDS_ON B
State = ACTIVE
Confidence = HIGH
```

At T2 evidence shows the relation was false.

KCS updates the current relation and propagates appropriate review.

Historical preserves:

- T1 relation;
- evidence then available;
- T2 correction;
- correction provenance;
- downstream review consequences.

Historical must not continue presenting the T1 relation as current.

KCS must not erase the fact that T1 existed.

### Result KCS-H1 — PASS

The systems are complementary.

### Important finding KCS-H2

Historical should not create a competing live dependency graph.

Where a relationship is operationally maintained by KCS, Historical should normally preserve historical snapshots/events or temporal projections of that graph.

Otherwise:

```text
KCS Live Graph
+
Historical Live Graph
→ competing sources of current truth
```

### Important finding KCS-H3

KCS already includes UNKNOWN and DISPUTED dependency states and explicitly states that absence from KCS is not proof of civil absence.

This strongly aligns with Historical's ESCP architecture.

The interface should preserve those states rather than converting them into simple null/absent values.

### Important finding KCS-H4

KCS change propagation generates a **review set**, not automatic invalidation.

Historical must preserve that distinction.

A historical record that an object was marked REVIEW_REQUIRED does not establish that the object was invalid.

### Important finding KCS-H5

KCS may change its dependency graph retrospectively after discovering a previously missing dependency.

Historical therefore needs both:

```text
Current KCS reconstruction of dependency history
and
Actual KCS represented state at historical time T
```

These are not identical.

This is another direct application of Contemporary Reconstruction versus Present-Best Reconstruction.

---

# 4. Continuity ↔ Historical

Continuity Protocol V2 treats preservation as a constitutional responsibility but extends beyond information retention into:

- participant continuity;
- institutional continuity;
- infrastructure;
- constitutional succession;
- restoration;
- civilisational resilience;
- capability stewardship.

Historical preserves evidence needed by Continuity but must not become Continuity.

## Continuity owns

- recovery planning;
- restoration decisions;
- capability continuity;
- continuity arrangements;
- resilience;
- succession;
- restoration verification;
- current stewardship action.

## Historical owns

- historical state;
- past capability records;
- provenance;
- former dependency context;
- prior recovery attempts;
- failure history;
- restoration evidence as history;
- reconstruction of previous configurations.

## Boundary test: restoring an old system

A critical system fails.

Continuity queries Historical for the last known functioning configuration.

Historical returns:

- historical configuration;
- date;
- dependencies;
- authority state;
- known limitations;
- provenance;
- later corrections;
- recoverability status.

Historical must not say:

> "Restore this."

Continuity must evaluate whether restoration is legitimate, safe and compatible with current architecture.

### Result C-H1 — PASS

The authority boundary holds.

## Important finding C-H2 — Non-Loss Tension

Continuity adopts a Principle of Non-Loss: minimise unnecessary loss.

Historical also values preservation but must support privacy, forgetting and authorised destruction.

These are not contradictions.

They imply:

> **Non-Loss ≠ Universal Retention.**

Loss can be necessary to preserve autonomy, privacy, safety or legitimate constitutional boundaries.

Historical therefore needs to communicate destruction/forgetting decisions to Continuity where they materially affect recoverability, without allowing Continuity's preservation objective to silently veto legitimate forgetting.

## Important finding C-H3 — Library Language

Continuity describes the Library as constitutional memory and includes historical records among its preserved content.

Historical now provides a more specialised architecture for temporal state and reconstruction.

This suggests a useful refinement:

> **Library preserves usable civilisational knowledge; Historical preserves interpretable civilisational past state; Continuity preserves the ability to carry necessary civilisational capability forward.**

The three overlap in objects but differ in function.

## Important finding C-H4 — Provenance

Continuity's provenance model strongly supports Historical, but its language of permanent provenance may conflict in edge cases with legitimate anonymity, privacy and forgetting.

Historical v0.2 already resolves this through:

> **Provenance Completeness ≠ Identity Traceability.**

This may eventually need back-propagation into Continuity/KCS wording so "permanent provenance" cannot be misread as permanent public identity linkage.

## Important finding C-H5 — Honest Failure

Continuity explicitly preserves honest failure because failed work can prevent repeated mistakes.

Historical's developmental-memory and negative-space architecture provides the temporal mechanism for this.

The interface is therefore reinforcing rather than duplicative:

```text
Continuity says why failure should survive.
Historical specifies how its historical meaning survives.
```

---

# 5. Three-System Interaction

A useful combined case is:

1. participant reports a systemic failure through Civil Attention;
2. the responsible domain investigates;
3. investigation changes a KCS dependency;
4. KCS identifies downstream review requirements;
5. a continuity plan becomes outdated;
6. systems are corrected;
7. Historical preserves the full temporal chain.

The chain is:

```text
Civil Attention
    ↓
Issue / Routing / Domain Action
    ↓
Domain Finding
    ↓
KCS Knowledge / Dependency Change
    ↓
Review Propagation
    ↓
Continuity Re-evaluation
    ↓
Operational Changes
    ↓
Historical Temporal Custody
```

Historical may also support later reconstruction across the entire chain without becoming the operational controller of any step.

This is exactly the kind of multi-system event for which relational preservation is necessary.

If Historical preserved only the final corrected documents, it would lose:

- the original participant signal;
- why investigation occurred;
- what KCS previously represented;
- what changed;
- which systems were reviewed;
- why Continuity changed;
- what alternatives existed;
- what the civilisation learned.

---

# 6. New Interface Requirement — Historical Event Spine

The cross-domain test exposes a useful concept not yet explicit enough in v0.2.

Historical needs a way to connect consequential state transitions across domain boundaries without becoming a universal workflow engine.

Candidate:

## Historical Event Spine

A lightweight temporal/provenance relation linking:

```text
Source Event
→ Domain Transition
→ Knowledge Change
→ Dependency Effect
→ Authority/Decision
→ Operational Outcome
→ Later Correction
```

The Event Spine does not execute the process.

It makes the process historically reconstructable.

This may be implemented through KCS relationships rather than a separate database.

The requirement is semantic, not technological.

---

# 7. New Interface Requirement — Operational/Historical State Pair

For objects that continue to exist operationally after entering Historical custody, the architecture should support:

```text
Operational Current State
↔
Historical State Sequence
```

Historical should reference current authoritative state where appropriate rather than independently declaring it.

This is especially important for:

- judicial status;
- governance authority;
- KCS epistemic state;
- Civil Attention issue state;
- continuity/recovery state.

---

# 8. New Interface Requirement — Handoff Does Not Mean Ownership Transfer

The phrase "Historical handoff" can imply that the source system relinquishes ownership.

That is not always correct.

Three patterns exist:

### A. Transfer

Operational source ceases custody and Historical becomes primary custodian.

### B. Dual Custody

Operational source remains active while Historical preserves qualified historical states.

### C. Reference Preservation

Historical preserves provenance/relationships while authoritative content remains under another legitimate custodian.

Therefore:

> **Historical Handoff ≠ Mandatory Ownership Transfer.**

This should be explicit in the next revision.

---

# 9. Interface Conflicts Identified

No major architectural contradiction was found.

Four areas require future resolution.

## IC-1 — Permanent Provenance Language

Continuity/KCS language may need clarification against Historical's protected/anonymous provenance architecture.

## IC-2 — Library / Historical Boundary

Continuity's description of Library as constitutional memory predates the formal Historical domain. The functional separation should eventually be normalised across both systems.

## IC-3 — Historical Event Spine Implementation

Need to determine whether KCS's typed relationship graph already fully supplies the mechanism or whether Historical requires a temporal projection/interface companion.

Do not create a duplicate graph before this is tested.

## IC-4 — Handoff Semantics

Source domains need a shared vocabulary for transfer, dual custody and reference preservation.

---

# 10. ESCP Finding

Cross-domain operation expands the evaluation-space problem.

A historical reconstruction can fail even when every individual domain preserved its own records correctly if the **relationships between domain transitions** are lost.

Therefore:

> **Domain-Level Completeness ≠ Cross-Domain Historical Completeness.**

This is a significant new distinction.

The historical value can exist in the chain between systems rather than inside any one system.

---

# 11. Test Result

**Civil Attention ↔ Historical:** PASS  
**KCS ↔ Historical:** PASS WITH TEMPORAL SOURCE-OF-TRUTH CLARIFICATION  
**Continuity ↔ Historical:** PASS WITH PROVENANCE/LIBRARY CLARIFICATION  
**Three-System Chain:** PASS IF CROSS-DOMAIN RELATIONSHIPS ARE PRESERVED

No major Historical function needs replacement.

The test instead strengthens the need for relational architecture.

---

# 12. Required Refinements

The next Historical revision or interface companion should incorporate:

1. **Historical Handoff ≠ Ownership Transfer.**
2. Transfer / Dual Custody / Reference Preservation modes.
3. Operational-current-state ↔ historical-state-sequence relation.
4. Explicit prohibition on Historical maintaining competing current truth where another domain is authoritative.
5. Cross-domain Historical Event Spine requirement.
6. **Domain-Level Completeness ≠ Cross-Domain Historical Completeness.**
7. Protected provenance compatibility with Continuity/KCS.
8. Functional separation of Library, Historical and Continuity.
9. Preservation of Civil Attention parent-Issue versus Domain-Action resolution distinction.
10. Preservation of KCS REVIEW_REQUIRED as review state, not invalidity.

---

## Status

**Cross-Domain Interfaces Tested:** 3 primary systems + combined chain  
**Major Authority Collision:** None  
**Major Duplication Risk:** KCS live dependency graph if Historical creates a competing current graph  
**New Major Insight:** historical information can exist specifically in transitions between Concord domains  
**Result:** PASS WITH INTERFACE REFINEMENT  
**Next:** Resolve the Event Spine against KCS capabilities and test the Historical boundary against Judiciary/Governance authority state.
