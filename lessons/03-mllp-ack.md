# Week 3: MLLP and acknowledgments

## Theory
- **MLLP framing:** `<VT 0x0B>` + message + `<FS 0x1C><CR 0x0D>`. TCP is a stream, so one `recv()` is not one message. You must buffer and find the frame.
- **Original mode ACK:** `MSA-1` = `AA` (accept), `AE` (error), `AR` (reject). `MSA-2` = control ID of the message you are acknowledging.
- **Enhanced mode:** `CA/CE/CR` (commit) vs `AA/AE/AR` (application). Driven by MSH-15/16.
- `ERR` segment: location, error code, severity. Never ACK `AA` before you have safely stored the message.
- ACK `MSH-9` is `ACK^A01^ACK` and you swap sender and receiver.

## Tasks (`mllp.py`, `ack.py`, `tests/test_mllp.py`)
Follow the comments. Required behaviors:
1. Server that handles multiple concurrent clients.
2. Correct framing across split and coalesced TCP chunks (test by sending bytes one at a time).
3. ACK generation from an incoming message, plus NACK with ERR for a malformed one.
4. Client with timeout and retry. What does the sender do if no ACK arrives?
5. Graceful shutdown and logging with the message control ID in every log line.

## Checkpoint questions
1. A sender gets no ACK. Do they resend? What problem does that create, and how do you solve it (hint: MSH-10)?
2. Difference between `AE` and `AR`? Give a real example of each.
3. Why must framing logic be tested with fragmented input?
4. Where does TLS fit with MLLP?
