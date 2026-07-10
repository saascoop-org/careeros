# ADR 0003: Use Knowledge Graph plus Vector Search

## Status

Proposed

## Context

Career data is relational, temporal, semantic and evidence-based.

## Decision

Use PostgreSQL for canonical records, Neo4j for professional relationships and a Vector Database for semantic retrieval.

## Consequences

- More infrastructure to operate.
- Stronger reasoning over projects, skills, evidence and career artifacts.
- Better support for RAG and agent workflows.
