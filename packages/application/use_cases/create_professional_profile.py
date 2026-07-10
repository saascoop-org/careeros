from packages.domain.entities.professional_profile import ProfessionalProfile


class CreateProfessionalProfile:
    def execute(
        self,
        full_name: str,
        headline: str | None = None,
        primary_language: str = "en",
    ) -> ProfessionalProfile:
        return ProfessionalProfile(
            full_name=full_name,
            headline=headline,
            primary_language=primary_language,
        )
