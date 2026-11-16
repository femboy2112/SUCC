#!/usr/bin/env python3
"""Exact Main XXVI carry/CRT interface checks; no asymptotic source estimate.

The Gaussian-rational phase controls verify the transport inequality independently
of Gamma quadrature. They do not numerically certify a Gamma special function.
The original-source carrier is separately computed with Fraction and with a
growing integer modulus. Retained holdout data are replayed, never called fresh.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import lcm
from pathlib import Path
import hashlib
import json

Z = tuple[F, F]
ROOT = Path(__file__).resolve().parents[1]


def r(n: int) -> F:
    if n < 1:
        raise ValueError("positive source index required")
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def zi(c: int) -> Z:
    return tuple(map(F, ((1, 0), (0, 1), (-1, 0), (0, -1))[c % 4]))


def add(a: Z, b: Z) -> Z:
    return a[0]+b[0], a[1]+b[1]


def mul(a: Z, b: Z) -> Z:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def scale(a: Z, b: F) -> Z:
    return a[0]*b, a[1]*b


def norm2(a: Z) -> F:
    return a[0]**2+a[1]**2


def div(a: Z, b: Z) -> Z:
    q = norm2(b)
    if not q:
        raise ValueError("nonzero reference required")
    return scale(mul(a, (b[0], -b[1])), 1/q)


def selected(c: int) -> int:
    return int(c % 4 in (1, 2))


def decode(z: Z) -> F:
    return (1-mul((F(1), F(1)), z)[0])/2


def carry_prefix(horizon: int = 512) -> list[int]:
    """Independent rational recurrence and 4L integer lift must agree exactly."""
    if horizon < 1:
        raise ValueError("positive horizon required")
    modulus, a, u = 1, 0, F(0)
    carries = []
    for n in range(1, horizon+1):
        old = modulus
        for odd in range(8*(n-1)+1, 8*n, 2):
            modulus = lcm(modulus, odd)
        forcing = modulus*r(n)
        assert forcing.denominator == 1
        a = (16*(modulus//old)*a+int(forcing)) % (4*modulus)
        u = 16*u+r(n)
        assert (modulus*u).denominator == 1
        assert int(modulus*u) % (4*modulus) == a
        c = u.__floor__() % 4
        assert a//modulus == c
        assert selected(c) == int(modulus <= a < 3*modulus)
        # Authentic rational clock, typed independently of the real floor.
        assert u.denominator % 2 == 1
        assert u.numerator*pow(u.denominator, -1, 4) % 4 == n % 4
        carries.append(c)
    return carries


def phase_controls() -> dict:
    """Exact bound plus three deliberate mutants, using Gaussian rationals."""
    for c in range(4):
        assert decode(zi(c)) == selected(c)
    # Conjugating the declared orientation loses selected residues1 and3.
    assert any(decode(zi(-c)) != selected(c) for c in range(4))
    # a=-i/2 is the exact Gamma(2,1) Fourier response at (xi,omega)=(1,0).
    a = (F(0), F(-1, 2))
    cases, inverse_errors = 0, []
    for b in (1, 2, 7, 32, 129):
        word = tuple((n*n+n//3) % 4 for n in range(b, 2*b))
        for sign in (-1, 0, 1):
            g, total_error = (F(0), F(0)), F(0)
            for n, c in zip(range(b, 2*b), word):
                eps = F(7, 4*n)
                perturbation = (sign*eps, F(0))
                psi = add(a, perturbation)
                assert norm2(add(psi, scale(a, F(-1)))) <= eps**2
                g = add(g, mul(zi(c), psi))
                total_error += eps
            g = scale(g, F(1, b))
            true_density = F(sum(map(selected, word)), b)
            error = abs(true_density-decode(div(g, a)))
            mean_error = total_error/b
            # Squared form of sqrt(2)/(2|a|) times mean_error.
            assert error**2 <= mean_error**2/(2*norm2(a))
            assert error**2 <= F(49, 32)*1/(norm2(a)*b*b)
            inverse_errors.append(str(error))
            cases += 1
    # Forgotten winding maps every phase to1 and every gate to0.
    assert decode((F(1), F(0))) == 0
    assert any(selected(c) for c in carry_prefix(16))
    try:
        div((F(1), F(0)), (F(0), F(0)))
    except ValueError:
        pass
    else:
        raise AssertionError("zero-response inversion was accepted")
    return {"exact_transport_cases": cases, "orientation_mutant_rejected": True,
            "forgotten_winding_mutant_rejected": True,
            "zero_reference_mutant_rejected": True,
            "errors": inverse_errors,
            "Gamma_quadrature_claimed": False}


def retained_recount(canonical_prefix: list[int]) -> dict:
    source = ROOT / "research/2026-11-15/three_count_hail_mary/receipts/fresh_source/carry_residues_mod4.txt"
    normalized = source.read_text().strip()
    residues = [int(c) for c in normalized]
    assert len(residues) == 131072
    assert residues[:len(canonical_prefix)] == canonical_prefix
    # Index n is stored at n-1. Use a sliding joint table, not prefix sums.
    cells = [[0]*4 for _ in range(4)]

    def update(n: int, sign: int) -> None:
        cells[n % 4][residues[n-1]] += sign

    b = 32769
    for n in range(b, 2*b):
        update(n, 1)
    minimum_l = minimum_d = None
    minimum_l_b = minimum_d_b = None
    maximum_error, maximum_error_b = F(-1), None
    count = failures = 0
    for b in range(32769, 65537):
        lvalue = F(cells[2][1]+cells[3][2]-cells[1][1], b)
        dvalue = F(sum(row[1]+row[2] for row in cells), b)
        # K=j-c, so reconstruct the parent's three masses independently.
        first = F(cells[0][0], b)
        second = F(sum(cells[j][(j-1) % 4] for j in range(4)), b)
        third = F(sum(cells[j][(j-k) % 4] for j in range(2) for k in range(2)), b)
        assert lvalue == first+second-third
        error = max(F(0), F(1,16)-first)+max(F(0), F(1,4)-second)+max(F(0), third-F(1,4))
        assert lvalue <= dvalue
        if minimum_l is None or lvalue < minimum_l:
            minimum_l, minimum_l_b = lvalue, b
        if minimum_d is None or dvalue < minimum_d:
            minimum_d, minimum_d_b = dvalue, b
        if error > maximum_error:
            maximum_error, maximum_error_b = error, b
        failures += error > F(1, 32)
        count += 1
        if b < 65536:
            update(b, -1)
            update(2*b, 1)
            update(2*b+1, 1)
    assert (minimum_l, minimum_l_b) == (F(1997,33657), 33657)
    assert (minimum_d, minimum_d_b) == (F(16393,32911), 32911)
    assert (maximum_error, maximum_error_b) == (F(136,33785), 33785)
    assert count == 32768 and failures == 0
    return {"status": "RETAINED_SHARED_SOURCE_RECOUNT_ONLY", "shells": count,
            "shell_range": [32769,65536], "minimum_L": str(minimum_l),
            "minimum_L_B": minimum_l_b, "minimum_d": str(minimum_d),
            "minimum_d_B": minimum_d_b, "maximum_error": str(maximum_error),
            "maximum_error_B": maximum_error_b, "failures": failures,
            "residues_normalized_sha256": hashlib.sha256(normalized.encode()).hexdigest(),
            "residues_file_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "fresh_source_computation_claimed": False}


def run() -> dict:
    carries = carry_prefix(512)
    return {"status": "EXACT_FINITE_INTERFACE_AUDIT", "canonical_fraction_states": 512,
            "growing_CRT_states": 512, "phase_controls": phase_controls(),
            "retained_recount": retained_recount(carries),
            "pi_normality_proved": False, "R0_proved": False,
            "source_selected_saving_proved": False}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
