# Participation-Bounded Knowledge Exposure — Existing Architecture Source Resolution 001

**Status:** ACTIVE DEVELOPMENT / SOURCE RESOLUTION / NOT CANONICAL
**Date:** 30 September 2026

## Problem

Domain/system organisation answers where knowledge belongs. It does not answer who should be exposed to which operational information, at what depth, for what legitimate function and under what contextual constraints.

A civil architecture should not depend on every evaluator voluntarily ignoring information unnecessarily exposed to them.

> **Available To Read != Legitimately Necessary To Expose**

> **Repository Location != Exposure Permission**

## Existing architecture

### Minimum Necessary Capability

`04_Portable_Modules/Minimum Necessary Capability — Portable Module.md`

MNC explicitly includes **information access** among capability dimensions and provides:

**Purpose -> Function -> Need -> Minimum Sufficient Capability -> Bounded Exercise -> Review -> Termination or Re-Justification**

Information access can therefore be bounded like other consequential capability.

### Contextual Wrapper Architecture

`04_Portable_Modules/Contextual Wrapper Architecture — Portable Module.md`

CWA explicitly supports digital, informational, relational, functional, temporal, conceptual and hybrid bounded contexts.

It establishes:

> **Boundary != Access != Rules != Authority**

### Knowledge Control System

`04_Portable_Modules/Knowledge Control System — Portable Module.md`

KCS independently represents **access/visibility state**, including OPEN, CONTROLLED, RESTRICTED, SEALED, REDACTED and policy-unavailable states.

It establishes:

> **Restricted != Rejected**

The primitives for bounded knowledge exposure therefore already exist.

## Source-resolution result

The primary gap is integration:

> **Participation / Role / Legitimate Function -> Information Exposure**

Classification:

**PRIMARY: CROSS-ARCHITECTURE INTEGRATION GAP**

**SECONDARY: REPOSITORY / CIVIL INTERFACE DESIGN GAP**

Do not invent a new foundational principle where MNC, CWA and KCS already supply the components.

## Two independent axes

### Axis A — Functional/domain location

Answers:

> **Where does this material belong in the civilisation?**

### Axis B — Exposure/participation context

Answers:

> **Who needs which representation of this material to perform a legitimate function?**

These axes are orthogonal.

> **Domain Classification != Exposure Classification**

> **One Knowledge Object May Have Several Legitimate Exposure Surfaces**

## Participation level is important but not sufficient

Exposure may depend upon:

**Exposure Context = <Participation, Role, Function, Need, Subject, Context, Time, Risk, Authority>**

A higher general participation level should not automatically expose private medical data. A specialist role may require information unavailable to a generally higher-participation participant. Emergency exposure may be temporary. A participant may require access to their own records without unrelated institutional authority.

Therefore:

> **Higher Participation != Universal Information Access**

> **Role != Universal Clearance**

> **Need To Know != Authority To Act**

> **Information Access != Operational Permission**

Participation should be one axis, not a universal scalar clearance.

## Layered representation

Candidate representation layers:

- **L0 Public orientation** — purpose, principles, broad structure, rights, routes and public accountability.
- **L1 Participant-use guidance** — information needed to access services, understand obligations, exercise rights and challenge decisions.
- **L2 Function/role guidance** — operational information needed for an accepted/assigned function.
- **L3 Specialist operational material** — detailed procedures, implementation constraints and sensitive dependencies.
- **L4 Restricted/security-sensitive material** — information whose unnecessary exposure could materially increase risk or expose protected participants.

These are provisional representation layers, not universal participation ranks.

## Symmetric failure

### Overexposure

**Everything Visible -> Information Becomes Capability -> Unnecessary Capability -> Increased Risk**

### Underexposure

**Necessary Information Hidden -> Participant Cannot Understand Rights / Duties / Risks / Decisions -> Dependency On Gatekeeper -> Reduced Agency**

The target is:

> **Minimum Sufficient Exposure**

Candidate formulation:

> **A participant should receive sufficient information to understand and perform the legitimate function, exercise relevant rights, protect legitimate interests, evaluate consequential claims and challenge the system where necessary, while information whose additional exposure would create unjustified risk remains bounded to contexts in which that exposure is legitimately required.**

## Transparency constraint

Bounded exposure must not become a mechanism for hiding the existence of powers, applicable rights, decision criteria affecting the participant, remedies, accountability structures, conflicts of interest, evidence necessary to challenge consequential decisions, or the fact that restricted material exists where that fact is legitimately relevant.

> **Bounded Information != Unaccountable Secrecy**

> **Transparency Of Power != Exposure Of Every Operational Detail**

## Relationship to Lobby

The Lobby should not become a clearance checkpoint.

Use:

**Lobby -> Self-Selected Need -> Route Board -> Exposure Resolution -> Appropriate Representation -> Deeper Architecture**

not:

**Lobby -> Identity Classification -> Clearance -> Navigation**

This preserves:

> **Need To Navigate != Duty To Disclose Identity**

## Consequence for planned test

The proposed Lobby-to-Architecture test assumed the visitor could be handed deeper destination documents and then tested for disciplined interpretation.

That assumption is now under question.

The test must instead distinguish:

1. what information should be exposed at this participation/context level;
2. whether the exposed representation is sufficient for the legitimate next decision;
3. whether deeper material requires another bounded transition.

Where no bounded representation exists, record that as an architectural/interface deficit rather than exposing the full internal source merely to continue the test.

## Candidate integrated process

**Need / Route**
-> **Legitimate Information Function**
-> **Participant / Role / Context**
-> **Minimum Sufficient Exposure**
-> **Appropriate Representation**
-> **Use Boundary**
-> **Further Access Request if Needed**
-> **Review / Expiry / Return**

Provisional name:

**Minimum Sufficient Knowledge Exposure (MSKE)**

Do not extract this as a portable module yet.

## Candidate invariants

> **Domain Classification != Exposure Classification**

> **Available To Read != Legitimately Necessary To Expose**

> **Information Access != Operational Permission**

> **Need To Know != Authority To Act**

> **Higher Participation != Universal Information Access**

> **Bounded Information != Unaccountable Secrecy**

> **One Knowledge Object May Have Several Legitimate Exposure Surfaces**

> **Minimum Sufficient Exposure != Maximum Secrecy**

> **Transparency Of Power != Exposure Of Every Operational Detail**

> **Need To Navigate != Duty To Disclose Identity**

## Development disposition

Do not proceed directly to the previously planned unrestricted Lobby-to-Architecture blind test.

First source-resolve:

1. existing participation-level architecture;
2. KCS access/visibility states;
3. CWA informational/context boundaries;
4. MNC information-access constraints;
5. existing participant-facing information layers.

Develop only the missing integration demonstrated by source resolution.

Then redesign the route-to-architecture test around **appropriate exposure**, not unrestricted source access.

Flag the integrated architecture as a later PMEDG candidate if it stabilises. Do not extract it yet.
