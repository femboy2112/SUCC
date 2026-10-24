"""Serial exact-source Lean check and axiom export; no normality authority.

Use --dependency-project for a read-only compatible mathlib cache. Every
dependency revision is checked against formal/duck_pi/lake-manifest.json.
Output is an observation tied to source hashes, not self-authenticating proof.
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
PROJECT = ROOT / "formal/duck_pi"
MODULES = ("BaileyCrandall", "BBPIntegral", "PiSource", "BBPSourceGenesis")
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}
NAMESPACE = "ObservationalSUCC.PiSourceGenesis"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def output(cmd: list[str], cwd: Path) -> str:
    return subprocess.check_output(cmd, cwd=cwd, text=True).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dependency-project", type=Path, default=PROJECT)
    args = parser.parse_args()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    build = Path(tempfile.mkdtemp(prefix="build-", dir=destination))
    dependency = args.dependency_project.resolve()
    manifest = json.loads((PROJECT / "lake-manifest.json").read_text())
    pins = {p["name"]: p["rev"] for p in manifest["packages"]}
    if pins["mathlib"] != "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84":
        raise RuntimeError("Unexpected mathlib source pin")
    paths = [str(build)]
    for name, revision in sorted(pins.items()):
        package = dependency / ".lake/packages" / name
        actual = output(["git", "rev-parse", "HEAD"], package)
        dirty = output(["git", "status", "--porcelain", "--untracked-files=no"], package)
        if actual != revision or dirty:
            raise RuntimeError(f"Dependency source mismatch: {name}: {actual} {dirty}")
        library = package / ".lake/build/lib"
        if name == "mathlib" and not library.is_dir():
            raise RuntimeError(f"Missing compiled dependency: {library}")
        paths.append(str(library))
    env = {**os.environ, "LEAN_PATH": os.pathsep.join(paths)}
    version = output(["lean", "--version"], PROJECT)
    if "version 4.14.0" not in version:
        raise RuntimeError(f"Unexpected Lean: {version}")
    source_paths = [PROJECT / f"{m}.lean" for m in MODULES]
    source_paths.extend([
        Path(__file__).resolve(), PROJECT / "lean-toolchain",
        PROJECT / "lake-manifest.json", ROOT / "formal/kernel_audit/ExportCommand.lean",
        ROOT / "scripts/cambrian_audit_c_lean.py",
    ])
    hashes = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in source_paths}
    commit = output(["git", "rev-parse", "HEAD"], ROOT)
    status = output(["git", "status", "--short", "--", *hashes], ROOT)
    # Strip Lean's nested comments before checking forbidden source authority.
    from cambrian_audit_c_lean import uncomment
    for path in source_paths:
        if path.suffix == ".lean" and re.search(
            r"\b(sorry|admit|axiom|unsafe|native_decide)\b", uncomment(path.read_text())
        ):
            raise RuntimeError(f"Forbidden proof token: {path}")
    commands = []
    failures = []

    def run(label: str, command: list[str]) -> subprocess.CompletedProcess:
        start = time.time()
        result = subprocess.run(
            command, cwd=PROJECT, env=env, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300,
        )
        log = destination / f"{label}.log"
        log.write_text(result.stdout)
        commands.append({
            "label": label, "command": command, "cwd": str(PROJECT),
            "exit_code": result.returncode, "seconds": round(time.time()-start, 3),
            "log": log.name, "log_sha256": sha(result.stdout.encode()),
        })
        print(f"{label}: exit {result.returncode}", flush=True)
        return result

    for module in MODULES:
        result = run(module, [
            "lean", "-j", "1", "-M", "4096", "-o", str(build/f"{module}.olean"),
            str(PROJECT/f"{module}.lean"),
        ])
        if result.returncode:
            failures.append(module)
            break
    exports = {}
    controls = []
    if not failures:
        source = (PROJECT/"BBPSourceGenesis.lean").read_text()
        names = [NAMESPACE+"."+n for n in re.findall(r"^theorem\s+(\w+)", source, re.M)]
        export = build/"SourceGenesisAudit.lean"
        export.write_text(
            "import BBPSourceGenesis\n" +
            (ROOT/"formal/kernel_audit/ExportCommand.lean").read_text() + "\n" +
            "".join(f"#check @{n}\n#print axioms {n}\n#succ_export {n}\n" for n in names)
        )
        result = run("axiom-export", ["lean", "-j", "1", "-M", "4096", str(export)])
        if result.returncode:
            failures.append("axiom-export")
        for line in result.stdout.splitlines():
            if "SUCC_THEOREM_JSON " not in line:
                continue
            item = json.loads(line.split("SUCC_THEOREM_JSON ", 1)[1])
            name = item.pop("name")
            if name in exports or name not in names or set(item["axioms"])-ALLOWED_AXIOMS:
                raise RuntimeError(f"Invalid theorem export: {name}")
            item["type_sha256"] = sha(item["type_expr"].encode())
            exports[name] = item
        if set(exports) != set(names):
            failures.append("incomplete-exports")
        examples = (
            ("pole-sign", "poleMoment 1 = (15/64 : ℝ)", "pole_moment_one", "15/64", "14/64"),
            ("initial-state", "Int.fract (16*(1/3 : ℝ)+ObservationalSUCC.BaileyCrandall.forcing 1) = 7/15",
             "forced_first_third", "7/15", "1/3"),
            ("kernel-factor", "DuckPiIntegral.numerator (1/2) = (1-(1/2 : ℝ))*kernelH (1/2)",
             "kernel_factorization (1/2)", "(1-(1/2 : ℝ))", "(2-(1/2 : ℝ))"),
            ("invariant-sign", "(∑ j ∈ Finset.range (1+1), (-1 : ℝ)^j * (Nat.choose 1 j : ℝ) * 16^j) = (-15 : ℝ)^1",
             "weighted_binomial_invariant 1", "(-15 : ℝ)^1", "(15 : ℝ)^1"),
        )
        for label, statement, proof, old, new in examples:
            pair = {}
            for kind in ("positive", "mutant"):
                claim = statement if kind == "positive" else statement.replace(old, new, 1)
                body = ("import BBPSourceGenesis\nopen scoped BigOperators\nopen "+NAMESPACE+
                        "\nexample : "+claim+" := by\n  exact "+proof+"\n")
                path = build/f"{label}_{kind}.lean"
                path.write_text(body)
                result = run(f"{label}-{kind}", ["lean", "-j", "1", "-M", "4096", str(path)])
                pair[kind] = (result, sha(body.encode()))
            positive, positive_sha = pair["positive"]
            mutant, mutant_sha = pair["mutant"]
            bad_infrastructure = any(token in mutant.stdout.lower() for token in (
                "unknown module", "unknown constant", "unknown identifier", "unexpected token",
            ))
            passed = (positive.returncode == 0 and mutant.returncode != 0 and
                      "type mismatch" in mutant.stdout.lower() and not bad_infrastructure)
            controls.append({"name": label, "passed": passed,
                             "positive_sha256": positive_sha, "mutant_sha256": mutant_sha})
            if not passed:
                failures.append(label)
    unchanged = hashes == {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in source_paths}
    if not unchanged:
        failures.append("source-changed-during-check")
    record = {
        "schema": "succ.pi-source-genesis.lean-observation.v1",
        "status": "KERNEL_CHECKED" if not failures else "FAILED",
        "commit_at_start": commit, "commit_at_end": output(["git", "rev-parse", "HEAD"], ROOT),
        "scoped_status_at_start": status, "lean_version": version,
        "dependency_project": str(dependency), "dependency_revisions": pins,
        "source_hashes": hashes, "sources_unchanged": unchanged,
        "commands": commands, "theorem_exports": exports,
        "negative_controls": controls, "failures": failures,
        "normality_proved": False, "historical_authority_modified": False,
    }
    (destination/"kernel-observation.json").write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(record["status"], len(exports), "theorems;", len(controls), "paired controls", flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
