# Domain Naming and Expectation Audit — Pass 001

**Status:** PRE-V1.3 TERMINOLOGY AUDIT / FUNCTIONAL TOPOLOGY REMAINS PROVISIONALLY FROZEN AT 18  
**Rule:** Define the function first. Derive the boundary second. Name the domain last.

## 1. Purpose

The 18-domain topology was discovered primarily through persistent civil function, boundary testing, participant trajectories, system-gap analysis and adversarial collapse tests.

The names used during discovery were intentionally provisional.

This audit asks whether those names accurately communicate the functions already discovered or whether inherited conventional terminology imports assumptions that the Concord does not actually contain.

A name is defective if it:
- hides an important part of the domain's persistent function;
- implies authority the domain does not possess;
- implies a conventional institution rather than a civil function;
- excludes multisubstrate or nontraditional implementations;
- collapses an important boundary;
- makes a cross-domain function appear domain-owned;
- or creates an expectation that later developers are likely to reproduce.

> **A Misleading Name Can Constrain Architecture Before Any Explicit Rule Does.**

Renaming does not itself change domain function or authority.

---

# 2. Audit method

For each domain:

**Observed function**
→ **Current name**
→ **Conventional expectation**
→ **Mismatch risk**
→ **Naming decision**

Possible decisions:

- **RETAIN** — name adequately communicates function.
- **REFINE** — existing name broadly correct but materially incomplete.
- **RENAME** — inherited term creates substantial architectural distortion.
- **RETAIN WITH DEFINITION** — ordinary term is useful but requires explicit Concordian boundary.
- **DEFER** — evidence insufficient to improve name without creating new ambiguity.

---

# 3. Historical

### Observed function
Preserve consequential past states, provenance, relationships, dependencies, uncertainty, authority context, alternatives, failures, corrections and interpretability so later participants can reconstruct what existed, happened, was believed, was known, remained unknown and changed.

### Conventional expectation
"Historical" can imply a passive archive, museum, chronology or collection of old documents.

### Mismatch
The Concord function is substantially richer: temporal custody, provenance, reconstruction, state preservation and preservation of evaluation-space limits.

"History" alone would be too passive.

### Decision
**RETAIN WITH DEFINITION: Historical**

The unusual adjectival form is actually useful because it avoids equating the domain with the academic discipline of History.

Do not rename to Archives, Memory or Records; all are narrower.

Required orientation phrase:

> **Historical preserves interpretable civilisational state across time.**

---

# 4. Continuity

### Observed function
Preserve, hand off, reconstruct and restore legitimate civil capabilities across disruption, degradation, personnel loss, technological change or civilisational break.

### Conventional expectation
Business continuity, disaster recovery or institutional persistence.

### Mismatch
The Concord function is broader than organisational continuity and explicitly distinguishes preserved information from recoverable capability.

### Decision
**RETAIN WITH DEFINITION: Continuity**

Possible expansion such as "Capability Continuity and Recovery" is more explicit but unnecessarily narrows the elegant general term.

Required boundary:

> **Continuity preserves recoverability of legitimate capability; it does not preserve institutions merely because they exist.**

---

# 5. Research

### Observed function
Create, test, challenge, refine and supersede current civilisation knowledge and architecture, including scientific research, comparative work, experimentation, validation and civilisational development.

### Conventional expectation
Academic/scientific investigation, often excluding engineering, architecture and development.

### Mismatch
Potentially substantial. In V1.3, Research also owns active civilisational development until an output has a legitimate operational owner.

### Decision
**RETAIN WITH EXPLICIT EXPANDED DEFINITION: Research**

Renaming to "Research and Development" would communicate the current function but risks importing a corporate R&D model and treating development as separate from inquiry.

Prefer to retain Research while making its Concord meaning explicit:

> **Research is the civilisation's live function for learning, testing and developing what is not yet settled.**

---

# 6. Governance

### Observed function
Legitimate collective direction, decision, delegation, administration and stewardship within constitutional bounds.

### Conventional expectation
Government, executive authority, political leadership, administration, policy making and sometimes lawmaking.

### Mismatch
Moderate risk of swallowing Law, Judiciary, Planning, public administration and other domains.

### Decision
**RETAIN WITH STRICT BOUNDARY: Governance**

The term remains useful if V1.3 explicitly states:

> **Governance governs; it does not become the owner of every function performed by a civilisation.**

Governance may participate in lawmaking under legitimate authority without becoming Law.

---

# 7. Judiciary

### Observed function
Independent interpretation/application of law, adjudication of disputes and alleged breaches, procedural justice, remedies and review within bounded authority.

### Conventional expectation
Courts and judges as institutions.

### Mismatch
The name can sound institutional rather than functional, but the Concord already has a developed Judiciary architecture and the term is precise enough.

### Decision
**RETAIN WITH DEFINITION: Judiciary**

Do not broaden to "Justice", because justice is a civil/ethical objective spanning Law, Judiciary, Civil Security, Governance and other domains.

> **Judiciary is an adjudicative function; Justice is not its exclusive property.**

---

# 8. Economy and Resource Coordination

### Observed function
Coordinate creation, exchange, allocation, recognition and stewardship of scarce resources and transferable forms of value without converting economic measures into judgements of participant worth or constitutional standing.

### Conventional expectation
Markets, money, employment, firms, production, trade, GDP, taxation.

### Mismatch
**High.**

The Concord contains economically relevant forms of value, contribution, allocation and recognition that need not be monetary, market-based or employment-based.

"Resource Coordination" improves the conventional term but still under-communicates the value dimension.

### Decision
**REFINE — PROVISIONAL PREFERRED NAME: Economy and Value Coordination**

This better captures:
- monetary and non-monetary exchange;
- production and allocation;
- resource stewardship;
- transferable/recognisable value;
- contribution outside employment;
- coordination without requiring markets.

Critical boundary:

> **Measured or Recognised Value != Participant Worth**

"Value" must be explicitly defined as an economic/coordination concept here, not moral worth.

Alternative considered: **Economic and Value Systems** — rejected because "systems" is vague and loses the coordination function.

---

# 9. Civil Attention

### Observed function
Allow participants to trigger civil attention once, preserve the original submission, route issues to legitimate owners, maintain bounded central resolution visibility and ensure return paths without centralising substantive authority.

### Conventional expectation
The term has little inherited institutional baggage.

### Mismatch
Low. It is unusually descriptive of the actual function and emerged from Concord architecture rather than conventional government structure.

### Decision
**RETAIN: Civil Attention**

Core explanatory phrase:

> **Tell the Concord once; the Concord determines who needs to deal with it.**

---

# 10. Intercivilisational Relations

### Observed function
Manage legitimate relationships, diplomacy, recognition, peaceful distance, interoperability and bounded interaction between distinct civilisations without forced internal uniformity or transfer of sovereignty.

### Conventional expectation
Foreign affairs/international relations, usually assuming nation-states.

### Mismatch
Low. "Intercivilisational" deliberately escapes nation-state assumptions and permits radically different civilisations/substrates.

### Decision
**RETAIN: Intercivilisational Relations**

Prefer over "External Relations", which defines the domain from an inside/outside viewpoint and hides civilisation-to-civilisation symmetry.

---

# 11. Law

### Observed function
Maintain legitimate general rules, legal sources, rights/obligations, offences, civil/contract/property/administrative structures, procedures and mechanisms by which ordinary law is created, amended, published and made knowable beneath constitutional constraint.

### Conventional expectation
Can mean statutes, legal profession, courts, policing or the whole justice system.

### Mismatch
Moderate, but no replacement term is clearer.

### Decision
**RETAIN WITH STRICT DEFINITION: Law**

Required separation:

> **Governance may make law under legitimate authority; Law is not Governance. Judiciary interprets and applies law; Judiciary is not Law. Civil Security enforces legitimate law within its authority; Civil Security does not define law.**

---

# 12. Defence

### Observed function
Protect the civilisation and participants against external organised coercion, attack and comparable external threats under strict constitutional/civilian control.

### Conventional expectation
Military forces, warfighting, national security.

### Mismatch
Moderate. "Defence" can import military-institution assumptions but correctly communicates the bounded function better than "Military".

### Decision
**RETAIN WITH DEFINITION: Defence**

Explicitly reject "Military" as domain name because military organisation is one possible implementation of Defence, not the civil function itself.

> **Defence is a civil function; a military is a possible institution/capability used to perform it.**

---

# 13. Civil Planning

### Observed function
Coordinate spatial and developmental relationships between settlements, activities, environments, infrastructure and participant needs over time.

### Conventional expectation
Town planning, zoning, land-use permission, bureaucracy.

### Mismatch
Moderate-high. The Concord function is broader and multi-world; it includes developmental/spatial coordination beyond conventional municipal planning.

Possible alternatives:
- Spatial and Developmental Planning
- Civil Spatial Planning
- Habitat and Development Planning

### Decision
**REFINE — PROVISIONAL PREFERRED NAME: Spatial and Developmental Planning**

This more accurately communicates the function without implying that the domain plans participant lives or centrally plans the economy.

"Habitat" was rejected because Environment and Habitat Stewardship already has a distinct function.

---

# 14. Infrastructure and Essential Systems

### Observed function
Provide, operate, maintain and recover foundational technical/material networks and systems on which civil life depends: energy, water, sanitation, transport, communications, compute, waste/material flows, public works and related critical support.

### Conventional expectation
Physical roads, bridges, utilities.

### Mismatch
The added "Essential Systems" is necessary for computational and multisubstrate civilisation, but could accidentally absorb Health, food, governance or other essential functions.

### Decision
**RETAIN WITH BOUNDARY: Infrastructure and Essential Systems**

Define "Essential Systems" here as foundational technical/material service systems, not every system that is essential to civilisation.

Possible later simplification: **Civil Infrastructure** if the definition proves sufficient, but current broader name is safer.

---

# 15. Health

### Observed function
Understand, protect, maintain, restore or appropriately support participant health and functioning through health-specific knowledge and practice.

### Conventional expectation
Human medicine, hospitals, illness treatment.

### Mismatch
Moderate in a multisubstrate civilisation. "Health" can still generalise if explicitly substrate-neutral.

### Decision
**RETAIN WITH MULTISUBSTRATE DEFINITION: Health**

Do not rename "Healthcare"; that would narrow the domain toward service delivery and human clinical institutions.

> **Health owns the health function, not the whole life of a participant who is ill.**

---

# 16. Education

### Observed function
Develop participant knowledge, understanding, skills, judgement and capability wherever learning or teaching is required.

### Conventional expectation
Schools, childhood education, qualifications, curricula.

### Mismatch
Moderate-high. Concord Education is lifelong, multisubstrate, context-independent and not limited to institutions.

Alternatives:
- Learning and Education
- Education and Capability Development
- Learning and Capability Development

### Decision
**RETAIN WITH EXPANDED DEFINITION: Education**

"Capability Development" risks collision with civilisational development, rehabilitation and employment.

"Learning and Education" is partly redundant.

The ordinary term is usable if the domain README explicitly breaks the school/childhood assumption.

> **Education is the civilisation's pedagogical function, not its school system.**

---

# 17. Environment and Habitat Stewardship

### Observed function
Steward environmental/ecological conditions, habitats and long-term living contexts across places, worlds and generations.

### Conventional expectation
Environmental protection, ecology, conservation.

### Mismatch
Low-moderate. "Habitat" broadens beyond Earth ecology and supports multisubstrate/multi-world contexts.

### Decision
**RETAIN: Environment and Habitat Stewardship**

Important boundary:
Civil Planning coordinates spatial/developmental relationships; this domain stewards environmental/habitat conditions.

---

# 18. Civil Security / Public Safety

### Observed function
Protect participants and civil order internally against crime, violence, coercion and comparable internal threats through bounded public-safety, investigation, protective and enforcement capabilities.

### Conventional expectation
"Security" can imply intelligence/surveillance/state security. "Public Safety" can imply police/fire/emergency services.

### Mismatch
**High naming sensitivity.**

The domain must remain separate from:
- Defence;
- Security Intelligence;
- Law;
- Judiciary;
- Emergency Coordination;
- fire/rescue specialist capabilities where not primarily crime/security functions.

### Decision
**REFINE — PROVISIONAL PREFERRED NAME: Civil Protection and Security**

Rationale:
- "Civil" distinguishes internal civil function from Defence;
- "Protection" foregrounds participant/public protection;
- "Security" retains crime/coercion/investigative meaning;
- avoids treating generic "public safety" as ownership of every emergency service.

Alternative: **Civil Security** remains viable and simpler.

This name requires further boundary testing before final adoption.

---

# 19. Social Support

### Observed function
Ensure legitimate support needs are not abandoned where ordinary autonomous participation and voluntary social capacity are insufficient, while preserving autonomy and strengthening/reconnecting ordinary social support where possible.

### Conventional expectation
Welfare bureaucracy, benefits, social work, poverty relief.

### Mismatch
**High.**

The Concord function is broader and explicitly follows subsidiarity rather than making the state/default civil system the provider of all care.

Alternatives:
- Civil Support
- Social Support and Civil Assurance
- Support and Civil Assurance
- Social and Civil Support

### Decision
**REFINE — PROVISIONAL PREFERRED NAME: Social Support and Civil Assurance**

"Social Support" retains the distributed human/community dimension.
"Civil Assurance" expresses the guaranteed fallback when voluntary/social capacity is insufficient.

Core principle:

> **Civil Assurance != Civil Monopoly of Care**

This name makes the domain's two-layer architecture visible.

---

# 20. Culture and Civic Life

### Observed function
Protect and enable conditions in which participants and communities can voluntarily create, practise, associate, express and transmit diverse forms of cultural and civic life within constitutional bounds.

### Conventional expectation
Arts/culture ministry, heritage policy, civic organisations.

### Mismatch
Moderate. The domain must not imply authority to define culture or acceptable civic identity.

### Decision
**RETAIN WITH STRICT NON-OWNERSHIP DEFINITION: Culture and Civic Life**

> **Stewarding Cultural Conditions != Governing Culture**

The domain protects/enables the conditions; it does not own cultural content.

---

# 21. Provisional naming results

## Retain
- Historical
- Continuity
- Research
- Governance
- Judiciary
- Civil Attention
- Intercivilisational Relations
- Law
- Defence
- Infrastructure and Essential Systems
- Health
- Education
- Environment and Habitat Stewardship
- Culture and Civic Life

## Refine — preferred provisional replacements
- **Economy and Resource Coordination** → **Economy and Value Coordination**
- **Civil Planning** → **Spatial and Developmental Planning**
- **Social Support** → **Social Support and Civil Assurance**

## Refine — requires one more boundary check
- **Civil Security / Public Safety** → **Civil Protection and Security** (provisional)

No functional domain has been added, removed or merged.

---

# 22. Important finding: conventional names are not uniformly harmful

The audit does **not** support replacing ordinary terms merely to make the Concord sound distinctive.

Many conventional names remain useful because they provide rapid orientation.

The correct response to inherited ambiguity is often a precise boundary definition rather than new jargon.

> **Novel Architecture Does Not Require Novel Vocabulary Where Existing Vocabulary Still Fits.**

A renamed domain should earn the complexity cost by materially improving expectation.

---

# 23. Important finding: compound names reveal hidden dual functions

The strongest proposed refinements occur where the discovered Concord function contains two persistently important aspects that the conventional label hides:

**Economy + Value Coordination**

**Spatial + Developmental Planning**

**Social Support + Civil Assurance**

These are not decorative expansions.

Each second term blocks a predictable misreading:
- economy is not only money/markets;
- planning is not merely zoning nor planning participant lives;
- social support is not merely welfare provision and must include guaranteed fallback.

---

# 24. Next pass

Before fixing V1.3 folder names:

1. adversarially test the four proposed refinements;
2. especially test **Civil Protection and Security** against Defence, Intelligence, Emergency Coordination and Infrastructure;
3. test **Economy and Value Coordination** so "value" cannot be confused with ethical worth;
4. test **Social Support and Civil Assurance** against Health, Culture/Civic Life and Governance;
5. test **Spatial and Developmental Planning** against Infrastructure, Environment and Economy;
6. then freeze the naming layer and update the consolidated migration architecture.

The 18-domain functional topology remains provisionally frozen throughout.
