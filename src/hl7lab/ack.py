# WEEK 3 - ACK / NACK GENERATION
#
# TODO 1: make_ack(incoming, code, errors=None): returns an ACK message built with your builder.
#         - MSH: swap sending/receiving app+facility, MSH-9 = ACK^<trigger>^ACK, new MSH-10, same version as incoming.
#         - MSA-1 = code (AA/AE/AR), MSA-2 = incoming MSH-10, MSA-3 = optional text.
#
# TODO 2: Add ERR segments for each error: location (ERR-2), error code (ERR-3), severity (ERR-4), text.
#
# TODO 3: Enhanced mode: look at incoming MSH-15/16 and decide whether to answer with CA/CE/CR or AA/AE/AR (or both stages).
#
# TODO 4: If the incoming message is so broken you cannot read its control ID, what do you send?
#         Document the decision in a comment and test it.
