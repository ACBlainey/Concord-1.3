# Prospective Finding — Developmental Dependency Topology and Upstream Bottleneck Resolution

**Status:** V1.2a PROSPECTIVE FINDING / TESTABLE  
**Date:** September 2026  
**Canonical effect:** NONE  
**Origin:** CDRP → TIF-001 → Civilisation Clock dependency observation

# 1. Finding

Civilisational systems should not be assessed for developmental maturity only in isolation.

A system can be locally coherent at its current level while being unable to advance because a capability it legitimately depends upon belongs to another architectural unit that has not yet developed far enough.

This produces a distinct condition:

# **Developmental Dependency Gap (DDG)**

> A required capability has an identifiable legitimate owning system, but that upstream system has not yet reached the developmental level required by one or more downstream dependents.

This differs from:

- **Structural Gap** — no adequate civil function/owner has been identified;
- **Integration Gap** — adequate function exists but the requiring system is not properly connected to it;
- **Developmental Dependency Gap** — the correct owner exists, but its current maturity does not yet satisfy the dependent requirement.

# 2. Core Relation

Let system A require capability x supplied by system B:

A --requires x--> B.

Let:

- M(B) = current maturity of B;
- R(B|A,x) = maturity/capability level B must possess to satisfy A's requirement.

Then a developmental dependency gap exists where:

M(B) < R(B|A,x).

The appropriate response is not automatically to create a new subsystem inside A.

Instead:

Detect unmet requirement
→ identify legitimate capability owner
→ assess owner maturity
→ develop owner
→ propagate capability downstream
→ retest dependent.

# 3. Bidirectional Developmental Information

Dependency topology carries information in two directions.

## Downstream

**Capabilities flow downstream.**

An upstream system's developed functions enable dependent systems.

## Upstream

**Unmet requirements flow upstream.**

A downstream system can reveal that an upstream owner lacks a capability now required by the wider architecture.

Therefore:

Upstream Capability → Downstream Development

while:

Downstream Unmet Requirement → Upstream Development Signal.

This creates a recursive developmental feedback structure.

# 4. Upstream Bottlenecks

If multiple systems independently expose requirements owned by the same immature upstream system, apparently separate development gaps may have a common cause.

For systems A, B, C and D:

A → U
B → U
C → U
D → U

where U is underdeveloped, local patching of A–D may be inefficient or structurally wrong.

The preferred sequence may be:

Develop U
→ propagate new capability
→ retest A,B,C,D
→ retain only surviving local residuals.

This condition is an **Upstream Development Bottleneck (UDB)**.

# 5. Development Priority

The most underdeveloped system is not necessarily the system that should be developed first.

Development priority should consider at least:

- maturity deficit;
- number of downstream dependencies;
- criticality of the required capability;
- severity of blocked downstream development;
- whether one upstream improvement can satisfy multiple domains;
- whether delay creates safety/rights/continuity risk;
- whether the dependency is genuine or only convenient.

A numerical score is not yet justified.

The dependency graph itself should first be tested as a qualitative prioritisation mechanism.

# 6. Developmental Levelling Reinterpreted

Earlier developmental levelling can now be refined.

Do not simply raise every system independently toward the same nominal maturity.

Instead:

Map systems
→ map owned capabilities
→ map dependencies
→ identify maturity deficits
→ identify upstream bottlenecks
→ develop prerequisite systems
→ propagate capabilities
→ retest dependents
→ repeat
→ then advance abstraction layer.

Thus levelling is **dependency-aware**.

# 7. Gap Attribution Rule

A gap observed in system A should not automatically be attributed to A.

Candidate diagnostic:

MissingRelation(A,r)
+ ExplicitOrLegitimateOwner(B,r)
+ Maturity(B)BelowRequired
→ DevelopmentalDependencyGap(A→B,r)

and:

DevelopmentalDependencyGap(A→B,r)
→ DoNotCreateDuplicateLocalSubsystemInAWithoutIndependentNeed.

This extends the existing architectural-unit anti-false-positive rule.

# 8. First Candidate Empirical Case — Civilisation Clock

CDRP exposed the need for consequence-relevant ordering of divergent civil events.

Initial classification produced TIF-001.

Subsequent architectural reasoning identifies the early-stage **Civilisation Clock** as a plausible legitimate owner of at least part of this temporal/dependency function.

Therefore the case becomes:

CDRP
→ consequence-relevant ordering requirement
→ Civilisation Clock
→ assess Clock maturity
→ develop Clock if required
→ retest CDRP/TIF-001.

The hypothesis is stronger if the Clock is independently found to be upstream of multiple other systems.

# 9. Falsification Conditions

The model is weakened if:

- apparent upstream dependencies repeatedly prove artificial;
- developing the proposed owner does not resolve downstream gaps;
- most requirements still require domain-local mechanisms;
- dependency mapping merely redescribes document references without predicting useful development order;
- high-connectivity systems are not development bottlenecks;
- the model systematically routes functions to inappropriate owners;
- local solutions outperform upstream development without architectural duplication or inconsistency.

# 10. Test

Construct a dependency map centred on the Civilisation Clock.

For every candidate dependent:

1. identify the required capability;
2. verify that the Clock is a legitimate owner rather than merely related;
3. determine whether the capability currently exists;
4. classify current maturity;
5. determine whether missing Clock development blocks the dependent;
6. specify the minimum Clock extension;
7. predict which downstream gap should reduce if that extension is developed;
8. develop/retest only after the prediction is frozen.

If multiple independently identified downstream problems converge on the same missing Clock capability, this supports the Upstream Development Bottleneck model.

# 11. Broader Implication

If supported, civilisational topology can perform more than structural gap detection.

It can potentially answer:

- what is missing;
- where the missing capability belongs;
- which system is underdeveloped;
- what other systems depend upon it;
- which upstream development has the greatest downstream leverage;
- and what order of development should be tested next.

This would turn the maturity map into a **dependency-aware civilisational development planner**.

This remains a prospective, falsifiable finding.
