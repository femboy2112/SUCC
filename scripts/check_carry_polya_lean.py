"""Serial Lean kernel replay with pinned dependencies, exports and false controls.

The cache project is read-only. This verifies only the named finite algebraic
statements; analytic/spectral/paper theorems retain their separate authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time

from cambrian_audit_c_lean import uncomment

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "formal/mathlib_bridge"
MODULES = ("DivisorBoundary", "PolyaCoherence")
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def output(command, cwd):
    return subprocess.check_output(command, cwd=cwd, text=True).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dependency-project", type=Path, default=PROJECT)
    args = parser.parse_args()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    dependency = args.dependency_project.resolve()
    pins = {p["name"]: p["rev"] for p in
            json.loads((PROJECT / "lake-manifest.json").read_text())["packages"]}
    if pins["mathlib"] != "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84":
        raise RuntimeError("Unexpected mathlib pin")
    build = Path(tempfile.mkdtemp(prefix="kernel-build-", dir=destination))
    paths = [str(build)]
    for name, revision in sorted(pins.items()):
        package = dependency / ".lake/packages" / name
        actual = output(["git", "rev-parse", "HEAD"], package)
        dirty = output(["git", "status", "--porcelain", "--untracked-files=no"], package)
        if actual != revision or dirty:
            raise RuntimeError(f"Dependency mismatch: {name}: {actual} {dirty}")
        paths.append(str(package / ".lake/build/lib"))
    env = {**os.environ, "LEAN_PATH": os.pathsep.join(paths)}
    version = output(["lean", "--version"], ROOT)
    if "version 4.14.0" not in version:
        raise RuntimeError(f"Unexpected Lean version: {version}")
    sources = [ROOT / "formal" / f"{m}.lean" for m in MODULES]
    sources += [Path(__file__).resolve(), ROOT / "lean-toolchain",
                PROJECT / "lake-manifest.json",
                ROOT / "formal/kernel_audit/ExportCommand.lean",
                ROOT / "scripts/cambrian_audit_c_lean.py"]
    hashes = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in sources}
    names = []
    for module in MODULES:
        source = (ROOT / "formal" / f"{module}.lean").read_text()
        if re.search(r"\b(sorry|admit|axiom|unsafe|native_decide)\b", uncomment(source)):
            raise RuntimeError(f"Forbidden proof token in {module}")
        names += [f"ObservationalSUCC.{module}.{n}"
                  for n in re.findall(r"^theorem\s+(\w+)", source, re.M)]
    commands, failures, exports, controls = [], [], {}, []

    def run(label, command):
        start = time.monotonic()
        result = subprocess.run(command, cwd=ROOT / "formal", env=env,
                                capture_output=True, text=True, timeout=300)
        log = result.stdout + result.stderr
        (destination / f"{label}.log").write_text(log)
        commands.append({"label": label, "command": command,
                         "cwd": str(ROOT / "formal"), "exit_code": result.returncode,
                         "seconds": round(time.monotonic() - start, 3),
                         "log": f"{label}.log", "log_sha256": sha(log.encode())})
        print(f"{label}: exit {result.returncode}", flush=True)
        return result, log

    for module in MODULES:
        result, _ = run(module, ["lean", "-j", "1", "-M", "1536", "-o",
                                 str(build / f"{module}.olean"),
                                 str(ROOT / "formal" / f"{module}.lean")])
        if result.returncode:
            failures.append(module)
            break
    if not failures:
        export_file = build / "Audit.lean"
        export_file.write_text(
            "".join(f"import {m}\n" for m in MODULES) +
            (ROOT / "formal/kernel_audit/ExportCommand.lean").read_text() + "\n" +
            "".join(f"#check @{n}\n#print axioms {n}\n#succ_export {n}\n" for n in names))
        result, log = run("axiom-export", ["lean", "-j", "1", "-M", "1536", str(export_file)])
        if result.returncode:
            failures.append("axiom-export")
        for line in log.splitlines():
            if "SUCC_THEOREM_JSON " not in line:
                continue
            item = json.loads(line.split("SUCC_THEOREM_JSON ", 1)[1])
            name = item.pop("name")
            if name in exports or name not in names or set(item["axioms"]) - ALLOWED_AXIOMS:
                raise RuntimeError(f"Invalid exported authority: {name}")
            item["type_sha256"] = sha(item["type_expr"].encode())
            exports[name] = item
        if set(exports) != set(names):
            failures.append("incomplete-exports")
        examples = [
            ("boundary-sign", "DivisorBoundary", "(N : ℕ) (f : ℕ → ℤ)",
             "edgeSum N f = boundarySum N f - selectedSum N f",
             "signed_boundary_identity N f", " - selectedSum", " + selectedSum"),
            ("polya-gram", "PolyaCoherence", "(m k a b : ℝ)",
             "((m-k)*a+k*b)^2 + k*(m-k)*(a-b)^2 = m*((m-k)*a^2+k*b^2)",
             "row_energy m k a b", "= m*", "= (m+1)*"),
        ]
        for label, module, variables, statement, proof, old, new in examples:
            pair = {}
            for kind in ("positive", "mutant"):
                claim = statement if kind == "positive" else statement.replace(old, new, 1)
                body = (f"import {module}\nopen ObservationalSUCC.{module}\n" +
                        f"example {variables} : {claim} := by\n  exact {proof}\n")
                path = build / f"{label}-{kind}.lean"
                path.write_text(body)
                result, log = run(f"{label}-{kind}",
                                  ["lean", "-j", "1", "-M", "1536", str(path)])
                pair[kind] = {"exit_code": result.returncode, "source_sha256": sha(body.encode()),
                              "type_mismatch": "type mismatch" in log.lower()}
            passed = (pair["positive"]["exit_code"] == 0 and
                      pair["mutant"]["exit_code"] != 0 and pair["mutant"]["type_mismatch"])
            controls.append({"name": label, "passed": passed, **pair})
            if not passed:
                failures.append(label)
    unchanged = hashes == {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in sources}
    if not unchanged:
        failures.append("source-changed-during-check")
    record = {"schema": "succ.carry-polya.kernel-observation.v1",
              "status": "KERNEL_CHECKED" if not failures else "FAILED",
              "commit_at_observation": output(["git", "rev-parse", "HEAD"], ROOT),
              "lean_version": version, "dependency_revisions": pins,
              "source_hashes": hashes, "sources_unchanged": unchanged,
              "commands": commands, "theorem_exports": exports,
              "negative_controls": controls, "failures": failures,
              "scope": "Finite boundary telescoping and real Polya Gram algebra only",
              "pi_normality_proved": False, "RH_proved": False}
    (destination / "kernel-observation.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(record["status"], len(exports), "theorems;", len(controls), "paired controls")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
