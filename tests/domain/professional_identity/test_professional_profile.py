from uuid import uuid4
import pytest
from packages.domain.professional_identity import ContactInformation, DateRange, DomainValidationError, Experience, LocalizedText, PersonName, ProfessionalProfile, Skill

def test_create_minimal_professional_profile() -> None:
    profile = ProfessionalProfile(profile_id=uuid4(), schema_version="1.0", name=PersonName(full_name="Sample Professional"))
    assert profile.schema_version == "1.0"

def test_create_profile_with_experience_and_skill() -> None:
    profile = ProfessionalProfile(
        profile_id=uuid4(), schema_version="1.0", name=PersonName(full_name="Sample Professional"),
        contact=ContactInformation(email="sample@example.org", country_code="BR"),
        experiences=(Experience(experience_id=uuid4(), organization="Example Organization", role=LocalizedText({"en": "BI Analyst"}), period=DateRange(start_year=2020, is_current=True)),),
        skills=(Skill(skill_id=uuid4(), name="Power BI"),),
    )
    assert len(profile.experiences) == 1
    assert profile.skills[0].name == "Power BI"

def test_reject_duplicate_entity_identifiers() -> None:
    duplicate_id = uuid4()
    with pytest.raises(DomainValidationError, match="unique"):
        ProfessionalProfile(profile_id=uuid4(), schema_version="1.0", name=PersonName(full_name="Sample Professional"), skills=(Skill(skill_id=duplicate_id, name="Power BI"), Skill(skill_id=duplicate_id, name="SQL Server")))
