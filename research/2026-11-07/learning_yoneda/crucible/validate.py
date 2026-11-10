"""Run only this additive dossier's exact and kernel checks, serially."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def main():
    env = dict(os.environ, PYTHONPATH=str(ROOT))
    commands = [
        ("oracle", [sys.executable, str(HERE / "hostile_oracle.py")]),
        ("unit", [sys.executable, "-m", "unittest", "discover", "-s", str(HERE),
                  "-p", "test_*.py", "-v"]),
        ("lean_version", ["lean", "--version"]),
        ("lean", ["lean", str(HERE / "ConditionalMemory.lean")]),
    ]
    records = []
    for name, command in commands:
        completed = subprocess.run(command, cwd=ROOT, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (HERE / f"{name}_stdout.txt").write_text(completed.stdout)
        (HERE / f"{name}_stderr.txt").write_text(completed.stderr)
        records.append({"name": name, "command": command,
                        "cwd": str(ROOT), "returncode": completed.returncode})
    files = [HERE / name for name in (
        "ConditionalMemory.lean", "hostile_oracle.py", "test_hostile.py",
        "PREREGISTRATION.md", "HOSTILE_THEOREMS.md", "finite_receipt.json",
    )]
    result = {
        "python": platform.python_version(), "commands": records,
        "sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in files},
        "all_passed": all(r["returncode"] == 0 for r in records),
        "formal_scope": "conditional memory decoder lemmas and explicit C5 only",
        "normality_or_RH_kernel_claim": False,
    }
    (HERE / "validation.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps(result, sort_keys=True))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
