# WEEK 2 - WRITE THESE TESTS FIRST (pytest)
#
# test 1: round trip - for every file in samples/, parse then to_string equals the original (after normalizing line endings to \r).
# test 2: get("PID-5-1") == "DOE" for adt_a01.hl7; get("PID-3[2]-1") is the national ID.
# test 3: repeated segments - OBX[1] and OBX[2] in oru_r01.hl7 return different values.
# test 4: missing field/segment returns the default and does not raise.
# test 5: MSH special numbering - get("MSH-2") == "^~\\&", get("MSH-9-2") == "A01".
# test 6: non-default delimiters (e.g. '#' as field separator) parse correctly.
# test 7: escape/unescape round trip for text containing | ^ ~ \ &
# test 8: garbage input ("hello", empty string, binary) raises your HL7ParseError.
# test 9: set() then to_string() changes exactly the intended field.
# test 10: Z-segments survive a round trip untouched.
