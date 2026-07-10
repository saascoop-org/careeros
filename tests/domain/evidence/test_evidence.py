from datetime import UTC, datetime
from uuid import uuid4
import pytest
from packages.domain.evidence import ClaimReference, CollectionMethod, ConfidenceScore, Consent, Evidence, EvidenceSource, EvidenceSourceType, EvidenceValidationError, EvidenceVisibility, VerificationStatus

def _consent():
    return Consent(True, EvidenceVisibility.PRIVATE, "Resume generation", datetime.now(UTC))

def test_create_valid_evidence():
    evidence=Evidence(uuid4(),"1.0",EvidenceSource(EvidenceSourceType.EMPLOYMENT_RECORD,"Employment record"),CollectionMethod.MANUAL,datetime.now(UTC),VerificationStatus.USER_CONFIRMED,ConfidenceScore(0.8),_consent())
    assert evidence.confidence.value==0.8

def test_rejected_evidence_requires_zero_confidence():
    with pytest.raises(EvidenceValidationError, match="zero confidence"):
        Evidence(uuid4(),"1.0",EvidenceSource(EvidenceSourceType.DOCUMENT,"Invalid document"),CollectionMethod.FILE_IMPORT,datetime.now(UTC),VerificationStatus.REJECTED,ConfidenceScore(0.5),Consent(False,EvidenceVisibility.PRIVATE))

def test_duplicate_claims_are_rejected():
    claim=ClaimReference(uuid4(),"experience","achievements[0]")
    with pytest.raises(EvidenceValidationError, match="duplicate"):
        Evidence(uuid4(),"1.0",EvidenceSource(EvidenceSourceType.USER_STATEMENT,"Statement"),CollectionMethod.USER_CONFIRMATION,datetime.now(UTC),VerificationStatus.USER_CONFIRMED,ConfidenceScore(0.7),_consent(),claims=(claim,claim))

def test_evidence_cannot_supersede_itself():
    eid=uuid4()
    with pytest.raises(EvidenceValidationError, match="supersede itself"):
        Evidence(eid,"1.0",EvidenceSource(EvidenceSourceType.DOCUMENT,"Document"),CollectionMethod.FILE_IMPORT,datetime.now(UTC),VerificationStatus.UNVERIFIED,ConfidenceScore(0.4),_consent(),supersedes_evidence_id=eid)
