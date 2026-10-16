#!/usr/bin/env python3
"""Reproducible source-stable validation, with bounded serial child processes."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot():
    return {str(p.relative_to(ROOT)): sha(p)
            for directory in ("observational_succ", "tests", "scripts")
            for p in sorted((ROOT / directory).glob("*.py"))}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--python", required=True)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--focused-only", action="store_true")
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1",
               OMP_NUM_THREADS="1", MKL_NUM_THREADS="1")
    before = snapshot()
    result = {"timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "head_at_start": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
              "source_before": before, "commands": [], "finished": False}
    commands = [("versions", ["-c", "import sys,numpy,scipy,mpmath,sympy; print(sys.version); print({x.__name__: x.__version__ for x in (numpy,scipy,mpmath,sympy)})"])]
    commands += [("focused-"+name, ["-m", "unittest", "discover", "-s", "tests", "-p", f"test_{name}.py", "-v"])
                 for name in ("observer_schur", "observer_schur_source", "compact_galerkin", "observer_discovery", "formal_instance_bridge", "source_proof_certificate")]
    if not args.focused_only:
        commands += [("full-unittest", ["-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"])]
    commands += [(name, [f"scripts/{name}.py"] +
                  (["--output", str(args.output.resolve() / "compact-probe.json")]
                   if name == "compact_galerkin_probe" else [])) for name in (
        "verify_provenance", "observer_foundations_probe", "ordinal_succ_report_probe",
        "observer_schur_probe", "compact_galerkin_probe", "observer_discovery_probe",
        "source_proof_certificate_probe")]
    commands.append(("round-capsules", ["-c",
        "import json; from pathlib import Path; "
        "from observational_succ.source_proof_certificate import audit_capsules; "
        "print(json.dumps(audit_capsules(json.loads(Path('research/2026-10-16/OBSERVER_SCHUR_CAPSULES.json').read_text()), Path.cwd()), indent=2))"]))
    failed = False
    for label, argv in commands:
        start = time.monotonic()
        command = [args.python, "-B", *argv]
        try:
            proc = subprocess.run(command, cwd=ROOT, env=env, text=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                  timeout=1800 if label == "full-unittest" else 300)
            output, code = proc.stdout, proc.returncode
        except subprocess.TimeoutExpired as exc:
            output = exc.stdout or ""
            if isinstance(output, bytes):
                output = output.decode(errors="replace")
            output += "\nTIMEOUT: validation incomplete\n"
            code = 124
        log = args.output / (label + ".log")
        log.write_text(output)
        result["commands"].append({"argv": command, "label": label, "exit_code": code,
                                   "elapsed_seconds": round(time.monotonic()-start, 3),
                                   "log": log.name, "sha256": sha(log)})
        (args.output / "validation.json").write_text(json.dumps(result, indent=2)+"\n")
        print(f"{label}: exit {code}", flush=True)
        failed |= code != 0
    result.update(source_after=snapshot(), finished=True)
    result["source_stable"] = result["source_after"] == before
    result["all_commands_passed"] = not failed
    (args.output / "validation.json").write_text(json.dumps(result, indent=2)+"\n")
    raise SystemExit(0 if not failed and result["source_stable"] else 1)


if __name__ == "__main__":
    main()
