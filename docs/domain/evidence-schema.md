# Evidence Schema v1

## Files

- Domain: `packages/domain/evidence/`
- JSON Schema: `schemas/evidence.schema.json`
- YAML example: `schemas/examples/evidence.example.yml`
- Tests: `tests/domain/evidence/`

## Design

The domain uses standard-library dataclasses and enums, remaining independent from FastAPI, Pydantic, SQLAlchemy, storage and AI SDKs.

## Compatibility

The existing Professional Identity `EvidenceReference` remains unchanged. The full Evidence aggregate is resolved through an application port using `evidence_id`.

## Versioning

The initial schema version is `1.0`. Breaking field changes require a major schema version and migration notes.
