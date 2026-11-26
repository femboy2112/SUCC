#!/usr/bin/env python3
"""Reproduce the independent exact place-seam audit of 2026-11-26.

Expected p-valuations are obtained by repeated integer division, and real
magnitudes are reconstructed from prime-log coefficients. These checks do not
call the toolkit's factorization function to derive expected values. The finite
scope is exactly the 33,073 checks originally run in the independent audit.

This calibrates rational samples and input handling. The pointwise-continuous
path theorem, flat-germ statement and analytic obstruction use the paper proofs.
"""

from fractions import Fraction
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.principia_place_seam import (
    path_via_trivial,
    place_readout,
    rational_capacity,
)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def independent_valuation(q, prime):
    """Compute v_p(q) directly, independently of prime factorization output."""
    numerator, denominator = abs(q.numerator), q.denominator
    answer = 0
    while numerator % prime == 0:
        numerator //= prime
        answer += 1
    while denominator % prime == 0:
        denominator //= prime
        answer -= 1
    return answer


def run():
    checked = 0
    for numerator in range(-41, 42):
        if not numerator:
            continue
        for denominator in range(1, 32):
            q = Fraction(numerator, denominator)
            real = place_readout(q, "infinity")
            rebuilt = Fraction(1)
            for prime, coefficient in real.log_coefficients:
                require(coefficient.denominator == 1, "Nonintegral normalized real coefficient")
                rebuilt *= Fraction(prime) ** coefficient.numerator
            require(rebuilt == abs(q), "Real-magnitude reconstruction differs from source")

            for prime in (2, 3, 5, 7, 11, 13, 17, 19):
                report = place_readout(q, prime, Fraction(3, 7))
                expected = -Fraction(3, 7) * independent_valuation(q, prime)
                require(report.log_coefficients == (((prime, expected),) if expected else ()),
                        "Prime readout differs from repeated-division valuation")
                checked += 1

            for parameter in (Fraction(1, 13), Fraction(6, 13), Fraction(1, 2),
                              Fraction(7, 13), Fraction(12, 13)):
                report = path_via_trivial(q, parameter, "infinity", 5).observation
                if parameter == Fraction(1, 2):
                    require(not report.log_coefficients, "Midpoint is not log-null")
                else:
                    exponent = abs(1 - 2 * parameter)
                    if parameter < Fraction(1, 2):
                        rebuilt = Fraction(1)
                        for prime, coefficient in report.log_coefficients:
                            power = coefficient / exponent
                            require(power.denominator == 1,
                                    "Path exponent does not restore integral source valuation")
                            rebuilt *= Fraction(prime) ** power.numerator
                        require(rebuilt == abs(q), "Left path lost normalized source magnitude")
                    else:
                        expected = -exponent * independent_valuation(q, 5)
                        require(report.log_coefficients == (((5, expected),) if expected else ()),
                                "Right path differs from normalized 5-adic valuation")
                checked += 1

    for malformed in (None, (), [], {}, object(), 3.0, Fraction(3), True, "3"):
        try:
            place_readout(Fraction(7, 3), malformed)
        except ValueError:
            pass
        else:
            raise AssertionError("Malformed place admitted")
        checked += 1

    for numerator in (-36, -15, -1, 1, 15, 36):
        for denominator in (7, 11, 35):
            q = Fraction(numerator, denominator)
            certificate = rational_capacity(q, denominator, ())
            require(certificate.integral_witness == numerator, "Wrong integral source witness")
            require(certificate.magnitude_lower_bound == Fraction(1, denominator),
                    "Unpaid or incorrectly normalized denominator")
            require(abs(q) >= certificate.magnitude_lower_bound, "False capacity lower bound")
            checked += 1

    require(checked == 33073, "The preserved audit scope has changed")
    return {
        "status": "PASS",
        "independent_exact_checks": checked,
        "arithmetic": "exact Fraction/integer",
        "scope": {
            "source_numerators": "-41 through 41, excluding zero",
            "source_denominators": "1 through 31",
            "primes": [2, 3, 5, 7, 11, 13, 17, 19],
            "prime_readout_exponent": "3/7",
            "path_parameters": ["1/13", "6/13", "1/2", "7/13", "12/13"],
            "path": "infinity -> trivial -> 5",
            "malformed_place_cases": 9,
            "capacity_cases": 18,
            "real_reconstruction_checks": 2542,
        },
        "counting": "Eight prime cases and five path cases per source pair, plus nine malformed places and eighteen capacity cases. Real reconstruction assertions are also checked but are not separately added to the preserved count.",
        "boundary": "Finite calibration only; continuum and universal claims use paper proofs.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, indent=2))
