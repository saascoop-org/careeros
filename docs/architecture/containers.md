# Container View

## MVP containers

```mermaid
flowchart TB
    CLI[CLI]
    API[FastAPI API]
    APP[Application Core]
    DB[(PostgreSQL or local structured files)]
    GEN[Document Generator]
    LLM[Optional LLM Adapter]
    OUT[(Markdown / PDF outputs)]

    CLI --> APP
    API --> APP
    APP --> DB
    APP --> LLM
    APP --> GEN
    GEN --> OUT
```

## Initial implementation recommendation

For the first real application:

- YAML or JSON for the user profile;
- YAML or Markdown for the opportunity;
- Python application service;
- Jinja2 or equivalent template engine;
- Markdown output;
- PDF export as a separate adapter;
- optional LLM adapter behind an interface.

PostgreSQL should be introduced when multiple users, concurrent access or richer querying become necessary.
