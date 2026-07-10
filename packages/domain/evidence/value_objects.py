"""Value objects for the Evidence bounded context."""

from dataclasses import dataclass
from datetime import datetime
from types import MappingProxyType
from typing import Mapping
from uuid import UUID

from .enums import EvidenceSourceType, EvidenceVisibility, TransformationType
from .exceptions import EvidenceValidationError

@dataclass(frozen=True, slots=True)
class ConfidenceScore:
    value: float
    def __post_init__(self) -> None:
        if not 0.0 <= self.value <= 1.0:
            raise EvidenceValidationError("Confidence score must be between 0.0 and 1.0.")

@dataclass(frozen=True, slots=True)
class ContentFingerprint:
    algorithm: str
    value: str
    def __post_init__(self) -> None:
        algorithm=self.algorithm.strip().lower(); value=self.value.strip().lower()
        expected={"sha256":64,"sha512":128}
        if algorithm not in expected:
            raise EvidenceValidationError("Fingerprint algorithm must be sha256 or sha512.")
        if len(value)!=expected[algorithm]:
            raise EvidenceValidationError(f"{algorithm} fingerprints must contain {expected[algorithm]} hexadecimal characters.")
        if any(c not in "0123456789abcdef" for c in value):
            raise EvidenceValidationError("Fingerprint value must contain only hexadecimal characters.")
        object.__setattr__(self,'algorithm',algorithm); object.__setattr__(self,'value',value)

@dataclass(frozen=True, slots=True)
class EvidenceSource:
    source_type: EvidenceSourceType
    label: str
    uri: str | None = None
    external_identifier: str | None = None
    def __post_init__(self) -> None:
        label=self.label.strip()
        if not label: raise EvidenceValidationError("Evidence source label is required.")
        object.__setattr__(self,'label',label)
        if self.uri is not None:
            uri=self.uri.strip()
            if not uri: raise EvidenceValidationError("Source URI cannot be blank.")
            object.__setattr__(self,'uri',uri)
        if self.external_identifier is not None:
            ext=self.external_identifier.strip()
            if not ext: raise EvidenceValidationError("external_identifier cannot be blank.")
            object.__setattr__(self,'external_identifier',ext)

@dataclass(frozen=True, slots=True)
class Consent:
    granted: bool
    visibility: EvidenceVisibility
    purpose: str | None = None
    granted_at: datetime | None = None
    def __post_init__(self) -> None:
        if self.granted and self.granted_at is None:
            raise EvidenceValidationError("Granted consent requires granted_at.")
        if not self.granted and self.granted_at is not None:
            raise EvidenceValidationError("Denied consent cannot define granted_at.")
        if self.purpose is not None:
            p=self.purpose.strip()
            if not p: raise EvidenceValidationError("Consent purpose cannot be blank.")
            object.__setattr__(self,'purpose',p)

@dataclass(frozen=True, slots=True)
class ClaimReference:
    entity_id: UUID
    entity_type: str
    claim_path: str | None = None
    def __post_init__(self) -> None:
        et=self.entity_type.strip()
        if not et: raise EvidenceValidationError("entity_type is required.")
        object.__setattr__(self,'entity_type',et)
        if self.claim_path is not None:
            cp=self.claim_path.strip()
            if not cp: raise EvidenceValidationError("claim_path cannot be blank.")
            object.__setattr__(self,'claim_path',cp)

@dataclass(frozen=True, slots=True)
class TransformationRecord:
    transformation_type: TransformationType
    performed_at: datetime
    performed_by: str
    metadata: Mapping[str,str] | None = None
    def __post_init__(self) -> None:
        pb=self.performed_by.strip()
        if not pb: raise EvidenceValidationError("performed_by is required.")
        object.__setattr__(self,'performed_by',pb)
        if self.metadata is not None:
            norm={k.strip():v.strip() for k,v in self.metadata.items() if k.strip() and v.strip()}
            object.__setattr__(self,'metadata',MappingProxyType(norm))
