"""Cross-check two exact implementations of one piecewise-quadratic method.

Pass the pinned #657 tests/test_borwein_bbp_sweep.py as the sole argument.
This is implementation corroboration, not an independent mathematical proof.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compare(parent_path):
    local_path = Path(__file__).with_name("borwein_probe.py")
    local = load("local_borwein_comparison", local_path)
    parent = load("parent_borwein_comparison", parent_path)
    cases = [
        ("fixed_zero", [F()]),
        ("fixed_nonzero", [F(1, 15)]),
        ("duplicates", [F(2, 7)] * 4),
        ("unequal_configuration", [F(1, 7), F(2, 5), F(5, 6)]),
    ]
    cases += [("grid_" + str(n), [F(j, n) for j in range(n)])
              for n in (3, 9)]
    cases += [("source_" + str(n), parent.shell_phases(n))
              for n in (3, 7, 15, 31)]
    rows = []
    for name, phases in cases:
        value = local.exact_sweep(local.probability(phases))[0]
        other = parent.supremum_exact(phases)
        if value != other:
            raise AssertionError((name, value, other))
        rows.append({"case": name, "equal": True, "exact_supremum": str(value)})
    return {
        "scope": "Separate implementations of the same quadratic method.",
        "parent_sha": "7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf",
        "implementation_sha256": [
            hashlib.sha256(p.read_bytes()).hexdigest()
            for p in (local_path, parent_path)
        ],
        "cases": rows,
        "pass_count": len(rows),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("parent_path", type=Path)
    args = parser.parse_args()
    print(json.dumps(compare(args.parent_path), indent=2))
