"""Entities and aggregate root for Professional Identity."""
from dataclasses import dataclass, field
from uuid import UUID
from .enums import LanguageProficiency, PublicationType, SkillLevel
from .exceptions import DomainValidationError
from .value_objects import ContactInformation, DateRange, EvidenceReference, LocalizedText, PersonName

def _validate_non_blank(value: str, field_name: str) -> str:
    cleaned = value.strip()
    if not cleaned:
        raise DomainValidationError(f"{field_name} cannot be blank.")
    return cleaned

@dataclass(frozen=True, slots=True)
class Experience:
    experience_id: UUID
    organization: str
    role: LocalizedText
    period: DateRange
    description: LocalizedText | None = None
    achievements: tuple[LocalizedText, ...] = field(default_factory=tuple)
    technologies: tuple[str, ...] = field(default_factory=tuple)
    evidence: tuple[EvidenceReference, ...] = field(default_factory=tuple)
    def __post_init__(self) -> None:
        object.__setattr__(self, "organization", _validate_non_blank(self.organization, "organization"))

@dataclass(frozen=True, slots=True)
class Project:
    project_id: UUID
    name: LocalizedText
    description: LocalizedText
    role: LocalizedText | None = None
    period: DateRange | None = None
    technologies: tuple[str, ...] = field(default_factory=tuple)
    outcomes: tuple[LocalizedText, ...] = field(default_factory=tuple)
    urls: tuple[str, ...] = field(default_factory=tuple)
    evidence: tuple[EvidenceReference, ...] = field(default_factory=tuple)

@dataclass(frozen=True, slots=True)
class Skill:
    skill_id: UUID
    name: str
    level: SkillLevel | None = None
    years_of_experience: float | None = None
    evidence: tuple[EvidenceReference, ...] = field(default_factory=tuple)
    def __post_init__(self) -> None:
        object.__setattr__(self, "name", _validate_non_blank(self.name, "skill name"))
        if self.years_of_experience is not None and self.years_of_experience < 0:
            raise DomainValidationError("years_of_experience cannot be negative.")

@dataclass(frozen=True, slots=True)
class Certification:
    certification_id: UUID
    name: str
    issuer: str
    issued_year: int
    credential_url: str | None = None
    expires_year: int | None = None
    evidence: tuple[EvidenceReference, ...] = field(default_factory=tuple)
    def __post_init__(self) -> None:
        object.__setattr__(self, "name", _validate_non_blank(self.name, "certification name"))
        object.__setattr__(self, "issuer", _validate_non_blank(self.issuer, "issuer"))
        if self.expires_year is not None and self.expires_year < self.issued_year:
            raise DomainValidationError("expires_year cannot be earlier than issued_year.")

@dataclass(frozen=True, slots=True)
class Education:
    education_id: UUID
    institution: str
    program: LocalizedText
    period: DateRange
    description: LocalizedText | None = None
    evidence: tuple[EvidenceReference, ...] = field(default_factory=tuple)
    def __post_init__(self) -> None:
        object.__setattr__(self, "institution", _validate_non_blank(self.institution, "institution"))

@dataclass(frozen=True, slots=True)
class Language:
    language_code: str
    proficiency: LanguageProficiency
    evidence: tuple[EvidenceReference, ...] = field(default_factory=tuple)
    def __post_init__(self) -> None:
        code = self.language_code.strip()
        if not 2 <= len(code) <= 10:
            raise DomainValidationError("language_code must be a valid language tag.")
        object.__setattr__(self, "language_code", code)

@dataclass(frozen=True, slots=True)
class Publication:
    publication_id: UUID
    title: LocalizedText
    publication_type: PublicationType
    published_year: int
    publisher: str | None = None
    url: str | None = None
    evidence: tuple[EvidenceReference, ...] = field(default_factory=tuple)

@dataclass(frozen=True, slots=True)
class ProfessionalProfile:
    profile_id: UUID
    schema_version: str
    name: PersonName
    contact: ContactInformation = field(default_factory=ContactInformation)
    summaries: tuple[LocalizedText, ...] = field(default_factory=tuple)
    experiences: tuple[Experience, ...] = field(default_factory=tuple)
    projects: tuple[Project, ...] = field(default_factory=tuple)
    skills: tuple[Skill, ...] = field(default_factory=tuple)
    certifications: tuple[Certification, ...] = field(default_factory=tuple)
    education: tuple[Education, ...] = field(default_factory=tuple)
    languages: tuple[Language, ...] = field(default_factory=tuple)
    publications: tuple[Publication, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        version = self.schema_version.strip()
        if not version:
            raise DomainValidationError("schema_version is required.")
        object.__setattr__(self, "schema_version", version)
        self._ensure_unique_identifiers()

    def _ensure_unique_identifiers(self) -> None:
        identifiers: list[UUID] = []
        identifiers.extend(item.experience_id for item in self.experiences)
        identifiers.extend(item.project_id for item in self.projects)
        identifiers.extend(item.skill_id for item in self.skills)
        identifiers.extend(item.certification_id for item in self.certifications)
        identifiers.extend(item.education_id for item in self.education)
        identifiers.extend(item.publication_id for item in self.publications)
        if len(identifiers) != len(set(identifiers)):
            raise DomainValidationError("Entity identifiers must be unique within a ProfessionalProfile.")
