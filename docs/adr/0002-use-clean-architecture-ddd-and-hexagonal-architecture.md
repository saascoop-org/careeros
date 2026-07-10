# ADR 0002: Use Clean Architecture, DDD and Hexagonal Architecture

## Status

Proposed

## Context

CareerOS must integrate many external platforms while preserving a stable career domain model.

## Decision

We will isolate domain logic from frameworks, databases and external providers using Clean Architecture and Hexagonal Architecture.

## Alternatives considered

- Simple monolithic CRUD app: faster initially, weaker long-term modularity.
- Fully distributed microservices: powerful but too expensive and complex for MVP.

## Consequences

- Slower initial setup.
- Better testability and long-term maintainability.
- Easier migration between infrastructure providers.
