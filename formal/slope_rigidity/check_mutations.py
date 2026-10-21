"""Require actual Lean rejection of false slope propositions before admission.

The positive module is built by kernel_audit/generate.py. These temporary
mutations never enter the installed theorem environment or its export list.
"""
from pathlib import Path
import subprocess
import tempfile

source = Path("PrimitiveSlope.lean").read_text()
mutations = {
    "missing_reducedness": ("(hab' : a'.Coprime b')", "(hab' : True)"),
    "oversized_gap": ("d * e * f ≤ ((a : ℤ) * c' - (a' : ℤ) * c).natAbs :=",
                      "d * e * f + 1 ≤ ((a : ℤ) * c' - (a' : ℤ) * c).natAbs :="),
}
for name, (old, new) in mutations.items():
    if old not in source:
        raise RuntimeError("mutation anchor missing: " + name)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", dir=".", delete=False) as handle:
        handle.write(source.replace(old, new))
        path = Path(handle.name)
    try:
        result = subprocess.run(["lake", "env", "lean", str(path)], text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # Both mutations must fail because the available proof has the wrong
        # proposition. A missing import, executable or interrupted process is
        # not a successful negative control.
        if (result.returncode == 0 or "error:" not in result.stdout
                or "type mismatch" not in result.stdout):
            raise RuntimeError(f"mutation did not produce the expected type mismatch: {name}: {result.stdout}")
        print("MUTATION_REJECTED " + name)
        print(result.stdout)
    finally:
        path.unlink()
