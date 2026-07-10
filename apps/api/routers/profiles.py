from fastapi import APIRouter
from pydantic import BaseModel

from packages.application.use_cases.create_professional_profile import CreateProfessionalProfile
from packages.domain.entities.professional_profile import ProfessionalProfile

router = APIRouter(prefix="/profiles", tags=["profiles"])


class CreateProfileRequest(BaseModel):
    full_name: str
    headline: str | None = None
    primary_language: str = "en"


@router.post("")
def create_profile(request: CreateProfileRequest) -> ProfessionalProfile:
    use_case = CreateProfessionalProfile()
    return use_case.execute(
        full_name=request.full_name,
        headline=request.headline,
        primary_language=request.primary_language,
    )
