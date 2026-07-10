# Data Flow and Provenance

## Rule

Generated statements must preserve a connection to source evidence.

## Simplified flow

```mermaid
sequenceDiagram
    actor User
    participant Profile as Profile Repository
    participant Opportunity as Opportunity Analyzer
    participant Tailoring as Tailoring Engine
    participant Composer as Résumé Composer
    participant Validator as Claim Validator

    User->>Profile: Provide or update career evidence
    User->>Opportunity: Provide opportunity description
    Opportunity->>Tailoring: Structured requirements
    Profile->>Tailoring: Approved professional evidence
    Tailoring->>Composer: Ranked evidence with explanations
    Composer->>Validator: Draft résumé and evidence references
    Validator-->>User: Validated output and warnings
```

## Provenance fields

Every generated claim should support:

- claim identifier;
- source entity identifier;
- source type;
- source location;
- verification status;
- confidence;
- transformation explanation;
- generation timestamp;
- model or rule version;
- user approval status.
