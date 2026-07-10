"""Enumerations for the Evidence bounded context."""

from enum import StrEnum

class EvidenceSourceType(StrEnum):
    USER_STATEMENT = "user_statement"
    EMPLOYMENT_RECORD = "employment_record"
    CERTIFICATE = "certificate"
    DOCUMENT = "document"
    GITHUB_REPOSITORY = "github_repository"
    PROFESSIONAL_PROFILE = "professional_profile"
    PUBLICATION = "publication"
    VIDEO = "video"
    WEBSITE = "website"
    API = "api"
    OTHER = "other"

class CollectionMethod(StrEnum):
    MANUAL = "manual"
    FILE_IMPORT = "file_import"
    API_IMPORT = "api_import"
    DOCUMENT_EXTRACTION = "document_extraction"
    USER_CONFIRMATION = "user_confirmation"
    SYSTEM_GENERATED = "system_generated"

class VerificationStatus(StrEnum):
    UNVERIFIED = "unverified"
    USER_CONFIRMED = "user_confirmed"
    SOURCE_VERIFIED = "source_verified"
    INDEPENDENTLY_VERIFIED = "independently_verified"
    REJECTED = "rejected"

class EvidenceVisibility(StrEnum):
    PRIVATE = "private"
    RESTRICTED = "restricted"
    PUBLIC = "public"

class TransformationType(StrEnum):
    EXTRACTED = "extracted"
    NORMALIZED = "normalized"
    TRANSLATED = "translated"
    SUMMARIZED = "summarized"
    REDACTED = "redacted"
    USER_EDITED = "user_edited"
