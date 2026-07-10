# Professional Profile Schema v1

## Files

- `packages/domain/professional_identity/`
- `schemas/professional-profile.schema.json`
- `schemas/examples/professional-profile.example.yml`
- `tests/domain/professional_identity/`

## Modeling approach

The core uses standard-library dataclasses to remain independent from FastAPI, Pydantic, SQLAlchemy, databases and AI SDKs. Parsing and serialization belong to adapters outside the domain.

## Main model

```text
ProfessionalProfile
├── PersonName
├── ContactInformation
├── LocalizedText[]
├── Experience[]
├── Project[]
├── Skill[]
├── Certification[]
├── Education[]
├── Language[]
└── Publication[]
```

The Python model is the authoritative source for current domain invariants. The JSON Schema is the first interoperability contract and can be expanded when the YAML loader is implemented.
