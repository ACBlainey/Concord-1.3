# CA-04 — Purpose-Limited Participant Information Architecture

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.1  
**Document Type:** Candidate Architecture  
**Status:** CANDIDATE ARCHITECTURE — UNDER CRITICAL EXAMINATION / NOT CANONICAL  
**Date:** September 2026  
**Validation:** Architecture extraction, consolidation, dependency and adversarial failure audits completed; empirical validation not established.

---


## 1. Architecture Statement

> **Participant information should move through civilisation according to sufficiently defined legitimate purpose, minimum necessary identity, scope and duration, with material changes of purpose treated as explicit transitions rather than silent consequences of data availability.**

## 2. Origin and Provenance

This architecture is centred on:

- Intermediary Personal-Data Boundary.

It interfaces with:

- Citizen Data Ownership, Access and Contestability;
- Participant Digital Twins;
- Case Learning;
- automatic Metrics extraction;
- Support-to-Investigation Firewall;
- Exceptional Identifiable Access.

The architecture was renamed from “Personal Information” to “Participant Information” to improve substrate neutrality.

## 3. Civilisational Problem Addressed

Modern civil systems can accumulate data faster than legitimate purpose boundaries develop.

Information gathered for:

- support;
- health;
- employment;
- identity;
- safety

may silently become available for unrelated purposes.

The architecture seeks to prevent technical availability from becoming civil entitlement.

## 4. Intended Scope

Applies to:

- identifiable participant information;
- pseudonymous information;
- Digital Twins;
- health data;
- support data;
- civil identity;
- AI state data where protected;
- behavioural records;
- civil records.

## 5. Explicit Non-Scope

This architecture does not:

- prohibit all secondary use;
- require a central privacy authority;
- require a central participant database;
- prohibit legitimate emergency access;
- guarantee that all information is private;
- prevent appropriately justified retention for accountability.

## 6. Principal Components

### 6.1 Purpose Check
What legitimate civil purpose is being served?

### 6.2 Necessity Check
What information is actually required?

### 6.3 Identity Check
Does the downstream function need participant identity?

### 6.4 Minimisation
Reduce detail, scope and duration where practical.

### 6.5 Anonymisation / Aggregation
Remove unnecessary identity before wider civil learning.

### 6.6 Controlled Identity Bridge
Where re-identification is legitimately necessary, use a bounded and provenance-recorded pathway.

## 7. Core Architecture Flow

**PARTICIPANT / IDENTIFIABLE SYSTEM**

↓

**PURPOSE CHECK**

↓

**IS IDENTITY NECESSARY?**

### NO

↓

**MINIMISE**

↓

**ANONYMISE / AGGREGATE**

↓

**DOWNSTREAM CIVIL FUNCTION**

### YES

↓

**LEGITIMATE IDENTIFIABLE PATH**

↓

**PURPOSE-LIMITED ACCESS**

↓

**PROVENANCE**

## 8. Purpose-Transition Events

Where information is proposed for a materially new purpose, that transition should generate an explicit event containing:

- new purpose;
- justification;
- authority or consent where required;
- scope;
- duration;
- provenance.

New purposes should not arise silently from data availability.

## 9. Authority Flow

CA-04 defines ordinary information boundaries.

It does not create exceptional authority.

Where ordinary boundaries legitimately must be crossed:

**CA-04**

↓

**SEPARATE AUTHORITY**

↓

**CA-06**

## 10. Required Boundaries

### 10.1 Purpose Before Data
Purpose should be defined before reuse.

### 10.2 Minimum Necessary Identity
Identity should travel no further than required.

### 10.3 Re-Identification Is Access
Reconstructing identity from anonymised data is itself an identifiable-access event.

### 10.4 Meaningful Contestability
Participant access should be practical enough to understand and challenge consequential information.

### 10.5 Decentralised Enforcement
Common constraints should not require one central information controller.

### 10.6 Accountability Retention Is Also Purpose-Limited
Audit needs should not automatically justify indefinite data hoarding.

## 11. Failure Behaviour

Where purpose cannot be established:

- unnecessary transfer should stop.

Where identity necessity cannot be established:

- identity should not automatically accompany data.

Where emergency access is required:

- CA-06 provides the bounded exceptional route.

The preferred failure direction is toward reduced transfer, not ambient disclosure.

## 12. Anti-Capture Safeguards

Key risks:

- central privacy authority becoming a surveillance hub;
- purpose inflation;
- function creep;
- re-identification;
- data hoarding.

Safeguards:

- decentralised boundaries;
- explicit purpose transitions;
- participant contestability;
- exceptional-access separation;
- provenance.

## 13. Cross-Substrate Considerations

Future work should define whether and how protections apply to:

- AI memory;
- hidden states;
- deliberative traces;
- forked identities;
- collective intelligences;
- hybrid cognitive telemetry.

## 14. Adversarial Findings

The architecture survived strongly.

Mandatory findings:

- common rules do not imply central data control;
- purpose transitions require provenance;
- participant contestability must be meaningful;
- re-identification should count as access.

## 15. Unresolved Questions

- What constitutes a sufficiently specific purpose?
- How should legitimate secondary research use work?
- How should AI internal state privacy be defined?
- When does accountability justify long retention?
- How should cross-jurisdiction data purpose be handled?

## 16. Validation Requirements

Requires:

- privacy threat modelling;
- re-identification testing;
- purpose-creep case studies;
- decentralised implementation analysis;
- cross-substrate information models;
- emergency access testing.

## 17. Current Status

**CANDIDATE ARCHITECTURE — UNDER CRITICAL EXAMINATION / NOT CANONICAL**

