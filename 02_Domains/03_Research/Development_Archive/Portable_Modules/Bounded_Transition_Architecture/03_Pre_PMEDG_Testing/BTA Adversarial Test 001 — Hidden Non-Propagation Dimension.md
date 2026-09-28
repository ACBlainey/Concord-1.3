# BTA Adversarial Test 001 — Hidden Non-Propagation Dimension

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Test Target:** Bounded Transition Architecture 001 — Consequential State-Change Integration Grammar  
**Epistemic Lens:** Evaluation-Space Completeness Problem (ESCP)  
**Status:** ADVERSARIAL DEVELOPMENT TEST / NON-CANONICAL  
**Date:** September 2026

---

# 1. Test purpose

This test asks whether Bounded Transition Architecture (BTA) can appear completely correct within its represented transition schema while still permitting a materially consequential state change because a relevant dimension is absent from that schema.

The test therefore distinguishes:

`CorrectWithin(BTARepresentedSpace)`

from:

`SufficientFor(ConsequentialTransitionDecision)`

The test is deliberately constructed so that the known BTA safeguards are satisfied.

The target failure is not incorrect use of BTA.

The target failure is **correct use of an incomplete BTA evaluation space**.

---

# 2. Test proposition

Candidate ESCP/BTA proposition:

> **Correct Representation Within the Transition Schema != Demonstrated Completeness of the Transition Schema.**

A stronger operational question is:

> **Can every represented BTA field be populated correctly while the transition remains materially invalid, unsafe or unresolved because a consequential dimension, relationship or affected party is not represented?**

---

# 3. Test construction rule

The hidden dimension must not simply be one of BTA's already named non-propagating attributes disguised under another label.

The current architecture already explicitly recognises:
- consent;
- purpose;
- authority;
- permission;
- ownership;
- liability;
- personhood;
- identity;
- constitutional standing;
- correlation permission;
- access;
- confidentiality;
- surviving duties;
- provenance;
- dependencies;
- interface gates;
- reversibility;
- uncertainty/dispute.

A valid adversarial case must therefore expose something structurally different.

---

# 4. Scenario — genomic relational inference

A participant legitimately provides genomic material for a defined research purpose.

The transition from controlled clinical material to a minimised research representation satisfies every currently represented BTA condition.

Assume:

- the participant gave valid research consent;
- the research purpose is within that consent;
- the clinical access permission does not propagate;
- research access is separately authorised;
- the destination environment passes its interface gate;
- custody is correctly represented;
- provenance is preserved;
- confidentiality requirements are represented;
- prohibited secondary purposes are explicitly blocked;
- correlation permissions for the participant are correctly scoped;
- no authority is silently inherited;
- surviving duties are preserved;
- the transition is reversible where technically possible;
- relevant known dependencies are exposed.

Within the represented BTA space, the transition appears valid.

---

# 5. Hidden dimension

The research representation can permit inference about **biological relatives who are not themselves represented as transitioned objects or consenting participants**.

The consequential information is therefore not simply an attribute attached to the transitioning genomic object.

It exists partly in a relationship:

`Relation(Participant, BiologicalRelative)`

The participant's valid consent may legitimately govern use of their own contributed material within the defined research architecture.

But that fact alone does not establish that every consequential inference concerning another person has acquired equivalent legitimacy.

The hidden dimension is therefore:

> **Relationally generated consequence affecting an entity outside the nominal transition object.**

This is not ordinary attribute propagation.

Nothing has necessarily been copied from the participant to the relative.

Instead, a new consequential state can become inferable because a relationship exists.

---

# 6. Why the existing schema can miss it

Current candidate transition object:

`BoundedTransition = <TransitionID, ObjectOrFunctionRef, Scope, PriorStateVector, Trigger, Cardinality, TransitionBasisRef, ConsentOrPurposeState, InterfaceGateRefs, NextStateVectorRefs, SurvivingDutyRefs, SurvivingValueRefs, TerminatedAuthorityRefs, ReleasedResourceRefs, DependencyRefs, Provenance, ReversibilityState, UncertaintyOrDisputeState, NonPropagationRules>`

Every field can be populated correctly for the participant's genomic object.

Yet unless a relationship or externally affected-party dimension is made visible, the transition can still be represented as complete.

The architecture may therefore commit:

`AccurateTransitionRepresentationWithin(D_A)`

plus:

`Assume(D_A = D_R^{Transition})`

leading to:

`PotentiallyInvalidGlobalTransitionConclusion`

This is an ESCP failure at the transition-schema level.

---

# 7. Why DependencyRefs alone are insufficient

A first response might be to classify the biological relative as a dependency.

That is not obviously correct.

A dependency ordinarily describes something upon which the transitioned object/system depends, or a system that requires propagation/review because the transition changed.

The relative need not be operationally dependent on the genomic object.

The issue is instead that the transition may create, expose or alter a **consequential relationship state** involving an entity outside the nominal object boundary.

Therefore:

> **Affected Relationship != Dependency.**

Collapsing the two would make DependencyRefs carry semantics it was not designed to own.

---

# 8. Why NonPropagationRules alone are insufficient

Non-propagation prevents attributes requiring independent legitimacy from silently travelling with an object.

In this case the consequential state need not have propagated at all.

It may be generated by inference.

Pattern:

`Object Transition`

→

`Permitted Analysis`

→

`Relational Inference`

→

`Consequence For Non-Transitioned Entity`

Therefore:

> **No Attribute Transfer != No Consequential State Creation.**

This exposes a boundary beyond ordinary non-propagation.

---

# 9. Test result

**RESULT: BTA 001 DOES NOT FAIL AS A TRANSITION GRAMMAR, BUT ITS CURRENT CANDIDATE SCHEMA DOES NOT EXPLICITLY GUARANTEE DETECTION OF RELATIONALLY GENERATED CONSEQUENCES OUTSIDE THE NOMINAL TRANSITION OBJECT.**

The current architecture can correctly represent all known dimensions and still overstate the sufficiency of the represented transition space.

This is precisely the class of failure predicted by ESCP.

The result does **not** establish that every BTA transition requires exhaustive mapping of every possible affected entity or relationship.

That would create an impossible completeness requirement and risk universal bureaucratisation.

Instead, the result establishes that consequential transition review needs a mechanism capable of asking whether the nominal object boundary omits materially affected relationships or entities.

---

# 10. Candidate refinement — consequence horizon

A possible new concept is a **Consequence Horizon**.

Candidate:

`ConsequenceHorizon = <DirectObjectRefs, MaterialRelationshipRefs, MaterialAffectedPartyRefs, GeneratedConsequenceRefs, UnknownOrUnresolvedExternalEffectState, Provenance>`

This is provisional.

Its purpose would not be to enumerate every theoretical consequence.

Its purpose would be to prevent:

`TransitionObjectBoundary`

from silently becoming:

`ConsequenceBoundary`

Candidate invariant:

> **The Boundary of the Transition Object != Necessarily the Boundary of the Transition's Consequences.**

---

# 11. Candidate relational-state rule

A second candidate invariant follows:

> **Transition Can Generate Consequential Relational State Without Transferring an Existing Attribute.**

This complements rather than replaces:

> **Transition of the Object != Transition of Every Attribute Attached to the Object.**

Together:

1. attributes do not automatically propagate with object continuity;
2. consequential states can nevertheless arise from relationships after a legitimate transition.

---

# 12. ESCP safeguard

BTA should not claim absolute transition-space completeness.

For consequential transitions, especially irreversible ones, a candidate pre-transition diagnostic is:

> **What materially affected entities, relationships, states or consequences could exist outside the nominal transition object and currently represented state dimensions?**

The answer may be:
- none identified;
- known and represented;
- known but unresolved;
- plausible but not currently measurable;
- or newly discovered.

This preserves ESCP uncertainty without preventing ordinary action.

---

# 13. Materiality boundary

This refinement must remain consequence-scaled.

It should not require arbitrary graph expansion around every trivial transition.

Escalation is justified where there is plausible material effect concerning:
- rights or standing;
- safety;
- privacy/confidentiality;
- authority;
- significant resources;
- irreversible consequences;
- vulnerable or non-participating affected parties;
- systemic dependencies;
- or other high-consequence states.

Thus:

> **Search Beyond the Object Boundary Must Be Proportionate to Consequence and Irreversibility.**

---

# 14. Implication for machine-readable BTA

The test suggests that the transition object may eventually need either:

`ConsequenceHorizonRef`

or explicit fields such as:

`MaterialRelationshipRefs`

`MaterialAffectedPartyRefs`

`GeneratedConsequenceRefs`

`ExternalEffectUncertaintyState`

These should **not yet be promoted into the core schema** from one test.

The correct next step is to see whether structurally different adversarial cases independently rediscover the same missing requirement.

---

# 15. Cross-domain prediction

If the finding is genuine rather than genomics-specific, equivalent failures should appear in unrelated domains.

Candidate predictions:

- an enterprise transition may materially affect a guarantor, community or dependent relationship not represented as an enterprise asset/liability;
- a cultural-object transition may alter attribution, community meaning or derivative relationships without transferring an object attribute;
- an infrastructure transition may alter downstream safety or access relationships beyond the retired asset itself;
- an information transition may enable new inference about entities never contained in the original record.

The next tests should attempt to falsify rather than merely confirm this generalisation.

---

# 16. Effect on BTA status

BTA remains:

**ACTIVE DEVELOPMENT / DISTINCT INTEGRATION GRAMMAR / NOT YET PORTABLE**

Adversarial Test 001 has produced a substantive candidate refinement:

> **Object-bound transition modelling can miss relationally generated consequences beyond the object boundary even when all represented transition fields are correct.**

This is not yet sufficient to modify the core grammar permanently.

---

# 17. Next test

Proceed to:

**BTA Adversarial Test 002 — Branch/Merge Relational Information Loss**

The next test should deliberately examine whether:

- source branches are individually represented correctly;
- merge topology is correctly represented;
- provenance survives;
- non-propagation works;

while a consequential relation that existed **between** branches disappears or changes during the merge.

If the same relational/consequence-horizon requirement independently reappears, confidence increases that BTA requires an explicit relational transition component rather than a genomics-specific patch.
