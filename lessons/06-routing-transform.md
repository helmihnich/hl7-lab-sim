# Week 6: Routing and transformation

## Theory
- Integration engine pattern: **receive -> persist -> validate -> route -> transform -> deliver -> ack/retry**.
- Routing by MSH-9, sending facility, patient class (PV1-2), or custom rules.
- Transformations: field mapping, code translation (local -> LOINC/SNOMED/ICD-10), date/timezone normalization, enrichment, Z-segment stripping.
- Delivery guarantees: at-least-once + idempotent receivers. Retry with backoff, dead-letter queue.
- **HL7 v2 -> FHIR:** ADT -> Patient + Encounter; ORU -> DiagnosticReport + Observation. Read the official v2-to-FHIR Implementation Guide mapping.

## Tasks (`router.py`, `transform_fhir.py`, tests)
1. Declarative routing table (YAML): conditions -> destinations.
2. A persistent queue (SQLite is fine) so messages survive a crash. Prove it with a kill test.
3. Retry with exponential backoff and a dead-letter table plus a CLI to inspect and replay.
4. A code-translation table (CSV) for local lab codes -> LOINC, with a policy for unmapped codes.
5. ADT^A01 -> FHIR `Patient` and `Encounter` bundle; ORU^R01 -> `DiagnosticReport` + `Observation`s. Validate the output against FHIR JSON structure.
6. Simple dashboard or CLI summary: messages received, ACKed, rejected, retried.

## Checkpoint questions
1. What is lost when mapping v2 -> FHIR, and what do you invent?
2. Why persist before ACKing?
3. How do you replay safely without causing duplicates?
4. How do you version your mapping rules?
