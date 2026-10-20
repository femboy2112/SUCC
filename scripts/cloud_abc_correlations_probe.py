#!/usr/bin/env python3
"""Reproduce the cloud ABC exact receipt; never promotes tests to a theorem."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.cloud_abc_correlations import (  # noqa: E402
    moment_budget, powerful_singleton_witness, triple_expansion,
)
from observational_succ.abc_triple_moment import S_t_enclosure  # noqa: E402
from fractions import Fraction  # noqa: E402


def main() -> int:
    command = [sys.executable, "-m", "unittest", "discover", "-s", "tests",
               "-p", "test_cloud_abc_correlations.py", "-v"]
    test = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    budgets = {}
    for t in (Fraction(1, 2), Fraction(3, 5), Fraction(13, 20)):
        b = moment_budget(t)
        budgets[str(t)] = {
            "delta": str(b.delta), "eta": str(b.eta),
            "low_power_of_two_exponent": b.low_power,
            "tail_power_of_two_exponent": b.tail_power,
            "tail_coefficient": str(2 / b.delta),
            "exponent_balance": str(2 + 2*b.eta + b.t-Fraction(2, 3)),
        }
    files = ["observational_succ/cloud_abc_correlations.py",
             "tests/test_cloud_abc_correlations.py",
             "scripts/cloud_abc_correlations_probe.py",
             "research/2026-10-20/CLOUD_ABC_CORRELATIONS.md"]
    receipt = {
        "parent_sha": "0e56e0ae26f3d52a2ea34c0a4288478139fcb634",
        "lane": "B", "theorem_scope": "all real X>=2 and all real 0<=t<2/3",
        "universal_authority": "paper proof in Sections 2-6; not finite tests",
        "formal_verification": "NOT RUN; no Lean artifact in lane B",
        "mean_value_theorem": "S_t(X)/X^2 tends to (2*zeta(2))^-1 prod_p(1+3p/(p+1)A_p(t)), 0<=t<2/3",
        "development_correction": "First local-density test used handwritten 1/2700 for moduli(4,9,25); exact product and residue census give1/2160. Expected test value corrected; implementation unchanged.",
        "academic_originality": "UNVERIFIED; new-to-project elementary synthesis",
        "test_command": "python -m unittest discover -s tests -p test_cloud_abc_correlations.py -v",
        "test_exit_code": test.returncode,
        "test_output": test.stdout + test.stderr,
        "files_sha256": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in files},
        "powerful_singleton_counterexample": powerful_singleton_witness(),
        "nonprimitive_packing_counterexample": {
            "X": 34, "moduli": [8, 9, 17], "triples": [[8, 9, 17], [16, 18, 34]],
            "packing_majorant": "35/18", "actual_nonprimitive_count": 2,
        },
        "integer_expansion_anchor": {"X": 24, "t": 1, "value": triple_expansion(24, 1)},
        "rational_moment_observation": {
            "X": 64, "t": "1/2",
            "interval": [str(x) for x in S_t_enclosure(64, Fraction(1, 2), precision=10**6)],
            "status": "finite observation, not universal verification",
        },
        "constant_certificates": budgets,
        "primary_source_comparison": {
            "url": "https://arxiv.org/html/2410.12234v2",
            "version_date": "2026-05-09", "retrieved": "2026-10-20",
            "imported_as_theorem_dependency": False,
        },
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return test.returncode


if __name__ == "__main__":
    raise SystemExit(main())
