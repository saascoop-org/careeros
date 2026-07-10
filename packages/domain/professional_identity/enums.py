"""Enumerations used by the Professional Identity domain."""
from enum import StrEnum

class EvidenceStatus(StrEnum):
    UNVERIFIED = "unverified"
    USER_CONFIRMED = "user_confirmed"
    VERIFIED = "verified"

class SkillLevel(StrEnum):
    AWARENESS = "awareness"
    FOUNDATION = "foundation"
    PRACTITIONER = "practitioner"
    ADVANCED = "advanced"
    EXPERT = "expert"

class LanguageProficiency(StrEnum):
    BASIC = "basic"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    FLUENT = "fluent"
    NATIVE = "native"

class PublicationType(StrEnum):
    ARTICLE = "article"
    BLOG_POST = "blog_post"
    BOOK = "book"
    CONFERENCE_PAPER = "conference_paper"
    COURSE = "course"
    PRESENTATION = "presentation"
    VIDEO = "video"
    OTHER = "other"
