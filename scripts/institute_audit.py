#!/usr/bin/env python3
"""Audit the institute registry; this never executes registry-supplied commands."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from observational_succ.institute_audit import audit_registry

root = Path(__file__).resolve().parents[1]
registry = json.loads((root/"research/2026-10-18/institute/theorem_registry.json").read_text())
print(json.dumps(audit_registry(registry, root), indent=2))
