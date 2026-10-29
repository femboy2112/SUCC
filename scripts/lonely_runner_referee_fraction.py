#!/usr/bin/env python3
"""Separate Fraction band-subtraction census; imports no SUCC search/checker."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd


def source_gaps(n, speeds):
    intervals = sorted((max(F(0), F(n*k-1, n*v)), min(F(1), F(n*k+1, n*v)))
                       for v in speeds for k in range(v+1))
    answer, frontier = [], F(0)
    for a, b in intervals:
        if a > frontier:
            answer.append((frontier, a))
        frontier = max(frontier, b)
    if frontier < 1:
        answer.append((frontier, F(1)))
    return tuple(answer)


def subtract_source_bands(n, gaps, velocity):
    """Subtract each intersecting closed source band from each open input gap."""
    delta, result = F(1, n), []
    for a, b in gaps:
        lo = velocity*a-delta
        hi = velocity*b+delta
        first = max(0, lo.numerator//lo.denominator)
        last = min(velocity, -((-hi.numerator)//hi.denominator))
        frontier = a
        for winding in range(first, last+1):
            left = max(a, (F(winding)-delta)/velocity)
            right = min(b, (F(winding)+delta)/velocity)
            if left >= right:
                continue
            if left > frontier:
                result.append((frontier, left))
            frontier = max(frontier, right)
        if frontier < b:
            result.append((frontier, b))
    return tuple(result)


def deletion_value(n, r):
    if 2*r > n-1:
        return F(1, r)
    denominator = n+r
    while gcd(denominator, r) != 1:
        denominator += 1
    return F(2, denominator)


def fraction_census(n):
    if type(n) is not int or n < 5:
        raise ValueError("integer n>=5 required")
    raw = first_rejected = width_rejected = checked = first_count = 0
    accepted, pairs = [], []
    for r1, r2 in combinations(range(1, n), 2):
        source = tuple(v for v in range(1, n) if v not in (r1, r2))
        baseline = source_gaps(n, source)
        mu = max(deletion_value(n, r1), deletion_value(n, r2))
        gamma_bound = F(2*(n-2)*(n-1), n*(n-4))/(mu-F(1, n))
        gamma_cap = (gamma_bound.numerator-1)//gamma_bound.denominator
        raw += (2*n-3)*sum(range(n, gamma_cap+1))
        occupancy_bound = F(4*(n-2), n*(n-4))/max(b-a for a, b in baseline)
        first_cap = min(gamma_cap, (occupancy_bound.numerator-1)//occupancy_bound.denominator)
        first_rejected += (2*n-3)*sum(range(max(n, first_cap+1), gamma_cap+1))
        pair_accepted = []
        pair_checked = 0
        for w1 in range(n, first_cap+1):
            first_count += 1
            residual = subtract_source_bands(n, baseline, w1)
            if not residual:
                raise ArithmeticError("one-insertion cover contradicts Gamma")
            cap = min(2*(n-1)*w1, F(2, n)//max(b-a for a, b in residual))
            width_rejected += 2*(n-1)*w1-max(w1, cap)
            # Deliberately no center-divisibility or single-band-winding filter.
            # Every width-surviving source undergoes exact Fraction subtraction.
            for w2 in range(w1+1, cap+1):
                checked += 1; pair_checked += 1
                if not subtract_source_bands(n, residual, w2):
                    item = {"removed": [r1, r2], "inserted": [w1, w2]}
                    accepted.append(item); pair_accepted.append([w1, w2])
        pairs.append({"removed": [r1, r2], "first_cap": first_cap,
                      "fraction_cover_checks": pair_checked, "accepted": pair_accepted})
    if first_rejected+width_rejected+checked != raw:
        raise ArithmeticError("independent domain accounting failed")
    return {"n": n, "complete": True, "proved_domain_count": raw,
            "first_occupancy_rejected": first_rejected, "width_rejected": width_rejected,
            "first_speeds": first_count, "fraction_cover_checks": checked,
            "survivor_count": len(accepted), "survivors": accepted, "pairs": pairs,
            "no_primary_census_or_verifier_import": True,
            "authority": "Fraction band subtraction plus shared proved finite bounds"}


def known_controls():
    result = []
    for n, removed, added in ((5, (1, 3), (6, 8)), (8, (2, 3), (11, 13)),
                              (74, (70, 72), (140, 144)), (284, (280, 282), (560, 564))):
        speeds = tuple(v for v in range(1, n) if v not in removed)+added
        if source_gaps(n, speeds):
            raise ArithmeticError("known exact positive failed full Fraction union")
        t = F(1, n)
        value = min(min((v*t) % 1, 1-(v*t) % 1) for v in speeds)
        if value != F(1, n):
            raise ArithmeticError("positive lower witness failed")
        gw = []
        if n in (74, 284):
            for r in removed:
                window = list(range(n-r, 2*(n-r)))
                divisors = [gcd(r, b) for b in window]
                if min(divisors) <= 1:
                    raise ArithmeticError("published Goddyn-Wong condition failed")
                gw.append({"removed": r, "multiplier": 2, "window": window, "gcds": divisors})
        result.append({"n": n, "removed": list(removed), "inserted": list(added),
                       "full_fraction_cover": True, "lower_witness_time": [1, n],
                       "exact_loneliness": [1, n], "goddyn_wong_windows": gw})
    return result
