#!/usr/bin/env python3
"""Check reviewed capsule integrity. Does not execute arbitrary capsule commands."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from observational_succ.source_proof_certificate import audit_capsules


if __name__ == "__main__":
    capsules = json.loads((ROOT / "research/2026-10-15/PROOF_TEETH_CAPSULES.json").read_text())
    print(json.dumps(audit_capsules(capsules, ROOT), indent=2, sort_keys=True))
