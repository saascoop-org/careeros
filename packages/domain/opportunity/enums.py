"""Enumerations for the Opportunity bounded context."""

from enum import StrEnum


class EmploymentType(StrEnum):
    """Engagement or employment arrangement."""

    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    FREELANCE = "freelance"
    INTERNSHIP = "internship"
    TEMPORARY = "temporary"
    VOLUNTEER = "volunteer"
    OTHER = "other"


class WorkModel(StrEnum):
    """Where the work is expected to happen."""

    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"
    FLEXIBLE = "flexible"
    UNSPECIFIED = "unspecified"


class SeniorityLevel(StrEnum):
    """Seniority expected by the opportunity."""

    INTERN = "intern"
    ENTRY = "entry"
    JUNIOR = "junior"
    MID = "mid"
    SENIOR = "senior"
    LEAD = "lead"
    PRINCIPAL = "principal"
    MANAGER = "manager"
    DIRECTOR = "director"
    EXECUTIVE = "executive"
    UNSPECIFIED = "unspecified"


class RequirementLevel(StrEnum):
    """Importance of an opportunity requirement."""

    REQUIRED = "required"
    PREFERRED = "preferred"
    OPTIONAL = "optional"


class OpportunityStatus(StrEnum):
    """Lifecycle status of an opportunity."""

    DRAFT = "draft"
    OPEN = "open"
    PAUSED = "paused"
    CLOSED = "closed"
    ARCHIVED = "archived"


class CompensationPeriod(StrEnum):
    """Period used by a compensation range."""

    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    FIXED = "fixed"
