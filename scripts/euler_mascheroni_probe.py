#!/usr/bin/env python3
"""Replay exact finite Euler--Mascheroni / BBP / completed-Li certificates.

This receipt contains rational enclosures and exact finite controls only.
The paper proofs of infinite statements have separate authority.  In
particular, no finite prefix establishes pi normality or all-degree Li
positivity.  Run with --write PATH once, then --verify PATH to replay.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha1, sha256
import json
from math import isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from observational_succ import euler_bbp_regulator as bbp
from observational_succ import euler_gamma_li_bridge as li
from observational_succ import euler_mascheroni_succ as gamma
from observational_succ import gamma_character_bridge as characters
from observational_succ.pi_source_collision import bbp_states
from observational_succ.pi_source_genesis import (
    ComplexBox, character_interval, machin_pi_interval,
)


def outward(low, high, places=12):
    """Both displayed endpoints are exact rationals rounded outward."""
    scale = 10**places
    return Q((low*scale).__floor__(), scale), Q((high*scale).__ceil__(), scale)


def pack(interval):
    return [str(x) for x in interval]


def decimal_grid(value, places):
    scale = 10**places
    integer = value*scale
    assert integer.denominator == 1
    sign = "-" if integer < 0 else ""
    integer = abs(integer.numerator)
    return f"{sign}{integer//scale}.{integer%scale:0{places}d}"


def det(matrix):
    """Independent rational elimination for the finite Gram controls."""
    rows = [list(row) for row in matrix]
    answer = Q(1)
    for i in range(len(rows)):
        pivot = next((j for j in range(i, len(rows)) if rows[j][i]), None)
        if pivot is None:
            return Q()
        if pivot != i:
            rows[i], rows[pivot] = rows[pivot], rows[i]
            answer = -answer
        diagonal = rows[i][i]
        answer *= diagonal
        for j in range(i+1, len(rows)):
            ratio = rows[j][i]/diagonal
            for k in range(i+1, len(rows)):
                rows[j][k] -= ratio*rows[i][k]
    return answer


def square_bounds(low, high):
    return (Q() if low <= 0 <= high else min(low*low, high*high),
            max(low*low, high*high))


def sqrt_bounds(low, high, places=12):
    scale = 10**places
    a = isqrt((low*scale*scale).__floor__())
    b = isqrt((high*scale*scale).__floor__())+1
    result = Q(a, scale), Q(b, scale)
    assert result[0]**2 <= low and result[1]**2 >= high
    return result


def finite_gamma_controls():
    raw = gamma.paired_raw_prefix(7, 2)
    correction = gamma.paired_boundary_correction(7, 2)
    compensated = gamma.regularized_prefix_bounds(7, 1, 2)
    assert compensated == (raw+correction, raw+correction)
    assert raw != compensated[0]
    n, p, s, a = 7, 6, 3, Q(1, 8)
    mean = sum((gamma.regularized_prefix_bounds(n, (a+j)/p, s)[0]
                for j in range(p)), Q())/p
    scale, (anomaly, _) = gamma.refinement_affine_data(p, s)
    refined = scale*gamma.regularized_prefix_bounds(p*n, a, s)[0]+anomaly
    assert mean == refined and anomaly != 0
    quarter_pi = gamma.hurwitz_difference_bounds(Q(1, 4), Q(3, 4), 64)
    independent_pi = machin_pi_interval()
    assert quarter_pi[0] < independent_pi[0] < independent_pi[1] < quarter_pi[1]
    kernel = gamma.finite_mellin_kernel(9, (1, 2, 3))
    determinants = [det([row[:size] for row in kernel[:size]]) for size in (1, 2, 3)]
    assert all(x > 0 for x in determinants)
    null = det(gamma.finite_mellin_kernel(9, (1, 1, 2)))
    assert null == 0
    counterfeits = []
    for order in (0, 1, 3, 6):
        polynomial = gamma.jet_counterfeit_coefficients(order)
        preserved = [gamma.polynomial_moment(polynomial, k) for k in range(order+1)]
        changed = gamma.polynomial_moment(polynomial, order+1)/4
        assert all(x == 0 for x in preserved) and changed != 0
        counterfeits.append({"preserved_moment_degrees": [0, order],
                             "first_changed_moment": order+1,
                             "positive_perturbation_change": str(changed),
                             "changes_source": True})
    return {
        "gamma_enclosure_N128": pack(outward(*gamma.gamma_bounds(128))),
        "raw_pair_N7_r2": str(raw), "exact_boundary_correction": str(correction),
        "compensated_value": str(compensated[0]),
        "omitted_boundary_mutant_rejected": True,
        "finite_refinement": {"N": n, "p": p, "s": s, "a": str(a),
                              "exact_equality": True, "anomaly": str(anomaly),
                              "composite_multiplier_is_allowed": True},
        "quarter_Hurwitz_pi_N64": pack(outward(*quarter_pi)),
        "Machin_enclosure_strictly_inside": True,
        "positive_Gram_leading_minors": [str(x) for x in determinants],
        "repeated_exponent_Gram_determinant": str(null),
        "positive_kernel_is_not_Weil_form": True,
        "fixed_finite_moment_counterfeits": counterfeits,
    }


def bbp_regulator_controls():
    cases = 0
    for p in (2, 3, 6):
        for s in (0, 1, 2):
            for z in (Q(1, 16), Q(1)):
                direct = bbp.lerch_prefix(s, Q(1, 8), z, p*5)
                refined = bbp.lerch_refined_prefix(s, Q(1, 8), z, p, 5)
                assert direct == refined
                cases += 1
    for s in (0, 1, 2):
        for z in (Q(1, 16), Q(1)):
            assert bbp.source_prefix(24, s, z) == bbp.source_hurwitz_prefix(24, s, z)
    pi_interval = bbp.source_sum_interval(24, 1, Q(1, 16))
    machin = machin_pi_interval()
    assert pi_interval[0] < machin[0] < machin[1] < pi_interval[1]
    zero_prefix = bbp.source_prefix(32, 0)
    analytic_zero = bbp.balanced_boundary_zero_value()
    assert zero_prefix == 0 and analytic_zero == Q(15, 8)
    try:
        bbp.numerical_power_clock(400, dps=70)
    except ValueError as exc:
        precision_guard = str(exc)
    else:
        raise AssertionError("unguarded catastrophic-cancellation diagnostic")
    return {
        "exact_finite_Lerch_refinement_cases": cases,
        "original_BBP_pi_N24": pack(outward(*pi_interval, places=28)),
        "independent_Machin_strictly_inside": True,
        "unregulated_B1_N64": pack(outward(*bbp.source_sum_interval(64))),
        "literal_exponent_zero_prefix_N32": str(zero_prefix),
        "analytic_exponent_zero_boundary": str(analytic_zero),
        "cofinal_limit_s1_over_m_N2_power_m": str(bbp.cofinal_limit_for_power_clock(2)),
        "cofinal_limit_authority": "paper proof; not inferred from a finite computation",
        "changed_exponent_is_changed_forcing": True,
        "insufficient_precision_guard": precision_guard,
    }


def clock_controls():
    epsilon, cutoff = Q(1, 64), 4096
    tv = characters.clock_total_variation_lower(epsilon, cutoff)
    assert tv > Q(4, 5)
    rows = []
    for n in (256, 1024):
        values = tuple(characters.dyadic_log_periodic_sign(k) for k in range(1, 3*n+1))
        double = characters.harmonic_window(values, n, 2*n)
        triple = characters.harmonic_window(values, n, 3*n)
        assert abs(double) <= Q(5, n)
        rows.append({"N": n, "B2": pack(outward(double, double)),
                     "B3": pack(outward(triple, triple)),
                     "B2_absolute_envelope": str(Q(5, n))})
    n = 2**16-1
    mean = Q(characters.dyadic_control_signed_count(n), n)
    assert mean < Q(-1, 10)
    return {
        "epsilon": str(epsilon), "event_cutoff": cutoff,
        "total_variation_certified_lower_outward": pack(outward(tv, tv)),
        "lower_exceeds_four_fifths": True,
        "one_time_dilation_counterfeit": rows,
        "counterfeit_ordinary_mean_at_65535": str(mean),
        "counterfeit_is_not_BBP_source": True,
        "source_to_pi_h1_window_bounds_N32": {
            str(p): str(characters.source_character_window_envelope(32, p))
            for p in (2, 3)},
    }


def actual_character_windows():
    for phase, real, imag in ((Q(), 1, 0), (Q(1, 4), 0, 1), (Q(1, 2), -1, 0)):
        box = character_interval(phase, phase, order=16, bits=64).outward(60)
        assert box.real_low <= real <= box.real_high
        assert box.imag_low <= imag <= box.imag_high
    states = bbp_states(384)
    needed = sorted(set(range(33, 97)) | set(range(129, 385)))
    boxes = {n: character_interval(states[n], states[n], order=16, bits=64).outward(60)
             for n in needed}
    rows, squares_by_window = [], {}
    for n0 in (32, 128):
        for p in (2, 3):
            total = ComplexBox(Q(), Q(), Q(), Q())
            for n in range(n0+1, p*n0+1):
                box = boxes[n]
                total += ComplexBox(box.real_low/n, box.real_high/n,
                                    box.imag_low/n, box.imag_high/n)
            a, b = square_bounds(total.real_low, total.real_high)
            c, d = square_bounds(total.imag_low, total.imag_high)
            square = a+c, b+d
            squares_by_window[n0, p] = square
            modulus = sqrt_bounds(*square)
            rows.append({"N": n0, "p": p, "h": 1,
                         "real": pack(outward(total.real_low, total.real_high)),
                         "imag": pack(outward(total.imag_low, total.imag_high)),
                         "modulus": pack(modulus),
                         "modulus_decimal": [decimal_grid(q, 12) for q in modulus],
                         "modulus_squared": pack(outward(*square))})
    assert squares_by_window[128, 2][0] > squares_by_window[32, 2][1]
    return {
        "source": "original zero-initial four-pole BBP, exact rational circle states",
        "source_horizon": 384,
        "instrument": "80-term Machin; Taylor order 16; phase bits 64; outward box bits 60",
        "exact_zero_quarter_half_turn_controls_passed": True,
        "rows": rows,
        "rigorous_nonmonotonicity": "abs(B2(128)) > abs(B2(32))",
        "authority": "rational interval certificate for precisely four finite windows",
        "asymptotic_cancellation_proved": False,
    }


def completed_li_controls():
    result = li.certified_li_prefix(3, 512)
    assert result["strictly_positive_through"] == 3
    rows = []
    for n, interval in enumerate(result["li"], 1):
        displayed = outward(interval.lower, interval.upper, places=8)
        rows.append({"n": n, "enclosure": pack(displayed),
                     "decimal_enclosure": [decimal_grid(q, 8) for q in displayed]})
    contract = li.finite_jet_countermodel_contract(4)
    polynomial = contract.pop("polynomial_in_s_minus_one")
    for s in (Q(1, 4), Q(3, 4)):
        assert sum((c*(s-1)**k for k, c in enumerate(polynomial)), Q()) == 1
    assert all(c == 0 for c in polynomial[:4])
    contract["off_line_anchors"] = [str(x) for x in contract["off_line_anchors"]]
    return {
        "degree": 3, "cutoff": 512,
        "stieltjes_enclosures": [pack(outward(x.lower, x.upper)) for x in result["stieltjes"]],
        "li_enclosures": rows,
        "completion": "actual Gamma, pole normalization, and log(pi) channels retained",
        "construction": result["construction"],
        "strictly_positive_through": 3,
        "fixed_arch_gamma0_sensitivity": str(li.first_new_stieltjes_sensitivity(0)),
        "coupled_gamma0_sensitivity": str(li.first_new_stieltjes_sensitivity(0, coupled_arch_gamma=True)),
        "finite_jet_counterfeit": contract,
        "counterfeit_source_failure": "no ordinary absolutely convergent Dirichlet series (paper proof)",
        "all_degree_positivity_proved": False,
    }


def source_manifest():
    paths = [
        "observational_succ/euler_mascheroni_succ.py",
        "observational_succ/euler_bbp_regulator.py",
        "observational_succ/gamma_character_bridge.py",
        "observational_succ/euler_gamma_li_bridge.py",
        "tests/test_euler_mascheroni_succ.py",
        "tests/test_euler_bbp_regulator.py",
        "tests/test_gamma_character_bridge.py",
        "tests/test_euler_gamma_li_bridge.py",
        "observational_succ/pi_source_collision.py",
        "observational_succ/pi_source_genesis.py",
        "observational_succ/bbp_source_memory.py",
        "observational_succ/observer_reflection.py",
        "observational_succ/source_prime_certificates.py",
        "observational_succ/suzuki_arch_intervals.py",
        "scripts/euler_mascheroni_probe.py",
    ]
    result = {}
    for path in paths:
        data = (ROOT/path).read_bytes()
        result[path] = {"sha256": sha256(data).hexdigest(),
                        "git_blob_sha": sha1(f"blob {len(data)}\0".encode()+data).hexdigest()}
    return result


def build_receipt():
    return {
        "schema_version": 1,
        "authority": "exact finite identities and rational interval certificates; paper limits separate",
        "source_baseline_main": "e648df3e4fca73ab6b942232b5ca4b310e9cac08",
        "euler_mascheroni": finite_gamma_controls(),
        "bbp_regulator": bbp_regulator_controls(),
        "two_clocks": clock_controls(),
        "actual_character_windows": actual_character_windows(),
        "completed_li": completed_li_controls(),
        "source_manifest": source_manifest(),
        "pi_normality_proved": False,
        "RH_proved": False,
        "new_Lean_authority": False,
        "independent_external_referee": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    receipt = build_receipt()
    if args.verify:
        expected = json.loads(args.verify.read_text(encoding="utf-8"))
        if receipt != expected:
            raise SystemExit("Euler--Mascheroni receipt mismatch; inspect source hashes and certificate fields")
        print("Euler--Mascheroni finite receipt replay: PASS (four actual BBP windows, three Li coefficients)")
    elif args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n", encoding="utf-8")
        print(f"Wrote exact finite receipt: {args.write}")
    else:
        print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
