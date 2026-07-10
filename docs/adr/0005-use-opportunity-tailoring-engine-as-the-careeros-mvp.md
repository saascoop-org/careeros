# ADR 0005: Use the Opportunity Tailoring Engine as the CareerOS MVP

## Status

Accepted

## Date

2026-07-09

## Context

CareerOS has a broad long-term vision that includes professional identity, knowledge graphs, connectors, career intelligence, AI agents and multiple generated career assets.

Implementing the complete vision before validating a concrete user need would increase scope, technical risk and time to first value.

A current real-world need exists: generate a truthful and tailored résumé for an international Upwork opportunity involving Microsoft data technologies and Subject Matter Expert responsibilities.

This provides a concrete validation case for the CareerOS concept.

## Decision

The first CareerOS MVP will be the **Opportunity Tailoring Engine**.

It will receive:

- a structured professional profile;
- approved professional evidence;
- a specific opportunity description;
- output preferences.

It will generate:

- a tailored résumé;
- opportunity match analysis;
- keyword coverage;
- evidence traceability;
- optional supporting application artifacts.

The MVP will use a modular monolith and local structured files before introducing distributed services, Neo4j, a vector database or autonomous multi-agent orchestration.

## Architectural constraints

- the domain must remain independent from FastAPI and AI providers;
- generated claims must reference evidence;
- AI-assisted output must be reviewable;
- the user must approve the final artifact;
- the opportunity must be replaceable without code changes;
- a second opportunity must be supported before the MVP is considered reusable.

## Alternatives considered

### Build the complete CareerOS platform first

Rejected because it delays validation and introduces unnecessary early complexity.

### Build only a generic résumé template

Rejected because it would not validate opportunity-specific tailoring or evidence ranking.

### Generate the résumé manually and document it later

Rejected because it would not produce a reusable software capability.

### Begin with automatic external profile ingestion

Rejected because authentication, scraping, data quality and privacy would distract from the central value hypothesis.

## Consequences

### Positive

- validates the product with a real application;
- creates an immediate useful output;
- limits the MVP scope;
- establishes evidence and provenance early;
- produces a public case study;
- creates a foundation for future career assets.

### Negative

- the initial profile requires manual structuring;
- the first release has limited automation;
- some enterprise infrastructure is postponed;
- PDF rendering may initially be basic.

## Success criteria

The MVP is considered validated when:

- the real Upwork résumé is generated;
- no unsupported claims are present;
- each selected claim has evidence;
- the user approves the result;
- tests cover the core workflow;
- a second opportunity can be processed without code changes.

## Future review

Review this ADR after the first two real applications or before introducing persistent databases, external connectors or multi-agent orchestration.
