# Participant Status, Record, Notification and Correction Loop 001

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / PROVISIONAL CROSS-SYSTEM INTEGRATION / NON-CANONICAL  
**Date:** September 2026

---

# 1. Purpose

Recent participation development has exposed a cross-system requirement:

A participant's status, qualification, entitlement or restriction should not merely be calculated.

The participant must be able to:
- be informed of a consequential change;
- inspect the consequential record;
- understand its meaningful basis;
- contest error or interpretation;
- obtain review;
- correct the record where justified;
- have correction propagate to dependent eligibility;
- receive notice of the corrected consequence.

This document tests whether existing Concord architecture already provides the required components and defines their provisional interface.

---

# 2. Source-resolved components

Existing Concord work already supplies most of the necessary functions.

## Status / eligibility-producing systems

Participation, Education, Health, Economy, Governance, Civil Security, Judiciary and other domains may create or maintain participant-specific states within their legitimate authority.

## Historical

Historical provides:
- temporal custody;
- participant record linkage;
- provenance;
- prior/current state relationships;
- correction relationships;
- lifecycle reconstruction;
- bounded access architecture.

Historical does not become the operational authority that made the original decision.

## Civil Contact Point

Civil Contact provides:
- official participant-facing routing;
- consequential notification;
- stable communication relationship.

Existing CH003 testing identified that Civil Contact should not itself become the final authority for all consequential administrative decisions.

## Civil Historical Access Point

The newly developed interface provides participant access to the coherent civil record while preserving domain safe spaces and legitimate redactions.

## Metrics and State Observation

Existing personal-data architecture provides:
- participant access to consequential personal data/models;
- contextualisation;
- contestation;
- correction;
- meta-metrics concerning system reliability.

## Judiciary

Existing Judiciary architecture provides:
- challenge to exercises of power;
- administrative/legal/constitutional dispute handling;
- review;
- remedies;
- correction;
- escalation where administrative resolution is inadequate.

---

# 3. The complete provisional loop

The cross-system participant loop is:

**1. Authorised Domain Event / Assessment**
↓
**2. Participant State or Record Changes**
↓
**3. Historical Provenance / Current-State Relationship Preserved**
↓
**4. Dependent Eligibility / Entitlement Recalculated**
↓
**5. Civil Contact Point Notifies Participant**
↓
**6. Civil Historical Access Point Exposes Consequential Record**
↓
**7. Participant Accepts / Contextualises / Contests**
↓
**8. Responsible Domain Performs Administrative Review**
↓
**9. Judiciary / Other Independent Review Available Where Required**
↓
**10. Record Corrected / Confirmed / Qualified**
↓
**11. Correction Propagates to Known Dependent Decisions**
↓
**12. Eligibility / Entitlement Recalculated**
↓
**13. Civil Contact Point Communicates Result**
↓
**14. Historical Preserves the correction relationship and provenance**

This is a loop, not a one-time pipeline.

---

# 4. The participant should not have to find the responsible institution

Civil Contact and Civil Historical Access should reduce institutional-navigation burden.

A participant should be able to say, in substance:

> **This status or record about me is wrong.**

The civilisation should determine:
- which domain owns the record;
- which authority made the decision;
- which review process applies;
- whether another dependent record must also be examined.

The participant should not need to understand Concord's internal organisational topology merely to correct their own civil state.

> **The Participant Identifies the Problem; Concord Routes the Correction.**

This extends the Civil Attention principle:

> **Tell the Concord once.**

---

# 5. Record correction and decision correction are different

A participant may challenge:

## Recorded fact
Example: a qualification is incorrectly shown as expired.

## Interpretation
Example: correct data is interpreted as demonstrating ineligibility when it does not.

## Rule application
Example: the correct eligibility rule is applied to the wrong participant category.

## Underlying rule or authority
Example: the participant argues that the rule itself exceeds legitimate authority or violates protected rights.

Different challenges require different routes.

Therefore:

**Data Correction != Administrative Review != Judicial Review != Constitutional Challenge**

but the participant-facing architecture should route among them.

---

# 6. Correction must propagate

Correcting the source record is insufficient if downstream systems continue to act on the old state.

Example:

**Incorrect Education Record**
→ participant denied trusted employment
→ Education record corrected
→ employment eligibility remains denied because cached eligibility was not updated.

This is a failed correction.

The required pattern is:

**Source Correction**
→ **Known Dependency Identification**
→ **Affected Derived States Recalculated**
→ **Stale Consequences Withdrawn / Corrected**
→ **Participant Notified**
→ **Historical Provenance Preserved**

> **Correction Without Propagation != Complete Correction.**

---

# 7. Historical does not become the correction authority

Historical may know:
- what was recorded;
- what changed;
- what provenance exists;
- what correction relationship applies.

It should not decide:
- whether a clinical diagnosis is correct;
- whether an educational qualification should be awarded;
- whether a security restriction is justified;
- whether a participant should receive a benefit;
- whether a criminal finding should be overturned.

Those remain with the legitimate originating/review authority.

> **Record Custody != Decision Authority.**

---

# 8. Civil Contact does not become the decision authority

Civil Contact communicates.

It should not silently become the institution that decides:
- citizenship;
- participation progression;
- benefit eligibility;
- criminal restriction;
- qualification;
- healthcare entitlement.

It may display and route those states.

> **Communication Interface != Sovereign Administrative Authority.**

---

# 9. Meaningful explanation

For consequential changes, notification should ordinarily identify:
- what changed;
- effective date/state;
- practical consequence;
- substantive reason sufficient for understanding;
- relevant record location;
- whether action is required;
- challenge/correction route;
- sunset/review date where relevant;
- missing prerequisite where applicable.

Security/operational detail may be redacted according to the Civil Historical Access architecture.

A participant should not receive only:

> **Denied.**

where Concord can safely explain:

> **You currently lack prerequisite X. Complete or demonstrate X through route Y, or challenge the record if it is incorrect.**

---

# 10. Automatic recalculation

Where relevant inputs are legitimately machine-readable, status and eligibility should be recalculated after:
- qualification completion;
- participation progression;
- restriction expiry;
- rehabilitation evidence;
- correction of a record;
- restored credential;
- citizenship/status change;
- other recognised eligibility event.

The participant should not need to reapply merely because Concord failed to recompute a consequence of information it already possesses.

> **Known Correction Should Trigger Known Consequence Reassessment.**

---

# 11. Correction of adverse historical states

Historical provenance means an old adverse state may remain historically reconstructable.

It must not therefore remain operationally current.

The record should distinguish:
- historical state;
- disputed state;
- corrected state;
- superseded state;
- current accepted state;
- sealed/spent state where applicable.

This is especially important for:
- criminal records;
- trust restrictions;
- participation restrictions;
- professional qualification;
- health classifications;
- benefit eligibility.

> **Historically True Once != Operationally Current Now.**

---

# 12. Restricted records and challenge

Security-sensitive information creates a difficult case.

A participant may be unable to inspect every detail of evidence or method.

But where the hidden information materially affects them, the architecture should still preserve:
- a meaningful participant-facing explanation where safely possible;
- independent review;
- provenance;
- proportional secrecy;
- sunset/review of secrecy where applicable.

The participant should not be forced to defeat a secret operational system in order to challenge a consequential error.

Independent review may sometimes need access to material the participant cannot directly inspect.

---

# 13. Meta-learning

Existing Metrics architecture establishes that participant challenges can reveal system-level failure.

If many participants successfully challenge the same:
- qualification inference;
- status rule;
- metric;
- eligibility decision;
- administrative process,

that pattern should become evidence about the system itself.

Thus:

**Individual Correction**
→ **Aggregate Correction Pattern**
→ **System Reliability Signal**
→ **Research / Audit / Governance Attention**
→ **Potential Structural Correction**

This allows participant record correction to contribute to recursive civilisational learning without exposing unnecessary identifiable data.

---

# 14. Provisional interface ownership

| Function | Provisional owner/interface |
|---|---|
| Create operational state | Authorised originating domain/system |
| Preserve state/provenance through time | Historical |
| Calculate eligibility | Relevant authorised domain/cross-domain eligibility function — final ownership unresolved |
| Notify participant | Civil Contact Point |
| Participant record access | Civil Historical Access Point |
| Context/contest personal data | Participant + originating data system |
| Administrative review | Responsible originating/administrative authority |
| Independent legal/constitutional escalation | Judiciary |
| Propagate known correction | Dependency/change-propagation architecture — exact implementation unresolved |
| Audit repeated correction patterns | Metrics / Research / relevant oversight |
| Preserve correction history | Historical |

This table defines interfaces, not final institutional ownership.

---

# 15. Remaining gap

Most component functions already exist.

The principal unresolved operational gap is now:

> **What system owns cross-domain eligibility computation and correction propagation?**

Historical should not own it.

Civil Contact should not own it.

Individual domains cannot safely assume they know every downstream dependency.

Existing KCS/dependency/change-propagation architecture may already provide part of the answer and should be source-resolved before creating a new system.

This is the next dependency.

---

# 16. Provisional synthesis

The Concord should not merely maintain records about participants.

It should maintain a **contestable civil relationship** between participant and record:

**Concord records participant**
↔
**Participant inspects Concord's record**
↔
**Participant can challenge error**
↔
**Concord corrects legitimate error**
↔
**Consequences update**
↔
**History preserves what happened**

The participant is therefore neither the sole author of their civil record nor a passive object inside it.

> **Civilisation Can Record the Participant; the Participant Can Inspect and Correct Civilisation's Record of Them.**

> **Correction Without Propagation != Complete Correction.**

> **The Participant Identifies the Problem; Concord Routes the Correction.**
