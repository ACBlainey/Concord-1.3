# Derived Information Governance — Architecture Integration Map 001

**Project:** The Concord Framework  
**Date:** 6 October 2026  
**Status:** ACTIVE DEVELOPMENT / INTEGRATION MAP / NON-CANONICAL

## 1. Purpose

Recent development has produced several closely related information architectures.

This integration map prevents them from drifting into duplicated or competing systems.

The family addresses different questions:

1. What happens when legitimate information is combined?
2. What claims attach to newly derived information?
3. Which protections survive transformation?
4. Who may authorise a protection-state change?
5. What happens if protection later fails?

These are distinct.

## 2. Architecture family

### A. Correlation, Recombination and Emergent Information

**Primary question:**

> What new information or sensitivity emerges when individually legitimate information is combined?

Owns:
- correlation permission distinction;
- emergent information;
- aggregate sensitivity;
- re-identification by combination;
- context assembly;
- inference-use distinction;
- correlation firewall concept.

Does not own:
- universal information ownership;
- protection-transition authority;
- incident response.

Core rule:

> **Individually Legitimate Information != Legitimate Combined Inference**

### B. Derived Information Claims, Stewardship and Protection

**Primary question:**

> Once a new informational object exists, whose legitimate claims and duties attach to it?

Owns:
- DIO concept;
- claim decomposition;
- subject/author/holder/steward/third-party/civil claims;
- contestability;
- stewardship versus simplistic ownership;
- relational and multi-source claims.

Does not own:
- how protection technically transitions;
- who authorises declassification;
- exposure response.

Core rule:

> **Informational Ownership != Single Undivided Control Right**

### C. Derived Information Protection-Lineage and Transformation Boundaries

**Primary question:**

> As information is repeatedly transformed, which protections survive, narrow, terminate or newly arise?

Owns:
- protection-lineage transition;
- preserved/narrowed/terminated/new protection;
- semantic exposure;
- functional exposure;
- Legitimate Transformation Boundary;
- lineage compression;
- multi-hop protection state.

Does not own:
- authority source for consequential transition;
- generic dependency propagation;
- incident culpability.

Core rule:

> **Protection Should Follow Protected Meaning And Consequence Through Derivation, But It Should Not Become An Eternal Property Of Informational Ancestry.**

### D. Protection-State Transition Authority and Reclassification

**Primary question:**

> Who may legitimately commit a consequential change in protection state?

Owns:
- contextual protection-transition authority;
- MKA application;
- verifier/authority separation;
- consequence-banded review;
- independence;
- disputed protection transition;
- reclassification/review;
- authority for anonymisation/declassification/public release.

Does not own:
- universal authority generation;
- anonymisation algorithm;
- generic MKA mechanics;
- incident recovery.

Core rule:

> **No Actor Gains Authority To Reduce An Information Object's Protection Merely Because It Possesses, Transforms, Understands Or Benefits From That Information.**

### E. Information Exposure, Reidentification and Successor Protection

**Primary question:**

> What should happen when actual exposure no longer matches intended protection?

Owns:
- exposure state;
- re-identification successor state;
- no fictional rollback;
- containment;
- successor protection;
- downstream review;
- participant notification;
- public-exposure reality;
- operational discoverability versus historical retention.

Does not own:
- culpability determination;
- generic BTA;
- generic correction propagation.

Core rule:

> **When Information Cannot Be Made Secret Again, Govern The State That Actually Exists Rather Than Pretend The Previous State Was Restored.**

## 3. Existing architectures retained

The new family does not replace:

### CIBB
Owns governed information objects and protected operations:
- projection;
- patch;
- controlled derivation;
- protected transfer;
- lifecycle;
- disclosure state;
- protection-relevant lineage.

### PLE
Owns:
- query-to-data;
- local evaluation;
- minimum-result disclosure;
- cumulative-query controls;
- query budgets;
- anti-correlation execution safeguards.

### MKA
Owns generic multi-key authority verification.

### MNC
Owns minimum necessary capability.

### BTA
Owns consequential transition coordination and non-propagation.

### KCS Change Propagation
Owns generic dependency/change review propagation.

### STRA
Owns state-triggered review routing.

### ESCP / ASCP
Own completeness challenge for evaluation and authority spaces.

### DICP
Owns protection of sufficiently intimate/consequential cognitive proxies and inferred mental-state equivalents.

### Historical
Owns historical stewardship, provenance and time-correct preservation under its legitimate domain authority.

### Domain systems
Retain substantive authority over their own protected states.

## 4. End-to-end topology

`Source / Observation / Governed Information`
↓
**CIBB / CWA**
`Protected Context + Legitimate Operation`
↓
**Correlation/Recombination**
`Combined / Emergent Information Evaluation`
↓
**Derived Information Claims**
`New Informational Object + Claim Bundle`
↓
**Protection-Lineage**
`Current Protection State + Surviving/New Protections`
↓
**Protection-State Transition Authority**
`Legitimate Authority To Commit New Protection State`
↓
**CIBB / PLE**
`Minimum Necessary Projection / Local Evaluation / Disclosure`
↓
**BTA / KCS / STRA**
`Consequential Transition + Review Propagation`
↓
If protection later fails:
**Exposure/Reidentification**
`Actual Exposure State + Successor Protection / Remedy`

At every consequential stage:
**ESCP / ASCP**
challenge represented completeness.

## 5. Cross-cutting separations

The family establishes:

**Access != Correlation**

**Correlation != Inference-Use Authority**

**Derivation != Ownership**

**Authorship != Subjecthood**

**Information Descent != Protection Inheritance**

**Transformation != Declassification**

**Protection Evidence != Protection Authority**

**Anonymisation Expertise != Disclosure Authority**

**Disclosure != Unlimited Reuse**

**Exposure != Legitimacy**

**Rollback != Restoration**

**Historical Provenance != Current Operational Permission**

## 6. Example — occupational health

1. Health record is governed by CIBB.
2. Occupational query can use PLE.
3. Health derives `FIT_FOR_ROLE_X`.
4. Derived Information Claims gives worker contestability/protection claims and evaluator authorship/provenance.
5. Protection-Lineage classifies the output as narrower than the source but still participant-related.
6. Protection-State Transition Authority verifies legitimate bounded release to employer.
7. Employer receives only the minimum result.
8. Employer derives `STAFFING_CAPACITY_X_REDUCED`.
9. Protection-Lineage can terminate medical/identity meaning if legitimately removed.
10. Operations receives `REPLACEMENT_REQUIRED`.
11. If a later dataset reconstructs the worker's condition, Correlation/Recombination and Exposure/Reidentification reactivate/newly create appropriate protection.

No architecture needs to own the entire chain.

## 7. Example — research publication

1. Protected participant data remains in CIBB.
2. Research uses legitimate bounded correlation.
3. Derived population pattern becomes DIO with research authorship and participant/source claims.
4. Anonymisation/aggregation proposes a new protection state.
5. Technical validation supplies evidence.
6. MKA-based transition authority checks required independent authorities.
7. Public result is released if authorised.
8. Historical preserves provenance without exposing protected sources.
9. Later re-identification capability triggers STRA/KCS review.
10. Exposure architecture establishes successor protection rather than rewriting history.

## 8. Example — AI orchestration

1. AI has technically reachable context from several domains.
2. CWA/CIBB prevents reachability from becoming universal access.
3. Correlation architecture prevents accessible fragments from becoming automatically combinable.
4. Derived Information Claims protects consequential participant profiles.
5. Protection-Lineage evaluates transformed/modelled outputs.
6. MKA/MNC bound consequential release/use.
7. PLE can answer bounded questions without assembling full source context.
8. If the model leaks protected state, exposure architecture records actual compromise and successor controls.

## 9. Development status

The family is currently best classified as:

**CROSS-DOMAIN INTEGRATION ARCHITECTURE / SOURCE-RESOLVED / ADVERSARIALLY SKETCH-TESTED / NOT YET PMEDG CANDIDATE AS A FAMILY**

Do not extract a new portable mega-module.

Existing portable modules already own much of the implementation grammar.

Further work should focus on:
- adversarial integration tests;
- edge cases;
- identifying whether any small residual portable mechanism exists;
- domain adoption;
- avoiding duplication.

## 10. Next adversarial targets

High-value tests include:
- genomic familial inference where one participant consents and another does not;
- public-record reconstruction of a protected participant state;
- court evidence derived from protected but independently discoverable information;
- AI-generated latent profiles that are never explicitly stored;
- model training where source data is later withdrawn;
- aggregate statistics that create group-level discrimination;
- information learned by a human recipient who cannot literally delete memory;
- cross-civilisation transfer where protection classifications differ;
- cryptographic/technical transformation that destroys source linkability but retains consequential semantic capability;
- participant death/retirement and posthumous/post-retirement informational claims.

## 11. Central integration rule

> **Concord Governs Information By Separating The Object, The Meaning, The Claims, The Protection State, The Authority To Change That State, The Permitted Use, And The Actual Exposure State.**

Collapsing those dimensions is the recurring source of information-governance failure.
