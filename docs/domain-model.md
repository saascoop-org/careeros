# Domain Model

## Core aggregates

- ProfessionalProfile
- Experience
- Project
- Skill
- Certification
- Publication
- Repository
- CareerArtifact
- EvidenceSource
- CareerGoal

## Relationships

```mermaid
erDiagram
    ProfessionalProfile ||--o{ Experience : has
    ProfessionalProfile ||--o{ Project : owns
    ProfessionalProfile ||--o{ Skill : demonstrates
    Project ||--o{ Skill : uses
    Project ||--o{ EvidenceSource : proven_by
    Experience ||--o{ Project : includes
    CareerArtifact ||--o{ EvidenceSource : cites
```
