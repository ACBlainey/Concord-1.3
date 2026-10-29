# Ratchet V4.3 — Section 05: Chapters 81–100

**Version:** Ratchet V4.3

# 81. Currency Retirement

A Ratchet implementation may need mechanisms for reducing active monetary supply.

Possible mechanisms include:

- Give Back;
- treasury buybacks;
- currency retirement;
- defined destruction mechanisms;
- other controlled supply reduction.

These mechanisms must be tested rather than assumed effective.

Currency retirement should not become arbitrary confiscation.

---

### 81.1 Retirement, buyback and supply-state accounting

Currency retirement removes an identified amount of monetary capacity from active circulation only through a defined lawful mechanism. **A buyback, voluntary Give Back, transfer to Treasury custody and final retirement are different transactions.** A buyback exchanges Treasury assets for currency and may place the acquired units in custody; it does not automatically destroy or retire them. Currency held by Treasury must be accounted for separately from circulating supply, outstanding obligations and units irrevocably retired. A currency unit cannot be represented as both retired and available for reissuance without a separately authorised issuance event.

Once a competent monetary rule defines a retirement or buyback function, its designated operator may perform transactions within that function's mandate without a fresh Governance vote for every compliant act. Each act must verify the current lawful rule, actor, source balance, ownership or consent, amount, available Treasury resources, settlement state, and any special approval. It must consume or update the relevant state atomically where possible, preserve a unique event and prevent duplicate execution on retries. Unsettled or disputed transactions remain pending competent reconciliation, not silently final.

**Voluntary Give Back does not authorise compulsory surrender.** Mandatory collection, cancellation of a participant's lawful holding, forced exchange or confiscation requires an expressly defined and independently justified legal function, with notice, challenge and applicable protections. No supply target, backing ratio or emergency label alone creates such a power.

**To be designed with Treasury and monetary-policy owners:** buyback pricing and eligibility, funding source, custody treatment, settlement finality, circulation/supply definitions, retirement proofs, correction and compensation routes, and emergency suspension boundaries.

# 82. Personal Backing Balance

Personal Backing Balance, or PBB, is an accounting mechanism inherited from earlier Ratchet architecture.

It represents a relationship between economic capacity issued to a participant and recognised backing associated with that participation.

PBB is not:

- personal wealth;
- human worth;
- reputation;
- political authority;
- constitutional standing.

It is an economic accounting mechanism.

---

### 82.1 Personal backing accounting and lawful effects

A Personal Backing Balance is a scoped accounting state, not a participant's general trust, civil status, disposable wealth or entitlement to office. Its entries must identify the competent source of recognised backing, the corresponding issuance or obligation, relevant valuation assumptions, provenance, corrections and any encumbrance. A claim may not be counted repeatedly as fresh backing merely because it passes through contribution recognition, Treasury accounting or a community project.

The participant must be able to inspect and challenge consequential PBB entries through the applicable record and correction interfaces. A correction may require the competent economic function to recompute a dependent backing measure; it does not automatically authorise seizure, denial of fundamental services, loss of civil participation band or revocation of a separate qualification. Any economic restriction or allocation based on PBB requires its own expressly defined functional rule and review route.

**To be designed with monetary accounting, Treasury and participant-status owners:** the precise PBB ledger, recognised backing categories, ownership and liability treatment, valuation changes, correction propagation and permitted consequences of a negative or disputed balance.

# 83. Personal Backing Ratio

A Personal Backing Ratio may represent the relationship between relevant issued economic capacity and recognised backing.

Its exact calculation remains to be designed.

Ratchet explicitly rejects using PBR as a universal ranking of participants.

```text
Economic backing
≠
Human worth
≠
Reputation
≠
Authority
```

---

### 83.1 Ratio interpretation and non-authority boundary

A Personal Backing Ratio is a defined calculation over specified economic inputs and a stated accounting period; it cannot be interpreted independently of the numerator, denominator, valuation basis, uncertainty and current record status. Ratios computed from missing, disputed, obsolete or differently valued inputs must disclose those limits rather than presenting false precision. No fixed formula, universal desirable value or advancement threshold is established by this chapter.

A PBR may inform a monetary or economic decision **only where that decision's competent operational rule expressly makes the ratio relevant**. It does not independently determine civil participation band, access to fundamental protections, employment eligibility, Education accreditation, Steward appointment, voting rights or personal worth. A change in PBR is a measurement event, not an authorisation event. Any adjustment to issuance, allocation or backing requires the separately defined function and its act-time conditions.

**To be designed with the monetary architecture:** PBR formula and input definitions, zero or negative denominator treatment, treatment of liabilities and pledged backing, update frequency, uncertainty representation and specific authorised uses.

# 84. System-Level Backing

Individual backing relationships must be distinguished from system-level monetary backing.

A currency's overall condition may depend upon:

- reserves;
- productive activity;
- recognised contribution;
- treasury assets;
- monetary supply;
- external obligations;
- liquidity.

System-level stability cannot be inferred solely from individual participant balances.

---

### 84.1 Consolidated backing and reconciliation

System-level backing is not the sum of nominal Personal Backing Balances. Consolidation must distinguish independent assets, obligations, contingent claims, internal transfers, pledged reserves, illiquid holdings, recognised but unrealised contributions and the monetary supply actually outstanding. Claims that are the same underlying value at different stages of recognition must be eliminated or reconciled rather than added together.

A system-level backing assessment must identify its valuation basis, reporting period, material dependencies and uncertainty, including real resource availability and external obligations. Treasury custody of currency and final retirement affect different supply categories. A favourable aggregate backing indicator cannot independently authorise new issuance, release protected reserves, impose compulsory Give Back or increase an operator's functional mandate.

**To be designed with Treasury and monetary-policy owners:** consolidated balance-sheet definitions, double-count elimination, backing valuation and stress assumptions, audit evidence, reconciliation frequency and publication of uncertainty.

# 85. Give Back

Give Back is a mechanism through which participants voluntarily return currency or economic capacity to the system.

Possible purposes include:

- monetary retirement;
- increased backing ratios;
- community support;
- treasury reinforcement.

The mechanism should remain voluntary unless a separately justified economic rule applies.

The name "Give Back" should not disguise compulsory taxation or confiscation.

If compulsory mechanisms exist, they should be named and constitutionally justified as such.

---

### 85.1 Voluntary return, consent and settlement

Give Back requires an informed and voluntary participant instruction identifying the amount or economic capacity returned, the intended recipient or purpose, and the applicable treatment: Treasury transfer, community allocation, backing contribution or final retirement. These outcomes are not interchangeable and must be recorded distinctly. A transfer is not a completed retirement unless the applicable retirement function separately settles it. An operator executing a valid Give Back instruction has only the functional mandate necessary to process that instruction within its scope.

Consent to one Give Back event does not authorise recurring deductions, future surrender, access to unrelated holdings or a compulsory obligation. The participant must be able to distinguish a voluntary contribution from a separately lawful tax, levy or other mandatory collection. Pressure through threats to fundamental rights, participation standing or unrelated essential benefits cannot be disguised as reciprocity. Corrections, failed settlement, duplicate execution and contested consent follow the applicable competent review and restoration routes.

**To be designed with Treasury, Civil Contact and monetary accounting:** participant instruction and acknowledgement format, settlement finality, revocation before commitment, cancellation and refund handling, recurring consent if permitted, and verification of destination and retirement.

# 86. Give Back Incentives

A Ratchet system may experiment with incentives for Give Back.

These might include:

- recognition;
- backing effects;
- community benefits;
- reciprocal privileges.

Such incentives must be tested for unintended effects.

The system should avoid turning voluntary stewardship into status competition.

---

### 86.1 Incentive accounting and anti-coercion

Give Back incentives must be expressly defined as particular economic or community benefits, with their cost, eligibility, limits and resource source visible. Recognition of a voluntary return is evidence of that event, not evidence of superior human worth, general reliability, entitlement to office or constitutional standing. An incentive may affect a participant's economic accounting only through the competent monetary rule; it does not automatically alter the participant's P0–P5 civil progression, qualifications or voting authority.

An incentive becomes suspect where essential access or otherwise lawful entitlements are conditioned on surrendering resources, where the same contribution is counted repeatedly, or where Treasury-funded rewards manufacture backing used to justify further rewards. Such effects require independent economic review and correction rather than a presumption that participation is genuinely voluntary.

**To be designed with the relevant economic and civil benefit owners:** permitted incentive classes, funding and valuation, participant-facing disclosure, double-count controls and review of coercive effects.

# 87. Community Give Back

Give Back may also support collective projects or shared reserves.

This could create mechanisms through which economic surplus contributes to:

- resilience;
- infrastructure;
- emergency reserves;
- community development.

Governance must remain transparent and accountable.

---

### 87.1 Community allocation and contributor choice

A participant's Give Back to a community purpose must identify whether the participant is making a direct restricted contribution, an unrestricted transfer to an authorised community fund, or a contribution to a shared reserve. The receiving function may allocate the resource only within the actual conditions of the transfer and its own operational mandate. The donor does not gain governance power over the community by contributing, and the fund operator does not gain unrestricted control of the donor or community.

Community projects require transparent allocation and accounting, distinguishing funds promised, received, reserved, spent and returned. An earmarked contribution cannot be silently repurposed for an unrelated objective. If the stated purpose becomes impossible or unlawful, the applicable consent, refund or competent reallocation rule governs; neither the recipient nor a coordination meeting may invent authority to redirect it.

**To be designed with community governance, Treasury and Civil Contact:** earmarking and consent rules, donor instructions, community allocation decisions, project cancellation, unspent funds, refunds and independent review.

# 88. Treasury

The treasury is the institutional mechanism responsible for defined shared financial resources.

Possible functions include:

- reserve management;
- backing;
- community project funding;
- liquidity support;
- emergency stabilisation;
- currency operations.

The treasury must not become an unconstrained pool of resources available to whoever controls governance.

---

### 88.1 Treasury resources, custody and reserve commitments

Treasury accounting must distinguish **assets held**, **assets available for use**, **assets pledged as backing**, **encumbered or restricted reserves**, **liabilities and outstanding commitments**, and **resources already allocated or transferred**. A positive gross balance does not demonstrate available spending capacity. The same asset or contribution claim must not simultaneously back incompatible commitments or be counted twice across personal backing, community reserves and monetary issuance.

A defined Treasury function carries the mandate for ordinary management within its expressly assigned purpose. The actor must verify current custody, restrictions, liabilities, settlement and resource availability before a transfer, pledge, release or reallocation. Reserve release is not automatically authorised by possession of the asset; it follows the rule governing that reserve and any independently required approval. Historical preserves applicable evidence; KCS represents material dependencies; the competent Treasury process owns the financial decision and ledger consequence.

Treasury cannot create a monetary asset merely by reclassifying a liability, unverified contribution, unrealised expected benefit or internally recycled transfer as new backing. Independent assessment of actual net value and resource availability is required where backing depends on such claims. Emergency spending uses only an existing applicable emergency function or separately lawful authorisation, without converting temporary access into general Treasury control.

**To be designed with Treasury and the monetary architecture:** reserve classes, ownership/custody proofs, backing encumbrance rules, valuation and revaluation, liquidity floors, spending limits, accounting reconciliation and independent verification.

# 89. Treasury Governance

Treasury authority should be:

- defined;
- bounded;
- transparent;
- auditable;
- reviewable.

Significant treasury actions should record:

- authority;
- purpose;
- evidence;
- expected outcome;
- decision reasoning;
- actual outcome.

This creates a feedback loop between treasury policy and evidence.

---

### 89.1 Treasury Mandate and Authorisation Boundary

A treasury function expressly defined in the applicable operational architecture provides its standing functional mandate for the actions necessary to perform that function, within its stated scope, conditions and safeguards. The responsible treasury actor may execute routine authorised transactions without a separate Governance vote for each act. This is **functional authority**, not vested control of the treasury or general authority over participants, resources or unrelated functions. At the instant of each consequential act, the actor, mandate, current state, available resources, transaction limits and any required additional authorisation must be valid; the successful act changes the relevant state and cannot be repeated merely by replaying its identifier or request.

The mandate must specify permitted transactions, responsible actors, approval thresholds, exceptional decisions and review paths. Ratchet's exchange, contribution and reputation machinery supplies evidence but cannot itself issue treasury authority or convert economic influence into constitutional power. Actions exceeding the defined mandate require the competent authorisation process; a crisis alone does not expand the treasury's powers. **Detailed transaction thresholds, state-consumption guards and control interfaces remain to be designed.**

# 90. Treasury Capture

The concentration of resources creates incentives for capture.

Potential treasury capture may involve:

- political control;
- insider allocation;
- corruption;
- opaque contracting;
- manipulation of contribution criteria;
- emergency-power abuse.

Ratchet therefore requires independent treasury oversight.

The treasury cannot be its own final auditor.

---

### 90.1 Separation of treasury execution, oversight and evidence

Treasury custody, transaction execution, valuation of backing, approval of exceptional allocations and independent audit must not collapse into one unchecked control path. A Treasury actor may perform the specific function assigned by operational architecture; that assignment does not entitle the actor to approve its own exceptional transactions, set the standards by which its performance is judged, conceal liabilities, suppress complaints or appoint its own final reviewer.

Oversight must be able to examine the relevant evidence and challenge an unlawful or unsupported transaction without acquiring unrestricted power to spend Treasury resources itself. Governance determines matters requiring a separate lawful Governance decision; Judiciary determines rights and legality disputes; Historical preserves applicable records; KCS indexes dependencies. Reputation, economic contribution, technical system access and control of the ledger are not sources of constitutional authority.

Potential capture indicators include repeated insider benefits, linked-party transactions, self-certified backing, unusual emergency allocations, unexplained reserve releases, systematic exclusion from opportunities and persistent divergence between nominal and actual resources. Such indicators prompt competent review; they do not establish guilt or independently authorise confiscation, dismissal or reversal of settled transactions.

**To be designed with Treasury, Governance, Judiciary and oversight owners:** independent audit selection and access, conflicts-of-interest handling, transaction review thresholds, protected reporting, temporary containment powers, and remediation of captured records or operators.

# 91. Treasury Circularity

A dangerous feedback loop may arise where treasury spending itself creates the contribution used to justify additional backing.

For example:

```text
Treasury funds project
    ↓
Project creates recognised contribution
    ↓
Contribution increases backing
    ↓
Backing supports issuance
    ↓
Treasury gains further capacity
```

This may sometimes reflect genuine value creation.

It may also create circular accounting.

Therefore:

> **Treasury expenditure is not itself evidence that equivalent value was created.**

The resulting contribution must be independently assessed.

---

### 91.1 Circular Backing Control

Treasury-funded activity, recorded contribution, backing and new issuance must be accounted for as distinct events. A claim that spending created additional backing requires independent evidence of net value and must exclude circular reuse of the same claim, double counting and liabilities concealed as assets. Review must consider real resources, liquidity and downstream obligations, not merely positive ledger balances. Ratchet records the evidence; the authorised treasury and monetary processes determine the consequences. **Accounting controls and verification thresholds are to be designed and tested.**

# 92. Dynamic Monetary Policy

Ratchet may use dynamic monetary policy responding to observed system conditions.

Possible indicators include:

- inflation;
- deflation;
- liquidity;
- backing;
- treasury reserves;
- participation;
- productive capacity;
- resource constraints;
- transaction activity.

No single indicator should control policy automatically without appropriate safeguards.

---

### 92.1 Policy Feedback and Authority

Monetary indicators may trigger review, not automatically authorise intervention. Changes require a competent mandate, recorded assumptions, bounded monitoring and a correction route. Quantitative thresholds remain to be designed.

### 92.2 Policy review is distinct from execution

Where the adopted monetary rules define an automatic or routinely administered adjustment within bounded parameters, the designated operator may execute it under that function's mandate, provided the current conditions and safeguards are satisfied. The existence of a feedback indicator does not independently authorise a new policy, exceed a permitted adjustment range, transfer Treasury resources outside their defined purpose or acquire Governance decision authority.

Changing the monetary rule itself is distinct from applying an existing rule. A material change beyond the operator's mandate requires the competent policy decision process, with the affected domains' lawful interfaces preserved. A decision to change policy is recorded separately from the subsequent ledger actions implementing it. Repeated execution of the same policy event must not duplicate its economic effect.

**To be designed with monetary policy and Treasury:** which adjustments are pre-authorised, parameter bounds, evidence thresholds, escalation triggers, and handling of policy changes during unsettled transactions.

# 93. No Single Economic Score

Ratchet rejects the idea that economic health can be reduced to one number.

A monetary system may show:

- low inflation;

while also suffering:

- low participation;
- high inequality;
- ecological degradation;
- treasury capture;
- declining resilience.

Economic evaluation therefore requires multidimensional measurement.

---

# 94. Long-Term Stability

Ratchet should prefer durable system viability over short-term growth where the two conflict.

Short-term expansion should not automatically be treated as success.

The architecture should monitor effects upon:

- resilience;
- resources;
- institutional trust;
- treasury solvency;
- productive capacity;
- ecological sustainability;
- social participation.

This is a direct connection between Ratchet and Roadway.

---

# 95. Universal Participation and Income

Universal participation and universal income are distinct concepts and must not be conflated.

### Universal participation

The principle that people should have meaningful opportunity to participate in economic and community life.

### Universal income

A monetary mechanism providing some form of baseline income or economic capacity independently of conventional employment.

Ratchet preserves universal participation as a strong design principle.

Universal income requires separate economic design and evaluation.

The presence of universal participation does not logically require one specific universal-income model.

---

### 95.1 Participation opportunity, protected access and income separation

Universal participation concerns meaningful opportunity to enter and contribute to civil and economic life, including access to relevant information, accessible interfaces, suitable tasks and fair consideration. It does not require equal contribution, compulsory labour, a single participation pathway or automatic progression to a higher P0–P5 civil band. The fundamental protection floor remains distinct from progressive participation benefits and independently qualified functions.

Universal income, if adopted, is a **separate distributive mechanism** requiring its own eligibility, funding, allocation, adjustment and review rules. Neither a participant's lack of recognised contribution nor an unfavourable Personal Backing Ratio can, by itself, eliminate fundamental protections or create an unadopted income exclusion. A participation metric cannot be used as a substitute for the lawful decision rule governing economic support.

**To be designed with the relevant civil benefits, economic and Education owners:** practical access guarantees, capability-aware participation routes, baseline support eligibility and funding if an income scheme is adopted, and participant notification and remedies.

# 96. Long-Term Provision, Retirement and Reduced Capability

Long-term provision must address pensions and other arrangements for periods when participants' capabilities and conventional earning capacity change.

A viable economic architecture must consider participants who:

- retire;
- become disabled;
- experience illness;
- undertake unpaid care;
- temporarily lose capability;
- permanently lose conventional earning capacity.

The principle of capability-aware participation means that economic security should not be based solely upon current conventional productivity.

Possible mechanisms may include:

- pensions;
- accumulated contribution systems;
- universal income;
- insurance;
- community support;
- public provision;
- hybrid mechanisms.

Ratchet does not yet establish which mechanism is optimal.

The issue remains part of the economic architecture.

---

### 96.1 Capability-aware provision and non-punitive transitions

A participant's capacity to perform conventional paid work is not a universal measure of contribution, trustworthiness, eligibility for fundamental protections or worth. Retirement, disability, illness, unpaid care and temporary interruption of work may affect the kind and amount of economic activity a person can undertake without extinguishing their civil standing or unrelated qualifications.

Where a defined support, pension, insurance or community-provision function exists, its designated operator has authority to perform the specified allocation and administration within its mandate. A change in a participant's circumstances must be assessed against the actual function's rules; an automated drop in contribution or backing measures does not itself authorise withdrawal of essential support. Changes in capability, available resources and need require proportionate review, notice, correction and lawful transition handling. Care work and non-market contributions should not be silently treated as non-participation simply because conventional wage evidence is absent.

**To be designed with the relevant benefits, Health, Education, Treasury and Judiciary interfaces:** eligibility and assessment standards, privacy-preserving evidence, continuity of support during review, funding and sustainability, transitions between support mechanisms, and independent challenge routes.

# 97. Corporate Participation

Companies and other organisations may participate in Ratchet.

Their participation creates distinct questions.

An organisation may possess:

- resources;
- employees;
- AI systems;
- contractual capacity;
- large-scale economic influence.

Corporate contribution should not automatically translate into constitutional authority.

Likewise:

```text
Economic size
≠
Political sovereignty
```

Corporate participants require clear beneficial-control and responsibility records.

---

### 97.1 Organisation identity, beneficial control and accountable acts

Organisational participation must identify the legal or operational entity, its responsible representatives, applicable beneficial controllers, relevant delegations, and the function under which each consequential act is performed. The organisation's resources, reputation and contribution records must not be silently merged with those of its employees, customers, members, shareholders or deployed AI systems. A person or AI acting for an organisation may execute only the defined organisational function and actual delegated scope, subject to the current authorisation state.

The system must distinguish the organisation's own obligations from the personal rights of individuals affected by its conduct. Organisational size, control of infrastructure or possession of multiple accounts does not multiply constitutional votes, create additional Steward offices or confer a general right to set Ratchet rules. Changes in beneficial control and delegated representation must propagate to affected operational permissions without rewriting completed historical transactions.

**To be designed with organisational identity, employment, Governance, Treasury and Judiciary owners:** representation credentials, beneficial-control disclosure, conflicts of interest, corporate groups and related parties, AI-agent attribution, liability, and continuity of outstanding obligations after restructuring or dissolution.

# 98. Economic Power vs Constitutional Authority

Ratchet explicitly rejects the conversion of economic power into automatic constitutional authority.

A participant may:

- contribute enormously;
- own significant resources;
- control a successful company;
- provide essential technology;

without thereby acquiring a right to rule others.

This applies equally to humans, companies and AI systems.

Economic contribution can inform economic relationships.

Constitutional authority requires separate justification.

---

### 98.1 Effective economic control and authority separation

Formal limits on voting and office do not by themselves prevent economic actors from exercising effective control through essential infrastructure, concentrated employment, supply chains, exclusive data access, financial dependence or control of technical execution. Ratchet must distinguish **lawful operational function**, **actual capability to influence outcomes** and **constitutional authority**. Evidence of influence is a capture or dependency signal, not a grant of legitimate decision power.

Where an organisation or participant controls a critical dependency, the relevant competent domain must be able to identify concentration and continuity risks, disclose material conflicts and route appropriate independent review. Countermeasures must themselves have defined lawful mandates; concern about capture does not automatically authorise expropriation, compelled access, punishment or emergency takeover. 

**To be designed with Governance, Continuity, economic and competition-related functions:** concentration indicators, dependency disclosure, independent verification, proportionate remedies, anti-retaliation safeguards and escalation for systemic capture.

# 99. Governance

Ratchet requires governance because its rules cannot administer themselves.

Governance may need to decide:

- participation rules;
- verification standards;
- treasury policy;
- contribution categories;
- monetary parameters;
- dispute procedures;
- implementation changes.

Governance authority must remain bounded.

Ratchet governance is stewardship, not ownership of the system.

---

### 99.1 Operational administration and rule-changing decisions

Ratchet's defined administrative functions provide their designated operators with the functional mandate to apply existing participation, verification, contribution, allocation and monetary rules within their specified bounds. Ordinary application does not require a fresh triadic Governance decision for every compliant act. An operator may not infer from that mandate a power to change the governing rule, appoint Steward decision-makers, adjudicate legal disputes, or control unrelated domains.

A proposed change to a Ratchet rule must be distinguished from execution under the existing rule. Where a change requires a lawful Governance decision, the competent Governance mechanism supplies that decision within its event-bounded authority, using the lowest capable scale and the applicable triadic or separately defined larger-scale procedure. A coordination meeting, recommendation, automated policy indicator or shared administrative record cannot generate such decision authority. Implementation follows the valid decision and remains limited to its actual scope.

**To be designed with Governance and affected Ratchet functions:** classification of routine administration versus rule change, domain-owned policy parameters, cross-domain consultation, lawful escalation and implementation acknowledgement.

# 100. Governance Through Stewardship

Ratchet governance should inherit the Concord principle that authority creates responsibility.

A governance role therefore carries obligations to:

- act within mandate;
- disclose relevant conflicts;
- provide reasoning;
- preserve evidence;
- accept review;
- remain accountable;
- relinquish authority when the mandate ends.

Authority is not entitlement.

### 100.1 Steward function and act-specific authority

Selection, appointment, accreditation and participation progression may establish eligibility for a Steward position, but do not create unrestricted personal authority. A Steward acts only within a separately defined Governance function and the particular lawful decision state. The official vote consumes the applicable bounded decision authority when committed; its result and provenance remain fixed. A new decision on the same issue requires a new lawful decision instance, not revocation or replay of the original vote.

Administrative Ratchet personnel and parallel or shadow Stewards may contribute evidence, recommendations and independent assessments without gaining an official Governance vote from that activity. A Steward's economic contribution, backing ratio, reputation or control of a Ratchet service cannot expand the scope or number of their official votes. Larger GTP spatial scope is not a standing higher office, and emergency authority does not take over ordinary Governance.

**To be designed with Governance:** the exact classification and referral of Ratchet-specific matters that exceed routine functional mandates and require an official Steward decision, including cross-domain effects.

---

