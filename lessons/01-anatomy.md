# Week 1: Anatomy of an HL7 v2 message

## Theory
- A message is a set of **segments**, one per line, separated by `\r` (carriage return, 0x0D). This is not `\n`, and the difference matters.
- Segment = 3-letter ID + fields separated by `|`.
- Field -> repetitions (`~`) -> components (`^`) -> subcomponents (`&`). Escape char is `\`. Declared in **MSH-1 and MSH-2**: `|` and `^~\&`.
- **MSH numbering trap:** MSH-1 *is* the `|` itself, so `MSH-2` is `^~\&` and the first "real" field is MSH-3. Other segments do not do this.
- Key MSH fields: sending app/facility (3,4), receiving (5,6), datetime (7), **message type (9)** e.g. `ADT^A01^ADT_A01`, **control ID (10)**, processing ID (11: P/T/D), **version (12)**.
- Common data types: ST, NM, DT, TS/DTM, ID, IS, CE/CWE, CX (patient IDs), XPN (names), XAD (addresses), XTN (phones), EI, HD.
- Empty vs null: `||` means "not present", `|""|` means "delete this value". Know the difference.

## Practice
Open the files in `samples/`. For each message, in a new file `lessons/week1-notes.md`:
- Draw a table: segment, field number, field name, value, data type.
- Find the patient ID, name, DOB, sex, visit number, location and attending doctor.
- Spot the repetitions and components.

## Tasks (no code yet)
1. Annotate `samples/adt_a01.hl7` fully.
2. Annotate `samples/oru_r01.hl7`. Where is the result value, unit, reference range and abnormal flag?
3. Hand-write an `ADT^A03` (discharge) from the A01 by changing only what must change.
4. Read the HL7 v2.5.1 spec chapter 2 (control) and chapter 3 (ADT). Write 10 bullet points.

## Checkpoint questions (put answers in `lessons/answers.md`)
1. Why is the message terminator `\r`, and what breaks if a file uses `\n`?
2. In `PID|1||123^^^HOSP^MR||DOE^JOHN`, which field is the identifier list and what are its components?
3. What is the difference between `~` and `^`?
4. How does a receiver know which version it is reading?
5. What does MSH-11 = `T` imply for a production system?
