# AI Governance

## Role of AI

AI may assist with:

- extracting structured requirements;
- ranking relevant evidence;
- suggesting concise wording;
- translating approved content;
- identifying omissions or inconsistencies.

AI may not:

- invent evidence;
- claim a certification that is not recorded;
- inflate seniority;
- submit an application without user approval;
- make hidden decisions that cannot be reviewed.

## Human approval

All externally used outputs require explicit user review.

## Provider abstraction

Model access must be implemented behind an application port.

Example:

```python
class LanguageModelPort(Protocol):
    def generate_structured(self, request: StructuredPrompt) -> StructuredResponse:
        ...
```

## Evaluation

AI-assisted features should be evaluated for:

- factual consistency;
- evidence coverage;
- omission risk;
- unsupported claims;
- language quality;
- reproducibility;
- cost and latency;
- bias across career backgrounds.
