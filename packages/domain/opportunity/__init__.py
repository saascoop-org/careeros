"""Opportunity domain package."""

from .entities import Opportunity
from .enums import (
    CompensationPeriod,
    EmploymentType,
    OpportunityStatus,
    RequirementLevel,
    SeniorityLevel,
    WorkModel,
)
from .exceptions import OpportunityValidationError
from .value_objects import (
    CompensationRange,
    ExternalSource,
    Location,
    OpportunityRequirement,
    Organization,
)

__all__ = [
    "CompensationPeriod",
    "CompensationRange",
    "EmploymentType",
    "ExternalSource",
    "Location",
    "Opportunity",
    "OpportunityRequirement",
    "OpportunityStatus",
    "OpportunityValidationError",
    "Organization",
    "RequirementLevel",
    "SeniorityLevel",
    "WorkModel",
]
