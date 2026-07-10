# ADR 0004: Keep CareerOS independent and enable future interoperability

## Status

Accepted

## Date

2026-07-09

## Context

CareerOS and FreireAI are open source initiatives within the broader SaaSCoop ecosystem, but they are at different stages of maturity and have distinct primary missions.

CareerOS focuses on structuring, maintaining and activating a person's professional identity. Its core capabilities include consolidating professional evidence, building a career knowledge base, generating career documents and supporting employability decisions.

FreireAI focuses on education, learning, pedagogical support and access to knowledge.

There is a plausible future relationship between both projects. For example, CareerOS could identify skill gaps and FreireAI could support a learning journey, while verified learning achievements could later become professional evidence in CareerOS.

However, implementing this integration now would introduce architectural and organizational coupling before either product has a stable integration requirement, mature domain contracts or validated user demand.

## Decision

CareerOS will be designed, developed, deployed and governed as an independent product.

CareerOS must not require FreireAI, or any other SaaSCoop project, to perform its core responsibilities.

Any future integration with FreireAI or other ecosystem projects must be optional and implemented through explicit, versioned and technology-neutral contracts, such as:

- public APIs;
- domain events;
- import and export schemas;
- MCP-compatible interfaces;
- optional adapters or plugins.

Integration-specific code must remain outside the CareerOS core domain and must not introduce direct dependencies from domain entities or use cases to another SaaSCoop project.

The current CareerOS MVP will not include a FreireAI integration.

## Scope

This decision applies to:

- source-code dependencies;
- runtime dependencies;
- deployment topology;
- domain models;
- data ownership;
- release cycles;
- project governance;
- branding and product communication.

## Architectural principles

1. **Independent value:** CareerOS must deliver value when deployed by itself.
2. **Low coupling:** Cross-project integrations must depend on stable contracts rather than internal implementation details.
3. **Optional interoperability:** Integrations may enrich the platform, but they must not become mandatory for core use cases.
4. **Data ownership:** CareerOS remains authoritative for professional identity data under its responsibility.
5. **Replaceable adapters:** An integration adapter can be disabled or replaced without changing the CareerOS domain.
6. **Evolutionary design:** Integration work begins only after a validated use case and a sufficiently stable contract exist.

## Integration entry criteria

A future integration proposal should be evaluated only when all the following conditions are met:

- both projects have a minimally stable product boundary;
- a concrete user journey demonstrates measurable value;
- data ownership and consent responsibilities are documented;
- the contract can be versioned independently;
- failure of the external project does not break CareerOS core capabilities;
- security, privacy and audit requirements are defined;
- the proposal is recorded in a new ADR.

## Alternatives considered

### Embed CareerOS within FreireAI

Rejected because it would reduce CareerOS autonomy, blur product boundaries and make professional identity management dependent on an educational platform.

### Embed FreireAI capabilities within CareerOS

Rejected because education is not part of the CareerOS core domain and would significantly expand the MVP scope.

### Build the integration immediately

Rejected because the current projects do not yet have stable contracts or validated integration requirements.

### Keep the projects permanently isolated

Rejected because optional interoperability may create future value for users and the SaaSCoop ecosystem.

## Consequences

### Positive

- CareerOS can evolve and be adopted independently.
- The MVP remains focused and easier to validate.
- Each project can use its own roadmap and release cycle.
- Future integrations can be tested and replaced without modifying the core domain.
- External communities can adopt CareerOS without adopting the full SaaSCoop ecosystem.
- Architectural coupling is postponed until there is evidence that it is necessary.

### Negative

- Future integration will require explicit contract design and adapter implementation.
- Some shared capabilities may initially be duplicated.
- Cross-project user journeys will not be available in the first CareerOS versions.

### Risks

- Product teams may create informal integrations that bypass the approved contracts.
- Ecosystem messaging may imply a level of integration that does not yet exist.
- Premature reuse of shared internal libraries could create hidden coupling.

These risks will be mitigated through architecture reviews, ADRs, dependency checks and clear product documentation.

## Non-goals

This decision does not:

- prevent CareerOS from being part of the SaaSCoop ecosystem;
- prevent future collaboration between CareerOS and FreireAI;
- define the future integration protocol;
- create a shared data model across all SaaSCoop projects;
- establish FreireAI as a CareerOS dependency.

## Future review

This ADR should be reviewed when:

- CareerOS and FreireAI both have stable MVPs;
- a validated user journey requires data exchange between them;
- a shared interoperability standard is proposed for SaaSCoop projects;
- regulatory, privacy or governance requirements materially change.

Any modification to this decision must be recorded in a new ADR that supersedes this one.
