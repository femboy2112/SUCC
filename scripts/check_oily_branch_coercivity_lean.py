"""Pinned finite branch-coercivity checks, exact exports and falsifying mutants.

The dependency tree is read-only and must have the repository's exact pins.
No analytic BBP, trigonometric or irrationality-measure theorem is certified.
An optional runtime note records host executable-path compatibility only.
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

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "formal/OilyBranchCoercivity.lean"
PREFIX = "ObservationalSUCC.OilyBranchCoercivity."
THEOREMS = (
    "coefficient_norms", "adjacent_branch_quadratic",
    "separated_branch_quadratic", "loss_implies_small_phase",
    "trigonometric_rational_margin", "branch_rational_margin",
    "gap_energy_forces_loss", "adjacent_gap_forces_loss",
    "separated_gap_forces_loss",
)
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def output(command: list[str], cwd: Path) -> str:
    return subprocess.check_output(command, cwd=cwd, text=True).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dependency-project", type=Path,
                        default=ROOT / "formal/mathlib_bridge")
    parser.add_argument("--lean", default=os.environ.get("LEAN_BIN", "lean"))
    parser.add_argument("--runtime-note", type=Path)
    args = parser.parse_args()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    receipt = destination / "kernel-observation.json"
    receipt.unlink(missing_ok=True)
    build = Path(tempfile.mkdtemp(prefix="oily-coercivity-build-", dir=destination))
    manifest_path = ROOT / "formal/mathlib_bridge/lake-manifest.json"
    pins = {p["name"]: p["rev"] for p in json.loads(manifest_path.read_text())["packages"]}
    if pins["mathlib"] != "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84":
        raise RuntimeError("Unexpected mathlib pin")
    if (ROOT / "lean-toolchain").read_text().strip() != "leanprover/lean4:v4.14.0":
        raise RuntimeError("Unexpected Lean pin")
    paths = [str(build)]
    for name, revision in sorted(pins.items()):
        package = args.dependency_project.resolve() / ".lake/packages" / name
        actual = output(["git", "rev-parse", "HEAD"], package)
        dirty = output(["git", "status", "--porcelain", "--untracked-files=no"], package)
        if actual != revision or dirty:
            raise RuntimeError(f"Dependency source mismatch: {name}: {actual} {dirty}")
        paths.append(str(package / ".lake/build/lib"))
    env = {**os.environ, "LEAN_PATH": os.pathsep.join(paths)}
    version = output([args.lean, "--version"], ROOT)
    if not re.search(r"version 4\.14\.0,", version):
        raise RuntimeError("Unexpected compiler version: " + version)
    from check_source_faithful_carry_lean import strip_comments
    text = SOURCE.read_text()
    code = strip_comments(text)
    if re.search(r"\b(sorry|admit|axiom|unsafe|native_decide)\b", code):
        raise RuntimeError("Forbidden proof authority token")
    names = tuple(re.findall(r"^theorem\s+(\w+)", code, re.M))
    if names != THEOREMS:
        raise RuntimeError("Every and only declared theorem must be audited")
    source_paths = (
        SOURCE, Path(__file__).resolve(), ROOT / "lean-toolchain", manifest_path,
        ROOT / "formal/kernel_audit/ExportCommand.lean",
        ROOT / "scripts/check_source_faithful_carry_lean.py",
    )
    hashes = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in source_paths}
    commit = output(["git", "rev-parse", "HEAD"], ROOT)
    commands, failures, exports, controls = [], [], {}, []

    def run(label: str, path: Path, compile_module: bool = False):
        cmd = [args.lean, "-j", "1", "-M", "2048", "-DmaxHeartbeats=1200000"]
        if compile_module:
            cmd += ["-o", str(build / "OilyBranchCoercivity.olean")]
        cmd.append(str(path))
        start = time.monotonic()
        result = subprocess.run(cmd, cwd=ROOT, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                timeout=300)
        (destination / f"{label}.log").write_text(result.stdout)
        commands.append({"label": label, "command": cmd,
                         "exit_code": result.returncode,
                         "seconds": round(time.monotonic()-start, 3),
                         "log_sha256": sha(result.stdout.encode())})
        print(f"{label}: exit {result.returncode}", flush=True)
        return result

    checked = run("finite-kernel", SOURCE, True)
    if checked.returncode:
        failures.append("finite-kernel")
    else:
        export = build / "OilyCoercivityExport.lean"
        export.write_text("import OilyBranchCoercivity\n" +
            (ROOT / "formal/kernel_audit/ExportCommand.lean").read_text() + "\n" +
            "".join(f"#succ_export {PREFIX}{name}\n" for name in THEOREMS))
        exported = run("axiom-export", export)
        if exported.returncode:
            failures.append("axiom-export")
        for line in exported.stdout.splitlines():
            if not line.startswith("SUCC_THEOREM_JSON "):
                if line.strip():
                    failures.append("unexpected-export-output")
                continue
            item = json.loads(line.removeprefix("SUCC_THEOREM_JSON "))
            name = item.pop("name")
            if name in exports or name not in {PREFIX+n for n in THEOREMS}:
                raise RuntimeError("Unknown or duplicate theorem export")
            if set(item["axioms"])-ALLOWED_AXIOMS or not item["type_expr"]:
                raise RuntimeError("Unapproved axioms or empty theorem type")
            item["type_sha256"] = sha(item["type_expr"].encode())
            exports[name] = item
        if set(exports) != {PREFIX+n for n in THEOREMS}:
            failures.append("incomplete-theorem-exports")

        # Each variant changes a mathematical premise or sharp constant in an
        # otherwise elaboratable source. A parser/import failure is not a kill.
        mutants = (
            ("adjacent-norm-too-small", "≤ 546*(a^2+b^2+c^2)",
             "≤ 545*(a^2+b^2+c^2)"),
            ("separated-norm-too-small", "≤ 514*(a^2+b^2+c^2+d^2)",
             "≤ 513*(a^2+b^2+c^2+d^2)"),
            ("missing-small-loss", "(small : loss ≤ 1/29)", "(small : True)"),
            ("false-rational-margin", "= 2329025/37950062592", "= 0"),
        )
        for label, before, after in mutants:
            if text.count(before) != 1:
                raise RuntimeError("Mutation is not unique: " + label)
            mutated = text.replace(before, after)
            path = build / (label + ".lean")
            path.write_text(mutated)
            result = run(label, path)
            infrastructure_error = any(s in result.stdout.lower() for s in (
                "unknown module", "unknown constant", "unknown identifier",
                "unexpected token", "failed to locate application"))
            passed = result.returncode != 0 and "error:" in result.stdout and not infrastructure_error
            controls.append({"name": label, "passed": passed,
                             "source_sha256": sha(mutated.encode())})
            if not passed:
                failures.append(label)
    unchanged = hashes == {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in source_paths}
    if not unchanged:
        failures.append("source-changed-during-check")
    record = {
        "schema": "succ.oily-branch-coercivity.lean-observation.v1",
        "status": "KERNEL_CHECKED" if not failures else "FAILED",
        "commit_at_start": commit,
        "commit_at_end": output(["git", "rev-parse", "HEAD"], ROOT),
        "lean_version": version, "dependency_revisions": pins,
        "dependency_project": str(args.dependency_project.resolve()),
        "source_hashes": hashes, "sources_unchanged": unchanged,
        "theorem_exports": exports, "negative_controls": controls,
        "commands": commands, "failures": failures,
        "runtime_note": None if args.runtime_note is None else json.loads(args.runtime_note.read_text()),
        "dynamic_preload_present": bool(os.environ.get("LD_PRELOAD")),
        "normality_proved": False, "analytic_transport_formalized": False,
        "irrationality_measure_formalized": False,
        "historical_authority_modified": False,
    }
    receipt.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(record["status"], len(exports), "theorems;", len(controls), "mutants", flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
