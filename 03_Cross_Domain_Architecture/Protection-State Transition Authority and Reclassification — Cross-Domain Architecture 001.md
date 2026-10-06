# Protection-State Transition Authority and Reclassification — Cross-Domain Architecture 001

**Project:** The Concord Framework  
**Date:** 6 October 2026  
**Status:** ACTIVE DEVELOPMENT / CROSS-DOMAIN ARCHITECTURE / PROVISIONAL / NON-CANONICAL  
**Primary interfaces:** Derived Information Protection-Lineage and Transformation Boundaries; CIBB; Multi-Key Authority (MKA); Minimum Necessary Capability (MNC); Private Local Evaluation (PLE); ESCP/ASCP; Historical; KCS Change Propagation; BTA; civil review and judiciary

## 1. Purpose

A Legitimate Transformation Boundary (LTB) can establish that a derived informational object has a materially different protection state from its source.

That raises a necessary authority question:

> Who may legitimately determine that the boundary has been crossed?

If the holder of information can unilaterally declare its own derivative anonymous, declassified, non-sensitive or unrestricted, protection can be defeated by relabelling.

If every participant or source contributor possesses an absolute veto over every protection transition, useful aggregation, research, statistics, accountability and public knowledge can become impossible.

This architecture defines the authority and review interface for consequential protection-state transitions.

## 2. Core distinction

Three questions must remain separate:

1. **Epistemic classification** — what does the output actually reveal or enable?
2. **Protection classification** — what protections apply to that resulting information state?
3. **Transition authority** — who may legitimately commit the change in governed protection state?

Therefore:

> **Ability To Assess Protection State != Authority To Change Protection State**

and:

> **Protection-State Evidence != Protection-State Authority**

## 3. No universal classifier

There is no single actor who should automatically own all protection-state transitions.

Required authority depends upon the protected boundaries implicated by the actual transformation.

Potential authority dimensions can include:
- participant consent or participant-held rights;
- source-object stewardship;
- domain-specific authority;
- confidentiality/fiduciary duties;
- legal or constitutional protection;
- third-party rights;
- institutional information stewardship;
- research authority;
- historical retention authority;
- security constraints;
- public disclosure authority.

Therefore:

> **Protection Transition Authority Is Contextual, Not Universal.**

## 4. MKA composition

MKA already provides the correct generic mechanism for consequential acts crossing independently protected authority boundaries.

For a proposed transition:

`ProtectedState A -> NewProtectionState B`

first identify the actual act:
- transform;
- anonymise;
- aggregate;
- declassify;
- disclose;
- re-purpose;
- publish;
- archive;
- destroy source linkage;
- certify non-linkability;
- or another consequential information operation.

Then ask which independently protected authority dimensions are required.

> **Authority Verification != Authority Creation**

> **All Represented Keys Valid != All Required Keys Represented**

A protection transition may proceed only where the actual route has the required legitimate authority.

## 5. Transition verifier versus authority source

A privacy, security, research, Historical or technical evaluator may assess whether a transformation meets declared criteria.

That evaluator does not become the source of every authority required for the transition.

Therefore:

> **Protection-State Verifier != Protection-State Authority Source**

A verifier can establish evidence such as:
- direct identifiers removed;
- k-anonymity-like threshold satisfied;
- bounded projection contains no declared protected field;
- re-identification test passed;
- semantic exposure reduced;
- query-composition risk below declared threshold.

But the legitimate basis for acting on that evidence remains external.

## 6. Routine pre-authorisation

Not every transformation requires a committee or bespoke decision.

A legitimate policy can pre-authorise a bounded class of transformations where:
- purpose is stable;
- method is validated;
- consequence is low or understood;
- output class is bounded;
- authority sources are established;
- expiry/review is defined where needed;
- deviations route to review.

Example:

A Health service may pre-authorise routine generation of a bounded appointment reminder from protected scheduling data.

The operator need not seek fresh constitutional authority for every reminder.

> **Pre-Authorised Transformation != Unauthorised Automation**

## 7. Consequence-banded transition review

Review burden should scale with:
- sensitivity;
- identifiability;
- number of participants;
- scope of release;
- persistence;
- publicness;
- purpose change;
- irreversibility;
- downstream decision consequence;
- re-identification risk;
- externality;
- uncertainty.

Candidate bands:

### T0 — Internal equivalent-state transformation
Encoding/storage/internal formatting where protected meaning and audience do not materially change.

No substantive protection transition is claimed.

### T1 — Bounded projection
Minimum-necessary output to an already legitimate recipient for established purpose.

Can commonly be pre-authorised.

### T2 — Protection narrowing
Output removes material detail/identity but remains protected or purpose-bounded.

Requires validated transformation and legitimate disclosure/use basis.

### T3 — Participant-specific protection termination
A source-specific participant protection is claimed no longer to apply.

Requires stronger evidence and authority because error may expose a participant.

### T4 — Broad/public release or irreversible declassification
Highest ordinary burden; may require independent assessment and multiple authority keys.

These bands are provisional and need not become universal labels.

## 8. Independence

Where the actor benefiting from declassification also controls the classification process, incentive conflict exists.

For consequential transitions, require proportionate independence.

> **Beneficiary Of Reduced Protection != Sufficient Sole Certifier By Default**

This does not require external review for every low-risk operation.

Independence burden scales with consequence and conflict.

## 9. Participant role

A participant's consent can be a required authority key where the protected interest is legitimately theirs to control.

But participant consent does not automatically extinguish:
- third-party privacy;
- legal retention duties;
- evidential integrity;
- public accountability requirements;
- another participant's rights;
- security restrictions.

Therefore:

> **Participant Consent != Universal Declassification Authority**

Conversely, institutional ownership or public-interest claims do not erase participant-held protections.

## 10. Technical anonymisation authority

Technical experts can evaluate anonymisation properties.

They do not thereby acquire authority to release the output.

> **Anonymisation Expertise != Disclosure Authority**

Likewise:

> **Disclosure Authority != Proof Of Anonymisation**

Both may be required.

## 11. Disputed transition state

A protection transition can be disputed.

Candidate states:
- PROPOSED;
- VALIDATED_WITHIN_SCOPE;
- AUTHORISED;
- ACTIVE;
- DISPUTED;
- REVIEW_DUE;
- SUPERSEDED;
- REVOKED_FOR_FUTURE_USE;
- HISTORICAL_ONLY.

Dispute does not automatically prove the transition invalid.

But where consequence warrants, disputed status can suspend new dissemination or trigger bounded review.

> **Disputed != Invalid**

> **Disputed != Safe To Ignore**

## 12. Re-identification and changed context

A legitimate anonymisation decision can later become stale because:
- new public datasets appear;
- computational capability changes;
- population size changes;
- another dataset becomes linkable;
- repeated releases create a mosaic;
- a rare attribute becomes identifying.

Therefore:

`ProtectionStateAt(t1) != GuaranteedProtectionStateAt(t2)`

A material re-identification route can trigger review.

STRA can route the review.

KCS Change Propagation can identify affected downstream objects.

BTA can coordinate consequential protection-state transition where state actually changes.

## 13. Revocation versus historical validity

If a previously legitimate public release later becomes re-identifiable, the earlier decision is not automatically retroactively illegitimate.

The current system may nevertheless need to:
- stop future release;
- reduce future precision;
- alter access;
- issue correction/warning;
- change linkage keys;
- withdraw controlled copies where feasible and legitimate;
- reassess downstream use.

Therefore:

> **Current Protection Failure != Automatic Historical Wrongdoing**

and:

> **Historical Legitimacy != Current Continuation Authority**

## 14. Irreversible public disclosure

Some disclosures cannot realistically be recalled.

This increases the burden before release.

Where public release is effectively irreversible:

> **Irreversibility Raises Pre-Transition Completeness And Authority Burden.**

This directly follows ESCP and MNC.

It does not require certainty; it requires proportionate completeness and caution.

## 15. Right to contest classification

Where protection classification materially affects a participant, there should ordinarily be a route to contest:
- factual assumptions;
- identity/linkability assessment;
- semantic exposure;
- purpose;
- claimed consent;
- expiry;
- recipient class;
- consequential use.

Contestability does not automatically give the participant veto over all public facts or independently legitimate information.

> **Right To Contest != Automatic Right To Control Every Outcome**

## 16. Classification provenance

Consequential transition records should preserve enough provenance to answer:
- what changed;
- from which protection state;
- to which protection state;
- transformation method/version;
- evidence;
- legitimate authority basis;
- required authority keys;
- verifier;
- scope;
- purpose;
- date;
- expiry/review condition;
- uncertainty;
- contest/review history.

The record itself may need protection.

## 17. Protection-state rollback

If a transition is found defective, simply restoring the previous label may be insufficient.

Information may already have propagated.

Therefore:

**Protection-State Rollback != Restoration Unless Prior Exposure State Is Actually Re-established**

This is a direct BTA application.

Remedy may instead require a successor state:
- stop further disclosure;
- mark compromised;
- notify affected legitimate parties;
- change credentials/identifiers;
- constrain downstream use;
- preserve evidence;
- provide remedy;
- establish a new bounded protection state.

## 18. Source destruction

An anonymisation process may propose destroying the source linkage after validation.

That is a separate lifecycle act.

> **Authority To Anonymise != Authority To Destroy Source**

CIBB lifecycle authority and Historical/legal retention requirements remain independently relevant.

Likewise:

> **Authority To Retain Source != Authority To Re-Link Anonymised Output**

## 19. Public information

Information being public can alter the protection analysis.

It does not automatically remove all restrictions on consequential recombination, cognitive inference or misuse.

DICP remains relevant.

Therefore:

**Public Source != Universal Consequential Use Authority**

A public-release transition should not be interpreted as consent to every future inference.

## 20. PLE as a safer alternative

Before terminating protection to enable a function, ask whether the function can be satisfied through PLE:

`Query -> Protected Context -> Minimum Result`

rather than:

`Protected Dataset -> Broad Disclosure`

This creates a powerful minimisation rule:

> **If A Legitimate Function Can Be Satisfied Without Declassification, Declassification Requires Independent Justification.**

This does not prohibit release where release itself is the legitimate objective.

## 21. MNC application

MNC asks for the least capability sufficient for the legitimate function.

For information transitions:

`Purpose -> Information Function -> Required Disclosure Capability -> Minimum Sufficient Output -> Review -> Expiry`

Therefore:

> **Minimum Necessary Information Capability Applies To Protection-State Transition Authority Itself.**

An actor authorised to approve T1 bounded projections need not receive authority to approve T4 public releases.

## 22. ESCP/ASCP challenge

Before consequential protection termination ask:

> What materially relevant protected boundary, authority source, affected participant, auxiliary dataset, re-identification route, future use, third-party interest or prohibition would have to be missing for this transition to be illegitimate or over-scoped?

This challenges both:
- information-space completeness;
- authority-space completeness.

## 23. Transfer tests

### Health aggregate publication

Health proposes publication of disease statistics.

Technical evaluator verifies aggregation and re-identification risk.

Health/research authority supplies legitimate purpose.

Participant-specific consent may not be necessary where the legitimate civil framework permits sufficiently anonymous statistics, but participant privacy remains a protected boundary that the transformation must actually satisfy.

Publication authority remains separate from technical validation.

PASS.

### Research dataset

Research wants to release a de-identified dataset.

The researchers who benefit from publication should not be the sole high-consequence certifier where re-identification risk is material.

Independent validation and appropriate authority composition may be required.

PASS.

### Historical archive

Historical holds participant records whose ordinary operational access has expired.

Historical may retain them under historical stewardship.

That does not authorise public release.

A later public-release transition needs its own authority and protection analysis.

PASS.

### AI-generated participant profile

An AI produces a participant risk profile from public data.

The AI/operator cannot declare the profile unrestricted merely because its inputs were public.

DICP and derived-information protections may apply.

PASS.

### Operational capacity signal

Medical -> occupational fitness -> aggregate staffing capacity.

By the staffing-capacity stage, participant identity and medical semantics may legitimately have terminated.

Routine pre-authorised transformation can suffice if the architecture reliably prevents reconstruction.

PASS.

## 24. Failure modes

- self-declassification;
- verifier sovereignty;
- technical-authority collapse;
- consent absolutism;
- institutional-ownership absolutism;
- stale anonymisation;
- retroactive illegitimacy collapse;
- rollback fiction;
- source-destruction bundling;
- public-source laundering;
- declassification convenience;
- authority-band inflation.

## 25. Candidate invariants

PSTAR-01 — Ability To Assess Protection State != Authority To Change Protection State.  
PSTAR-02 — Protection-State Evidence != Protection-State Authority.  
PSTAR-03 — Protection Transition Authority Is Contextual, Not Universal.  
PSTAR-04 — Protection-State Verifier != Protection-State Authority Source.  
PSTAR-05 — Pre-Authorised Transformation != Unauthorised Automation.  
PSTAR-06 — Beneficiary Of Reduced Protection != Sufficient Sole Certifier By Default.  
PSTAR-07 — Participant Consent != Universal Declassification Authority.  
PSTAR-08 — Anonymisation Expertise != Disclosure Authority.  
PSTAR-09 — Disclosure Authority != Proof Of Anonymisation.  
PSTAR-10 — Disputed != Invalid.  
PSTAR-11 — Disputed != Safe To Ignore.  
PSTAR-12 — Current Protection Failure != Automatic Historical Wrongdoing.  
PSTAR-13 — Historical Legitimacy != Current Continuation Authority.  
PSTAR-14 — Irreversibility Raises Pre-Transition Completeness And Authority Burden.  
PSTAR-15 — Right To Contest != Automatic Right To Control Every Outcome.  
PSTAR-16 — Protection-State Rollback != Restoration Unless Prior Exposure State Is Actually Re-established.  
PSTAR-17 — Authority To Anonymise != Authority To Destroy Source.  
PSTAR-18 — Authority To Retain Source != Authority To Re-Link Anonymised Output.  
PSTAR-19 — Public Source != Universal Consequential Use Authority.  
PSTAR-20 — If A Legitimate Function Can Be Satisfied Without Declassification, Declassification Requires Independent Justification.  
PSTAR-21 — Minimum Necessary Information Capability Applies To Protection-State Transition Authority Itself.

## 26. Architectural classification

This is **not** a new universal authority engine.

It is an interface architecture applying existing:
- MKA;
- MNC;
- CIBB;
- ESCP/ASCP;
- PLE;
- BTA;
- KCS/STRA

to protection-state transitions.

It should therefore remain cross-domain architecture rather than being extracted as a competing portable authority module.

## 27. Central rule

> **No Actor Gains Authority To Reduce An Information Object's Protection Merely Because It Possesses, Transforms, Understands Or Benefits From That Information.**

A legitimate protection-state transition requires the appropriate contextual authority for the actual change, supported by proportionate evidence that the claimed new information state is real.
