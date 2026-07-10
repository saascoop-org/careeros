# Security and Privacy Architecture

## Classification

CareerOS may process personal, professional and potentially sensitive information.

## Baseline controls

- local-first development for the MVP;
- secrets only through environment variables or secret managers;
- no credentials committed to Git;
- minimal data sent to external AI providers;
- user confirmation before external export;
- audit metadata for generated outputs;
- explicit retention and deletion policies;
- dependency scanning;
- protected default branch;
- reviewed pull requests.

## AI-specific controls

- prompts must exclude unnecessary personal data;
- model responses are untrusted input;
- generated claims must be validated against evidence;
- prompt and output logging must be configurable;
- private data must not be used for public examples without consent.

## Threats considered

- fabricated résumé claims;
- prompt injection from imported opportunity text;
- leakage of personal data;
- malicious document content;
- unauthorized modification of professional records;
- dependency compromise;
- insecure export files.
