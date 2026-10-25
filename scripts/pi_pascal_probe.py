#!/usr/bin/env python3
"""Reproducible exact, held-out probes for the Pascal/BBP research round.

All decisions use integers and Fractions. Decimal strings are outward-rounded
display only. The Machin enclosure is an independent real oracle; no pi digits
enter any source or countermodel construction. See the frozen hole contract.
"""
from __future__ import annotations

import argparse
from collections import Counter
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial, isqrt, lcm
from pathlib import Path
import platform
import time

from observational_succ.bbp_two_adic import particular_mod, rational_mod
from observational_succ.pi_pascal_source import (
    POLES, difference_valuation, forcing_difference, mahler_coefficients,
    minimal_mahler_degree, newton_mod, odd_pole_counts, odd_pole_valuation,
    rational_valuation, reciprocal_difference, source_difference_mod,
)
from observational_succ.pi_pascal_kernel import (
    absolute_shadow_endpoint_obstructions, coherent_filter_degree,
    filter_carry_modulus, filtered_phase_from_carry,
    forcing_pascal_beta_bounds, forcing_pascal_moment,
    pascal_pi_interval, rational_filter_coefficients,
    scaled_pascal_error_interval, scaled_pascal_forcing, scaled_pascal_source,
    source_pascal_row, tail_pascal_interval,
)
from observational_succ.pi_pascal_controls import (
    pascal_endpoint_budget, pascal_window_average, positive_moment_countermodel,
    valuation_two,
)


ROOT = Path(__file__).resolve().parents[1]
COUNTS: Counter = Counter()


def require(group, condition):
    if not condition:
        raise AssertionError(group)
    COUNTS[group] += 1


def forcing_original(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def original_values(last):
    result = [Q()]
    for n in range(1, last+1):
        result.append(16*result[-1]+forcing_original(n))
    return result


def difference(values, start, order):
    return sum(((-1)**(order-j)*comb(order, j)*values[start+j]
                for j in range(order+1)), Q())


def function_difference(function, start, order):
    return sum(((-1)**(order-j)*comb(order, j)*function(start+j)
                for j in range(order+1)), Q())


def rational_receipt(value):
    value = Q(value)
    n = abs(value.numerator)
    nb = n.to_bytes(max(1, (n.bit_length()+7)//8), "big")
    d = value.denominator
    db = d.to_bytes(max(1, (d.bit_length()+7)//8), "big")
    encoded = (b"-" if value < 0 else b"+") + len(nb).to_bytes(8, "big") + nb + db
    bounds = []
    for rounding in (ROUND_FLOOR, ROUND_CEILING):
        with localcontext() as context:
            context.prec = 22
            context.rounding = rounding
            bounds.append(str(Decimal(value.numerator)/Decimal(d)))
    return {"sign": (value > 0)-(value < 0), "numerator_bits": n.bit_length(),
            "denominator_bits": d.bit_length(), "sha256_binary_rational": sha256(encoded).hexdigest(),
            "outward_decimal": bounds}


def interval_receipt(interval):
    return [rational_receipt(x) for x in interval]


def arctangent_interval(reciprocal, terms):
    value = sum((Q((-1)**j, (2*j+1)*reciprocal**(2*j+1))
                 for j in range(terms)), Q())
    error = Q(1, (2*terms+1)*reciprocal**(2*terms+1))
    return (value, value+error) if terms % 2 == 0 else (value-error, value)


def machin_interval(terms=256):
    a, b = arctangent_interval(5, terms), arctangent_interval(239, terms)
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


def scale_interval(interval, multiplier):
    result = tuple(multiplier*x for x in interval)
    return result if multiplier >= 0 else result[::-1]


def convolution(left, right):
    answer = [Q()]*(len(left)+len(right)-1)
    for j, a in enumerate(left):
        for k, b in enumerate(right):
            answer[j+k] += a*b
    return tuple(answer)


def recurrence_coefficients(k):
    """Literal displayed polynomial coefficients, not imported evaluators."""
    return ((8*k+1)*(2*k+1)*(8*k+5)*(4*k+3),
            -2048*k**4-400*k*k+6*k,
            24*k*(k-1)*(128*k*k-128*k+51),
            -2048*k*(k-1)**2*(k-2),
            512*k*(k-1)*(k-2)*(k-3))


def run():
    COUNTS.clear()
    started = time.monotonic()
    values = original_values(192)
    pi_interval = machin_interval()
    alpha = tuple(x/16 for x in pi_interval)
    calibration = [(n, k) for n in range(17) for k in range(1, 17)]
    held_out = [(n, k) for n in (19, 31, 64, 127) for k in range(17, 41)]
    for label, cases in (("calibration", calibration), ("held_out", held_out)):
        for n, k in cases:
            direct_r = function_difference(forcing_original, n, k)
            direct_u = difference(values, n, k)
            require(label+"_forcing_product", forcing_difference(n, k) == direct_r)
            require(label+"_forcing_valuation", rational_valuation(direct_r) == difference_valuation(k))
            require(label+"_source_valuation", rational_valuation(direct_u) == difference_valuation(k))
            require(label+"_source_correction", rational_valuation(direct_u-direct_r) == difference_valuation(k)+4)
            moment = forcing_pascal_moment(n, k)
            require(label+"_beta_original", moment == (-1)**k*function_difference(forcing_original, n+1, k))
            lower, upper = forcing_pascal_beta_bounds(n, k)
            require(label+"_beta_bounds", lower < moment < upper)
            raw = tuple(16**n*15**k*x-direct_u for x in alpha)
            independent = scale_interval(raw, (-1)**k)
            enclosure = tail_pascal_interval(n, k, terms=5)
            require(label+"_machin_tail", enclosure[0] < independent[0] < independent[1] < enclosure[1])

    for start in (Q(-3), Q(-1), Q(1, 3), Q(7, 5), Q(-2, 7)):
        for k in range(1, 25):
            exact = function_difference(forcing_original, start, k)
            require("rational_start_product", exact == forcing_difference(start, k))
            require("rational_start_valuation", rational_valuation(exact) == difference_valuation(k))

    degree_table = []
    for bits in (1, 2, 4, 8, 16, 32, 64, 128, 256):
        degree = minimal_mahler_degree(bits)
        require("minimal_degree_threshold", difference_valuation(degree) < bits <= difference_valuation(degree+1))
        coefficients = mahler_coefficients("source", degree+1)
        at_next = sum((coefficients[k]*comb(degree+1, k) for k in range(degree+1)), Q())
        error = values[degree+1]-at_next
        require("minimax_sharpness", error == coefficients[degree+1]
                and rational_valuation(error) == difference_valuation(degree+1))
        at_degree = sum((coefficients[k]*comb(degree, k) for k in range(degree)), Q())
        require("lower_degree_fails", rational_valuation(values[degree]-at_degree) < bits)
        for n in (0, 1, 17, 63, 127):
            require("newton_original", newton_mod(n, bits) == rational_mod(values[n], bits))
        for n in (-37, -1, 1009):
            require("newton_backwards", newton_mod(n, bits) == particular_mod(n, bits))
        degree_table.append({"bits": bits, "minimal_degree": degree})
    for n in (-37, -1, 19, 127):
        for k in (1, 4, 17, 40):
            bits = difference_valuation(k)+6
            observed = source_difference_mod(n, k, bits)
            require("backwards_difference_valuation", rational_valuation(observed) == difference_valuation(k))

    n, bits = 128, 16
    degree = minimal_mahler_degree(bits)
    polynomial = sum((a*comb(n, k) for k, a in enumerate(mahler_coefficients("source", degree))), Q())
    ratio = abs(polynomial)/values[n]
    bound = Q(16*(degree+1)*(17*n)**degree, 15*16**n)
    require("crossnorm_congruence", rational_mod(polynomial, bits) == rational_mod(values[n], bits))
    require("crossnorm_smallness", ratio <= bound < Q(1, 2**400))
    phase_gap = (polynomial-values[n]) % 1
    phase_gap = min(phase_gap, 1-phase_gap)
    require("crossnorm_real_phase_gap", phase_gap > Q(1, 16))
    crossnorm = {"index": n, "bits": bits, "degree": degree,
                 "real_relative_size": rational_receipt(ratio),
                 "proved_bound": rational_receipt(bound),
                 "circle_distance": rational_receipt(phase_gap)}

    for p in (3, 5, 7, 11, 13):
        for start in (0, 1, 19, 127):
            for k in (1, 7, 17, 40):
                for slope, offset, weight in POLES:
                    exact = reciprocal_difference(start, k, slope, offset)
                    require("odd_pole_valuation", rational_valuation(exact, p) == odd_pole_valuation(start, k, slope, offset, p))
                    require("odd_pole_counts", all(count-fact in (0, 1) for _, count, fact in
                                                   odd_pole_counts(start, k, slope, offset, p)))
    cancellation = {"prime": 3, "start": 0, "order": 1,
                    "weighted_pole_valuations": [rational_valuation(w*reciprocal_difference(0, 1, a, b), 3)
                                                  for a, b, w in POLES],
                    "sum": str(forcing_difference(0, 1)),
                    "sum_valuation": rational_valuation(forcing_difference(0, 1), 3)}
    require("odd_cancellation_retained", cancellation["weighted_pole_valuations"] == [0, -1, 0, -1]
            and cancellation["sum"] == "83/35" and cancellation["sum_valuation"] == 0)

    filters = []
    for q in (2, 3, 5, 7, 11, 13, 15, 16, 17, 31):
        d = coherent_filter_degree(q)
        if q == 15:
            d = 1  # critical error case, distinct from the coherent family
        for k in (1, 2, 4, 8, 16, 32):
            a = difference(values, 0, d*k)
            x = scaled_pascal_source(q, d, k)
            scale = Q(q, 15**d)**k
            require("filter_literal_source", x == scale*a)
            error_interval = scaled_pascal_error_interval(q, d, k, terms=5)
            independent = scale_interval(tuple(q**k*t-x for t in alpha), (-1)**(d*k))
            require("filter_machin_error", error_interval[0] < independent[0] < independent[1] < error_interval[1])
            modulus = filter_carry_modulus(q, d, k)
            carry = a.__floor__() % modulus
            require("filter_carry_readout", filtered_phase_from_carry(a % 1, carry, q, d, k) == x % 1)
            next_x = scaled_pascal_source(q, d, k+1)
            require("filter_forcing", next_x-q*x == scaled_pascal_forcing(q, d, k))
            require("filter_forcing_sign", (-1)**(d*k)*scaled_pascal_forcing(q, d, k) > 0)
            direct_tail = tuple(16**(d*k)*t-values[d*k] for t in alpha)
            direct_error = scale_interval(direct_tail, Q(q, 16**d)**k)
            require("direct_better_on_probe", 0 < direct_error[0] < direct_error[1] < error_interval[0])
            if k in (1, 8, 32):
                filters.append({"multiplier": q, "degree": d, "order": k,
                                "pascal_carry_modulus": str(modulus),
                                "direct_carry_modulus": str(Q(q, 16**d).denominator**k),
                                "pascal_error": interval_receipt(error_interval),
                                "direct_error": interval_receipt(direct_error)})
        if q != 15:
            for r in (2, 3, 5):
                e = coherent_filter_degree(r)
                require("operator_composition", convolution(rational_filter_coefficients(q, d), rational_filter_coefficients(r, e))
                        == rational_filter_coefficients(q*r, d+e))
                require("additive_degree", coherent_filter_degree(q*r) == d+e)
    for q in (2, 3, 5):
        d = coherent_filter_degree(q)
        for power in (2, 4):
            for k in (1, 3, 8):
                require("power_coherence", scaled_pascal_source(q**power, power*d, k)
                        == scaled_pascal_source(q, d, power*k))
    for k in (1, 2):
        modulus = 5**k
        outputs = {filtered_phase_from_carry(Q(2, 15), c, 3, 1, k) for c in range(modulus)}
        require("universal_carry_classes", len(outputs) == modulus)
    wrong_carry = {"actual": str(scaled_pascal_source(3, 1, 1) % 1),
                   "carry_dropped": str(filtered_phase_from_carry(Q(2, 15), 0, 3, 1, 1))}
    require("wrong_carry_falsifier", wrong_carry == {"actual": "47/75", "carry_dropped": "2/75"})
    endpoints = {str(q): list(absolute_shadow_endpoint_obstructions(q))
                 for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)}
    require("integer_filter_small_primes", all(endpoints[str(q)] for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)))
    require("integer_filter_31_passes_endpoints", not endpoints["31"])

    # Post-discovery controls for the bounded final holonomic/height followup.
    # These are explicitly separate from the preregistered calibration split.
    d_values = [(-1)**k*function_difference(forcing_original, 1, k) for k in range(97)]
    a_values = [difference(values, 0, k) for k in range(98)]
    for k in range(4, 97):
        coefficients = recurrence_coefficients(k)
        require("holonomic_order_four", sum(coefficients[j]*d_values[k-j] for j in range(5)) == 0)
        require("holonomic_order_five", sum((-1)**j*coefficients[j]*(a_values[k-j+1]-15*a_values[k-j]) for j in range(5)) == 0)
        phase_relation = sum(((-1)**j*coefficients[j]*((a_values[k-j+1] % 1)-15*(a_values[k-j] % 1))
                              for j in range(5)), Q())
        require("holonomic_integer_carry", phase_relation.denominator == 1)
    base31 = []
    for k in (1, 2, 8, 16, 32, 64):
        v = sum((comb(k, j)*2**j*(-1)**(k-j)*values[j] for j in range(k+1)), Q())
        error = tuple(31**k*t-v for t in alpha)
        bound = forcing_pascal_moment(0, k)/15+Q(1, (8*k+1)*(8*k+2))
        require("integer_base31_error", -bound < error[0] < error[1] < bound)
        base31.append({"order": k, "signed_error": interval_receipt(error),
                       "absolute_upper_bound": rational_receipt(bound)})
    for n in (1, 7, 19, 64, 127):
        require("local_tripling_identity", (values[n+1]-values[n])/5 == 3*values[n]+forcing_original(n+1)/5)
        require("local_31_identity", 2*values[n+1]-values[n] == 31*values[n]+2*forcing_original(n+1))

    primes = [p for p in range(3, 8*192+1)
              if all(p % d for d in range(2, isqrt(p)+1))]
    odd_lcms, current = [1], 1
    for bound in range(1, 8*192+1):
        if bound % 2:
            current = lcm(current, bound)
        odd_lcms.append(current)
    height_samples = []
    for n in range(1, 193):
        prime_product, prime_count = 1, 0
        for p in primes:
            upper = 8*n-7 if p % 8 == 1 else 8*n-3
            if p % 8 in (1, 5) and 2*n+1 <= p <= upper:
                require("source_fresh_prime_valuation", rational_valuation(values[n], p) == -1)
                prime_product *= p
                prime_count += 1
        denominator = values[n].denominator
        require("source_height_divisibility", denominator % prime_product == 0
                and odd_lcms[8*n-3] % denominator == 0)
        if n in (8, 16, 32, 64, 128, 192):
            height_samples.append({"index": n, "denominator_bits": denominator.bit_length(),
                                   "certified_prime_count": prime_count,
                                   "prime_product_bits": prime_product.bit_length(),
                                   "lcm_bound_bits": odd_lcms[8*n-3].bit_length()})
    for p in (5, 13, 17, 29, 37, 41, 53, 73, 89, 97, 101, 173, 193):
        birth = (p+7)//8 if p % 8 == 1 else (p+3)//8
        coefficient = 4 if p % 8 == 1 else -1
        last = (p-1)//2
        for n in (birth, (birth+last)//2):
            for k in (1, 2, 7, 16):
                if n+k <= last and p != 5:
                    actual = difference(values, n, k)
                    residue = Q(coefficient, p)*16**(n-birth)*15**k
                    remaining = actual-residue
                    require("translated_pascal_fresh_prime", rational_valuation(actual, p) == -1
                            and (remaining == 0 or rational_valuation(remaining, p) >= 0))
                    phase = actual % 1
                    require("translated_pascal_real_separation", min(phase, 1-phase) >= Q(1, odd_lcms[8*(n+k)-3]))
            if n+1 <= last:
                annihilated = values[n+1]-16*values[n]
                require("filter_annihilates_local_prime", rational_valuation(annihilated, p) >= 0)
        for k in (birth, last):
            require("forcing_origin_prime", rational_valuation(function_difference(forcing_original, 0, k), p) == -1)
    cancelled = difference(values, 0, 35)
    local_residue = sum((-1)**(35-j)*comb(35, j)*pow(16, j-12, 89) for j in range(12, 36)) % 89
    require("origin_source_prime_cancellation", local_residue == 0 and rational_valuation(cancelled, 89) == 0)
    prime_height = {"range": [1, 192], "prime_classes_mod_8": [1, 5], "samples": height_samples,
                    "origin_cancellation": {"prime": 89, "birth": 12, "order": 35,
                        "pascal_local_residue": local_residue, "actual_valuation": rational_valuation(cancelled, 89)},
                    "boundary": "No exponential height asymptotic is inferred from finite samples."}

    unsigned = []
    for k in (1, 4, 8, 16, 32, 64):
        b = source_pascal_row(0, k, sign=1)
        interval = tuple(17**k*t-b for t in alpha)
        require("unsigned_exact_positive", 0 < interval[0] < interval[1])
        require("unsigned_bounds", Q(2**k, 1024*(k+1)**2) < interval[0]
                and interval[1] < Q(4*2**k, k*k))
        if k >= 16:
            require("unsigned_absolute_growth", interval[0] > 1)
        unsigned.append({"order": k, "absolute_error": interval_receipt(interval)})
        enclosure = pascal_pi_interval(k, terms=5)
        require("pascal_pi_machin", enclosure[0] < pi_interval[0] < pi_interval[1] < enclosure[1])

    depth, precision = 12, 17
    reference = tuple(difference(values, 0, j)/factorial(j) for j in range(1, depth+1))
    model = positive_moment_countermodel(reference, precision)
    model_values = [model.unwrapped(n) for n in range(depth+1)]
    require("countermodel_mass_positive", model.moment(0) == 1 and model.perturbation_bound < Q(1, 2))
    for k in range(1, depth+1):
        for n in range(depth+1-k):
            actual = difference(model_values, n, k)
            delta = actual-difference(values, n, k)
            require("countermodel_finite_jet", valuation_two(actual) == difference_valuation(k))
            require("countermodel_finite_precision", delta == 0 or valuation_two(delta) >= difference_valuation(k)+precision)
    for n in range(1, 65):
        require("countermodel_carry_15", (16*model.phase(n-1)+model.forcing(n)).__floor__() == 15)
        require("countermodel_positive_forcing", model.forcing(n) > 0)
    for n in (0, 1, 19, 64):
        for k in (1, 3, 8):
            require("countermodel_CM", (-1)**k*function_difference(model.moment, n, k) > 0)
    phases = [model.phase(n) for n in range(64, 88)]
    cluster_width = max(phases)-min(phases)
    require("countermodel_complete_cluster", cluster_width < Q(1, 256))
    tiny = positive_moment_countermodel(reference[:2], 3)
    next_jet = function_difference(tiny.unwrapped, 0, 3)/factorial(3)
    require("finite_certificate_cannot_be_extrapolated", valuation_two(next_jet) == -1
            and valuation_two(next_jet) != 2)
    countermodel = {"certified_depth": depth, "normalized_precision": precision,
                    "density_coefficient_receipts": [rational_receipt(x) for x in model.density],
                    "perturbation_bound": rational_receipt(model.perturbation_bound),
                    "cluster_start": 64, "cluster_length": 24,
                    "cluster_width": rational_receipt(cluster_width),
                    "real_pair_fraction_at_radius_1_over_256": "1",
                    "changes_BBP_forcing": True,
                    "outside_certificate_control": {"depth": 2, "precision": 3,
                       "next_normalized_jet_valuation": valuation_two(next_jet),
                       "wanted_valuation_if_extrapolated": 2}}

    for length, order, bound in ((17, 9, 3), (31, 12, 1), (8, 1, 2)):
        samples = [-Q(bound)]*order+[Q()]*(length-order)+[Q(bound)]*order
        direct = sum(samples[:length], Q())/length
        actual = pascal_window_average(samples, length, order)
        require("averaging_endpoint_sharp", actual-direct == pascal_endpoint_budget(length, order, bound))
        require("averaging_stationary_non_Haar", pascal_window_average([Q(1)]*(length+order), length, order) == 1)

    files = [
        "research/2026-10-24/PI_PASCAL_HOLE_CONTRACT.md",
        "observational_succ/pi_pascal_source.py", "observational_succ/pi_pascal_kernel.py",
        "observational_succ/pi_pascal_controls.py", "scripts/pi_pascal_probe.py",
        "tests/test_pi_pascal_source.py", "tests/test_pi_pascal_kernel.py", "tests/test_pi_pascal_controls.py",
        "research/2026-10-24/PI_PASCAL_MAHLER_SOURCE.md",
        "research/2026-10-24/PI_PASCAL_REAL_KERNEL.md",
        "research/2026-10-24/PI_PASCAL_ADVERSARIAL_BOUNDARY.md",
        "research/2026-10-24/PI_PASCAL_HOLONOMIC_FRONTIER.md",
        "research/2026-10-24/PI_PASCAL_PRIME_HEIGHT.md",
    ]
    return {"schema": "succ.pi_pascal_probe.v1", "truth_state": "VERIFIED_FINITE",
            "pi_normality": "OPEN", "real_half_retention": "OPEN", "same_law_tripling": "OPEN",
            "parent_commit": "3acd547ff122368d5694efdab029b3156a292d8a",
            "arithmetic": "integer/Fraction decisions; outward Decimal display only",
            "python": platform.python_version(), "elapsed_seconds": round(time.monotonic()-started, 3),
            "calibration": {"starts": [0, 16], "orders": [1, 16], "pairs": len(calibration)},
            "held_out": {"starts": [19, 31, 64, 127], "orders": [17, 40], "pairs": len(held_out)},
            "checks_by_group": dict(sorted(COUNTS.items())), "total_exact_checks": sum(COUNTS.values()),
            "minimal_degree": degree_table, "crossnorm": crossnorm,
            "odd_prime_cancellation": cancellation, "base_filters": filters,
            "wrong_carry_control": wrong_carry, "integer_filter_endpoint_tests": endpoints,
            "holonomic_centers": [4, 96], "integer_base31": base31,
            "post_discovery_prime_height_controls": prime_height,
            "unsigned_absolute_errors": unsigned, "positive_moment_countermodel": countermodel,
            "independent_pi_oracle": {"identity": "16 arctan(1/5)-4 arctan(1/239)",
                "terms_each": 256, "width": rational_receipt(pi_interval[1]-pi_interval[0])},
            "file_sha256": {path: sha256((ROOT/path).read_bytes()).hexdigest() for path in files},
            "limits": ["Finite checks support evaluators, not universal proofs or distribution estimates.",
                "The polynomial-density constructor certifies dyadic jets only through its stated depth.",
                "The infinite entire-kernel countermodel is a separate paper construction.",
                "All-prime rational filters create new trajectories; equality of selected laws remains open.",
                "Large absolute unsigned error is not a lower bound on its circle distance."]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = run()
    result = json.dumps(receipt, indent=2, ensure_ascii=False)+"\n"
    if args.output:
        args.output.write_text(result)
        print(json.dumps({"output": str(args.output), "checks": receipt["total_exact_checks"],
                          "elapsed_seconds": receipt["elapsed_seconds"], "pi_normality": "OPEN"}))
    else:
        print(result, end="")
