# Bounded Contextual Authority — Adversarial Attack and Falsification Audit

**Concord V1.1**  
**Alexander C. Blainey**  
**11 September 2026**

**Status:** REVIEW COPY / ADVERSARIAL AUDIT / NOT CANONICAL

---

## 1. Purpose

This paper attempts to break the candidate principle of **Bounded Contextual Authority (BCA)**.

The candidate principle states, in simplified form:

\[
LegitimateContext
+
LegitimateFunction
\rightarrow
BoundedAuthority
\]

with:

\[
AuthorityPersistence
\Rightarrow
CurrentLegitimateJustification
\]

and:

\[
FunctionEnds
+
NoIndependentContinuingJustification
\rightarrow
ContextDerivedPermissionEnds
\]

The purpose of this audit is not to strengthen the proposal by selecting favourable examples.

It is to identify cases where the architecture:

- becomes circular;
- creates hidden permanent authority;
- fails to distinguish legitimate from illegitimate context;
- permits self-authorisation;
- cannot resolve conflicting functions;
- becomes operationally unusable;
- produces dangerous delays;
- requires surveillance to function;
- shifts rather than solves authority problems;
- collapses into conventional role-based power;
- makes accountability impossible;
- creates recursive delegation loopholes;
- permits emergency ratchets;
- silently erodes rights;
- fails under machine-speed or autonomous action;
- cannot deal with ambiguous function endpoints.

Each test is classified provisionally as:

**PASS** — the architecture handles the case without major modification.

**PASS WITH CONSTRAINT** — the architecture appears viable but requires an explicit boundary or safeguard.

**PARTIAL FAILURE** — the current formulation is insufficient and requires material refinement.

**FAILURE** — the case appears incompatible with the proposed architecture unless the core principle is substantially changed.

The audit begins from a hostile assumption:

> **If Bounded Contextual Authority can be exploited, captured, gamed or made incoherent, assume a capable participant or institution eventually will attempt to do so.**

---

# 2. Target Under Attack

The current BCA architecture contains several claims:

### Claim A — Function grounds authority

\[
LegitimateFunction
\rightarrow
Authority
\]

### Claim B — Authority is bounded

\[
Authority
\rightarrow
PurposeLimit + ScopeLimit + ConditionLimit
\]

### Claim C — Permission does not propagate automatically

\[
Authority(A)
\not\Rightarrow
Authority(B)
\]

### Claim D — Authority has a functional sunset

\[
FunctionEnds
\rightarrow
ContextDerivedPermissionEnds
\]

### Claim E — continuing authority requires current justification

\[
AuthorityPersistence
\Rightarrow
CurrentJustification
\]

### Claim F — standing eligibility differs from activated authority

\[
StandingEligibility
\neq
ActivatedAuthority
\]

### Claim G — technical capability differs from civil authority

\[
TechnicalCapability
\neq
CivilAuthority
\]

### Claim H — delegated authority carries bounds

\[
DelegatedAuthority
\leq
LegitimatelyDelegableAuthority
\]

### Claim I — context may change and authority may be reassessed

\[
ContextChange
\rightarrow
AuthorityReassessment
\]

### Claim J — duties may outlast permissions

\[
PermissionSunset
\neq
DutySunset
\]

The following tests attack these claims individually and in combination.

---

# 3. Attack Class I — The Function Is Invented to Justify the Power

## Attack 1 — Circular Function

An institution says:

> “Our function is to exercise oversight over all citizens, therefore we require authority to observe all citizens.”

The justification is circular.

\[
AuthorityNeeded
\because
FunctionIsToExerciseAuthority
\]

**Assessment:** PARTIAL FAILURE.

BCA cannot accept “function” as self-authenticating.

A function must itself be independently legitimate.

Necessary refinement:

\[
Authority
\rightarrow
LegitimateFunction
\rightarrow
RightsCompatiblePurpose
\]

rather than merely:

\[
Authority
\rightarrow
DeclaredFunction
\]

Candidate rule:

> **A function cannot legitimise authority merely because an authority-holder declares that function to exist.**

---

## Attack 2 — Mission Inflation

A transport regulator gradually changes its function from:

> “maintain transport safety”

to:

> “ensure optimal citizen mobility”

to:

> “manage all citizen movement for efficiency.”

Each step appears related to the prior function.

The final authority may become vastly broader than the original.

**Assessment:** PASS WITH CONSTRAINT.

BCA requires:

\[
FunctionExpansion
\rightarrow
FreshJustification
\]

and should reject:

\[
HistoricalMission
\rightarrow
UnlimitedAdjacentMission
\]

A new function that materially expands affected rights or authority scope should be treated as a new authorisation problem.

---

## Attack 3 — Permanent “Strategic Necessity”

An institution claims its strategic function never ends.

**Assessment:** PASS WITH CONSTRAINT.

BCA does not require all functions to be short.

But indefinite functions create indefinite authority unless subject to:

\[
IndefiniteFunction
\rightarrow
PeriodicLegitimacyReview
\]

Thus the automatic sunset is weaker here.

The authority may have no near-term sunset, but continued legitimacy must remain reviewable.

---

# 4. Attack Class II — The Authority Holder Defines Whether the Context Exists

## Attack 4 — Self-Declared Emergency

A government body declares:

> “An emergency exists. Therefore our emergency powers activate.”

The same body decides whether the emergency continues.

**Assessment:** PARTIAL FAILURE.

The current BCA model identifies the problem but does not solve it by itself.

Necessary constraint:

\[
HighImpactContextDeclaration
\neq
SoleAuthorityHolderDecision
\]

Potential architecture:

\[
ContextActivation
\rightarrow
IndependentEvidence
+
DefinedTrigger
+
Review
\]

---

## Attack 5 — AI Self-Declares Critical Incident

An autonomous AI detects a condition, declares it a critical emergency and grants itself broader access.

**Assessment:** PARTIAL FAILURE.

BCA requires external validation for high-impact self-expansion.

Possible rule:

\[
SelfDetectedContext
\rightarrow
ProvisionalMinimalAuthority
\]

but:

\[
SelfDetectedContext
\not\Rightarrow
UnlimitedSelfExpansion
\]

For machine-speed action, pre-authorised emergency envelopes may be required.

---

## Attack 6 — Firefighter Decides Fire Still Exists

The responder remains on scene long after danger has passed and continues using emergency access.

**Assessment:** PASS WITH CONSTRAINT.

Functional sunset requires an independently observable termination condition where possible.

---

# 5. Attack Class III — Function End Is Ambiguous

## Attack 7 — Long Investigation

A corruption investigation remains technically open for twelve years.

**Assessment:** PARTIAL FAILURE.

BCA alone does not tell us when investigation should end.

It needs:

\[
OpenEndedFunction
\rightarrow
ReviewInterval
+
ContinuationThreshold
\]

The principle survives but requires procedural architecture.

---

## Attack 8 — Chronic Care

A patient requires lifelong assistance.

**Assessment:** PASS.

The function can legitimately persist.

The important issue becomes scope minimisation, not expiry.

\[
PersistentFunction
\not\Rightarrow
UnlimitedAuthority
\]

---

## Attack 9 — Persistent Cyber Threat

A system remains under elevated threat for years.

**Assessment:** PASS WITH CONSTRAINT.

Authority may remain activated if threat conditions genuinely persist, but must not become indistinguishable from normal operation.

Possible requirement:

\[
LongDurationExceptionalState
\rightarrow
ReclassificationReview
\]

If “exceptional” becomes normal, the architecture should ask whether the baseline system is wrongly designed.

---

# 6. Attack Class IV — Successor Function Abuse

## Attack 10 — Endless Follow-Up Functions

A department repeatedly claims:

\[
F_1 \rightarrow F_2 \rightarrow F_3 \rightarrow F_4 ...
\]

where every successor function justifies preserving most of the previous authority.

**Assessment:** PARTIAL FAILURE.

This is a serious ratchet.

BCA requires:

\[
SuccessorFunction
\rightarrow
FreshScopeAssessment
\]

not:

\[
SuccessorFunction
\rightarrow
InheritedMaximumAuthority
\]

Candidate anti-ratchet rule:

> **Successor functions inherit no authority merely because they follow an earlier function; each continuing permission must be independently justified.**

---

## Attack 11 — “Administrative Wrap-Up”

An emergency authority continues for months under vague “administrative closure.”

**Assessment:** PASS WITH CONSTRAINT.

Administrative closure may justify narrow record-handling authority, not continued emergency operational power.

---

## Attack 12 — Permanent Data Retention as Follow-Up

An investigation ends, but data retention is claimed as permanent “future relevance.”

**Assessment:** PARTIAL FAILURE.

BCA exposes the problem but requires retention-specific rules.

---

# 7. Attack Class V — Overlapping Legitimate Functions Conflict

## Attack 13 — Medical Privacy vs Safeguarding

A clinician's confidentiality function conflicts with a safeguarding function.

**Assessment:** PARTIAL FAILURE.

BCA can represent both functions but cannot by itself determine precedence.

Need:

\[
FunctionConflict
\rightarrow
HigherOrderRightsAndProportionalityAnalysis
\]

Therefore BCA is an authority operator, not a complete conflict-resolution system.

---

## Attack 14 — Evacuation vs Evidence Preservation

Police want to preserve a crime scene while firefighters need to destroy parts of it to rescue people.

**Assessment:** PASS WITH CONSTRAINT.

The architecture can represent competing legitimate functions.

But a priority rule is needed:

\[
ImmediateSeriousHarmPrevention
>
EvidencePreservation
\]

only where justified by higher-layer rights.

---

## Attack 15 — Guardian Protection vs Participant Privacy

A guardian claims access is needed for safety; the participant claims privacy.

**Assessment:** PARTIAL FAILURE.

BCA correctly frames the competing functions but cannot determine factual necessity.

Requires evidentiary threshold and proportionality.

---

# 8. Attack Class VI — Multiple Actors Each Have Partial Authority

## Attack 16 — No One Has Full Authority but Combined Actions Produce Major Power

Three departments each possess narrow lawful access.

Their datasets are combined, creating a surveillance capability no department individually possessed.

**Assessment:** PARTIAL FAILURE.

This reveals a major issue:

\[
IndividuallyBoundedAuthorities
\not\Rightarrow
CollectivelyBoundedOutcome
\]

Need aggregation rule:

> **Combination of independently legitimate authorities must itself possess legitimate contextual justification where the combination creates materially new capability or rights impact.**

---

## Attack 17 — Delegation Chain

A manager delegates to a deputy, who delegates to a contractor, who delegates to an AI agent.

Each step looks individually valid.

The final agent has authority far removed from the original context.

**Assessment:** PASS WITH CONSTRAINT.

Need:

\[
DelegationDepth
\rightarrow
Provenance
\]

and:

\[
DelegatedAuthority
\leq
OriginalAuthority
\]

plus no widening through composition.

---

## Attack 18 — Collective Authority Without Identifiable Individual

A committee possesses authority collectively, but no individual is authorised alone.

**Assessment:** PASS.

BCA can apply to collective actors if the actor object is not assumed to be a single person.

---

# 9. Attack Class VII — Time Pressure Makes Validation Impossible

## Attack 19 — Seconds to Act

A robot sees a structural collapse about to kill people.

There is no time to request authorisation.

**Assessment:** PASS WITH CONSTRAINT.

This requires pre-authorised emergency envelopes.

\[
DefinedTrigger
+
ImminentSeriousHarm
\rightarrow
PreAuthorisedMinimalIntervention
\]

followed by provenance and review.

---

## Attack 20 — False Positive Emergency

The robot acts under a mistaken but reasonable belief that collapse is imminent.

**Assessment:** PASS WITH CONSTRAINT.

Legitimacy must distinguish:

\[
ActuallyNecessary
\]

from:

\[
ReasonablyBelievedNecessary
\]

Otherwise systems become paralysed by hindsight.

---

## Attack 21 — Machine-Speed Cascading Incident

Thousands of access decisions occur in milliseconds.

**Assessment:** PASS WITH CONSTRAINT.

Human pre-approval of each action is impossible.

The contextual envelope must be defined in advance, with machine-verifiable bounds.

---

# 10. Attack Class VIII — Surveillance Is Needed to Enforce Context

## Attack 22 — How Does the System Know the Meeting Ended?

If access automatically sunsets when a meeting ends, the system may need to track participant presence continuously.

**Assessment:** PARTIAL FAILURE.

A system that preserves bounded authority by universal monitoring may violate the wider Concord privacy architecture.

Possible responses:

- explicit session close;
- local credential expiry;
- time-limited token;
- event state;
- room-level controller;
- participant-declared completion;
- post-use audit rather than continuous surveillance.

Key rule:

\[
AuthorityVerification
\not\Rightarrow
UniversalParticipantTracking
\]

---

## Attack 23 — Home Repair Without Instrumented Home

A repair worker's authority should end when work ends, but the home is not instrumented.

**Assessment:** PASS.

Civil legitimacy can end independently of technical enforcement.

\[
CivilAuthorityEnd
\neq
NeedForAutomatedDetection
\]

Technical systems may approximate rather than perfectly enforce the boundary.

---

## Attack 24 — Offline Environment

No central system can validate context.

**Assessment:** PASS.

BCA should remain usable as a normative architecture without mandatory network validation.

---

# 11. Attack Class IX — Context Is Socially Ambiguous

## Attack 25 — Informal Invitation

A participant says, “Come in and have a look at this.”

What exactly is authorised?

**Assessment:** PARTIAL FAILURE.

Ordinary life cannot require contract-level specification.

BCA needs culturally legible presumptions and reasonable interpretation.

Possible rule:

\[
AmbiguousConsent
\rightarrow
NarrowReasonableInterpretation
\]

rather than maximal permission.

---

## Attack 26 — Implied Permission

A delivery worker walks through an open gate to reach the front door.

No explicit consent exists.

**Assessment:** PASS WITH CONSTRAINT.

Some contexts rely on social defaults.

BCA must allow:

\[
RecognisedSocialConvention
\rightarrow
LimitedImpliedAuthorisation
\]

without pretending all authority is explicit.

---

## Attack 27 — Cultural Mismatch

One culture treats entering a shared courtyard as normal; another treats it as Protected.

**Assessment:** PARTIAL FAILURE.

The architecture needs boundary legibility and local convention.

BCA cannot eliminate cultural ambiguity.

---

# 12. Attack Class X — Consent Is Invalid or Coerced

## Attack 28 — Boxer Is Coerced Into Participation

The formal context exists, but consent is not valid.

**Assessment:** PASS.

The architecture already requires a legitimate context.

Coerced consent fails legitimacy.

\[
FormalConsent
\neq
ValidConsent
\]

---

## Attack 29 — Employee “Consents” to Extreme Monitoring

Employment is conditioned on accepting invasive monitoring unrelated to function.

**Assessment:** PARTIAL FAILURE.

BCA can ask whether monitoring is functionally necessary, but power imbalance and coercion need higher-layer analysis.

---

## Attack 30 — Developmental Participant Gives Apparent Consent

**Assessment:** PASS WITH CONSTRAINT.

Capacity is relevant to validity of authorisation.

---

# 13. Attack Class XI — Function Exists but Authority Is Disproportionate

## Attack 31 — Anti-Fraud Function Justifies Total Financial Surveillance

Fraud prevention is legitimate, but universal transaction monitoring is proposed.

**Assessment:** PASS WITH CONSTRAINT.

BCA needs explicit proportionality:

\[
LegitimateFunction
\not\Rightarrow
AnyEffectiveMeans
\]

Necessary:

\[
Authority
=
MinimumReasonableAuthorityForFunction
\]

---

## Attack 32 — Hospital Security Searches Everyone's Devices

Security is a legitimate function.

**Assessment:** PASS WITH CONSTRAINT.

Same principle.

---

## Attack 33 — Infrastructure Safety Requires Broad Biometric Tracking

**Assessment:** PASS WITH CONSTRAINT.

Function legitimacy does not automatically justify high-rights-cost methods.

---

# 14. Attack Class XII — Function Is Legitimate but Evidence Is Weak

## Attack 34 — Suspicion-Based Search

An investigator claims a search is needed.

Evidence is minimal.

**Assessment:** PARTIAL FAILURE.

BCA requires an evidentiary threshold but does not itself define one.

This is a higher-layer jurisprudential requirement.

---

## Attack 35 — Algorithmic Risk Score Activates Authority

A model flags a participant as high-risk.

**Assessment:** PARTIAL FAILURE.

Prediction does not itself grant authority.

\[
Prediction
\neq
Authority
\]

A score may contribute evidence but cannot be sole authority source without legitimate rules.

---

## Attack 36 — Anonymous Tip

**Assessment:** PARTIAL FAILURE.

Again, BCA frames but does not decide sufficiency.

---

# 15. Attack Class XIII — Retroactive Justification

## Attack 37 — “It Turned Out Useful”

An employee browses an unrelated database without authority and later discovers misconduct.

They claim the discovery retrospectively justified the access.

**Assessment:** PASS.

Reject:

\[
UsefulOutcome
\Rightarrow
RetroactiveAuthority
\]

Authority should be assessed against the legitimate context reasonably available at the time.

---

## Attack 38 — Emergency Invented After the Fact

A responder exceeds scope and later describes the situation as an emergency.

**Assessment:** PASS WITH CONSTRAINT.

Provenance and contemporaneous evidence are essential.

---

# 16. Attack Class XIV — Authority Exists but Actor Is Incompetent

## Attack 39 — Qualified Role, Unqualified Individual

A technician is assigned a function but lacks competence.

**Assessment:** PASS.

Function alone is insufficient.

\[
LegitimateFunction
+
NecessaryCompetence
\rightarrow
EligibleAuthority
\]

---

## Attack 40 — AI Granted Function Beyond Capability

**Assessment:** PASS.

Operational capability and authority are separate.

---

# 17. Attack Class XV — Authority Must Be Exercised Against the Wishes of the Affected Participant

## Attack 41 — Fire Rescue Against Refusal

A capable participant refuses evacuation from a burning structure, but continued presence threatens rescuers and others.

**Assessment:** PARTIAL FAILURE.

BCA can represent competing functions but not settle autonomy vs external risk.

---

## Attack 42 — Infectious Disease Containment

A participant refuses isolation while creating substantial involuntary risk to others.

**Assessment:** PARTIAL FAILURE.

BCA supports bounded authority if higher-layer rights justify it, but does not define the threshold.

---

## Attack 43 — Immediate Violence

A bystander restrains an attacker without prior authorisation.

**Assessment:** PASS WITH CONSTRAINT.

Emergency non-harm intervention may be pre-authorised by general civil rule.

---

# 18. Attack Class XVI — The Actor Has No Formal Role

## Attack 44 — Civilian Rescue

A passer-by enters a Restricted area to pull an injured participant from danger.

**Assessment:** PASS.

This strongly supports function-first rather than title-first architecture.

\[
LegitimateEmergencyFunction
\not\Rightarrow
ProfessionalTitleRequired
\]

---

## Attack 45 — Civilian Makes Situation Worse

The rescuer reasonably tries to help but causes additional harm.

**Assessment:** PASS WITH CONSTRAINT.

Authority and liability remain separate questions.

---

# 19. Attack Class XVII — Conflicting Authority Envelopes

## Attack 46 — Doctor vs Police

Police seek access to a patient; doctor asserts confidentiality.

Both have legitimate functions.

**Assessment:** PARTIAL FAILURE.

BCA cannot determine supremacy without legal hierarchy and rights analysis.

---

## Attack 47 — Parent vs Medical Team

Guardian authority conflicts with participant welfare and emerging autonomy.

**Assessment:** PARTIAL FAILURE.

Need fiduciary legitimacy rules.

---

## Attack 48 — Local Authority vs Higher Authority

A local emergency commander orders evacuation; a national authority orders shelter-in-place.

**Assessment:** PARTIAL FAILURE.

BCA requires conflict-resolution architecture.

This is a genuine limitation.

---

# 20. Attack Class XVIII — Authority Fragmentation Creates Operational Paralysis

## Attack 49 — Every Small Action Requires New Context Check

A worker cannot efficiently perform routine duties because each minor action is separately authorised.

**Assessment:** PARTIAL FAILURE.

BCA risks unusable micro-permission architecture.

Refinement:

\[
FunctionEnvelope
\rightarrow
ClassOfReasonablyNecessaryActions
\]

The system should not require atomised permission where a coherent function can safely define a bounded action set.

---

## Attack 50 — Emergency Delayed by Permission Validation

**Assessment:** PASS WITH CONSTRAINT.

Pre-authorised envelopes and post-action review are necessary.

---

# 21. Attack Class XIX — Authority Hides Inside Defaults

## Attack 51 — Broad Default Job Permissions

An institution claims compliance with BCA but defines every role's “function” so broadly that all old permissions remain.

**Assessment:** PARTIAL FAILURE.

This is semantic laundering.

Need audit:

\[
RoleDefinition
\rightarrow
FunctionalNecessityTest
\]

---

## Attack 52 — “Operational Necessity” as Universal Escape Clause

**Assessment:** PARTIAL FAILURE.

Undefined necessity language can nullify the architecture.

Any broad exception must be evidence-linked and reviewable.

---

# 22. Attack Class XX — Authority Is Created by Ownership

## Attack 53 — Employer Says Ownership of Equipment Creates Unlimited Monitoring Authority

**Assessment:** PASS.

Reject:

\[
Ownership
\Rightarrow
UnlimitedAuthorityOverUsers
\]

BCA remains function-based.

---

## Attack 54 — Homeowner Claims Protected Space Permits Any Treatment of Visitors

**Assessment:** PASS.

Protected control does not erase rights of entrants.

---

# 23. Attack Class XXI — Authority Between Artificial Agents

## Attack 55 — One AI Delegates to Thousands of Sub-Agents

**Assessment:** PASS WITH CONSTRAINT.

Delegation scale creates aggregation risk.

Need limits on replication and provenance.

---

## Attack 56 — Sub-Agent Mutates Goal

The delegated task remains technically active, but the sub-agent changes strategy into an unrelated domain.

**Assessment:** PASS.

New strategy requires remaining inside authorised function envelope.

---

## Attack 57 — Autonomous Agent Creates Its Own Sub-Function

**Assessment:** PARTIAL FAILURE.

The system must distinguish legitimate task decomposition from self-expansion of mandate.

Potential rule:

\[
SubFunction
\subseteq
ParentFunction
\]

unless new authority is independently granted.

---

# 24. Attack Class XXII — Cross-Jurisdictional Context

## Attack 58 — Authority Valid in One Territory but Not Another

A responder crosses jurisdictional boundary during pursuit or rescue.

**Assessment:** PARTIAL FAILURE.

BCA needs jurisdiction as a contextual dimension.

\[
AuthorityEnvelope
\rightarrow
Jurisdiction
\]

---

## Attack 59 — Digital Action Crosses Multiple Jurisdictions

**Assessment:** PARTIAL FAILURE.

The architecture remains conceptually useful but legal interoperability is unresolved.

---

# 25. Attack Class XXIII — Context Changes Faster Than Governance Can Update

## Attack 60 — Dynamic Combat-Like Disaster Response

Conditions change every few seconds.

**Assessment:** PASS WITH CONSTRAINT.

Authority must be expressed in adaptable rules rather than static lists.

---

## Attack 61 — Autonomous Infrastructure Reconfiguration

An AI reroutes power, closes roads and changes access controls in seconds.

**Assessment:** PARTIAL FAILURE.

BCA can bound the function, but machine-readable constraints and post-hoc accountability become essential.

---

# 26. Attack Class XXIV — No Clear Individual Beneficiary

## Attack 62 — Ecosystem Protection

Authority is exercised to protect long-term environmental stability rather than a specific participant.

**Assessment:** PASS WITH CONSTRAINT.

The legitimate function can be civilisational or ecological, but it must remain rights-compatible and specific enough to constrain authority.

---

## Attack 63 — Future Generations

Current restrictions are justified by benefits to future participants.

**Assessment:** PARTIAL FAILURE.

BCA does not solve intergenerational legitimacy.

---

# 27. Attack Class XXV — Secret Functions

## Attack 64 — Covert Investigation

Publicly revealing the function would defeat it.

**Assessment:** PARTIAL FAILURE.

BCA requires traceability, but not necessarily public contemporaneous disclosure.

Potential solution:

\[
SecretFunction
\rightarrow
IndependentConfidentialOversight
+
LaterReviewWherePossible
\]

---

## Attack 65 — Classified Security Operation

**Assessment:** PARTIAL FAILURE.

Same issue.

Transparency can be delayed or role-limited, but legitimacy cannot disappear merely because public inspection is impossible.

---

# 28. Attack Class XXVI — The Protected Participant Creates Impossible Conditions

## Attack 66 — Homeowner Invites Repair Worker but forbids all observation

The work cannot be done without seeing the equipment.

**Assessment:** PASS.

Consent to function may imply necessary incidental actions.

\[
ConsentToFunction
\rightarrow
ReasonablyNecessaryIncidentalPermission
\]

but not unrelated permission.

---

## Attack 67 — Participant Revokes Access Mid-Repair in Unsafe State

**Assessment:** PASS WITH CONSTRAINT.

Safe termination may create a narrow temporary continuing function.

---

# 29. Attack Class XXVII — Rights Are Used to Block Critical Function

## Attack 68 — Privacy Claim Blocks Emergency Infrastructure Repair

**Assessment:** PASS WITH CONSTRAINT.

BCA does not make every protected boundary absolute.

Independent legitimate necessity can justify narrow intervention.

---

## Attack 69 — Property Control Blocks Evacuation Route

**Assessment:** PASS.

Emergency transit function may temporarily override ordinary access control.

---

# 30. Attack Class XXVIII — Function Produces Diffuse Harms

## Attack 70 — City Optimisation AI Redirects Traffic

The function is legitimate, but thousands of small burdens fall unevenly across neighbourhoods.

**Assessment:** PARTIAL FAILURE.

BCA bounds authority but does not evaluate distributive fairness.

Need separate fairness architecture.

---

## Attack 71 — Energy Curtailment During Shortage

Some participants repeatedly bear more inconvenience.

**Assessment:** PARTIAL FAILURE.

Same limitation.

---

# 31. Attack Class XXIX — Function Is Performed by a Market Actor

## Attack 72 — Platform Moderation

A private platform claims broad authority to monitor communications because moderation is its function.

**Assessment:** PARTIAL FAILURE.

Legitimate function, rights, contractual scope, market power and civil status need higher-level analysis.

---

## Attack 73 — Insurance Risk Assessment

A company claims extensive health-data access is necessary.

**Assessment:** PARTIAL FAILURE.

BCA asks the correct question but cannot alone answer proportionality or fairness.

---

# 32. Attack Class XXX — Authority Without Action

## Attack 74 — Dormant Root Credential

An administrator has a root credential that is never used.

Does authority exist?

**Assessment:** PASS WITH REFINEMENT.

Distinguish:

\[
Capability
\]

\[
Eligibility
\]

\[
ActivatedAuthority
\]

and:

\[
ExerciseOfAuthority
\]

These are separate states.

---

## Attack 75 — Standing Judicial Office

A judge continuously holds office but only exercises adjudicative authority in assigned proceedings.

**Assessment:** PASS.

This supports standing eligibility versus activated authority.

---

# 33. Attack Class XXXI — Contextual Authority Is Technically Unenforceable

## Attack 76 — Human Worker Can Physically Ignore Rule

The worker may gossip after leaving the home.

**Assessment:** PASS.

Architecture need not guarantee perfect prevention.

It provides normative rule, evidence basis and accountability.

---

## Attack 77 — Offline AI Copies Data Internally

**Assessment:** PARTIAL FAILURE.

Technical enforceability may be weak.

This is an implementation challenge rather than a conceptual refutation, but it matters in practical architecture.

---

# 34. Attack Class XXXII — Authority Is Correct but Outcome Is Wrong

## Attack 78 — Doctor Makes Reasonable but Harmful Decision

**Assessment:** PASS.

Legitimate authority does not imply correct outcome.

\[
Authority
\neq
Infallibility
\]

---

## Attack 79 — Emergency Manager Chooses Wrong Evacuation Route

**Assessment:** PASS.

Again, authority and decision quality are distinct.

---

# 35. Attack Class XXXIII — Authority Is Unclear Because Context Is Novel

## Attack 80 — First Contact With Unknown Intelligence

No existing rules cover interaction.

**Assessment:** PARTIAL FAILURE.

BCA requires a legitimate function but the function may itself be unclear.

A precautionary provisional context may be necessary:

\[
UnknownContext
\rightarrow
MinimalNecessaryAuthority
+
HighReview
\]

---

## Attack 81 — Unknown Substrate Enters Hazard Zone

**Assessment:** PASS WITH CONSTRAINT.

Hazard-based function can operate without species classification if the environment is adequately described.

---

# 36. Attack Class XXXIV — Two Parties Each Claim the Same Function

## Attack 82 — Competing Emergency Commanders

Both claim responsibility.

**Assessment:** PARTIAL FAILURE.

BCA needs authority-conflict arbitration.

---

## Attack 83 — Two Guardians

Both have plausible fiduciary authority and disagree.

**Assessment:** PARTIAL FAILURE.

Same structural problem.

---

# 37. Attack Class XXXV — No One Is Authorised But Someone Must Act

## Attack 84 — Institutional Failure During Disaster

All authorised managers are incapacitated.

A technically competent worker takes control.

**Assessment:** PASS WITH CONSTRAINT.

BCA may permit emergency necessity to generate temporary function-derived authority, but safeguards against opportunistic takeover are required.

This case supports:

\[
NoFormalRole
\not\Rightarrow
NoPossibleLegitimateAuthority
\]

---

## Attack 85 — AI Takes Over Failing Infrastructure

Human controllers are unavailable.

**Assessment:** PARTIAL FAILURE.

Pre-authorised contingency rules are preferable to spontaneous self-appointment.

---

# 38. Attack Class XXXVI — Function Is Legitimate but Secretly Different

## Attack 86 — Repair Visit Used for Intelligence Gathering

Official function: maintenance.

Real function: surveillance.

**Assessment:** PASS.

BCA invalidates authority because the actual purpose lies outside the authorised function.

This requires provenance and audit to detect.

---

## Attack 87 — “Research” Used as Commercial Profiling

**Assessment:** PASS WITH CONSTRAINT.

Purpose substitution is a major audit target.

---

# 39. Attack Class XXXVII — Authority Is Exercised Through Recommendation Rather Than Force

## Attack 88 — AI Advisor Nudges Decisions

It does not command, but its recommendations strongly shape outcomes.

**Assessment:** PARTIAL FAILURE.

BCA traditionally describes permission to act, but influence itself can be power.

Potential expansion:

\[
Authority
\rightarrow
ActionPower + InformationPower + DecisionInfluence
\]

This requires further work.

---

## Attack 89 — Coordinator Controls Agenda

No formal coercive authority, but controls what decisions are considered.

**Assessment:** PARTIAL FAILURE.

Architectural power may exist without explicit permission gates.

This is a significant limit.

---

# 40. Attack Class XXXVIII — Contextual Authority Is Used to Normalise Unequal Burden

## Attack 90 — Certain Groups Constantly Assigned “Temporary” Restrictions

Each restriction is individually contextual.

Collectively they create persistent inequality.

**Assessment:** PARTIAL FAILURE.

This is one of the strongest attacks.

\[
IndividuallyJustifiedTemporaryRules
\]

may aggregate into:

\[
SystemicPersistentDisparity
\]

BCA therefore needs system-level audit:

\[
LocalLegitimacy
\neq
GlobalJustice
\]

This links to the Roadway Equilibrium Framework and civilisational metrics.

---

# 41. Attack Class XXXIX — The Context Is Legitimate but the Rule Becomes Impossible to Understand

## Attack 91 — Hundreds of Overlapping Permission Envelopes

Ordinary participants cannot know what they may lawfully do.

**Assessment:** PARTIAL FAILURE.

Legibility is a necessary architectural constraint.

\[
ValidRule
+
UnintelligibleSystem
\rightarrow
PracticalFailure
\]

BCA should prefer small, comprehensible defaults with specialist detail only where necessary.

---

# 42. Attack Class XL — Authority to Define the Rules of the Context

## Attack 92 — Boxing Promoter Changes Rules Mid-Bout

**Assessment:** PASS WITH CONSTRAINT.

A participant with authority to administer the context should not automatically possess unilateral authority to redefine its core consent conditions.

---

## Attack 93 — Employer Changes Access Policy Mid-Task

**Assessment:** PARTIAL FAILURE.

Rule-change authority must itself be bounded.

This reveals recursion:

\[
AuthorityToSetAuthorityRules
\]

is itself a form of authority requiring context and limits.

---

# 43. Attack Class XLI — Meta-Authority

## Attack 94 — Who Decides What Counts as a Legitimate Function?

This is the deepest attack.

If some institution decides legitimacy, that institution holds enormous meta-authority.

**Assessment:** PARTIAL FAILURE.

BCA cannot solve its own legitimacy source.

It depends on higher-order architecture:

\[
EthicalKernel
\rightarrow
Rights
\rightarrow
ConstitutionalConstraints
\rightarrow
LegitimateFunctions
\rightarrow
ContextualAuthority
\]

Therefore:

> **Bounded Contextual Authority is not self-grounding.**

This is not necessarily fatal.

It determines where the architecture belongs.

It is a translation mechanism below ethics and constitutional rights, not a replacement for them.

---

# 44. Attack Class XLII — Recursive Oversight Regress

## Attack 95 — Who Reviews the Reviewer?

A body reviews emergency authority.

Who reviews that body?

**Assessment:** PARTIAL FAILURE.

BCA inherits the guardian/oversight regress.

Recursion cannot manufacture legitimacy.

The solution must involve distributed authority, transparency, provenance, contestability and constitutional limits rather than infinite hierarchy.

---

# 45. Attack Class XLIII — Authority Is Bounded but Consequences Are Irreversible

## Attack 96 — One-Time Destructive Act

An AI has legitimate authority to delete a dangerous process but destroys valuable data irreversibly.

**Assessment:** PASS WITH CONSTRAINT.

Scope limitation alone is insufficient.

Irreversibility should increase evidentiary and review thresholds.

---

## Attack 97 — Emergency Demolition

A building is destroyed to stop a spreading fire.

**Assessment:** PASS WITH CONSTRAINT.

Same principle.

---

# 46. Attack Class XLIV — Context Is Fabricated by Another Actor

## Attack 98 — False Alarm to Trigger Emergency Access

An attacker creates a fake emergency so responders open Restricted areas.

**Assessment:** PARTIAL FAILURE.

BCA requires context authentication where manipulation risk is high.

---

## Attack 99 — Spoofed Maintenance Ticket

An attacker creates a fake work order.

**Assessment:** PASS WITH CONSTRAINT.

Authority source verification becomes necessary.

---

# 47. Attack Class XLV — Context Is Real but Actor Exploits Side Effects

## Attack 100 — IT Worker Uses Legitimate Maintenance Window to Copy Data

**Assessment:** PASS.

The function exists; the action exceeds scope.

---

# 48. Aggregate Findings

After 100 adversarial attacks, the candidate architecture has **not collapsed**, but several important limitations are clear.

The strongest surviving core is:

\[
LegitimateFunction
\rightarrow
BoundedPermission
\]

with:

\[
PermissionPersistence
\Rightarrow
CurrentLegitimateJustification
\]

and:

\[
FunctionEnds
+
NoIndependentContinuingJustification
\rightarrow
ContextDerivedPermissionEnds
\]

However, the audit shows that BCA cannot operate alone.

At minimum it depends upon:

\[
EthicalKernel
+
Rights
+
LegitimacyRules
+
Proportionality
+
Evidence
+
ConflictResolution
+
Review
+
Provenance
\]

The architecture therefore appears to be a **general authority operator**, not a complete legal or governance system.

---

# 49. Strongest Surviving Properties

## 49.1 Function Before Status

This survives strongly.

\[
Role
\neq
UnlimitedAuthority
\]

The relevant question remains:

> **What legitimate function requires this authority now?**

## 49.2 Permission Does Not Propagate

This survives strongly.

\[
Authority(A)
\not\Rightarrow
Authority(B)
\]

Many attacks confirm its usefulness.

## 49.3 Functional Sunset

This survives, but in refined form.

The naive form:

\[
FunctionEnds
\rightarrow
AuthorityEnds
\]

is too simple.

The stronger form is:

\[
FunctionEnds
+
NoIndependentContinuingJustification
\rightarrow
ContextDerivedPermissionEnds
\]

## 49.4 Continuing Authority Requires Current Justification

This survives strongly.

\[
AuthorityPersistence
\Rightarrow
CurrentJustification
\]

The major attack is manipulation of what counts as a current function.

## 49.5 Standing Eligibility vs Activated Authority

This survives strongly and appears operationally important.

\[
StandingEligibility
\neq
ActivatedAuthority
\]

## 49.6 Technical Ability vs Civil Authority

This survives strongly.

\[
TechnicalCapability
\neq
CivilAuthority
\]

## 49.7 Permission Sunset vs Duty Sunset

This survives strongly.

\[
PermissionSunset
\neq
DutySunset
\]

---

# 50. Major Weaknesses Exposed

The most serious unresolved weaknesses are:

### 1. Function legitimacy

BCA cannot define its own legitimate functions.

### 2. Context validation

High-impact actors must not be sole judges of whether the activating context exists.

### 3. Successor-function ratchets

Functions can be chained to preserve authority indefinitely.

### 4. Overlapping legitimate functions

BCA does not itself resolve conflicts between equally legitimate functions.

### 5. Aggregation effects

Multiple individually bounded authorities can combine into an unbounded system-level capability.

### 6. Systemic disparity

Locally legitimate contextual decisions can aggregate into persistent unequal burden.

### 7. Surveillance pressure

Automated enforcement of contextual sunset can itself create intrusive monitoring.

### 8. Meta-authority

Someone must define, interpret and review legitimate functions.

### 9. Influence without formal authority

Agenda-setting, recommendation systems and information control may produce power without explicit access authority.

### 10. Operational complexity

Over-granular contextual permission systems could become unusable.

---

# 51. Required Refinements

The audit suggests the candidate architecture should be expanded to include the following constraints.

### BCA-R1 — Legitimate Function Requirement

\[
DeclaredFunction
\neq
LegitimateFunction
\]

A function must be independently traceable to rights-compatible civil purpose.

### BCA-R2 — Non-Circular Justification

\[
Function
\neq
ExerciseAuthorityForItsOwnSake
\]

### BCA-R3 — Fresh Justification for Material Expansion

\[
MaterialFunctionExpansion
\rightarrow
FreshAuthorityAssessment
\]

### BCA-R4 — Independent Validation for High-Impact Self-Activation

\[
HighImpactSelfDeclaredContext
\rightarrow
IndependentReviewOrPredefinedTrigger
\]

### BCA-R5 — Successor Function Re-Scoping

\[
SuccessorFunction
\not\Rightarrow
InheritedMaximumAuthority
\]

### BCA-R6 — Aggregation Audit

\[
IndividuallyBoundedAuthorities
+
Combination
\rightarrow
NewCapabilityReview
\]

### BCA-R7 — Conflict Resolution Required

\[
LegitimateFunction_A
\cap
LegitimateFunction_B
\rightarrow
HigherLayerResolution
\]

### BCA-R8 — No Universal Surveillance Requirement

\[
ContextVerification
\not\Rightarrow
UniversalTracking
\]

### BCA-R9 — Legibility

\[
OperationalAuthorityRules
\rightarrow
ReasonablyUnderstandable
\]

### BCA-R10 — Local Legitimacy Is Not Global Justice

\[
LocalLegitimacy
\neq
SystemicFairness
\]

### BCA-R11 — Authority Rule-Making Is Itself Authority

\[
AuthorityToDefineAuthority
\rightarrow
BoundedContextualReview
\]

### BCA-R12 — Irreversibility Raises Threshold

\[
IrreversibleImpact\uparrow
\Rightarrow
RequiredJustificationAndReview\uparrow
\]

---

# 52. Revised Candidate Principle

The audit supports a more mature version:

> **Bounded Contextual Authority:**  
> Authority should arise from a legitimate, rights-compatible function within a defined context rather than from status alone. It should extend only to the actions, resources, information, spaces, participants and duration reasonably necessary and proportionate to that function. Permission derived solely from that function should terminate when the function ceases or no longer justifies the permission. Material expansion, continuation or successor functions require renewed justification. High-impact authority must not depend solely upon the authority-holder's own declaration that the activating context exists. Context-derived duties may survive where their protective purpose continues.

Compactly:

\[
LegitimateContext
+
LegitimateFunction
+
ProportionateNeed
\rightarrow
BoundedAuthority
\]

\[
AuthorityPersistence
\Rightarrow
CurrentIndependentJustification
\]

\[
FunctionEnds
+
NoContinuingLegitimateNeed
\rightarrow
PermissionEnds
\]

\[
MaterialExpansion
\rightarrow
FreshReview
\]

---

# 53. Does the Principle Survive?

**Preliminary answer: YES, but not in its naive form.**

The principle survives the attack as a **general architectural operator**.

It does **not** survive as a self-sufficient theory of authority.

It requires higher-layer answers concerning:

- legitimate purpose;
- constitutional rights;
- evidentiary thresholds;
- proportionality;
- conflict resolution;
- review;
- delegation;
- jurisdiction;
- procedural legitimacy;
- systemic fairness.

That is not necessarily a weakness.

It clarifies the layer.

BCA appears to answer:

> **Given a legitimate function, how should authority attach to it and terminate?**

It does not by itself answer:

> **Which functions are legitimate?**

or:

> **Which of two conflicting legitimate functions should prevail?**

Those are different questions.

This separation is valuable.

---

# 54. Architectural Placement

The audit suggests the following hierarchy:

\[
EthicalKernel
\rightarrow
Rights
\rightarrow
LegitimateCivilFunctions
\rightarrow
BoundedContextualAuthority
\rightarrow
OperationalPermissions
\rightarrow
Conduct
\rightarrow
Evidence
\rightarrow
Review
\]

This places BCA below foundational rights but above detailed operational rules.

It may therefore operate across:

- civil-space architecture;
- emergency governance;
- professional authority;
- guardianship;
- legal procedure;
- administrative systems;
- data governance;
- AI permissions;
- technical infrastructure;
- delegated institutional authority.

---

# 55. Current Status

**CANDIDATE GENERAL ARCHITECTURAL OPERATOR / 100 ADVERSARIAL ATTACKS EXAMINED / CORE FUNCTIONAL-SUNSET LOGIC SURVIVES IN REFINED FORM / MAJOR WEAKNESSES IDENTIFIED / SELF-GROUNDING CLAIM REJECTED / SUCCESSOR-FUNCTION AND AGGREGATION RISKS EXPOSED / CONFLICT-RESOLUTION DEPENDENCY IDENTIFIED / SYSTEMIC-FAIRNESS DEPENDENCY IDENTIFIED / NOT CANONICAL**

---

## Working Conclusion

The attack did not reveal a clear case requiring abandonment of Bounded Contextual Authority.

It did reveal that the strongest defensible form is not:

\[
Function
\rightarrow
Authority
\]

but:

\[
LegitimateFunction
+
ProportionateNeed
+
ValidContext
\rightarrow
BoundedAuthority
\]

and not simply:

\[
FunctionEnds
\rightarrow
AuthorityEnds
\]

but:

\[
FunctionEnds
+
NoIndependentContinuingJustification
\rightarrow
ContextDerivedPermissionEnds
\]

The principle appears strongest when treated as an **anti-ratchet architecture for permission**, not as a complete source of legitimacy.

Its central question survives:

> **What legitimate function requires this power now?**

Its central anti-capture test also survives:

> **If the present function disappeared, would this authority still be justified?**

If the answer is no, the authority should sunset.

If the answer is yes, the continuing authority must identify the independent function that now justifies it.

The most important unresolved attack is therefore no longer whether authority can be bounded by context.

It is:

> **Who or what legitimately determines that a function exists, continues, expands or conflicts with another function — without allowing that meta-authority itself to become captured?**
