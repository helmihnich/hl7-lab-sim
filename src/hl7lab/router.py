# WEEK 6 - ENGINE: ROUTING, QUEUE, RETRY
#
# TODO 1: Pipeline: receive -> persist -> validate -> route -> transform -> deliver -> mark done. ACK only after persist.
#
# TODO 2: Routing table (YAML): conditions on MSH-9, MSH-3/4, PV1-2, etc. -> list of destinations (MLLP host:port, file, FHIR sink).
#
# TODO 3: Persistent queue (SQLite) with states: received, queued, delivered, failed, dead. Survives a crash.
#
# TODO 4: Retry with exponential backoff + jitter; after N attempts move to the dead-letter state.
#
# TODO 5: CLI commands: list dead messages, show one, replay one (idempotently).
#
# TODO 6: Metrics counters (received/acked/rejected/retried/dead) exposed via CLI or a tiny HTTP endpoint.
