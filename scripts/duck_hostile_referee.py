"""Independent exact controls for the Duck/BBP research campaign.

This script imports no proposed Duck/BBP implementation.  Finite receipts are
implementation checks; the universal arguments are in DUCK_INDEPENDENT_REFEREE.md.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import factorial
from pathlib import Path


def natural(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"expected a genuine integer >= {minimum}")
    return value


def frac(value: F) -> F:
    return value - value.numerator // value.denominator


def bbp_four_terms(m: int) -> F:
    natural(m, 1)
    return F(4, 8*m-7) - F(2, 8*m-4) - F(1, 8*m-3) - F(1, 8*m-2)


def bbp_rational(m: int) -> F:
    natural(m, 1)
    return F(120*m*m-89*m+16, 512*m**4-1024*m**3+712*m*m-206*m+21)


def sharp_bbp_polynomial_gap(m: int) -> tuple[int, int]:
    """Two independent exact evaluations of 47D - 15m²A."""
    natural(m, 1)
    a = 120*m*m-89*m+16
    d = (2*m-1)*(4*m-1)*(8*m-7)*(8*m-3)
    u = m-1
    return 47*d - 15*m*m*a, 22264*u**4 + 42263*u**3 + 26429*u*u + 5443*u


def forced_orbit(n: int, forcing=bbp_four_terms) -> F:
    natural(n)
    x = F(0)
    for m in range(1, n+1):
        x = frac(16*x + forcing(m))
    return x


def bbp_tail_interval(n: int, terms: int) -> tuple[F, F]:
    natural(n)
    natural(terms)
    partial = sum((bbp_four_terms(n+k) / 16**k for k in range(1, terms+1)), F(0))
    remainder = F(8, 15 * 16**terms * (n+terms+1)**2)
    return partial, partial + remainder


def atan_reciprocal_interval(q: int, terms: int) -> tuple[F, F]:
    natural(q, 2)
    natural(terms, 1)
    partial = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(terms)), F(0))
    next_term = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(partial, partial+next_term), max(partial, partial+next_term)


def machin_interval(terms: int = 80) -> tuple[F, F]:
    """Independent alternating-arctangent enclosure of the geometric pi."""
    a, b = atan_reciprocal_interval(5, terms)
    c, d = atan_reciprocal_interval(239, terms)
    return 16*a - 4*d, 16*b - 4*c


def intervals_meet_mod_one(left: tuple[F, F], right: tuple[F, F]) -> bool:
    a, b = left
    c, d = right
    if a > b or c > d:
        raise ValueError("reversed interval")
    low, high = a-d, b-c
    ceil_low = -((-low.numerator) // low.denominator)
    return ceil_low <= high.numerator // high.denominator


def fake_forcing(n: int) -> F:
    natural(n, 1)
    return (F(16, n*n) - F(1, (n+1)**2)) / 64


def fake_closed_orbit(n: int) -> F:
    natural(n)
    return frac(F(16**n, 64) - F(1, 64*(n+1)**2))


def fake_alternating_derivative(n: int, order: int) -> F:
    """(-1)^order times the exact derivative, at positive integer n."""
    natural(n, 1)
    natural(order)
    return F(factorial(order+1), 64) * (F(16, n**(order+2)) - F(1, (n+1)**(order+2)))


def cyclic_factor_maps(period: int, target_step: tuple[int, ...]) -> list[tuple[int, ...]]:
    natural(period, 1)
    k = len(target_step)
    if k == 0 or any(type(v) is not int or not 0 <= v < k for v in target_step):
        raise ValueError("invalid finite target transition")
    return [q for q in product(range(k), repeat=period)
            if set(q) == set(range(k))
            and all(q[(i+1) % period] == target_step[q[i]] for i in range(period))]


def c2_c3_nontrivial_common_factors() -> list[dict]:
    """Onto factors of C2 have at most two states, so k=2 is exhaustive."""
    return [{"target_step": step, "left": left, "right": right}
            for step in product(range(2), repeat=2)
            for left in cyclic_factor_maps(2, step)
            for right in cyclic_factor_maps(3, step)]


def delayed_probe(budget: int) -> dict:
    natural(budget)
    terminal = budget + 2
    observe = lambda x: int(x == terminal)
    left, right = 0, 1
    agreements = []
    for length in range(budget+2):
        agreements.append(observe(left) == observe(right))
        left, right = min(left+1, terminal), min(right+1, terminal)
    return {"budget": budget, "all_budget_words_agree": all(agreements[:-1]),
            "next_word_distinguishes": not agreements[-1]}


def thue_morse_prefix(length: int) -> tuple[int, ...]:
    natural(length)
    return tuple(n.bit_count() % 2 for n in range(length))


def clock_stationarity_residuals(masses: tuple[F, ...]) -> tuple[F, ...]:
    """Necessary marginal equations for the one-way clock, not a periodic clock."""
    if not masses:
        return ()
    return (masses[0],) + tuple(masses[k]-masses[k-1] for k in range(1, len(masses)))


def receipt() -> dict:
    points = list(range(1, 97)) + [101, 997, 10**6+3, 10**30]
    assert all(bbp_four_terms(m) == bbp_rational(m) for m in points)
    assert all(0 < bbp_rational(m) <= F(8, m*m) for m in points)
    assert all(sharp_bbp_polynomial_gap(m)[0] == sharp_bbp_polynomial_gap(m)[1] >= 0 for m in points)
    assert all(bbp_rational(m) <= F(47, 15*m*m) for m in points)
    pi_low, pi_high = machin_interval()
    phase_rows = []
    for n in range(1, 13):
        x = forced_orbit(n)
        lo, hi = bbp_tail_interval(n, 16)
        true = (16**(n-1)*pi_low, 16**(n-1)*pi_high)
        wrong = (16**n*pi_low, 16**n*pi_high)
        valid = intervals_meet_mod_one((x+lo, x+hi), true)
        wrong_valid = intervals_meet_mod_one((x+lo, x+hi), wrong)
        assert valid and not wrong_valid
        phase_rows.append({"n": n, "correct_index_overlap": valid, "wrong_index_overlap": wrong_valid})
    assert all(forced_orbit(n, fake_forcing) == fake_closed_orbit(n) for n in range(129))
    assert all(fake_alternating_derivative(n, k) > 0 for n in range(1, 25) for k in range(9))
    words = thue_morse_prefix(16384)
    triples = {words[k:k+3] for k in range(len(words)-2)}
    assert (0, 0, 0) not in triples and (1, 1, 1) not in triples
    common = c2_c3_nontrivial_common_factors()
    assert not common
    delays = [delayed_probe(k) for k in range(25)]
    assert all(row["all_budget_words_agree"] and row["next_word_distinguishes"] for row in delays)
    return {"schema": "succ.duck.hostile-referee.v1", "status": "EXACT_FINITE_CHECK",
            "no_production_implementation_imports": True,
            "bbp_arithmetic_points": len(points), "bbp_phase_controls": phase_rows,
            "sharp_bbp_bound_constant": "47/15, attained at m=1",
            "fake_orbit_indices": 129, "fake_derivative_checks": 216,
            "fake_leading_coefficient": "15/64", "fake_fourier_limit_paper_proved": "1",
            "c2_c3_nontrivial_common_factor_count": len(common),
            "delay_controls": delays, "thue_morse_digits": len(words),
            "thue_morse_forbidden_triples": ["000", "111"],
            "universal_proof_boundary": "See DUCK_INDEPENDENT_REFEREE.md; finite checks do not prove the universal claims.",
            "pi_normality": "OPEN"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = json.dumps(receipt(), indent=2) + "\n"
    if args.output:
        args.output.write_text(result)
    print(result)
