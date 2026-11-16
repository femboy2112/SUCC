#!/bin/sh
set -eu
cd "$(dirname "$0")"
python -W error -m unittest discover -s . -p 'test_pi_slot_probe.py' -v
python independent_audit.py
python -m compileall -q pi_slot_probe.py test_pi_slot_probe.py independent_audit.py
python -m json.tool CLAIM_LEDGER.json > /dev/null
python -m json.tool FINITE_REPORT.json > /dev/null
