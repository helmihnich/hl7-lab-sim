# WEEK 4 - ADT / LAB TRAFFIC GENERATOR
#
# TODO 1: Patient factory with a fixed random seed (faker). Synthetic data only. Realistic IDs, names, DOB, addresses.
#
# TODO 2: Encounter state machine: REGISTERED -> ADMITTED -> TRANSFERRED* -> DISCHARGED, plus cancel paths (A11, A13).
#         Illegal transitions must be impossible (or deliberately produced in 'chaos' mode).
#
# TODO 3: Each transition emits the right ADT trigger (A04/A01/A02/A03/A11/A13/A08/A40) with consistent
#         PID/PV1 data. PV1-19 visit number stays the same for the whole encounter.
#
# TODO 4: Lab flow: from an admitted patient, create an ORM/OML order, then later an ORU with a realistic panel.
#         Use real LOINC codes, units, reference ranges, abnormal flags.
#
# TODO 5: Scenario runner: reads a YAML scenario ("08:00 admit 5 patients, 08:30 order CBC for each...") and replays it
#         at configurable speed, sending through your MLLP client.
#
# TODO 6: 'Chaos' flag: with some probability inject faults (missing PID-3, duplicate control ID, wrong version,
#         out-of-order events, bad dates). Needed for week 5.
