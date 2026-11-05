# Week 7: Make the GitHub shine

## Tasks
1. **README** with: one-line pitch, architecture diagram (Mermaid), quick start (`docker compose up`), demo GIF or terminal recording, supported message types table, design decisions, limitations.
2. **Docker + docker-compose:** engine, EHR sim, LIS sim, one command to run the whole hospital.
3. **CI (GitHub Actions):** lint (ruff), type-check (mypy), tests, coverage badge.
4. **Tests:** aim for >85% coverage, plus an end-to-end test that runs a full day scenario.
5. **Docs:** `docs/` with the segment cheat sheet, conformance profile guide, ADRs.
6. **Release:** tag `v1.0.0`, write release notes, pin repo, add topics: `hl7`, `hl7v2`, `healthcare`, `mllp`, `fhir`, `interoperability`.
7. **Security note:** a `SECURITY.md` stating synthetic data only, TLS option, PHI handling.
8. Write a short blog post or LinkedIn post: "What I learned building an HL7 v2 integration engine."

## Final exam (I will grill you)
- Walk me through what happens, byte by byte, from the EHR sending an A01 to the FHIR Patient appearing.
- I give you a broken production message. Diagnose it in 5 minutes.
- Explain your three most important design decisions and what you would change at scale.

## Interview-ready checklist
- [ ] Explain MLLP framing without notes
- [ ] Explain every field of MSH
- [ ] Explain AA/AE/AR and CA/CE/CR
- [ ] Describe an ADT hospital stay as a sequence of events
- [ ] Explain idempotency and ordering problems
- [ ] Map one v2 message to FHIR on a whiteboard
