#!/usr/bin/env bash
set -euo pipefail
research_dir="research/2026-11-15/gamma_phase_disintegration"
export PYTHONPATH="$PWD${PYTHONPATH:+:$PYTHONPATH}"
python -W error -m unittest discover -s "$research_dir" -p 'test_*.py' -v
python "$research_dir/audit_forcing.py"
python "$research_dir/audit_modes.py" --output /tmp/succ_gamma_mode_audit_replay.json
python "$research_dir/audit_resonance.py"
python "$research_dir/audit_tilt_hierarchy.py"
python "$research_dir/make_figure.py"
python -m compileall -q "$research_dir"
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
