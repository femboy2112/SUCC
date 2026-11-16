"""Exact finite controls for shared-carrier coding and arithmetic coupling.

These are finite falsifiers/calibrations, not a universal Goldbach proof.
Entropy calculations deliberately accept only probabilities that are powers
of two, so all reported bit counts are exact rational numbers.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from math import factorial, prod
from pathlib import Path
from random import Random

from cylinder import omega
import prime_observer as po

PARENT_COMMIT = "836d03806183c1f73488dca1d37e149a9826eb53"


def entropy_dyadic(events: list) -> Fraction:
    if not events:
        raise ValueError("nonempty uniform event list required")
    answer = Fraction(0)
    for count in Counter(events).values():
        p = Fraction(count, len(events))
        a, b = p.numerator, p.denominator
        if a & (a - 1) or b & (b - 1):
            raise ValueError("this exact probe supports power-of-two probabilities")
        answer += p * (b.bit_length() - a.bit_length())
    return answer


def carrier_statistics(rows: list[tuple[object, tuple]]) -> dict:
    """Rows are equiprobable draws of (carrier, observed tuple)."""
    carriers = [c for c, _ in rows]
    observations = [x for _, x in rows]
    if not rows or len({len(x) for x in observations}) != 1:
        raise ValueError("nonempty observations of a fixed arity required")
    arity = len(observations[0])
    hc, hx = entropy_dyadic(carriers), entropy_dyadic(observations)
    hcx = entropy_dyadic(rows)
    separate = sum((entropy_dyadic([x[i] for x in observations])
                    for i in range(arity)), Fraction(0))
    conditional_sum = sum(
        (entropy_dyadic([(c, x[i]) for c, x in rows]) - hc
         for i in range(arity)), Fraction(0))
    return {
        "joint_bits": hx, "separate_bits": separate, "carrier_bits": hc,
        "conditional_local_bits": conditional_sum,
        "carrier_code_bits": hc + conditional_sum,
        "total_correlation": separate - hx,
        "extra_carrier_bits": hcx - hx,
        "residual_total_correlation": conditional_sum - (hcx - hc),
        "gain_over_separate": separate - hc - conditional_sum,
        "all_one_probability": Fraction(
            sum(all(v == 1 for v in x) for x in observations), len(rows)),
    }


def joint_source(window: int, *, transported: bool = False) -> dict:
    po.integer(window, 2)
    if type(transported) is not bool:
        raise ValueError("transported must be boolean")
    return {(n, omega(po.relabel(n) if transported else n)): 1
            for n in range(2, window + 1)}


def polynomial_square(source: dict, sum_bound: int) -> dict:
    """Integer bivariate Cauchy square, retaining position up to sum_bound."""
    po.integer(sum_bound, 0)
    for (position, degree), coefficient in source.items():
        for value in (position, degree, coefficient):
            po.integer(value, 0)
    result = Counter()
    for (a, r), x in source.items():
        for (b, s), y in source.items():
            if a + b <= sum_bound:
                result[a + b, r + s] += x * y
    return {key: value for key, value in result.items() if value}


def histogram(source: dict) -> dict:
    result = Counter()
    for (_, degree), coefficient in source.items():
        result[degree] += coefficient
    return dict(sorted(result.items()))


def run_probe() -> dict:
    checks = Counter()

    def require(condition: bool, group: str) -> None:
        checks[group] += 1
        if not condition:
            raise AssertionError(f"carrier probe failed: {group}")

    bits = tuple(product((0, 1), repeat=2))
    cases = {
        "shared": [(b, (b, b)) for b in (0, 1)],
        "opposite": [(b, (b, 1 - b)) for b in (0, 1)],
        "independent": [(0, (a, b)) for a, b in bits],
        "unexplained": [(0, (b, b)) for b in (0, 1)],
        "bloated": [((b, u, v), (b, b))
                    for b, u, v in product((0, 1), repeat=3)],
        "parity": [((a, b), (a, b, a ^ b)) for a, b in bits],
    }
    stats = {name: carrier_statistics(rows) for name, rows in cases.items()}
    # Expected (joint, separate, carrier code, extra carrier, residual TC).
    expected = {
        "shared": (1, 2, 1, 0, 0), "opposite": (1, 2, 1, 0, 0),
        "independent": (2, 2, 2, 0, 0), "unexplained": (1, 2, 2, 0, 1),
        "bloated": (1, 2, 3, 2, 0), "parity": (2, 3, 2, 0, 0),
    }
    keys = ("joint_bits", "separate_bits", "carrier_code_bits",
            "extra_carrier_bits", "residual_total_correlation")
    for name, row in stats.items():
        require(tuple(row[k] for k in keys) == expected[name], "entropy_controls")
        require(row["carrier_code_bits"] - row["joint_bits"] ==
                row["extra_carrier_bits"] + row["residual_total_correlation"],
                "carrier_cost_identity")
    require(stats["shared"]["all_one_probability"] == Fraction(1, 2) and
            stats["opposite"]["all_one_probability"] == 0,
            "orientation_counterexample")
    parity = [x for _, x in cases["parity"]]
    for i, j in ((0, 1), (0, 2), (1, 2)):
        mutual = (entropy_dyadic([x[i] for x in parity]) +
                  entropy_dyadic([x[j] for x in parity]) -
                  entropy_dyadic([(x[i], x[j]) for x in parity]))
        require(mutual == 0, "pairwise_blindness")
    try:
        entropy_dyadic([0, 1, 2])
    except ValueError:
        require(True, "entropy_precision_guard")
    else:
        require(False, "entropy_precision_guard")

    # Independent source algorithms: trial-factor degree versus marking sieve.
    bound = 512
    square = polynomial_square(joint_source(bound), bound)
    flags = po.sieve_mask(bound)
    for n in range(4, bound + 1):
        direct = sum(flags[a] * flags[n - a] for a in range(2, n - 1))
        require(square.get((n, 2), 0) == direct, "joint_coefficient_vs_sieve")
    for n in (4, 6, 7, 20, 68, 100, 256):
        target = square.get((n, 2), 0)
        for aperture in (n - 2, n - 1, n, n + 13):
            observed = polynomial_square(joint_source(aperture), n)
            require(observed.get((n, 2), 0) == target, "finite_horizon")
    require(polynomial_square(joint_source(4), 7).get((7, 2), 0) == 0 and
            polynomial_square(joint_source(5), 7).get((7, 2), 0) == 2,
            "premature_prefix_control")

    ordinary = joint_source(98)
    counterfeit = joint_source(98, transported=True)
    expected_histogram = {1: 25, 2: 34, 3: 21, 4: 11, 5: 4, 6: 2}
    require(histogram(ordinary) == histogram(counterfeit) == expected_histogram,
            "same_spectrum")
    ordinary_count = polynomial_square(ordinary, 100).get((100, 2), 0)
    fake_count = polynomial_square(counterfeit, 100).get((100, 2), 0)
    require((ordinary_count, fake_count) == (12, 0), "different_embedding")
    for aperture in (98, 99, 100, 128, 256):
        result = polynomial_square(joint_source(aperture, transported=True), 100)
        require(result.get((100, 2), 0) == 0, "permanent_source_defect")
    for seed in range(8):
        order = list(range(2, 129))
        Random(seed).shuffle(order)
        last_needed = max(order.index(n) for n in range(2, 99))
        prefix = {(n, omega(n)): 1 for n in order[:last_needed + 1]}
        require(polynomial_square(prefix, 100).get((100, 2), 0) == 12,
                "fair_order_control")

    tiny = joint_source(3)
    difference = Counter((a - b, r - s) for a, r in tiny for b, s in tiny)
    require(polynomial_square(tiny, 6).get((6, 2), 0) == 1 and
            difference.get((6, 2), 0) == 0, "square_not_absolute_square")
    unit_source = {**joint_source(9), (1, 0): 1}
    require(polynomial_square(unit_source, 10).get((10, 2), 0) -
            polynomial_square(joint_source(9), 10).get((10, 2), 0) == 2,
            "unit_contamination")

    transported_mult = lambda m, n: po.relabel(po.relabel(m) * po.relabel(n))
    require(transported_mult(2, 1) == 2, "transport_preserves_anchor")
    require((transported_mult(2, 9), transported_mult(2, 8) + 2) == (106, 18),
            "transport_breaks_braid")
    shifted_mult = lambda m, n: m * (n - 1) + 1
    for m in (2, 3, 5):
        require(shifted_mult(m, 1) != m, "anchor_is_necessary")
        for n in range(1, 17):
            require(shifted_mult(m, n + 1) == shifted_mult(m, n) + m,
                    "anchor_free_braid")
            require(shifted_mult(m, shifted_mult(3, n)) ==
                    shifted_mult(3 * m, n), "anchor_free_composition")
    transported_count = sum(
        omega(po.relabel(n)) == 1 and
        omega(po.relabel(po.relabel(100 - po.relabel(n)))) == 1
        for n in range(2, 99))
    require(transported_count == 12, "coherent_transport_preserves_count")

    phases = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for n in range(1, 17):
        real, imag = phases[(n - 1) % 4]
        error_squared = (real - 1) ** 2 + imag ** 2
        require(error_squared <= 2 * (n - 1) ** 2, "approximate_braid_bound")

    allocations = factorial(97) // prod(factorial(c) for c in expected_histogram.values())
    require(allocations > 1, "histogram_assignment_count")
    here = Path(__file__).resolve().parent
    hashes = {name: hashlib.sha256((here / name).read_bytes()).hexdigest()
              for name in ("carrier_probe.py", "cylinder.py", "prime_observer.py")}
    return {
        "schema": "shared-carrier-v1", "parent_commit": PARENT_COMMIT,
        "checks": dict(sorted(checks.items())), "total_checks": sum(checks.values()),
        "failures": 0, "entropy_units": "exact rational bits",
        "entropy_controls": stats,
        "joint_coefficient_targets": {"min": 4, "max": bound, "all_integers": True},
        "histogram": expected_histogram,
        "ordinary_sum100": ordinary_count, "transported_sum100": fake_count,
        "coherently_transported_sum100": transported_count,
        "histogram_assignment_control": {
            "labels": 97, "number_of_assignments": str(allocations),
            "conditional_entropy_if_uniform": f"log2({allocations})",
            "fixed_width_bits_required": (allocations - 1).bit_length(),
            "is_lower_bound_for_actual_arithmetic_description": False,
        },
        "source_sha256": hashes, "goldbach_proved": False,
        "all_object_based_proofs_ruled_out": False,
        "universal_compression_advantage_claimed": False,
        "finite_computation_proves_universal_claims": False,
    }


if __name__ == "__main__":
    receipt = run_probe()
    output = Path(__file__).resolve().parent / "receipts/CARRIER_REPORT.json"
    output.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n")
    print(json.dumps({"checks": receipt["total_checks"], "failures": 0,
                      "ordinary_sum100": receipt["ordinary_sum100"],
                      "transported_sum100": receipt["transported_sum100"],
                      "receipt": str(output)}, indent=2))
