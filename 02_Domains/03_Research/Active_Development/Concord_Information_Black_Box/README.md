# Concord Information Black Box — Active Development Record

## Status
- Architectural discovery: **CLOSED**
- Abstraction floor: **STABLE within CRADP Blind Test 003 scope**
- Broad CRADP architectural testing: **COMPLETE**
- Formalisation: **ACTIVE**
- PMEDG extraction testing: **NEXT**
- Portable-module graduation: **NOT YET**

## Purpose
The Concord Information Black Box (CIBB) is the architecture for governed information containment, contextual projection, modification, transformation, protected movement, structural/control change, lifecycle governance, recovery, disclosure-risk coordination and exceptional access.

CIBB developed from the requirement that protected master information should remain inside a governed boundary and that users/systems ordinarily receive only the information operation they are legitimately authorised to perform.

## Current core topology
1. **Information Plane** — Projection, Patch, Controlled Derivation, Protected Transfer.
2. **Structural / Control Plane** — Structure Modify, Control Modify.
3. **Lifecycle Plane** — Create, Activate, Supersede, Retire, Retain, Archive, Destroy.
4. **Exceptional System Plane** — Direct Master Access.

Authority does not automatically cross planes.

## Core general rule
**Authorised(A) + Authorised(B) does not automatically imply Authorised(A composed with B).**

This Non-Compositional Authority principle applies to information, structure, controls, lifecycle, workflows, disclosure, recovery and multi-party operations. Legitimate bounded workflows and explicitly constituted multi-party authority remain permitted.

## Validation history
### CRADP CIBB 001
Found incomplete lifecycle representation, cumulative-disclosure gaps, authority-dependency underspecification, provenance-integrity gaps, anomaly-observation feedback risk and authority-succession/interface issues.

### Specification 002
Separated Information Operations from Governed Lifecycle Operations; added cumulative disclosure, Authority Dependency Policy, provenance integrity, observation independence and authority succession.

### CRADP CIBB 002
Found no architectural failure. Identified missing Structural/Control operation plane, cross-session/domain disclosure coordination, general compositional authority, plus smaller recovery/emergency/re-identification clarifications.

### Specification 003
Added Structural/Control Plane, Non-Compositional Authority, Bounded Disclosure State, Restore as composite workflow, emergency sunset and derivative re-identification review.

### CRADP CIBB 003
Clean evaluator found:
- no missing operation plane;
- no missing primitive;
- no reducible plane;
- legitimate multi-plane workflows remain representable;
- no new unresolved CIBB abstraction layer;
- stable abstraction floor demonstrated within frozen test scope;
- no further broad Active Development cycle required.

Remaining work was formalisation-level: composition triggers, residual disclosure risk, grant-authority boundaries and recovery activation barrier.

## Development discipline from this point
Conceptual expansion alone is no longer sufficient to reopen the architectural core.

A proposed architectural change should demonstrate at least one of:
- contradiction;
- failed formalisation;
- failed PMEDG extraction;
- implementation impossibility;
- new empirical evidence;
- failed targeted validation;
- external-interface incompatibility.

## PMEDG
CIBB remains a PMEDG candidate. Extraction/graduation must not be treated as complete merely because the internal Concord architecture is mature.

A separate candidate has also emerged: **Non-Compositional Authority**. It should be flagged for later PMEDG consideration but not extracted prematurely.
