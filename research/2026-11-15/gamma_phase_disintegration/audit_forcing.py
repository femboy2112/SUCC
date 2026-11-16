#!/usr/bin/env python3
"""Independent exact and numerical audit of the forcing Mellin retention theorem.

No SUCC production module is imported. Exact Fraction checks cover the original
four poles, positive rate regrouping, polynomial cancellation, and the rational
coprimality argument. The mpmath checks are finite diagnostics, not interval
certificates or a replacement for the written proof.

Run from any directory:
    python audit_forcing.py > receipts/forcing_audit.json
Or pass --output PATH to write the same JSON directly.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import gcd
from pathlib import Path

import mpmath as mp


POLES = ((0, 4), (3, -2), (4, -1), (5, -1))
RATE_CELLS = ((0, 3, 4), (3, 4, 2), (4, 5, 1))
DECIMAL_PRECISION = 70
TOLERANCE = "1e-60"


class Audit:
    def __init__(self) -> None:
        self.counts = {
            "exact_source_assertions": 0,
            "exact_boundary_assertions": 0,
            "numeric_fourier_assertions": 0,
            "numeric_direct_quadrature_assertions": 0,
            "numeric_complex_mellin_assertions": 0,
            "mutation_assertions": 0,
        }

    def check(self, condition: bool, category: str, label: str) -> None:
        if not condition:
            raise AssertionError(label)
        self.counts[category] += 1


def exact_source(a: Fraction) -> Fraction:
    return sum((Fraction(c, 1) / (a + d) for d, c in POLES), Fraction())


def exact_rate_integral(a: Fraction) -> Fraction:
    """Integrate each positive w(u)/(a+u)^2 cell by its antiderivative."""
    return sum(
        (Fraction(c) * (1 / (a + lo) - 1 / (a + hi))
         for lo, hi, c in RATE_CELLS),
        Fraction(),
    )


def exact_audit(audit: Audit) -> dict:
    special = [Fraction(1, 7), Fraction(7, 3), Fraction(1, 10)]
    source_times = [Fraction(8 * n - 7) for n in range(1, 129)]
    domain = special + source_times
    category = "exact_source_assertions"
    for a in domain:
        direct = exact_source(a)
        rate = exact_rate_integral(a)
        rational_form = (15 * a * a + 121 * a + 240) / (
            a * (a + 3) * (a + 4) * (a + 5)
        )
        audit.check(direct == rate, category, f"positive rate regrouping a={a}")
        audit.check(direct == rational_form, category, f"denominator clearing a={a}")
        audit.check(direct > 0, category, f"strict positive source a={a}")
        audit.check(direct < 4 / a, category, f"strict phasor disk a={a}")

    # The polynomial identity is checked coefficientwise, before sample values.
    quotient = [4, 4, 4, 2, 1]
    multiplied = [Fraction(0) for _ in range(6)]
    for k, coefficient in enumerate(quotient):
        multiplied[k] += coefficient
        multiplied[k + 1] -= coefficient
    audit.check(multiplied == [4, 0, 0, -2, -1, -1], category,
                "Q(x)=(1-x)(4+4x+4x^2+2x^3+x^4)")
    for x in [Fraction(0), Fraction(1, 13), Fraction(2, 7), Fraction(1, 2),
              Fraction(12, 13), Fraction(1)]:
        left = 4 - 2 * x**3 - x**4 - x**5
        right = (1 - x) * sum(Fraction(c) * x**k
                              for k, c in enumerate(quotient))
        audit.check(left == right, category, f"polynomial sample x={x}")
        audit.check(left >= 0, category, f"polynomial nonnegative x={x}")

    # All source channels are retained: deleting one destroys the equality.
    a = Fraction(9)
    wrong = 4 / a - 2 / (a + 3) - 1 / (a + 4)
    audit.check(wrong != exact_rate_integral(a), "mutation_assertions",
                "deleted fifth-rate channel must fail the authentic equality")

    boundary_samples = []
    category = "exact_boundary_assertions"
    for a in domain:
        p, q = a.numerator, a.denominator
        aa, bb, cc = p + 3 * q, p + 4 * q, p + 5 * q
        audit.check(gcd(p, q) == 1, category, f"reduced rational a={a}")
        audit.check(gcd(bb, aa) == 1, category, f"gcd(B,A)=1 a={a}")
        audit.check(gcd(bb, cc) == 1, category, f"gcd(B,C)=1 a={a}")
        audit.check(bb > 1, category, f"B has a prime divisor a={a}")
        audit.check(aa < bb < cc, category, f"positive rate-log differences a={a}")
        # A finite check of the consequence; the all-exponent claim is the
        # written coprimality proof, not this bounded scan.
        if a in special:
            for k in range(1, 7):
                for ell in range(1, 7):
                    audit.check(bb ** (k + ell) != aa**ell * cc**k,
                                category, f"boundary nonalignment a={a},k={k},l={ell}")
            boundary_samples.append({"a": str(a), "A": aa, "B": bb, "C": cc,
                                     "gcd_B_AC": gcd(bb, aa * cc)})
    return {
        "source_domain": "a=8n-7 for n=1..128, plus 1/7, 7/3, 1/10",
        "number_of_source_parameters": len(domain),
        "boundary_samples": boundary_samples,
        "finite_boundary_exponent_scan": "k,l=1..6 at the three extra rational a",
        "authority": "The universal claims use the paper proofs, not finite scans.",
    }


def number(a: Fraction):
    return mp.mpf(a.numerator) / a.denominator


def source(a):
    return mp.fsum(mp.mpf(c) / (a + d) for d, c in POLES)


def disk_factor(a, omega):
    return 4 / a - mp.fsum(
        mp.mpf(v) / (a + d) * mp.exp(-1j * omega * mp.log1p(d / a))
        for d, v in ((3, 2), (4, 1), (5, 1))
    )


def signed_fourier(a, omega):
    return mp.gamma(1 + 1j * omega) * disk_factor(a, omega) / source(a)


def positive_rate_mellin(a, z):
    """Independent bounded positive-rate integration, with complex test weight."""
    integrals = []
    for lo, hi, weight in RATE_CELLS:
        value = mp.quad(
            lambda u: mp.exp(-z * mp.log1p(u / a)) / (a + u)**2,
            [lo, hi],
        )
        integrals.append(weight * value)
    return mp.gamma(2 + z) * mp.fsum(integrals) / source(a)


def signed_mellin(a, z):
    return mp.power(a, z) * mp.gamma(1 + z) / source(a) * mp.fsum(
        mp.mpf(c) * mp.power(a + d, -1 - z) for d, c in POLES
    )


def direct_positive_fourier(a, omega):
    """Direct integral in scaled y=a*t; expm1 retains the small-y cancellation."""
    def integrand(y):
        q = -2 * mp.expm1(-3 * y / a) - mp.expm1(-4 * y / a) - mp.expm1(-5 * y / a)
        return mp.exp(-y) * q * mp.exp(1j * omega * mp.log(y)) / (a * source(a))
    return mp.quad(integrand, [0, mp.mpf("0.1"), 1, 10, mp.inf])


def text_number(value):
    return mp.nstr(value, 45)


def text_complex(value):
    return {"real": text_number(mp.re(value)), "imag": text_number(mp.im(value))}


def numerical_audit(audit: Audit) -> dict:
    mp.mp.dps = DECIMAL_PRECISION
    tol = mp.mpf(TOLERANCE)
    a_values = [Fraction(1, 7), Fraction(7, 3), Fraction(1, 10),
                Fraction(1), Fraction(9), Fraction(17), Fraction(89), Fraction(997)]
    max_rate_error = mp.mpf(0)
    max_direct_error = mp.mpf(0)
    max_mellin_error = mp.mpf(0)
    fourier_cases = 0
    direct_cases = 0
    mellin_cases = 0
    samples = []
    complex_samples = []
    for aq in a_values:
        a = number(aq)
        frequencies = [mp.mpf(0), mp.mpf("0.37"), mp.mpf(-2),
                       2 * mp.pi, mp.mpf(10), 2 * mp.pi * a, -2 * mp.pi * a]
        for omega in frequencies:
            phi = signed_fourier(a, omega)
            rate = positive_rate_mellin(a, 1j * omega)
            gamma1 = abs(mp.gamma(1 + 1j * omega))
            gamma2 = abs(mp.gamma(2 + 1j * omega))
            error = abs(phi - rate) / gamma2
            max_rate_error = max(max_rate_error, error)
            category = "numeric_fourier_assertions"
            audit.check(error < tol, category, f"signed/rate quadrature a={aq},w={omega}")
            audit.check(mp.re(disk_factor(a, omega) / source(a)) >= 1 - tol,
                        category, f"right half-plane a={aq},w={omega}")
            audit.check(abs(phi) >= gamma1 * (1 - tol), category,
                        f"Gamma-1 lower envelope a={aq},w={omega}")
            audit.check(abs(phi) <= gamma2 * (1 + tol), category,
                        f"Gamma-2 upper envelope a={aq},w={omega}")
            audit.check(abs(phi) > 0, category, f"finite Fourier nonzero a={aq},w={omega}")
            # Keep relative error at huge frequencies; an absolute 1e-60
            # comparison would be vacuous once the Gamma factor is tiny.
            reflected = signed_fourier(a, -omega)
            audit.check(abs(reflected - mp.conj(phi)) / gamma2 < tol,
                        category, f"orientation/conjugation a={aq},w={omega}")
            if omega == 0:
                audit.check(abs(phi - 1) < tol, category, f"zero-frequency normalization a={aq}")
            if omega == 2 * mp.pi * a:
                samples.append({
                    "a": str(aq), "omega": text_number(omega),
                    "phi": text_complex(phi),
                    "abs_phi_over_abs_Gamma1": text_number(abs(phi) / gamma1),
                    "abs_phi_over_abs_Gamma2": text_number(abs(phi) / gamma2),
                    "rate_error_over_abs_Gamma2": text_number(error),
                })
            fourier_cases += 1

        for omega in [mp.mpf("0.37"), mp.mpf(-2)]:
            phi = signed_fourier(a, omega)
            direct = direct_positive_fourier(a, omega)
            scale = abs(mp.gamma(2 + 1j * omega))
            error = abs(phi - direct) / scale
            max_direct_error = max(max_direct_error, error)
            audit.check(error < tol, "numeric_direct_quadrature_assertions",
                        f"direct positive source quadrature a={aq},w={omega}")
            direct_cases += 1

        for real_part, imaginary_part in [("-0.9", "0.37"), ("-0.9", "-4"),
                                           ("-0.25", "2.1"), ("0", "0"),
                                           ("0.5", "3"), ("2", "-1")]:
            z = mp.mpc(real_part, imaginary_part)
            actual = signed_mellin(a, z)
            rate = positive_rate_mellin(a, z)
            sigma = mp.re(1 + z)
            margin = 4 * a**(-sigma) - mp.fsum(
                mp.mpf(v) * (a + d)**(-sigma) for d, v in ((3, 2), (4, 1), (5, 1))
            )
            lower = abs(mp.power(a, z) * mp.gamma(1 + z) / source(a)) * margin
            # The positive mixture bounds |M(z)| by its Gamma modulus times
            # the positive real power moment. This is a scale, not a proof
            # inferred from the numerical quadrature.
            upper = abs(mp.gamma(2 + z)) * mp.fsum(
                weight * mp.quad(lambda u: mp.exp(-mp.re(z) * mp.log1p(u / a)) /
                                (a + u)**2, [lo, hi])
                for lo, hi, weight in RATE_CELLS
            ) / source(a)
            error = abs(actual - rate) / upper
            max_mellin_error = max(max_mellin_error, error)
            category = "numeric_complex_mellin_assertions"
            audit.check(sigma > 0, category, f"declared half-plane z={z}")
            audit.check(margin > 0, category, f"dominance margin a={aq},z={z}")
            audit.check(error < tol, category, f"Mellin signed/rate a={aq},z={z}")
            audit.check(abs(actual) >= lower * (1 - tol), category,
                        f"Mellin dominance lower bound a={aq},z={z}")
            audit.check(abs(actual) <= upper * (1 + tol), category,
                        f"Mellin positive-mixture upper bound a={aq},z={z}")
            if aq in [Fraction(1, 7), Fraction(7, 3)] and real_part == "-0.9":
                complex_samples.append({"a": str(aq), "z": text_complex(z),
                                        "M": text_complex(actual),
                                        "dominance_lower_bound": text_number(lower)})
            mellin_cases += 1

    mutation_samples = []
    for aq in [Fraction(1, 7), Fraction(7, 3), Fraction(9)]:
        a = number(aq)
        d = mp.mpf(3)
        omega = 2 * mp.pi / mp.log1p(d / a)
        one_gap_bracket = 1 - mp.exp(-1j * omega * mp.log1p(d / a))
        audit.check(abs(one_gap_bracket) < tol, "mutation_assertions",
                    f"one-gap boundary-zero mutation a={aq}")
        authentic_bracket = 4 - mp.fsum(
            mp.mpf(v) * mp.exp(-1j * omega * mp.log1p(dd / a))
            for dd, v in ((3, 2), (4, 1), (5, 1))
        )
        audit.check(abs(authentic_bracket) > tol, "mutation_assertions",
                    f"authentic boundary separates mutation a={aq}")
        removable = mp.fsum(mp.mpf(v) * mp.log1p(dd / a)
                            for dd, v in ((3, 2), (4, 1), (5, 1))) / (a * source(a))
        positive = positive_rate_mellin(a, mp.mpf(-1))
        audit.check(abs(removable - positive) / positive < tol, "mutation_assertions",
                    f"removable Mellin value z=-1 a={aq}")
        audit.check(removable > 0, "mutation_assertions",
                    f"positive removable Mellin value a={aq}")
        mutation_samples.append({
            "a": str(aq), "one_gap_d": "3", "boundary_frequency": text_number(omega),
            "one_gap_normalized_bracket_modulus": text_number(abs(one_gap_bracket)),
            "authentic_normalized_bracket_modulus": text_number(abs(authentic_bracket)),
            "authentic_removable_M_minus_1": text_number(removable),
        })

    return {
        "precision_decimal_digits": DECIMAL_PRECISION,
        "relative_tolerance": TOLERANCE,
        "a_values": [str(a) for a in a_values],
        "fourier_frequency_protocol": ["0", "0.37", "-2", "2*pi", "10", "2*pi*a", "-2*pi*a"],
        "direct_positive_kernel_frequencies": ["0.37", "-2"],
        "complex_mellin_protocol": ["-0.9+0.37i", "-0.9-4i", "-0.25+2.1i", "0", "0.5+3i", "2-i"],
        "fourier_cases": fourier_cases,
        "direct_positive_quadrature_cases": direct_cases,
        "complex_mellin_cases": mellin_cases,
        "max_signed_rate_error_over_Gamma2": text_number(max_rate_error),
        "max_direct_error_over_Gamma2": text_number(max_direct_error),
        "max_complex_mellin_error_over_positive_upper_scale": text_number(max_mellin_error),
        "moving_frequency_samples": samples,
        "complex_mellin_samples": complex_samples,
        "mutation_samples": mutation_samples,
        "scope": "Finite mpmath diagnostics; not rigorous interval enclosures. Paper proofs establish universal statements.",
    }


def run() -> dict:
    audit = Audit()
    exact = exact_audit(audit)
    numeric = numerical_audit(audit)
    return {
        "audit": "independent_forcing_mellin_retention",
        "status": "PASS",
        "production_imports": [],
        "assertion_counts": audit.counts,
        "total_assertions": sum(audit.counts.values()),
        "exact": exact,
        "numerical": numeric,
        "boundaries": {
            "pi_normality_proved": False,
            "R0_proved": False,
            "green_tail_nonvanishing_proved_by_this_audit": False,
            "numeric_interval_certification": False,
            "all_frequency_claim_authority": "Written inequalities and coprimality proof, not this finite audit.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write JSON here instead of stdout.")
    args = parser.parse_args()
    payload = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(payload, end="")
    else:
        args.output.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
