# Week 4: Real workflows and the traffic generator

## Theory
- **ADT (patient administration):** A01 admit, A02 transfer, A03 discharge, A04 register, A08 update, A11 cancel admit, A13 cancel discharge, A40 merge patient. Know the *sequence* in a real hospital stay.
- **ORM^O01 / OML^O21:** orders. **ORU^R01:** results. **SIU:** scheduling. **MDM:** documents. **VXU:** immunization.
- Segments to master: `PID, PV1, PV2, NK1, IN1, AL1, DG1, ORC, OBR, OBX, NTE, EVN, MRG`.
- OBX value types: NM, ST, CWE, TX, ED/RP (attachments). Result status (OBX-11): F, P, C.
- **Z-segments:** local extensions. When are they acceptable and what is the risk?
- Cancel and update semantics: A11 must reference an earlier A01. State matters.

## Tasks (`generator.py`, `tests/test_generator.py`)
1. Build a patient/encounter state machine (registered -> admitted -> transferred -> discharged).
2. Each state change emits the correct trigger event with consistent IDs.
3. Lab flow: ORM order -> LIS sim -> ORU result (with a realistic panel, units, ranges, flags H/L/A).
4. Use `faker` with a fixed seed for reproducible fake patients. Add deliberate "bad" messages (missing PID-3, wrong version, bad date) behind a flag for week 5.
5. A scenario file (YAML/JSON) describing a day in the hospital that the generator replays.

## Checkpoint questions
1. What happens downstream if you send an A03 for a patient never admitted?
2. A08 vs A01: when is each right?
3. How does a merge (A40) change which identifier survives?
4. Why do labs use OBR-4 / OBX-3 codes (LOINC) instead of free text?
