# Decision Process

## Default workflow

1. Open an issue describing the problem.
2. Explain the context, alternatives and constraints.
3. Collect feedback.
4. Implement through a pull request.
5. Record significant architectural decisions in an ADR.
6. Link the issue, ADR and pull request.
7. Publish the outcome.

## When an ADR is required

- new bounded context;
- database or infrastructure strategy;
- AI provider coupling;
- data ownership change;
- security or privacy model;
- external project dependency;
- integration protocol;
- major governance-related technical constraint.

## Disagreements

Maintainers should seek consensus.

When consensus is not possible, the responsible maintainer records:

- the decision;
- alternatives;
- objections;
- consequences;
- review date.

## Emergency decisions

Security incidents may require immediate action. The decision must be documented after containment.
