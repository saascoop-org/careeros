# Opportunity Domain

## Purpose

The Opportunity bounded context represents a professional objective that can be
analyzed and compared with a Professional Profile.

Examples include:

- employment opportunities;
- freelance contracts;
- consulting engagements;
- internships;
- volunteer roles;
- programs and fellowships.

The domain is designed around normalized business concepts rather than one
specific applicant tracking system or marketplace.

## Aggregate root

`Opportunity` is the aggregate root.

It contains:

- stable identifier;
- schema version;
- multilingual title and description;
- organization;
- lifecycle status;
- employment type;
- work model;
- seniority;
- locations and languages;
- responsibilities;
- normalized requirements;
- keywords;
- optional compensation;
- optional external source;
- publication and closing timestamps.

## Ubiquitous language

| Term | Meaning |
|---|---|
| Opportunity | Professional role, contract, program or engagement |
| Organization | Company, institution or client offering the opportunity |
| Requirement | Expected qualification, skill or constraint |
| Responsibility | Work or outcome expected from the professional |
| Keyword | Search or matching term explicitly associated with the opportunity |
| Work model | Remote, hybrid, onsite or flexible arrangement |
| External source | Platform or document where the opportunity originated |
| Compensation range | Optional monetary interval and payment period |

## Invariants

- schema version is mandatory;
- organization name is mandatory;
- requirement identifiers are unique;
- opportunity keywords are unique;
- requirement keywords are unique;
- open opportunities contain at least one requirement or responsibility;
- closing time cannot precede publication time;
- compensation values cannot be negative;
- maximum compensation cannot be lower than minimum;
- currency uses a three-letter code;
- country uses a two-letter code.

## Interoperability strategy

External ATS and marketplace payloads must be mapped through adapters.

```text
External platform payload
          |
          v
Anti-corruption adapter
          |
          v
CareerOS Opportunity
```

The domain must not import vendor-specific fields or SDKs.

Unmapped source data can remain available in infrastructure-level raw records,
but it should not distort the core domain model.

## Multilingual content

Titles, descriptions, responsibilities and requirements use `LocalizedText`
from the Professional Identity shared domain vocabulary.

This enables one opportunity to preserve the original language and optional
user-approved translations.

## Privacy

Opportunity descriptions may contain client or recruiter information.

Private opportunity files and confidential messages must not be committed to
the public repository. Public examples must use synthetic or explicitly
approved data.
