# WEEK 5 - VALIDATION
#
# TODO 1: Profile file format (YAML): for each message type, list segments with usage (R/O/X) and cardinality,
#         and per field: required?, data type, max length, allowed table values.
#
# TODO 2: Validator: parse -> check structure -> check fields -> check business rules. Collect ALL issues, not just the first.
#
# TODO 3: Issue object: location (e.g. 'PID-7'), severity (error/warning), code, message. Convert to ERR segments.
#
# TODO 4: Data type checks: TS/DTM formats, NM numeric, ID/IS against tables, CX/XPN structure.
#
# TODO 5: Business rules: discharge not before admit, A11 refers to an existing A01, OBX units present for NM, etc.
#
# TODO 6: Duplicate detection (SQLite): key = sending app + facility + MSH-10. Decide what happens on exact vs different duplicate.
#
# TODO 7: PHI-safe logging filter that masks names, IDs, DOB, addresses.
