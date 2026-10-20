"""Reproducible exact receipts for cloud Ramanujan transport (stdout JSON)."""
from dataclasses import asdict
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.cloud_ramanujan_transport import (  # noqa: E402
    modulus_enclosure, modulus_partial_sum, modulus_tail_bound,
    prime_product, prime_product_enclosure, ramanujan_sum,
    singular_coefficient, totient,
)


def encode(value):
    if isinstance(value, Fraction):
        return {"numerator": value.numerator, "denominator": value.denominator}
    raise TypeError(type(value).__name__)


def main():
    controls = {}
    coarse = prime_product(10, 3)
    fine = prime_product_enclosure(10, 101)
    controls["omitted_divisor_breaks_naive_upper"] = {
        "N": 10, "P": 3, "naive_upper": coarse,
        "certified_larger_lower": fine.lower,
        "refuted": fine.lower > coarse,
        "repaired_enclosure": asdict(prime_product_enclosure(10, 3)),
    }
    controls["distinct_cutoffs"] = {
        "N": 2, "P": 3, "Q": 3,
        "prime_product": prime_product(2, 3),
        "modulus_sum": modulus_partial_sum(2, 3),
    }
    controls["zero_finite_identity"] = all(
        ramanujan_sum(q, 0) == totient(q) for q in range(1, 101))
    controls["fractional_cutoff_rejected"] = False
    try:
        prime_product_enclosure(2, Fraction(5, 2))
    except ValueError:
        controls["fractional_cutoff_rejected"] = True
    finite = []
    for N, Q in ((2, 61), (30, 61), (202, 61), (-42, 61), (1, 61)):
        observed = sum((abs(singular_coefficient(q, N))
                        for q in range(Q + 1, 1001)), Fraction())
        bound = modulus_tail_bound(N, Q)
        assert observed <= bound
        finite.append({"N": N, "Q": Q, "holdout_end": 1000,
                       "observed_finite_absolute_tail": observed,
                       "proved_infinite_tail_bound": bound,
                       "modulus_enclosure": modulus_enclosure(N, Q),
                       "prime_enclosure": asdict(prime_product_enclosure(N, 101))})
    files = ("observational_succ/cloud_ramanujan_transport.py",
             "tests/test_cloud_ramanujan_transport.py",
             "research/2026-10-20/CLOUD_RAMANUJAN_TRANSPORT.md",
             "scripts/cloud_ramanujan_probe.py")
    out = {
        "schema": "succ.cloud.ramanujan.receipt.v1",
        "base_sha": "0e56e0ae26f3d52a2ea34c0a4288478139fcb634",
        "claim_boundary": "Exact finite receipts; universal proofs are in the dossier; no Goldbach proof.",
        "controls": controls,
        "finite_tail_checks": finite,
        "sha256": {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in files},
    }
    print(json.dumps(out, default=encode, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
