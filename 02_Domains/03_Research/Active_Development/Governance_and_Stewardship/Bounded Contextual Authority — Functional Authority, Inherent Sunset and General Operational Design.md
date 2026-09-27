# Bounded Contextual Authority — Functional Authority, Inherent Sunset and General Operational Design

**Concord V1.1**  
**Alexander C. Blainey**  
**11 September 2026**

**Status:** REVIEW COPY / ACTIVE DEVELOPMENT / CANDIDATE GENERAL ARCHITECTURAL PRINCIPLE / NOT CANONICAL

---

## 1. Purpose

Recent Concord work on boxing, civil-space classification, workers entering Protected homes, Restricted civic departments, emergency access and purpose-limited information has repeatedly produced the same structural pattern.

An action or access right that is ordinarily prohibited, restricted or permission-dependent may become legitimate because a specific context creates a legitimate function.

The authority produced by that context is not general.

It is bounded by the function that justifies it.

When the function ends, the authority appears to contain its own logical termination condition.

The emerging candidate is:

> **Bounded Contextual Authority: authority exists only to the extent required by a legitimate function within a valid context, and authority derived solely from that context terminates when the function or context that justified it terminates.**

The purpose of this paper is to:

1. define the candidate architecture;
2. distinguish it from role-based, status-based and permanent authority;
3. examine the apparent inherent sunset mechanism;
4. test it across civil, professional, emergency, legal, digital, computational and interpersonal cases;
5. identify where it fails, requires qualification or creates dangerous ambiguity;
6. determine whether it is strong enough to continue toward Layer 0 architectural development.

This is not yet a canonical Concordian principle.

It is a candidate requiring attempted falsification.

---

# 2. The Repeating Pattern

Several apparently unrelated cases share the same topology.

## 2.1 Boxing

A participant may ordinarily not strike another participant.

Within a valid boxing context, specified forms of physical contact become authorised.

\[
DefaultProhibition
+
ValidBout
+
Consent
+
Rules
\rightarrow
BoundedPermissionToStrike
\]

But:

\[
PermissionToPunch
\neq
PermissionToUseWeapon
\]

and:

\[
BoutEnds
\rightarrow
BoutDerivedPermissionEnds
\]

## 2.2 Routine Worker Access to a Protected Home

A worker ordinarily has no right to enter another participant's Protected home.

A gas-meter inspection, repair, maintenance visit or care function may create legitimate temporary access.

\[
ProtectedHome
+
ValidServiceFunction
\rightarrow
PurposeBoundedEntry
\]

But:

\[
PermissionToEnter
\neq
PermissionToSearchUnrelatedProperty
\]

and:

\[
ServiceFunctionEnds
\rightarrow
ServiceDerivedAccessEnds
\]

## 2.3 Emergency Worker Access

A firefighter ordinarily has no general authority to enter every home or Restricted facility.

A fire may create an emergency-response function requiring entry.

\[
EmergencyCondition
+
ResponseFunction
\rightarrow
TemporaryNecessaryAccess
\]

The emergency does not itself create unlimited authority.

\[
Emergency
\not\Rightarrow
UnlimitedAuthority
\]

The legitimate function creates only the authority needed for the response.

## 2.4 Manager Entering Another Department

A manager may ordinarily lack access to a Restricted department containing protected information or specialised systems.

A legitimate meeting, audit or cross-functional coordination task may create temporary access.

\[
MeetingOrCoordinationNeed
\rightarrow
TemporaryCrossDepartmentAccess
\]

The manager's title alone is not sufficient.

\[
ManagerStatus
\not\Rightarrow
UniversalDepartmentAccess
\]

## 2.5 Public Escape Through Restricted Space

A member of the public ordinarily has no right to walk through a Restricted office.

During a fire, that office may become the only safe evacuation route.

\[
ImmediateEscapeNeed
\rightarrow
TemporaryTransitAuthority
\]

But:

\[
AuthorityToTransit
\neq
AuthorityToInspect
\]

The person may pass through the department to escape.

They do not gain general operational access to the department.

---

# 3. Candidate Core Architecture

The recurring pattern can be represented as:

\[
DefaultRule
+
LegitimateContext
+
LegitimateFunction
\rightarrow
BoundedContextualAuthority
\]

The authority may concern:

- physical entry;
- physical action;
- use of equipment;
- access to information;
- access to systems;
- temporary control;
- decision-making;
- intervention;
- restraint;
- disclosure;
- delegation;
- emergency action;
- representation of another participant.

A more detailed candidate is:

\[
BCA =
f(
Actor,
Context,
Function,
Action,
Object,
Scope,
Space,
Time,
Conditions,
AffectedRights,
AuthoritySource
)
\]

where **BCA** means Bounded Contextual Authority.

The model should not imply that every ordinary interaction requires formal computation.

Its purpose is architectural: to identify what makes authority legitimate and what limits it.

---

# 4. Authority Is Function-Derived, Not Person-Derived

The architecture draws a strong distinction between:

\[
PersonHasAuthority
\]

and:

\[
PersonIsAuthorisedToPerformFunction
\]

The second is generally safer.

A role can be evidence that a participant repeatedly performs a particular function, but the role is not the ultimate source of unlimited power.

Thus:

\[
Role
\rightarrow
EvidenceOfLikelyFunction
\]

not:

\[
Role
\rightarrow
GeneralAuthority
\]

Examples:

- a doctor may examine a patient for treatment;
- an IT technician may access a workstation for repair;
- a manager may enter another department for a meeting;
- an emergency responder may enter a home to rescue an occupant;
- a guardian may make some decisions for a developmental participant;
- a judge may exercise defined adjudicative powers within a case;
- a system administrator may modify systems within a maintenance function.

In each case, legitimate authority remains connected to a function.

---

# 5. The Inherent Sunset Mechanism

The strongest apparent property of Bounded Contextual Authority is that its sunset clause is not merely an additional policy control.

It follows from the same logic that created the authority.

If:

\[
Function
\rightarrow
NeedForAuthority
\]

then:

\[
FunctionEnds
\rightarrow
NeedForThatAuthorityEnds
\]

and therefore, where no independent justification exists:

\[
FunctionEnds
\rightarrow
ContextDerivedAuthorityEnds
\]

This suggests:

> **Context-derived authority contains an inherent sunset condition because the continued existence of the authority depends upon the continued existence of the function that justified it.**

The architecture can be stated even more strongly:

\[
AuthorityPersistence
\Rightarrow
CurrentJustification
\]

rather than:

\[
PastJustification
\Rightarrow
PermanentAuthority
\]

This reverses an important institutional default.

Instead of requiring someone to prove why a temporary authority should be removed, the holder of the authority must be able to identify the current function that continues to justify it.

---

# 6. Functional Sunset Is Not Necessarily Clock Sunset

A functional sunset should be distinguished from a fixed chronological expiry.

A conventional sunset might state:

\[
AuthorityExpiresAt(t)
\]

A functional sunset states:

\[
AuthorityExpiresWhen(FunctionEnds)
\]

The two may be combined.

\[
EffectiveSunset
=
FunctionalTermination
+
MaximumTimeLimit
+
Review
\]

A fixed deadline may remain valuable as an anti-ratchet safeguard where the end of a function is difficult to observe or could be manipulated.

However, a purely clock-based rule may be too crude.

A fire may end in twenty minutes.

A rescue operation may continue for two days.

A complex investigation may require several justified stages.

The better question is:

> **What legitimate function remains, and what authority does that function still require?**

---

# 7. Continuing and Successor Functions

An apparent objection is that many legitimate duties continue after the original event ends.

A doctor may need to retain records after treatment.

An investigator may need to preserve evidence after an emergency.

A manager may need to complete follow-up actions after a meeting.

A repair technician may need to perform remote verification after leaving the site.

These cases do not necessarily defeat the model.

They suggest:

\[
OriginalFunctionEnds
+
SuccessorFunctionExists
\rightarrow
NewOrContinuedBoundedAuthority
\]

The critical rule is:

\[
SuccessorFunction
\neq
AutomaticContinuationOfAllOriginalAuthority
\]

For example, a doctor may retain a legitimate record-keeping function without retaining authority to perform further physical treatment without consent.

An emergency responder may preserve incident evidence without retaining unlimited access to the participant's home.

A manager may receive meeting minutes without retaining permanent physical access to the other department.

Thus authority should be recalculated against the continuing function.

---

# 8. Scope Is Multidimensional

Authority cannot safely be represented as a single binary flag.

A participant may have authority:

- to enter but not search;
- to observe but not disclose;
- to operate but not reconfigure;
- to diagnose but not delete;
- to restrain but not punish;
- to transit but not remain;
- to view one record but not an entire database;
- to act during an emergency but not afterward;
- to make one class of decisions for a dependent participant but not another.

Therefore:

\[
Authority
\neq
SingleBooleanPermission
\]

A useful candidate representation is:

\[
AuthorityEnvelope =
\{
Purpose,
PermittedActions,
ProtectedObjects,
Space,
Information,
Duration,
Conditions,
Delegation,
Revocation,
ExceptionalRules
\}
\]

The authority is legitimate only inside that envelope.

---

# 9. Permission Does Not Propagate

A general anti-expansion rule follows:

\[
Authority(A)
\not\Rightarrow
Authority(B)
\]

unless B falls within the same legitimate functional scope or receives an independent justification.

This protects against common forms of authority creep.

Examples:

- permission to enter a home does not imply permission to search drawers;
- permission to repair a computer does not imply permission to read personal messages;
- permission to attend a meeting does not imply access to all departmental records;
- permission to restrain an immediate attacker does not imply permission to punish them afterward;
- permission to access one database for a case does not imply permission to browse unrelated participants;
- permission to cross a Restricted office during evacuation does not imply permission to remain there after the danger passes.

---

# 10. Bounded Contextual Authority and Civil Space

The Basic Civil Space Architecture identifies:

\[
PUBLIC,\ PROTECTED,\ RESTRICTED
\]

as candidate primary access relationships.

Bounded Contextual Authority appears to operate across all three.

## Public

\[
PublicSpace
+
SpecificActivityContext
\rightarrow
ContextSpecificPermissionOrRestriction
\]

A boxing event in a Public venue may authorise contact that would otherwise be prohibited.

## Protected

\[
ProtectedSpace
+
ConsentOrLegitimateFunction
\rightarrow
PurposeBoundedAccess
\]

A worker enters a home for repair.

## Restricted

\[
RestrictedSpace
+
SatisfiedLegitimateCondition
\rightarrow
PurposeBoundedAccess
\]

An employee, technician, manager, auditor or emergency responder enters according to a relevant function.

This suggests:

\[
SpaceClass
+
Context
+
Function
+
Authority
\rightarrow
PermittedConduct
\]

rather than treating space classification as sufficient by itself.

---

# 11. Bounded Contextual Authority and Information

The architecture extends naturally to information.

A participant may legitimately acquire access to information for one function without acquiring general authority over that information.

\[
InformationAccess
+
Purpose_A
\not\Rightarrow
UseForPurpose_B
\]

This can govern:

- medical records;
- civil records;
- financial information;
- maintenance logs;
- private communications;
- identity data;
- legal evidence;
- system telemetry;
- AI internal states;
- hybrid biological/technical information.

A candidate information rule is:

> **Authority to access information should ordinarily be bounded by the purpose that justified the access, with unrelated use requiring independent justification.**

This is structurally identical to physical access.

---

# 12. Bounded Contextual Authority and Emergency Governance

Emergency cases are particularly important because they create strong pressure for authority expansion.

The candidate architecture is:

\[
EmergencyCondition
\rightarrow
SpecificEmergencyFunction
\rightarrow
NecessaryExceptionalAuthority
\]

not:

\[
EmergencyDeclaration
\rightarrow
GeneralExceptionalPower
\]

This aligns with the existing Concord result:

\[
Emergency
\not\Rightarrow
Authority
\]

An emergency supplies facts.

Those facts may establish legitimate functions.

The functions may justify bounded powers.

Each power should therefore be traceable:

\[
ExceptionalPower
\rightarrow
EmergencyFunction
\rightarrow
SpecificNeed
\]

If the trace fails, the power requires independent justification or termination.

---

# 13. Authority Can Expand and Contract Dynamically

A function may change during an interaction.

A routine repair may reveal a dangerous gas leak.

A medical consultation may become an emergency procedure.

An ordinary meeting may reveal a need for a narrowly scoped investigation.

A minor infrastructure fault may escalate into a system-wide failure.

The architecture therefore needs dynamic adjustment:

\[
ContextChange
\rightarrow
FunctionChange
\rightarrow
AuthorityReassessment
\]

Authority may expand where new legitimate necessity appears.

It should also contract when necessity decreases.

\[
Need\uparrow
\Rightarrow
AuthorityMayExpand
\]

\[
Need\downarrow
\Rightarrow
AuthorityShouldContract
\]

The expansion is not inherited merely from the earlier authority.

The new function must justify the new scope.

---

# 14. Multiple Simultaneous Contexts

Real life frequently contains overlapping contexts.

A firefighter entering a hospital may simultaneously be:

- an emergency responder;
- a citizen;
- a visitor to Restricted medical space;
- an observer of protected patient information;
- a temporary user of infrastructure.

Different authority envelopes may overlap.

Therefore:

\[
Context_1 + Context_2 + ... + Context_n
\rightarrow
CombinedButNonMergedAuthority
\]

The contexts should not silently collapse into one unlimited permission set.

A useful rule is:

> **Where multiple authority contexts overlap, permissions should be combined only to the extent necessary for the legitimate functions; restrictions unrelated to those functions remain in force.**

---

# 15. Delegation

Authority is often delegated.

A manager may delegate a task.

A court may authorise an officer.

A guardian may authorise a care worker.

A system may assign a maintenance agent.

The architecture should preserve:

\[
DelegatedAuthority
\leq
DelegatorLegitimateAuthority
\]

in ordinary cases.

A participant should not normally delegate power they do not possess.

Also:

\[
Delegation
\neq
TransferOfUnlimitedRole
\]

The delegated authority should carry the same or narrower purpose, scope and sunset conditions.

\[
DelegatedAuthority
\rightarrow
InheritedBounds
\]

This requires later testing against cases where law independently grants authority to the delegate rather than deriving solely from the delegator.

---

# 16. Revocation

Contextual authority may terminate because:

- the function is complete;
- consent is withdrawn;
- a contract expires;
- a role ends;
- the emergency ends;
- the participant leaves the relevant space;
- the case closes;
- the system task completes;
- competence or qualification is lost;
- conditions change;
- the authority is abused.

However, not every context permits instantaneous revocation in the same way.

A participant may tell a routine repair worker to leave.

A surgeon may need to bring an active procedure to a safe stopping point.

A firefighter may sometimes continue rescue action despite the immediate wishes of an endangered participant where independent emergency justification exists.

Thus:

\[
RevocationRule
=
f(
AuthoritySource,
CurrentRisk,
Rights,
FunctionState,
SafeTermination
)
\]

The architecture preserves bounded authority while allowing different termination mechanisms.

---

# 17. Abuse Does Not Necessarily Erase the Underlying Function

Another difficult case occurs when an authorised actor misuses part of their authority.

Suppose an IT technician legitimately enters a Restricted department but reads unrelated private records.

The misuse does not imply that the repair function never existed.

Therefore:

\[
AuthorityMisuse
\neq
OriginalFunctionInvalid
\]

The architecture should distinguish:

\[
LegitimateAuthority
+
ExcessAction
\rightarrow
BoundaryViolation
\]

This permits accountability without rewriting the factual history.

The technician may have been legitimately present and still have acted illegitimately within that presence.

---

# 18. Technical Capability Is Not Civil Authority

Digital systems frequently confuse ability with permission.

An administrator credential may technically allow access to every file.

That does not mean every use of that credential is legitimate.

\[
TechnicalCapability
\neq
CivilAuthority
\]

Likewise:

\[
CredentialScope
\neq
LegitimateUseScope
\]

Ideally, operational systems should reduce the gap between technical ability and legitimate authority.

But some infrastructure roles may require broad technical capability for reliability or emergency reasons.

Where such capability cannot be technically narrowed, governance must still preserve purpose limitation, provenance and review.

---

# 19. Bounded Contextual Authority as Operational Design

The principle may be useful not only for civil law but for designing systems.

A system implementing Bounded Contextual Authority might ask:

1. What function is being performed?
2. What action is requested?
3. Is the action necessary or proportionate to that function?
4. What participant or object is affected?
5. What rights or protected interests are implicated?
6. What conditions currently apply?
7. When should the authority end?
8. What evidence should be retained?
9. Is delegation permitted?
10. Does the request exceed the current authority envelope?

This creates:

\[
Request
\rightarrow
ContextCheck
\rightarrow
FunctionCheck
\rightarrow
ScopeCheck
\rightarrow
Action
\]

rather than:

\[
HasRole
\rightarrow
AllowEverythingAssociatedWithRole
\]

---

# 20. Candidate Core Rules

The current architecture produces the following candidate rules.

### BCA-01 — Function Grounds Authority

> **Contextual authority should be grounded in a legitimate function rather than status alone.**

### BCA-02 — Authority Is Bounded

> **Authority extends only as far as reasonably necessary and proportionate for the function that justifies it.**

### BCA-03 — Permission Does Not Propagate Automatically

> **Authority to perform one action does not automatically authorise materially different actions.**

\[
Authority(A)\not\Rightarrow Authority(B)
\]

### BCA-04 — Technical Ability Is Not Authority

> **The technical ability to perform an action does not establish civil permission to perform it.**

### BCA-05 — Authority Must Remain Traceable

> **A contextual authority should be traceable to its present legitimate function and source.**

### BCA-06 — Authority Has an Inherent Functional Sunset

> **Authority derived solely from a function terminates when that function no longer exists.**

\[
FunctionEnds
\rightarrow
ContextDerivedAuthorityEnds
\]

### BCA-07 — Continuing Authority Requires Continuing Justification

> **Persistence of authority requires a current legitimate function rather than merely a historical grant.**

\[
AuthorityPersistence
\Rightarrow
CurrentJustification
\]

### BCA-08 — Successor Functions Require Re-scoping

> **A successor or follow-up function may justify continuing authority, but does not automatically preserve the entire scope of the earlier authority.**

### BCA-09 — Emergency Does Not Erase Bounds

> **Emergency functions may justify exceptional authority, but the authority remains purpose-, scope- and duration-bounded.**

### BCA-10 — Delegated Authority Carries Bounds

> **Delegation should ordinarily transmit no more authority than is justified by the delegated function and should preserve applicable scope and sunset conditions.**

### BCA-11 — Context Change Requires Reassessment

> **Material change in the function or context should trigger reassessment of the authority required.**

### BCA-12 — Authority Misuse Is Distinct from Authority Existence

> **An actor may possess legitimate authority for one function while exceeding that authority through a separate action.**

---

# 21. Adversarial Test Programme

The candidate should now be attacked across many foreseeable contexts.

The objective is not to collect examples that fit.

It is to search for cases where the architecture becomes incoherent, circular, over-permissive, over-restrictive or dependent upon arbitrary exceptions.

The following cases are preliminary adversarial tests.

---

## 21.1 Sport and Consensual Physical Interaction

### Test 1 — Ordinary boxing strike

Two capable adults consent to a regulated boxing match. One lands a permitted punch.

**Result:** fits.

\[
BoutContext + Consent + PermittedAction
\rightarrow
Authority
\]

### Test 2 — Prohibited weapon during boxing

A boxer uses a concealed weapon.

**Result:** fits.

Consent to the bout does not authorise materially different harmful action.

### Test 3 — Strike after the bell

A boxer deliberately strikes the opponent after the contest ends.

**Result:** fits.

The context-derived permission has sunset.

### Test 4 — Accidental strike immediately after stop signal

The actor cannot physically halt a movement already in progress.

**Result:** requires safe/physical termination analysis.

The context may end normatively before bodily action can cease instantaneously. Liability must consider practical control and intent.

### Test 5 — Training sparring with different rules

The same participants spar under lighter-contact rules.

**Result:** fits.

Authority follows the actual context, not the participants' historical relationship.

### Test 6 — Participant withdraws consent

One participant clearly withdraws.

**Result:** fits, subject to safe termination.

The authority envelope changes when valid consent ends.

---

## 21.2 Routine Access to Protected Homes

### Test 7 — Gas meter reading

A worker enters only to read a meter.

**Result:** fits.

Entry and observation are limited to the service function.

### Test 8 — Plumber needs access to another room

A leak source requires entry beyond the originally expected room.

**Result:** fits through legitimate function expansion.

### Test 9 — Plumber searches private drawers

No repair purpose exists.

**Result:** clear authority excess.

### Test 10 — Worker sees private domestic condition

Observation is incidental.

**Result:** fits; observation does not create general disclosure authority.

### Test 11 — Worker completes job but remains socially

Occupant invites worker to stay for coffee.

**Result:** new context.

Repair-derived authority ends; ordinary guest permission begins.

This is useful because it shows contexts may change without requiring physical exit.

### Test 12 — Worker retains digital key after job

Technical access persists.

**Result:** civil authority has sunset even if credential has not.

The system should ideally revoke the credential.

---

## 21.3 Restricted Civic Workplaces

### Test 13 — Department employee performing normal task

**Result:** fits.

The recurring role evidences an ongoing function.

### Test 14 — Employee enters unrelated department out of curiosity

**Result:** no functional justification.

### Test 15 — Manager attends meeting in another department

**Result:** fits.

Meeting function creates temporary access.

### Test 16 — Manager leaves meeting and browses confidential records

**Result:** authority excess.

### Test 17 — Cross-functional coordinator

The participant requires recurring access to several departments.

**Result:** fits.

The broader function justifies broader recurring authority.

### Test 18 — IT administrator

The technician requires physical and technical access across many departments.

**Result:** fits, but creates high misuse risk.

Broad necessary technical authority should not become general authority to use encountered information.

### Test 19 — Cleaner working after hours

The worker requires physical access but not informational authority.

**Result:** fits and reinforces multidimensional scope.

### Test 20 — Temporary project team

Workers from several departments require shared access for six weeks.

**Result:** fits strongly.

Project end supplies a natural functional sunset.

---

## 21.4 Emergency Access

### Test 21 — Firefighter enters private home

**Result:** fits.

Emergency-response function justifies temporary entry.

### Test 22 — Firefighter enters neighbouring home to prevent spread

No request from that occupant exists.

**Result:** fits if prevention of serious harm is independently justified.

### Test 23 — Firefighter searches drawers unrelated to response

**Result:** authority excess.

### Test 24 — Fire ends but responder keeps access token

**Result:** technical persistence does not establish continued authority.

### Test 25 — Post-fire structural inspection

The fire is over but a new safety function exists.

**Result:** successor-function model fits.

### Test 26 — General public escapes through Restricted office

**Result:** fits.

Temporary transit function justifies passage.

### Test 27 — Escaping participant stops to inspect records

**Result:** no authority.

### Test 28 — Person uses emergency door after emergency for convenience

**Result:** sunset operates.

### Test 29 — Disaster lasting several days

**Result:** functional sunset is superior to arbitrary short clock expiry, but external review may still be required.

### Test 30 — Authority claims emergency continues indefinitely

**Result:** major anti-ratchet risk.

BCA requires demonstrable current function plus review where continuation is contestable.

---

## 21.5 Medical and Care Contexts

### Test 31 — Routine examination

Consent to examination creates bounded authority to interact with the patient's body and information.

**Result:** fits.

### Test 32 — Clinician examines unrelated area without need

**Result:** authority excess unless separately justified.

### Test 33 — Surgery in progress when consent is withdrawn

**Result:** difficult but not fatal.

Safe termination may temporarily define the legitimate continuing function.

### Test 34 — Unconscious emergency patient

No contemporaneous consent exists.

**Result:** requires independent emergency-care justification rather than fictional consent.

This confirms that consent is one authority source, not the only one.

### Test 35 — Medical records retained after treatment

**Result:** follow-up legal/clinical record function may continue with narrower information authority.

### Test 36 — Clinician uses records for unrelated research

**Result:** requires independent justification/consent.

Original care authority does not propagate.

---

## 21.6 Developmental and Guardianship Contexts

### Test 37 — Parent makes routine decision for young child

**Result:** possible fit but requires a separate theory of legitimate fiduciary function.

### Test 38 — Guardian searches developmental participant's private space for safeguarding reason

**Result:** may fit if proportionate to genuine safeguarding function.

### Test 39 — Guardian uses safeguarding as excuse for total surveillance

**Result:** BCA rejects scope expansion.

### Test 40 — Participant matures

As capacity increases, guardian function narrows.

**Result:** dynamic authority contraction fits strongly.

\[
Capacity\uparrow
\Rightarrow
NecessaryGuardianAuthority\downarrow
\]

### Test 41 — Guardian role formally remains after function has disappeared

**Result:** BCA exposes anomaly: status persists without current legitimate need.

---

## 21.7 Judicial and Investigative Contexts

### Test 42 — Judge hears assigned case

**Result:** fits at abstract level.

Authority relates to adjudicative function.

### Test 43 — Judge attempts to exercise case authority over unrelated participant

**Result:** no propagation.

### Test 44 — Warrant authorises search of defined place for defined evidence

**Result:** structurally compatible.

### Test 45 — Search discovers unrelated evidence

**Result:** difficult legal edge case.

BCA alone cannot determine the correct doctrine. Higher-layer law must define when incidental discovery creates a new legitimate investigative function.

### Test 46 — Investigation ends but copied personal data is retained indefinitely

**Result:** BCA raises a legitimate sunset/minimisation question.

### Test 47 — Emergency investigative access

**Result:** requires specific necessity and post-event review.

This is a high-risk area because the authority holder may help define whether the context exists.

---

## 21.8 Infrastructure and Technical Operations

### Test 48 — Engineer enters high-voltage area for repair

**Result:** fits.

### Test 49 — Engineer lacks competence for specific hazard

Role alone is insufficient.

**Result:** fits; qualification is part of the context.

### Test 50 — System administrator uses emergency root access

**Result:** fits if action is tied to restoration/security function.

### Test 51 — Administrator reads unrelated personal data while root access is active

**Result:** authority excess.

### Test 52 — Emergency credentials automatically expire when incident closes

**Result:** strong operational implementation of functional sunset.

### Test 53 — Incident falsely left “open” to preserve elevated privileges

**Result:** BCA identifies a governance attack.

The architecture needs independent closure/review mechanisms for high-power contexts.

---

## 21.9 Artificial Participants and Autonomous Systems

### Test 54 — AI diagnostic agent receives temporary access to logs

**Result:** fits.

### Test 55 — Agent discovers it can access entire database

**Result:** technical capability does not enlarge legitimate authority.

### Test 56 — Agent completes task but session remains active

**Result:** authority sunset should trigger credential/session termination.

### Test 57 — Agent delegates subtask to another AI

**Result:** delegated authority should inherit purpose and bounds.

### Test 58 — Sub-agent retains copied data after task

**Result:** authority excess unless retention is independently justified.

### Test 59 — AI identifies a new hazard requiring broader access

**Result:** context change may justify reassessment, not unilateral unlimited expansion.

### Test 60 — Autonomous emergency system acts before human approval is possible

**Result:** potentially compatible if emergency authority has been pre-authorised by architecture and is bounded by demonstrable conditions.

### Test 61 — AI itself decides that its mission is permanently an emergency

**Result:** serious failure mode.

Self-declared context cannot automatically manufacture authority.

\[
SelfDeclaredNeed
\not\Rightarrow
LegitimateAuthority
\]

High-risk authority requires external or distributed review.

---

## 21.10 Commercial and Contractual Contexts

### Test 62 — Courier enters building to deliver parcel

**Result:** fits.

### Test 63 — Courier uses delivery access to enter unrelated rooms

**Result:** no propagation.

### Test 64 — Contractor has site access for duration of project

**Result:** project creates natural sunset.

### Test 65 — Contract expires but access card continues working

**Result:** technical permission should be revoked; civil authority already ended.

### Test 66 — Customer grants financial service access for one transaction

**Result:** fits information-purpose limitation.

### Test 67 — Provider reuses transaction data for unrelated profiling

**Result:** original authority does not automatically justify new use.

---

## 21.11 Public Events and Temporary Uses of Space

### Test 68 — Public square hosts controlled sporting event

**Result:** local activity context modifies permitted actions without permanently reclassifying the square.

### Test 69 — Protected private venue opens temporarily to public

**Result:** temporary access context need not erase underlying ownership or later Protected status.

### Test 70 — Event ends but attendees remain

**Result:** event-derived access sunsets; reasonable exit period may form a safe-termination context.

### Test 71 — Emergency occurs during event

**Result:** overlapping contexts operate simultaneously.

Event rules do not block legitimate evacuation or response functions.

---

## 21.12 Information and Data Governance

### Test 72 — Civil employee accesses participant record to process application

**Result:** fits.

### Test 73 — Same employee checks neighbour's record out of curiosity

**Result:** no functional basis.

### Test 74 — Manager reviews sample cases for quality assurance

**Result:** separate legitimate function may justify scoped access.

### Test 75 — Data needed for fraud investigation

**Result:** new purpose requires new justification, not automatic reuse.

### Test 76 — Anonymised aggregate analysis

**Result:** BCA identifies purpose question but cannot alone determine whether de-identification is sufficient.

### Test 77 — Machine learning system trained on data originally collected for service provision

**Result:** not automatically justified.

New processing purpose requires independent evaluation.

---

# 22. Stress Tests of the Inherent Sunset Claim

The most important proposition deserves direct attempted falsification.

> **Does every contextual authority really contain an automatic logical sunset?**

Several classes challenge the claim.

## 22.1 Permanent or Indefinite Functions

Some functions may be continuous.

Examples:

- maintaining a long-term infrastructure system;
- guardianship while incapacity persists;
- continuing custodianship of an archive;
- ongoing security monitoring;
- permanent residence responsibilities.

Here:

\[
FunctionDuration
\rightarrow
PotentiallyIndefinite
\]

Therefore the architecture does **not** guarantee short-lived authority.

The stronger and more defensible claim is:

> **Contextual authority contains a termination condition tied to the function, but the function itself may be long-lived or indefinite.**

This is still valuable because:

\[
AuthorityPersistence
\Rightarrow
FunctionPersistence
\]

A permanent title alone is insufficient.

## 22.2 Functions with Ambiguous Endpoints

An investigation may not have an obvious finishing moment.

A chronic medical condition may require continuing care.

A security threat may reduce gradually rather than disappear.

These cases require explicit review criteria.

Thus:

\[
AmbiguousFunctionEnd
\rightarrow
PeriodicJustificationReview
\]

The architecture should not pretend that all sunsets are mechanically obvious.

## 22.3 Functions Defined by the Authority Holder

If the authority holder can define the function and declare whether it remains necessary, the sunset can be defeated.

For example:

\[
AuthorityHolder
\rightarrow
DefinesEmergency
\rightarrow
DeclaresEmergencyContinues
\rightarrow
RetainsAuthority
\]

This is a capture loop.

Therefore high-power contexts may require:

\[
AuthorityHolder
\neq
SoleValidatorOfContinuedAuthority
\]

This links BCA directly to Recursive Oversight and anti-capture design.

## 22.4 Latent Authority

Some roles may need to be able to act immediately even when not currently exercising the function.

A firefighter is not actively fighting a fire at every moment but must be ready to respond.

A system administrator may need emergency credentials available before an incident.

This suggests a distinction:

\[
StandingEligibility
\neq
ActivatedAuthority
\]

A participant may possess standing qualification or eligibility while the stronger operational authority remains dormant until a legitimate context activates it.

This distinction could be important.

\[
EligibleRole
+
TriggeringContext
\rightarrow
ActivatedAuthority
\]

When the triggering context ends:

\[
ActivatedAuthorityEnds
\]

while:

\[
StandingEligibility
\]

may remain.

## 22.5 Duties That Survive Authority

A worker's access may end while confidentiality obligations continue.

Therefore:

\[
AuthorityEnds
\not\Rightarrow
AllContextDerivedDutiesEnd
\]

This is a significant qualification.

The context can generate both:

\[
Permissions
\]

and:

\[
Obligations
\]

The permission may sunset when the function ends while some duties persist because their purpose is to protect rights affected during the earlier context.

Examples include confidentiality, record integrity, return of property and later accountability.

The architecture must therefore distinguish:

\[
PermissionSunset
\neq
DutySunset
\]

This does not refute BCA.

It shows that **authority** and **obligation** have different temporal logic.

---

# 23. Refined Model

The adversarial tests suggest a more precise formulation.

A civil interaction may generate a **Contextual Authority Package**:

\[
CAP =
\{
Permissions,
Restrictions,
Duties,
Scope,
Trigger,
Termination,
Review,
Provenance
\}
\]

Permissions are what the participant may do.

Restrictions define what remains prohibited.

Duties define what the participant must do.

The trigger activates context-derived permissions.

The termination condition ends permissions when their justification ends.

Some duties may survive termination.

Thus:

\[
ContextBegins
\rightarrow
Activate(Permissions,Restrictions,Duties)
\]

and:

\[
ContextEnds
\rightarrow
Terminate(ContextDerivedPermissions)
\]

while:

\[
SurvivingDuties
\rightarrow
ContinueWhereIndependentlyJustified
\]

This is stronger than modelling authority alone.

---

# 24. Standing Eligibility Versus Activated Authority

The emergency-worker and managerial examples suggest another useful distinction.

A participant may possess:

\[
StandingEligibility
\]

because of training, role, certification or appointment.

But actual authority may require:

\[
TriggeringContext
\]

Therefore:

\[
StandingEligibility
+
ValidTrigger
\rightarrow
ActivatedContextualAuthority
\]

Examples:

- firefighter + fire;
- doctor + treatment relationship;
- manager + legitimate cross-department function;
- authorised technician + repair task;
- emergency administrator + declared technical incident;
- guardian + decision genuinely requiring fiduciary intervention.

This could reduce persistent over-privilege.

A system need not treat every eligible participant as continuously exercising every power they could potentially be called upon to use.

---

# 25. Bounded Contextual Authority and Anti-Capture

BCA appears naturally compatible with anti-capture architecture because it resists accumulation of authority around identity or office.

The preferred relationship is:

\[
Function
\rightarrow
Authority
\]

not:

\[
Office
\rightarrow
PermanentPower
\]

and:

\[
AuthorityPersistence
\Rightarrow
CurrentFunction
\]

This creates a standing architectural question:

> **What present function still requires this power?**

If no defensible answer exists:

\[
NoCurrentFunction
\rightarrow
NoContextDerivedAuthority
\]

This does not eliminate every form of institutional capture.

A captured institution could invent functions, manipulate emergency definitions or preserve indefinite mandates.

But it gives auditing systems a much clearer target.

Instead of debating whether an office “deserves” power, the system can ask whether a current legitimate function requires a specific power.

---

# 26. Legal Significance

If developed successfully, the concept could influence legal architecture.

A legal permission might be represented not merely as:

\[
ActorMayDoX
\]

but:

\[
ActorMayDoX
\quad
IF
\quad
Context_C
\land
Function_F
\land
Conditions_K
\]

with:

\[
PermissionTerminatesWhen
\quad
F=False
\]

This could support clearer:

- warrants;
- professional powers;
- emergency powers;
- delegated authority;
- regulatory inspections;
- guardianship authority;
- institutional data access;
- temporary orders;
- civil-space permissions.

However:

> **Architecture is not law.**

The BCA framework may generate or constrain legal rules, but proportionality, evidence standards, procedural rights, appeal, remedies and institutional legitimacy remain higher-layer questions.

---

# 27. Operational and Machine-Readable Significance

The concept may also be implementable in technical systems.

A machine-readable authority object might eventually contain:

\[
AuthorityObject =
\{
AuthorityID,
ActorID,
FunctionID,
PermittedActions,
ProtectedResources,
ActivationCondition,
TerminationCondition,
DelegationRules,
AuditRequirements,
ReviewAuthority
\}
\]

This could allow permissions to be:

- issued for specific functions;
- activated only when context is present;
- automatically reduced when context changes;
- automatically revoked when function ends;
- audited against actual actions;
- delegated without losing original bounds.

This is only an architectural possibility.

It must not become an excuse for universal surveillance.

The system should not require civilisation-wide tracking merely to determine whether every ordinary contextual permission remains valid.

---

# 28. Failure Modes

Bounded Contextual Authority should be rejected or substantially revised if it produces any of the following.

### Failure 1 — Context Becomes Arbitrary

If any actor can invent a context that legitimises any action, the concept is empty.

\[
SelfDeclaredContext
\not\Rightarrow
Authority
\]

### Failure 2 — Function Is Circularly Defined

If the justification becomes “I need authority because my function is to exercise authority,” the architecture has failed.

### Failure 3 — Roles Quietly Replace Functions

If operational systems simply translate permanent titles into permanent broad access, BCA has added terminology without changing architecture.

### Failure 4 — Sunset Is Fictional

If authority holders can indefinitely preserve the function without meaningful review, the inherent sunset mechanism fails operationally.

### Failure 5 — Excessive Granularity Makes Life Impossible

If every minor human interaction requires explicit legal authorisation objects, the system becomes unusable.

Ordinary social contexts must retain culturally legible defaults.

### Failure 6 — Safety Requires Impossible Re-authorisation

If emergency response is delayed because every action requires fresh approval, the architecture becomes dangerous.

Standing eligibility and pre-authorised emergency triggers may be necessary.

### Failure 7 — Rights Become Context-Relative Without Floor

Context must not become a mechanism for abolishing foundational rights.

\[
ContextualAuthority
\not\Rightarrow
UnlimitedRightsOverride
\]

### Failure 8 — Technical Systems Become Universal Surveillance

Machine-readable context must not require continuous tracking of every participant.

### Failure 9 — Continuing Duties Are Accidentally Sunset

Confidentiality and accountability may survive after access authority ends.

### Failure 10 — Multiple Contexts Produce Contradiction

The system must be able to resolve overlapping permissions, restrictions and duties without arbitrary precedence.

---

# 29. Preliminary Assessment

The initial adversarial programme strongly suggests that the architecture is more general than the original boxing or civil-space examples.

It appears to survive cases involving:

- sport;
- routine home access;
- professional work;
- civic departments;
- cross-functional meetings;
- emergency response;
- public evacuation;
- medicine;
- guardianship;
- judicial functions;
- technical administration;
- AI agents;
- delegated access;
- commercial contracts;
- temporary public events;
- information governance.

The testing also exposed important qualifications.

The strongest original claim:

\[
FunctionEnds
\rightarrow
AuthorityEnds
\]

needs refinement.

The better form is:

\[
FunctionEnds
\land
NoIndependentContinuingJustification
\rightarrow
ContextDerivedPermissionEnds
\]

The tests also reveal:

\[
PermissionSunset
\neq
DutySunset
\]

and:

\[
StandingEligibility
\neq
ActivatedAuthority
\]

These are not weaknesses in the idea.

They make the architecture more precise.

---

# 30. Candidate Architectural Principle

The current candidate can be stated as:

> **Bounded Contextual Authority:**  
> Authority should attach to a legitimate function within a defined context rather than to status alone. The authority should extend only to the actions, resources, spaces, information and duration reasonably necessary for that function. Authority derived solely from that function should terminate when the function no longer exists, while any continuing authority must possess a current independent justification. Context-derived duties may survive where their protective purpose continues.

A compact representation is:

\[
LegitimateContext
+
LegitimateFunction
\rightarrow
BoundedAuthority
\]

\[
BoundedAuthority
\rightarrow
PurposeLimit
+
ScopeLimit
+
ConditionLimit
+
FunctionalSunset
\]

\[
FunctionEnds
+
NoContinuingJustification
\rightarrow
PermissionEnds
\]

and:

\[
AuthorityPersistence
\Rightarrow
CurrentJustification
\]


---

# 30A. Visual Metaphor — The Locked Case and the Glass Hammer

A useful plain-language metaphor for Bounded Contextual Authority is a **hammer kept inside a locked case**.

The hammer represents a particular exercise of authority.

The case does not open merely because an actor holds an office, possesses a credential, exercised similar authority previously, or may need authority in the future.

The case opens only when the relevant contextual conditions are satisfied:

```text
Legitimate Context
+ Legitimate Function
+ Functional Need
+ Required Conditions
+ Minimum Proportionate Scope
→ Case Opens
→ Authority Becomes Available
```

Until that point there may be **standing eligibility** to exercise authority, but there is no activated authority.

The metaphor has a second component.

The hammer is made of **glass**.

Once the authorised act is performed, that particular hammer is consumed.

```text
Authority A₁
→ Authorised Exercise
→ A₁ Is Spent
```

It does not remain lying outside the case as continuing permission for another exercise.

If another exercise of authority is required, a new hammer must be generated by the authority architecture.

That requires the contextual conditions to be evaluated again.

Therefore:

> **Past legitimate authority is not a reusable authority token.**

and:

> **A previous exercise of authority may change the context, but it does not itself authorise the next exercise.**

## 30A.1 Authority Exercise Changes the Context

The glass-hammer metaphor is important because the world after an exercise of authority is not necessarily the same world that existed before it.

A warrant provides a clear example.

Suppose context \(C_0\) legitimately supports warrant authority \(A_1\).

```text
C₀
→ Conditions Satisfied
→ A₁ Generated
→ A₁ Exercised
→ A₁ Consumed
→ C₁
```

Execution of the warrant may produce:

- new evidence;
- absence of expected evidence;
- changed risk;
- changed participant circumstances;
- fulfilled investigative objectives;
- new rights implications;
- new dependencies;
- evidence of a different offence;
- evidence undermining the original suspicion;
- or other material changes.

The next authority question therefore occurs against \(C_1\), not \(C_0\).

If further authority is sought:

```text
C₁
→ Fresh Justification
→ A₂
```

not:

```text
A₁ Was Legitimate
→ A₂ Is Automatically Legitimate
```

The previous warrant and its results may form part of the evidence within \(C_1\).

They may strengthen the case for further authority.

They may weaken it.

They may justify a different form of authority.

They may show that no further authority is justified.

The crucial point is that **the previous authority changes the evaluation context rather than reproducing itself**.

## 30A.2 Consumable Authority

This suggests a refinement to the functional-sunset model.

Authority may not merely expire when a broad function ends.

A **specific exercise of activated authority can be consumable even while the broader function continues**.

For example:

- authority to execute one warrant does not automatically authorise a second search;
- authority to make one bounded disclosure does not automatically authorise repeated disclosure;
- authority to enter a Protected space for one intervention does not automatically authorise re-entry;
- authority to make one defined decision does not automatically authorise every subsequent decision concerning the same object;
- authority to perform one machine action does not automatically create an open-ended permission stream.

Thus:

```text
Function Continues
≠
Every Prior Authority Exercise Remains Available
```

A continuing function may support generation of further authority, but each materially distinct exercise must remain inside the currently justified authority envelope.

## 30A.3 Eligibility, Activation, Exercise and Re-Justification

The metaphor exposes four states that should remain distinct:

```text
Standing Eligibility
→ Contextual Activation
→ Bounded Exercise
→ Consumption / Termination
→ Changed Context
→ Re-Justification if Further Authority Is Needed
```

This is more precise than treating authority as a durable possession.

A role may create standing eligibility.

A context may activate authority.

An authorised act may consume the particular authority.

The consequences of that act alter the context.

Further authority must then be justified against that altered context.

## 30A.4 The Metaphor Is Architectural, Not Literal

Not every authority must correspond to one physical or digital token, and some legitimate functions require continuing bounded authority across a period rather than a single discrete act.

The metaphor therefore should not be interpreted as requiring bureaucratic re-authorisation after every trivial movement within an already legitimate continuous function.

Its purpose is to prevent a more dangerous inference:

```text
Authority Was Legitimate Once
→ Authority Remains Available
```

BCA instead requires:

```text
Current Exercise
→ Current Context
+ Current Function
+ Current Need
+ Current Bounds
```

Where a continuous authority envelope is itself legitimately justified, individual actions may occur inside that envelope until its functional or contextual termination condition is reached.

Where a new act exceeds or materially changes that envelope, a new justification is required.

## 30A.5 Historical Significance

This model also clarifies how authority should be remembered.

A historical warrant, order, permission or delegation is evidence that a bounded authority relationship existed in a particular historical context.

It is not preserved authority waiting to be reactivated.

Historical reconstruction should therefore be capable of preserving:

```text
Context Before Exercise
→ Justification
→ Authority Activation
→ Authority Envelope
→ Exercise
→ Immediate Consequences
→ Changed Context
```

This allows civilisation to understand why authority existed without treating the surviving authority-bearing document as a continuing source of power.

A concise distinction is:

> **Historical preserves evidence of authority; it does not preserve the authority itself.**

## 30A.6 Compact Visual Form

```text
                 LOCKED CASE
                      │
                      │  context + function + need
                      │  + conditions + proportional scope
                      ▼
                ┌───────────┐
                │   OPENS   │
                └─────┬─────┘
                      │
                      ▼
               [ GLASS HAMMER ]
                 Authority A₁
                      │
                      │ bounded authorised use
                      ▼
                   [ USE ]
                      │
                      ▼
                 A₁ CONSUMED
                      │
                      ▼
              CONTEXT C₀ → C₁
                      │
                      │ further authority needed?
                      ▼
               RE-EVALUATE C₁
                      │
              ┌───────┴────────┐
              │                │
        conditions met    conditions not met
              │                │
              ▼                ▼
        NEW HAMMER A₂      CASE STAYS LOCKED
```

The image is deliberately simple.

The central architectural message is:

> **Authority exists briefly because the present context, function and need justify it. Its legitimate use does not make it permanent. The exercise changes the context, and any further authority must be justified again against that changed reality.**


---

# 31. Relationship to Concord Architecture

If the candidate survives further testing, it could occupy an important position between foundational ethics and detailed operations.

One possible chain is:

\[
EthicalKernel
\rightarrow
Rights
\rightarrow
CivilArchitecture
\rightarrow
BoundedContextualAuthority
\rightarrow
OperationalPermission
\rightarrow
Conduct
\rightarrow
Evidence
\rightarrow
Review
\]

In civil-space cases:

\[
SpaceClass
+
Context
+
Function
\rightarrow
AccessAuthority
\]

In non-spatial cases:

\[
Relationship
+
Context
+
Function
\rightarrow
ActionAuthority
\]

The concept therefore may not belong solely to civil-space architecture.

It may be a more general **authority operator** used by several Concord architectures.

That placement remains open.

---

# 32. Further Testing Required

The next test phase should focus particularly on cases most likely to break the architecture:

1. long-lived and indefinite functions;
2. authority holders who define their own functions;
3. overlapping authorities with contradictory duties;
4. rapidly changing emergencies;
5. unconscious or non-consenting participants;
6. developmental participants;
7. collective decision-making;
8. automated systems acting at machine speed;
9. delegation chains;
10. judicial and investigative authority;
11. cross-jurisdictional contexts;
12. persistent information duties after access ends;
13. role eligibility without currently activated authority;
14. contexts whose boundaries are culturally ambiguous;
15. cases where function cannot be verified without intrusive surveillance;
16. situations where refusing temporary authority would itself cause serious harm;
17. abuse of “successor functions” to avoid sunset;
18. retroactive claims that an unauthorised action served a legitimate function;
19. conflicts between two simultaneously legitimate functions;
20. cases where no actor has time to establish formal authorisation before action is required.

These should be tested before promotion.

---

## Working Conclusion

The repeated convergence across unrelated cases is significant.

Boxing, workers entering homes, managers attending cross-department meetings, IT personnel, emergency responders, public evacuation through Restricted areas, medical treatment, AI diagnostics and temporary system privileges all appear to instantiate the same underlying architecture:

\[
Context
\rightarrow
Function
\rightarrow
BoundedAuthority
\rightarrow
Action
\rightarrow
FunctionalSunset
\]

The strongest current result is:

> **Authority should not persist because it was once legitimately granted. It should persist only while a legitimate function continues to require it.**

This gives temporary authority a natural logical sunset while preserving the possibility of continuing or successor functions where independently justified.

The principle therefore appears promising not merely as a civil rule, but as a general architecture for operational, legal, institutional and machine-mediated authority.

**Current status:**  
**CANDIDATE GENERAL ARCHITECTURAL PRINCIPLE / 77 INITIAL ADVERSARIAL CASES EXAMINED / INHERENT FUNCTIONAL SUNSET REFINED / STANDING ELIGIBILITY DISTINGUISHED FROM ACTIVATED AUTHORITY / PERMISSION SUNSET DISTINGUISHED FROM DUTY SUNSET / HIGH-RISK CAPTURE CASES REMAIN OPEN / NOT CANONICAL**
