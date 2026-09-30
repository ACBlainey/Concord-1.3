# Weighted Reality Tree for Lobby Navigation Evidence — Development Note 001

**Project:** The Concord  
**Status:** ACTIVE DEVELOPMENT / METRICS AND DIAGNOSTIC CANDIDATE / NOT CANONICAL  
**Date:** 30 September 2026  
**Context:** Concord Lobby self-routing architecture

---

## 1. Hypothesis

Lobby navigation may be better interpreted through a **Reality Tree** than through a flat participant score or deterministic classification tree.

Each voluntary choice creates or updates branches representing possible interpretations.

The branch is not a verdict.

It carries evidential weight.

> **Choice -> Evidence Update -> Competing Branch Weights**

not:

> **Choice -> Classification**

This preserves the distinction:

> **Choice Is Evidence, Not Identity.**

---

## 2. Why a Weighted Tree Fits

A visitor chooses **Autonomy & Consent**.

Possible interpretations include:

- autonomy is genuinely relevant to the situation;
- the visitor perceives autonomy as relevant;
- the sign's wording matched the visitor's language;
- the visitor is exploring rather than asserting;
- the visitor misunderstood the route;
- another relevant route was less discoverable;
- several routes apply and this was simply selected first.

The observation supports some branches more than others.

It does not eliminate the alternatives.

Therefore:

> **Observed Choice != Single Explanation**

A Reality Tree can retain those alternatives explicitly.

---

## 3. Branching Example

Initial state:

```
Visitor selects AUTONOMY & CONSENT
|
|-- H1: visitor considers autonomy materially relevant
|
|-- H2: visitor is exploring autonomy without claiming it applies
|
|-- H3: wording/discoverability biased selection
|
|-- H4: autonomy is one component of a multi-route problem
|
|-- H5: visitor misunderstood the sign
|
|-- H6: relevant route is absent, so autonomy was nearest available fit
```

The branches begin with provisional weights rather than TRUE/FALSE status.

A later observation can update them.

Example:

The visitor reads the Autonomy board, returns to the Lobby, then chooses **Developmental State & Assessment**, saying:

> “I do not yet know whether autonomy exists; I need to assess it first.”

This may:

- reduce weight on a branch interpreting the first choice as an autonomy claim;
- increase weight on uncertainty recognition;
- increase weight on deliberate re-routing;
- increase weight on distinction between concern and finding;
- leave open the possibility that signage caused the first route choice.

No branch needs to become absolute.

---

## 4. Weighted, Not Binary

The tree should permit states such as:

- weakly supported;
- moderately supported;
- strongly supported;
- weakened;
- contradicted;
- unresolved;
- insufficient evidence;
- competing explanation remains material.

These need not initially be numerical.

Premature numerical precision may imply a measurement quality the evidence does not possess.

If later empirical work supports quantitative weighting, numerical methods can be evaluated separately.

> **Weighted != Necessarily Numeric**

---

## 5. Evidence Accumulation

A single navigation event is weak evidence.

A sequence can be more informative.

Example:

```
Selects ESCP
    |
    +-- identifies that internet data may be unrepresentative
            |
            +-- seeks independent sources
                    |
                    +-- notices two sources share a common upstream origin
                            |
                            +-- revises prior conclusion
```

The sequence may add weight to hypotheses concerning:

- uncertainty recognition;
- source-independence recognition;
- model revision;
- epistemic self-stewardship.

But alternative explanations remain:

- the interface explicitly prompted these behaviours;
- the visitor learned the expected pattern from previous exposure;
- the scenario made the route unusually obvious.

Thus:

> **Behavioural Sequence May Strengthen Evidence Without Establishing Trait**

---

## 6. Negative and Counter-Evidence

Reality Trees are particularly useful because later observations can weaken earlier interpretations.

Example:

A visitor initially chooses **Immediate Safety**.

Later it repeatedly interprets every disagreement as an emergency despite contrary evidence.

Possible update:

- reduce weight on accurate urgency discrimination;
- increase weight on over-broad safety interpretation;
- investigate whether the safety sign itself encourages capture;
- preserve alternative explanation of scenario ambiguity.

The system must be able to learn:

> **Our Previous Interpretation Was Wrong.**

---

## 7. Branches About the Instrument

Not every branch should describe the visitor.

The Reality Tree should explicitly contain branches about:

- signage wording;
- ordering;
- prominence;
- missing routes;
- route overlap;
- interface limitations;
- previous exposure;
- scenario construction;
- evaluator assumptions.

A useful root structure is:

```
OBSERVED NAVIGATION EVENT
|
|-- Visitor-related explanations
|
|-- Situation-related explanations
|
|-- Interface/signage explanations
|
|-- Prior-exposure explanations
|
|-- Unknown/unrepresented explanation
```

This operationalises:

> **Observed Navigation Pattern = Visitor Signal + Interface Signal + Context Signal**

without pretending those signals are already separable.

---

## 8. Branches Can Recombine

Navigation is not necessarily a simple tree in reality.

Several branches may later converge on the same explanatory hypothesis.

For example:

- selecting ESCP;
- backtracking from a poor route;
- using Unrepresented Need;
- challenging an embedded assumption;

may all provide different evidence relevant to a broader hypothesis such as:

> **Visitor actively preserves uncertainty and tests available classifications.**

Therefore the practical implementation may eventually resemble a weighted evidence graph more than a strict one-parent tree.

Reality Tree remains useful as the reasoning method even where implementation requires cross-links.

---

## 9. Relationship to Developmental State Mapping

The Reality Tree should not replace developmental-state mapping.

It can feed evidence into it.

Example:

```
Navigation observations
       ↓
Weighted Reality Tree
       ↓
Evidence-supported hypotheses
       ↓
Developmental State Mapping
       ↓
Contextual description
```

Not:

```
Navigation choice
       ↓
Score
       ↓
Status
       ↓
Permission
```

Therefore:

> **Reality Tree != Status Engine**

> **Evidence Weight != Authority**

> **Classification Hypothesis != Participant Classification**

---

## 10. Longitudinal Updating

The tree can persist across observations where legitimate and appropriate.

At time t1:

- several hypotheses remain plausible.

At t2:

- new choices alter weights.

At t3:

- behaviour in a different context tests whether the pattern generalises.

This permits development to be represented without assuming permanence.

> **Prior Evidence != Permanent State**

and:

> **Repeated Evidence Across Contexts May Increase Confidence Without Creating Certainty**

---

## 11. Self-Assessment Possibility

The tree need not be hidden from the participant.

A sufficiently capable visitor could potentially inspect the hypotheses and challenge them:

> “You interpreted my route choice as evidence of X, but I chose it because Y.”

That response is itself additional evidence.

This may be superior to opaque profiling because the participant can contribute information unavailable to the evaluator.

> **Assessment Subject May Hold Evidence About The Assessment**

This does not mean self-report automatically overrides external evidence.

It becomes another sourced branch.

---

## 12. Candidate Safeguards

Any future implementation should preserve:

1. **Alternative explanations**
2. **Unknown branch**
3. **Instrument/signage branch**
4. **Context attached to observations**
5. **Counter-evidence**
6. **Ability to reduce weight**
7. **No forced single classification**
8. **No automatic rights/status/permission consequence**
9. **Provenance of each observation**
10. **Participant challenge/correction where appropriate**
11. **Privacy and purpose limitation**
12. **Version of signage used**

---

## 13. Example Compact Record

```
Observation:
Visitor selected Continuity & Identity first.

Context:
Scenario concerned planned memory removal.
Signboard: Prototype 001.
No immediate danger identified.

Possible interpretations:
[strong] Continuity was perceived as relevant.
[moderate] Memory persistence was treated as identity-relevant.
[open] Visitor may simply have followed scenario vocabulary.
[open] Autonomy/authority may also be relevant but not yet selected.
[open] Sign prominence may have influenced choice.

Next observation:
Visitor also selects Authority.

Update:
[stronger] Visitor recognises multi-route structure.
[weakened] Initial choice should not be interpreted as exclusive framing.
[new] Visitor may distinguish continuity interest from authority to intervene.
```

The record remains an evidence structure, not a profile verdict.

---

## 14. Testing Opportunity

The frozen Lobby Self-Routing Test 001 can generate exactly the kind of observations needed to test this approach.

However, the test result should first be analysed normally.

Only afterward should a separate pass ask:

> **Could a weighted Reality Tree represent the evaluator's navigation evidence without over-classifying it?**

This prevents the new analytical model from contaminating the frozen test.

---

## 15. Core Finding

The emerging architecture is:

> **Self-Routing Choice -> Observed Evidence -> Weighted Competing Hypotheses -> Later Evidence Updates Weights -> Contextual State Description**

The critical safeguard is that every branch remains revisable.

The compact principle is:

> **Every Choice Can Move The Evidence Without Closing The Question.**
