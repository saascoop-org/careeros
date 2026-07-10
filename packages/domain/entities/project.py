from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str] = Field(default_factory=list)
    outcomes: list[str] = Field(default_factory=list)
    evidence_urls: list[str] = Field(default_factory=list)
