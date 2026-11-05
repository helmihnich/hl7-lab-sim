# WEEK 3 - TESTS
#
# test 1: decoder yields one message from one complete frame.
# test 2: feed the same frame one byte at a time - still exactly one message.
# test 3: two frames in one chunk - two messages.
# test 4: junk bytes before the start byte are discarded.
# test 5: frame larger than the limit is rejected without exhausting memory.
# test 6: server + client integration on localhost with an ephemeral port: send A01, receive AA with MSA-2 == sent MSH-10.
# test 7: malformed message -> AE/AR with an ERR segment.
# test 8: client retries after a timeout, and the server does not process the duplicate twice (needs week 5 duplicate store; mark xfail until then).
# test 9: 20 concurrent clients all get correct, matching ACKs.
