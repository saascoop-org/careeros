"""Value objects for the Evidence bounded context."""

from dataclasses import dataclass
from datetime import datetime
from types import MappingProxyType
from typing import Mapping
from uuid import UUID

from .enums import (
    EvidenceSourceType,
    EvidenceVisibility,
    TransformationType,
)
from .exceptions import EvidenceValidationError


@dataclass(frozen=True, slots=True)
class ConfidenceScore:
    """Normalized confidence score between zero and one."""

    value: float

    def __post_init__(self) -> None:
        if not 0.0 <= self.value <= 1.0:
            raise EvidenceValidationError(
                "Confidence score must be between 0.0 and 1.0."
            )


@dataclass(frozen=True, slots=True)
class ContentFingerprint:
    """Hash metadata used to detect source-content changes."""

    algorithm: str
    value: str

    def __post_init__(self) -> None:
        algorithm = self.algorithm.strip().lower()
        value = self.value.strip().lower()

        expected_lengths = {"sha256": 64, "sha512": 128}
        if algorithm not in expected_lengths:
            raise EvidenceValidationError(
                "Fingerprint algorithm must be sha256 or sha512."
            )
        if len(value) != expected_lengths[algorithm]:
            raise EvidenceValidationError(
                f"{algorithm} fingerprints must contain "
                f"{expected_lengths[algorithm]} hexadecimal characters."
            )
        if any(character not in "0123456789abcdef" for character in value):
            raise EvidenceValidationError(
                "Fingerprint value must contain only hexadecimal characters."
            )

        object.__setattr__(self, "algorithm", algorithm)
        object.__setattr__(self, "value", value)


@dataclass(frozen=True, slots=True)
class EvidenceSource:
    """Description of the original evidence source."""

    source_type: EvidenceSourceType
    label: str
    uri: str | None = None
    external_identifier: str | None = None

    def __post_init__(self) -> None:
        label = self.label.strip()
        if not label:
            raise EvidenceValidationError("Evidence source label is required.")
        object.__setattr__(self, "label", label)

        if self.uri is not None:
            uri = self.uri.strip()
            if not uri:
                raise EvidenceValidationError("Source URI cannot be blank.")
            object.__setattr__(self, "uri", uri)

        if self.external_identifier is not None:
            identifier = self.external_identifier.strip()
            if not identifier:
                raise EvidenceValidationError(
                    "external_identifier cannot be blank."
                )
            object.__setattr__(self, "external_identifier", identifier)


@dataclass(frozen=True, slots=True)
class Consent:
    """User consent and intended evidence visibility."""

    granted: bool
    visibility: EvidenceVisibility
    purpose: str | None = None
    granted_at: datetime | None = None

    def __post_init__(self) -> None:
        if self.granted and self.granted_at is None:
            raise EvidenceValidationError(
                "Granted consent requires granted_at."
            )
        if not self.granted and self.granted_at is not None:
            raise EvidenceValidationError(
                "Denied consent cannot define granted_at."
            )
        if self.purpose is not None:
            purpose = self.purpose.strip()
            if not purpose:
                raise EvidenceValidationError(
                    "Consent purpose cannot be blank."
                )
            object.__setattr__(self, "purpose", purpose)


@dataclass(frozen=True, slots=True)
class ClaimReference:
    """Reference to a professional entity or claim supported by evidence."""

    entity_id: UUID
    entity_type: str
    claim_path: str | None = None

    def __post_init__(self) -> None:
        entity_type = self.entity_type.strip()
        if not entity_type:
            raise EvidenceValidationError("entity_type is required.")
        object.__setattr__(self, "entity_type", entity_type)

        if self.claim_path is not None:
            claim_path = self.claim_path.strip()
            if not claim_path:
                raise EvidenceValidationError(
                    "claim_path cannot be blank."
                )
            object.__setattr__(self, "claim_path", claim_path)


@dataclass(frozen=True, slots=True)
class TransformationRecord:
    """Immutable description of a transformation applied to evidence."""

    transformation_type: TransformationType
    performed_at: datetime
    performed_by: str
    metadata: Mapping[str, str] | None = None

    def __post_init__(self) -> None:
        performed_by = self.performed_by.strip()
        if not performed_by:
            raise EvidenceValidationError("performed_by is required.")
        object.__setattr__(self, "performed_by", performed_by)

        if self.metadata is not None:
            normalized = {
                key.strip(): value.strip()
                for key, value in self.metadata.items()
                if key.strip() and value.strip()
            }
            object.__setattr__(
                self,
                "metadata",
                MappingProxyType(normalized),
            )
