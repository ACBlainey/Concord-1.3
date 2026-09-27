# Concord Domain Interfaces

This folder is the integration registry between the common Civil Attention system and individual Concord domains.

Each participating Concord system should ultimately have a corresponding Civil Attention companion/interface record here **and** a dedicated Civil Attention subfolder within the domain itself.

The domain-local folder owns the domain-specific implementation/companion material. This root registry owns the cross-system map and common routing visibility.

## Required Domain Interface

Each domain integration should identify:
- receiving function(s);
- accepted Issue classes;
- DAO binding;
- protected-information boundary;
- return-state mapping;
- dependency interfaces;
- Responsibility Resolution route;
- review/Clock interface;
- escalation/challenge route;
- link to the domain-local Civil Attention companion.

## Integration Rule

Do not copy and modify the Civil Attention core into each domain.

Reference the graduated core and append the domain companion.

> **Standardise the interface; preserve legitimate contextual variation.**

## Rollout State

The root Civil Attention architecture is now established. Domain-local companion deployment is the next integration phase and should be source-resolved against each Concord system rather than bulk-generated from folder names alone.