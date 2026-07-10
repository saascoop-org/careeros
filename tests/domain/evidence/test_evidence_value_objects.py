"""Tests for Evidence value objects."""

from datetime import UTC, datetime
from uuid import uuid4

import pytest

from packages.domain.evidence import (
    ClaimReference,
    ConfidenceScore,
    Consent,
    ContentFingerprint,
    EvidenceSource,
    EvidenceSourceType,
    EvidenceValidationError,
    EvidenceVisibility,
    TransformationRecord,
    TransformationType,
)


@pytest.mark.parametrize("value", [-0.01, 1.01])
def test_confidence_rejects_out_of_range(value: float) -> None:
    with pytest.raises(EvidenceValidationError):
        ConfidenceScore(value)


def test_fingerprint_rejects_algorithm() -> None:
    with pytest.raises(EvidenceValidationError):
        ContentFingerprint("md5", "0" * 32)


def test_consent_requires_date() -> None:
    with pytest.raises(EvidenceValidationError):
        Consent(
            True,
            EvidenceVisibility.PRIVATE,
            "Resume",
        )


def test_source_rejects_blank_label() -> None:
    with pytest.raises(EvidenceValidationError):
        EvidenceSource(
            EvidenceSourceType.DOCUMENT,
            " ",
        )


def test_claim_rejects_blank_entity_type() -> None:
    with pytest.raises(EvidenceValidationError):
        ClaimReference(
            uuid4(),
            " ",
        )


def test_transformation_normalizes_metadata() -> None:
    transformation = TransformationRecord(
        transformation_type=TransformationType.EXTRACTED,
        performed_at=datetime.now(UTC),
        performed_by=" careeeros-document-parser ",
        metadata={" parser_version ": " 0.1.0 "},
    )

    assert transformation.performed_by == "careeeros-document-parser"
    assert transformation.metadata == {"parser_version": "0.1.0"}
