import pytest
from packages.domain.professional_identity import ContactInformation, DateRange, DomainValidationError, LocalizedText

def test_localized_text_uses_default_language() -> None:
    text = LocalizedText(values={"en": "Data professional", "pt-BR": "Profissional de dados"}, default_language="pt-BR")
    assert text.get() == "Profissional de dados"

def test_localized_text_requires_default_language() -> None:
    with pytest.raises(DomainValidationError, match="default_language"):
        LocalizedText(values={"en": "Data professional"}, default_language="pt-BR")

def test_date_range_accepts_incomplete_dates() -> None:
    period = DateRange(start_year=2012, start_month=12, is_current=True)
    assert period.start_day is None

def test_current_date_range_rejects_end_date() -> None:
    with pytest.raises(DomainValidationError, match="Current"):
        DateRange(start_year=2020, end_year=2024, is_current=True)

def test_contact_information_rejects_invalid_country_code() -> None:
    with pytest.raises(DomainValidationError, match="country_code"):
        ContactInformation(country_code="BRA")
