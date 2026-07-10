from typing import Protocol

from packages.domain.entities.professional_profile import ProfessionalProfile


class ProfileRepository(Protocol):
    def save(self, profile: ProfessionalProfile) -> ProfessionalProfile:
        ...
