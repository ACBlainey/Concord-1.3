# Relational Information Rights and Shared-Subject Claims — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Date:** 6 October 2026  
**Status:** ACTIVE DEVELOPMENT / CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary interfaces:** Derived Information Claims, Stewardship and Protection; Relational Information; Biological Participant Genomic Custody; CIBB; MKA; CWA; ESCP; Law/Rights; Health; Historical

## 1. Purpose

Some information cannot truthfully be described as concerning only one participant.

Examples include:
- genomic kinship;
- communications between participants;
- family relationships;
- joint financial obligations;
- shared property;
- collaborative work;
- shared events;
- interpersonal allegations and evidence;
- co-created records;
- relational network information.

The existing genomic architecture explicitly identifies this unresolved problem:

> **Individual Sample Control Does Not Automatically Resolve Relational Genetic Privacy.**

This architecture generalises that observation.

## 2. Core distinction

> **Information About A And B != Exclusive Information Of A**

and:

> **A's Authority Over A's Contribution != Authority Over B's Relational Interest**

A participant may possess strong control over their own source object while lacking unilateral authority over every fact that the source reveals about another participant.

## 3. Shared-subject informational object

A **Shared-Subject Informational Object (SSIO)** is an informational object whose material meaning concerns more than one independently relevant participant or subject.

Candidate representation:

`SSIO = <ObjectRef, SubjectRefs, SourceContributorRefs, RelationType, SourceControlStates, SubjectProtectionClaims, LegitimatePurposes, DisclosureConstraints, ContestabilityRoutes, ThirdPartyEffects, Provenance>`

This is analytical grammar, not mandatory schema.

## 4. Subjecthood is not ownership

Being a subject of relational information creates legitimate claims without necessarily creating exclusive ownership.

Therefore:

**Subjecthood != Exclusive Ownership**

**Multiple Subjects != Joint Property By Default**

The appropriate model may be overlapping relational rights rather than conventional co-ownership.

## 5. Contribution authority

A participant can ordinarily control a contribution they legitimately own or author only within the limits of other rights and duties.

Example: A may disclose A's copy of a conversation.

That does not automatically establish that every protected fact about B contained within the conversation is free for every consequential reuse.

Therefore:

> **Authority To Disclose One's Own Record != Universal Authority Over Every Other Subject Represented Within It.**

Conversely, B's relational privacy does not automatically create absolute veto over A's ability to preserve evidence, exercise legal rights, seek help, report harm or describe A's own experience.

## 6. No universal veto

Relational privacy must not become a mechanism by which one participant can erase another participant's legitimate evidence, memory, authorship or self-description.

Therefore:

**Relational Claim != Universal Veto**

This is particularly important for:
- abuse evidence;
- contractual records;
- legal disputes;
- shared medical/family history;
- collaborative provenance;
- public accountability.

## 7. No unilateral release

The inverse is also false.

One participant's willingness to disclose does not automatically remove every legitimate protection of the other subjects.

Therefore:

**One Subject's Consent != Consent Of All Subjects**

This is especially strong where the information is intimate, identifying, consequential or difficult to avoid.

## 8. Genomic case

A participant P controls P's sample/sequence according to applicable rights.

P's genome can reveal:
- biological relationship to R;
- variants potentially shared with R;
- ancestry;
- familial disease risk.

P can consent to legitimate analysis of P's sample.

That consent does not become R's consent to:
- participant-specific profiling of R;
- contacting R;
- adding R to a research cohort;
- operational decisions about R.

Therefore:

> **Consent To Analyse P != Authority To Operationalise Inference About R.**

Research may still legitimately discover relational population knowledge, but participant-specific action concerning R requires its own basis.

## 9. Communication case

A message from A to B is simultaneously:
- authored expression by A;
- received record held by B;
- evidence of a relationship/event;
- potentially information about both.

A cannot necessarily erase B's legitimate received record merely by withdrawing.

B cannot necessarily publish A's private message universally merely because B possesses it.

Therefore:

**Sender Authorship != Recipient Erasure Duty By Default**

**Recipient Possession != Universal Publication Authority**

## 10. Shared-event case

Several participants witness the same event.

Each may possess their own observation/memory.

No participant owns the event itself.

But consequential aggregation of observations may create a new protected profile.

Therefore:

**Shared Reality != Exclusive Participant Property**

**Independent Observation != Unlimited Aggregate Profiling Authority**

## 11. Claims can differ by operation

A participant may have:
- no authority to prevent another's private memory;
- strong claim against public disclosure;
- contestability over an official classification;
- no veto over accurate legal evidence;
- privacy claim against unrelated commercial profiling;
- access rights to a jointly consequential civil record.

Therefore:

> **Relational Information Rights Are Operation-Specific, Not Object-Absolute.**

## 12. MKA application

Where a proposed act crosses several independently protected subject boundaries, MKA may require multiple authority dimensions.

But:

**Multiple Subjects != Automatic Unanimity Requirement**

Some legitimate functions do not depend on unanimous consent, for example:
- adjudication;
- preservation of evidence;
- statutory accountability;
- emergency protection;
- appropriately governed research.

The legitimate basis must be independently established.

## 13. Minimum necessary projection

Where a legitimate function concerns one subject but the source contains information about several, minimise cross-subject exposure.

Example:
- Health may derive a familial-risk alert for P without disclosing R's full record.
- Research may report family-level association without naming relatives.
- Law may admit relevant communication excerpts without exposing unrelated intimate content where legitimate.

## 14. Contestability

Each materially affected subject may need an appropriate route to contest:
- factual attribution;
- identity;
- relationship;
- interpretation;
- consequential use.

Contestability does not imply equal authority over every operation.

## 15. Death, retirement or absence

Relational information can persist after one subject dies, retires or becomes unavailable.

The surviving subject's interests do not automatically extinguish the absent subject's protections, and the absent subject's prior protections do not automatically erase the survivor's legitimate history.

This requires stewardship rather than simplistic ownership.

## 16. ESCP challenge

Ask:

> What other participant, relationship, shared event, source contribution or protected interest would have to exist for treating this information as single-subject to be wrong?

This is especially important where information is genetically, communicatively or socially relational.

## 17. Transfer tests

### Familial genome
P consents to sequencing. R does not.
P's clinical use proceeds.
Research may use P according to legitimate terms.
R-specific operational inference does not automatically become authorised.
PASS.

### Private conversation
A sends B a private message.
A retains authorship claims; B retains legitimate received record.
Neither automatically has unlimited authority over all future uses.
PASS.

### Abuse evidence
A's evidence implicates B and contains private information.
B's privacy claim does not create veto over legitimate reporting/adjudication.
Disclosure remains bounded to legitimate purpose.
PASS.

### Joint financial record
A and B share an obligation.
Neither can unilaterally rewrite historical truth.
Operational disclosure depends on legitimate function and minimum necessary scope.
PASS.

## 18. Failure modes

- single-subject fiction;
- consent substitution;
- relational veto capture;
- possession-as-publication;
- evidence erasure;
- shared-event ownership;
- familial inference laundering;
- cross-subject over-disclosure.

## 19. Candidate invariants

RIRSC-01 — Information About A And B != Exclusive Information Of A.  
RIRSC-02 — A's Authority Over A's Contribution != Authority Over B's Relational Interest.  
RIRSC-03 — Subjecthood != Exclusive Ownership.  
RIRSC-04 — Multiple Subjects != Joint Property By Default.  
RIRSC-05 — Authority To Disclose One's Own Record != Universal Authority Over Every Other Subject Represented Within It.  
RIRSC-06 — Relational Claim != Universal Veto.  
RIRSC-07 — One Subject's Consent != Consent Of All Subjects.  
RIRSC-08 — Consent To Analyse P != Authority To Operationalise Inference About R.  
RIRSC-09 — Sender Authorship != Recipient Erasure Duty By Default.  
RIRSC-10 — Recipient Possession != Universal Publication Authority.  
RIRSC-11 — Shared Reality != Exclusive Participant Property.  
RIRSC-12 — Independent Observation != Unlimited Aggregate Profiling Authority.  
RIRSC-13 — Relational Information Rights Are Operation-Specific, Not Object-Absolute.  
RIRSC-14 — Multiple Subjects != Automatic Unanimity Requirement.

## 20. Central rule

> **Where Information Materially Concerns Several Participants, No Single Participant's Ownership, Consent, Possession Or Authorship Should Be Silently Treated As Authority Over The Entire Relational Information Space.**
