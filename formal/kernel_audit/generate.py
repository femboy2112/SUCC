"""Rebuild local Lean theorems and export source-bound kernel observations.

Run from any directory with pinned Lean/Lake and the manifest dependencies cached.
Output is evidence for coordinator review, NEVER self-authenticating authority.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
TOOLCHAIN = "leanprover/lean4:v4.14.0"
MATHLIB = "4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84"
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
PROJECTS = {
    "mathlib_bridge": ("MasonStothersBridge", [
        "SUCC.MasonStothersBridge.radical_neg_prod",
        "SUCC.MasonStothersBridge.succ_mason_stothers_core",
        "SUCC.MasonStothersBridge.succ_mason_stothers_charZero",
        "SUCC.MasonStothersBridge.control_hW_is_load_bearing",
        "SUCC.MasonStothersBridge.polynomial_fermat",
    ]),
    "cloud_schur": ("CloudSchur", [
        "ObservationalSUCC.CloudSchur.finite_schur_psd_iff",
        "ObservationalSUCC.CloudSchur.finite_negative_direction",
        "ObservationalSUCC.CloudSchur.scalar_schur_identity",
        "ObservationalSUCC.CloudSchur.scalar_negative_lift",
        "ObservationalSUCC.CloudSchur.zero_diagonal_negative",
    ]),
}


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def command(args: list[str], cwd: Path, logfile: Path, *, check_axioms: bool = True) -> str:
    run = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, check=False)
    logfile.write_text(run.stdout)
    for line in run.stdout.splitlines():
        if "SUCC_THEOREM_JSON " in line:
            entry = json.loads(line.split("SUCC_THEOREM_JSON ", 1)[1])
            print(f"KERNEL_EXPORTED {entry['name']} type_sha256={sha256(entry['type_expr'].encode())}")
        else:
            print(line, flush=True)
    if run.returncode:
        raise RuntimeError(f"command failed ({run.returncode}): {args}; see {logfile}")
    if check_axioms and ("sorryAx" in run.stdout or "uses 'sorry'" in run.stdout):
        raise RuntimeError(f"forbidden proof shortcut in {logfile}")
    return run.stdout


def parse_exports(log: str, expected: list[str]) -> dict:
    exports = {}
    for line in log.splitlines():
        marker = "SUCC_THEOREM_JSON "
        if marker not in line:
            continue
        entry = json.loads(line.split(marker, 1)[1])
        name = entry.pop("name")
        if name in exports or name not in expected:
            raise ValueError(f"unexpected or duplicate theorem: {name}")
        if not isinstance(entry["type_expr"], str) or not entry["type_expr"]:
            raise ValueError("missing actual theorem type")
        if set(entry["axioms"]) - ALLOWED:
            raise ValueError(f"unapproved axioms for {name}: {entry['axioms']}")
        entry["type_sha256"] = sha256(entry["type_expr"].encode())
        exports[name] = entry
    if set(exports) != set(expected):
        raise ValueError(f"missing theorem exports: {set(expected) - set(exports)}")
    return exports


def source_hashes() -> dict[str, str]:
    paths = [ROOT / ".github/workflows/mathlib_bridge.yml"]
    for family in [*PROJECTS, "kernel_audit"]:
        directory = ROOT / "formal" / family
        paths.extend(p for p in directory.rglob("*") if p.is_file()
                     and ".lake" not in p.parts and "__pycache__" not in p.parts
                     and (p.suffix in {".lean", ".py", ".toml"}
                          or p.name in {"lean-toolchain", "lake-manifest.json"}))
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()) for p in sorted(set(paths))}


def check_dependencies(project: Path) -> dict[str, str]:
    if (project / "lean-toolchain").read_text().strip() != TOOLCHAIN:
        raise RuntimeError("toolchain pin mismatch")
    packages = json.loads((project / "lake-manifest.json").read_text())["packages"]
    revisions = {p["name"]: p["rev"] for p in packages}
    if revisions["mathlib"] != MATHLIB:
        raise RuntimeError("mathlib pin mismatch")
    for name, revision in revisions.items():
        package = project / ".lake/packages" / name
        actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=package, text=True).strip()
        dirty = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"],
                                        cwd=package, text=True).strip()
        if actual != revision or dirty:
            raise RuntimeError(f"dependency {name} is not a clean pinned tree")
    return revisions


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    receipt = output / "kernel-attestation.json"
    receipt.unlink(missing_ok=True)  # A failed rerun must not leave a stale success.
    before = source_hashes()
    version = command(["lean", "--version"], ROOT, output / "lean-version.log").strip()
    if "version 4.14.0" not in version:
        raise RuntimeError("actual compiler does not match pinned toolchain")
    exports, dependencies = {}, None
    template = (ROOT / "formal/kernel_audit/ExportCommand.lean").read_text()
    for family, (module, names) in PROJECTS.items():
        project = ROOT / "formal" / family
        pins = check_dependencies(project)
        if dependencies is not None and pins != dependencies:
            raise RuntimeError("projects must use exactly the same dependency revisions")
        dependencies = pins
        # Local theorem oleans are rebuilt; official pinned dependency cache is reused.
        shutil.rmtree(project / ".lake/build", ignore_errors=True)
        source = (project / f"{module}.lean").read_text()
        if re.search(r"\b(sorry|admit|native_decide)\b", source):
            raise RuntimeError(f"forbidden shortcut token in {family}")
        command(["lake", "build"], project, output / f"{family}-build.log")
        audit = f"import {module}\n" + template + "\n"
        for name in names:
            audit += f"#check @{name}\n#print axioms {name}\n#succ_export {name}\n"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", prefix="KernelAudit", dir=project,
                                         delete=False) as handle:
            handle.write(audit)
            audit_path = Path(handle.name)
        try:
            log = command(["lake", "env", "lean", str(audit_path)], project,
                          output / f"{family}-exports.log")
            exports.update(parse_exports(log, names))
        finally:
            audit_path.unlink()
    bridge = ROOT / "formal/mathlib_bridge"
    control = subprocess.run(["lake", "env", "lean", "controls/WrongSource.lean"], cwd=bridge,
                             text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (output / "wrong-source.log").write_text(control.stdout)
    if control.returncode == 0 or "type mismatch" not in control.stdout:
        raise RuntimeError("wrong-source control did not fail for the expected type mismatch")
    command(["python3", "check_mutations.py"], ROOT / "formal/cloud_schur",
            output / "schur-mutations.log", check_axioms=False)
    if source_hashes() != before:
        raise RuntimeError("checked source changed during build")
    environment = {"toolchain": TOOLCHAIN, "manifest_rev": MATHLIB, "source_hashes": before}
    record = {
        "schema": "succ.lean.kernel.v1", **environment,
        "environment_sha256": sha256(canonical(environment)),
        "dependency_revisions": dependencies,
        "theorem_exports": exports,
        "build": {
            "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
            "git_tree": subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip(),
            "lean_version": version,
            "negative_controls": ["wrong_source_type", "semidefinite_is_not_invertible", "wrong_negative_value"],
            "log_sha256": {p.name: sha256(p.read_bytes()) for p in sorted(output.glob("*.log"))},
        },
    }
    receipt.write_bytes(canonical(record) + b"\n")
    print(f"KERNEL_RECORD_SHA256 {sha256(receipt.read_bytes())}")
    print(f"KERNEL_RECORD_CANONICAL_SHA256 {sha256(canonical(record))}")
    print(f"KERNEL_ENVIRONMENT_SHA256 {record['environment_sha256']}")
    # Preserve a complete compact copy in retrievable job logs as well as artifact.
    # This is merely transport, not a signature or independent authentication.
    encoded = base64.b64encode(gzip.compress(receipt.read_bytes(), mtime=0)).decode()
    for index, start in enumerate(range(0, len(encoded), 12000)):
        print(f"KERNEL_RECORD_GZIP_BASE64_{index:04d} {encoded[start:start + 12000]}")
    print("UNADMITTED_BUILD_RECORD: requires independent coordinator admission, not caller JSON trust")


if __name__ == "__main__":
    main()
