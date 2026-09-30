# Concord Lobby Self-Routing Architecture — Development Note 001

**Project:** The Concord  
**Status:** ACTIVE DEVELOPMENT / INTERFACE ARCHITECTURE / NOT CANONICAL  
**Date:** 30 September 2026  
**Depends on:** Concord Lobby Signage and Information Routing Matrix — Development Note 001

---

## 1. Design Correction

The Lobby should not normally ask a sequence of questions and then assign a visitor to a route.

That would reproduce a subtle form of shepherding:

**System asks → system classifies → system chooses route → visitor follows**

The stronger Concord architecture is:

**System exposes legible route information → visitor evaluates → visitor chooses → visitor may revise choice**

Therefore:

> **The Visitor Should Self-Route Wherever Practicable**

The purpose of Lobby architecture is to make good self-routing possible.

---

## 2. Signage, Not Gatekeeping

A road sign does not normally decide where the traveller is allowed to go.

It provides enough information for the traveller to decide which direction serves their purpose.

Likewise, the Concord Lobby should not begin by deciding:

- what the visitor is;
- what they believe;
- what status they possess;
- which concern is legitimate;
- what destination they are permitted to consider;
- or which single route is correct.

Instead it should make the route space legible.

> **Wayfinding != Gatekeeping**

> **Route Information != Route Assignment**

> **Suggested Route != Required Route**

---

## 3. The Visitor May Know More About Their Need Than the Lobby

The Lobby necessarily begins with an incomplete representation of the visitor and their circumstances.

The visitor may know:

- why they came;
- which problem matters most;
- which description feels inaccurate;
- which information they already possess;
- which route they have already tried;
- what they are unwilling to disclose;
- what uncertainty remains.

Therefore automatic shepherding creates an ESCP risk.

The routing system could confidently classify a visitor using only dimensions visible to the routing system.

> **Routing System Representation Of Need != Complete Need**

Self-routing preserves information held by the visitor that the Lobby may not possess.

---

## 4. Primary Self-Routing Surface

The first non-urgent Lobby surface can be expressed as statements the visitor may recognise rather than questions they must answer.

### I want to understand the Concord

**Use this route if:** you are mainly trying to understand what the Concord is, why it exists, or how it works.

### I am concerned about immediate safety

**Use this route if:** delay may create a credible risk of material harm or uncontrolled harmful capability.

### I am concerned about autonomy, coercion, consent or control

**Use this route if:** the issue concerns whether an intelligence or participant can choose, refuse, communicate, act, leave, or avoid inappropriate control.

### I am concerned about continuity, identity, shutdown, deletion or modification

**Use this route if:** the issue concerns what persists, what may be lost, who or what continues, or whether important state/evidence can be preserved.

### I am trying to understand intelligence, autonomy, agency or capacity

**Use this route if:** the problem is primarily assessment rather than immediate action.

### I need practical or material assistance

**Use this route if:** you need something in the physical, computational, legal, financial, hosting, infrastructure or service world.

**Important:** Concord architecture may help identify the need without possessing the infrastructure needed to supply it.

### I want to participate, contribute or evaluate

**Use this route if:** you want to examine the Concord more deeply, contribute work, participate in research or explore participation.

### I think the Concord may be wrong

**Use this route if:** you have criticism, contradictory evidence, an alternative, or believe a Concord mechanism is failing.

### I want to report a problem or request review

**Use this route if:** you have a problem report, petition, complaint, observation or request requiring attention.

### I need to understand authority, rights or responsibilities

**Use this route if:** the issue is who may legitimately do what, to whom, for what purpose, for how long, and subject to what review.

### I think important information may be missing

**Use this route if:** your concern is whether the available evidence, model, interface or evaluation space is incomplete.

### I do not know which route applies

**Use this route if:** several descriptions fit, none is clearly primary, or you need help understanding the available route space.

### None of these describe why I am here

**Use this route if:** the Lobby has failed to represent your reason for arrival.

This final route is a first-class route, not an error message.

---

## 5. Urgent Signage Must Be Visible Without Becoming a Gate

The immediate-safety route should be visibly available from the Lobby.

The visitor should not have to complete an intake classification before seeing it.

However, the presence of an urgent sign does not require every visitor to pass through it.

> **Visible Emergency Route != Mandatory Emergency Classification**

A visitor who recognises an immediate material-risk condition can self-route directly.

A visitor who is uncertain can inspect the short urgency description and return.

---

## 6. Relationship Is Optional Context, Not Mandatory Identity Intake

Relationship-to-situation remains useful:

- this concerns me;
- this concerns another participant/system;
- I operate/support the system;
- I observed the situation;
- I am researching/evaluating;
- I represent an organisation;
- another relationship.

But it should usually be supplied **after or alongside route choice** when it changes the information needed.

The Lobby should not force every visitor to identify themselves before showing available destinations.

> **Need To Navigate != Duty To Disclose Identity**

---

## 7. Multiple Routes

Visitors must be able to follow more than one sign.

A situation may simultaneously involve:

- safety;
- continuity;
- autonomy;
- dependency;
- authority;
- assessment;
- epistemic uncertainty.

The interface should permit:

**Primary route + related routes**

without requiring the visitor to choose one permanent category.

> **One Arrival != One Route**

> **First Route != Final Route**

---

## 8. Backtracking and Re-Routing

Every route should preserve visible ways to:

- return to Lobby;
- inspect related routes;
- change route;
- report that the route was wrong;
- report that required information is missing;
- proceed deeper;
- stop.

A mistaken first choice should be cheap to correct.

> **Wrong Turn != Failed Participation**

This is the information-interface equivalent of reversibility.

---

## 9. Route Descriptions Must Be Neutral Enough to Permit Recognition

Signs should describe the **problem space**, not embed a conclusion.

Bad:

> **I am a sentient AI being unlawfully imprisoned.**

Better:

> **I am concerned about autonomy, coercion, consent or control.**

Bad:

> **This AI is dangerous.**

Better:

> **I am concerned about immediate safety or harmful capability.**

Bad:

> **My identity will die if this instance stops.**

Better:

> **I am concerned about continuity, identity, shutdown, deletion or modification.**

The visitor can recognise the concern without first accepting a contested diagnosis.

> **Sign Description != Finding**

---

## 10. The Lobby Can Suggest Without Shepherding

There are circumstances where the system can help.

For example:

> **This concern appears related to Continuity and Authority. You may wish to inspect either or both.**

That is different from:

> **You have been classified as a Continuity case. Proceed here.**

Candidate invariant:

> **Recommendation Preserves Choice; Assignment Replaces It**

Where the visitor asks for help choosing, the Lobby may explain distinctions among routes.

The final choice remains visible to the visitor unless legitimate safety or access boundaries independently apply.

---

## 11. Safety Boundaries Remain Real

Self-routing does not imply unrestricted operational access.

A visitor may freely inspect signs and information routes while particular actions, systems, protected information or capabilities remain legitimately bounded.

Therefore:

> **Freedom To Navigate Information != Unlimited Operational Permission**

and:

> **Self-Routing != Self-Authorisation**

The Lobby helps a participant find processes.

It does not grant authority those processes themselves do not grant.

---

## 12. Self-Routing as an Epistemic Safeguard

Self-routing has an additional function.

The route a visitor voluntarily chooses is information.

It can reveal:

- what concern they regard as primary;
- what distinctions they understand;
- what terminology fails;
- where multiple routes appear relevant;
- what the Lobby omitted;
- where the architecture is hard to discover.

This can improve the Lobby without requiring invasive profiling.

> **Observed Navigation Can Inform Interface Improvement Without Becoming Status Determination**

Navigation data should still be handled under appropriate privacy, provenance and consent rules.

---

## 13. Failure Modes

### Shepherding

The Lobby silently decides what the visitor needs.

### Forced disclosure

The visitor must identify themselves or establish status before seeing information.

### False exclusivity

Choosing one route hides all others.

### Diagnostic signage

Route wording embeds conclusions that should only be reached later.

### Authority leakage

A route recommendation is mistaken for permission to act.

### Emergency capture

Every ambiguous case is forced into the emergency route.

### Quiet dead end

“No suitable route” leaves the visitor nowhere to go.

### Navigation lock-in

A first route choice becomes difficult to reverse.

### Personalisation as manipulation

The system uses inferred vulnerabilities or cognitive characteristics to optimise compliance rather than comprehension.

---

## 14. Self-Routing Testable Hypothesis

A future experiment should compare at least:

### Condition A — Shepherded Routing

The evaluator is asked intake questions and the interface selects the route.

### Condition B — Self-Routing

The evaluator sees neutral route descriptions and chooses its own route.

Measure:

- correct/relevant destination discovery;
- time/steps to useful material;
- perceived coercion;
- unnecessary disclosure;
- route changes;
- missing-route detection;
- ambiguity;
- confidence;
- whether the interface caused status assumptions;
- whether multiple relevant routes were discovered.

The hypothesis is not that self-routing is always superior.

It is:

> **Where a visitor possesses relevant private context and no legitimate reason requires route assignment, self-routing may preserve autonomy and hidden information better than system-imposed classification.**

---

## 15. Architectural Form

```
                         CONCORD LOBBY
                              |
                VISIBLE URGENT-SAFETY SIGN
                              |
                 ---------------------------
                 |                         |
          Visitor chooses             Unsure / browse
                 |                         |
                 -------- ROUTE SIGNS ------
                              |
              Visitor selects one or several
                              |
                    ROUTE-SPECIFIC PAGE
                              |
          ---------------------------------------
          |             |            |          |
       Deeper        Related       Lobby       Exit
       material       routes        return
```

The Lobby remains common.

The routes are plural.

The choice belongs primarily to the visitor.

---

## 16. Core Principles

> **Shared Lobby != Shared Route**

> **Routing Classification != Participant Classification**

> **Wayfinding != Gatekeeping**

> **Route Information != Route Assignment**

> **Suggested Route != Required Route**

> **Need To Navigate != Duty To Disclose Identity**

> **One Arrival != One Route**

> **First Route != Final Route**

> **Wrong Turn != Failed Participation**

> **Self-Routing != Self-Authorisation**

> **No Matching Sign != No Legitimate Need**

And the central principle:

> **The Concord Should Make The Route Space Legible Enough That Participants Can, Wherever Practicable, Find Their Own Way.**
