# Embedded Contextual Wrappers for Knowledge Sections — Design Resolution 001

**Project:** The Concord  
**Status:** ACTIVE DEVELOPMENT / DESIGN RESOLUTION / NOT CANONICAL  
**Date:** 30 September 2026  
**Parent:** Knowledge Retrieval Through Contextual Wrappers — Architecture Integration Note 001  
**Applies to:** Participation-bounded retrieval from the living Concord corpus

---

## 1. Design resolution

The preferred architecture is to store knowledge-access classification **with the authoritative source material itself**, using embedded contextual-wrapper markers around documents, sections, subsections or other stable semantic regions.

Do not make an external access-envelope table the authoritative location of section classification.

The governing principle is:

> **Content + Access Boundary = One Versioned Knowledge Object**

This is a direct implementation of Contextual Wrapper Architecture over Concord knowledge.

---

## 2. Why embedded wrappers are preferred

An external mapping such as:

**File A / Section 7 -> Access Class X**

can become stale when:

- a file is renamed;
- a file is moved;
- headings change;
- sections are reordered;
- sections are split or merged;
- content is transferred between domains;
- the repository is migrated;
- a new version becomes authoritative.

If the access boundary is embedded with the bounded semantic material, ordinary movement of that material carries the classification with it.

Therefore:

> **Move The Knowledge -> Move Its Wrapper**

and:

> **Access Classification Should Travel With The Material It Classifies**

This reduces pointer drift and separates authoritative access metadata from derived repository topology.

---

## 3. External indexes remain useful but non-authoritative

The design does not prohibit indexes.

A retrieval system may build:

- access indexes;
- search indexes;
- participant-specific discovery maps;
- caches;
- semantic indexes;
- route indexes;
- compiled access tables.

But these should be derived from the authoritative embedded wrapper state.

Therefore:

> **Embedded Wrapper = Authoritative Access Classification**

> **External Access Index = Derived Retrieval Aid**

If a derived index conflicts with the current embedded wrapper, the embedded wrapper controls unless a higher legitimate architecture explicitly determines otherwise.

Derived indexes should be rebuildable.

---

## 4. Document defaults and nested overrides

A document may establish a default wrapper.

Sections inherit that wrapper unless a valid nested wrapper changes the context.

Conceptually:

```
[DOCUMENT WRAPPER: PARTICIPANT]

Public/participant material...

[BEGIN WRAPPER: ROLE=HEALTH_PROFESSIONAL; FUNCTION=CLINICAL_CARE]

Specialist clinical material...

[END WRAPPER]

Participant material resumes...
```

The exact syntax above is illustrative only.

The final grammar has not yet been selected.

Core behaviour:

**Document Default**
-> **Section Override**
-> **Subsection Override**
-> **End Nested Context**
-> **Return To Parent Wrapper**

This mirrors CWA nested-context behaviour.

---

## 5. Classification need not be a single level

The marker must eventually be capable of expressing more than a scalar participation level.

A wrapper may depend upon combinations of:

- participation level/state;
- role;
- function;
- qualification;
- subject;
- relationship;
- consent;
- privacy state;
- security state;
- delegated responsibility;
- temporal condition;
- emergency condition;
- jurisdiction/context;
- review state;
- authority basis.

Therefore a marker grammar should not be designed around only:

```
LEVEL=3
```

It must be capable of representing contextual predicates without becoming unreadable.

Participation remains an important input, not universal clearance.

---

## 6. Positive exposure and restriction

A wrapper should be able to describe both ordinary exposure and narrower contextual access.

Examples of conceptual states may include:

- OPEN;
- PARTICIPANT;
- SELF/SUBJECT;
- ROLE-BOUNDED;
- FUNCTION-BOUNDED;
- CONTROLLED;
- RESTRICTED;
- SEALED;
- REDACTED;
- TEMPORARY;
- CONTEXTUAL.

These labels are provisional.

The next instance must source-resolve them against KCS, participation architecture, privacy architecture and existing Concord terminology before fixing the vocabulary.

---

## 7. Retrieval behaviour

The intended runtime behaviour is:

**Participant / Evaluator Context**
+
**Information Request**
+
**Legitimate Function**
-> **Locate Relevant Authoritative Knowledge**
-> **Parse Embedded Contextual Wrappers**
-> **Resolve Applicable Context**
-> **Retrieve Permitted Semantic Regions**
-> **Return Bounded View With Provenance**

Material outside the resolved wrapper context should not enter the evaluator's active information space merely because it exists in the same source file.

Therefore:

> **Whole File Available To Retrieval Engine != Whole File Exposed To Participant**

---

## 8. Example

A single Governance file might conceptually contain:

```
[DOCUMENT DEFAULT: OPEN]

## Purpose
...

## Constitutional relationship
...

[BEGIN: PARTICIPANT]

## Exercising a participant right
...

[END]

[BEGIN: ROLE=GOVERNANCE_CASE_OFFICER; FUNCTION=CASE_PROCESSING]

## Internal case-processing procedure
...

[END]

[BEGIN: RESTRICTED; ROLE=SECURITY; FUNCTION=INCIDENT_RESPONSE]

## Sensitive operational procedure
...

[END]
```

The source remains one file.

Different retrieval contexts expose different semantic regions.

No participant-specific copy of the Governance document is created.

---

## 9. Bounded view disclosure

A retrieved view must not imply that it is the complete source where it is not.

Where legitimate and safe, the retrieval output should indicate that:

- the view is contextually bounded;
- additional material may exist;
- omission does not imply absence;
- further access may require another legitimate context or review.

Therefore:

> **Retrieved Material != Complete Knowledge Object**

> **Not Retrieved != Does Not Exist**

> **Awareness Of Restricted Material != Entitlement To Restricted Material**

This is required by ESCP as well as access architecture.

---

## 10. Public accountability

Embedded restriction must not permit sensitive implementation detail to swallow public accountability information.

Where operational material is restricted, the architecture should still preserve appropriate accessible material describing, where applicable:

- existence of the power/process;
- legitimate basis;
- scope;
- affected rights/interests;
- accountability;
- review;
- challenge;
- remedy.

These may be separate semantic sections under broader wrappers within the same authoritative source.

Thus the source can contain both:

**Publicly Accountable Description**

and:

**Restricted Operational Implementation**

without duplicating the same substantive text into separate document families.

---

## 11. Change integrity

Embedding solves much of the stale external-pointer problem, but not every change problem.

If a writer changes the meaning of material inside an existing wrapper, the classification may itself require review.

Examples:

- sensitive operational detail is added to an OPEN section;
- personally identifying information is inserted into participant-level material;
- a formerly restricted procedure becomes public;
- a section changes function while retaining its old wrapper.

Therefore:

> **Wrapper Moves With Content, But Wrapper Validity Must Still Track Content Meaning**

Future editing/change-propagation processes should detect or require review of wrapper-relevant changes.

---

## 12. Machine readability and human readability

The wrapper grammar should ideally satisfy both.

Humans editing Markdown should be able to see and understand the boundary.

Retrieval systems should be able to parse it deterministically.

The grammar should therefore aim for:

- explicit boundaries;
- unambiguous nesting;
- predictable inheritance;
- machine-readable fields;
- human-readable meaning;
- low editing burden;
- compatibility with Markdown;
- preservation through ordinary repository tools;
- visible failure when malformed.

Avoid access semantics that depend only on invisible external metadata.

---

## 13. Fail-closed versus fail-open requires development

A malformed or missing wrapper creates an important unresolved question.

Automatically treating malformed material as OPEN could expose protected information.

Automatically treating every unclassified legacy section as RESTRICTED could make the existing Concord unusable during migration.

The migration architecture therefore requires an explicit transitional policy.

Do not silently choose one.

Record this as a required development question:

> **How should legacy, missing, malformed, conflicting or unresolvable knowledge wrappers behave during migration and operation?**

This should be tested adversarially.

---

## 14. Legacy corpus migration

The existing V1.3 corpus predates embedded wrappers.

It should not be mass-classified by crude automated assumptions.

Recommended sequence:

1. define and test wrapper grammar;
2. source-resolve participation/access vocabulary;
3. define inheritance and conflict behaviour;
4. define legacy/unclassified handling;
5. select a small representative corpus sample;
6. manually/classificationally map semantic sections;
7. blind-test retrieval;
8. revise grammar where necessary;
9. only then begin systematic corpus-wide classification.

The migration should preserve source content unless substantive editing is independently justified.

The initial task is to **wrap**, not rewrite.

---

## 15. Relationship to repository migration principle

This architecture aligns with:

> **Migrate the Living Result; Archive the Developmental Path**

because access classification remains attached to the living authoritative object rather than generating a parallel family of access-specific copies.

Historical versions retain the wrapper state applicable to their version where present.

Current access rules for historical material may additionally be governed by Historical-domain architecture; this interaction requires source resolution.

---

## 16. Candidate wrapper grammar requirements

Before choosing exact syntax, the grammar should support at least:

- document default;
- begin bounded region;
- end bounded region;
- nested region;
- participation predicate;
- role predicate;
- function predicate;
- subject/self predicate;
- contextual predicate;
- temporal predicate where required;
- access state;
- restriction state;
- inheritance;
- explicit override;
- review metadata where needed;
- stable source/semantic identity where needed;
- human-readable reason/basis where consequential.

It should also define what happens when predicates combine:

- AND;
- OR;
- inherited conditions;
- override;
- narrowing;
- widening;
- conflict.

Do not assume that widening a parent restriction is legitimate merely because syntax permits it.

---

## 17. Architectural composition

The current working composition is:

**KCS**
-> authoritative knowledge object, provenance and represented access state

**CWA**
-> embedded bounded informational contexts and inheritance

**MNC**
-> minimum sufficient information capability

**Participation / Role / Qualification architecture**
-> participant-side context

**BCA**
-> bounds authority used to establish or alter access

**Change Propagation**
-> detects source changes that may invalidate wrapper state

**Retrieval System**
-> evaluates context and exposes only permitted semantic regions

This is an integration problem, not a reason to duplicate these architectures.

---

## 18. Updated next-step instruction

The next major development instance should treat embedded CWA wrappers as the preferred hypothesis.

Its first implementation task should be to design and test a **small, explicit, human-readable and machine-readable Markdown wrapper grammar** against representative Concord documents.

Do not immediately classify the whole repository.

Use representative cases containing:

- wholly public material;
- mixed public/participant material;
- role-specific material;
- privacy-sensitive material;
- security-sensitive material;
- nested contexts;
- temporary/emergency access;
- self-access;
- material whose classification is uncertain.

Test whether the grammar can express existing Concord access intentions without duplicating source content or manufacturing new authority.

Only after that test should corpus-wide classification begin.

---

## 19. Core invariants

> **Content + Access Boundary = One Versioned Knowledge Object**

> **Move The Knowledge -> Move Its Wrapper**

> **Access Classification Should Travel With The Material It Classifies**

> **Embedded Wrapper = Authoritative Access Classification**

> **External Access Index = Derived Retrieval Aid**

> **Document Classification != Necessarily Section Classification**

> **Whole File Available To Retrieval Engine != Whole File Exposed To Participant**

> **Retrieved Material != Complete Knowledge Object**

> **Not Retrieved != Does Not Exist**

> **Wrapper Moves With Content, But Wrapper Validity Must Still Track Content Meaning**

> **The Initial Task Is To Wrap, Not Rewrite**

---

## 20. Development status

This design is sufficiently clear to guide the next instance, but the exact marker syntax, classification vocabulary, inheritance rules, conflict rules, legacy behaviour and corpus classifications remain to be developed and tested.

Do not treat the illustrative marker syntax in this note as canonical.

Do not begin bulk corpus modification until the wrapper grammar has passed a bounded representative test.
