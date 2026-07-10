"""Tests for the Opportunity aggregate."""

from datetime import UTC, datetime, timedelta
from uuid import uuid4

import pytest

from packages.domain.opportunity import (
    Opportunity,
    OpportunityRequirement,
    OpportunityStatus,
    OpportunityValidationError,
    Organization,
    RequirementLevel,
)
from packages.domain.professional_identity import LocalizedText


def _localized(value: str) -> LocalizedText:
    return LocalizedText(values={"en": value})


def test_create_valid_open_opportunity() -> None:
    opportunity = Opportunity(
        opportunity_id=uuid4(),
        schema_version="1.0",
        title=_localized("Microsoft Data Subject Matter Expert"),
        description=_localized(
            "Review and validate technical learning content."
        ),
        organization=Organization(name="Example Client"),
        status=OpportunityStatus.OPEN,
        requirements=(
            OpportunityRequirement(
                requirement_id="req-001",
                text=_localized("Experience with Microsoft Fabric"),
                level=RequirementLevel.REQUIRED,
                keywords=("Microsoft Fabric",),
            ),
        ),
        languages=("en",),
        keywords=("Microsoft Fabric", "Power BI"),
    )

    assert opportunity.status is OpportunityStatus.OPEN
    assert opportunity.requirements[0].requirement_id == "req-001"


def test_open_opportunity_requires_requirements_or_responsibilities() -> None:
    with pytest.raises(OpportunityValidationError, match="Open opportunities"):
        Opportunity(
            opportunity_id=uuid4(),
            schema_version="1.0",
            title=_localized("Data Consultant"),
            description=_localized("Consulting opportunity"),
            organization=Organization(name="Example Client"),
            status=OpportunityStatus.OPEN,
        )


def test_duplicate_requirement_ids_are_rejected() -> None:
    requirement = OpportunityRequirement(
        requirement_id="req-001",
        text=_localized("Power BI experience"),
        level=RequirementLevel.REQUIRED,
    )

    with pytest.raises(OpportunityValidationError, match="identifiers"):
        Opportunity(
            opportunity_id=uuid4(),
            schema_version="1.0",
            title=_localized("BI Consultant"),
            description=_localized("BI consulting opportunity"),
            organization=Organization(name="Example Client"),
            requirements=(requirement, requirement),
        )


def test_closing_date_cannot_precede_publication_date() -> None:
    published_at = datetime.now(UTC)

    with pytest.raises(OpportunityValidationError, match="closes_at"):
        Opportunity(
            opportunity_id=uuid4(),
            schema_version="1.0",
            title=_localized("Data Engineer"),
            description=_localized("Data engineering opportunity"),
            organization=Organization(name="Example Client"),
            published_at=published_at,
            closes_at=published_at - timedelta(days=1),
        )


def test_duplicate_keywords_are_rejected() -> None:
    with pytest.raises(OpportunityValidationError, match="keywords"):
        Opportunity(
            opportunity_id=uuid4(),
            schema_version="1.0",
            title=_localized("Power BI Consultant"),
            description=_localized("Analytics opportunity"),
            organization=Organization(name="Example Client"),
            keywords=("Power BI", "Power BI"),
        )
