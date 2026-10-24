"""Pinned exterior kernel observation; this does not modify the authority catalogue."""
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

project = ROOT / "formal/exterior_rigidity"
output = Path(sys.argv[1]).resolve()
output.mkdir(parents=True, exist_ok=True)
receipt = output / "exterior-kernel-observation.json"
receipt.unlink(missing_ok=True)
files = [project / n for n in ["ExteriorRigidity.lean", "lakefile.toml", "lake-manifest.json",
                              "lean-toolchain", "check.py"]]
files += [ROOT / "formal/kernel_audit/ExportCommand.lean", ROOT / "formal/kernel_audit/generate.py",
          ROOT / ".github/workflows/exterior-rigidity.yml"]


def source_hashes():
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()) for p in files}


before = source_hashes()
version = command(["lean", "--version"], project, output / "lean-version.log").strip()
if "version 4.14.0" not in version:
    raise RuntimeError("actual compiler does not match pinned toolchain")
source = (project / "ExteriorRigidity.lean").read_text()
if re.search(r"\b(sorry|admit|native_decide)\b", source):
    raise RuntimeError("forbidden proof token")
pins = check_dependencies(project)
shutil.rmtree(project / ".lake/build", ignore_errors=True)
command(["lake", "build"], project, output / "exterior-build.log")
names = ["ObservationalSUCC.ExteriorRigidity." + n for n in [
    "row_product_dvd_det", "source_sum_replacement", "source_sum_channel",
    "source_sum_scaled_channel", "row_product_dvd_natAbs", "effective_shared_prime_modulus",
    "primitive_column_forces_modulus_gcd_one", "primitive_full_product",
    "determinant_vanishes_below_modulus", "nonprimitive_shared_prime_control",
    "higher_dimensional_nonsingleton_control",
]]
audit = "import ExteriorRigidity\n" + (ROOT / "formal/kernel_audit/ExportCommand.lean").read_text()
for name in names:
    audit += f"\n#check @{name}\n#print axioms {name}\n#succ_export {name}\n"
with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", dir=project, delete=False) as handle:
    handle.write(audit)
    path = Path(handle.name)
try:
    log = command(["lake", "env", "lean", str(path)], project, output / "exterior-exports.log")
    exports = parse_exports(log, names)
finally:
    path.unlink()

controls = {
    "shared_prime_overclaim": (
        "((∏ i, d i) * q / Nat.gcd q (univ.gcd d)) ∣ A.det.natAbs := by",
        "((∏ i, d i) * q) ∣ A.det.natAbs := by",
        ("type mismatch", "unsolved goals", "tactic 'rewrite' failed")),
    "nonstrict_determinant_bound": (
        "(hbound : A.det.natAbs < E)", "(hbound : A.det.natAbs ≤ E)", ("type mismatch",)),
    "false_nonsingleton_arithmetic": (
        "(9015 : ℕ) ^ 3 < 1001 * 1002 * 2003 * 3005",
        "(9015 : ℕ) ^ 3 > 1001 * 1002 * 2003 * 3005", ("unsolved goals",)),
}
for name, (old, new, expected) in controls.items():
    if source.count(old) != 1:
        raise RuntimeError("mutation anchor missing or ambiguous: " + name)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", dir=project, delete=False) as handle:
        handle.write(source.replace(old, new))
        path = Path(handle.name)
    try:
        result = subprocess.run(["lake", "env", "lean", str(path)], cwd=project, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (output / f"{name}.log").write_text(result.stdout)
        if (result.returncode == 0 or "error:" not in result.stdout
                or not any(fragment in result.stdout for fragment in expected)):
            raise RuntimeError("mutation did not produce its expected proof error: " + name)
        print("MUTATION_REJECTED " + name)
        print(result.stdout)
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
print("EXTERIOR_RECORD_SHA256 " + sha256(receipt.read_bytes()))
encoded = base64.b64encode(gzip.compress(receipt.read_bytes(), mtime=0)).decode()
for index, start in enumerate(range(0, len(encoded), 12000)):
    print(f"EXTERIOR_RECORD_GZIP_BASE64_{index:04d} {encoded[start:start + 12000]}")
