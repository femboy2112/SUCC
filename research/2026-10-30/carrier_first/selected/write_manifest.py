"""Pin inherited source bytes, read-only dependencies and all selected artifacts."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = "1c6ce7d7ee83a0bd751bde8092e46ff798855fd3"
PARENT = "research/2026-10-30/universal_nz_carrier"
SIBLINGS = [
    ("e14916aa2b4dfc2cce948facc729fb02ce1efafa", "research/2026-10-30/carrier_adelic_transport/PRIME_FRAME_TRANSPORT.md"),
    ("e14916aa2b4dfc2cce948facc729fb02ce1efafa", "research/2026-10-30/carrier_adelic_transport/SPECTRAL_SOURCE_TRANSPORT.md"),
    ("f316d1b1e87291a89c4d4034ccf27a947e7088ad", "research/2026-10-30/fibonacci_extrusion/arithmetic/FIBONACCI_ARITHMETIC.md"),
    ("f650aab0c8710b502f3e08ec1cb2b351c26b2b3f", "research/2026-10-30/selected_finiteband/certified_band.py"),
    ("f650aab0c8710b502f3e08ec1cb2b351c26b2b3f", "research/2026-10-30/arithmetic_barrier/transfer/transfer_probe.py"),
    ("f650aab0c8710b502f3e08ec1cb2b351c26b2b3f", "research/2026-10-30/arithmetic_barrier/transfer/test_transfer.py"),
]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    inherited = []
    for p in sorted((ROOT/PARENT).rglob("*")):
        if not p.is_file() or "__pycache__" in p.parts:
            continue
        relative = str(p.relative_to(ROOT))
        old = subprocess.check_output(["git", "show", BASE+":"+relative], cwd=ROOT)
        assert old == p.read_bytes(), relative
        inherited.append(dict(commit=BASE, path=relative, sha256=sha(old)))
    siblings = []
    for commit, path in SIBLINGS:
        raw = subprocess.check_output(["git", "show", commit+":"+path], cwd=ROOT)
        siblings.append(dict(commit=commit, path=path, sha256=sha(raw)))
    receipts = []
    for p in sorted((HERE/"receipts").glob("*.json")):
        record = json.loads(p.read_text())
        if "command" not in record:
            continue
        assert "exit_code" in record, p
        assert record["exit_code"] == (1 if p.name == "signed-probe.json" else 0), p
        assert sha(p.with_suffix(".log").read_bytes()) == record["log_sha256"], p
        receipts.append(dict(path=str(p.relative_to(HERE)), exit_code=record["exit_code"]))
    artifacts = {str(p.relative_to(HERE)): sha(p.read_bytes()) for p in sorted(HERE.rglob("*"))
                 if p.is_file() and "__pycache__" not in p.parts
                 and p.name != "SOURCE_MANIFEST.json"}
    local_review = ROOT/"research/2026-10-30/carrier_first/analytic/ANALYTIC_TRANSPORT.md"
    result = dict(parent=BASE, artifacts=artifacts, sources=inherited+siblings,
                  receipts=receipts,
                  local_cross_review=dict(path=str(local_review.relative_to(ROOT)),
                                          sha256=sha(local_review.read_bytes())),
                  literature=["https://dlmf.nist.gov/3.3",
                    "https://www.colorado.edu/amath/sites/default/files/attached-files/mathcomp_88_fd_formulas.pdf"],
                  authority="local proofs and finite exact tests; same-model independent implementations; no new Lean or external referee",
                  pi_normality="OPEN", rh="OPEN")
    (HERE/"SOURCE_MANIFEST.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(dict(status="PASS", artifacts=len(artifacts), parent_files=len(inherited),
                          sibling_inputs=len(siblings), command_receipts=len(receipts),
                          expected_preserved_failures=1)))


if __name__ == "__main__":
    main()
