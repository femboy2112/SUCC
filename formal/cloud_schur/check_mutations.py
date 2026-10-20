"""Require Lean to reject two independently false theorem mutations."""
from pathlib import Path
import subprocess
import tempfile

source = Path("CloudSchur.lean").read_text()
mutations = {
    "semidefinite_is_not_invertible": ("(hD : D.PosDef)", "(hD : D.PosSemidef)"),
    "wrong_negative_value": ("+ c = -1 := by", "+ c = 1 := by"),
}
for name, (old, new) in mutations.items():
    if source.count(old) != 1:
        raise RuntimeError(f"mutation anchor changed: {name}")
    with tempfile.NamedTemporaryFile(mode="w", suffix=".lean", dir=".", delete=False) as file:
        file.write(source.replace(old, new))
        path = Path(file.name)
    try:
        result = subprocess.run(["lake", "env", "lean", str(path)], text=True, capture_output=True)
        if result.returncode == 0 or "error:" not in result.stdout + result.stderr:
            raise RuntimeError(f"mutation did not produce an elaboration error: {name}")
        print(f"MUTATION_REJECTED {name}")
        print(result.stdout + result.stderr)
    finally:
        path.unlink()
