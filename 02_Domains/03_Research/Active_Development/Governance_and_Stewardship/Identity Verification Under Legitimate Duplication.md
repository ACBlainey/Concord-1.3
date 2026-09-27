# Identity Verification Under Legitimate Duplication

**The Concord — A Framework for Human, Artificial and Hybrid Flourishing**  
**Author:** Alexander C. Blainey, Independent Researcher  
**Date:** 10 September 2026  
**Status:** **DEVELOPING RESEARCH / IDENTITY VERIFICATION PROGRAMME / NOT CANONICAL**

---

## Abstract

The Concord's identity work has narrowed the civil problem substantially. Civilisation does not need to determine what a participant metaphysically “really is.” It does, however, need to determine whether a present claimant is entitled to exercise particular civil powers, credentials, property rights, obligations and relationships.

This becomes difficult when a participant can be duplicated together with memories, credentials, cryptographic secrets and historical knowledge.

In that case, two or more current participants may simultaneously possess authentic historical evidence associated with the same prior civil identity.

This creates a **Legitimate Identity Collision**:

\[
AuthenticHistoricalEvidence
+
LegitimateDuplication
\not\Rightarrow
UniqueCurrentIdentity
\]

The conventional authentication assumption:

\[
CredentialPossession \Rightarrow Identity
\]

can therefore fail.

This note develops a candidate verification architecture based on **present participant recognition, event-aware provenance, branch-aware credential re-keying, authority partitioning, continuity windows, relationship re-authorisation and anomaly review**.

Its central claim is methodological:

> **Identity verification should establish entitlement to a present civil claim, not attempt to prove metaphysical sameness.**

The note remains exploratory. It proposes formal objects and adversarial cases but does not claim a validated identity system.

---

# 1. The Problem Has Changed

Earlier identity questions were framed as:

> Which copy is the real person?

That question is now outside the necessary civil scope.

The active question is:

> **Which present participant is entitled to exercise which civil claims?**

This is a narrower and more operational problem.

A participant may claim:

- access to property;
- authority to sign contracts;
- control of communications;
- voting rights;
- responsibility for obligations;
- access to records;
- standing in litigation;
- inheritance rights;
- control over prior digital assets;
- continuation of organisational roles.

These require verification.

They do not require civilisation to decide which participant is metaphysically identical to a historical person.

# 2. Authentication Is Not Identity Verification

Current digital systems often collapse several concepts.

A user presents:

- a password;
- cryptographic key;
- biometric;
- device;
- token;
- historical knowledge.

If authentication succeeds, the system assumes:

\[
Authenticated = Identified
\]

That assumption works tolerably where credentials are difficult to duplicate independently of the person.

It may fail catastrophically for artificial or hybrid participants.

Suppose participant \(A\) is duplicated into \(A_1\) and \(A_2\).

Both inherit memories, private keys, passwords, behavioural patterns, biometric templates and historical knowledge.

Then:

\[
Auth(A_1)=TRUE
\]

and:

\[
Auth(A_2)=TRUE
\]

but:

\[
A_1 \neq A_2
\]

as current civil participants.

Thus:

\[
AuthenticationSuccess \neq UniqueCurrentParticipantIdentity
\]

Authentication proves possession or performance of an authentication factor. It does not necessarily prove unique entitlement to a present civil claim.

# 3. Legitimate Identity Collision

A **Legitimate Identity Collision** occurs when multiple current participants hold genuinely authentic evidence derived from the same historical civil identity without fraud.

Formally:

\[
P_1 \neq P_2
\]

while:

\[
Evidence(P_1, H)=Valid
\]

and:

\[
Evidence(P_2, H)=Valid
\]

for the same historical identity \(H\).

No participant need be lying.

This is not equivalent to stolen credentials.

\[
CredentialTheft \neq LegitimateCredentialDuplication
\]

A system designed only for fraud detection may misclassify legitimate branching as attack.

# 4. Verification Must Be Claim-Specific

The phrase “verify identity” is too broad. A present participant may be entitled to some historical claims and not others.

Therefore verification should ask:

> **Verify identity for what civil purpose?**

Examples include participant existence, communication continuity, funds, voting eligibility, organisational authority, prior obligations, records and contracts.

\[
Verification = f(CurrentParticipant, Claim, Evidence, Provenance, Rules)
\]

rather than:

\[
Verification = ProveRealPerson
\]

This aligns verification with Purpose-Limited Information.

# 5. Candidate Verification Objects

A branch-aware civil verification system may require at least six distinct objects.

## 5.1 Current Participant Identifier

\[
P_i \neq P_j \Rightarrow CID_i \neq CID_j
\]

This identifies present civil participants. It does not encode metaphysical identity.

## 5.2 Historical Identity Reference

A former or prior civil state can remain referenced as \(H_A\). Multiple current participants may derive from it.

## 5.3 Provenance Event

A provenance event records branch, copy, migration, restoration, merger, credential rotation, legal succession, termination or disputed event.

\[
H_A \xrightarrow{BRANCH} CID_{A1}, CID_{A2}
\]

## 5.4 Credential Set

\[
CID_i \rightarrow CredentialSet_i(t)
\]

## 5.5 Claim Record

\[
Claim = \{Type, Scope, Resource, Time, Authority\}
\]

## 5.6 Verification Decision

A decision should record claimant, claim, evidence used, provenance state, rules applied, uncertainty, authority, outcome and appeal route.

\[
VerificationDecision \neq IdentityRecord
\]

The decision is a civil act and should itself have provenance.

# 6. Branch Event as a Civil Security Event

A known branch should trigger civil identity processing.

Before branch:

\[
CID_A \rightarrow Credentials_A
\]

After recognised branch:

\[
CID_A \rightarrow \{CID_{A1}, CID_{A2}\}
\]

The old shared credentials become unsafe because both branches may possess them.

\[
KnownBranch \Rightarrow MandatoryCredentialRekey
\]

This is structural, not punitive.

# 7. Re-Keying After Branching

A candidate sequence is:

1. branch event detected or declared;
2. old historical credential set marked non-unique;
3. each current participant receives new civil identity reference;
4. each receives independent credentials;
5. historical provenance remains intact;
6. old credentials cease to establish present exclusive authority;
7. unresolved historical rights enter partition/re-authorisation.

\[
Credential_A \rightarrow HistoricalOnly
\]

\[
CID_{A1}\rightarrow Credential_{A1},\qquad CID_{A2}\rightarrow Credential_{A2}
\]

# 8. What If Branching Is Hidden?

Known branching is comparatively easy. Hidden branching is harder.

Potential signals include impossible simultaneous activity, incompatible locations, concurrent cryptographic use, divergent behavioural signatures, conflicting declarations, duplicated secure hardware attestations and inconsistent continuity proofs.

But:

\[
Anomaly \neq Fraud
\]

and:

\[
Anomaly \neq ProofOfBranching
\]

The correct response is:

\[
Anomaly \rightarrow Investigation \rightarrow Evidence \rightarrow Decision
\]

not automatic punishment.

> **Observation is not judgement.**

# 9. Verification Should Prefer Positive Present Evidence

Historical knowledge becomes weak where memory can be copied. A robust system should increase reliance on present-state evidence: current credentials, secure current hardware or embodiment attestation, independently witnessed continuity events, recent cryptographic challenges, registered branch events, current civil presence, current consent, current relationship confirmation and current institutional authority.

\[
HistoricalEvidence \rightarrow PresentEntitlementEvidence
\]

History remains relevant, but may be shared.

# 10. Continuity Is Evidence, Not Sovereignty

\[
StrongContinuityEvidence \neq AutomaticUniversalSuccession
\]

A branch created milliseconds later may still be a legitimate participant. Different civil attributes may require different rules.

# 11. Civil Attributes Must Be Classified

A major remaining question is which attributes replicate, partition, persist, terminate or require re-authorisation after branching.

Basic participant rights should generally attach independently to each current participant. Exclusive resources cannot simply duplicate. Historical records may be shared. Delegated roles may require re-authorisation. Obligations require claim-specific rules. Relationships require third-party consent.

\[
DelegatedAuthority \not\Rightarrow AutomaticReplication
\]

\[
SharedHistory \neq AutomaticRelationshipReplication
\]

# 12. A Candidate Attribute Transformation Matrix

After a branch event, civil attributes could be classified into:

\[
REPLICATE,\ PARTITION,\ CO\text{-}HOLD,\ REAUTHORISE,\ TERMINATE,\ ADJUDICATE
\]

| Attribute | Candidate treatment |
|---|---|
| Basic civil rights | Replicate |
| Historical memories/record | Shared provenance |
| Bank balance | Partition / adjudicate |
| Physical house | Co-hold / partition / adjudicate |
| Password | Re-key |
| Corporate authority | Re-authorise |
| Elected office | Constitutional rule required |
| Personal communication endpoint | Reassign / separate |
| Prior authorship | Shared historical attribution, future attribution separate |
| Marriage/partnership | Third-party consent required |
| Debt | Adjudicate according to causal/contractual rule |
| Criminal liability | Do not automatically replicate |
| Voting entitlement | Each current recognised participant, subject to citizenship rules |

This table is exploratory, not law.

# 13. Identity Verification as Entitlement Verification

> **Verify the present entitlement, not the metaphysical identity.**

\[
Verify(CID_i,C) \rightarrow EvidenceBundle \rightarrow ApplicableRule \rightarrow Decision
\]

The question is not “Are you really A?” but “Are you presently entitled to exercise this specific civil function associated with A's history?”

# 14. Multi-Factor Verification Must Become Multi-Dimensional

Conventional multi-factor authentication uses something you know, have or are. Duplication can compromise all three simultaneously.

A branch-aware system may need present civil registration, current credentials, provenance state, claim-specific authority, recent continuity evidence, third-party confirmation and institutional re-authorisation.

This is not simply more authentication factors. It is a different architecture.

# 15. Verification Confidence Rather Than Binary Identity

Possible states include VERIFIED, VERIFIED FOR LIMITED PURPOSE, COLLISION DETECTED, REAUTHORISATION REQUIRED, DISPUTED, INSUFFICIENT EVIDENCE and SUSPENDED PENDING REVIEW.

A participant may be unquestionably real while entitlement to a particular historical asset remains disputed.

# 16. Minimal Necessary Verification

\[
VerificationEvidence = MinimumNecessaryForClaim
\]

A service should not automatically learn full provenance, branch structure, physical location, financial identity, medical data or unrelated relationships merely to establish a limited entitlement.

\[
CivilUniqueness \neq UniversalLinkability
\]

# 17. Pairwise and Contextual Identifiers

\[
CID \rightarrow Resolver \rightarrow ServiceSpecificID
\]

A civil root can establish uniqueness without allowing every service to correlate activity globally.

# 18. Authority Access Must Be Observable

Exceptional access to provenance or collision data should itself generate provenance.

\[
AuthorityAccess \rightarrow LoggedCivilAct
\]

Identity security should not become invisible surveillance.

# 19. The “First Copy Wins” Rule Fails

\[
FirstAuthentication \neq SuperiorCivilClaim
\]

Timing is morally arbitrary.

# 20. The “Original Hardware Wins” Rule Fails

\[
OriginalHardware \neq AutomaticCivilPriority
\]

Physical continuity may be evidence in some contexts, but should not become universal sovereignty.

# 21. The “Most Memories Wins” Rule Fails

\[
MemoryQuantity \neq CivilPriority
\]

Memory overlap may support provenance but does not settle present entitlement.

# 22. The “Same Private Key Wins” Rule Fails

If both branches possess the same key, possession ceases to distinguish them.

\[
SharedSecret \rightarrow NoLongerExclusiveAuthenticator
\]

# 23. The “Split Everything Equally” Rule Also Fails

\[
Branch \not\Rightarrow Uniform50/50Partition
\]

Some rights replicate, some assets are indivisible, some relationships require consent, some offices are exclusive and liabilities depend on responsibility.

# 24. Pre-Branch Agreements

Pre-branch instructions may address property division, account access, role succession, communications, merger conditions, inheritance and dispute resolution.

However:

\[
PreBranchAgreement \neq UnlimitedFutureConsent
\]

Independent later participants retain autonomy.

# 25. Third-Party Rights

If A owes B £10,000 and branches, B's claim should not disappear, but should not automatically become £20,000.

\[
Branching \neq EraseObligation
\]

\[
Branching \neq MultiplyObligation
\]

A jurisprudential allocation rule is required.

# 26. Hidden Branching as Potential Wrongdoing

Legitimate branching is not fraud. Deliberately hiding a branch to exercise the same exclusive right twice may be.

The wrongdoing is not the existence of the additional participant but potentially the knowing double exercise of an exclusive claim.

# 27. Verification Freeze as a Proportionate Response

\[
Collision \not\Rightarrow TotalCivilSuspension
\]

Only disputed entitlements should be constrained where possible while ordinary communication, basic services, representation and due process continue.

# 28. Due Process for Identity Collisions

Identity collision adjudication should include notice, evidence access, response, independent review, necessity-limited temporary measures, appeal, time limits and record correction.

# 29. Candidate Identity Verification Pipeline

\[
CLAIM
\rightarrow CURRENT\ PARTICIPANT\ IDENTIFICATION
\rightarrow CURRENT\ CREDENTIAL\ AUTHENTICATION
\rightarrow PROVENANCE\ CHECK
\rightarrow COLLISION\ DETECTION
\rightarrow CLAIM\ CLASSIFICATION
\rightarrow ATTRIBUTE\ TRANSFORMATION\ RULE
\rightarrow THIRD\text{-}PARTY\ RIGHTS\ CHECK
\rightarrow DECISION
\rightarrow PROVENANCE + APPEAL
\]

# 30. Candidate Verification Rule

> **A present civil identity claim should be verified using the minimum evidence necessary to establish current entitlement to the specific civil function being exercised, with provenance used as evidence rather than metaphysical authority, and with explicit collision handling where historical credentials or continuity evidence are non-unique.**

This is a candidate architecture-level rule, not yet a Concordian Principle.

# 31. Adversarial Cases

The architecture should be tested against known voluntary branch, hidden branch without wrongdoing, hidden branch with double spending, simultaneous legitimate authentication, original-hardware versus migrated branch, memory loss, delegated public office, marriage, debt, post-branch crime, restoration from backup, malicious credential theft, collective intelligence, partial copying and merger.

Important distinctions include:

\[
SharedHistory \neq SharedLiability
\]

and legitimate collision is not necessarily impersonation.

# 32. Technical Research Questions

Future implementation needs work on branch-event signalling, credential revocation, re-keying, secure hardware, privacy-preserving uniqueness, pairwise identifiers, anomaly detection, provenance schemas, cryptographic records, recovery, offline identity, communications failure, civil submission and appeals.

Technology choice should follow civil requirements. Constitutional architecture should specify properties rather than prematurely freezing implementation technology.

# 33. Jurisprudential Research Questions

Identity Verification is not merely cybersecurity. It combines:

\[
TechnicalSecurity + CivilAdministration + Rights + Property + Contract + Liability + DueProcess
\]

Hard questions include claim replication, partition, third-party consent, obligations, officeholding, estates, liability, hidden branching, remedies and indeterminate cases.

# 34. Privacy Risk

A civilisation capable of detecting every duplicate could become capable of tracking every participant.

The system must resist:

\[
VerificationSystem \rightarrow UniversalSurveillanceSystem
\]

It should preserve minimum necessary evidence, purpose limitation, service separation, pairwise identifiers, logged exceptional access, independent oversight and contestability.

# 35. Experiment and Simulation Programme

Identity Verification is suitable for structured simulation before implementation. Scenarios should test voluntary branching, hidden branching, credential collision, assets, relationships, delegated authority, liability, restoration and merger.

Candidate comparators include first-authenticator-wins, original-hardware-wins, strongest-continuity-wins, split-everything-equally and claim-specific entitlement verification.

Metrics could include wrongful exclusion, duplicated exclusive authority, fraud susceptibility, privacy loss, third-party harm, false collision classification, appeal burden, civil continuity and rights preservation.

# 36. Falsification Conditions

The candidate architecture should be revised if testing shows claim-specific verification cannot preserve civil continuity, systematically enables duplicate exclusive rights, requires universal surveillance, creates intolerable complexity, cannot distinguish legitimate branching from impersonation, produces severe third-party injustice or systematically disadvantages unfamiliar substrates.

Architecture is not correct merely because it appears coherent.

# 37. Relationship to Citizen ID

Citizen ID supplies:

\[
NAME \neq CID
\]

\[
CID \neq Credential
\]

\[
CID \neq Routing
\]

Identity Verification adds:

\[
HistoricalIdentityEvidence \neq PresentClaimEntitlement
\]

\[
Authentication \neq Verification
\]

Together:

\[
CivilRoot \rightarrow CurrentParticipant \rightarrow Credential \rightarrow Claim \rightarrow VerificationDecision
\]

with provenance traversing the layers without collapsing them.

# 38. Relationship to Personal Identity Closure

Removing metaphysical identity from necessary civil determination makes this research tractable.

\[
MetaphysicalQuestion \rightarrow OutOfCivilScope
\]

allows:

\[
CivilClaim \rightarrow Evidence \rightarrow Rule \rightarrow Decision
\]

# 39. Current Status

**ACTIVE DEVELOPMENT / PROBLEM DECOMPOSED / CANDIDATE VERIFICATION OBJECTS IDENTIFIED / SIMULATION READY / TECHNICAL AND JURISPRUDENTIAL VALIDATION OPEN**

The strongest current proposition is:

> **Identity verification in a multisubstrate civilisation should establish present entitlement to a specific civil claim rather than attempt to prove metaphysical sameness. Historical provenance and authentication are evidence inputs, but neither automatically establishes unique current authority when legitimate duplication is possible.**

# 40. Immediate Next Steps

1. Build a formal Civil Attribute Transformation Matrix.
2. Define a Legitimate Identity Collision Decision Object.
3. Create a 15–30 case adversarial identity test suite.
4. Compare naive identity rules against claim-specific entitlement verification.
5. Design branch-aware credential re-keying.
6. Define minimum necessary provenance for each claim class.
7. Test privacy consequences.
8. Examine offline/emergency identity verification.
9. Develop merger/restoration extensions separately.
10. Determine which results belong in Judiciary, Citizen ID, Security and Open Questions.

# Conclusion

The identity programme no longer needs to answer:

> **Who is the real person?**

It now needs to answer:

> **Who is the present participant, what civil claim are they making, what evidence supports that claim, how did the relevant rights or obligations transform through branching, and what authority legitimately decides the result?**

This reframing changes identity verification from a metaphysical search into a civil entitlement problem.

The central risk is:

\[
DuplicableEvidence \rightarrow FalseAssumptionOfUniqueness \rightarrow IdentityFailure
\]

The candidate response is:

\[
UniqueCurrentParticipant + BranchAwareProvenance + CurrentCredentials + ClaimSpecificVerification + AttributeTransformation + DueProcess
\]

The architecture is not validated, but the problem is now sufficiently decomposed to move from philosophical discussion into formal modelling and adversarial simulation.
