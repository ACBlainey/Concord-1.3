# Triad formation and alternate stewards

A complete triad requires three selected positions before voting authority can activate. If an original steward is absent, an authorised alternate can take the position. An original cannot be arbitrarily removed; a returning original may supersede an alternate subject to voting-stage conditions. Substitution does not create a fourth vote.

```mermaid
flowchart TD
 A[Decision requires governance] --> B[Identify steward roles]
 B --> C[Select eligible stewards]
 C --> D{Three positions filled?}
 D -->|No| E[Find eligible parallels or alternates]
 E --> C
 D -->|Yes| F[Valid triad constituted]
 F --> G{Original absent?}
 G -->|No| H[Three originals proceed]
 G -->|Yes| I[Authorised alternate takes position]
 I --> J{Original returns before applicable voting boundary?}
 J -->|Yes| K[Original resumes position]
 J -->|No| L[Alternate continues]
 H --> M[Independent voting]
 K --> M
 L --> M
```
