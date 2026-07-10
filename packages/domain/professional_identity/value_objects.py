"""Value objects for the Professional Identity domain."""
from dataclasses import dataclass, field
from datetime import date
from typing import Mapping
from uuid import UUID
from .enums import EvidenceStatus
from .exceptions import DomainValidationError

@dataclass(frozen=True, slots=True)
class LocalizedText:
    values: Mapping[str, str]
    default_language: str = "en"

    def __post_init__(self) -> None:
        normalized = {k.strip(): v.strip() for k, v in self.values.items() if k.strip() and v.strip()}
        if not normalized:
            raise DomainValidationError("LocalizedText requires at least one non-empty value.")
        if self.default_language not in normalized:
            raise DomainValidationError("default_language must identify one of the available localized values.")
        object.__setattr__(self, "values", normalized)

    def get(self, language: str | None = None) -> str:
        selected = language or self.default_language
        return self.values.get(selected, self.values[self.default_language])

@dataclass(frozen=True, slots=True)
class DateRange:
    start_year: int
    start_month: int | None = None
    start_day: int | None = None
    end_year: int | None = None
    end_month: int | None = None
    end_day: int | None = None
    is_current: bool = False

    def __post_init__(self) -> None:
        if self.start_year < 1900:
            raise DomainValidationError("start_year must be 1900 or later.")
        self._validate_month_day(self.start_year, self.start_month, self.start_day, "start")
        if self.is_current and any(v is not None for v in (self.end_year, self.end_month, self.end_day)):
            raise DomainValidationError("Current date ranges cannot define an end date.")
        if self.end_year is not None:
            self._validate_month_day(self.end_year, self.end_month, self.end_day, "end")
            if self.end_year < self.start_year:
                raise DomainValidationError("end_year cannot be earlier than start_year.")
            if self.end_year == self.start_year and self.start_month is not None and self.end_month is not None and self.end_month < self.start_month:
                raise DomainValidationError("End month cannot be earlier than start month.")
        if self.end_year is None and any(v is not None for v in (self.end_month, self.end_day)):
            raise DomainValidationError("end_month and end_day require end_year.")

    @staticmethod
    def _validate_month_day(year: int, month: int | None, day: int | None, label: str) -> None:
        if month is None and day is not None:
            raise DomainValidationError(f"{label}_day requires {label}_month.")
        if month is not None and not 1 <= month <= 12:
            raise DomainValidationError(f"{label}_month must be between 1 and 12.")
        if day is not None:
            try:
                date(year, month or 1, day)
            except ValueError as exc:
                raise DomainValidationError(f"Invalid {label} date.") from exc

@dataclass(frozen=True, slots=True)
class EvidenceReference:
    evidence_id: UUID
    status: EvidenceStatus = EvidenceStatus.UNVERIFIED
    source_label: str | None = None

    def __post_init__(self) -> None:
        if self.source_label is not None and not self.source_label.strip():
            raise DomainValidationError("source_label cannot be blank.")
        if self.source_label is not None:
            object.__setattr__(self, "source_label", self.source_label.strip())

@dataclass(frozen=True, slots=True)
class PersonName:
    full_name: str
    preferred_name: str | None = None

    def __post_init__(self) -> None:
        full_name = self.full_name.strip()
        if not full_name:
            raise DomainValidationError("full_name is required.")
        object.__setattr__(self, "full_name", full_name)
        if self.preferred_name is not None:
            preferred = self.preferred_name.strip()
            object.__setattr__(self, "preferred_name", preferred or None)

@dataclass(frozen=True, slots=True)
class ContactInformation:
    email: str | None = None
    phone: str | None = None
    city: str | None = None
    country_code: str | None = None
    website_urls: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if self.email is not None and "@" not in self.email:
            raise DomainValidationError("email must contain '@'.")
        if self.country_code is not None and len(self.country_code.strip()) != 2:
            raise DomainValidationError("country_code must be a two-letter ISO code.")
