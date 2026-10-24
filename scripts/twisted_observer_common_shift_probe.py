#!/usr/bin/env python3
"""Exact two-wire controls with unchanged BBP forcing and common shifts.

Replays p=2081 with no supplied pi digits and no production-source imports.
Both variants preserve the complete synchronized wire differential.  The
dyadic variant changes carrier parity and eventually coalesces; the odd
3-primary variant retains odd denominators but changes the 3-primary state.
Both change the authentic initial zero.  Neither is a counterexample to
pi normality, and neither establishes a new asymptotic collision estimate.

The dyadic mechanism extends PR266's control to two synchronized wires.
The odd variant uses density of Z[1/3] and exact finite verification.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


def forcing(n: int) -> Q:
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def trajectory(initial: Q, horizon: int) -> tuple[list[Q], list[int]]:
    states, carries = [initial % 1], []
    for n in range(1, horizon+1):
        raw = 16*states[-1]+forcing(n)
        carries.append(raw // 1)
        states.append(raw % 1)
    return states, carries


def positive_tail_interval(n: int, terms: int) -> tuple[Q, Q]:
    """Source-only enclosure using positive decreasing authentic forcing.

    The omitted geometric tail is below r(n+terms+1)/(15*16**terms).
    The construction uses this enclosure only to choose a control.  Every
    reported finite collision and carry is then checked on exact states.
    """
    low = sum((forcing(n+k)/16**k for k in range(1, terms+1)), Q())
    return low, low+forcing(n+terms+1)/Q(15*16**terms)


def nearest_integer(value: Q) -> int:
    return (2*value.numerator+value.denominator)//(2*value.denominator)


def circle_distance(value: Q) -> Q:
    value %= 1
    return min(value, 1-value)


def ordered_close_pairs(values: list[Q], radius: Q) -> int:
    if not values or not Q(0) <= radius < Q(1, 2):
        raise ValueError("nonempty sample and radius in [0,1/2) required")
    values = sorted(value % 1 for value in values)
    n = len(values)
    doubled = values+[value+1 for value in values]
    j, directed = 0, 0
    for i in range(n):
        j = max(j, i+1)
        while j < i+n and doubled[j]-doubled[i] <= radius:
            j += 1
        directed += j-i-1
    return n+2*directed


def calibrate_pair_counter() -> int:
    cases = (([Q(0), Q(1, 16), Q(15, 16), Q(1, 2), Q(1, 16)], Q(1, 16)),
             ([Q(0), Q(0), Q(1, 3), Q(2, 3)], Q(0)),
             ([Q(1, 17), Q(8, 17), Q(16, 17)], Q(2, 17)))
    for values, radius in cases:
        brute = sum(circle_distance(x-y) <= radius for x in values for y in values)
        if ordered_close_pairs(values, radius) != brute:
            raise AssertionError("independent endpoint/wrap pair-count calibration failed")
    return len(cases)


def fraction_digest(value: Q) -> str:
    return sha256((str(value.numerator)+"/"+str(value.denominator)).encode()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    calibrations = calibrate_pair_counter()
    p, cells = 2081, 16
    first, last = (p-1)//8+1, (p-1)//2
    length = last-first+1
    depth_margin = 0
    while 16**depth_margin < 8*cells:
        depth_margin += 1
    horizon = last+depth_margin
    carry_prefix = (first-2)//9
    gamma = Q(1, 15)
    source, carries = trajectory(Q(), horizon)
    companion, companion_carries = trajectory(gamma, horizon)
    for x, z in zip(source, companion):
        if (z-x) % 1 != gamma:
            raise AssertionError("original source wires lost their differential")
    low, high = positive_tail_interval(first, horizon-first)
    target = (1-source[first]-(low+high)/2) % 1
    dyadic = Q(nearest_integer(target*16**(horizon-first)), 16**horizon)
    odd_denominator, odd_depth = 1, 0
    while odd_denominator < 16**horizon:
        odd_denominator *= 3
        odd_depth += 1
    odd = Q(nearest_integer(target*Q(odd_denominator, 16**first)), odd_denominator)

    actual_pairs = ordered_close_pairs(source[first:last+1], Q(1, cells))
    if actual_pairs != 76544:
        raise AssertionError("the actual p2081 source receipt changed")
    results = []
    for kind, delta in (("dyadic", dyadic), ("odd_3_primary", odd)):
        if not 0 < delta < 2*Q(1, 16**first):
            raise AssertionError("common initial change exceeded its declared size")
        changed, changed_carries = trajectory(delta, horizon)
        changed_companion, changed_companion_carries = trajectory(gamma+delta, horizon)
        for n, (x, z, xp, zp) in enumerate(zip(
                source, companion, changed, changed_companion)):
            displacement = (16**n*delta) % 1
            if ((zp-xp) % 1 != gamma or (xp-x) % 1 != displacement
                    or (zp-z) % 1 != displacement):
                raise AssertionError("common-shift or cable-differential identity failed")
        if (changed_carries[:carry_prefix] != carries[:carry_prefix]
                or changed_companion_carries[:carry_prefix]
                != companion_carries[:carry_prefix]):
            raise AssertionError("a declared literal carry prefix changed")
        max_distance = max(circle_distance(x) for x in changed[first:last+1])
        if not 2*max_distance < Q(1, cells):
            raise AssertionError("the changed source did not form a close cluster")
        pairs = ordered_close_pairs(changed[first:last+1], Q(1, cells))
        if pairs != length**2:
            raise AssertionError("the selected finite collision is not maximal")
        if kind == "dyadic":
            denominator = delta.denominator
            if denominator & (denominator-1):
                raise AssertionError("dyadic control has a non-dyadic denominator")
            if source[horizon] != changed[horizon] or companion[horizon] != changed_companion[horizon]:
                raise AssertionError("dyadic control did not coalesce")
        else:
            denominator = delta.denominator
            while denominator % 3 == 0:
                denominator //= 3
            if denominator != 1 or delta.denominator == 1:
                raise AssertionError("odd control has no nontrivial pure 3-primary shift")
            if gcd(16, delta.denominator) != 1 or source[horizon] == changed[horizon]:
                raise AssertionError("odd control failed its noncoalescence contract")
            if any(x.denominator % 2 == 0 for x in changed+changed_companion):
                raise AssertionError("odd-carrier control acquired an even denominator")
        # Alter only one wire at time zero: the same-forcing differential
        # formula must detect this mutation, not mislabel it a common shift.
        mutant, _ = trajectory(gamma+delta+Q(1, 17), 2)
        if all((z-x) % 1 == gamma for x, z in zip(changed[:3], mutant)):
            raise AssertionError("one-wire mutation was not detected")
        results.append({
            "kind": kind,
            "initial_zero_changed": True,
            "exact_four_pole_forcing_retained": True,
            "synchronized_differential": str(gamma),
            "differential_time_samples_checked": horizon+1,
            "both_literal_carry_prefix_lengths": carry_prefix,
            "ordered_close_pairs": pairs,
            "scaled_collision": str(Q(cells*pairs, length**2)),
            "odd_carrier_retained": kind == "odd_3_primary",
            "primary_components_preserved": "all odd primes" if kind == "dyadic" else "all primes except 3",
            "coalescence": {"by_time": horizon} if kind == "dyadic" else "never (unit action on nontrivial 3-primary shift)",
            "shift_numerator_bits": delta.numerator.bit_length(),
            "shift_denominator_bits": delta.denominator.bit_length(),
            "shift_sha256": fraction_digest(delta),
            "odd_depth_before_reduction": odd_depth if kind == "odd_3_primary" else None,
            "asymptotic_normality_claim": "none",
        })
    result = {
        "status": "VERIFIED_FINITE",
        "pi_normality": "OPEN",
        "source_scope": "original forcing, deliberately changed common initial state",
        "inherited_control": "PR266 dyadic control; two-wire extension and odd-grid alternative",
        "prime": p, "first_state": first, "last_state": last,
        "length": length, "cells": cells,
        "actual_ordered_close_pairs": actual_pairs,
        "actual_scaled_collision": str(Q(cells*actual_pairs, length**2)),
        "pair_counter_independent_calibrations": calibrations,
        "variants": results,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(json.dumps({"status": "VERIFIED_FINITE", "actual_pairs": actual_pairs,
                          "changed_pairs_both_variants": length**2,
                          "both_wire_carry_prefixes": carry_prefix}, sort_keys=True))
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
