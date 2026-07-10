# Architecture Overview

## Style

CareerOS uses:

- Domain-Driven Design
- Clean Architecture
- Hexagonal Architecture
- Event-driven workflows
- Multi-agent orchestration
- Knowledge Graph + RAG

## Layers

```mermaid
flowchart TB
    API[API / UI / CLI] --> Application[Application Use Cases]
    Application --> Domain[Domain Model]
    Application --> Ports[Ports]
    Ports --> Infrastructure[Infrastructure Adapters]
    Infrastructure --> Databases[(PostgreSQL / Neo4j / Vector DB)]
    Infrastructure --> External[LinkedIn, GitHub, Upwork, ORCID, PDFs, DOCX]
```

## Why this architecture

This structure keeps the career domain independent from vendors, LLM providers, databases and ingestion sources. It supports long-term maintainability and makes the project suitable for open source collaboration.
