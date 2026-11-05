# Week 2: Build your own parser and builder

## Theory
- Parsing must respect the **delimiters declared in MSH**, not hard-coded ones.
- Addressing notation: `PID-5-1`, `OBX[2]-5`, `PID-3[2]-1`. Your API should support a path like this.
- Round trip: `parse(msg).to_string() == msg` for every sample. This is your first big quality test.
- Handle: repeated segments, empty trailing fields, missing segments, unknown Z-segments, escape sequences (`\F\`, `\S\`, `\T\`, `\R\`, `\E\`, `\X..\`).

## Tasks (implement in `src/hl7lab/parser.py` and `builder.py`)
Follow the comments in those files. Then in `tests/test_parser.py`:
1. Round trip on every file in `samples/`.
2. Path access with repeats and defaults for missing values.
3. Escape and unescape.
4. Messages with non-default delimiters.
5. Garbage input raises a clear custom exception (never a bare `IndexError`).

## Stretch
- Install `hl7apy` and `python-hl7`. Write a test that compares your parse result against both. Write down 3 differences in `lessons/week2-notes.md`.
- Add a CLI: `python -m hl7lab pretty samples/adt_a01.hl7` prints segments in a readable table.

## Checkpoint questions
1. Why is `split("|")` on the whole message wrong for MSH?
2. How would you represent "field present but empty" vs "field absent"?
3. What should the parser do if a segment ID is lowercase?
4. When is it right to be strict, and when lenient? (Postel's law and its limits in healthcare.)
