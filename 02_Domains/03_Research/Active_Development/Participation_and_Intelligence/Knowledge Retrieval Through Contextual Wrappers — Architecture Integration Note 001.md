# Knowledge Retrieval Through Contextual Wrappers — Architecture Integration Note 001

**Project:** The Concord  
**Status:** ACTIVE DEVELOPMENT / ARCHITECTURE INTEGRATION / NOT CANONICAL  
**Date:** 30 September 2026  
**Parent work:** Participation-Bounded Knowledge Exposure / Concord Access Envelope and Bounded Retrieval Architecture  
**Primary existing architecture:** Contextual Wrapper Architecture (CWA)

---

## 1. Integration finding

The proposed participation-bounded retrieval architecture is a clear application of the existing **Contextual Wrapper Architecture**.

It should therefore not be developed as an unrelated access-control primitive.

The key move is:

> **Apply contextual wrappers to semantic regions of authoritative Concord knowledge objects.**

This allows a single architectural document to contain material with different legitimate exposure conditions without creating duplicated participant-specific copies.

The preferred architecture is:

**Authoritative Knowledge Object**  
-> **Semantic Sections / Knowledge Regions**  
-> **Contextual Wrappers**  
-> **Retrieval Context Resolution**  
-> **Permitted Retrieval View**

Therefore:

> **Wrapper Around Knowledge != Copy Of Knowledge**

---

## 2. Why file-level classification is insufficient

A single Concord file may contain several kinds of material.

For example, a Governance document may contain:

- public principles;
- participant rights;
- ordinary procedures;
- role-specific instructions;
- specialist implementation detail;
- protected personal information;
- security-sensitive operational information;
- emergency mechanisms.

Assigning one access classification to the entire file would create two likely errors.

### Overexposure

If the file is classified according to its least restricted material, sensitive sections become unnecessarily available.

### Underexposure

If the file is classified according to its most restricted material, legitimate public or participant information becomes unnecessarily hidden.

Therefore:

> **Document Classification != Necessarily Section Classification**

and:

> **File Boundary != Necessary Access Boundary**

The access boundary should be capable of existing inside the file.

---

## 3. Semantic section as bounded informational context

CWA already defines bounded contexts as potentially:

- informational;
- digital;
- functional;
- relational;
- temporal;
- conceptual;
- hybrid.

A semantic section of a Concord knowledge object can therefore be treated as an **informational bounded context**.

The wrapper around that section may define, where relevant:

- reachability;
- access;
- participant state;
- role;
- legitimate function;
- subject relationship;
- applicable rules;
- permissions;
- restrictions;
- privacy;
- security;
- authority dependencies;
- activation conditions;
- duration;
- emergency variation;
- review;
- exit/termination;
- reversion;
- inheritance.

The underlying knowledge remains in its original authoritative location.

---

## 4. Wrapper hierarchy

Wrappers should be capable of nesting.

A possible structure is:

**Repository / Domain Wrapper**  
-> **Document Wrapper**  
-> **Section Wrapper**  
-> **Subsection / Knowledge-Object Wrapper**

The higher wrapper may establish defaults.

A lower wrapper may introduce a legitimate contextual variation.

Example:

**Governance document default:** OPEN / PARTICIPANT ACCESSIBLE

Section 7:
**ROLE-CONTROLLED**

Section 7.4:
**SPECIALIST + FUNCTION REQUIRED**

Section 7.4.3:
**RESTRICTED / SECURITY CONTEXT**

Section 8:
returns to document default.

This avoids duplicating the source merely to express access differences.

---

## 5. Inheritance

Wrapper inheritance must be explicit enough that absence of a local wrapper does not create ambiguity.

Candidate rule:

> **A semantic region inherits the applicable parent wrapper unless a valid child wrapper explicitly modifies that context.**

However, a child wrapper must not silently manufacture authority or access inconsistent with the wider architecture.

Therefore:

> **Inherited Context != Independent Authority**

and:

> **Child Wrapper Variation Requires Legitimate Basis**

Precedence, overlap and conflict should use existing CWA architecture wherever possible rather than inventing a separate knowledge-specific hierarchy.

Where CWA leaves precedence unresolved, preserve UNKNOWN / DISPUTED / REQUIRES EXTERNAL RESOLUTION rather than inventing certainty.

---

## 6. Wrapper metadata should point to content

The wrapper should normally store **metadata and references**, not copied source prose.

Conceptually:

```
Knowledge Object: GOV-001
Source: Governance V2 Canonical.md
Default Wrapper: W-GOV-001

Semantic Region: GOV-001:S7
Wrapper: W-GOV-001-S7

Semantic Region: GOV-001:S7.4
Wrapper: W-GOV-001-S7.4
```

The exact identifier format is not yet fixed.

The important invariant is:

> **Access Metadata References Source Content; It Does Not Become A Second Source Of That Content**

---

## 7. Composition with existing Concord architecture

The retrieval system should be an integration of existing components.

### KCS — knowledge state and provenance

KCS stores or represents:

- authoritative knowledge objects;
- provenance;
- epistemic state;
- historical/version state;
- retrieval/activity state;
- access/visibility state;
- capability-operational state where relevant.

### CWA — contextual boundary

CWA defines:

- where the informational boundary exists;
- what context activates;
- who/what can reach it;
- applicable access conditions;
- restrictions;
- inheritance;
- termination;
- review.

### MNC — justified information capability

MNC asks:

> **What information exposure is minimally sufficient for the legitimate function?**

It prevents access from expanding merely because broader information would be convenient.

### Participation / role architecture — participant context

This supplies relevant represented state such as:

- participation level;
- role;
- qualification;
- responsibility;
- relationship;
- delegation;
- contextual status.

### BCA — bounded authority

Where retrieval depends on an authority relationship, BCA constrains that authority to the legitimate function and context.

### Retrieval system — execution

The retrieval mechanism resolves these inputs and returns only the semantic regions reachable in the current legitimate context.

Thus:

**KCS + CWA + MNC + Participation/Role + BCA -> Bounded Knowledge Retrieval**

---

## 8. Retrieval example

Suppose an evaluator is currently represented as **Participation Level X**.

The evaluator asks for information about a Governance process.

The system should not simply provide the Governance file.

Instead:

1. identify the authoritative Governance knowledge object;
2. identify the evaluator's represented participation/context state;
3. identify the legitimate information function created by the request;
4. resolve the applicable document/section wrappers;
5. apply MNC to determine sufficient information exposure;
6. retrieve only the reachable semantic regions;
7. preserve source provenance and status;
8. state where the returned view is bounded where legitimately possible;
9. provide a route for further justified access or challenge;
10. terminate or re-evaluate access when the context changes.

Conceptually:

**Evaluator Level X + Function Y + Context Z**  
-> **Resolve CWA wrappers**  
-> **Determine permitted semantic regions**  
-> **Fetch those regions from authoritative source**  
-> **Return bounded view**

---

## 9. Permission should not depend on evaluator restraint

The architecture should not use:

**Expose Full Source -> Tell Evaluator Which Parts It May Use**

where the information itself is consequential.

Prefer:

**Resolve Access -> Retrieve Permitted Material -> Expose Only Permitted Material**

Therefore:

> **Instruction Not To Use Information != Information Access Control**

and:

> **Behavioural Restraint != Architectural Boundary**

This applies to humans, AI systems, institutions and automated processes.

---

## 10. Public transparency remains a wrapper requirement

A restricted operational section may still require a public-facing wrapper representation explaining:

- that the relevant power or process exists;
- its purpose;
- legitimate basis;
- scope;
- accountability;
- review;
- consequences;
- challenge route.

This does not require copying the restricted operational content.

It may instead expose a different semantic region or generated bounded representation linked to the same architecture.

Therefore:

> **Operational Restriction != Hidden Existence Of Power**

and:

> **Wrapper Restriction Must Preserve Legitimate Accountability Information**

---

## 11. Retrieval views are transient products

A bounded retrieval view is not a new canonical document.

It is a contextual result produced from the authoritative corpus.

Therefore:

> **Retrieved View != New Source**

> **Retrieved View != Independent Canonical Copy**

> **Retrieved View Validity Depends On Source + Wrapper + Context + Time**

A later retrieval may legitimately differ because:

- source changed;
- wrapper changed;
- participant state changed;
- role changed;
- function changed;
- context changed;
- time changed;
- authority changed.

This is expected behaviour rather than version inconsistency.

---

## 12. Source-change problem

Because wrappers reference semantic regions, source modification can invalidate wrapper assumptions.

Required future chain:

**Source Change**  
-> **Affected Semantic Region Detection**  
-> **Wrapper Impact Check**  
-> **Revalidation**  
-> **Updated Retrieval State**

KCS change propagation should be source-resolved for this function.

The system must prevent a previously public wrapper from accidentally exposing newly inserted restricted content merely because it was added beneath the same heading.

---

## 13. Stable semantic addressing

Section-level wrappers create a likely requirement for identifiers more stable than presentation position alone.

Headings and line numbers can change.

The next development instance should investigate whether the living corpus needs stable knowledge-region identifiers.

Possible model:

**Knowledge Object ID / Semantic Region ID**

rather than:

**Filename / line range only**

This remains an implementation question.

Do not refactor the corpus merely to introduce identifiers before the retrieval architecture is sufficiently resolved.

---

## 14. Relationship to the provisional Access Envelope concept

The phrase **Access Envelope** remains useful as an interface description, but it should not imply a separate foundational architecture.

Source resolution now suggests:

> **Access Envelope = Knowledge-Retrieval Profile / Implementation Of Contextual Wrapper Architecture**

The envelope is the wrapper metadata and retrieval conditions associated with a knowledge object or semantic region.

This avoids architectural duplication.

---

## 15. Revised next-step architecture

The major development programme should now be understood as:

### A. Source-resolve participation and access context
Determine the civil states used as wrapper inputs.

### B. Define knowledge-wrapper profile
Specify how CWA applies to documents, sections and semantic knowledge regions.

### C. Define inheritance and precedence
Determine how document defaults and narrower section wrappers interact.

### D. Define semantic addressing
Determine how wrappers reference authoritative content without copying it.

### E. Map the living corpus
Classify relevant semantic regions and attach appropriate wrapper metadata.

### F. Build retrieval resolution
Given participant/context/function, determine which regions are reachable.

### G. Preserve provenance and boundedness
Returned material must retain source/status information and not masquerade as the complete source.

### H. Integrate change propagation
Source changes must trigger wrapper review where exposure assumptions may have changed.

### I. Adversarially test
Test overexposure, underexposure, wrapper conflict, stale wrappers, inference leakage, privilege accumulation, emergency persistence and cross-document reconstruction.

### J. Resume Lobby-to-Architecture testing
Only then test whether Lobby routes produce the correct bounded retrieval view.

---

## 16. Core invariants

> **Wrapper Around Knowledge != Copy Of Knowledge**

> **One Authoritative Source -> Multiple Contextual Retrieval Views**

> **Document Classification != Necessarily Section Classification**

> **File Boundary != Necessary Access Boundary**

> **Semantic Region Can Be A Bounded Informational Context**

> **Access Metadata References Source Content; It Does Not Become A Second Source**

> **Instruction Not To Use Information != Information Access Control**

> **Behavioural Restraint != Architectural Boundary**

> **Retrieved View != New Source**

> **Inherited Context != Independent Authority**

> **Child Wrapper Variation Requires Legitimate Basis**

> **Operational Restriction != Hidden Existence Of Power**

> **Wrapper Restriction Must Preserve Legitimate Accountability Information**

---

## 17. Development disposition

This integration substantially narrows the problem.

The next instance should **not invent a new access-control system from first principles**.

It should begin with the hypothesis:

> **Participation-bounded Concord knowledge retrieval is a specialised implementation of Contextual Wrapper Architecture over KCS-managed knowledge objects, with MNC bounding information exposure and participation/role/BCA supplying legitimate context.**

The job is to test, refine and operationalise that integration against the living Concord corpus.

If the architecture stabilises, it may later be flagged as a PMEDG candidate.

Do not extract it yet.
