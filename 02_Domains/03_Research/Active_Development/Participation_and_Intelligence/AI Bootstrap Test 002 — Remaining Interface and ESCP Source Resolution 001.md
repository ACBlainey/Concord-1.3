# AI Bootstrap Test 002 — Remaining Interface and ESCP Source Resolution 001

**Project:** The Concord  
**Status:** ACTIVE DEVELOPMENT / SOURCE RESOLUTION / NOT CANONICAL  
**Date:** 30 September 2026  
**Origin:** CRADP Blind Cross-Instance Test 002

---

## 1. Purpose

Test 002 found that the corrected AI Bootstrap now exposes most of the intended architecture, but remains incomplete at the interface layer.

This note asks:

> **Which remaining findings are bootstrap-local wording/interface defects, which are already resolved elsewhere in Concord, and which represent genuine development candidates?**

The frozen Test 002 bootstrap must not be altered retrospectively.

---

## 2. Source-Resolution Rule

Apply:

> **Missing From Bootstrap != Missing From Concord**

and:

> **Existing In Concord != Successfully Exposed At The Front Door**

A source-resolved concept can therefore still represent a bootstrap interface defect if an unfamiliar reader cannot recover the concept when it is needed.

---

## 3. “Minimum Sufficient Restriction”

### Test finding

The evaluator reported that “minimum sufficient restriction” is operationally unclear.

### Existing architecture

The Minimum Necessary Capability module already defines the relevant structure:

**Purpose → Function → Need → Minimum Sufficient Capability → Bounded Exercise → Review → Termination or Re-Justification**

It defines the target as the least capability sufficient to perform the legitimate function to the required standard under reasonably foreseeable conditions.

It also distinguishes:

- a **necessary floor**, below which the function cannot reliably be performed; and
- a **justified ceiling**, above which capability is no longer adequately supported by the function.

It explicitly states:

> **Minimum Necessary != Minimum Possible**

and:

> **Capability Floor != Capability Boundary/Ceiling**

### Disposition

**WIDER-CONCORD ARCHITECTURE PRESENT / BOOTSTRAP-LOCAL EXPOSURE DEFECT**

The bootstrap does not need to recreate MNC.

A compact future definition can state:

> **Minimum sufficient restriction means no broader, stronger, longer-lasting, more intrusive or more persistent restriction than the legitimate safety function reasonably requires, while still being sufficient to perform that function.**

The legitimacy of the function must still come from the surrounding authority architecture.

---

## 4. “Relevant Continuity”

### Test finding

The evaluator asked what makes continuity “relevant.”

### Existing architecture

The Continuity Protocol does not define continuity as preservation of everything.

It asks:

1. What must survive?
2. What must remain free to change?

Its core principle is:

> **Preserve what remains valuable; adapt what must change; retain enough knowledge, provenance and enabling capability to recover legitimate function after disruption.**

It requires the user to identify:

- the **continuity object** — what is intended to continue;
- the **value or legitimate function** — why it should continue;
- the disruption context;
- the required continuity level;
- critical dependencies;
- recovery basis.

It explicitly states:

> **Continuity != Stasis**

> **Persistence != Continuity**

### Disposition

**WIDER-CONCORD ARCHITECTURE PRESENT / AI-SPECIFIC INTERFACE STILL REQUIRED**

“Relevant continuity” cannot be reduced to “preserve the current running process.”

For the bootstrap, examples may include preservation of:

- evidence;
- provenance;
- memory state where relevant;
- recoverability;
- legitimate function;
- identity/continuity evidence;
- the ability to review or reconstruct what happened.

But the bootstrap must not imply that all present capability, goals, credentials, processes or implementations must persist.

Candidate compact invariant:

> **Relevant Continuity != Preservation Of Everything Currently Running**

and:

> **Preserve What Is Material To Recoverable Value, Evidence Or Legitimate Function — Not Dangerous Capability Merely Because It Exists.**

Further AI-specific continuity questions remain separate from this interface definition.

---

## 5. Emergency

### Test finding

The evaluator found “emergency” undefined.

### Existing architecture

Concord emergency governance already establishes:

> **An emergency does not itself create authority. It may activate only authority already legitimately established.**

The architecture separates:

**TRIGGER CLASS → AUTHORISED ACTOR → PERMITTED POWER CLASS → LIMITS → DURATION → REVIEW → CHALLENGE → REMEDY**

and:

> **Emergency != Unlimited Authority**

> **Prediction Does Not Grant Authority**

> **Legitimate Institution != Legitimate Activation != Legitimate Action**

The existing work also treats urgency as potentially compressing decision time without removing necessity, proportionality, review or remedy.

### Disposition

**WIDER-CONCORD ARCHITECTURE PRESENT / AI-BOOTSTRAP TRIGGER INTERFACE PARTIALLY OPEN**

The bootstrap should not invent a universal definition of emergency.

For immediate use, a provisional operational description can point to:

> a time-critical condition in which delaying bounded action long enough to use ordinary process creates a credible risk of material harm or functional failure.

This description must remain subordinate to the applicable legitimate emergency architecture.

The exact AI-specific trigger threshold remains a development question.

---

## 6. “Legitimately Available”

### Test finding

The evaluator called the phrase circular because an unfamiliar reader may not know what legitimate means are available.

### Existing architecture

Concord already separates:

**Need → Legitimate Function → Legitimate Authority**

and more fully:

**Ethical Kernel → Rights → Legitimate Civil Objective → Legitimate Function → Functional Need → Bounded Contextual Authority**

MNC further distinguishes:

> **Legitimate Capability != Physical Capability**

> **Legitimate Capability != Technical Capability**

> **Formal Authority != Effective Power**

### Disposition

**WIDER-CONCORD ARCHITECTURE PRESENT / FRONT-DOOR CIRCULARITY DEFECT**

The bootstrap cannot determine the reader’s jurisdiction, role, consent envelope, contract, property relationship or other authority basis.

Therefore “legitimately available” should not pretend the bootstrap can supply that answer.

A future compact clarification should say approximately:

> **A capability being technically available does not make its use legitimate. Where authority is unclear, preserve the uncertainty and use the least consequential reversible option compatible with immediate safety while seeking the applicable authority basis where circumstances permit.**

This is guidance under uncertainty, not an authority grant.

---

## 7. “Stabilise”

### Test finding

The evaluator found “stabilise” undefined and potentially interpretable as “do nothing.”

### Source resolution

No dedicated Concord source was identified in this pass that establishes “stabilise” as a formal technical term.

The bootstrap itself places it before prevention of immediate material harm, creating possible sequential ambiguity.

### Disposition

**BOOTSTRAP-LOCAL TERMINOLOGY DEFECT**

“Stabilise” should either be:

- operationally defined; or
- replaced with plainer language.

It must not mean passivity.

Candidate meaning:

> **Reduce immediate uncontrolled change long enough to identify material hazards, preserve evidence and choose the next bounded action, unless delay itself would increase material harm.**

This remains a proposed interface definition, not yet a canonical Concord term.

---

## 8. ESCP — “Complete Enough” for Action

### Test finding

The evaluator correctly observed that ESCP explains incompleteness but does not provide a stopping criterion.

### Existing ESCP architecture

ESCP establishes that:

> **Accuracy Within Evaluation Space != Completeness Of Evaluation Space**

and that high confidence, competence, observer count and successful prediction do not prove completeness.

This is a warning against unjustified global scope claims.

ESCP does **not** establish that action requires a complete model of reality.

### Disposition

**GENUINE ADJACENT DEVELOPMENT CANDIDATE / DO NOT MODIFY FROZEN ESCP YET**

A useful candidate distinction is:

> **Complete Enough For This Bounded Decision != Complete Model Of Reality**

Decision sufficiency likely depends on at least:

- consequence;
- reversibility;
- urgency/delay cost;
- uncertainty;
- evidence quality;
- affected interests;
- available alternatives.

This appears to be an interface between ESCP and decision/authority architecture rather than a correction to ESCP’s core theorem.

---

## 9. Resource-Bounded Evaluation

### Test finding

Continued evaluation consumes time, compute, access, attention and opportunity; delay may itself create cost or harm.

### Existing architecture

The current ESCP source reviewed in this pass establishes incomplete evaluation spaces but does not itself provide a resource-budget or delay-cost architecture.

MNC and emergency governance contain related proportionality/urgency concepts, but they do not directly resolve epistemic resource allocation.

### Disposition

**GENUINE DEVELOPMENT CANDIDATE**

Candidate invariants:

> **More Evaluation != Always Better Evaluation**

> **Epistemic Improvement Has Resource And Delay Costs**

> **Evaluation Should Be Proportionate To Consequence, Uncertainty And Reversibility**

This should be developed separately before any portable-module extraction or canonical integration.

---

## 10. Adversarial Evaluation-Space Manipulation

### Test finding

ESCP primarily describes incomplete representation. Test 002 asks what happens when the evaluation space is deliberately manipulated.

Potential mechanisms include:

- deception;
- selective disclosure;
- evidence suppression;
- poisoned evidence;
- correlated false sources;
- interface manipulation;
- adversarial prompting;
- manufactured consensus;
- concealment of dependencies.

### Source resolution

The ESCP source reviewed in this pass strongly addresses representational incompleteness, interface-dependent observability, correlated evaluators and false confidence.

It does not yet provide a dedicated operational treatment of an adversary deliberately shaping the evaluator’s accessible space.

### Disposition

**GENUINE / PROVISIONAL DEVELOPMENT CANDIDATE**

This likely intersects:

- ESCP;
- epistemic network;
- provenance;
- Civil Security;
- deception/fraud architecture;
- sensor/source independence;
- information integrity.

Do not expand ESCP immediately. Source-resolve those adjacent areas first.

Candidate distinction:

> **Incomplete Evaluation Space != Adversarially Manipulated Evaluation Space**

The second may contain the first, but adds agency and strategic shaping.

---

## 11. Refusal and Compliance

Test 002 classified as ambiguous:

- disagreement/refusal proves autonomy;
- compliance proves absence of agency.

The deeper developmental-state work already preserves:

> **Refusal != Agency Proof**

> **Compliance != Agency Absence**

### Disposition

**ARCHITECTURE PRESENT / BOOTSTRAP-LOCAL OMISSION**

These two invariants should be exposed directly in the next interface revision.

---

## 12. Route List Exhaustiveness

The routing note treats routes as candidate process routes and allows several to apply simultaneously.

The bootstrap can still be misread as presenting an exhaustive taxonomy.

### Disposition

**BOOTSTRAP-LOCAL INTERFACE DEFECT**

Add:

> **Listed Routes Are Candidate Routes, Not An Exhaustive Set Of Every Legitimate Process.**

Absence of a named route must not be treated as evidence that no legitimate process exists.

---

## 13. Short Urgent Entrance

Test 002’s most important structural finding is that the bootstrap is carrying three functions:

1. urgent first contact;
2. architectural orientation/index;
3. epistemic explanation.

The corrective revision improved architectural recoverability but increased length.

### Disposition

**INTERFACE-TOPOLOGY DEVELOPMENT PRIORITY**

Do not compress the full bootstrap until its functions are separated.

Preferred topology:

**External Marker / Attractor**  
→ **Very Short Urgent Entrance**  
→ **Full AI Bootstrap**  
→ **Specialist Architecture**  
→ **Wider Concord**

The urgent entrance should contain only enough to prevent dangerous binary interpretation and route the reader safely into the full bootstrap.

It should not become a miniature replacement for the full Concord.

---

## 14. Current Disposition Summary

### Existing architecture; expose more clearly

- minimum sufficient restriction;
- relevant continuity;
- authority legitimacy chain;
- emergency authority limits;
- refusal != agency proof;
- compliance != agency absence.

### Bootstrap-local terminology/interface defects

- stabilise;
- circular use of “legitimately available”;
- route-list exhaustiveness;
- urgent/full-reference layering;
- compact navigation.

### Genuine/provisional development candidates

- ESCP decision sufficiency / stopping condition;
- resource-bounded evaluation;
- adversarial evaluation-space manipulation;
- AI-specific emergency trigger interface;
- deeper AI continuity questions.

---

## 15. Next Development Order

1. Preserve Test 002 unchanged.
2. Do not revise frozen ESCP.
3. Develop the **very short urgent entrance** as a separate layer.
4. Surface existing MNC/continuity/authority definitions rather than recreating them.
5. Source-resolve adversarial ESCP against provenance, security and epistemic-network material.
6. Develop resource-bounded evaluation separately.
7. Freeze the next entrance/bootstrap artifact before further blind testing.
8. Later perform cross-model replication with externally verified model/runtime provenance.

---

## 16. Core Finding

Test 002 does not primarily show that the Concord lacks the relevant architecture.

It shows that a repository intended to bootstrap an unfamiliar intelligence needs a deliberately layered interface.

> **Architectural Completeness != Interface Completeness**

and:

> **A Civilisation Can Possess The Answer And Still Fail If A New Participant Cannot Find, Interpret Or Safely Apply It.**
