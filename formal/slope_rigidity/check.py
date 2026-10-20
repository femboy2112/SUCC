"""Build and audit the standalone slope project; no automatic authority admission."""
import base64
import gzip
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "formal/kernel_audit"))
from generate import canonical, check_dependencies, command, parse_exports, sha256

project = ROOT / "formal/slope_rigidity"
output = Path(sys.argv[1]).resolve()
output.mkdir(parents=True, exist_ok=True)
receipt = output / "slope-kernel-observation.json"
receipt.unlink(missing_ok=True)
files = [project / n for n in ["PrimitiveSlope.lean", "lakefile.toml", "lake-manifest.json",
                              "lean-toolchain", "check.py"]]
files += [ROOT / "formal/kernel_audit/ExportCommand.lean", ROOT / "formal/kernel_audit/generate.py",
          ROOT / ".github/workflows/slope-rigidity.yml"]


def source_hashes():
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()) for p in files}


before = source_hashes()
version = command(["lean", "--version"], project, output / "lean-version.log").strip()
if "version 4.14.0" not in version:
    raise RuntimeError("actual compiler does not match pinned toolchain")
source = (project / "PrimitiveSlope.lean").read_text()
if re.search(r"\b(sorry|admit|native_decide)\b", source):
    raise RuntimeError("forbidden proof token")
pins = check_dependencies(project)
shutil.rmtree(project / ".lake/build", ignore_errors=True)
command(["lake", "build"], project, output / "slope-build.log")
names = ["ObservationalSUCC.PrimitiveSlope." + n for n in [
    "determinant_divisibility_int", "nat_dvd_int_cast", "determinant_divisibility",
    "reduced_pair_injective", "primitive_triple_determinant_ne_zero", "modulus_le_natAbs",
    "primitive_determinant_gap", "nonprimitive_control", "noncoprime_moduli_control",
]]
audit = "import PrimitiveSlope\n" + (ROOT / "formal/kernel_audit/ExportCommand.lean").read_text()
for name in names:
    audit += f"\n#check @{name}\n#print axioms {name}\n#succ_export {name}\n"
with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", dir=project, delete=False) as handle:
    handle.write(audit)
    path = Path(handle.name)
try:
    log = command(["lake", "env", "lean", str(path)], project, output / "slope-exports.log")
    exports = parse_exports(log, names)
finally:
    path.unlink()

controls = {
    "missing_reducedness": ("(hab' : a'.Coprime b')", "(hab' : True)"),
    "oversized_gap": ("d * e * f ≤ ((a : ℤ) * c' - (a' : ℤ) * c).natAbs :=",
                      "d * e * f + 1 ≤ ((a : ℤ) * c' - (a' : ℤ) * c).natAbs :="),
}
for name, (old, new) in controls.items():
    if old not in source:
        raise RuntimeError("mutation anchor missing: " + name)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", dir=project, delete=False) as handle:
        handle.write(source.replace(old, new))
        path = Path(handle.name)
    try:
        result = subprocess.run(["lake", "env", "lean", str(path)], cwd=project, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (output / f"{name}.log").write_text(result.stdout)
        if result.returncode == 0 or "error:" not in result.stdout:
            raise RuntimeError("mutation was not rejected by elaboration: " + name)
        print("MUTATION_REJECTED " + name)
    finally:
        path.unlink()

if source_hashes() != before:
    raise RuntimeError("checked source changed during build")
record = {
    "schema": "succ.lean.research.v1",
    "status": "KERNEL_CHECKED_NOT_AUTHORITY_ADMITTED",
    "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
    "toolchain": (project / "lean-toolchain").read_text().strip(),
    "lean_version": version,
    "dependency_revisions": pins,
    "source_hashes": before,
    "theorem_exports": exports,
    "negative_controls": list(controls),
    "log_sha256": {p.name: sha256(p.read_bytes()) for p in sorted(output.glob("*.log"))},
}
receipt.write_bytes(canonical(record) + b"\n")
print("SLOPE_RECORD_SHA256 " + sha256(receipt.read_bytes()))
encoded = base64.b64encode(gzip.compress(receipt.read_bytes(), mtime=0)).decode()
for index, start in enumerate(range(0, len(encoded), 12000)):
    print(f"SLOPE_RECORD_GZIP_BASE64_{index:04d} {encoded[start:start + 12000]}")
