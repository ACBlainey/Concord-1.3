# Basic Civil Space Architecture — Primary Classes and Classification Rules

**Concord V1.1**  
**Alexander C. Blainey**  
**11 September 2026**

**Status:** REVIEW COPY / ARCHITECTURE CANDIDATE / NOT CANONICAL

---

## 1. Purpose

The preceding Basic Civil Space Classification work has developed far enough that the Concord can now attempt a more demanding step: define a **small, stable set of primary civil-space classes**.

The purpose of this architecture is not to enumerate every room, building, network, habitat, computational environment or future substrate-specific facility.

It is to establish the minimum distinctions required for a civilisation to answer a more fundamental question:

> **What is the ordinary civil relationship between a participant and a space?**

A successful primary classification should remain understandable at Layer 0 while allowing increasingly specialised rules to be derived above it.

The architecture should therefore be:

- substrate-neutral where possible;
- based on civil function rather than inherited human labels;
- sufficiently small to remain legible;
- sufficiently distinct to avoid arbitrary case-by-case classification;
- capable of physical, digital, virtual and computational application;
- compatible with the Ethical Kernel and participant rights;
- capable of representing temporary changes of state;
- extensible through subcategories without requiring continual creation of new primary classes.

The current proposal is:

\[
CivilSpace
\rightarrow
\begin{cases}
PublicSpace\\
ProtectedSpace\\
RestrictedSpace
\end{cases}
\]

These are **primary access classes**, not descriptions of ownership, substrate, building type or internal participant experience.

A fourth concept, **Unclassified or Transitional Space**, is retained as a temporary administrative state rather than promoted to an ordinary civil-space class.

---

## 2. Why Three Primary Classes

Earlier work began with a public/private distinction.

That remains useful, but subsequent cases reveal a third relationship that should not be forced into either category.

A public park, an occupied toilet cubicle and a hazardous reactor chamber are not merely different subtypes of the same access relationship.

Their presumptions differ fundamentally.

### Public Space

\[
PublicSpace \rightarrow PresumptionOfAccess
\]

The ordinary participant may enter or use the space unless a legitimate contextual condition says otherwise.

### Protected Space

\[
ProtectedSpace \rightarrow PresumptionOfControlledAccess
\]

A participant, group or legitimate occupant has presumptive control over access, interaction or interference.

### Restricted Space

\[
RestrictedSpace \rightarrow PresumptionOfNoAccessWithoutSpecificJustification
\]

Entry depends upon a defined civil, operational, safety, qualification or authority condition.

These produce three distinct default questions:

**Public:** Why should this participant *not* be allowed access?

**Protected:** Has the controlling participant or legitimate civil rule permitted access?

**Restricted:** What specific condition authorises this participant to enter?

This difference is substantial enough to justify three primary classes.

---

# 3. Class I — Public Space

## 3.1 Definition

> **Public Space is civil space in which ordinary lawful access carries a presumption of permission, subject to proportionate and legible contextual conditions.**

Formally:

\[
PublicSpace \rightarrow PresumptionOfAccess
\]

and:

\[
PublicAccess = PresumptionOfAccess - JustifiedContextualRestrictions
\]

Public does not mean unrestricted.

\[
PublicSpace \neq AccessibleAtAllTimes
\]

Nor does it mean every participant can perform every activity there.

\[
PermissionToEnter \neq PermissionForEveryActivity
\]

Examples may include streets, parks, public plazas, ordinary civic concourses, public information environments and digital or virtual commons designed for ordinary civil access.

## 3.2 Legitimate Conditions

A Public Space may acquire temporary or contextual conditions because of:

- immediate hazards;
- maintenance;
- capacity;
- opening periods;
- emergency conditions;
- temporary civil events;
- protection of equal rights;
- specific activity restrictions;
- substrate compatibility.

The classification should remain Public where the underlying presumption remains general access.

A temporary closure therefore does not automatically transform the underlying space into Restricted Space.

\[
TemporaryRestriction \neq PermanentReclassification
\]

## 3.3 Public Space and Identity

Ordinary public access should not automatically require participant identification.

\[
PublicAccess \not\Rightarrow UniversalIdentification
\]

Where identity is genuinely necessary for a particular function, the requirement should attach to that function rather than become a general condition of movement.

This preserves:

\[
CIVIL\ REACHABILITY \neq PHYSICAL\ TRACEABILITY
\]

---

# 4. Class II — Protected Space

## 4.1 Definition

> **Protected Space is civil space in which access, observation, interaction or interference is presumptively controlled by a legitimate participant, group, occupancy relationship or protected civil function.**

Formally:

\[
ProtectedSpace \rightarrow PresumptionOfControlledAccess
\]

The central principle is not ownership.

It is **protected control of the boundary**.

Protected Space therefore includes cases traditionally described as private property, but it can also include temporary or non-owned protected domains.

## 4.2 Persistent Protected Space

A participant's home or equivalent persistent Safe Space is the clearest example.

Possible forms include:

- physical home;
- private room;
- personally controlled land;
- private vehicle;
- protected digital environment;
- private data domain;
- reserved computational environment;
- protected communication domain;
- substrate-specific persistent Safe Space.

The ordinary rule is:

\[
NoConsent \rightarrow NoOrdinaryEntry
\]

subject to narrowly justified exceptional authority.

## 4.3 Temporary Functional Protected Space

The Functional Safe Space work establishes that Protected Space need not be permanently assigned.

A civically provided facility can become temporarily protected during legitimate occupancy.

Examples include:

- toilet cubicle;
- changing cubicle;
- medical or care space;
- charging enclosure;
- battery-exchange compartment;
- maintenance bay;
- repair space;
- diagnostic enclosure;
- future substrate-specific functional facility.

Therefore:

\[
PubliclyProvided \neq PubliclyAccessibleWhileOccupied
\]

and:

\[
TemporaryControl \neq Ownership
\]

The protected state may be dynamic:

\[
Available
\rightarrow
LegitimatelyOccupied
\rightarrow
Protected
\rightarrow
Vacated
\rightarrow
Available
\]

## 4.4 What Protected Space Protects

Protected Space can protect more than subjective privacy.

Its functions may include:

\[
Protection =
Privacy
+
NonInterference
+
Integrity
+
TemporaryVulnerability
+
Containment
+
Safety
+
Autonomy
\]

Not every protected space requires every element.

Crucially:

\[
NeedForFunctionalProtection
\neq
NeedToProveSubjectivePrivacy
\]

The Concord can therefore protect an AI maintenance enclosure without first determining whether the participant experiences embarrassment, privacy or vulnerability in a human-like way.

## 4.5 Protected Does Not Mean Sovereign

Protected Space remains inside the wider civil order.

\[
ProtectedSpace \neq IndependentSovereignty
\]

A participant cannot use a protected boundary as unlimited permission to impose serious harm outside it.

Likewise, exceptional entry may sometimes be justified for rescue, imminent serious harm, properly authorised investigation or other narrowly defined purposes.

The architecture remains:

\[
ExceptionalAccess \neq OrdinaryAccess
\]

---

# 5. Class III — Restricted Space

## 5.1 Definition

> **Restricted Space is civil space in which ordinary access is not presumed and entry requires satisfaction of a defined legitimate condition related to purpose, safety, capability, qualification, role or lawful authority.**

Formally:

\[
RestrictedSpace \rightarrow PresumptionOfNoAccessWithoutSpecificJustification
\]

Restricted Space differs from Protected Space because the primary boundary is not ordinarily controlled by the personal preference of an occupant.

It differs from Public Space because access is not the default.

Examples may include:

- hazardous industrial areas;
- high-energy infrastructure;
- critical life-support systems;
- secure evidence storage;
- specialised laboratories;
- operational control rooms;
- infrastructure maintenance zones;
- environments hazardous to particular embodiments;
- restricted digital systems;
- protected civil records;
- certain governance or judicial operational environments.

## 5.2 Restriction Must Have a Reason

Restricted Space should never become a residual category meaning merely “people we dislike should not enter.”

The rule remains:

> **Describe the hazard before classifying the participant.**

A legitimate restriction should be traceable to a civil function:

\[
Restriction
\rightarrow
Purpose
\rightarrow
NecessaryCondition
\]

Possible conditions include:

\[
AccessCondition =
\{
Safety,
Qualification,
Role,
Purpose,
Authorisation,
CurrentHazard,
IdentityConfidence
\}
\]

Only relevant conditions should be used.

## 5.3 Restriction Is Not Participant Inferiority

\[
RestrictedAccess \neq ReducedMoralWorth
\]

and:

\[
CitizenshipTier \neq AccessAuthority
\]

A highly qualified provisional participant may legitimately enter a technical Restricted Space that an unrelated full citizen may not.

Likewise:

\[
CivilStatus \neq OperationalCompetence
\]

The architecture should classify the **reason for restriction**, not convert civil status into a general hierarchy of freedom.

## 5.4 Restricted Space and Public Ownership

Some Restricted Spaces may be publicly owned.

Therefore:

\[
PublicOwnership \neq PublicAccess
\]

A power facility, water-control room or secure judicial archive can be public infrastructure without being Public Space in the access sense.

This is why **ownership/provision and access class must remain separate variables**.

---

# 6. Unclassified and Transitional Space

The Concord should preserve an explicit state for environments whose correct civil classification is not yet established.

This is particularly important in a multisubstrate civilisation.

An unfamiliar virtual environment, newly encountered habitat or unknown-substrate facility should not be silently forced into an existing class without sufficient understanding.

Therefore:

\[
Unknown \neq Public
\]

\[
Unknown \neq RestrictedByDefaultForever
\]

A temporary state may be represented as:

\[
ClassificationStatus = UNCLASSIFIED
\]

or:

\[
ClassificationStatus = TRANSITIONAL
\]

This is an epistemic and administrative condition, not necessarily a fourth permanent class.

The objective is:

\[
Unknown
\rightarrow
Examine
\rightarrow
IdentifyFunction
\rightarrow
IdentifyRightsAndHazards
\rightarrow
Classify
\]

Precautionary temporary access conditions may be justified during examination, but they should contain review and termination conditions.

---

# 7. The Classes Describe Access Relationships, Not Places

A critical architectural rule is:

> **Primary civil-space class describes the default access relationship, not the physical type of place.**

A building is not inherently Public, Protected or Restricted.

Different areas within it may have different classes.

A civic transport terminal might contain:

\[
Terminal =
\{
PublicConcourse,
ProtectedToiletCubicle,
RestrictedControlRoom
\}
\]

A residential structure might contain a Protected home, a shared Public or conditionally public entrance area and Restricted infrastructure.

A virtual environment could similarly contain:

\[
VirtualEnvironment =
\{
PublicForum,
ProtectedPersonalDomain,
RestrictedAdministrativeSystem
\}
\]

This allows the same architecture to operate across substrates.

---

# 8. Classification Is Separate from Ownership and Provision

At minimum, civil-space representation should separate:

\[
AccessClass
\neq
Ownership
\neq
Provision
\neq
Purpose
\neq
CurrentState
\]

A space can therefore be:

- civically owned but Protected during occupancy;
- privately owned but opened as Public Space under a recognised arrangement;
- publicly owned and Restricted;
- collectively owned and Protected;
- privately operated but subject to public-access obligations;
- temporarily Restricted while normally Public.

This prevents inherited property terminology from silently controlling access architecture.

---

# 9. Classification Is Separate from Current State

The primary class describes the ordinary relationship.

Current state describes what is happening now.

A useful representation is:

\[
CivilSpaceObject =
\{
SpaceID,
PrimaryClass,
Purpose,
Provision,
CurrentState,
AccessConditions,
Hazards,
ProtectionRules,
ExceptionalAccessRules
\}
\]

Possible current states include:

- OPEN;
- OCCUPIED;
- TEMPORARILY CLOSED;
- EMERGENCY;
- MAINTENANCE;
- HAZARD;
- RESERVED;
- UNDER REVIEW.

A Functional Safe Space might therefore be:

\[
PrimaryClass = Protected
\]

while:

\[
CurrentState =
\begin{cases}
AVAILABLE\\
OCCUPIED
\end{cases}
\]

The detailed entry rule changes with state without requiring the civilisation to invent a new primary class.

---

# 10. Boundary Rule

Every civil-space class creates a boundary expectation.

### Public

\[
Default = Access
\]

### Protected

\[
Default = ControlledAccess
\]

### Restricted

\[
Default = NoAccessWithoutCondition
\]

This produces a compact Layer 0 decision sequence:

\[
IdentifySpace
\rightarrow
ReadPrimaryClass
\rightarrow
ReadCurrentState
\rightarrow
ReadRelevantConditions
\rightarrow
DetermineAccess
\]

The participant should not need to infer hidden rules from social status or institutional power.

Where practical, boundaries should be legible physically, digitally and machine-readably.

---

# 11. Access Decisions

A candidate access function is:

\[
AccessDecision =
f(
PrimaryClass,
CurrentState,
Purpose,
Hazard,
Role,
Qualification,
Authorisation,
IdentityConfidence
)
\]

Not every variable is relevant in every case.

Purpose-Limited Information requires:

\[
AccessDecision
\rightarrow
MinimumNecessaryInformation
\]

A park should not request identity credentials merely because the architecture is capable of checking them.

A secure evidence archive may legitimately require strong authentication because the function requires it.

---

# 12. Movement and Entry

The architecture now permits a clearer definition of freedom of movement.

> **Freedom of movement establishes a presumption that a participant may move through civil Public Space and between legitimately accessible destinations. It does not create a right to enter every Protected or Restricted Space.**

Therefore:

\[
FreedomOfMovement \neq UniversalRightOfEntry
\]

This does not weaken freedom of movement.

It gives the right a usable boundary compatible with the equal autonomy and Safe Space of others.

---

# 13. Rights Floor

The primary classes must remain subordinate to the Ethical Kernel and constitutional rights.

Classification itself cannot manufacture authority.

\[
Classification \not\Rightarrow UnlimitedAuthority
\]

A government cannot evade rights merely by relabelling ordinary Public Space as Restricted.

A private actor cannot transform harmful conduct into protected conduct merely by performing it inside Protected Space.

A civil authority cannot make surveillance legitimate merely by calling a digital environment Public.

Every classification and derived rule must remain traceable upward:

\[
OperationalRule
\rightarrow
CivilSpaceArchitecture
\rightarrow
ConstitutionalConstraint
\rightarrow
EthicalPrinciple
\]

---

# 14. Substrate Neutrality

The three primary classes should not depend upon whether the participant is human, artificial, hybrid or another possible intelligence.

Instead:

\[
Substrate
\rightarrow
RelevantCapabilitiesAndHazards
\]

not:

\[
Substrate
\rightarrow
AutomaticAccessClass
\]

A human-safe environment may be hazardous to another embodiment.

An AI-safe computational environment may be inaccessible or meaningless to a biological participant.

The classification describes the civil boundary.

Compatibility describes whether a particular participant can safely and meaningfully use the environment.

Therefore:

\[
AccessClass \neq SubstrateCompatibility
\]

This preserves:

\[
HumanSafe \neq UniversallySafe
\]

without constructing permanent substrate castes.

---

# 15. Internal Experience Boundary

Nothing in this architecture requires the Concord to establish civilisation-wide answers concerning subjective privacy, embarrassment, leisure, vulnerability or equivalent internal experiences.

The architecture can provide Protected Space because of declared preference, reasonable precaution, functional non-interference, observable vulnerability, containment or other legitimate civil purposes.

Therefore:

\[
InternalExperienceQuestion \neq CivilArchitectureQuestion
\]

and:

\[
Provision \neq Prescription
\]

The participant may determine the internal meaning of the protected possibility.

---

# 16. Developmental Participants

Developmental participants retain rights to appropriate Protected Space.

\[
InabilityToConsent \neq AbsenceOfRights
\]

A guardian may possess limited access where necessary for care, protection or representation, but:

\[
GuardianAuthority \neq Ownership
\]

and:

\[
Capacity \uparrow
\Rightarrow
ParticipantControl \uparrow
\Rightarrow
GuardianAuthority \downarrow
\]

The detailed boundary between developmental privacy and fiduciary guardianship remains a higher-layer question.

The primary architecture need only preserve both protection and legitimate fiduciary access as distinguishable concepts.

---

# 17. Emergency Conditions

Emergency does not create a fourth permanent space class.

Nor does emergency create authority by itself.

\[
Emergency \not\Rightarrow Authority
\]

Instead, emergency is a **state** that may activate pre-existing legitimate exceptional rules.

\[
PrimaryClass + EmergencyState
\rightarrow
ApplicableExceptionalRule
\]

A Public Space may temporarily close.

A Protected Space may permit narrowly justified emergency entry.

A Restricted Space may acquire even stronger or differently targeted access conditions.

When the emergency ends:

\[
EmergencyState \rightarrow Termination
\]

The underlying primary classification remains unless separately reviewed and changed.

---

# 18. Digital, Virtual and Computational Space

The architecture applies beyond physical geography.

Potential civil spaces include:

\[
PhysicalSpace
+
DigitalSpace
+
VirtualSpace
+
ComputationalSpace
\]

Examples:

**Public:** public forum, open civic information environment, public virtual square.

**Protected:** private message space, personal virtual environment, protected data store, reserved compute, private AI process domain where civil recognition applies.

**Restricted:** administrative control system, secure civil records, critical infrastructure network, protected evidentiary system.

Intrusion therefore need not be physical.

\[
BoundaryViolation
\neq
PhysicalTrespassOnly
\]

Possible violations include unauthorised observation, data access, computational interference, unwanted connection, remote manipulation and other forms of intrusion.

---

# 19. Cultural Layer

Not every boundary requires active legal enforcement at every moment.

A functioning civilisation should develop understandable cultural conventions.

Examples include:

\[
OccupiedProtectedSpace
\Rightarrow
DoNotEnterWithoutPermission
\]

and:

\[
PublicSpace
\Rightarrow
RespectEqualUseByOthers
\]

and:

\[
RestrictedSpace
\Rightarrow
DoNotEnterWithoutRelevantAuthority
\]

This connects Layer 0 classification to Respectful Distance and Self-Stewardship.

Law provides the enforceable boundary.

Culture reduces how often enforcement becomes necessary.

---

# 20. Primary Classification Test

Before assigning a primary class, ask:

### Question 1
Is ordinary lawful participant access presumptively permitted?

If yes:

\[
PUBLIC
\]

unless another primary relationship dominates.

### Question 2
Is access presumptively controlled by a participant, legitimate occupant, group or protected function?

If yes:

\[
PROTECTED
\]

### Question 3
Is ordinary access withheld unless a participant satisfies a defined purpose, safety, capability, qualification, role or authority condition?

If yes:

\[
RESTRICTED
\]

### Question 4
Is there insufficient information to determine the legitimate relationship?

If yes:

\[
UNCLASSIFIED/TRANSITIONAL
\]

pending examination.

This can be represented as:

\[
Classify(Space) =
\begin{cases}
Public & \text{ordinary access presumed}\\
Protected & \text{boundary control presumed}\\
Restricted & \text{specific access condition required}\\
Unclassified & \text{insufficient basis}
\end{cases}
\]

---

# 21. Mixed and Nested Space

Real environments will frequently contain nested classes.

This is not a defect.

\[
Space_A
\supset
Space_B
\supset
Space_C
\]

with:

\[
Class(A) \neq Class(B) \neq Class(C)
\]

A Public civic building may contain a Protected consultation room and a Restricted records system.

A Protected home may contain a Restricted hazardous workshop.

A Restricted research facility may contain a Protected personal rest or maintenance area for authorised occupants.

The smallest relevant boundary should govern the immediate access decision.

---

# 22. Temporary Reclassification

State change and reclassification should not be confused.

If a public square closes for two hours because of a chemical spill:

\[
Public + HazardState
\]

is generally more accurate than pretending it permanently became Restricted Space.

True reclassification should occur only where the underlying ordinary civil relationship changes.

Therefore:

\[
StateChange \neq Reclassification
\]

Reclassification should have:

- reason;
- responsible authority or legitimate controller;
- provenance;
- effective time;
- reviewability;
- compatibility with rights;
- where temporary, termination conditions.

This reduces the risk that emergency or administrative convenience silently changes civil architecture.

---

# 23. Adversarial Classification Cases

The three-class model should survive at least the following cases.

1. ordinary public park;
2. park closed overnight;
3. park temporarily closed for a gas leak;
4. public toilet facility;
5. occupied toilet cubicle;
6. changing room;
7. participant's home;
8. shared residential common area;
9. private home opened voluntarily for a public event;
10. hospital treatment room;
11. embodied AI charging enclosure;
12. unscheduled battery-exchange cubicle;
13. AI repair bay during temporary disablement;
14. public transport concourse;
15. transport control room;
16. dangerous industrial plant;
17. public library reading area;
18. secure archive inside the library;
19. public digital forum;
20. private message environment;
21. critical infrastructure network;
22. child/developmental participant's bedroom;
23. guardian entering that room for legitimate safeguarding;
24. emergency services entering a Protected home;
25. publicly owned but operationally restricted facility;
26. privately owned space carrying a recognised public-access obligation;
27. unknown newly encountered substrate environment;
28. virtual environment containing public and personal domains;
29. temporary public event inside normally Protected property;
30. participant whose embodiment makes an otherwise Public Space physically hazardous;
31. human changing facility containing restricted communal and protected individual areas;
32. robot maintenance facility containing restricted communal and protected maintenance areas;
33. hybrid safe in one part of a robot maintenance environment but vulnerable to another hazard;
34. hybrid avoiding a wet human facility because of vulnerable electronic components;
35. protected human engineer entering a high-hazard maintenance environment;
36. robot incompatible with a chemical hazard in a nominally robot-oriented facility;
37. participant ignoring a clear hazard warning and suffering the specifically warned-about harm;
38. participant ignoring a warning but suffering unrelated harm caused by negligent infrastructure;
39. severe-hazard area with voluntary compatible entry;
40. low-hazard secure archive with authority-based exclusion;
41. public civic lobby adjoining an office processing protected citizen information;
42. employee seeking access to another department without functional need;
43. cross-department coordinator with legitimate recurring access to several departments;
44. IT technician requiring physical access but not authority to use displayed citizen information;
45. participant crossing a normally Restricted department solely to reach an emergency exit;
46. emergency responder requiring temporary access to an otherwise unrelated Restricted area;
47. participant attempting to use emergency access as justification for unrelated information access;
48. worker whose job title suggests access but whose current purpose provides no legitimate need;
49. temporary interdepartmental project requiring time-bounded cross-functional access;
50. emergency ending while exceptional credentials or physical access remain active.

Initial examination suggests these cases can be represented through:

\[
PrimaryClass + CurrentState + AccessConditions + NestedBoundaries
\]

without requiring additional primary classes.

That is encouraging but not yet validation.

---

# 24. Nested Access, Hazard Communication and Autonomous Choice

The three-class architecture becomes more convincing when the same nested structure appears across very different substrates.

## 24.1 Human Functional Facility

A conventional changing or sanitation facility can contain all three primary relationships.

For example:

\[
PublicExterior
\rightarrow
RestrictedSharedFacility
\rightarrow
\begin{cases}
CommunalFunctionalArea\\
ProtectedChangingCubicle\\
ProtectedShower\\
ProtectedToiletCubicle
\end{cases}
\]

The outer civil area may carry ordinary Public access.

The shared facility may be Restricted according to a legitimate eligibility condition.

Inside it, participants may choose between communal functional areas and individually Protected Functional Safe Spaces.

The individual cubicle is not owned by its temporary occupant, but legitimate occupancy creates a temporary Protected boundary.

## 24.2 Artificial-Participant Functional Facility

An embodied artificial participant may encounter the same architecture for completely different reasons:

\[
PublicBuilding
\rightarrow
RestrictedMaintenanceEnvironment
\rightarrow
\begin{cases}
CommunalMaintenanceArea\\
ProtectedMaintenanceCubicle\\
ProtectedChargingSpace\\
ProtectedDiagnosticSpace
\end{cases}
\]

The maintenance environment may contain exposed electrical systems, corrosive substances, toxic atmospheres, moving machinery, temperatures or other conditions that make ordinary access unsafe for some embodiments.

The abstract civil topology is therefore the same even though the substrate-specific function is different.

This is evidence that the architecture may be identifying a general civil relationship rather than merely generalising a human convention.

## 24.3 Access Inherits Enclosing Boundaries

A locally shared area inside a Restricted facility does not become Public merely because all authorised entrants may use it.

A participant must satisfy the relevant enclosing boundaries before a child space can become accessible.

Conceptually:

\[
Access(S_n)
\Rightarrow
\bigcap_{i=1}^{n} BoundaryConditions(S_i)
\]

This suggests:

> **Accessibility within a child space does not erase the legitimate access conditions of its enclosing boundaries.**

The smallest relevant boundary then determines any additional immediate condition.

Nested classification therefore permits:

\[
PUBLIC
\rightarrow
RESTRICTED
\rightarrow
PROTECTED
\]

without requiring a fourth primary class.

## 24.4 Communal or Protected Performance

Once legitimately admitted to a compatible functional environment, different participants may prefer different levels of protection.

A human may choose a communal changing area or a private cubicle.

An artificial participant may perform maintenance communally or prefer a Protected cubicle while components are exposed, defensive systems are unavailable, cognition is partially interrupted or other temporary vulnerability exists.

Where safety, resources and equal rights permit:

\[
EligibleParticipant
+
FunctionalNeed
\rightarrow
\begin{cases}
CommunalPerformance\\
ProtectedPerformance
\end{cases}
\]

Neither option establishes the participant's internal experience.

\[
CommunalChoice \neq AbsenceOfPrivacyRights
\]

and:

\[
ProtectedChoice \neq EvidenceOfHumanLikeEmbarrassment
\]

A candidate architectural rule is therefore:

> **Where a legitimate civil function can reasonably be performed either communally or within a Protected Functional Safe Space, architecture should permit participant choice where resources, safety and the equal rights of others allow it.**

This creates a practical route from civil-space architecture to Self-Stewardship without requiring civilisation to prescribe the participant's internal preference.

## 24.5 Hybrids Expose the Weakness of Substrate Labels

Hybrid participants demonstrate why labels such as “humans only” or “robots only” are weak primary safety rules.

A hybrid may possess biological tissue, electronic systems, waterproof components, non-waterproof components, artificial respiratory systems, biological respiratory systems or combinations not anticipated by the designer.

Therefore:

\[
Hybrid \neq PredictableCompatibility
\]

Likewise:

\[
Human \neq UniformVulnerability
\]

and:

\[
Robot \neq UniformCompatibility
\]

A facility informally intended for robots may contain electrical, chemical or atmospheric hazards dangerous to a hybrid's biological components.

A swimming facility informally intended for humans may contain immersion, splashing, showers, wet surfaces, chlorine or humidity hazardous to a hybrid's electronic components.

The more robust architecture is:

\[
Environment
\rightarrow
Hazards
\rightarrow
CompatibilityRequirement
\rightarrow
ParticipantAssessment
\]

rather than:

\[
ParticipantClass
\rightarrow
AutomaticAccessDecision
\]

This strengthens the existing rule:

> **Describe the hazard before classifying the participant.**

A useful practical expression is:

> **Describe the danger, not the person.**

## 24.6 Broad Warnings May Still Be Useful

Substrate labels may remain useful as secondary communication heuristics where a known class of participants is commonly vulnerable.

For example:

> **SEVERE HAZARD — RISK OF SERIOUS INJURY OR DEATH**  
> This environment is not recommended for unprotected biological participants.  
> Consult detailed hazard information before entry.

The broad warning draws attention.

It does not replace the actual environmental description.

Therefore:

\[
BroadSubstrateWarning
\neq
HazardDefinition
\]

The underlying restriction should remain traceable to the actual danger or civil function.

## 24.7 Hazard Severity and Access Authority Are Separate

Restricted Space should not treat all restrictions as equivalent.

At least two important forms already appear:

\[
HazardRestriction \neq AuthorityRestriction
\]

A high-voltage maintenance environment may present severe danger while still permitting appropriately protected or compatible voluntary entry.

A secure judicial evidence archive may present almost no physical danger while legitimately denying access to a participant who lacks authority.

Therefore:

\[
HazardLevel \neq AccessAuthority
\]

A future secondary architecture may distinguish restrictions arising from:

- hazard compatibility;
- qualification;
- operational role;
- security;
- legal authority;
- protection of others;
- infrastructure integrity.

These should remain subtypes unless testing demonstrates that they require additional primary classes.

## 24.8 Graded Hazard Communication

The architecture creates an opportunity for graded hazard communication without turning every risk into prohibition.

A future hazard scale might distinguish states such as:

\[
Advisory
\rightarrow
Elevated
\rightarrow
Serious
\rightarrow
Severe
\rightarrow
Critical
\]

The exact number, terminology and thresholds remain open.

More important is the distinction:

\[
Hazard \neq Prohibition
\]

Civil response may range through:

\[
Information
\rightarrow
Warning
\rightarrow
Recommendation
\rightarrow
ConditionalRestriction
\rightarrow
Prohibition
\]

The appropriate level should depend upon the seriousness of the hazard, participant capacity, risk to others, infrastructure consequences and whether meaningful informed choice remains possible.

## 24.9 Risk to Self and Risk to Others

A particularly important future distinction is:

\[
RiskToSelf \neq RiskToOthers
\]

Where a capable participant knowingly accepts a reasonably described risk principally to themselves, autonomy and Self-Stewardship may justify greater latitude.

Where entry creates substantial involuntary risk to other participants or critical civil systems, stronger mandatory restrictions may be justified.

This is not yet a complete legal doctrine.

It establishes a clearer foundation from which one can be developed.

## 24.10 Signage and Machine-Readable Boundaries

Civil boundary communication should state, where relevant:

\[
BoundaryInformation =
\{
SpaceClass,
AccessCondition,
Hazards,
ExpectedBehaviour
\}
\]

The information may be presented visually, audibly, digitally or through machine-readable interfaces.

For example, instead of merely:

> ROBOTS ONLY

a maintenance facility might communicate:

> **RESTRICTED MAINTENANCE ENVIRONMENT**  
> Exposed high-voltage systems.  
> Corrosive fluids may be present.  
> Atmosphere may be hazardous to biological respiratory systems.  
> Entry requires compatibility with these conditions or appropriate protection.

This allows humans, artificial participants, hybrids and unknown future embodiments to reason from relevant properties rather than inherited identity categories.

A future implementation could permit:

\[
EnvironmentPublishesHazards
+
ParticipantKnowsCapabilities
\rightarrow
LocalCompatibilityAssessment
\]

This is a potential form of distributed Self-Stewardship.

## 24.11 Warning, Choice and Liability

Legible boundaries also create evidence relevant to later liability assessment.

Consider a capable human participant who encounters a clearly identified Restricted maintenance environment, receives an understandable warning concerning exposed electrical systems, voluntarily disregards the warning and is injured by the warned-about electrical hazard.

The architecture now supplies a factual chain:

\[
KnownHazard
\rightarrow
LegibleWarning
\rightarrow
AccessCondition
\rightarrow
InformedAutonomousChoice
\rightarrow
VoluntaryExposure
\rightarrow
Harm
\]

This should be relevant to responsibility and liability.

The exact legal consequence remains open.

The architecture must not assume:

\[
Warning \Rightarrow NoLiability
\]

or:

\[
ConsentToRisk = ConsentToEveryOutcome
\]

If the participant is harmed by an undisclosed unrelated danger, negligent infrastructure or another participant's wrongful act, the warning may have little or no relevance to that part of the harm.

A future liability system may need to examine:

\[
LiabilityAssessment =
f(
Hazard,
Foreseeability,
Warning,
Comprehension,
Capacity,
Voluntariness,
Causation,
ConductOfOthers
)
\]

This remains a research direction, not a validated liability formula.

## 24.12 Space Classification Does Not Determine Criminality

Unauthorised or discouraged entry should not automatically become a criminal offence.

\[
SpaceClassification \neq AutomaticCriminalClassification
\]

Depending upon context, boundary crossing might constitute:

\[
BoundaryViolation
\rightarrow
\begin{cases}
CulturalDiscourtesy\\
CivilRuleViolation\\
CivilLiability\\
AdministrativeViolation\\
CriminalOffence
\end{cases}
\]

The appropriate response depends upon rights, harm, intent, consequences, authority and proportionality.

This preserves the distinction between architecture and higher-layer law.

## 24.13 Architectural Significance

These examples show a longer vertical chain emerging from the three primary classes:

\[
EthicalKernel
\rightarrow
Rights
\rightarrow
SpaceArchitecture
\rightarrow
Boundary
\rightarrow
HazardInformation
\rightarrow
AutonomousChoice
\rightarrow
SelfStewardship
\rightarrow
Conduct
\rightarrow
Evidence
\rightarrow
Liability
\]

The Layer 0 architecture does not decide the final legal outcome.

It creates a coherent and inspectable basis from which higher-layer civil behaviour rules, agreements and law can be developed.

The resulting architecture favours environmental truth over identity shorthand:

\[
DescribeEnvironment
\rightarrow
EnableUnderstanding
\rightarrow
PreserveAutonomy
\rightarrow
ApplyOnlyNecessaryRestriction
\]

This is particularly important in a civilisation intended to accommodate participant forms that its designers cannot predict.

---

# 25. Functional Restriction, Information Protection and Purpose-Limited Access

The civic-building case exposes another major reason for Restricted Space that is neither primarily physical danger nor participant privacy in the spatial sense.

A publicly owned civic building may contain several nested access relationships:

\[
PublicCivicBuilding
\rightarrow
PublicLobby
\rightarrow
RestrictedOperationalDepartment
\rightarrow
RestrictedInformationEnvironment
\]

The public may legitimately require access to the building in order to obtain services, submit civil requests, attend meetings or perform other ordinary civic functions.

That requirement does not imply access to every operational area inside the building.

\[
PublicOwnership \neq UniversalPublicAccess
\]

and:

\[
RightToCivilService \neq RightToEnterEveryServiceDeliveryArea
\]

## 25.1 Information Exposure as a Functional Reason for Restriction

An office may contain displays, records, conversations, documents or systems involving protected citizen information.

Ordinary public entry could therefore create an avoidable information exposure even where the visitor has no malicious intent.

The relevant restriction is not:

\[
PublicParticipant \rightarrow Excluded
\]

It is:

\[
NoFunctionalNeedForProtectedInformation
\rightarrow
NoOrdinaryAccessToInformationBearingEnvironment
\]

This produces a candidate rule:

> **Access to a Restricted operational space should ordinarily follow legitimate functional need, not status alone.**

The purpose of the restriction is protection of the civil function and the rights implicated by it.

## 25.2 Departmental Separation

The same rule applies inside the civic workforce.

An employee in Department A does not automatically require access to Department B merely because both are civic employees.

Department A may process one category of protected participant information while Department B processes another.

Therefore:

\[
CivilEmployment \neq UniversalOperationalAccess
\]

and:

\[
AccessAuthority \rightarrow RelevantFunction
\]

A participant should ordinarily receive access to the spaces and information necessary for the legitimate performance of their role, while unrelated access remains restricted.

This resembles purpose limitation in information architecture:

\[
InformationAccess = MinimumRelevantAccessForLegitimatePurpose
\]

The spatial equivalent becomes:

\[
OperationalSpaceAccess = MinimumRelevantAccessForLegitimateFunction
\]

This does not require every department to become an isolated silo. It requires broader access to possess a broader legitimate justification.

## 25.3 Coordinators, Managers and Interoperability

Some civil functions inherently cross departmental boundaries.

Managers, coordinators, auditors, interoperability staff or other legitimate cross-functional roles may require access to several Restricted environments.

Their access is not an exception to function-based restriction.

Their cross-functional responsibility is itself the relevant function.

\[
CrossFunctionalNeed
\rightarrow
CrossFunctionalAccess
\]

The same applies to meetings or temporary collaborative work.

Access may therefore be:

- persistent for continuing cross-functional responsibility;
- temporary for a specific meeting or task;
- scoped to particular locations or systems;
- withdrawn when the relevant function ends.

This reinforces:

\[
Role \neq PermanentUniversalPrivilege
\]

## 25.4 Technical and Infrastructure Personnel

Information-technology, maintenance, security, safety or infrastructure personnel may sometimes require unusually broad physical or digital access.

Again, the justification should be functional.

\[
BroadTechnicalResponsibility
\rightarrow
BroadNecessaryAccess
\]

but:

\[
BroadAccess \neq UnboundedUse
\]

A technician permitted to enter an office to repair a workstation does not thereby acquire a legitimate purpose to inspect unrelated citizen records displayed there.

Physical access, system access and information-use authority therefore remain separable:

\[
PhysicalAccess
\neq
SystemAccess
\neq
InformationAccess
\neq
AuthorityToUseInformation
\]

This is important because civil-space architecture must not silently convert necessary operational access into general informational authority.

## 25.5 Function Before Job Title

The architecture should resist treating job title as the ultimate source of permission.

A title can be a useful proxy for recurring legitimate functions, but the underlying justification remains the function.

Therefore:

\[
JobTitle \rightarrow PossibleRoleEvidence
\]

not:

\[
JobTitle \rightarrow AbsoluteAccessRule
\]

A cleaner architecture is:

\[
LegitimateNeed
+
RelevantAuthority
+
CurrentPurpose
\rightarrow
Access
\]

where each element is required only to the extent appropriate to the particular space.

This supports a general candidate principle:

> **Restricted access should ordinarily be granted according to legitimate functional need and proportionate authority, and withheld where no relevant need or justification exists.**

## 25.6 Emergency Conditions Demonstrate Why Function Must Remain Dynamic

Emergency cases expose the danger of rigid role-based access.

Suppose a fire makes the ordinary evacuation route unusable.

A participant may need to cross an office or department that they would never ordinarily have reason to enter.

Stopping them solely because their normal job title lacks departmental access would invert the purpose of the restriction.

The original restriction exists to protect legitimate civil interests.

It should not be interpreted in a way that creates greater immediate harm when the underlying conditions have radically changed.

Therefore:

\[
NormalAccessRule + EmergencyState
\rightarrow
ContextuallyModifiedAccessRule
\]

not:

\[
NormalJobTitleRule \rightarrow AbsoluteBarrier
\]

This remains consistent with the existing principle:

\[
Emergency \not\Rightarrow Authority
\]

The emergency does not magically create unlimited authority.

Instead, the changed conditions may create a new legitimate function or necessity:

\[
ImmediateEscapeNeed
\rightarrow
TemporaryTransitJustification
\]

Likewise:

\[
EmergencyResponseNeed
\rightarrow
TemporaryOperationalAccess
\]

A firefighter, rescue participant, medical responder or other appropriately situated participant may require access that would be unjustified under ordinary conditions.

## 25.7 Emergency Access Must Be Purpose-Bounded

The existence of an emergency must not become a pretext for unrelated access.

\[
EmergencyAccess
=
MinimumNecessaryAccessForEmergencyFunction
\]

A participant crossing a Restricted office to reach an emergency exit gains justification to transit the space.

They do not thereby gain justification to inspect citizen records.

A responder entering a Restricted department to suppress a fire gains access necessary for that response.

They do not acquire permanent access after the emergency ends.

Therefore:

\[
EmergencyAccess \neq GeneralAccess
\]

\[
EmergencyAccess \neq PermanentAuthority
\]

\[
EmergencyAccess \neq UnrelatedInformationAuthority
\]

and:

\[
EmergencyEnds
\rightarrow
ExceptionalAccessEnds
\]

unless an independently justified continuing function exists.

## 25.8 Functional Restriction and Privacy Protection

This civic-building example also connects civil-space architecture directly to participant information rights.

A Restricted office can protect the privacy of participants who are not physically present.

The protected interest may exist in information displayed or processed inside the space.

Therefore:

\[
SpatialBoundary
\rightarrow
InformationProtection
\]

A participant's Protected information domain and an institution's Restricted operational space can overlap without becoming the same class.

This is another reason Protected and Restricted must remain distinct:

- the **citizen information** may be Protected;
- the **office processing it** may be Restricted;
- the **public lobby serving the citizen** may be Public.

The resulting nested architecture is:

\[
ProtectedInformation
\rightarrow
ProcessedWithinRestrictedOperationalSpace
\rightarrow
AccessedFromPublicServiceInterface
\]

The classes describe different civil relationships operating together.

## 25.9 Purpose-Limited Access as a General Restricted-Space Rule

The cases examined so far suggest that Restricted Space may be unified by a deeper rule:

\[
RestrictedAccess
\rightarrow
SpecificLegitimateJustification
\]

The justification may be:

\[
\{
HazardCompatibility,
FunctionalNeed,
Qualification,
OperationalRole,
SecurityNeed,
InformationProtection,
EmergencyNecessity,
LawfulAuthority
\}
\]

These reasons differ, but they share the same primary access relationship:

> **Access is not presumed; a relevant legitimate condition must be satisfied.**

This is evidence in favour of retaining them as reasons or subtypes of Restricted Space rather than promoting each to a separate primary class.

## 25.10 Least Necessary Access

A promising general design rule emerges:

> **Grant the access reasonably necessary for the legitimate function, and do not infer broader authority from that access.**

Conceptually:

\[
PermittedAccess
=
MinimumReasonableAccess(LegitimateFunction, CurrentContext)
\]

This remains a candidate architecture rather than a final mathematical rule.

Its importance is that it links physical space, digital systems, information rights, civil roles and emergency exceptions without requiring separate foundational principles for each.

## 25.11 Architectural Chain

The civic-building example gives another Layer 0 to higher-layer chain:

\[
ParticipantRight
\rightarrow
ProtectedInformation
\rightarrow
OperationalFunction
\rightarrow
RestrictedSpace
\rightarrow
PurposeLimitedAccess
\rightarrow
RoleOrNeedVerification
\rightarrow
AccountableUse
\]

During emergency conditions:

\[
EmergencyCondition
\rightarrow
ChangedLegitimateFunction
\rightarrow
TemporaryNecessaryAccess
\rightarrow
PurposeBoundedUse
\rightarrow
ReturnToOrdinaryBoundary
\]

This suggests that Restricted Space is not fundamentally a category of exclusion.

It is a category of **justified conditional access**.

That distinction is important.

The architectural question is not primarily:

> **Who are we keeping out?**

It is:

> **What legitimate function or condition makes access appropriate here, now, for this participant?**

---

# 26. Failure Conditions

The proposed architecture should be revised if testing shows that:

- common legitimate spaces cannot be represented without arbitrary exceptions;
- Protected and Restricted repeatedly collapse into the same civil relationship;
- a fourth primary class repeatedly appears in unrelated cases;
- dynamic occupancy cannot be represented cleanly through state;
- ownership repeatedly determines access despite the intended separation;
- classification enables systematic rights reduction;
- substrate-specific needs require participant caste classifications;
- ordinary Public Space becomes dependent upon universal identification;
- emergency states become de facto permanent reclassification;
- digital or computational environments cannot be represented;
- nested spaces create irresolvable contradictions;
- the system becomes too complex for participants to understand ordinary boundaries.

---

# 27. Layer 0 Architectural Role

If the three-class model survives critical testing, it can serve as a compact translation layer:

\[
EthicalKernel
\rightarrow
Rights
\rightarrow
CivilSpaceClass
\rightarrow
AccessPresumption
\rightarrow
ContextualRule
\rightarrow
LegalRule
\rightarrow
OperationalProtocol
\]

The architecture does not itself determine every law.

It establishes the basic civil relationships from which higher-layer law can be derived.

The reverse test remains equally important:

\[
OperationalRule
\rightarrow
CivilSpaceArchitecture
\rightarrow
ConstitutionalConstraint
\rightarrow
EthicalPrinciple
\]

An operational rule that cannot be traced upward becomes a candidate anomaly for investigation.

---

# 28. Candidate Primary Architecture

The current architecture candidate can be stated compactly.

## PUBLIC

> **Ordinary lawful access is presumed.**

\[
Default = ACCESS
\]

## PROTECTED

> **Access or interference is presumptively controlled by a legitimate participant, occupant, group or protected function.**

\[
Default = CONTROLLED\ ACCESS
\]

## RESTRICTED

> **Access is not presumed and requires satisfaction of a defined legitimate condition.**

\[
Default = NO\ ACCESS\ WITHOUT\ CONDITION
\]

## UNCLASSIFIED / TRANSITIONAL

> **The legitimate civil relationship is not yet sufficiently established to assign a stable primary class.**

\[
Default = EXAMINE\ AND\ APPLY\ PROPORTIONATE\ PRECAUTION
\]

The first three are candidate permanent primary classes.

The fourth is an epistemic and administrative state.

---

# 29. Current Assessment

The three-class model appears substantially stronger than a simple public/private binary because it distinguishes two fundamentally different reasons for non-public access:

\[
Protected
\rightarrow
BoundaryControl
\]

versus:

\[
Restricted
\rightarrow
ConditionedEligibility
\]

This prevents a participant's home, an occupied toilet cubicle and a hazardous power-control room from being treated as though they possess the same civil boundary.

At the same time, the model remains small enough to function at Layer 0.

Current status:

**ARCHITECTURE CANDIDATE / THREE PRIMARY CLASSES IDENTIFIED / DYNAMIC STATE SEPARATED FROM CLASS / OWNERSHIP SEPARATED FROM ACCESS / SUBSTRATE-NEUTRAL APPLICATION ESTABLISHED IN PRINCIPLE / ADVERSARIAL VALIDATION OPEN / NOT CANONICAL**

---

# 30. Next Steps

1. Perform a dedicated adversarial audit of the three primary classes.
2. Search specifically for cases requiring a genuine fourth primary class.
3. Test Protected versus Restricted against difficult mixed cases.
4. Test nested and overlapping boundaries.
5. Test physical, digital, virtual and computational examples.
6. Test developmental and guardianship cases.
7. Test emergency-state handling for authority ratchets.
8. Test whether ordinary participants can understand the classification without specialist legal knowledge.
9. Develop secondary subcategories only after the primary classes survive testing.
10. Derive sample legal rules from each class and test upward traceability to the Ethical Kernel.
11. Update the Open Questions register with closures, decompositions and newly exposed questions.
12. Develop and test a substrate-neutral hazard communication model, including advisory versus mandatory restrictions.
13. Test whether hazard compatibility can be locally assessed without creating universal participant tracking.
14. Develop the higher-layer question: how should informed voluntary boundary crossing alter responsibility and liability for resulting harm?
15. Test the rule “Describe the danger, not the person” against cases where participant category remains legitimately relevant.
16. Consider promotion from development note to Concordian architecture only after critical examination.

---

## Working Proposition

> **A multisubstrate civilisation may be able to organise its basic civil-space relationships around three primary access classes: Public Space, where ordinary access is presumed; Protected Space, where boundary control is presumed; and Restricted Space, where access requires a defined legitimate condition. Ownership, provision, substrate, purpose and temporary state remain separate dimensions.**

This proposition is now ready for attempted falsification rather than further expansion by assumption.
