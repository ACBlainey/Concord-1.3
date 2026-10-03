# MKA — PMEDG Graduation Review 001

**Project:** The Concord Framework  
**Date:** 3 October 2026  
**Status:** GRADUATION REVIEW / PROVISIONAL / NON-CANONICAL  
**Candidate:** Multi-Key Authority (MKA)  
**Embedded component:** Authority-Space Completeness Problem (ASCP)

## 1. Review question

Has MKA completed enough of the PMEDG development path to graduate from cross-domain candidate architecture into a portable module?

## 2. Evidence reviewed

The graduation review considers:

1. Multi-Key Authority and Rapid Authority Verification — Cross-Domain Source Resolution 001.
2. Multi-Key Authority — Cross-Domain Adversarial Test 001.
3. Authority-Space Completeness Problem — Development Note 001.
4. MKA - ASCP - ESCP - CBPR - CWA - BTA — Composition and Non-Duplication Audit 001.
5. MKA Portable Kernel Candidate — Extraction Boundary 001.
6. MKA Portable Kernel Candidate — Frozen Kernel 001.
7. MKA Blind Transfer Test 001 — Test Brief.
8. MKA Blind Transfer Test 001 — Scenario Pack.
9. MKA Blind Transfer Test 001 — Raw Clean Evaluator Result.
10. MKA Blind Transfer Test 001 — PMEDG and CRADP Assessment.

## 3. Development-path findings

### 3.1 Distinct problem

**PASS**

MKA owns a distinct problem:

> **Do the independently necessary authorities for this actual route legitimately compose into authority to commit this act now?**

Removal testing showed that CWA, ESCP/ASCP, CBPR and BTA do not independently answer that question.

### 3.2 Source resolution

**PASS**

The architecture was source-resolved across independently developed Concord systems rather than derived solely from the life-support case that exposed it.

### 3.3 Cross-domain applicability

**PASS**

The architecture applies across policing, custody, evidence, cognitive access, infrastructure, scarcity, emergency action, runtime execution, property/resource contexts and the independent blind-test domains.

### 3.4 Adversarial resilience

**PASS**

The cross-domain adversarial test produced refinements but did not collapse the architecture.

### 3.5 Non-duplication

**PASS**

Formal audit distinguished:

- ESCP — general evaluation-space completeness;
- CWA — context/permission/authority topology;
- ASCP — authority-space completeness;
- MKA — authority composition and current verification;
- CBPR — bounded runtime execution;
- BTA — transition coherence.

### 3.6 Minimum extraction boundary

**PASS**

The frozen kernel removed developmental history and retained only the transferable authority-composition contract.

### 3.7 Clean transfer

**PASS WITH NON-BLOCKING CLARIFICATION**

The clean evaluator reported:

**TRANSFER VALIDATED WITH NON-BLOCKING CLARIFICATIONS**

It found no falsification success requiring revision.

### 3.8 Anti-capture / anti-expansion

**PASS**

The candidate explicitly resists:

- authority creation by verifier;
- capability-to-authority conversion;
- credential-to-authority conversion;
- registry-to-authority conversion;
- emergency-to-unlimited-authority conversion;
- benefit-to-authority conversion;
- transition-to-authority conversion;
- automatic authority composition;
- automatic authority inheritance;
- bureaucratic key explosion.

## 4. ASCP disposition

ASCP should **remain embedded within MKA for this graduation**.

Reason:

ASCP derives its completeness discipline from ESCP but becomes operationally specific only when applied to MKA's authority graph.

Extracting ASCP separately now would risk creating a very small wrapper around:

> **All Represented Keys Valid != All Required Keys Represented**

without sufficient independent operational function outside MKA.

Therefore:

**ASCP = embedded MKA completeness layer / ESCP-derived specialist application**

This does not prevent later independent extraction if future architectures demonstrate substantial ASCP use outside MKA.

## 5. Non-blocking vocabulary clarification

The clean evaluator exposed a useful interface state:

`EXTERNAL_OWNER_REQUIRED`

This is not an authority decision.

It means:

> **The unresolved question belongs to an identified external architecture/domain owner and MKA should hand off rather than absorb that function.**

A second optional descriptive state may be:

`OUTSIDE_MKA_SCOPE`

These should be added to the portable module's interface vocabulary, with provenance showing that they arose from Blind Transfer Test 001.

They should not alter the tested kernel's substantive rules.

## 6. Does the clarification require another blind test?

**No blocking retest is required before graduation.**

Reason:

- it does not alter authority semantics;
- it does not alter the permission gate;
- it does not alter ASCP;
- it does not alter key validity;
- it does not alter composition;
- it does not alter prohibition handling;
- it does not alter freshness/commit logic;
- it merely makes an already-correct external handoff explicit.

A later regression test should include the new vocabulary.

## 7. Portability finding

MKA has demonstrated:

- substrate neutrality;
- domain neutrality;
- institutional neutrality;
- implementation neutrality;
- bounded scope;
- explicit external dependencies;
- independent clean transfer.

It therefore satisfies the architectural conditions for portable extraction.

## 8. Graduation decision

> **GRADUATE TO PORTABLE MODULE v1.0**

Graduation is architectural, not constitutional.

The portable module remains:

**NON-CANONICAL / OPTIONAL / REUSABLE / HOST-DEPENDENT FOR SUBSTANTIVE AUTHORITY SOURCES**

## 9. Portable-module requirements

The v1.0 module should contain:

1. purpose/problem;
2. authority-composition rule;
3. permission-before-authority gate;
4. actual-act/route representation;
5. embedded ASCP;
6. authority key/reference model;
7. scope validation;
8. composition/inheritance validation;
9. independence requirements;
10. prohibition layer;
11. predicate/freshness validation;
12. proposal/commit separation;
13. rerouting;
14. unknown/dispute handling;
15. external-owner handoff;
16. provenance;
17. review/reopening;
18. candidate state vocabulary;
19. invariants;
20. integration boundaries.

It should not contain the full developmental narrative.

## 10. Required dependency references

The portable module should identify conceptual interfaces with:

- ESCP;
- CWA;
- CBPR;
- BTA;
- host substantive authority sources.

These are interfaces, not mandatory bundled implementations.

## 11. Provenance package

The module provenance should point to:

- source resolution;
- adversarial test;
- composition audit;
- frozen kernel;
- blind-test brief;
- scenario pack;
- raw result;
- PMEDG/CRADP assessment;
- this graduation review.

## 12. Versioning

Recommended release:

**Multi-Key Authority — Portable Module v1.0**

Version 1.0 is justified because the module has crossed the minimum path from discovery through source resolution, adversarial testing, boundary isolation and clean transfer.

The new external-owner vocabulary is an integration clarification included at graduation, not a change to the core tested authority semantics.

## 13. Post-graduation tests

Recommended later tests:

1. regression test of `EXTERNAL_OWNER_REQUIRED`;
2. implementation test using a machine-readable authority registry without making the registry the authority source;
3. live composition test with CWA + CBPR + BTA;
4. high-speed emergency verification test;
5. complex delegation/inheritance graph test;
6. batch-action exception test.

These are maturation tests, not blockers to v1.0 graduation.

## 14. Final graduation statement

> **Multi-Key Authority has demonstrated a distinct cross-domain problem, source-resolved architecture, adversarial resilience, non-duplication, bounded extraction, and clean blind transfer. It is therefore approved for extraction as Portable Module v1.0, with ASCP embedded as its ESCP-derived authority-completeness layer and with explicit external-owner handoff vocabulary added as a non-semantic integration clarification.**

**PMEDG RESULT: GRADUATED**
