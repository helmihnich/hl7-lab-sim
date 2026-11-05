# HL7 v2 Mastery Roadmap: `hl7-lab-sim`

**Flagship project:** a Lab/ADT simulator. Mock systems (EHR, LIS, RIS) exchange realistic HL7 v2 traffic over MLLP. An integration engine in the middle validates, routes, transforms and ACKs it.

```
 [EHR sim] --ADT/ORM--> |            | --ORM--> [LIS sim]
                        |  ENGINE    |
 [LIS sim] --ORU------> | (your code)| --ORU--> [EHR sim]
                        |            | --FHIR--> [file / mock API]
```

## How we work
1. Read the lesson `.md` in `lessons/`.
2. Do the tasks in the matching `src/hl7lab/*.py` and `tests/*.py`. They contain **comments only**.
3. Write the tests first, then the code. Make them pass.
4. Commit once per task with a clear message (this gives you a good git history).
5. Send me your code and I review it like a senior integration engineer would.

**Hard rules:** use synthetic data only (never real PHI), and no HL7 library until week 2 is done. You parse by hand first, then compare with `hl7apy` / `python-hl7`.

## Timeline (6-10 h/week)
| Week | Theme | Deliverable |
|------|-------|-------------|
| 1 | Anatomy & reading | You can decode any message by eye; `samples/` annotated |
| 2 | Parser & builder | `parser.py`, `builder.py` + tests, round-trip safe |
| 3 | MLLP & ACK | TCP server/client, ACK/NACK, enhanced ack mode |
| 4 | Message types & generator | Realistic ADT/ORM/ORU traffic generator |
| 5 | Validation & reliability | Validator, duplicate detection, error handling |
| 6 | Routing & transformation | Router, mapping, ADT -> FHIR Patient/Encounter |
| 7 | Ship it | Docker, CI, docs, demo, README that sells you |

## Skills you can put on your CV after this
HL7 v2.x structure and data types, MLLP, ACK/NACK semantics, ADT/ORM/ORU workflows, conformance validation, interface error handling, Z-segments, HL7 v2 -> FHIR mapping, testing integration interfaces.

## Questions I will ask you along the way
Each lesson ends with "Checkpoint questions". Answer them in `lessons/answers.md`. I mark them.
