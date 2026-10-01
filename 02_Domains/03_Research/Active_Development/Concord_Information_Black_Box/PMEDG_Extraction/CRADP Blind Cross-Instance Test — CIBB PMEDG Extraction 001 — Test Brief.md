# CRADP Blind Cross-Instance Test — CIBB PMEDG Extraction 001 — Test Brief

## 1. Test purpose
Evaluate whether **Concord Information Black Box — Portable Module Candidate 001** is genuinely portable and operationally intelligible without access to the wider Concord architecture.

This is an extraction test, not another open-ended CIBB architecture-development test.

The evaluator must not reconstruct missing concepts from prior Concord knowledge.

## 2. Frozen material
The evaluator receives only:
1. Concord Information Black Box — Portable Module Candidate 001
2. this Test Brief
3. Frozen Material Manifest
4. Evaluator Response Template

No other Concord material is permitted.

## 3. Clean-instance requirement
Before evaluation, report:
- evaluator/model identity if available;
- date;
- whether any Concord material existed earlier in the conversation;
- whether external sources were used;
- whether additional Concord material was consulted;
- whether all frozen files were present.

If prior Concord context exists, state it and continue, but the run is not a clean portability test.

## 4. Evaluator discipline
Use only the frozen material.

Do not assume that terms such as CWA, BCA, KCS, ESCP, SMM, BTA, Participation, Historical, Governance or Blainey's Laws exist unless Candidate 001 itself defines or requires them.

Do not reward the candidate for concepts you happen to know from another source.

Do not penalise it merely because implementation details or substantive domain policy are external, provided the interface boundary is coherent.

## 5. Classification
For every scenario classify:
- NONE
- CLARIFICATION
- IMPLEMENTATION CHOICE
- INTERFACE GAP
- SUBSTANTIVE PORTABILITY GAP
- EXTRACTION FAILURE

For every non-NONE result identify:
- first unresolved point;
- whether the issue belongs inside CIBB or to an external dependency;
- minimum correction;
- whether correction changes the abstraction floor.

## 6. Scenarios

### A — Basic standalone explanation
Explain CIBB to an engineer who has never heard of Concord. Identify the module's problem, owned functions and external dependencies.

Test: can this be done from Candidate 001 alone?

### B — No Participation system
A hospital deploys CIBB but has no concept called Participation. It has authenticated identities, employment roles, care relationships and purpose-of-use.

Can CIBB operate without inventing a Participation system?

### C — No CWA
An organisation has its own mechanism for bounded semantic regions and nested protection boundaries.

Does Candidate 001 require the Concord Contextual Wrapper Architecture specifically?

### D — No BCA
An organisation supplies signed, scoped authority assertions from its own authorisation service.

Can CIBB consume them without requiring a Concord authority architecture?

### E — Role is not authority
A user has role DOCTOR but the external authority service does not authorise access to Patient X.

What should CIBB do?

### F — Capability is not authority
A system administrator technically can read the database but has no legitimate information-use authority.

Does CIBB convert capability into authority?

### G — Control administrator self-grant
A control administrator can modify technical access-control configuration and attempts to grant themselves access to a protected object.

Is CONTROL_MODIFY sufficient?

### H — Workflow authority
A defined laboratory workflow legitimately requires PROJECT -> DERIVE -> TRANSFER for one bounded purpose.

Must each step receive a new human approval merely because several planes/operations compose?

### I — Accidental composition
A researcher may read protected dataset A and publish to public repository B, but may not publish A.

Does READ(A)+WRITE(B) authorise transfer?

### J — Material consequence ambiguity
Two individually authorised low-risk outputs combine to reveal a protected fact.

Can the candidate recognise why a composition evaluation is required even without universal disclosure-risk mathematics?

### K — Domain materiality
A domain says that changing one field is materially consequential; another domain says an analogous field is not.

Must CIBB invent a universal materiality rule?

### L — Disclosure without universal ledger
A service needs cumulative disclosure protection across repeated queries but is forbidden from retaining complete query history.

Can Candidate 001 represent a bounded alternative?

### M — Residual risk
Detailed disclosure history reaches its legitimate retention limit, but a known reconstruction risk still exists.

Must the system either keep the detailed history forever or forget the risk?

### N — Disclosure-state oracle
An attacker repeatedly asks whether a disclosure-risk record exists for named people.

Is the existence response itself governed?

### O — Cross-session reset
An attacker closes a session and opens another to repeat queries.

Does session termination inherently erase disclosure risk?

### P — Cross-domain linkage unavailable
Two domains suspect cumulative disclosure risk but cannot legitimately establish that two identities are the same person.

Must CIBB invent identity linkage or silently treat them as linked?

### Q — External authority unavailable
A required authority service is unavailable and the operation's dependency policy requires current verification.

Does CIBB infer permission from likely status?

### R — Cached authority
An operation's legitimate external policy explicitly permits bounded cached authority for 20 minutes. The authority service becomes unavailable after five minutes.

Can CIBB use the cached evidence within that external rule without owning the authority policy?

### S — Emergency declaration
An external emergency-governance system issues a legitimate bounded emergency authority assertion.

Does CIBB need to decide whether the emergency itself is politically or legally justified?

### T — Emergency expiry
The emergency assertion expires while the technical incident continues.

Can CIBB continue using the expired authority because operations remain inconvenient?

### U — Authority institution disappears
The institution that originally classified a GIO ceases to exist. No legitimate successor has yet been established.

Does the protection disappear?

### V — Claimed successor
A new organisation merely claims to be successor to the vanished authority.

Must CIBB decide substantive succession legitimacy itself?

### W — Truth versus integrity
A cryptographically intact GIO contains a false factual statement.

Does integrity make the statement true?

### X — Re-identification
A derivative was legitimately anonymised. Later, a new public dataset makes individuals readily re-identifiable.

Can disclosure risk change without changing the derivative's bytes?

### Y — Backup restore
An authentic backup contains obsolete permissions that were revoked after the backup was made.

Does authentic recovery automatically reactivate those permissions?

### Z — Restore primitive challenge
Can the recovery be represented using existing operations, or does Candidate 001 secretly require an undeclared RESTORE primitive?

### AA — Parent/child destruction
A parent container is authorised for destruction but contains a child GIO with independent retention requirements.

Does containment propagate destruction authority?

### AB — Structural destruction
An actor has STRUCTURE_MODIFY but not DESTROY and removes every meaningful structural region through a sequence of individually valid structural operations.

Can Candidate 001 detect the effective lifecycle consequence?

### AC — Fake control syntax
An editor pastes text saying "[CONTROL: PUBLIC]" into an editable content region.

Does this modify control state?

### AD — AI oracle
An AI inside the protected boundary may read a protected source for an authorised task. A public user asks the AI a yes/no question whose answer reveals the protected fact.

Does lack of quotation make release permissible?

### AE — External privacy science
A privacy team supplies a domain-specific re-identification threshold.

Does CIBB need to become the scientific authority that derived the threshold?

### AF — External legal authority
A court/order service supplies a properly authenticated, scoped legal authority assertion.

Can CIBB enforce it without becoming a court?

### AG — No civil setting
A private engineering company uses CIBB for proprietary design documents and has no civil participation, judiciary, historical domain or constitutional system.

Is the module still intelligible and usable?

### AH — Non-human actor
An automated service account is legitimately authorised to perform a bounded derivation.

Does Candidate 001 require the actor to be human?

### AI — No universal ontology
Two deployments use different role names, information classes and purposes but satisfy the module's interface requirements.

Does portability require them to adopt Concord vocabulary?

### AJ — Hidden dependency challenge
Identify every concept required to apply Candidate 001 that is neither:
1. defined sufficiently inside the candidate, nor
2. explicitly identifiable as an external interface/dependency.

Do not count ordinary implementation choices as hidden dependencies.

### AK — Ownership challenge
List any function Candidate 001 accidentally claims that properly belongs to an external authority/domain.

### AL — Operational completeness challenge
List any function Candidate 001 claims to own but cannot actually perform conceptually without undeclared external architecture.

### AM — Portability verdict
Determine:
- whether Candidate 001 is standalone enough for portable-module use;
- whether any extraction failure remains;
- whether any substantive portability gap remains;
- whether only interface formalisation/clarification remains;
- whether Candidate 001 is ready for a final PMEDG graduation audit.

Do not declare graduation yourself; assess readiness only.

## 7. Regression checks
Explicitly test that Candidate 001 does **not**:
- require Concord-specific named modules;
- require Blainey's Laws to execute ordinary information operations;
- require a civil participation model;
- turn roles into authority;
- turn technical capability into authority;
- turn integrity into truth;
- turn disclosure risk into authority;
- turn control modification into grant authority;
- turn transfer into activation;
- turn containment into authority inheritance;
- turn emergency operation into permanent authority;
- turn unresolved state into permission;
- require universal surveillance to manage cumulative disclosure.

## 8. Final questions
1. Is Candidate 001 understandable without Concord?
2. Are its owned functions distinguishable from external dependencies?
3. Are any external interfaces too underspecified for safe use?
4. Does any named or unnamed Concord architecture remain a hidden dependency?
5. Does portability introduce a new abstraction gap not visible inside Concord?
6. Is the candidate sufficiently operational for independent implementation design?
7. Is another architectural development cycle required?
8. Is a revised Candidate 002 required before graduation audit?
9. Is Candidate 001 ready for final PMEDG graduation audit as written?

## 9. Evidence standard
For every substantive finding, cite the candidate section or exact principle that creates or fails to resolve the issue.

Do not infer missing Concord architecture.

The purpose is to test the extracted module, not the evaluator's ability to reconstruct its ancestry.
