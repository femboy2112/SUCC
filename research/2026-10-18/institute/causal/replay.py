#!/usr/bin/env python3
"""Replay bounded causal-stream checks and retain exact outputs/credentials."""
from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from observational_succ.institute_causal import (  # noqa: E402
    audit_public_transcript, audit_quotient, backward_exclusion_oracle,
    forward_history_oracle, refine_quotient, splice_counterexample,
    verify_history_certificate,
)


def encode(obj):
    if isinstance(obj, Fraction):
        return str(obj)
    if isinstance(obj, (set, frozenset)):
        return sorted(obj)
    raise TypeError(type(obj).__name__)


def bounded():
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))


def check(name, command, *, cap=False):
    started = datetime.now(timezone.utc).isoformat()
    before = time.monotonic()
    proc = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                          timeout=90, preexec_fn=bounded if cap else None)
    (HERE / f"{name}.stdout").write_text(proc.stdout)
    (HERE / f"{name}.stderr").write_text(proc.stderr)
    return {"name": name, "command": command, "cwd": str(ROOT),
            "started_utc": started, "elapsed_seconds": time.monotonic() - before,
            "returncode": proc.returncode,
            "stdout": f"{name}.stdout", "stderr": f"{name}.stderr",
            "address_space_limit_bytes": 1024**3 if cap else None}


def main():
    checks = [check("python_version", [sys.executable, "--version"]),
              check("lean_version", ["lean", "--version"]),
              check("focused_tests", [sys.executable, "-m", "unittest", "tests.test_institute_causal", "-v"]),
              check("causal_regression", [sys.executable, "-m", "unittest",
                    "tests.test_institute_causal", "tests.test_no_ghost", "tests.test_no_ghost_policy",
                    "tests.test_no_ghost_coherence", "tests.test_field_history_lift",
                    "tests.test_eodcs_causal_nerode", "-q"]),
              check("lean", ["lean", "formal/InstituteCausal.lean"], cap=True)]
    model, initial, transcript = splice_counterexample()
    dual = backward_exclusion_oracle(model, initial, transcript)
    quotient, failures = refine_quotient(model)
    fixture = {
        "source_id": model.source_id, "basis": model.basis,
        "source_states": model.states, "original": dict(model.original),
        "observation": dict(model.observation),
        "transitions": [{"before": s, "action": a, **asdict(e)}
                        for (s, a), e in model.transitions.items()],
        "initial": initial, "transcript": [asdict(r) for r in transcript],
        "forward": asdict(forward_history_oracle(model, initial, transcript)),
        "exclusion_certificate": asdict(dual),
        "certificate_verified": verify_history_certificate(model, initial, transcript, dual),
        "public_audit": asdict(audit_public_transcript(model, initial, transcript)),
        "public_report_quotient_audit": asdict(audit_quotient(model, model.observation)),
        "refined_quotient": dict(quotient), "refinement_counterexamples": failures,
        "model_only_not_physical_execution": True,
        "RH_proved": False,
    }
    (HERE / "splice_counterexample.json").write_text(json.dumps(fixture, indent=2, default=encode) + "\n")
    files = ["observational_succ/institute_causal.py", "tests/test_institute_causal.py",
             "formal/InstituteCausal.lean", "research/2026-10-18/INSTITUTE_CAUSAL_DESCENT.md",
             str(Path(__file__).resolve().relative_to(ROOT))]
    receipt = {
        "schema_version": 1,
        "base_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "branch": subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip(),
        "source_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files},
        "checks": checks,
        "passed": all(c["returncode"] == 0 for c in checks),
        "finite_enumeration_scope": {"primal_dual_cartesian_cases": 800, "quotient_cost_models": 81,
                                     "two_action_quotient_and_lift_models": 81},
        "novelty_status": "CLASSICAL_SPECIALIZATION_PROJECT_INTEGRATION",
        "independence_boundary": "Distinct algorithms share model specification and authoring session",
        "RH_proved": False,
    }
    (HERE / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"passed": receipt["passed"], "checks": [
        {"name": c["name"], "returncode": c["returncode"]} for c in checks],
        "receipt": str((HERE / "receipt.json").relative_to(ROOT))}, indent=2))
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
