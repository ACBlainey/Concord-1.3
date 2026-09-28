# Cultural Works Creation, Discovery and Distribution Architecture 001

**Author:** Alexander C. Blainey — Independent Researcher  
**Project:** The Concord Framework  
**Framework Version:** Concord V1.3  
**Status:** ACTIVE DEVELOPMENT / PROVISIONAL / NON-CANONICAL  
**Date:** September 2026  
**Origin:** User sketch — Culture

---

# 1. Source proposition

The originating sketch proposes a civil system through which participants can:
- create cultural works;
- host or make those works available;
- distribute them;
- search/discover digital works;
- discover representations and locations of physical works;
- discover physical venues and events;
- retain creator control over works and pricing where legitimately theirs;
- gain visibility/acclaim without requiring patronage, gatekeeping or nepotistic access.

This document develops that proposition without turning Concord into a cultural authority, taste arbiter or compulsory distributor.

---

# 2. Source resolution

Existing Culture architecture already provides principle-level foundations:
- voluntary creation, practice, association, expression and transmission;
- peaceful heterogeneity and non-conformity;
- authority-light cultural coexistence;
- stewardship/preservation of cultural works;
- provenance/authorship/version history;
- Contextual Wrapper for culturally distinct spaces/events/communities;
- Civil Attention for cultural/civic concerns.

Commerce supplies exchange architecture.
Historical supplies temporal custody/preservation.
Neither should be duplicated here.

The missing layer is an operating architecture for **creator-controlled publication/discovery/distribution and cultural-space discovery**.

---

# 3. Persistent function

> **Enable participants to create, publish, discover, access, exchange and preserve cultural works and cultural opportunities without requiring a central authority to decide what culture is worthy.**

---

# 4. Cultural work

A cultural work may include:
- writing;
- visual art;
- music/audio;
- performance;
- film/video;
- games/interactive works;
- design;
- craft;
- mixed media;
- digital-native works;
- physical works;
- representations of physical works;
- other participant-created cultural expression.

This is illustrative, not exhaustive.

---

# 5. Creator control

Where a participant legitimately controls a work, the system should allow them to determine, subject to applicable rights/law:
- whether to publish;
- whether to withdraw future distribution;
- price or free access;
- licensing terms;
- authorised versions;
- attribution;
- permitted distribution channels;
- physical/digital availability.

> **Publication Infrastructure != Ownership of the Work.**

> **Hosting != Authorship.**

> **Discovery != Transfer of Control.**

---

# 6. Provenance

Cultural works should support provenance sufficient to distinguish:
- creator/claimed creator where legitimately knowable;
- pseudonymous/anonymous authorship;
- version;
- derivative relationship;
- edition;
- authorised distributor/host where relevant;
- authenticity state;
- disputed attribution.

Historical/KCS provenance mechanisms should be reused.

> **Provenance Support != Mandatory Identity Disclosure.**

---

# 7. Publication object

Candidate:

`CulturalWork = <WorkID, CreatorOrAttributionState, WorkClass, VersionState, AccessState, DistributionTermsRef, PriceOrExchangeRef, RepresentationRefs, PhysicalLocationRefs, Provenance, HistoricalRef>`

Not every field must be public.

---

# 8. Discovery layer

Participants should be able to search/browse by legitimate metadata such as:
- work type;
- creator where disclosed;
- subject/theme;
- language;
- medium;
- location;
- accessibility;
- availability;
- date;
- event/venue;
- participant-selected tags;
- provenance/authenticity state where relevant.

The system should support both:
- intentional search;
- exploratory discovery.

---

# 9. Discovery is not cultural authority

A discovery system can become a de facto gatekeeper if one ranking determines visibility.

Therefore:

> **Search Rank != Cultural Worth.**

> **Visibility != Merit.**

> **Popularity != Cultural Authority.**

Discovery should support plural views rather than one canonical ranking.

Possible views:
- relevance to explicit query;
- recent;
- local;
- new creator;
- participant-selected categories;
- random/exploratory;
- peer/community-curated collections;
- critic/editor-curated collections;
- accessibility-compatible;
- event/time-specific;
- popularity/acclaim indicators where explicitly requested.

No single view should silently become the civilisation's taste function.

---

# 10. Acclaim

The source sketch seeks a route for artists to gain acclaim without gatekeeping/nepotism.

This should not become a universal acclaim score.

Acclaim may instead be represented as plural evidence:
- audience engagement;
- reviews;
- awards;
- peer recognition;
- community curation;
- sales/exchange;
- repeat attendance;
- citations/references;
- derivative influence;
- historical significance.

These are not equivalent.

> **Recognition Evidence != Universal Cultural Score.**

> **Popularity != Quality != Historical Significance != Commercial Success.**

---

# 11. Anti-gatekeeping architecture

The system should reduce unnecessary dependency on:
- one publisher;
- one gallery;
- one broadcaster;
- one venue owner;
- one recommender;
- one critic;
- one algorithm.

This does not abolish legitimate curators.

Curators can add value through:
- selection;
- criticism;
- expertise;
- thematic collections;
- trusted recommendation.

The protection is plurality and exit.

> **Curation != Sovereign Gatekeeping.**

---

# 12. Physical works

A physical work may have:
- digital representation;
- description;
- creator/provenance;
- current display/location where legitimately public;
- venue;
- accessibility information;
- sale/exhibition state.

The system should not publish private location merely because a work exists.

> **Discoverability of a Work != Entitlement to Its Physical Location.**

---

# 13. Venues and events

Participants should be able to discover:
- galleries;
- theatres;
- music/performance spaces;
- workshops;
- cultural/community spaces;
- temporary events;
- exhibitions;
- other legitimate cultural venues.

Contextual Wrapper Architecture should describe:
- access;
- local rules;
- restrictions;
- permissions;
- sensory/contextual conditions;
- exit;
- remedy.

A venue can therefore remain culturally distinctive without requiring uniform rules.

---

# 14. Digital hosting

The architecture may support:
- creator-hosted works;
- community hosts;
- commercial hosts;
- civil/shared hosting;
- distributed hosting.

The Culture domain need not own every copy.

> **Cultural Discovery Layer != Mandatory Central Repository.**

---

# 15. Distribution

Distribution may include:
- direct digital access;
- streaming;
- download;
- physical delivery;
- print/manufacture on demand;
- venue access;
- licensing;
- lending;
- exhibition;
- performance.

Exact legal rights remain for Law/IP architecture.

---

# 16. Commerce interface

Creators may choose:
- free distribution;
- sale;
- subscription;
- donation/support;
- licensing;
- commission;
- other legitimate exchange.

Commerce handles settlement/contract/consumer architecture.

Culture handles cultural discovery/participation context.

> **Cultural Value != Market Price.**

> **Commercial Success != Cultural Authority.**

---

# 17. Creator economic autonomy

Where the creator legitimately controls price/terms:

> **Platform Discovery Should Not Silently Become Price Control.**

But creator control does not override:
- law;
- prior contractual rights;
- consumer protections;
- legitimate collective rights;
- scarcity/venue constraints.

---

# 18. Recommendation

Recommendation can help participants navigate abundance.

But recommendation systems can become hidden cultural governors.

Requirements should include:
- distinguish recommendation from search;
- disclose material basis where practical;
- allow user control;
- permit alternative recommenders/views;
- avoid secret pay-to-rank where represented as neutral;
- preserve routes for new/low-visibility creators.

> **Recommendation != Canonical Cultural Judgement.**

---

# 19. New creator problem

A system optimised around prior engagement can make established creators increasingly visible and new creators increasingly invisible.

Therefore discovery should retain routes that do not require prior fame.

Possible mechanisms:
- new-work views;
- random/exploratory sampling;
- participant-controlled filters;
- local/community discovery;
- rotating exposure;
- open submission to voluntary curators.

No guaranteed acclaim follows.

> **Opportunity for Discovery != Entitlement to Attention.**

---

# 20. Nepotism and patronage

The source sketch specifically identifies nepotism/gatekeeping.

Architecture can reduce structural dependence on insider access by ensuring:
- direct publication routes;
- direct searchable presence;
- transparent venue/submission requirements where applicable;
- multiple curators/venues;
- direct participant-to-audience routes.

It cannot guarantee that participants will not prefer friends, familiar creators or particular communities.

> **Open Access to Publication != Guaranteed Equal Audience.**

---

# 21. Cultural safe spaces

Some cultural communities may legitimately be:
- membership-based;
- private;
- age-bounded;
- culturally specific;
- sensory-specific;
- invitation-based;
- protected.

Peaceful Heterogeneity and Contextual Wrapper govern these boundaries.

Open civilisation-wide discovery must not erase legitimate protected spaces.

---

# 22. Harm and rights boundary

Culture should remain authority-light.

Restrictions on cultural works should come from legitimate rights/law/safe-space architecture, not a central taste authority.

> **Offence, Unpopularity or Non-Conformity Alone != Cultural Prohibition.**

Specific rights/harm questions remain external to this architecture.

---

# 23. Historical interface

Historically significant cultural material may enter Historical custody/reference through legitimate processes.

But:

> **Historical Value != Automatic Unlimited Retention Authority.**

and:

> **Historical Preservation != Continuing Distribution Permission.**

Historical preserves temporal/provenance state; it does not inherit creator rights merely by preserving a record.

---

# 24. Cultural lineage

Where legitimate, relationships may preserve:
- influence;
- derivative work;
- adaptation;
- translation;
- performance history;
- edition;
- restoration;
- reinterpretation.

These relations can make culture navigable across time without asserting that influence is objectively complete.

---

# 25. Withdrawal and persistence

A creator may legitimately withdraw future publication/distribution in some contexts.

But:
- already sold physical copies may persist;
- lawful derivatives may persist;
- Historical records may have separate retention grounds;
- third-party rights may exist.

Therefore:

> **Withdrawal From Current Distribution != Erasure of Historical Existence.**

Exact rights require Law.

---

# 26. Civil Attention

Participants can use Civil Attention for:
- inaccessible cultural infrastructure;
- venue/system problems;
- discriminatory process claims;
- discovery-system manipulation;
- preservation concerns;
- proposed cultural services.

But:

> **Submission Volume != Cultural Merit.**

Civil Attention routes concerns; it does not select art.

---

# 27. Metrics boundary

Aggregate cultural metrics may help understand:
- venue demand;
- accessibility;
- underserved regions;
- infrastructure capacity;
- discovery concentration;
- new-creator visibility;
- preservation demand.

They must not silently become a cultural score.

> **Measure the System Without Pretending to Measure the Worth of Culture Itself.**

---

# 28. Discovery concentration metric

A useful system-health metric may ask:

How concentrated is visibility?

This does not imply concentration is automatically bad.

It can expose:
- algorithmic lock-in;
- platform capture;
- lack of discovery routes;
- extreme dependence on few intermediaries.

The metric evaluates infrastructure, not creator worth.

---

# 29. Cultural interoperability

A work may exist across:
- formats;
- hosts;
- venues;
- communities;
- substrates.

Standardised metadata/interface can improve discovery while preserving heterogeneous cultural content.

This echoes:

> **Standardise the Interface; Preserve Legitimate Contextual Variation.**

---

# 30. Participant-controlled discovery profile

A participant may choose discovery preferences.

Such preferences should not automatically become a permanent civil profile.

> **Cultural Preference Data != General Participant Identity.**

Privacy/minimum-necessary data rules apply.

---

# 31. AI and hybrid creators

The architecture should not assume all creators are human.

Creator/attribution states may include:
- human;
- AI;
- hybrid;
- collective;
- anonymous;
- pseudonymous;
- disputed/unknown.

Legal ownership/personhood questions remain external.

> **Ability to Create != Automatic Resolution of Legal Ownership or Personhood.**

---

# 32. Failure modes

## Central taste authority
One institution decides cultural worth.

## Algorithmic gatekeeping
Recommendation becomes unavoidable visibility control.

## Popularity lock-in
Prior attention recursively creates all future attention.

## Pay-to-rank opacity
Commercial promotion masquerades as neutral relevance.

## Identity coercion
Creators must reveal civil identity to participate unnecessarily.

## Cultural homogenisation
Interoperability standards dictate substantive content.

## Historical appropriation
Preservation is treated as ownership/distribution permission.

## Market reduction
Commercial success becomes cultural worth.

## Metric capture
Creators optimise to system metric rather than cultural purpose.

## Venue capture
Few physical venues become unavoidable cultural gatekeepers.

---

# 33. Candidate machine objects

`CulturalWork = <WorkID, AttributionState, WorkClass, VersionState, AccessState, DistributionTermsRef, ExchangeRef, RepresentationRefs, VenueOrLocationRefs, Provenance, HistoricalRef>`

`CulturalDiscoveryEntry = <WorkOrEventRef, MetadataRefs, AvailabilityState, AccessContextRef, DiscoveryViews, Provenance>`

`RecognitionEvidence = <SubjectRef, EvidenceClass, SourceRef, Context, TimeWindow, VerificationState, Provenance>`

No universal recognition score is implied.

---

# 34. Design invariants

> **Publication Infrastructure != Ownership of the Work.**

> **Search Rank != Cultural Worth.**

> **Popularity != Cultural Authority.**

> **Recognition Evidence != Universal Cultural Score.**

> **Curation != Sovereign Gatekeeping.**

> **Cultural Discovery Layer != Mandatory Central Repository.**

> **Cultural Value != Market Price.**

> **Recommendation != Canonical Cultural Judgement.**

> **Opportunity for Discovery != Entitlement to Attention.**

> **Open Access to Publication != Guaranteed Equal Audience.**

> **Historical Preservation != Continuing Distribution Permission.**

> **Measure the System Without Pretending to Measure the Worth of Culture Itself.**

---

# 35. Development status

**PROVISIONAL CULTURAL OPERATING ARCHITECTURE / SOURCE-RESOLVED / REQUIRES ADVERSARIAL TESTING**

Recommended tests:
- unknown creator versus famous creator;
- paid promotion;
- coordinated popularity manipulation;
- pseudonymous creator;
- withdrawn work;
- disputed authorship;
- offensive but lawful/non-harmful work;
- protected cultural space;
- scarce venue slots;
- inaccessible venue;
- AI-created work;
- hybrid authorship;
- derivative work dispute;
- preservation against creator wishes;
- monopoly host failure;
- recommender capture;
- local minority culture with low aggregate demand.

