"""Exceptions for the Opportunity bounded context."""


class OpportunityValidationError(ValueError):
    """Raised when an Opportunity domain invariant is violated."""
