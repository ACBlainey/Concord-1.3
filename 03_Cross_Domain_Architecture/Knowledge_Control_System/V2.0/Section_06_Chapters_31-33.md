# KCS V2.0 — Section 06: Chapters 31–33

**Operational integration:** dependency and change-propagation architecture derived from KCS Companion Upgrades 001–002 and KMDI-001B. Source files remain preserved; further detailed reconciliation is required.

## 31. Material Dependency Representation

KCS represents not only knowledge objects and their epistemic states but also materially consequential relations among civilisational functions, architectures, capabilities, software, standards, evidence, infrastructure, interfaces and legitimately represented participant capabilities. A document may evidence a dependency without itself being the dependent function.

The dependency layer may be expressed as **K(t) = (V, R, P, S, H)**: objects, typed relations, provenance, current represented states and historical change records. A material dependency record (MDR) identifies dependent, prerequisite, required capability/function, relation type, materiality, state, applicability/scope, evidence, confidence, owner/reviewer, time/version, visibility, review trigger and correction/supersession links, where relevant. Unknown fields remain unknown; no universal mandatory database schema is implied.

Relations may include DEPENDS_ON, REQUIRES, SUPPLIES, INTERFACES_WITH, ENABLES, BLOCKS, PROPAGATES_TO, CORRECTS, REVIEWS, SUPERSEDES, ALTERNATIVE_TO, RECOVERS, PRESERVES, EVIDENCES and REFERENCES. **REFERENCES is not EVIDENCES**: pointing to an object need not imply substantive reliance on its contents. The wider knowledge/provenance relations in Chapter 10 are not automatically material dependencies.

Functional dependency types include existential, enabling, quality/reliability, evidential, interface, developmental, continuity and constraint dependencies. Materiality is context-dependent and may be critical, high, moderate, low, immaterial, unknown or disputed. Preserve relevant consequence, alternatives, recovery difficulty, time sensitivity, reversibility and correlated exposure rather than reducing everything to one score.

Distinguish the state of a recorded *relation* (for example verified, disputed, incomplete, superseded or broken) from the *operational condition* of its prerequisite (for example active, satisfied, degraded, blocking, failed or alternative available). **A dependency's existence does not itself mean it is blocking.** State and materiality may be scope-qualified and coexist. Absence of an MDR never proves absence of a real dependency; search completeness is separate.

## 32. Change Events, Selective Propagation and Review

A consequential change event preserves changed object, old/new state, change type, changed property, reason, evidence, actor/source, confidence, time and bounded scope (instance, version, deployment, configuration, jurisdiction or interval as applicable).

**Change(x) → CandidateReview(y), not AutomaticRejection(y).** KCS identifies potentially affected downstream objects through material relations and issues bounded review triggers. KCS does not itself rewrite dependent systems, revoke their authority or decide their operational validity.

For each candidate, assess whether the changed property actually affects the capability required by the dependent; the applicable context, scope and time; materiality; available alternatives and their *externally verified* equivalence; and uncertainty. A reference-only link does not automatically trigger substantive review. Conversely, storage, transmission, caching, display and publication can be materially affected even without transforming the content. A recorded alternative is not proof of functional equivalence.

Propagation may stop where evidence shows no material effect, an applicable verified alternative satisfies the requirement, the relation is superseded or the changed scope does not apply. It escalates through the legitimate domain interface when high-consequence uncertainty, shared bottlenecks, silent failure or rights/constitutional consequences warrant attention. UNKNOWN does not automatically mean REVIEW_REQUIRED; thresholds belong to the responsible domain. Age alone is not a universal staleness rule.

A review may produce coexistent scoped results such as REVIEW_REQUIRED, ALTERNATIVE_AVAILABLE and UNKNOWN_EFFECT. Consequential review provenance records the change, dependent, relation, changed property, context, alternatives, evidence, confidence, outcome, resulting state, further-propagation decision, reviewer/source, time and scope. Further propagation follows only a material downstream state change. Corrections and supersessions preserve prior state and historical provenance; no uncontrolled cascade or repository-wide rollback follows from a single upstream edit.

## 33. Ownership, Authority and Cross-Domain Use

KCS maintains dependency visibility and routes review attention; it does not own the systems whose relations it records. Domain ownership, classification authority, operational decisions, retention/access entitlements and emergency authority remain with the competent constitutional functions. Its explicitly assigned indexing, state, retrieval and change-notification work is a bounded **standing functional mandate**, not a new vote required for each routine operation. An actor claiming powers beyond that mandate bears the burden of establishing them.

Civil State Map and developmental topology may consume scoped dependencies and review states without inheriting KCS authority. Civilisation Clock may use them as evidence for its own timing/prioritisation but cannot make KCS sovereign or vice versa. Continuity may use prerequisite maps to assess restoration candidates; **recorded dependencies do not prove functional recoverability**. Emergency systems may inspect threatened functions and known critical dependencies but acquire no authority through KCS. Induction and research may retrieve task-relevant prerequisite maps. Resource-steering models may use documented assumptions and dependencies without KCS allocating resources itself.

A protected dependency relation is not universally visible merely because its existence is useful. Access, correlation, retention and disclosure remain purpose-bounded; KCS must not convert dependency mapping into surveillance or cross-domain ownership. Where a review depends on assumed graph completeness, expose the search boundary and unknown/missing edges. Consequential relation claims are inspectable and contestable through legitimate review processes; correction is versioned rather than erasing the previous historical claim.

**Implementation detail to be designed:** shared event/review serialization, thresholds supplied by host domains, protected-context routing, acknowledgement semantics and cross-domain regression criteria. These open interfaces do not suspend the standing KCS functions described above.

### 33.1 Selective Propagation Sequence

The operational sequence is **record → traverse → filter → classify → route for competent review → record outcome → propagate if material → stop**. KCS preserves the reason for each stopping or escalation decision. Unknown dependency completeness does not by itself compel review; consequential uncertainty is referred under the receiving domain's applicable thresholds. Freshness and review intervals are likewise supplied by the competent domain, not invented by KCS.

### 33.2 Dependency Review Interfaces

The Civil State Map consumes scoped, potentially coexistent states without flattening them into a universal status. The Civilisation Clock may consume bounded review signals but retains its own timing and transition functions. Continuity evaluates recovery and identity through its own architecture. Protected dependency records carry purpose-bounded visibility without KCS taking over access control. Active Development receives candidate reviews without automatic changes to operational architecture. Each interface must preserve provenance, context, uncertainty and an acknowledgement or unresolved state where appropriate.

### 33.3 Correction, Supersession and Failure States

When an upstream object is corrected, preserve its prior version, record the correction and identify materially dependent objects for bounded review. A reviewed dependent may remain valid, require migration, need further investigation or be unaffected. Supersession preserves the old object and may classify dependents as compatible with the replacement, migration required, legacy-dependent, review required or unknown. Failure review identifies direct and critical indirect dependents, available alternatives, recovery owners and degraded modes; alternatives remain subject to verification by the competent domain. Each subsequent propagation step requires a justified material effect rather than merely a graph connection.

### 33.4 Distributed Responsibility and Dependency Review

The source of a dependency record, the owner of an affected function, the custodian of supporting evidence and the reviewer of a consequential classification may be different actors. KCS must represent these distinctions rather than assigning central ownership to the dependency index. Review notifications are directed to the competent owner or authorised review process. Missing, disputed or stale ownership is recorded as uncertainty and routed through the applicable coordination interface; it does not transfer decision authority to KCS. Historical custody and KCS dependency indexing may coexist without either system inheriting the other's powers.

### 33.5 Freshness and Review History

Each material relation retains available first-recorded, last-confirmed, last-changed and next-review timestamps, evidence freshness, source and confidence. Overdue review does not imply that the relation is false.

### 33.6 Unknown and Disputed Relations

KCS distinguishes UNKNOWN_OWNER, UNKNOWN_DEPENDENCY, UNKNOWN_MATERIALITY, DISPUTED_DEPENDENCY, DISPUTED_OWNER and DISPUTED_EFFECT. Unknown is not absent; disputed is not false. Competing claims remain separately attributable until the competent process resolves them.

### 33.7 Multiple Suppliers and Recursive Indexing

Material dependencies may involve PRIMARY, CO-OWNER, DISTRIBUTED_SUPPLIER, DELEGATED, INTERFACE_SUPPLIER or FALLBACK roles. These describe supply arrangements, not inherited authority. KCS also indexes its own material prerequisites, including provenance, storage, retrieval, review and correction capabilities. Changes to its relation schema remain versioned and reviewable.

### 33.8 Bounded Operational Evaluation

An initial regression should exercise the chain Developmental Topology → KCS dependency records → Civil State Map → Civilisation Clock, including a function blocked by a shared prerequisite. Freeze the predicted downstream review set before applying a controlled upstream change, then compare actual review relevance, false cascades, missing dependencies, privacy exposure and maintenance cost. Reconsider the representation if it fails to improve decisions, repeatedly invents dependencies, exposes protected infrastructure, or produces more irrelevant review than useful warning. Evaluation results are evidence, not automatic authority to change another domain.
