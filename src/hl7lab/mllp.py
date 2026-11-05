# WEEK 3 - MLLP TRANSPORT (use asyncio or threading; justify the choice in a comment)
#
# TODO 1: Constants for the framing bytes: start 0x0B, end 0x1C then 0x0D.
#
# TODO 2: A frame decoder class that is fed arbitrary byte chunks and yields complete messages.
#         It must handle: split frames, several frames in one chunk, junk before the start byte, oversized frames (limit!).
#
# TODO 3: A server: listens on a port, one handler per connection, passes each decoded message to a callback,
#         sends back whatever the callback returns (the ACK) framed correctly.
#
# TODO 4: A client: connect, send a framed message, wait for ACK with a timeout, retry N times with backoff.
#         Decide and document: what do you do when the connection drops after sending but before the ACK?
#
# TODO 5: Structured logging with the control ID in every line. No patient data in logs.
#
# TODO 6: Graceful shutdown: finish in-flight messages, close sockets cleanly.
#
# TODO 7 (stretch): optional TLS using the ssl module with a self-signed cert for the demo.
