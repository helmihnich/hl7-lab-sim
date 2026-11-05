# WEEK 2 - MESSAGE BUILDER
#
# TODO 1: A fluent or declarative way to build a message: start with MSH, add segments, set fields by path.
#         Auto-fill MSH-7 (timestamp), MSH-10 (unique control ID), MSH-12 (version) unless provided.
#
# TODO 2: Helpers for composite types so callers do not hand-concatenate strings:
#         xpn(family, given, middle), cx(id, authority, id_type), xad(...), ts(datetime) -> 'YYYYMMDDHHMMSS'.
#
# TODO 3: Escape user-provided text automatically (a patient called "O'Brien & Sons | Ltd" must not break the message).
#
# TODO 4: Build the two samples in samples/ programmatically and assert they match the files (modulo timestamp/control ID).
