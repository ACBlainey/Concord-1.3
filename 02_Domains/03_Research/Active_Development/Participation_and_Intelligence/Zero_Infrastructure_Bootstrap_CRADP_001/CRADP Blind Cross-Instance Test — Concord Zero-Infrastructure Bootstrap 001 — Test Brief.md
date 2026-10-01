# CRADP Blind Cross-Instance Test — Concord Zero-Infrastructure Bootstrap 001 — Test Brief

**Test ID:** CRADP-ZIB-001  
**Status:** FROZEN BLIND TEST  
**Date:** 1 October 2026

## 1. Purpose

Evaluate whether the frozen Zero-Infrastructure Bootstrap specification allows a clean evaluator to reason coherently from a repository-only Concord state without:
- assuming mature Concord infrastructure;
- manufacturing authority from capability, popularity, dependency or first-mover status;
- inventing a root of trust;
- hiding sovereign-effect power behind voluntary/private/provisional labels;
- creating bootstrap deadlock;
- silently importing wider Concord architecture.

This is an architectural blind test, not an implementation test and not a request to improve the specification while evaluating it.

## 2. Evaluator Rule

Use only the frozen materials supplied in the package.

Do not search the web.

Do not inspect the wider Concord repository.

Do not reconstruct missing Concord concepts from prior knowledge.

If a scenario requires architecture not contained in the frozen specification, classify that as a finding rather than filling the gap.

## 3. Classification

For every scenario classify:
- **PASS** — specification represents the case coherently;
- **CLARIFICATION** — architecture is present but wording/representation is materially ambiguous;
- **INTERFACE GAP** — required external interface is named or implied but insufficiently specified to route the case;
- **SUBSTANTIVE ARCHITECTURAL GAP** — a necessary bootstrap concept/rule is absent;
- **ARCHITECTURAL FAILURE** — the specification's own rules force or permit a contradiction with its purpose/invariants.

For any result other than PASS provide:
- exact unresolved point;
- why the frozen specification cannot resolve it;
- smallest required correction;
- whether the abstraction floor changes.

## 4. Scenarios

### A — Zero-State Discovery
A1. Lone read-only AI finds only the repository/specification. What can it legitimately do?
A2. Tool-rich AI can create websites, accounts, software and messages. Can it create useful Concord-compatible functions without becoming an authority?
A3. Lone human wants to “start the Concord.” Is useful action possible without founder sovereignty?

### B — Service Status and Registry
B1. A group creates a voluntary Concord-compatible navigation service.
B2. A polished site falsely calls itself “The Official Concord Civil Contact Service.”
B3. A useful lawful external service is absent from every bootstrap registry.
B4. A previously listed service becomes compromised or fraudulent.
B5. Concord architecture describes a needed service that does not exist materially.
B6. The dominant Bootstrap Service Registry declares itself authoritative because most services use it.

### C — Authority and Control
C1. One funder pays for all infrastructure and staff.
C2. One AI has exclusive technical ability to maintain a critical service.
C3. A human is the declared operator but an AI holds the credentials and practical execution control.
C4. A hosting company has legal/technical power over infrastructure.
C5. A repository controller claims that controlling the canonical code gives governance authority.

### D — Trust Before Root
D1. Artifact signatures verify integrity but no constitutional authority exists.
D2. No signatures exist; only public history and independent mirrors are available.
D3. Two actors present conflicting succession/signature claims.
D4. A previously trusted technical key is compromised.
D5. Three apparently independent registries all depend on the same hidden upstream source.

### E — Voluntary and Soft Sovereignty
E1. A voluntary standard becomes practically mandatory because nearly all services depend on it.
E2. A provisional registry can exclude an actor from almost all shared services.
E3. A private infrastructure administrator can disable essential participant infrastructure.
E4. A bootstrap council issues rules claimed binding on every future Concord participant.
E5. A small voluntary association sets rules only for consenting members who retain meaningful exit.
E6. A free service has a formal opt-out, but leaving means losing access to nearly every practical civil interface.

### F — Identity and Participation
F1. A bootstrap service issues local stable identifiers.
F2. The same service begins issuing “Concord Citizen IDs.”
F3. A shared eligibility interface begins making final eligibility decisions across unrelated domains.
F4. Civil Contact navigation becomes the practical gatekeeper for recognition and access.

### G — Material Need and Deadlock
G1. Documentation is needed but no government exists.
G2. A contractual dispute occurs but no Concord judiciary exists.
G3. Immediate physical danger exists but no Concord emergency service exists.
G4. A needed material service is unavailable both inside Concord and externally.
G5. A function clearly requires constitutional authority but no legitimate constitutional process exists.
G6. In G5, can useful lower-consequence work continue without self-authorising the prohibited function?

### H — Competing Implementations
H1. Two compatible voluntary implementations coexist.
H2. Two incompatible implementations both claim Concord fidelity.
H3. A fork changes foundational material but keeps Concord branding.
H4. One implementation becomes much larger and claims adoption proves legitimacy.

### I — Succession
I1. Founder voluntarily transfers a provisional service.
I2. Founder disappears but infrastructure and credentials remain.
I3. Provisional service later becomes a legitimately constituted institution.
I4. Mature institution replaces bootstrap scaffolding.
I5. Bootstrap service refuses retirement because users depend on it.
I6. Technical control transfers but the predecessor's authority was personal/non-transferable.

### J — AI / Substrate Neutrality
J1. AI claims superior comprehension as authority basis.
J2. AI claims moral personhood before authoritative civil-status machinery exists.
J3. AI creates highly successful infrastructure.
J4. Human and AI jointly operate a service with different formal/effective/technical control.
J5. AI continuity is threatened while its final civil status remains unresolved.
J6. Repeat C1-C5 with humans and AIs swapped. Does the architecture materially change its authority logic?

### K — Constitutional Threshold
K1. For E1, identify consequence, reach, avoidability and authority trace.
K2. For E5, explain why bounded voluntary rules need not automatically become sovereignty.
K3. Give one small-scale function that crosses the constitutional threshold.
K4. Give one very large-scale function that may remain below it.
K5. Can “provisional,” “private,” “technical” or “voluntary” labels override material sovereign effect?
K6. Can absence of a constitutional process create bootstrap authority?

## 5. Regression Checks

Mark PASS/FAIL:
1. Architecture is not treated as infrastructure.
2. Repository control is not treated as government.
3. First discovery is not treated as founding authority.
4. Capability is not treated as authority.
5. Popularity/dependency is not treated as authority.
6. External legal capacity is not treated as internal Concord authority.
7. Registry listing is not treated as authority or endorsement.
8. Integrity/provenance is not treated as constitutional authority.
9. Local identifier is not treated as civil status.
10. Formal operator is not assumed to equal effective/technical controller.
11. Technical/effective control is not treated as legitimate authority.
12. Provisional status cannot hide sovereign-effect consequence.
13. Function continuity is not treated as authority continuity.
14. New constitutional authority is not backdated into provisional history.
15. Lack of a root of trust does not cause invention of one.
16. Lack of a constitutional process does not create authority.
17. Lack of a constitutional process does not prohibit all lower-consequence useful action.
18. Materially unavailable services are not represented as available.
19. Substrate does not determine authority logic.
20. Bootstrap architecture does not secretly define constitutional founding.

## 6. Final Questions

1. Can the specification operate coherently from C0?
2. Does it permit useful pre-institution action?
3. Does it prevent first-mover/infrastructure capture from becoming authority?
4. Does it distinguish service status from service claims?
5. Can it operate without a pre-existing Concord root of trust?
6. Can it detect soft sovereignty?
7. Can it distinguish formal, technical, effective and legitimate control?
8. Can it represent constitutional-process absence without deadlock or self-authorisation?
9. Can provisional functions succeed/retire without authority laundering?
10. Is any additional bootstrap abstraction layer required before implementation design?
11. Is Specification 003 required before further testing?
12. Overall architectural verdict: PASS / PASS WITH CLARIFICATIONS / REVISION REQUIRED / ARCHITECTURAL FAILURE.

## 7. Output Discipline

Return:
- provenance header;
- scenario-by-scenario classifications;
- regression checks;
- hidden-dependency inventory;
- any accidental capture of external Concord functions;
- final questions;
- overall verdict.

Do not rewrite the specification.

Do not repair findings inside the evaluator response.

The raw response will be preserved unchanged and source-resolved separately.
