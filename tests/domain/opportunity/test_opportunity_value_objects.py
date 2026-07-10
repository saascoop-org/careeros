"""Tests for Opportunity value objects."""

from decimal import Decimal

import pytest

from packages.domain.opportunity import (
    CompensationPeriod,
    CompensationRange,
    ExternalSource,
    Location,
    OpportunityRequirement,
    OpportunityValidationError,
    Organization,
    RequirementLevel,
)
from packages.domain.professional_identity import LocalizedText


def _localized(value: str) -> LocalizedText:
    return LocalizedText(values={"en": value})


def test_organization_requires_name() -> None:
    with pytest.raises(OpportunityValidationError, match="name"):
        Organization(name=" ")


def test_organization_rejects_invalid_website() -> None:
    with pytest.raises(OpportunityValidationError, match="website"):
        Organization(name="Example Client", website="not-a-url")


def test_location_normalizes_country_code() -> None:
    location = Location(country_code="br", city="São Paulo")

    assert location.country_code == "BR"


def test_compensation_rejects_invalid_range() -> None:
    with pytest.raises(OpportunityValidationError, match="maximum"):
        CompensationRange(
            currency="USD",
            period=CompensationPeriod.HOURLY,
            minimum=Decimal("100"),
            maximum=Decimal("50"),
        )


def test_compensation_rejects_invalid_currency() -> None:
    with pytest.raises(OpportunityValidationError, match="currency"):
        CompensationRange(
            currency="US",
            period=CompensationPeriod.HOURLY,
        )


def test_requirement_rejects_duplicate_keywords() -> None:
    with pytest.raises(OpportunityValidationError, match="unique"):
        OpportunityRequirement(
            requirement_id="req-001",
            text=_localized("Experience with Power BI"),
            level=RequirementLevel.REQUIRED,
            keywords=("Power BI", "Power BI"),
        )


def test_external_source_requires_valid_uri() -> None:
    with pytest.raises(OpportunityValidationError, match="URI"):
        ExternalSource(
            platform="upwork",
            uri="invalid",
        )
