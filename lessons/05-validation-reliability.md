# Week 5: Validation and reliability (what separates juniors from seniors)

## Theory
- **Conformance profile:** per message type: required/optional/not-used (R/O/X), cardinality, data types, value sets (HL7 tables).
- Three validation layers: syntax (delimiters, structure), semantic (types, tables, dates), business (e.g. discharge after admit).
- **Idempotency:** duplicate MSH-10 must not create duplicates. **Ordering:** A08 arriving before A01.
- Error strategy: reject vs repair vs quarantine. Dead-letter queue. Alerting.
- PHI: logs must not leak names and IDs. Know why.

## Tasks (`validator.py`, `tests/test_validator.py`)
1. A rules file (YAML) defining a profile for ADT_A01 and ORU_R01, loaded at runtime. No hard-coded rules.
2. Validator returns a list of issues with location (e.g. `PID-7`), severity, code. These feed the ERR segment from week 3.
3. Duplicate detection store (SQLite) keyed on sending app + MSH-10.
4. Out-of-order handling policy, documented in `docs/decisions/` as an ADR (architecture decision record).
5. A log-redaction filter for PHI.
6. Run the "bad messages" from week 4. Every failure must produce a precise NACK.

## Checkpoint questions
1. Should the engine reject a message with an unknown Z-segment? Defend your answer.
2. Duplicate message with *different* content, same MSH-10. What do you do?
3. Where is validating too strict harmful in practice?
4. What is the difference between a validation error and a transport error?
