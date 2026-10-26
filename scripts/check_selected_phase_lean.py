"""Serial pinned Lean check, exact theorem exports and false-claim controls.

--dependency-project may point to an existing compatible cache. Its tracked
package sources and revisions are verified before read-only use. This produces
a local observation, not an admission into the historical authority catalogue.
No complex chord geometry, BBP source, irrationality measure or normality is certified.
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
PROJECT = ROOT / "formal/mathlib_bridge"
SOURCE = ROOT / "formal/SelectedPhase.lean"
NAMESPACE = "ObservationalSUCC.SelectedPhase"
PIN = "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84"
ALLOWED_AXIOMS = {"propext", "Classical.choice", "Quot.sound"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def output(command: list[str], cwd: Path) -> str:
    return subprocess.check_output(command, cwd=cwd, text=True).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dependency-project", type=Path, default=PROJECT)
    args = parser.parse_args()
    destination = args.output.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    receipt = destination / "kernel-observation.json"
    # An interrupted rerun must not leave an earlier success at this location.
    if receipt.exists():
        receipt.unlink()
    build = Path(tempfile.mkdtemp(prefix="selected-build-", dir=destination))
    dependency = args.dependency_project.resolve()
    manifest_path = PROJECT / "lake-manifest.json"
    manifest = json.loads(manifest_path.read_text())
    pins = {package["name"]: package["rev"] for package in manifest["packages"]}
    if pins.get("mathlib") != PIN:
        raise RuntimeError("Unexpected repository mathlib pin")
    expected_toolchain = "leanprover/lean4:v4.14.0"
    if (ROOT / "lean-toolchain").read_text().strip() != expected_toolchain:
        raise RuntimeError("Unexpected repository Lean pin")
    paths = [str(build)]
    for name, revision in sorted(pins.items()):
        package = dependency / ".lake/packages" / name
        actual = output(["git", "rev-parse", "HEAD"], package)
        dirty = output(["git", "status", "--porcelain", "--untracked-files=no"], package)
        if actual != revision or dirty:
            raise RuntimeError(f"Dependency source mismatch: {name}: {actual} {dirty}")
        library = package / ".lake/build/lib"
        if name == "mathlib" and not library.is_dir():
            raise RuntimeError(f"Missing compiled mathlib cache: {library}")
        paths.append(str(library))
    env = {**os.environ, "LEAN_PATH": os.pathsep.join(paths)}
    version = output(["lean", "--version"], ROOT)
    if not re.search(r"version 4\.14\.0,", version):
        raise RuntimeError(f"Unexpected Lean compiler: {version}")
    source_paths = (
        SOURCE, Path(__file__).resolve(), ROOT / "lean-toolchain", manifest_path,
        ROOT / "formal/kernel_audit/ExportCommand.lean",
        ROOT / "scripts/cambrian_audit_c_lean.py",
    )
    hashes = {str(path.relative_to(ROOT)): sha(path.read_bytes()) for path in source_paths}
    from cambrian_audit_c_lean import uncomment
    for path in source_paths:
        if path.suffix == ".lean" and re.search(
            r"\b(sorry|admit|axiom|unsafe|native_decide)\b", uncomment(path.read_text())
        ):
            raise RuntimeError(f"Forbidden proof authority token: {path}")
    names = [NAMESPACE + "." + name for name in
             re.findall(r"^theorem\s+(\w+)", SOURCE.read_text(), re.M)]
    if not names:
        raise RuntimeError("No theorem declarations found")
    commands = []
    failures = []
    exports = {}
    controls = []
    commit = output(["git", "rev-parse", "HEAD"], ROOT)

    def run(label: str, path: Path, *, compile_module: bool = False):
        command = ["lean", "-j", "1", "-M", "2048", "-DmaxHeartbeats=1200000"]
        if compile_module:
            command += ["-o", str(build / "SelectedPhase.olean")]
        command.append(str(path))
        start = time.monotonic()
        result = subprocess.run(command, cwd=ROOT, env=env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                timeout=600)
        log = destination / f"{label}.log"
        log.write_text(result.stdout)
        commands.append({"label": label, "command": command, "cwd": str(ROOT),
                         "exit_code": result.returncode,
                         "seconds": round(time.monotonic()-start, 3),
                         "log": log.name, "log_sha256": sha(result.stdout.encode())})
        print(f"{label}: exit {result.returncode}", flush=True)
        return result

    result = run("finite-kernel", SOURCE, compile_module=True)
    if result.returncode:
        failures.append("finite-kernel")
    else:
        export = build / "SelectedExport.lean"
        export.write_text(
            "import SelectedPhase\n" +
            (ROOT / "formal/kernel_audit/ExportCommand.lean").read_text() + "\n" +
            "".join(f"#check @{name}\n#print axioms {name}\n#succ_export {name}\n"
                    for name in names))
        result = run("axiom-export", export)
        if result.returncode:
            failures.append("axiom-export")
        for line in result.stdout.splitlines():
            if "SUCC_THEOREM_JSON " not in line:
                continue
            item = json.loads(line.split("SUCC_THEOREM_JSON ", 1)[1])
            name = item.pop("name")
            if name in exports or name not in names or set(item["axioms"])-ALLOWED_AXIOMS:
                raise RuntimeError(f"Unapproved theorem export: {name}")
            item["type_sha256"] = sha(item["type_expr"].encode())
            exports[name] = item
        if set(exports) != set(names):
            failures.append("incomplete-exports")

        # Paired exact controls reject a wrong forcing sign, an overcounted
        # block loss, and replacement of the strict integer gap by a weak one.
        examples = (
            ("backward-forcing-sign", "(3:ℝ)+2/16=50/16", "(3:ℝ)-2/16=50/16"),
            ("overcounted-block-loss", "(100:ℝ)-3/1250 ≤ 100-2/1250",
             "(100:ℝ)-3/1250 ≤ 100-4/1250"),
            ("strict-integer-gap", "(1:ℤ) ≠ 0", "(1:ℤ) = 0"),
        )
        for label, positive_claim, false_claim in examples:
            pair = {}
            for kind, claim in (("positive", positive_claim), ("mutant", false_claim)):
                body = ("import SelectedPhase\nopen " + NAMESPACE + "\n" +
                        "theorem exact_control : " + positive_claim +
                        " := by norm_num\n" +
                        "example : " + claim + " := by exact exact_control\n")
                path = build / f"{label}_{kind}.lean"
                path.write_text(body)
                result = run(f"{label}-{kind}", path)
                pair[kind] = result, sha(body.encode())
            positive, positive_sha = pair["positive"]
            mutant, mutant_sha = pair["mutant"]
            infrastructure_error = any(token in mutant.stdout.lower() for token in (
                "unknown module", "unknown constant", "unknown identifier", "unexpected token"))
            passed = (positive.returncode == 0 and mutant.returncode != 0 and
                      "type mismatch" in mutant.stdout.lower() and not infrastructure_error)
            controls.append({"name": label, "passed": passed,
                             "positive_sha256": positive_sha, "mutant_sha256": mutant_sha})
            if not passed:
                failures.append(label)

    unchanged = hashes == {str(path.relative_to(ROOT)): sha(path.read_bytes())
                           for path in source_paths}
    if not unchanged:
        failures.append("source-changed-during-check")
    record = {
        "schema": "succ.selected-phase.lean-observation.v1",
        "status": "KERNEL_CHECKED" if not failures else "FAILED",
        "commit_at_start": commit,
        "commit_at_end": output(["git", "rev-parse", "HEAD"], ROOT),
        "lean_version": version, "dependency_project": str(dependency),
        "dependency_revisions": pins, "source_hashes": hashes,
        "sources_unchanged": unchanged, "commands": commands,
        "theorem_exports": exports, "negative_controls": controls,
        "failures": failures, "normality_proved": False,
        "complex_character_bridge_formalized": False,
        "analytic_transport_formalized": False,
        "historical_authority_modified": False,
    }
    receipt.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n")
    print(record["status"], len(exports), "theorems;", len(controls), "paired controls",
          flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
