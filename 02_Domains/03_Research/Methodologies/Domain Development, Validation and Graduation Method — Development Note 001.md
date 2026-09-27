# Domain Development, Validation and Graduation Method — Development Note 001

**Project:** The Concord Framework  
**Classification:** Concordian Methodology / Domain Development  
**Status:** ACTIVE DEVELOPMENT / METHOD EXTRACTED FROM HISTORICAL DOMAIN CYCLE  
**Canonical Status:** NOT CANONICAL  
**Date:** 25 September 2026

---

# 1. Purpose

The development of the Historical domain produced a repeatable pattern for taking a Concord domain from an initially uncertain body of material to a bounded, tested and implementation-ready architecture.

This note records that method so the process does not have to be rediscovered independently for each domain.

The method is not a rigid sequence. Steps may recurse when testing exposes missing sources, boundary errors or conceptual failures.

The broad pattern is:

**SOURCE RESOLUTION**

→ **SYNTHESIS**

→ **FORMAL SPECIFICATION**

→ **ADVERSARIAL TESTING**

→ **CROSS-DOMAIN INTERFACE TESTING**

→ **SCHEMA / OBJECT EXTRACTION**

→ **SCHEMA ADVERSARIAL TESTING**

→ **CROSS-OBJECT CONSISTENCY AUDIT**

→ **END-TO-END CONFORMANCE**

→ **GRADUATION REVIEW**

→ **REPOSITORY SEPARATION**

→ **IMPLEMENTATION / CONTROLLED REOPENING**

---

# 2. Stage 1 — Source Resolution

Before designing a domain, inspect the existing Concord corpus for relevant architecture, principles, records, interfaces, unresolved questions and historical decisions.

The objective is not merely to collect facts.

Preserve:

- source provenance;
- relationships;
- contradictions;
- existing boundaries;
- terminology;
- partially developed mechanisms;
- negative results;
- unresolved questions;
- cross-domain dependencies;
- implicit architecture;
- development history.

Continue until additional source passes produce diminishing architectural returns.

This is **source saturation**, not proof that every possible source has been read.

> **Source Saturation ≠ Source Completeness.**

---

# 3. Stage 2 — Synthesis

Source resolutions should be consolidated into one or more synthesis documents.

A synthesis should identify:

- domain purpose;
- candidate functions;
- information or object classes;
- major relationships;
- authority boundaries;
- epistemic constraints;
- privacy/safety constraints;
- lifecycle;
- neighbouring domains;
- open contradictions;
- unresolved questions.

Where ESCP applies, explicitly record the limits of the evaluated source space.

The synthesis is the bridge between corpus reading and architecture.

---

# 4. Stage 3 — Formal Domain Specification

Create an initial formal specification.

It should attempt to state:

- purpose;
- governing principles;
- functions;
- scope;
- boundaries;
- invariants;
- lifecycle;
- interfaces;
- authority relationships;
- epistemic status;
- failure modes;
- unresolved questions.

Version the specification.

Do not overwrite earlier versions merely because later versions are better.

Earlier specifications are development evidence.

---

# 5. Stage 4 — Adversarial Boundary Testing

Attempt to break the domain conceptually.

Construct cases designed to expose:

- authority leakage;
- boundary confusion;
- false completeness;
- privacy failure;
- state loss;
- provenance loss;
- contradictory requirements;
- silent reinterpretation;
- current/historical confusion;
- operational/historical confusion;
- centralisation creep;
- accidental surveillance;
- failure under unusual participants or contexts.

Classify results rather than forcing a pass.

Useful categories include:

- PASS;
- PASS WITH REFINEMENT;
- SCHEMA/ARCHITECTURE REFINEMENT REQUIRED;
- EXTERNAL RESOLUTION REQUIRED;
- FUNDAMENTAL FAILURE.

Feed legitimate refinements back into a new specification version.

---

# 6. Stage 5 — Cross-Domain Interface Testing

A domain can be internally coherent and still fail where it touches the rest of the Concord.

Test important neighbouring systems directly.

Ask:

- who owns the live state?
- who owns historical state?
- who has authority?
- who merely preserves evidence?
- what passes across the interface?
- what must not pass?
- can one domain accidentally inherit another's authority?
- can duplicated representations drift?
- what happens when the domains disagree?
- what happens when one domain is unavailable?

Interface tests should use actual neighbouring-domain architecture where available rather than reconstructed assumptions.

---

# 7. Stage 6 — Formal Schema / Object Extraction

Once conceptual architecture is stable enough, extract it into implementation-neutral objects and interfaces.

Do not choose a database first and then force the architecture into it.

Schema extraction should reveal whether apparently simple concepts actually require:

- state transitions;
- typed relationships;
- contextual assertions;
- authority envelopes;
- provenance;
- versioning;
- uncertainty;
- search boundaries;
- correction relationships;
- dependency state.

The schema should remain substrate-neutral until implementation requirements justify otherwise.

---

# 8. Stage 7 — Schema Adversarial Testing

Attempt to make the formal objects silently misrepresent reality.

Useful failure cases include:

- simultaneous legitimate states;
- repeated state changes;
- later correction;
- missing replicas;
- derivative survival;
- taxonomy change;
- retrospective evidence;
- authority renewal;
- inaccessible domains;
- cross-jurisdiction conflict;
- re-identification through relationships;
- missed reviews;
- incomplete dependency knowledge.

A schema failure is particularly important when the conceptual architecture is correct but the representation would silently collapse it.

---

# 9. Stage 8 — Cross-Object Consistency Audit

Once new objects have accumulated, test them against one another.

The goal is not zero overlap.

The goal is to prevent competing sources of semantic truth.

For each overlapping pair ask:

- which object owns the concept?
- which object merely summarises it?
- which records state?
- which records permission?
- which records execution?
- which records evidence?
- which records interpretation?
- what happens if the objects disagree?

A useful rule from Historical is:

> **One concept may have multiple representations, but only one representation should be authoritative for its meaning within a given context.**

Also:

> **Recorded State ≠ Permission to Act on That State.**

---

# 10. Stage 9 — End-to-End Conformance Test

Do not graduate a domain solely because its components work independently.

Construct at least one realistic consequential scenario that traverses the architecture from beginning to end.

Exercise as many relevant elements as possible:

- creation;
- routing;
- authority;
- data/state changes;
- neighbouring domains;
- correction;
- failure;
- privacy;
- review;
- output;
- later reuse.

Ask whether the entire chain can be represented without:

- erasing earlier states;
- inventing authority;
- losing provenance;
- silently changing epistemic status;
- creating contradictory live sources;
- bypassing privacy or rights;
- depending on undefined transitions.

This is the system-level equivalent of component testing.

---

# 11. Stage 10 — Development Graduation Review

Graduation is a change in development mode.

It does not mean complete, perfect or immutable.

A domain is a candidate for graduation when:

- source saturation has been reached;
- purpose is stable;
- functions are stable;
- boundaries are stable;
- major interfaces have been tested;
- adversarial tests reveal refinements rather than recurring conceptual collapse;
- schemas can represent the architecture;
- cross-object consistency is manageable;
- an end-to-end case passes;
- remaining questions are predominantly implementation choices, external decisions or genuinely future cases.

Recommended state:

> **CANDIDATE GRADUATED DOMAIN — ARCHITECTURE STABLE / IMPLEMENTATION OPEN**

Graduation means open-ended conceptual expansion stops by default.

---

# 12. Stage 11 — Repository Separation

After graduation, reorganise the domain so a future participant sees the usable system first rather than the entire development process.

Recommended structure:

**Domain/**

- README / implementation handoff
- current formal specification
- current schema/object specification
- essential conceptual orientation documents
- other current operating architecture

**Domain/Development/**

- source resolutions
- syntheses
- superseded specifications
- superseded schemas
- adversarial tests
- interface tests
- consistency audits
- conformance tests
- graduation review
- other development provenance

This is not archival deletion.

The development record remains part of Concord history.

The separation serves two purposes:

1. the current system becomes legible;
2. the reasoning trail remains recoverable.

> **Separate Development Provenance From Current Architecture; Preserve Both.**

---

# 13. README / Implementation Handoff

A graduated domain should have a front-door README that tells a new AI instance, human contributor or implementer:

- what the domain is;
- what it is not;
- its governing principles;
- current baseline;
- key interfaces;
- major invariants;
- implementation work still open;
- decisions the domain does not own;
- recommended reading order;
- change-control triggers;
- where development provenance lives.

A future instance should not have to repeat source resolution merely to discover the current architecture.

---

# 14. Post-Graduation Change Control

Graduation should close speculative expansion, not correction.

Reopen architecture when evidence warrants it.

Candidate triggers include:

1. implementation cannot preserve an invariant;
2. a real or synthetic case produces silent state loss;
3. a cross-domain interface becomes contradictory;
4. constitutional architecture changes;
5. a new substrate exposes an unsupported assumption;
6. migration loses material relationships;
7. adversarial testing finds a new failure;
8. a new ESCP problem exposes a missing dimension;
9. a safety, privacy or authority failure arises;
10. another Concord module changes the dependency topology.

Changes should be proportional to the demonstrated failure.

Create a new version rather than silently rewriting the historical baseline.

---

# 15. Recursive Nature of the Method

The method is not a waterfall.

A schema test may reveal a missing conceptual distinction.

An interface test may require new source resolution.

An end-to-end test may expose a boundary failure.

The appropriate response is to return to the earliest affected layer, correct it, and propagate the correction forward.

Conceptually:

**DEVELOP**

→ **TEST**

→ **LOCATE FIRST FAILED ASSUMPTION**

→ **RETURN TO THAT LAYER**

→ **CORRECT**

→ **PROPAGATE FORWARD**

→ **RETEST.**

This aligns naturally with Concord's broader recursive development practices and back-propagation methods.

---

# 16. Development Provenance Is Part of the Result

Failed models, earlier specifications, rejected assumptions and test cases are not disposable clutter.

They show:

- what was considered;
- what failed;
- why architecture changed;
- what evidence existed;
- what evaluation space was available;
- what future developers should not unknowingly repeat.

The graduated system and the development trail therefore serve different functions.

> **Current Architecture Tells Us What the System Is.**

> **Development Provenance Tells Us How and Why It Became That System.**

Both matter.

---

# 17. Relationship to PMEDG

This method is related to, but distinct from, Portable Module Extraction, Development and Graduation (PMEDG).

PMEDG concerns extraction and maturation of portable modules.

This method concerns development and graduation of a **domain architecture** embedded in the Concord.

They should share compatible principles where useful:

- explicit development state;
- adversarial testing;
- portability/boundary awareness;
- preserved provenance;
- graduation criteria;
- controlled reopening.

They should not be collapsed merely because both use the term graduation.

---

# 18. Relationship to Existing Concordian Methods

Domain development can compose:

- Blaineyan Reasoning;
- Reality Trees;
- Outlier-First Design;
- ESCP;
- Bounded Contextual Authority;
- Contextual Wrapper Architecture;
- State and Maturity Mapping;
- Back-Propagation Method;
- empirical validation methods.

This development method is primarily an orchestration method: it describes how these and other tools can be applied across the lifecycle of a domain.

---

# 19. Historical as First Worked Example

Historical is the first domain in this development cycle to complete the full pattern:

**broad source resolution**

→ **source saturation**

→ **synthesis**

→ **formal specifications**

→ **adversarial boundary testing**

→ **cross-domain interface testing**

→ **formal schemas**

→ **schema adversarial testing**

→ **cross-object consistency**

→ **end-to-end conformance**

→ **graduation review**

→ **root/development repository separation**

→ **implementation handoff.**

Historical should therefore be retained as a worked example when applying this method to another domain.

The method should be revised if another domain exposes steps that Historical did not require.

---

# 20. Method Status

**Method extracted:** YES

**First complete worked example:** Historical Domain

**Cross-domain validation:** NOT YET COMPLETE

**Candidate status:** STRONG DEVELOPMENT METHOD / NOT YET CANONICAL

**Next validation:** Apply to another sufficiently developed Concord domain and record where the process requires modification.

---

# Conclusion

A Concord domain should not become "finished" merely because enough documents have accumulated.

It should become progressively more explicit, bounded and testable until its architecture can survive attempts to break it and can carry a consequential case from beginning to end.

Only then should development shift from open exploration to controlled change.

The resulting repository should make that distinction visible:

> **the current architecture at the front; the complete development history behind it.**
