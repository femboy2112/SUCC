"""Compare the independent SymPy receipt with the Fraction implementation.

This is a bridge between two implementations, not another independent derivation.
Run source_independent_audit.py first when regenerating its source receipt.
"""
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import source_acquisition as acquisition


def scalar_text(value):
    value = Fraction(value)
    return f"{value.numerator}/{value.denominator}"


def matrix_digest(value):
    rows = [[scalar_text(x) for x in row] for row in value]
    return sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def main():
    here = Path(__file__).resolve().parent
    receipt = json.loads((here / "receipts/source_independent_audit.json").read_text())
    assert receipt["status"] == "PASS"
    for name, key in [("source_acquisition.py", "source_acquisition_sha256"),
                      ("source_independent_audit.py", "audit_script_sha256")]:
        assert sha256((here / name).read_bytes()).hexdigest() == receipt[key], name
    comparisons = []
    for row in receipt["schedules"]:
        times = tuple(row["times"])
        raw = acquisition.sampling_matrix(times)
        inv = acquisition.inverse(raw)
        block = acquisition.block_matrix(times)
        assert matrix_digest(raw) == row["raw_sampling_matrix_sha256"], times
        assert matrix_digest(inv) == row["raw_inverse_sha256"], times
        for value, key in [(acquisition.determinant(raw), "raw_determinant"),
                           (acquisition.determinant(block), "normalized_block_determinant")]:
            assert sha256(scalar_text(value).encode()).hexdigest() == row[key]["sha256"], (times, key)
        comparisons.append({"times": list(times), "exact_matrix_matches": 2,
                            "exact_determinant_matches": 2})
    print(json.dumps({"status": "PASS", "arithmetic": "Fraction versus independent SymPy",
                      "schedules": comparisons, "matrix_matches": 2 * len(comparisons),
                      "determinant_matches": 2 * len(comparisons),
                      "audited_source_hashes_match": True,
                      "scope": "Finite cross-implementation agreement, not source authentication."},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
