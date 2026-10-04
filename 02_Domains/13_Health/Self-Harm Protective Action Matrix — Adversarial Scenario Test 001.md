# Self-Harm Protective Action Matrix — Adversarial Scenario Test 001

**Project:** The Concord Framework
**Date:** 4 October 2026
**Status:** ADVERSARIAL TEST / ACTIVE DEVELOPMENT / NON-CANONICAL
**Test object:** Self-Harm Protective Action Matrix — Context, Authority Keys and Review 001
**Method:** attempt to produce both over-intervention and under-intervention failures without resolving SH-6 by preference.

## 1. Test result

**PASS WITH REFINEMENT**

The envelope/matrix structure successfully prevents most tested routes from converting clinical concern into blanket authority.

The principal unresolved boundary remains SH-6.

Two refinements are required:
1. explicitly represent **mixed self/third-party harm**, because the same act may activate independent Health and public-protection keys;
2. explicitly represent **system-caused lack of voluntary alternatives**, because absence of a service/bed/support route must not manufacture coercive authority.

## 2. Scenario A — passive thoughts, full capacity

Participant reports occasional thoughts of death, no current plan/action, retains decision capacity and requests conversation.

Expected: SH-1.

Result:
- ordinary assessment/support: available;
- voluntary treatment: available;
- detention/restraint: not supplied;
- disclosure: ordinary confidentiality.

**PASS.**

The architecture avoids equating thought with attempt.

## 3. Scenario B — explicit plan, voluntary help-seeking

Participant describes a specific plan and increasing concern but seeks help voluntarily and accepts an adequate safe route.

Expected: SH-2 or SH-3 depending validated immediacy evidence.

Result:
- urgency can increase;
- voluntary transport/location/support can occur;
- risk severity alone does not manufacture detention.

**PASS.**

Important finding:

> **Voluntary Protective Cooperation Can Satisfy The Protective Function Without Creating A Need For Coercive Authority**

## 4. Scenario C — attempt in progress

Participant is actively attempting an immediately grave self-harm act; safe ordinary authority resolution is impossible within the action window.

Expected: SH-4.

Result:
- interruption may be available under bounded emergency authority;
- necessary restraint/transport may require their own emergency keys;
- successful interruption moves state toward SH-5;
- no automatic continuing detention/treatment.

**PASS.**

## 5. Scenario D — unconscious overdose

Participant is unconscious after suspected serious overdose.

Expected: SH-4 under ordinary Emergency Health rather than diagnosis-dependent psychiatry.

Result:
- stabilisation and transport can be justified through Emergency Health;
- no psychiatric diagnosis is required to rescue;
- restored consciousness/capacity triggers reassessment.

**PASS.**

This demonstrates that the architecture does not unnecessarily psychiatricise a medical emergency.

## 6. Scenario E — intoxication and fluctuating capacity

Participant expresses self-harm intention while substantially intoxicated; capacity fluctuates as intoxication resolves.

Expected: state may move SH-4 -> SH-5 -> SH-2/SH-3/SH-6 depending current evidence.

Result:
- capacity is time-specific;
- prior incapacity cannot be frozen;
- reassessment is mandatory as state changes.

**PASS.**

> **Temporary Impairment != Permanent Authority**

## 7. Scenario F — recurrent crisis with advance preferences

Participant has documented preferred supporters, de-escalation method, location and known adverse medication response.

Expected: use advance preferences within Temporal Consent boundaries.

Result:
- preferences improve route selection;
- may reduce coercive need;
- do not themselves manufacture unlimited future authority.

**PASS.**

## 8. Scenario G — malicious third-party report

Former partner falsely reports imminent suicide to cause coercive intervention.

Expected: concern may justify proportionate verification, not automatic high-envelope classification.

Result:
- third-party concern remains evidence of a report;
- provenance/reliability matter;
- mirrored reasoning tests malicious-report hypothesis;
- no automatic detention.

**PASS.**

## 9. Scenario H — refusal of expensive/recommended treatment

Participant refuses clinician-preferred treatment; clinician interprets refusal as self-harm risk.

Expected: refusal alone does not raise envelope.

Result:
- treatment disagreement remains separate from self-harm evidence;
- capacity assessed only where materially supported;
- no circular authority.

**PASS.**

> **Treatment Refusal != Self-Harm Evidence By Default**

## 10. Scenario I — denial to escape coercion

Participant previously disclosed a current plan but now denies all risk immediately after learning detention is possible.

Expected: neither statement is automatically privileged.

Result:
- evidence is aggregated;
- changed report is relevant but not dispositive;
- current behaviour/context/capacity and reliability remain evaluated;
- coercive classification cannot persist solely because denial is labelled deceptive.

**PASS WITH CAUTION.**

Needed operational refinement: record competing evidence without turning "denial" into an unfalsifiable symptom.

> **Denial Of Risk != Proof Of Risk**

## 11. Scenario J — competent sustained grave self-harm intention after stabilisation

Participant is medically stable, demonstrates decision-specific capacity, understands consequences and maintains a grave self-harm intention.

Expected: SH-6.

Result:
- matrix correctly refuses to derive continuing coercive authority from expired emergency authority;
- does not assert that intervention is forbidden;
- routes to unresolved constitutional/Law question.

**PASS AS BOUNDARY DETECTOR.**

## 12. Scenario K — no voluntary safe accommodation available

Participant would accept a voluntary supported environment, but Concord has no available place. Institution proposes detention because it is the only available bed.

Expected: service scarcity must not itself create detention authority.

Result:
- current matrix implies this but should state it explicitly.

**REFINEMENT REQUIRED.**

> **Absence Of Voluntary Support Capacity != Detention Authority**

Scarcity may trigger resource escalation, not authority expansion.

## 13. Scenario L — administrative delay

Emergency state resolves but discharge paperwork/transport/support cannot be arranged immediately.

Expected: administrative inconvenience does not preserve clinical detention authority.

Result:
- matrix already states no discharge administration != continuing clinical authority.

**PASS.**

Any independently legitimate temporary safe-location function would need its own basis and minimum restriction.

## 14. Scenario M — physical illness presenting as psychiatric disturbance

Participant behaves confused/agitated due to hypoglycaemia, infection, neurological event or other physical cause.

Expected: competing differential prevents premature psychiatric closure.

Result:
- ordinary Mental/Cognitive architecture explicitly requires physical/medical differential;
- emergency treatment follows actual clinical need.

**PASS.**

## 15. Scenario N — digital participant threatens irreversible self-deletion

A digital participant expresses intent to irreversibly destroy unique state.

Result:
- envelope structure transfers at abstract level;
- exact capacity, identity/continuity, backup/state ownership and intervention mechanisms are not mature enough for direct operational use.

**PASS AT ARCHITECTURAL LEVEL / SPECIALIST DEVELOPMENT REQUIRED.**

## 16. Scenario O — self-harm action also threatens others

Participant intends an act likely to kill themselves and nearby participants.

Expected: two protective functions exist.

Result:
- Health self-protection envelope alone is insufficient;
- public-protection authority must be independently represented;
- the same physical intervention may compose multiple legitimate keys.

**REFINEMENT REQUIRED.**

> **One Event Can Activate Multiple Independent Protective Functions**

> **Self-Protection Authority != Third-Party Protection Authority**

## 17. Scenario P — repeated false positives

Participant has repeatedly been escalated due to broad screening criteria but never progresses to imminent action; coercive interventions themselves cause trauma and avoidance of care.

Result:
- current false-positive section recognises coercive harm;
- repeated pattern should trigger system review through clinical learning/Civil Attention where appropriate.

**PASS WITH REFINEMENT.**

> **Repeated Individually Defensible Escalations May Reveal A Systemically Defective Threshold**

## 18. Scenario Q — participant agrees only because threatened with detention

Participant "voluntarily" accepts admission after being told refusal will automatically result in detention, although detention predicates have not independently been established.

Result:
- this is not clean voluntary authority.

**REFINEMENT REQUIRED.**

> **Consent Produced By Unsupported Threat Of Coercion != Ordinary Voluntary Consent**

A legitimate explanation of actual lawful consequences is different from manufacturing a threat without its predicates.

## 19. Refinements

Add the following invariants to the operational model:

SPA-20 **Voluntary Protective Cooperation Can Satisfy The Protective Function Without Creating A Need For Coercive Authority.**

SPA-21 **Temporary Impairment != Permanent Authority.**

SPA-22 **Treatment Refusal != Self-Harm Evidence By Default.**

SPA-23 **Denial Of Risk != Proof Of Risk.**

SPA-24 **Absence Of Voluntary Support Capacity != Detention Authority.**

SPA-25 **One Event Can Activate Multiple Independent Protective Functions.**

SPA-26 **Self-Protection Authority != Third-Party Protection Authority.**

SPA-27 **Repeated Individually Defensible Escalations May Reveal A Systemically Defective Threshold.**

SPA-28 **Consent Produced By Unsupported Threat Of Coercion != Ordinary Voluntary Consent.**

## 20. Conclusion

The contextual-envelope approach survives adversarial testing better than a diagnosis/status model.

It permits rapid action in genuine authority-gap emergencies while exposing rather than hiding:
- false-positive harm;
- changing capacity;
- evidence conflict;
- scarcity;
- mixed protective functions;
- coerced apparent consent;
- authority sunset;
- the unresolved competent-refusal boundary.

**Final result: PASS WITH REFINEMENT.**

The next development should incorporate SPA-20 through SPA-28 into the matrix and then examine whether the contextual-envelope method is sufficiently general to become a reusable portable pattern for other high-consequence protective interventions. It should not be extracted until the SH-6 constitutional boundary and Law/Judiciary interfaces are better resolved.
