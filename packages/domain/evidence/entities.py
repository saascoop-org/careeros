"""Entities and aggregate roots for Evidence and Provenance."""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from .enums import CollectionMethod, VerificationStatus
from .exceptions import EvidenceValidationError
from .value_objects import ClaimReference, ConfidenceScore, Consent, ContentFingerprint, EvidenceSource, TransformationRecord

@dataclass(frozen=True, slots=True)
class Evidence:
    evidence_id: UUID
    schema_version: str
    source: EvidenceSource
    collection_method: CollectionMethod
    collected_at: datetime
    verification_status: VerificationStatus
    confidence: ConfidenceScore
    consent: Consent
    fingerprint: ContentFingerprint | None = None
    content_reference: str | None = None
    claims: tuple[ClaimReference, ...] = field(default_factory=tuple)
    transformations: tuple[TransformationRecord, ...] = field(default_factory=tuple)
    supersedes_evidence_id: UUID | None = None
    def __post_init__(self) -> None:
        version=self.schema_version.strip()
        if not version: raise EvidenceValidationError("schema_version is required.")
        object.__setattr__(self,'schema_version',version)
        if self.content_reference is not None:
            ref=self.content_reference.strip()
            if not ref: raise EvidenceValidationError("content_reference cannot be blank.")
            object.__setattr__(self,'content_reference',ref)
        if self.verification_status is VerificationStatus.REJECTED and self.confidence.value != 0.0:
            raise EvidenceValidationError("Rejected evidence must have zero confidence.")
        keys={(c.entity_id,c.entity_type,c.claim_path) for c in self.claims}
        if len(keys)!=len(self.claims):
            raise EvidenceValidationError("Evidence cannot contain duplicate claim references.")
        if self.supersedes_evidence_id == self.evidence_id:
            raise EvidenceValidationError("Evidence cannot supersede itself.")
