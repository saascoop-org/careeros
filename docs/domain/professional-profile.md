# Professional Profile Domain

## Purpose

The `ProfessionalProfile` aggregate is the reusable representation of a person's professional identity inside CareerOS. It remains independent from résumé templates, opportunity matching, persistence, APIs and AI providers.

## Aggregate contents

- schema version and stable profile identifier;
- professional name and optional contact information;
- multilingual summaries;
- experiences, projects and skills;
- certifications, education and languages;
- publications and evidence references.

## Core invariants

- entity identifiers are unique inside the aggregate;
- sensitive contact fields are optional;
- multilingual text declares a default language;
- current date ranges cannot have an end date;
- incomplete dates are allowed;
- professional records can reference evidence identifiers.

## Evidence boundary

This aggregate stores only `EvidenceReference` values. Complete source metadata, verification history and provenance belong to the Evidence bounded context planned in issue `#4`.

## Compatibility

The initial schema version is `1.0`. Breaking changes require a new major schema version and documented migration guidance.

## Privacy

The model does not require home address, national identification numbers, date of birth, photo, marital status or demographic information.
