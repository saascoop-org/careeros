# System Context

```mermaid
flowchart LR
    U[Professional User]
    C[CareerOS]
    F[Local Files]
    M[LLM Provider]
    E[Exported Application Package]
    X[Future External Sources]

    U -->|profile, opportunity, review| C
    F -->|evidence and structured data| C
    C -->|optional bounded prompt| M
    M -->|structured suggestion| C
    C -->|résumé, reports, evidence map| E
    X -. optional future connectors .-> C
```

## Trust boundary

CareerOS is the system responsible for:

- professional profile records;
- opportunity records;
- evidence references;
- generated artifacts;
- approval and audit metadata.

An LLM is an external reasoning service, not the source of truth.
