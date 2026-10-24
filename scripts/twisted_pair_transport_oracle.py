#!/usr/bin/env python3
"""Exact, independently evaluated calibration for the twisted-pair instrument.

Run from the repository root with:
    python -m scripts.twisted_pair_transport_oracle

Prints a deterministic JSON receipt. No pi digits, trigonometric floating
point, or assertions about infinite cancellation are used. Gaussian root
signals are checked by direct integer component formulas independent of
the module's Gaussian multiplication and path-integration implementation.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

from observational_succ.twisted_pair_transport import (
    antiphase_certificate, apply_wire_orientation, bbp_synchronous_pair,
    recover_signal, sharp_antiphase_cycle, signed_lag_correlation,
    transported_lag_correlation, transported_quadratic_sum, verify_bbp_path,
    wire_twists,
)


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def direct_circle_distance(first, second=Q()):
    difference = first - second
    residue = difference - difference.numerator // difference.denominator
    return min(residue, 1 - residue)


def direct_correlation(signal, lag):
    real = imag = 0
    for start in range(len(signal) - lag):
        a, b = signal[start + lag]
        c, d = signal[start]
        real += a * c + b * d
        imag += b * c - a * d
    return real, imag


def run():
    bounds_checked = 0
    sharp_cycles = []
    for base in (2, 4, 6, 16, 32):
        denominator = 200 * (base + 1)
        bound = Q(1, 2 * (base + 1))
        for numerator in range(denominator):
            phase = Q(numerator, denominator)
            errors = (direct_circle_distance(phase, Q(1, 2)),
                      direct_circle_distance(base * phase, Q(1, 2)))
            cert = antiphase_certificate(base, phase)
            require((cert.first_error, cert.next_error) == errors,
                    "certificate differs from independent floor reduction")
            require(max(errors) >= bound, "even-radix obstruction failed")
            bounds_checked += 1
        first, second = sharp_antiphase_cycle(base)
        require(base * first % 1 == second and base * second % 1 == first,
                "sharp cycle failed")
        require(antiphase_certificate(base, first).attains_bound
                and antiphase_certificate(base, second).attains_bound,
                "sharp cycle fails equality")
        sharp_cycles.append({"base": base, "first": str(first),
                             "second": str(second), "error": str(bound)})
    odd_controls = 0
    for base in (3, 5, 17):
        require(base * Q(1, 2) % 1 == Q(1, 2), "odd-radix control failed")
        odd_controls += 1

    roots = ((1, 0), (-1, 0), (0, 1), (0, -1))
    correlation_checks = 0
    missing_transport_failures = 0
    quadratic_checks = 0
    for signal in product(roots, repeat=4):
        real_sum = sum(z[0] for z in signal)
        imag_sum = sum(z[1] for z in signal)
        expected_quadratic = real_sum ** 2 + imag_sum ** 2
        for signs in product((1, -1), repeat=4):
            observed = tuple((signs[t] * signal[t][0], signs[t] * signal[t][1])
                             for t in range(4))
            edges = tuple(signs[t] * signs[t + 1] for t in range(3))
            require(wire_twists(signs) == edges, "edge construction failed")
            require(apply_wire_orientation(signal, signs) == observed,
                    "wire observation failed")
            require(recover_signal(observed, edges, signs[0]) == signal,
                    "source reconstruction failed")
            require(transported_quadratic_sum(observed, edges) == expected_quadratic,
                    "quadratic source reconstruction failed")
            quadratic_checks += 1
            for lag in (1, 2, 3):
                expected = direct_correlation(signal, lag)
                require(signed_lag_correlation(signal, lag) == expected,
                        "direct public correlation failed integer oracle")
                require(transported_lag_correlation(observed, edges, lag) == expected,
                        "transported correlation failed integer oracle")
                raw = direct_correlation(observed, lag)
                missing_transport_failures += raw != expected
                correlation_checks += 1

    pair = bbp_synchronous_pair(24, Q(9, 17))
    exact = Q()
    changed = Q(9, 17)
    source_checks = 0
    for n in range(1, 25):
        source = (Q(4, 8 * n - 7) - Q(2, 8 * n - 4)
                  - Q(1, 8 * n - 3) - Q(1, 8 * n - 2))
        require(source == pair.source[n - 1], "four-pole source mismatch")
        for value, expected, carry in (
            (exact, pair.selected[n], pair.selected_carries[n - 1]),
            (changed, pair.control[n], pair.control_carries[n - 1]),
        ):
            lifted = 16 * value + source
            require(lifted - carry == expected and 0 <= expected < 1,
                    "literal source carry mismatch")
        exact = (16 * exact + source) % 1
        changed = (16 * changed + source) % 1
        require((changed - exact) % 1 == Q(9 * pow(16, n, 17), 17) % 1,
                "source-consistent difference is not the sharp 17-clock")
        source_checks += 1
    require(verify_bbp_path(pair.selected), "authentic path rejected")
    require(not verify_bbp_path(pair.control),
            "changed-initial control falsely accepted as selected source")
    changed_path = list(pair.selected)
    changed_path[5] = (changed_path[5] + Q(1, 1000)) % 1
    require(not verify_bbp_path(changed_path), "mutated source path accepted")

    require(bounds_checked == 13000, "bound coverage changed")
    require(correlation_checks == 12288, "correlation coverage changed")
    require(missing_transport_failures == 8064, "mutation calibration changed")
    root = Path(__file__).resolve().parents[1]
    filenames = (
        "observational_succ/twisted_pair_transport.py",
        "tests/test_twisted_pair_transport.py",
        "scripts/twisted_pair_transport_oracle.py",
    )
    return {
        "status": "VERIFIED_FINITE",
        "normality_conclusion": "NONE",
        "rational_antiphase_inequalities": bounds_checked,
        "sharp_two_cycles": sharp_cycles,
        "odd_radix_negative_controls": odd_controls,
        "signed_transport_identities": correlation_checks,
        "quadratic_transport_identities": quadratic_checks,
        "omitted_transport_mutations_detected": missing_transport_failures,
        "independent_bbp_source_and_carry_steps": source_checks,
        "comparison_changes_initial_state": True,
        "initial_source_and_path_mutations_rejected": 2,
        "file_sha256": {name: sha256((root / name).read_bytes()).hexdigest()
                        for name in filenames},
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, indent=2))
