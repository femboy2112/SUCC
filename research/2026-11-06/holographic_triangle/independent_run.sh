#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")"
python -m compileall -q hologram.py test_hologram.py independent_oracle.py linear_depth_probe.py test_linear_depth.py
python -m unittest discover -v -s . -p 'test_*.py' > LOCAL_TEST_STDOUT.txt 2> LOCAL_TEST_STDERR.txt
python independent_oracle.py > INDEPENDENT_ORACLE_RAW.json
python linear_depth_probe.py > LINEAR_DEPTH_RAW.json
python receipt.py > FINITE_RECEIPT.json
python receipt.py --verify
