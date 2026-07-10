from pydantic import BaseModel, Field


class ProfessionalProfile(BaseModel):
    """Canonical representation of a professional identity."""

    full_name: str
    headline: str | None = None
    primary_language: str = "en"
    skills: list[str] = Field(default_factory=list)
    source_refs: list[str] = Field(default_factory=list)
