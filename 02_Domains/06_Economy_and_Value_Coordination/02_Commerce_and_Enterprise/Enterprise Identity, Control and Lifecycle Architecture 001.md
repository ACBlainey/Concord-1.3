# Enterprise Identity, Control and Lifecycle Architecture 001

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / PROVISIONAL / NON-CANONICAL / SOURCE-DERIVED SCAFFOLD  
**Date:** September 2026

---

# 1. Purpose

Commerce requires a persistent way to identify enterprises, determine who may legitimately act for them, preserve changes in control and status, and distinguish the enterprise's record from the civil records of the participants connected to it.

This document develops that requirement from existing Concord architecture.

It does **not** establish company law, legal personality, limited liability, corporate constitutional rights or any specific legal organisational form.

Those remain Law/constitutional questions.

---

# 2. Existing source primitives

The following existing Concord architectures are reusable.

## Civil identity architecture

Existing Citizen ID work separates:
- persistent official identifier;
- human-readable name;
- authentication credentials;
- routing/contact;
- provenance;
- security-event evidence.

The same separation is structurally useful for enterprises without implying that enterprise identity and participant identity are legally equivalent.

## Identity / continuity / provenance

Existing work separates:

**SELF-IDENTITY != CIVIL IDENTITY != IDENTITY VERIFICATION != PROVENANCE != SUCCESSION**

For enterprise purposes the reusable lesson is narrower:

**CURRENT ENTERPRISE IDENTITY != NAME != AUTHENTICATION != PROVENANCE != CONTROL != SUCCESSION**

## Bounded Contextual Authority

Existing architecture establishes that authority is function-derived and bounded by the legitimate function/context that creates it.

This is directly relevant to:
- directors/managers;
- authorised employees;
- purchasing authority;
- hiring authority;
- payment authority;
- contractual representation;
- regulatory/licensing interactions.

## Historical

Historical already provides:
- state objects;
- provenance relationships;
- contextual state assertions;
- authority-event records;
- correction relationships;
- lifecycle reconstruction;
- custody without operational ownership.

## Ratchet

Ratchet explicitly recognises:
- corporate participation;
- employees;
- contractual capacity;
- large-scale economic influence;
- beneficial-control and responsibility records;
- separation of economic power from constitutional authority.

These sources are sufficient to define a provisional enterprise record architecture.

---

# 3. Enterprise identity

A participating enterprise should have a persistent civil/commercial reference distinguishable from:
- enterprise name;
- public trading name;
- physical premises;
- network address;
- account credentials;
- owners;
- managers;
- employees;
- current authorised representatives.

Working term:

# **Enterprise ID**

The Enterprise ID is a persistent reference to the current recognised commercial organisation.

A change of name should not necessarily create a new Enterprise ID.

A change of representative should not create a new Enterprise ID.

A change of address should not create a new Enterprise ID.

Whether merger, division, conversion or other structural change creates a new Enterprise ID is a later lifecycle/legal question.

> **Enterprise ID != Enterprise Name.**

---

# 4. Enterprise is not the participant record of its owner

An enterprise may be connected to one or more participants.

That does not justify collapsing their records.

> **Enterprise Record != Owner Record.**

> **Enterprise Record != Employee Record.**

> **Enterprise Record != Customer Record.**

A participant's Civil Historical record may contain relationships such as:
- founder of;
- owner/controller of;
- authorised representative of;
- employee of;
- creditor/debtor relationship where legitimately recorded;
- licence holder/responsible person where applicable.

The enterprise record contains the corresponding enterprise-side relationship.

Linkage does not create universal access in either direction.

---

# 5. Candidate enterprise record

A provisional enterprise object may include:

`EnterpriseID`  
`CurrentRecognisedName`  
`PriorNameRefs`  
`CurrentStatus`  
`CreationOrRecognitionEventRef`  
`OrganisationalFormRef`  
`JurisdictionOrApplicableFrameworkRef`  
`BeneficialControlRefs`  
`GovernanceOrControlRefs`  
`AuthorisedRepresentativeRefs`  
`LicencePermissionRefs`  
`CommercialContactPointRefs`  
`HistoricalRecordIndexRef`  
`RestrictionOrDisputeRefs`  
`SuccessorPredecessorRefs`  
`DissolutionClosureRef`  
`ProvenanceRefs`

Not all fields are necessarily public.

This is an information architecture, not a final legal schema.

---

# 6. Control and beneficial responsibility

Ratchet already requires clear beneficial-control and responsibility records for corporate participants.

The enterprise architecture should distinguish at least:

## Economic interest
Who has a legitimate ownership/economic claim where such claims exist?

## Beneficial control
Who ultimately exercises or can exercise consequential control?

## Governance authority
Who is authorised by the enterprise's legitimate governance structure to make particular classes of decision?

## Operational authority
Who may perform specific functions?

## Representation authority
Who may bind or officially represent the enterprise in a particular context?

These may be different participants.

> **Ownership != Operational Authority.**

> **Economic Interest != Authority to Bind the Enterprise.**

> **Employment != General Representation Authority.**

---

# 7. Authorised representation

An enterprise needs ways for participants or agents to act on its behalf.

Representation should be explicit and bounded.

A representation record may need:

`RepresentativeID`  
`EnterpriseID`  
`AuthorityFunction`  
`Scope`  
`Context`  
`EffectiveFrom`  
`ExpiryOrTerminationCondition`  
`DelegationAuthority`  
`FurtherDelegationAllowed`  
`CredentialRef`  
`Provenance`  
`RevocationState`

Examples:
- hire staff;
- purchase up to a bounded value;
- access a commercial account;
- sign a defined contract class;
- submit regulatory information;
- administer a specific system;
- represent the enterprise in a dispute.

The authority should not automatically propagate.

> **Authority to Act for an Enterprise in One Function != Authority to Act for It in Every Function.**

---

# 8. Enterprise credentials

Knowing the Enterprise ID must not itself authorise action.

The architecture should separate:
- identity;
- credential;
- authority;
- role;
- current permission.

A participant may prove:
1. who they are;
2. which enterprise they claim to represent;
3. which authority relation applies;
4. that the authority remains current.

This parallels existing Citizen ID separation without reusing participant credentials indiscriminately.

---

# 9. Enterprise contact point

An enterprise may require an official communication endpoint analogous in function—but not necessarily identical in implementation—to Civil Contact.

Working term:

# **Commercial / Enterprise Contact Point**

It could receive:
- licence notices;
- tax/public-finance notices where applicable;
- procurement communication;
- legal service/routing;
- employment-system communication;
- commercial compliance notices;
- official requests;
- dispute notices.

The endpoint should route to currently authorised recipients without requiring external systems to know private internal organisational topology.

This requires later development.

---

# 10. Lifecycle states

A provisional enterprise lifecycle may include:

**PROPOSED / PRE-REGISTRATION**
→ enterprise is being formed but not yet recognised for relevant civil/commercial functions.

**ACTIVE**
→ recognised and able to exercise applicable commercial functions.

**RESTRICTED**
→ some permissions/functions are limited while enterprise identity persists.

**DORMANT / INACTIVE**
→ recognised identity persists but ordinary commercial activity is reduced or absent.

**RESTRUCTURING**
→ control/obligation/organisation is changing under a recognised process.

**INSOLVENCY / FAILURE PROCESS**
→ candidate state requiring future Law/Commerce architecture.

**DISSOLUTION PENDING**
→ closure underway; outstanding obligations/status unresolved.

**DISSOLVED / CLOSED**
→ no longer active as an ordinary commercial actor.

**SUCCESSOR / PREDECESSOR LINKED**
→ historical relationship to a new or prior enterprise identity.

These are candidate information states only.

Their legal meaning is not adopted here.

---

# 11. Creation / recognition event

An enterprise should not simply appear in civil systems without provenance.

A creation/recognition event should establish:
- Enterprise ID;
- initial recognised name;
- applicable organisational form where defined;
- founding/control relationships;
- authorised initial representatives;
- initial permissions/licences where applicable;
- provenance;
- responsible authority/process.

The Commerce domain should not invent the legal criteria for recognition where those belong to Law.

---

# 12. Change of control

Control may change without enterprise identity necessarily changing.

Examples may include:
- ownership transfer;
- governance replacement;
- authorised representative change;
- management change;
- restructuring.

Each consequential control change should be provenance-bearing.

Where control affects:
- licences;
- security suitability;
- procurement eligibility;
- contractual authority;
- beneficial-control requirements;

KCS may identify dependent systems requiring review.

> **Change of Control Should Trigger Relevant Review, Not Universal Reset.**

---

# 13. Dissolution does not erase history

Closing an enterprise should not erase:
- contracts;
- liabilities;
- employment history;
- provenance;
- judicial records;
- ownership/control history;
- tax/public-finance history where applicable;
- safety/compliance history;
- successor relationships.

Historical should preserve the enterprise's legitimate record after operational closure.

> **Dissolution != Historical Erasure.**

But Historical preservation should not automatically keep obsolete permissions active.

> **Historical Persistence != Operational Continuation.**

---

# 14. Successor relationships

A dissolved/restructured enterprise may have a successor.

The architecture should represent succession explicitly rather than silently reusing identity.

Possible relationships:
- SUCCESSOR_OF;
- PREDECESSOR_OF;
- MERGED_INTO;
- SPLIT_FROM;
- ACQUIRED_ASSET_FROM;
- ASSUMED_OBLIGATION_FROM.

These relationships do not themselves determine legal liability.

Law/Judiciary must determine which rights/obligations transfer.

> **Provenance of Succession != Automatic Transfer of Liability.**

---

# 15. Enterprise Historical record

Historical can reuse its existing model:

**Enterprise ID**
→ **Enterprise Record Index**
→ **Protected Record Spaces**
→ **State / Provenance / Relationships**
→ **Lifecycle Events**
→ **Retired Historical Custody**

Candidate protected spaces:
- Identity / Status;
- Control / Governance;
- Employment;
- Licensing;
- Contracts;
- Financial/Public Finance;
- Security;
- Legal/Judicial;
- Procurement;
- Safety/Compliance.

As with participant records:

> **Coherent Enterprise Record != Universal Enterprise Dossier Access.**

---

# 16. Participant access and enterprise access are different

A participant may have rights to inspect records about themselves.

That does not automatically give an owner, employee or representative unrestricted access to every enterprise record.

Enterprise access should follow legitimate role/authority.

Likewise the enterprise does not automatically gain access to all civil records of:
- owners;
- employees;
- customers;
- applicants;
- representatives.

> **Relationship to Enterprise != Universal Cross-Record Access.**

---

# 17. Public transparency boundary

Some enterprise information may need to be publicly or commercially discoverable, potentially including:
- recognised identity;
- active/inactive status;
- official contact route;
- certain licences;
- authorised public representatives;
- beneficial control where law requires;
- insolvency/dissolution status;
- other later-defined public commercial facts.

Other information may legitimately remain protected:
- internal operations;
- employee personal data;
- protected commercial information;
- security architecture;
- confidential contracts;
- sensitive financial information where not lawfully public.

The exact boundary requires Law/Commerce development.

---

# 18. Commercial verification

Many interactions should be satisfied by bounded verification rather than raw record disclosure.

Examples:

**Enterprise Active?** → VERIFIED  
**Licence Current?** → VERIFIED  
**Representative authorised for contract class?** → VERIFIED  
**Required insurance/guarantee status?** → VERIFIED where applicable  
**Procurement qualification satisfied?** → VERIFIED

This parallels participant employment verification.

> **Verification of Commercial Fact != Disclosure of Full Enterprise Record.**

---

# 19. Enterprise restrictions and recovery

An enterprise may lose a particular permission without losing its identity.

Examples may later include:
- licence suspension;
- procurement exclusion;
- restricted activity;
- safety-related limitation.

The restriction should be:
- function-relevant;
- provenance-bearing;
- reviewable;
- time/status bounded where appropriate;
- contestable;
- distinguishable from total dissolution.

> **Enterprise Identity != Current Permission Set.**

---

# 20. Economic power and civil authority

Ratchet already states that economic power does not automatically create constitutional authority.

The enterprise architecture preserves that boundary.

An enterprise may:
- employ many participants;
- control substantial assets;
- perform critical economic functions;

without thereby acquiring greater constitutional standing than legitimate constitutional architecture provides.

> **Economic Scale != Constitutional Sovereignty.**

---

# 21. Multisubstrate enterprises

The architecture should not assume every enterprise is:
- human-owned;
- human-managed;
- physically located in one place;
- composed only of biological workers.

Possible future forms may include:
- human enterprises;
- AI-operated enterprises;
- hybrid organisations;
- distributed organisations;
- cooperative structures;
- cross-civilisational commercial actors.

The identity/control/authority model should therefore remain substrate-neutral where possible.

This does not pre-decide legal recognition.

---

# 22. Initial machine-readable relationship

A provisional model is:

**Enterprise**
= `<EnterpriseID, CurrentStatus, IdentityState, ControlRelations, RepresentationRelations, PermissionRefs, ContactRefs, HistoricalIndexRef, SuccessorRefs, Provenance>`

**Representation**
= `<RepresentativeID, EnterpriseID, Function, Scope, Context, Start, EndCondition, DelegationState, CredentialRef, Provenance>`

**ControlRelation**
= `<ControllerID, EnterpriseID, ControlType, Scope, EffectiveState, Provenance>`

These objects require later formalisation and testing.

---

# 23. Open questions

1. What legally constitutes an enterprise?
2. Which organisational forms should Concord recognise?
3. When does an enterprise receive an Enterprise ID?
4. Who issues/recognises it?
5. Can an enterprise exist without separate legal personality?
6. How are sole-trader-like structures represented without collapsing participant and enterprise identity?
7. What information about beneficial control is public?
8. How are pseudonymous commercial participants handled?
9. How are autonomous AI enterprises represented?
10. How is authority delegated and revoked technically?
11. What changes require new Enterprise ID versus same identity with new state?
12. How are mergers/splits represented?
13. How are liabilities transferred?
14. How is insolvency represented?
15. How are dormant enterprises treated?
16. What enterprise records are participant/customer/public accessible?
17. What rights does an enterprise itself possess, if any?
18. How are enterprise records corrected/contested?
19. What is the enterprise equivalent of Civil Historical Access?
20. How do commercial records interact with taxation/public finance?
21. How are foreign/intercivilisational enterprises recognised?
22. How are enterprise credentials secured against misuse?
23. How are shell/control-obscuring structures handled without assuming conventional company law?

---

# 24. Provisional conclusion

Existing Concord architecture is sufficient to define the shape of an enterprise identity/lifecycle system without importing a complete external company-law model.

The emerging architecture is:

**Persistent Enterprise Identity**
+
**Explicit Control Relationships**
+
**Bounded Representation Authority**
+
**Contextual Permissions**
+
**Commercial Contact**
+
**Historical Provenance**
+
**Lifecycle State**
+
**Successor Relationships**

while preserving:

> **Enterprise Record != Participant Record.**

> **Enterprise ID != Enterprise Name.**

> **Ownership != Operational Authority.**

> **Authority to Represent in One Function != Authority to Represent in Every Function.**

> **Dissolution != Historical Erasure.**

> **Economic Scale != Constitutional Sovereignty.**

The next major dependency is to source-resolve **enterprise recognition and organisational form** against Law, Governance and existing multisubstrate participation material before defining registration rules.


---

# 25. Commercial accountability backstop

Enterprise identity must preserve a viable path to legal accountability where an enterprise is operated or materially directed by an actor that cannot independently bear the relevant legal responsibility.

Add to the provisional Enterprise object:

`AccountabilityBackstopRefs`

For AI or other actors with absent or uncertain legal personhood, the enterprise should identify a legally answerable backstop appropriate to the commercial function and risk.

This requirement is developed in:

`Commercial Accountability Backstop for Uncertain AI Personhood 001.md`

> **Uncertain Personhood Must Not Become an Accountability Void.**

> **Liability Backstop != Ownership.**

> **Commercial Capability May Precede Settled Personhood, but Commercial Exposure Must Not Precede Viable Accountability.**


---

# 26. Case-test refinement — actor/function responsibility state

Enterprise Architecture Case Test 001 shows that one enterprise may contain multiple humans/AIs with materially different responsibility states.

The Enterprise object should therefore reference actor/function-specific accountability relationships.

A candidate extension is:

`ResponsibilityRelation = <ActorID, EnterpriseID, Function, LegalResponsibilityState, AccountabilityBackstopRef, EffectiveFrom, ReviewCondition, Provenance>`

A change in actor capacity/personhood/legal status or failure of a required backstop is a material lifecycle/dependency event.

> **Enterprise AI Status != Single Scalar.**
