# Opportunity Schema v1

## Files

- Domain models: `packages/domain/opportunity/`
- JSON Schema: `schemas/opportunity.schema.json`
- YAML example: `schemas/examples/opportunity.example.yml`
- Tests: `tests/domain/opportunity/`

## Modeling approach

The Python domain uses standard-library dataclasses, enums and value objects.

It remains independent from:

- FastAPI;
- Pydantic;
- databases;
- ATS SDKs;
- marketplace APIs;
- AI providers;
- YAML and JSON parsing libraries.

## Main structure

```text
Opportunity
├── LocalizedText title
├── LocalizedText description
├── Organization
├── Location[]
├── LocalizedText responsibilities[]
├── OpportunityRequirement[]
├── CompensationRange?
└── ExternalSource?
```

## External-platform compatibility

CareerOS does not model LinkedIn, Upwork, Greenhouse, Lever, Workday or another
platform directly in the core domain.

Each connector should translate its source payload into this stable contract.

Examples:

```text
Upwork adapter      ─┐
LinkedIn adapter    ─┼─> Opportunity
ATS adapter         ─┤
Manual YAML loader  ─┘
```

## Versioning

The initial schema version is `1.0`.

Optional backward-compatible fields may be added through a compatible schema
revision. Field removals, renames or semantic changes require a major schema
version and migration documentation.
