#!/usr/bin/env python3
"""Exact Pell/BBP interval observers; finite evidence, not normality evidence.

Run: python computation_probe.py --output computation_receipt.json
All proof-relevant arithmetic uses integers and fractions.Fraction.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial
from pathlib import Path
import platform


def source(n: int) -> Q:
    if n < 1:
        raise ValueError("The frozen four-pole source has n >= 1.")
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def source_integral(n: int) -> Q:
    # Integrate t^(8n-8) (1-t) (4+4t+4t^2+2t^3+t^4).
    k = 8*n-8
    return sum((Q(c, (k+j+1)*(k+j+2))
                for j, c in enumerate((4, 4, 4, 2, 1))), Q(0))


def bbp_table(count: int) -> list[Q]:
    partials = [Q(0)]
    for n in range(1, count+1):
        partials.append(partials[-1] + Q(1, 16**(n-1))*source(n))
    return partials


def bbp_interval(n: int, partials: list[Q]) -> tuple[Q, Q]:
    if n < 0:
        raise ValueError("n must be nonnegative")
    # pi - pi_n < 16^(1-n) / ((8n+1)(8n+2)).
    upper_error = Q(16, 16**n*(8*n+1)*(8*n+2))
    return partials[n], partials[n]+upper_error


def arctan_interval(inv: int, terms: int) -> tuple[Q, Q]:
    if inv <= 1 or terms < 1:
        raise ValueError("Require inv > 1 and terms >= 1")
    s = sum((Q((-1)**j, (2*j+1)*inv**(2*j+1))
             for j in range(terms)), Q(0))
    next_term = Q((-1)**terms, (2*terms+1)*inv**(2*terms+1))
    return min(s, s+next_term), max(s, s+next_term)


def machin_interval(terms: int) -> tuple[Q, Q]:
    a, b = arctan_interval(5, terms)
    c, d = arctan_interval(239, terms)
    return 16*a-4*d, 16*b-4*c


def floor_q(x: Q) -> int:
    return x.numerator//x.denominator


def floor_certificate(interval: tuple[Q, Q]) -> int | None:
    lo, hi = interval
    if lo > hi:
        raise ValueError("Malformed interval")
    lower, upper = floor_q(lo), floor_q(hi)
    return lower if lower == upper else None


def scale(interval: tuple[Q, Q], multiplier: int | Q) -> tuple[Q, Q]:
    lo, hi = interval
    a, b = multiplier*lo, multiplier*hi
    return min(a, b), max(a, b)


def pell(k: int) -> tuple[int, int]:
    if k < 1:
        raise ValueError("k must be positive")
    p, q = 1, 1
    for _ in range(1, k):
        p, q = p+2*q, p+q
    return p, q


def pell_interval(k: int) -> tuple[Q, Q]:
    p, q = pell(k)
    a, b = Q(p, q), Q(2*q, p)
    return min(a, b), max(a, b)


def outward_decimal(x: Q, places: int, upper: bool = False) -> str:
    unit = 10**places
    integer = -floor_q(-x*unit) if upper else floor_q(x*unit)
    sign = "-" if integer < 0 else ""
    integer = abs(integer)
    return f"{sign}{integer//unit}.{integer%unit:0{places}d}"


def display_interval(interval: tuple[Q, Q], places: int = 12) -> list[str]:
    return [outward_decimal(interval[0], places),
            outward_decimal(interval[1], places, upper=True)]


def intersects(a: tuple[Q, Q], b: tuple[Q, Q]) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])


def dyadic_hull(interval: tuple[Q, Q], bits: int = 128) -> tuple[Q, Q]:
    unit = 2**bits
    return Q(floor_q(interval[0]*unit), unit), Q(-floor_q(-interval[1]*unit), unit)


def stern_brocot_path(left: int, steps: int, compare) -> dict:
    a, b, c, d = left, 1, left+1, 1
    letters = []
    for _ in range(steps):
        assert b*c-a*d == 1
        m, n = a+c, b+d
        verdict = compare(Q(m, n))
        if verdict == 0:
            return {"rational_stop": str(Q(m, n)), "path": "".join(letters)}
        if verdict < 0:
            c, d = m, n
            letters.append("L")
        else:
            a, b = m, n
            letters.append("R")
    assert b*c-a*d == 1
    assert Q(c, d)-Q(a, b) == Q(1, b*d)
    return {"path": "".join(letters), "left": str(Q(a, b)),
            "right": str(Q(c, d)), "width": str(Q(1, b*d)),
            "unimodularity_checks": steps+1}


def character_interval(
    x_interval: tuple[Q, Q], h: int, pi_interval: tuple[Q, Q], terms: int = 22,
) -> tuple[tuple[Q, Q], tuple[Q, Q]]:
    """Rectangular enclosure of exp(2*pi*i*h*x), without floor(x) stability.

    Reduce the rational midpoint's phase exactly; bound the true input radius
    separately by 2*pi*|h|*radius. Sin/cos use rational Taylor centers and
    derivative <= 1. This is valid across the fractional-part branch cut.
    """
    if x_interval[0] > x_interval[1]:
        raise ValueError("Malformed input interval")
    lo, hi = dyadic_hull(x_interval)
    midpoint, radius = (lo+hi)/2, (hi-lo)/2
    phase = h*midpoint
    phase -= floor_q(phase+Q(1, 2))
    angle = scale(dyadic_hull(pi_interval), 2*phase)
    center, angle_radius = (angle[0]+angle[1])/2, (angle[1]-angle[0])/2
    sine = sum(((-1)**j*center**(2*j+1)/factorial(2*j+1)
                for j in range(terms)), Q(0))
    cosine = sum(((-1)**j*center**(2*j)/factorial(2*j)
                  for j in range(terms)), Q(0))
    sine_remainder = abs(center)**(2*terms+1)/factorial(2*terms+1)
    cosine_remainder = abs(center)**(2*terms)/factorial(2*terms)
    # pi < 22/7 is separately certified below by a rational Machin enclosure.
    shared_error = angle_radius + Q(44, 7)*abs(h)*radius
    se, ce = shared_error+sine_remainder, shared_error+cosine_remainder
    re = max(Q(-1), cosine-ce), min(Q(1), cosine+ce)
    im = max(Q(-1), sine-se), min(Q(1), sine+se)
    return re, im


def main() -> dict:
    max_term = 270
    partials = bbp_table(max_term)
    machin = machin_interval(300)
    assert Q(3) < machin[0] < machin[1] < Q(22, 7)

    for n in range(1, 201):
        assert source(n) == source_integral(n)
        assert Q(0) < source(n) < Q(15, (8*n-7)*(8*n-6))
    source_recurrence = Q(0)
    for n in range(1, max_term+1):
        source_recurrence = 16*source_recurrence+source(n)
        assert source_recurrence == 16**(n-1)*partials[n]
        previous = bbp_interval(n-1, partials)
        current = bbp_interval(n, partials)
        assert previous[0] < current[0] < current[1] < previous[1]

    tail_epochs = (0, 1, 2, 3, 4, 8, 16, 31, 64, 128, 256)
    tail_receipts = []
    for n in tail_epochs:
        lo, hi = bbp_interval(n, partials)
        assert lo < machin[0] < machin[1] < hi
        tail_receipts.append({"terms": n, "contains_independent_machin_interval": True,
                              "error_upper": str(hi-lo)})

    # Mutation: missing factor 16 is decisively rejected at N=1.
    bad_upper = partials[1]+Q(1, 16*(8+1)*(8+2))
    assert bad_upper < machin[0]
    assert 16*partials[1] != source(1)  # wrong source-clock normalization

    digit_exponents = tuple(range(33)) + (63, 127, 255)
    digits = []
    for j in digit_exponents:
        n = max(1, j+1)
        integer = floor_certificate(scale(bbp_interval(n, partials), 16**j))
        while integer is None:
            n += 1
            assert n <= max_term
            integer = floor_certificate(scale(bbp_interval(n, partials), 16**j))
        independent = floor_certificate(scale(machin, 16**j))
        assert independent is not None and integer == independent
        digits.append({"radix_exponent": j, "terms": n,
                       "hex_digit": format(integer % 16, "X"),
                       "independent_machin_agreement": True})

    previous = None
    for k in range(1, 201):
        p, q = pell(k)
        lo, hi = pell_interval(k)
        assert p*p-2*q*q == (-1)**k
        assert lo*lo < 2 < hi*hi
        assert hi-lo == Q(1, p*q)
        assert hi-lo <= Q(1, 4**(k-1))
        if previous is not None:
            assert previous[0] < lo < hi < previous[1]
        previous = (lo, hi)

    pell_digits = []
    for j in tuple(range(33))+(63, 127):
        k = 4*j+3
        scaled = scale(pell_interval(k), 16**j)
        integer = floor_certificate(scaled)
        assert integer is not None
        # Independent integer-only certificate: the floor squares bracket 2*16^(2j).
        target = 2*16**(2*j)
        assert integer**2 < target < (integer+1)**2
        pell_digits.append({"radix_exponent": j, "pell_depth": k,
                            "hex_digit": format(integer % 16, "X"),
                            "independent_square_bracket": True})

    def compare_sqrt2(m: Q) -> int:
        difference = Q(2)-m*m
        return (difference > 0)-(difference < 0)

    maximum_bbp_comparison_terms = 0

    def compare_pi(m: Q) -> int:
        nonlocal maximum_bbp_comparison_terms
        for terms in range(1, max_term+1):
            lo, hi = bbp_interval(terms, partials)
            if hi < m or lo > m:
                maximum_bbp_comparison_terms = max(maximum_bbp_comparison_terms, terms)
                return -1 if hi < m else 1
        raise AssertionError("Stern-Brocot comparison not resolved within finite probe budget")

    sqrt2_path = stern_brocot_path(1, 128, compare_sqrt2)
    pi_path = stern_brocot_path(3, 128, compare_pi)
    assert Q(sqrt2_path["left"])**2 < 2 < Q(sqrt2_path["right"])**2
    assert Q(pi_path["left"]) < machin[0] < machin[1] < Q(pi_path["right"])
    pi_path["maximum_bbp_comparison_terms"] = maximum_bbp_comparison_terms

    # Floor must abstain at a crossing, including a tight rational cut.
    assert floor_certificate((Q(6, 5), Q(13, 10))) == 1
    assert floor_certificate((Q(255, 256), Q(257, 256))) is None
    assert floor_q(Q(255, 256)) != floor_q(Q(257, 256))
    for bits in range(1, 65):
        epsilon = Q(1, 2**bits)
        assert floor_certificate((1-epsilon, 1+epsilon)) is None

    # Quarter-circle calibration plus sign-error mutation.
    phase_controls = ((Q(0), 1, 0), (Q(1, 4), 0, 1),
                      (Q(1, 2), -1, 0), (Q(3, 4), 0, -1))
    for x, real, imag in phase_controls:
        re, im = character_interval((x, x), 1, machin)
        assert re[0] <= real <= re[1] and im[0] <= imag <= im[1]
    _, im_quarter = character_interval((Q(1, 4), Q(1, 4)), 1, machin)
    assert im_quarter[0] > 0  # conjugating the character would fail this.
    re_cut, im_cut = character_interval((Q(255, 256), Q(257, 256)), 1, machin)
    assert re_cut[0] <= 1 <= re_cut[1] and im_cut[0] <= 0 <= im_cut[1]

    character_receipts = []
    for clock in (1, 2, 7, 23, 64):
        n = clock+12
        x_bbp = scale(bbp_interval(n, partials), 16**(clock-1))
        x_machin = scale(machin, 16**(clock-1))
        for h in (1, 8, 32):
            re, im = character_interval(x_bbp, h, machin)
            re2, im2 = character_interval(x_machin, h, machin)
            assert intersects(re, re2) and intersects(im, im2)
            character_receipts.append({"clock": clock, "h": h, "bbp_terms": n,
                                       "real_interval": display_interval(re),
                                       "imag_interval": display_interval(im),
                                       "independent_input_intersection": True})

    # Known-result recovery: source-authenticated 2-by-3 prime contrast.
    # Eight individual phase cells implement the seven-row donor table.
    phase_cells = (
        ("Y1", 1, Q(1, 8), Q(1, 6)),
        ("Y2", 16, Q(1, 6), Q(1, 3)),
        ("Y3", 16**2, Q(1, 6), Q(1, 3)),
        ("Y6", 16**5, Q(1, 2), Q(1)),
        ("Y2-Y1", 16-1, Q(1, 10), Q(1, 8)),
        ("Y6-Y3", 16**5-16**2, Q(2, 5), Q(5, 12)),
        ("Y3-Y1", 16**2-1, Q(1, 10), Q(1, 9)),
        ("Y6-Y2", 16**5-16, Q(3, 8), Q(2, 5)),
    )
    recovered_cells = []
    for label, multiplier, lower, upper in phase_cells:
        interval = scale(bbp_interval(12, partials), multiplier)
        integer = floor_certificate(interval)
        assert integer is not None
        lo, hi = interval[0]-integer, interval[1]-integer
        assert lower < lo <= hi < upper
        recovered_cells.append({"phase": label, "certified_cell": [str(lower), str(upper)],
                                "floor": integer, "bbp_terms": 12})

    return {
        "status": "PASS",
        "scope": "VERIFIED_FINITE; universal formulas proved in COMPUTATION_GRAPH.md",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(),
        "arithmetic": "integer and fractions.Fraction only; no floating-point acceptance tests",
        "source_normalization": "pi_N=sum_{n=1}^N16^(1-n)r(n); U_N=16^(N-1)pi_N",
        "source_integral_checks": 200,
        "source_recurrence_checks": max_term,
        "bbp_interval_nesting_checks": max_term,
        "tail_enclosures": tail_receipts,
        "pi_digit_certificates": digits,
        "pell_identity_nesting_checks": 200,
        "sqrt2_digit_certificates": pell_digits,
        "stern_brocot": {"sqrt2": sqrt2_path, "pi": pi_path},
        "character_certificates": character_receipts,
        "known_source_2_by_3_defect": {
            "individual_phase_cells": recovered_cells,
            "conclusion_with_elementary_trigonometry": "Im(a6-a3-a2+a1) < 1-sqrt(3) < 0",
            "provenance": "75dc9f9a230c5c71b3f580c5ac2f17780ba1d560/research/2026-11-10/basel_crt_omega_phasebridge/prime_archimedean/DIRICHLET_PRIME_DEFECT.md",
            "claim": "known-result recovery, not a new asymptotic theorem",
        },
        "negative_controls": {
            "missing_tail_factor_16": "REJECTED at N=1 by independent Machin interval",
            "source_clock_off_by_one": "REJECTED at N=1 by exact rational equality",
            "floor_across_integer": "ABSTAINED at 1 for 64 shrinking intervals",
            "conjugated_character": "REJECTED by the +i quarter-circle control",
        },
        "not_claimed": ["normality of pi", "normality of sqrt(2)", "all-epoch signed decay",
                        "general decidability of equality of computable reals",
                        "repository-wide tests", "Lean verification", "external referee"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = main()
    rendered = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(rendered)
        print(json.dumps({"status": receipt["status"], "receipt": str(args.output),
                          "script_sha256": receipt["script_sha256"]}, sort_keys=True))
    else:
        print(rendered, end="")
