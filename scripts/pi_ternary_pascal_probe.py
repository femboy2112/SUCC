#!/usr/bin/env python3
"""Exact source, carry, and adversarial receipts for weighted ternary Pascal."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ.bbp_two_adic import rational_mod
from observational_succ.pi_pascal_source import difference_valuation, rational_valuation
from observational_succ.pi_ternary_pascal import (
    FILTERS, alternating_words, ambiguous_cylinders, base81_reset_forcing,
    base81_reset_mahler, base81_reset_source, bernoulli_multiplied_half,
    dyadic_filtered_mod, dyadic_mahler, endpoint_denominator_possible,
    filter_error_interval, filtered_source, local_transport, phase_from_cover,
    source_states, ternary4_lift,
)
from scripts.pi_pascal_probe import machin_interval, rational_receipt

COUNTS = Counter()


def require(group, condition):
    if not condition:
        raise AssertionError(group)
    COUNTS[group] += 1


def original_values(last):
    values = [Q()]
    for n in range(1, last+1):
        r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        values.append(16*values[-1]+r)
    return values


def difference(values, start, order):
    return sum((comb(order, i)*(-1)**(order-i)*values[start+i]
                for i in range(order+1)), Q())


def run():
    COUNTS.clear()
    started = time.monotonic()
    values = original_values(220)
    alpha = tuple(x/16 for x in machin_interval(256))
    require("literal_source", tuple(values) == source_states(220))
    for k in range(97):
        require("weighted_row", sum(comb(k, j)*2**j for j in range(k+1)) == 3**k)

    calibration = [(n, k) for n in range(9) for k in range(1, 25)]
    extended = [(n, k) for n in (19, 31, 64) for k in range(25, 73)]
    for kind in ("ternary4", "base81"):
        sequence = [ternary4_lift(k) if kind == "ternary4"
                    else filtered_source(kind, k) for k in range(137)]
        for label, cases in (("calibration", calibration), ("extended", extended)):
            for n, k in cases:
                require(label+"_"+kind+"_difference_profile",
                        rational_valuation(difference(sequence, n, k)) == difference_valuation(k))
        for k, coefficient in enumerate(dyadic_mahler(kind, 96)[1:], 1):
            require(kind+"_mahler", rational_valuation(coefficient) == difference_valuation(k))
        for bits in range(1, 11):
            residues = [dyadic_filtered_mod(kind, n, bits) for n in range(2**bits)]
            require(kind+"_permutation", sorted(residues) == list(range(2**bits)))
        for k in range(1, 97):
            require(kind+"_origin_valuation", rational_valuation(sequence[k]) == rational_valuation(Q(k)))
            require(kind+"_modular_readout", dyadic_filtered_mod(kind, k, 64) == rational_mod(sequence[k], 64))

    kernel_cases = [(n, k) for n in (0, 4, 8) for k in range(25)]
    kernel_cases += [(n, k) for n in (19, 31, 64) for k in (25, 31, 41, 56, 72)]
    for name in FILTERS:
        q = FILTERS[name][2]
        for n, k in kernel_cases:
            value = filtered_source(name, k, n)
            sign = (-1)**k if name in ("ternary4", "ternary5") else 1
            oracle = sorted(sign*(q**k*16**n*a-value) for a in alpha)
            lower, upper = filter_error_interval(name, k, n, terms=5)
            require(name+"_machin_kernel", 0 < lower < oracle[0] < oracle[1] < upper)
        for n in range(97):
            transformed, q, error = local_transport(name, n)
            require(name+"_local_transport", transformed-q*values[n] == error > 0)
        for k in range(1, 49):
            transformed = filtered_source(name, k)
            b = FILTERS[name][1]**k
            h = b*transformed
            floor = h.numerator//h.denominator
            require(name+"_carry", phase_from_cover(h % 1, floor % b, b) == transformed % 1)

    for n in (0, 1, 2, 3, 8, 19):
        require("reset_initial", base81_reset_source(n, 0) == 0)
        for k in range(1, 49):
            require("reset_mahler", rational_valuation(base81_reset_mahler(n, k)) == difference_valuation(k))
            f = base81_reset_forcing(n, k-1)
            require("reset_recurrence", base81_reset_source(n, k)-81*base81_reset_source(n, k-1) == f > 0)
        f0, f1 = base81_reset_forcing(n, 0), base81_reset_forcing(n, 1)
        require("forcing_profile_differs", rational_valuation(f1-f0) == 2)

    for m in range(1, 65):
        for b in (1, 2):
            require("all_ternary_powers_small_denominator_excluded",
                    not endpoint_denominator_possible(3**m, b))
        require("denominator3_endpoint_cycle", endpoint_denominator_possible(3**m, 3) == (m % 4 == 0))

    for m in range(1, 8):
        for L in range(2, 11):
            expected = {prefix*2**L+s for prefix in range(2**m) for s in alternating_words(L)}
            actual = ambiguous_cylinders(3, m, L)
            require("alternating_cylinders", set(actual) == expected)
            require("alternating_mass_Haar", Q(len(actual), 2**(m+L)) == Q(2, 2**L))
    for q in (3, 5, 7, 11, 13, 17, 31, 81):
        for m in range(1, 7):
            L = q.bit_length()+2
            require("odd_multiplier_cylinders", len(ambiguous_cylinders(q, m, L)) == (q-1)*2**m)

    bias = Q(1, 4)
    require("positive_dimension_noninvariance", bernoulli_multiplied_half(3, bias) == Q(33, 52))
    require("base81_noninvariance", bernoulli_multiplied_half(81, bias) != Q(3, 4))
    require("dropped_carry_mutant", filtered_source("ternary4", 1) % 1-(values[1] % 1)/4 == Q(3, 4))
    require("odd_sign_mutant", filtered_source("ternary4", 7) > 3**7*alpha[1])
    positive_bad = filter_error_interval("positive8", 128, terms=5)
    require("positive_pascal_growing_error", positive_bad[0] > 1)

    rows = []
    for k in (4, 16, 32, 64):
        rows.append({"ternary_depth": 4*k,
                     "quarter_cover": str(4**(4*k)),
                     "older_cover": str(5**(4*k)),
                     "base81_cover": str(3**k),
                     "quarter_error": [rational_receipt(x) for x in filter_error_interval("ternary4", 4*k, terms=5)],
                     "base81_origin_error": [rational_receipt(x) for x in filter_error_interval("base81", k, terms=5)],
                     "base81_shift2_error": [rational_receipt(x) for x in filter_error_interval("base81", k, 2, terms=5)]})
    inputs = ["observational_succ/pi_ternary_pascal.py", "tests/test_pi_ternary_pascal.py",
              "scripts/pi_ternary_pascal_probe.py", "scripts/pi_ternary_carry_calibration.py",
              "observational_succ/pi_pascal_kernel.py", "observational_succ/pi_pascal_source.py",
              "scripts/pi_pascal_probe.py", "research/2026-10-24/PI_TERNARY_HOLE_CONTRACT.md",
              "research/2026-10-24/PI_TERNARY_CONSTRUCTOR.md",
              "research/2026-10-24/PI_TERNARY_TRANSLATOR.md",
              "research/2026-10-24/PI_TERNARY_ADVERSARY.md"]
    return {"status": "EXACT_FINITE_PASSED", "assertions": sum(COUNTS.values()),
            "counts": dict(sorted(COUNTS.items())), "elapsed_seconds": time.monotonic()-started,
            "parent": "6e8fa8b77886b13f1f533ed8083fd88c849d14b3",
            "ranges": {"difference_calibration": "starts0..8,orders1..24",
                       "difference_extended": "starts19,31,64,orders25..72",
                       "kernel_calibration": "starts0,4,8,orders0..24",
                       "kernel_extended": "starts19,31,64,orders25,31,41,56,72",
                       "mahler_origin": "orders1..96", "permutations": "moduli2..1024"},
            "split_boundary": "Extended independent-oracle region, not an untouched statistical holdout; constructor explored some overlapping valuations before registration.",
            "comparison_rows": rows,
            "controls": {"biased_binary_half": "3/4", "tripled_half": "33/52",
                         "base81_half": rational_receipt(bernoulli_multiplied_half(81, bias)),
                         "positive8_order128_error": [rational_receipt(x) for x in positive_bad]},
            "source_hashes": {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            "unproved": ["authentic real collision exponent", "same-law tripling orbase81 symmetry", "pi normality"]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in ("status", "assertions", "elapsed_seconds")}))


if __name__ == "__main__":
    main()
