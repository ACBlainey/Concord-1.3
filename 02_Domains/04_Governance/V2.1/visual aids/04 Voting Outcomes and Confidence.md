# Voting outcomes and confidence

All three votes matter equally. The affirmative support metric is the number of affirmative votes divided by three. Three for = 100%; two for = 66.7% (often expressed as 66%); one for = 33.3% (often 33%); zero for = 0%. Two matching affirmative votes produce an ordinary affirmative outcome only once all three votes are received. A missing vote is not a negative vote. The metric is vote support, not a statistical probability that a decision is correct.

```mermaid
flowchart TD
 A[Three votes committed] --> B{Number voting FOR?}
 B -->|3| C[Approved: 100% affirmative support]
 B -->|2| D[Approved: 66.7% affirmative support]
 B -->|1| E[Not approved: 33.3% affirmative support]
 B -->|0| F[Not approved: 0% affirmative support]
 C --> G[Final and irrevocable]
 D --> G
 E --> G
 F --> G
```
