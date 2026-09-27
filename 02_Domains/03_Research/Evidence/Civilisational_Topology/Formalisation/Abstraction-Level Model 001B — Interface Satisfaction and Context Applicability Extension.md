# Abstraction-Level Model 001B — Interface Satisfaction and Context Applicability Extension

**Status:** V1.2a FROZEN MODEL EXTENSION  
**Date:** September 2026  
**Canonical effect:** NONE  
**Parent:** Civilisational Abstraction-Level Completeness Model 001A  
**Trigger:** Abstraction-Level Audit 002

# 1. Problem

Audit 002 exposed two defects in a naive system-level AL measure.

First, later civil capabilities are deliberately distributed across legitimate system owners.

If every system had to internally implement every applicable higher-layer capability, AL measurement would reward duplication and contradict Developmental Topology.

Second, requirement applicability can change with deployment context.

A portable method may legitimately exercise no civil authority in one context while materially affecting participants in another.

The AL model therefore requires explicit interface-satisfaction and context-applicability rules.

# 2. Satisfaction Modes

For system S, requirement r, context c:

R(S,r,c) may be:

- SATISFIED-INTERNAL;
- SATISFIED-INTERFACE;
- NOT-APPLICABLE;
- UNSATISFIED;
- UNKNOWN;
- DISPUTED.

SATISFIED-INTERNAL and SATISFIED-INTERFACE both count toward layer completeness.

They must remain distinguishable.

# 3. Internal Satisfaction

SATISFIED-INTERNAL applies where:

- S legitimately owns the required function;
- the capability is present;
- evidence/provenance is sufficient for the audit claim.

Internal implementation is not automatically preferable.

# 4. Interface Satisfaction

SATISFIED-INTERFACE applies only where all of the following are sufficiently established:

I1 — a legitimate external owner O is identifiable;

I2 — O actually possesses the required capability at sufficient level;

I3 — S has an explicit or operationally sufficient interface to O for the required function;

I4 — scope and authority remain bounded;

I5 — the dependency is representable/provenance-visible;

I6 — failure/unavailability of O is not silently treated as continued satisfaction;

I7 — correction/review can propagate across the interface where materially required;

I8 — the interface does not create an unreviewable monopoly or hidden sovereignty.

Formally:

InterfaceSatisfied(S,r,O,c)
iff
Owner(O,r)
AND Capability(O,r)
AND SufficientInterface(S,O,r,c)
AND Bounded(O,S,r)
AND DependencyVisible(S,O,r)
AND FailureRepresentable(O,r)
AND CorrectionPropagatesWhereMaterial
AND Reviewable.

# 5. No Duplication Rule

If r is legitimately owned by O and sufficiently available to S through interface:

SATISFIED-INTERFACE(S,r,O)
NOT=> RequireDuplicateImplementation(S,r).

This preserves architectural specialisation.

# 6. Interface Failure Rule

If S depends on O for r but the interface is absent, inadequate, stale, disputed or unavailable:

R(S,r,c)=UNSATISFIED or UNKNOWN

according to evidence.

The existence of O alone is insufficient.

# 7. Owner Maturity Rule

If O is the legitimate owner but its capability is below the level required by S:

classify the requirement as a developmental dependency gap.

Do not:

- falsely mark S internally deficient;
- falsely mark the requirement satisfied;
- duplicate O inside S merely to raise S's AL.

# 8. Context Applicability

Applicability is evaluated as:

Applicable(r,S,c).

Context c may include:

- deployment domain;
- consequence class;
- participant exposure;
- authority exercised;
- scale;
- environment;
- substrate;
- operational versus experimental use.

# 9. Context-Specific N/A

NOT-APPLICABLE is valid only for the audited context.

Therefore:

N/A(r,S,c1)
NOT=> N/A(r,S,c2).

Example:

A private Reality Tree used by one researcher may not trigger participant standing requirements.

A Reality Tree used to structure a high-consequence civil pilot may trigger participant standing, review, provenance and remedy requirements.

# 10. Context-Specific AL

Where context materially changes triggered requirements, report:

A(S|c).

Do not silently collapse multiple deployment contexts into one scalar level.

A system may therefore have:

- base-method AL;
- operational-domain AL;
- high-consequence deployment AL.

# 11. Civilisational Floor With Interfaces

For required systems S_i operating in relevant contexts c_i:

L_C = min A(S_i|c_i).

Interface satisfaction permits distributed architecture to count as complete only when the required relation is actually available through legitimate interfaces.

Thus civilisational level measures **functional architectural completeness**, not self-contained duplication.

# 12. Interface Dependency and Floor Risk

A high-level shared owner can support many systems.

This creates efficiency but also concentration risk.

Therefore the State Map should record:

- shared owner;
- dependent systems;
- interface state;
- failure consequence;
- alternative/replacement path where required;
- last interface review.

High reuse does not imply sovereignty.

# 13. State Map Additions

For each AL requirement, CCSSL should be capable of recording:

- requirement ID;
- applicability context;
- satisfaction mode;
- internal owner if internal;
- external owner if interface;
- interface reference;
- evidence/provenance;
- dependency state;
- failure state;
- correction path;
- N/A rationale;
- audit state.

# 14. Audit Rule Update

Future audits must:

1. define context;
2. determine applicability;
3. identify legitimate owner;
4. test internal or interface satisfaction;
5. test owner maturity;
6. preserve Unknown/Disputed;
7. stop contiguous AL at first unresolved applicable requirement;
8. record higher feature exposure separately.

# 15. Prediction

If this extension is correct:

- Clock should be able to satisfy AL6 requirements through KMDI where the interface is sufficient without duplicating KMDI;
- specialised methods should avoid false penalties for authority functions not triggered in their audited context;
- participant-facing systems may gain some higher-layer completeness through legitimate Judiciary/Ratchet/KCS interfaces, but only where those interfaces are actually explicit/sufficient;
- the development graph should become more informative because AL deficits will distinguish local deficiency from upstream-owner/interface deficiency.

These predictions are frozen before retest.
