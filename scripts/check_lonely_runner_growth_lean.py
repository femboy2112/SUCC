"""Pinned serial kernel audit of actual finite-source gaps and upper-half growth.

The dependency cache is read-only. A fresh isolated output directory holds
compiled objects, complete theorem types, axiom lists, and paired mutations.
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
MODULES = ("LonelyRunnerDeletion", "LonelyRunnerTwoEntry", "LonelyRunnerGrowth")
NAMESPACE = "ObservationalSUCC.LonelyRunnerGrowth"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def validate_exports(items, expected):
    """Reject absent, duplicate, invented, or nonstandard-axiom authority."""
    expected = set(expected)
    if not expected:
        raise ValueError("zero expected theorem exports")
    result = {}
    for original in items:
        item = dict(original)
        name = item.pop("name")
        if name in result or name not in expected:
            raise ValueError("duplicate or unexpected theorem export")
        if set(item["axioms"]) - ALLOWED_AXIOMS:
            raise ValueError("nonstandard theorem axiom")
        if not item["type_expr"]:
            raise ValueError("missing exact theorem type")
        item["type_sha256"] = sha(item["type_expr"].encode())
        result[name] = item
    if set(result) != expected:
        raise ValueError("incomplete theorem exports")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dependency-project", type=Path, default=PROJECT)
    args = parser.parse_args()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    dependency = args.dependency_project.resolve()
    build = Path(tempfile.mkdtemp(prefix="growth-kernel-build-", dir=destination))
    pins = {p["name"]: p["rev"] for p in json.loads((PROJECT / "lake-manifest.json").read_text())["packages"]}
    if pins.get("mathlib") != "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84":
        raise RuntimeError("unexpected Mathlib source pin")

    def output(command, cwd):
        return subprocess.check_output(command, cwd=cwd, text=True).strip()

    paths = [str(build)]
    for name, revision in sorted(pins.items()):
        package = dependency / ".lake/packages" / name
        if output(["git", "rev-parse", "HEAD"], package) != revision:
            raise RuntimeError(f"dependency revision mismatch: {name}")
        if output(["git", "status", "--porcelain", "--untracked-files=no"], package):
            raise RuntimeError(f"tracked dependency modification: {name}")
        paths.append(str(package / ".lake/build/lib"))
    env = {**os.environ, "LEAN_PATH": os.pathsep.join(paths)}
    version = output(["lean", "--version"], ROOT)
    if "version 4.14.0" not in version:
        raise RuntimeError(f"unexpected Lean version: {version}")
    sources = [ROOT / "formal" / f"{name}.lean" for name in MODULES]
    sources += [Path(__file__).resolve(), ROOT / "lean-toolchain", PROJECT / "lake-manifest.json",
                ROOT / "formal/kernel_audit/ExportCommand.lean", ROOT / "scripts/cambrian_audit_c_lean.py"]
    hashes = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in sources}
    for module in MODULES:
        source = (ROOT / "formal" / f"{module}.lean").read_text()
        if re.search(r"\b(sorry|admit|axiom|unsafe|native_decide)\b", uncomment(source)):
            raise RuntimeError(f"forbidden proof token: {module}")
    source = (ROOT / "formal/LonelyRunnerGrowth.lean").read_text()
    names = [NAMESPACE + "." + name for name in re.findall(r"^theorem\s+(\w+)", source, re.M)]
    if not names:
        raise RuntimeError("zero growth theorems discovered")
    commands, failures, exports, controls = [], [], {}, []

    def run(label, path, object_path=None):
        command = ["lean", "-j", "1", "-M", "1536"]
        if object_path is not None:
            command += ["-o", str(object_path)]
        command += [str(path)]
        start = time.monotonic()
        result = subprocess.run(command, cwd=ROOT / "formal", env=env, capture_output=True,
                                text=True, timeout=300)
        log = result.stdout + result.stderr
        (destination / f"{label}.log").write_text(log)
        commands.append({"label": label, "command": command, "exit_code": result.returncode,
                         "seconds": round(time.monotonic()-start, 3),
                         "log": f"{label}.log", "log_sha256": sha(log.encode())})
        print(f"{label}: exit {result.returncode}", flush=True)
        return result, log

    for module in MODULES:
        result, _ = run(module, ROOT / "formal" / f"{module}.lean", build / f"{module}.olean")
        if result.returncode:
            failures.append(module)
            break
    if not failures:
        export_file = build / "GrowthAudit.lean"
        export_file.write_text("import LonelyRunnerGrowth\n" +
            (ROOT / "formal/kernel_audit/ExportCommand.lean").read_text() + "\n" +
            "".join(f"#check @{name}\n#print axioms {name}\n#succ_export {name}\n" for name in names))
        result, log = run("growth-axiom-export", export_file)
        if result.returncode:
            failures.append("growth-axiom-export")
        items = [json.loads(line.split("SUCC_THEOREM_JSON ", 1)[1])
                 for line in log.splitlines() if "SUCC_THEOREM_JSON " in line]
        try:
            exports = validate_exports(items, names)
        except ValueError as error:
            failures.append(str(error))
        examples = [
            ("band-width", "(v δ a b : ℝ) (hv : 0 < v) (hδ : δ < 1/2) (hab : a < b) "
             "(hc : ∀ t : ℝ, a < t → t < b → Bad v δ t)",
             "b-a ≤ 2*δ/v", "covered_open_interval_width v δ a b hv hδ hab hc", "2*δ/v", "δ/v"),
            ("integer-spacing", "(D A B : ℤ) (hD : 0 < D) (hab : (A:ℝ)/(D:ℝ) < (B:ℝ)/(D:ℝ))",
             "1/(D:ℝ) ≤ (B:ℝ)/(D:ℝ)-(A:ℝ)/(D:ℝ)",
             "integer_numerator_spacing D A B hD hab", "1/(D:ℝ)", "2/(D:ℝ)"),
            ("upper-half-cubic", "(n r s w₁ w₂ : ℤ) (hn : 5 ≤ n) (hr : 1 ≤ r) (hrs : r < s) "
             "(hs : s ≤ n-1) (hupper : n-1 < 2*r) (hw₁ : n ≤ w₁) (hw₂ : w₁ < w₂) "
             "(hc : Covers (insert w₂ (insert w₁ (retainedSource n r s))) (1/(n:ℝ)))",
             "w₂ < 3*n^3", "upper_half_cubic_growth n r s w₁ w₂ hn hr hrs hs hupper hw₁ hw₂ hc",
             "3*n^3", "0"),
        ]
        for label, variables, statement, proof, old, new in examples:
            pair = {}
            for kind in ("positive", "mutant"):
                target = statement if kind == "positive" else statement.replace(old, new, 1)
                body = f"import LonelyRunnerGrowth\nopen {NAMESPACE}\nexample {variables} : {target} := by\n  exact {proof}\n"
                path = build / f"{label}-{kind}.lean"
                path.write_text(body)
                result, log = run(f"{label}-{kind}", path)
                pair[kind] = {"exit_code": result.returncode, "source_sha256": sha(body.encode()),
                              "type_mismatch": "type mismatch" in log.lower()}
            passed = pair["positive"]["exit_code"] == 0 and pair["mutant"]["exit_code"] != 0 and pair["mutant"]["type_mismatch"]
            controls.append({"name": label, "passed": passed, **pair})
            if not passed:
                failures.append(label)
    unchanged = hashes == {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in sources}
    if not unchanged:
        failures.append("source-changed-during-check")
    record = {"schema": "succ.lonely-runner.growth-kernel.v1",
              "status": "KERNEL_CHECKED" if not failures else "FAILED",
              "commit_at_observation": output(["git", "rev-parse", "HEAD"], ROOT),
              "lean_version": version, "dependency_revisions": pins,
              "source_hashes": hashes, "sources_unchanged": unchanged, "commands": commands,
              "theorem_exports": exports, "negative_controls": controls, "failures": failures,
              "scope": "Actual finite-source labelled gaps; single- and two-band real interval width; unconditional upper-half second-speed and cubic growth bounds. The arbitrary-deletion hole and unrestricted growth theorem are not certified.",
              "unrestricted_gamma_kernel_proved": False, "general_lonely_runner_proved": False}
    (destination / "kernel-observation.json").write_text(json.dumps(record, sort_keys=True, indent=2)+"\n")
    print(record["status"], len(exports), "growth theorems;", len(controls), "paired controls")
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
