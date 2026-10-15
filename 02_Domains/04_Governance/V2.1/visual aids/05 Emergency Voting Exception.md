# Emergency voting exception

An emergency does not allow the creation of a two-person triad. Three steward positions must first have been selected. In an authorised emergency context, two affirmative votes can trigger action before the third vote arrives. Ordinary decisions await all three votes. The exceptional action and its provenance must be recorded.

```mermaid
flowchart TD
 A[Valid triad already constituted] --> B[Collect sealed votes]
 B --> C{All three received?}
 C -->|Yes| D[Final ordinary outcome]
 C -->|No| E{Authorised emergency context?}
 E -->|No| F[Wait for remaining vote]
 E -->|Yes| G{Two affirmative votes received?}
 G -->|No| F
 G -->|Yes| H[Emergency action may trigger]
 H --> I[Record exceptional action and provenance]
 F --> B
```
