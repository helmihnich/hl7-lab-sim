# WEEK 6 - HL7 v2 -> FHIR TRANSFORMATION
#
# TODO 1: ADT -> Patient: map PID-3 to identifier (system from CX.4), PID-5 to name, PID-7 birthDate, PID-8 gender
#         (translate F/M/O/U to FHIR codes), PID-11 address, PID-13 telecom.
#
# TODO 2: ADT -> Encounter: PV1-2 class, PV1-3 location, PV1-7 participant, PV1-19 identifier, PV1-44/45 period, status from trigger event.
#
# TODO 3: ORU -> DiagnosticReport + Observation(s): OBX-3 code, OBX-5 value (by OBX-2 type), OBX-6 unit, OBX-7 range, OBX-8 interpretation.
#
# TODO 4: Output a FHIR Bundle (type 'transaction'). Use deterministic IDs so replays do not create duplicates (conditional create / PUT).
#
# TODO 5: Code translation from a CSV table. Policy for unmapped codes: keep original with text, never silently drop. Document it.
#
# TODO 6: Convert HL7 timestamps to ISO 8601 and handle partial dates (YYYY, YYYYMM) and timezone offsets.
