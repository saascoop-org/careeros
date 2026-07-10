"""Entities and aggregate root for Opportunity."""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from packages.domain.professional_identity import LocalizedText

from .enums import (
    EmploymentType,
    OpportunityStatus,
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


@dataclass(frozen=True, slots=True)
class Opportunity:
    """Aggregate root representing a professional opportunity."""

    opportunity_id: UUID
    schema_version: str
    title: LocalizedText
    description: LocalizedText
    organization: Organization
    status: OpportunityStatus = OpportunityStatus.DRAFT
    employment_type: EmploymentType = EmploymentType.OTHER
    work_model: WorkModel = WorkModel.UNSPECIFIED
    seniority: SeniorityLevel = SeniorityLevel.UNSPECIFIED
    locations: tuple[Location, ...] = field(default_factory=tuple)
    languages: tuple[str, ...] = field(default_factory=tuple)
    responsibilities: tuple[LocalizedText, ...] = field(default_factory=tuple)
    requirements: tuple[OpportunityRequirement, ...] = field(
        default_factory=tuple
    )
    keywords: tuple[str, ...] = field(default_factory=tuple)
    compensation: CompensationRange | None = None
    source: ExternalSource | None = None
    published_at: datetime | None = None
    closes_at: datetime | None = None

    def __post_init__(self) -> None:
        version = self.schema_version.strip()
        if not version:
            raise OpportunityValidationError("schema_version is required.")
        object.__setattr__(self, "schema_version", version)

        normalized_languages = tuple(
            language.strip()
            for language in self.languages
            if language.strip()
        )
        if len(normalized_languages) != len(set(normalized_languages)):
            raise OpportunityValidationError(
                "Opportunity languages must be unique."
            )
        object.__setattr__(self, "languages", normalized_languages)

        normalized_keywords = tuple(
            keyword.strip()
            for keyword in self.keywords
            if keyword.strip()
        )
        if len(normalized_keywords) != len(set(normalized_keywords)):
            raise OpportunityValidationError(
                "Opportunity keywords must be unique."
            )
        object.__setattr__(self, "keywords", normalized_keywords)

        requirement_ids = [
            requirement.requirement_id for requirement in self.requirements
        ]
        if len(requirement_ids) != len(set(requirement_ids)):
            raise OpportunityValidationError(
                "Requirement identifiers must be unique."
            )

        if (
            self.published_at is not None
            and self.closes_at is not None
            and self.closes_at < self.published_at
        ):
            raise OpportunityValidationError(
                "closes_at cannot be earlier than published_at."
            )

        if (
            self.status is OpportunityStatus.OPEN
            and not self.requirements
            and not self.responsibilities
        ):
            raise OpportunityValidationError(
                "Open opportunities require at least one requirement "
                "or responsibility."
            )
