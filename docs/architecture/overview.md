# Architecture Overview

## Architectural style

CareerOS uses:

- Domain-Driven Design for domain boundaries;
- Clean Architecture for dependency direction;
- Hexagonal Architecture for external integrations;
- event-oriented integration where asynchronous behavior adds value;
- explicit provenance for generated content;
- modular monolith first, distributed services only when justified.

## Dependency rule

Dependencies must point inward:

```text
Interfaces / Infrastructure
            ↓
       Application
            ↓
          Domain
```

The domain cannot depend on:

- FastAPI;
- databases;
- OpenAI or another model provider;
- PDF libraries;
- GitHub;
- LinkedIn;
- FreireAI;
- cloud services.

## Initial modules

```text
careeros
├── professional_identity
├── opportunities
├── tailoring
├── documents
├── evidence
├── shared
└── interfaces
```

## MVP execution flow

```text
Structured Profile
        +
Opportunity Description
        ↓
Opportunity Analyzer
        ↓
Evidence Ranker
        ↓
Résumé Composer
        ↓
Claim Validator
        ↓
Markdown / PDF / Evidence Map
```

## Evolution rule

The architecture should evolve through validated use cases. Enterprise patterns must solve a concrete problem and not be added only for appearance.
