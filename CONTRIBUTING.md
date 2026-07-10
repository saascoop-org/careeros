# Contributing to CareerOS

Thank you for considering a contribution.

## Contribution principles

- Prefer small, reviewable pull requests.
- Document architectural decisions using ADRs.
- Protect user privacy by default.
- Avoid committing personal data, API keys or scraped private content.
- Add tests for new behavior.

## Local checks

```bash
ruff check .
mypy apps packages
pytest
```
