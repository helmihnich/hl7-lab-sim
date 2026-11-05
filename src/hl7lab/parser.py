# WEEK 2 - PARSER (no HL7 libraries allowed here)
#
# TODO 1: Define a custom exception hierarchy (e.g. HL7Error -> HL7ParseError).
#         Parsing garbage must raise these, never IndexError/AttributeError.
#
# TODO 2: Normalize line endings on input. Real feeds send \r, files often have \n or \r\n.
#         Decide: accept all, but always emit \r on output.
#
# TODO 3: Read the delimiters from MSH (MSH-1 = field sep, MSH-2 = component, repetition, escape, subcomponent).
#         Store them on the message object. Never hard-code '|' or '^' elsewhere.
#
# TODO 4: Model the structure: Message -> Segments -> Fields -> Repetitions -> Components -> Subcomponents.
#         Think about whether to parse lazily (keep raw string, parse on access) or eagerly. Pick one and justify in a comment.
#
# TODO 5: Handle the MSH special case: MSH-1 is the separator itself, so field numbering is shifted for this segment only.
#
# TODO 6: Implement path access: get("PID-5-1"), get("OBX[2]-5"), get("PID-3[2]-4").
#         Missing things return a default (empty string / None), they do not crash.
#
# TODO 7: Implement set(path, value) so that you can modify a parsed message.
#
# TODO 8: Implement escape / unescape for \F\ \S\ \T\ \R\ \E\ using the delimiters declared in MSH (not hard-coded).
#         Hex escapes \Xhh..\ are a stretch goal.
#
# TODO 9: to_string(): must produce a byte-identical message for untouched input (round trip).
#
# TODO 10: Iterate segments by ID: message.segments("OBX") returns all OBX in order.
#          Preserve unknown/Z-segments as-is.
