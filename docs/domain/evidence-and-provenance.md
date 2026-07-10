# Evidence and Provenance Domain

## Purpose

The Evidence bounded context records why a professional claim can be trusted, where it came from, how it entered CareerOS and how it was transformed.

## Key concepts

- **Evidence**: record supporting one or more professional claims.
- **Source**: original location or origin.
- **Provenance**: collection, transformation and verification history.
- **Verification**: how the source was validated.
- **Confidence**: confidence in the current interpretation.
- **Consent**: user authorization and visibility.

## Aggregate root

`Evidence` is the aggregate root. It stores metadata and references, never binary document content.

## Relationship with Professional Identity

Professional Identity keeps lightweight `EvidenceReference` values. The complete record is resolved by `evidence_id`; the two bounded contexts remain decoupled.

## Invariants

- confidence is between 0 and 1;
- rejected evidence has zero confidence;
- evidence cannot supersede itself;
- duplicate claim references are not allowed;
- granted consent requires a timestamp;
- corrections create a new record using `supersedes_evidence_id`.

## Privacy and security

`content_reference` points to protected storage. Imported content is untrusted input. Authorization, encryption, malware scanning and parsing belong outside the domain.
