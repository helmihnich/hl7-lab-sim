# Mirth track (parallel to weeks 3-7)

Goal: learn a real interface engine, then show on GitHub that you can use both your own code and an industry tool.

## Which engine?
Mirth Connect changed licensing in recent versions (newer releases are commercial, and community forks such as Open Integration Engine exist). Check the current licence and download page yourself before you pick, and use an open-source version for your public repo. Pin the exact image/version in your `docker-compose.yml`.

## Step A (after week 3): connect to Mirth
1. Run the engine in Docker (compose file in `deploy/`). Expose the admin port and one MLLP port.
2. Create a channel: **TCP Listener (MLLP) source -> destination that writes the message to a file**.
3. Send your simulator's A01 to it with your MLLP client. Confirm Mirth's auto-ACK matches what your `ack.py` would produce. Compare the two ACKs field by field and write the differences in `lessons/mirth-notes.md`.

## Step B (after week 4): transformers
1. Add a JavaScript transformer that maps PID fields to a simple JSON object.
2. Add a filter: only ADT^A01 and ADT^A08 pass.
3. Use a code-set map to translate a local lab code to LOINC.
4. Reproduce the same transformation in your Python `transform_fhir.py`. Which was faster to write, and which is easier to test?

## Step C (after week 5): errors and reliability
1. Send your "chaos" messages. Find where Mirth shows errors (dashboard, message browser, error tab).
2. Configure queueing and retry on a destination. Stop the destination and watch messages queue up.
3. Export the channel as XML and commit it to `mirth/channels/`. A channel in git is a strong portfolio item.

## Step D (week 6-7): the full flow
Simulator -> Mirth channel (validate, route, transform) -> your FHIR sink or your engine.
Document the architecture in the README with a Mermaid diagram.

## Checkpoint questions
1. What does Mirth do at each stage of a channel: source, filter, transformer, destination, response?
2. What does Mirth give you that your engine lacks, and the reverse?
3. Why is it bad practice to put business logic only in a transformer nobody tests?
4. How would you deploy channel changes safely across dev, test and prod?
