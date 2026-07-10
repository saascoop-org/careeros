"""Value objects for the Opportunity bounded context."""

from dataclasses import dataclass, field
from decimal import Decimal
from urllib.parse import urlparse

from packages.domain.professional_identity import LocalizedText

from .enums import CompensationPeriod, RequirementLevel
from .exceptions import OpportunityValidationError


@dataclass(frozen=True, slots=True)
class Organization:
    """Organization, company or client offering the opportunity."""

    name: str
    website: str | None = None
    industry: str | None = None

    def __post_init__(self) -> None:
        name = self.name.strip()
        if not name:
            raise OpportunityValidationError("Organization name is required.")
        object.__setattr__(self, "name", name)

        if self.website is not None:
            website = self.website.strip()
            parsed = urlparse(website)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                raise OpportunityValidationError(
                    "Organization website must be a valid HTTP or HTTPS URL."
                )
            object.__setattr__(self, "website", website)

        if self.industry is not None:
            industry = self.industry.strip()
            if not industry:
                raise OpportunityValidationError(
                    "Organization industry cannot be blank."
                )
            object.__setattr__(self, "industry", industry)


@dataclass(frozen=True, slots=True)
class Location:
    """Geographic location associated with an opportunity."""

    country_code: str | None = None
    region: str | None = None
    city: str | None = None
    timezone: str | None = None

    def __post_init__(self) -> None:
        if self.country_code is not None:
            country_code = self.country_code.strip().upper()
            if len(country_code) != 2 or not country_code.isalpha():
                raise OpportunityValidationError(
                    "country_code must be a two-letter ISO code."
                )
            object.__setattr__(self, "country_code", country_code)

        for field_name in ("region", "city", "timezone"):
            value = getattr(self, field_name)
            if value is not None:
                normalized = value.strip()
                if not normalized:
                    raise OpportunityValidationError(
                        f"{field_name} cannot be blank."
                    )
                object.__setattr__(self, field_name, normalized)


@dataclass(frozen=True, slots=True)
class CompensationRange:
    """Optional compensation range for an opportunity."""

    currency: str
    period: CompensationPeriod
    minimum: Decimal | None = None
    maximum: Decimal | None = None

    def __post_init__(self) -> None:
        currency = self.currency.strip().upper()
        if len(currency) != 3 or not currency.isalpha():
            raise OpportunityValidationError(
                "currency must be a three-letter ISO code."
            )
        object.__setattr__(self, "currency", currency)

        if self.minimum is not None and self.minimum < 0:
            raise OpportunityValidationError(
                "minimum compensation cannot be negative."
            )
        if self.maximum is not None and self.maximum < 0:
            raise OpportunityValidationError(
                "maximum compensation cannot be negative."
            )
        if (
            self.minimum is not None
            and self.maximum is not None
            and self.maximum < self.minimum
        ):
            raise OpportunityValidationError(
                "maximum compensation cannot be lower than minimum."
            )


@dataclass(frozen=True, slots=True)
class OpportunityRequirement:
    """A normalized requirement or responsibility from an opportunity."""

    requirement_id: str
    text: LocalizedText
    level: RequirementLevel
    category: str | None = None
    keywords: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        requirement_id = self.requirement_id.strip()
        if not requirement_id:
            raise OpportunityValidationError("requirement_id is required.")
        object.__setattr__(self, "requirement_id", requirement_id)

        if self.category is not None:
            category = self.category.strip().lower()
            if not category:
                raise OpportunityValidationError(
                    "Requirement category cannot be blank."
                )
            object.__setattr__(self, "category", category)

        normalized_keywords = tuple(
            keyword.strip()
            for keyword in self.keywords
            if keyword.strip()
        )
        if len(normalized_keywords) != len(set(normalized_keywords)):
            raise OpportunityValidationError(
                "Requirement keywords must be unique."
            )
        object.__setattr__(self, "keywords", normalized_keywords)


@dataclass(frozen=True, slots=True)
class ExternalSource:
    """External platform or document where the opportunity originated."""

    platform: str
    uri: str | None = None
    external_identifier: str | None = None

    def __post_init__(self) -> None:
        platform = self.platform.strip().lower()
        if not platform:
            raise OpportunityValidationError(
                "External source platform is required."
            )
        object.__setattr__(self, "platform", platform)

        if self.uri is not None:
            uri = self.uri.strip()
            parsed = urlparse(uri)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                raise OpportunityValidationError(
                    "External source URI must be a valid HTTP or HTTPS URL."
                )
            object.__setattr__(self, "uri", uri)

        if self.external_identifier is not None:
            identifier = self.external_identifier.strip()
            if not identifier:
                raise OpportunityValidationError(
                    "external_identifier cannot be blank."
                )
            object.__setattr__(self, "external_identifier", identifier)
