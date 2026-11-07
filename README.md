# Digital Forensics Portfolio Project

> Educational demonstration using **synthetic evidence only**. No real person's data is included. Results require analyst validation and should not be treated as proof of wrongdoing.

## Skills demonstrated
Windows Security Event IDs 4624/4625, CSV event parsing, UTC timeline construction, simple login anomaly triage, Python unit tests.

## Run (Python 3.9+; standard library only)
```bash
python login_timeline.py samples/security_events.csv --output timeline.json
python -m unittest discover -s tests -v
```

## Evidence handling
All example files are fictional. Preserve originals, verify hashes, document timestamps/time zones, and maintain a chain of custody before using any process in a real investigation.

## Limitations
Accepts a **simplified CSV export**, not native .evtx files. Count-based heuristic has no time window or exclusions; investigate legitimate causes of failed logins before making conclusions.

## Suggested next steps
Add screenshots from your own run, a sample investigator report, and a brief explanation of what you learned. Only list forensic tools you have personally operated.
