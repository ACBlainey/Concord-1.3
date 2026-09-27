# Machine-Readable Topology Dataset v0.3 — Cross-Scale Functional Role Graphs

**Status:** V1.2a FORMAL DATASET / H3 TEST INPUT  
**Date:** September 2026  
**Canonical effect:** NONE  
**Source basis:** Cross-Scale Motif Test 001 and its source-grounded frozen derivations

---

# 1. Purpose

This dataset converts four scale-specific architectural examples into a common functional-role representation so that cross-scale structural similarity can be tested explicitly.

The scales are:

- S1 — Participant
- S2 — Institutional
- S3 — Whole-civilisation
- S4 — Intercivilisational

The role vocabulary is deliberately small and fixed before calculating similarity.

---

# 2. Role Vocabulary

R1 — Reality / Need Recognition  
R2 — Legitimate Function  
R3 — Minimum Sufficient Scope / Boundary  
R4 — Protected Agency / Standing  
R5 — Asymmetry / Non-Domination Constraint  
R6 — Contestability / Review  
R7 — Correction / Repair  
R8 — Temporal Revision / Contraction / Exit  
R9 — Function-Over-Form Continuity  
R10 — Provenance / Learning

These are analytical roles, not ethical roots.

---

# 3. Canonical Candidate Grammar

The candidate role graph contains the following directed relations:

```csv
source,target,relation
R1,R2,grounds
R2,R3,bounds
R3,R4,preserves
R4,R6,enables_challenge
R5,R3,constrains_scope
R5,R6,requires_review
R6,R7,enables_correction
R7,R8,triggers_revision
R8,R9,preserves_function_over_form
R10,R6,supports_review
R7,R10,produces_learning
```

This is a test template, not a claim that every scale must instantiate every edge.

---

# 4. Scale-Specific Role Instantiations

## S1 — Participant

Concrete source examples: information relationship and developmental support.

```csv
role,participant_scale_instance
R1,actual need harm capability or information consequence
R2,legitimate support or information purpose
R3,least necessary substitution / bounded information use
R4,participant agency and standing
R5,dependency coercion paternalism or informational asymmetry constraint
R6,participant challenge and contestability
R7,correction repair or changed support
R8,reassessment return of agency or reduced intervention
R9,support/protection function can persist while method changes
R10,decision/information provenance and learning
```

## S2 — Institutional

Concrete source example: function-bounded governance authority.

```csv
role,institutional_scale_instance
R1,evidence of legitimate public/cooperative need
R2,defined institutional function
R3,mandate and scope boundary
R4,affected participant standing
R5,anti-capture minority protection and non-arbitrary power
R6,review challenge and independent oversight
R7,correction restructuring or replacement
R8,sunset renewal termination or contraction
R9,necessary function can survive institution replacement
R10,transparent justification outcome monitoring and provenance
```

## S3 — Whole-Civilisation

Concrete source example: canonical fractal architecture / subsidiarity.

```csv
role,whole_civilisation_instance
R1,problem condition and competence assessment
R2,civilisational function
R3,lowest competent legitimate scale
R4,local autonomy/competence and participant standing
R5,polycentric anti-sovereignty and anti-capture constraint
R6,recursive oversight/review
R7,correction or redistribution of responsibility
R8,escalation/de-escalation as conditions change
R9,stable civilisational function/purpose with adaptive institutional form
R10,recorded reasoning provenance and recursive learning
```

## S4 — Intercivilisational

Concrete source example: plural coexistence and interoperability.

```csv
role,intercivilisational_instance
R1,cross-boundary effect or cooperative need
R2,defined cooperative function
R3,minimum shared interface
R4,civilisational autonomy and affected-party standing
R5,asymmetry dependency and anti-domination review
R6,dispute/jurisdiction and agreement challenge
R7,correction repair or relationship adaptation
R8,amendment termination reduced integration or peaceful distance
R9,cooperative function can survive treaty/interface replacement
R10,relationship provenance failures corrections and learning
```

---

# 5. Edge Presence Matrix

1 = source-grounded relation established in Cross-Scale Motif Test 001/source material.  
0 = not established in this compressed pass; not proof of absence.

```csv
edge,S1,S2,S3,S4
R1->R2,1,1,1,1
R2->R3,1,1,1,1
R3->R4,1,1,1,1
R4->R6,1,1,1,1
R5->R3,1,1,1,1
R5->R6,1,1,1,1
R6->R7,1,1,1,1
R7->R8,1,1,1,1
R8->R9,1,1,1,1
R10->R6,1,1,1,1
R7->R10,1,1,1,1
```

---

# 6. Important Limitation

The all-ones matrix is **not** an independent statistical discovery.

The role graph was abstracted from the source-grounded recurrence already observed in Cross-Scale Motif Test 001.

Therefore this dataset demonstrates that the recurrence can be represented formally; it cannot by itself establish how surprising the recurrence is.

A stronger H3 test requires comparing the role graph against:

- additional cases not used to define it;
- negative/control architectures;
- alternative role mappings;
- perturbations of the mapping;
- or independently developed systems.

This protects against circular confirmation.

---

# 7. Appropriate Use

v0.3 is suitable for:

- graph isomorphism under role abstraction;
- testing stability under removal/addition of roles;
- extending to new scales;
- out-of-sample motif tests;
- provenance-aware topology tooling.

It is not sufficient for estimating a fractal dimension or claiming statistical scale invariance.
