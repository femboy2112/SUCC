"""Exact certificate construction; acceptance belongs to lonely_runner_verify.

This module uses Fraction and a greedy interval sweep. The verifier uses its
own integer-pair arithmetic and does not import this module. Neither searching
nor failure to find a chain proves nonexistence for other configurations.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from functools import reduce


def pair(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def cover_certificate(velocities, shifts, delta, *, source=None):
    """Produce a source-labelled covering chain, or raise ValueError at a gap."""
    if not isinstance(source, dict) or not source:
        raise ValueError("nonempty source metadata required")
    velocities = list(velocities)
    shifts = list(shifts)
    if not velocities or len(velocities) != len(shifts):
        raise ValueError("nonempty matching source arrays required")
    if any(type(v) is not int or v <= 0 for v in velocities):
        raise ValueError("positive integer velocities required")
    if len(set(velocities)) != len(velocities):
        raise ValueError("distinct velocities required")
    if any(type(s) not in (int, Fraction) for s in shifts):
        raise ValueError("exact rational shifts required")
    if type(delta) not in (int, Fraction):
        raise ValueError("exact rational radius required")
    shifts = [Fraction(s) % 1 for s in shifts]
    delta = Fraction(delta)
    if not 0 < delta < Fraction(1, 2):
        raise ValueError("radius must lie strictly between zero and one half")
    arcs = []
    for i, (v, s) in enumerate(zip(velocities, shifts)):
        for k in range(v + 2):
            left = max(Fraction(0), (k - s - delta) / v)
            right = min(Fraction(1), (k - s + delta) / v)
            if left < right:
                arcs.append((left, right, i, k))
    arcs.sort()
    selected, inequalities = [], []
    position, j = Fraction(0), 0
    while position < 1:
        best = None
        while j < len(arcs) and arcs[j][0] <= position:
            arc = arcs[j]
            if arc[1] > position and (best is None or arc[1] > best[1]):
                best = arc
            j += 1
        if best is None:
            raise ValueError(f"uncovered interval begins at {position}")
        left, right, i, k = best
        selected.append({"runner": i, "winding": k,
                         "left": pair(left), "right": pair(right)})
        inequalities.append({"left_cross": left.numerator * position.denominator,
                             "right_cross": position.numerator * left.denominator})
        position = right
    result = {
        "schema": "SUCC-shifted-cover-v1", "n": len(velocities),
        "velocities": velocities, "shifts": [pair(s) for s in shifts],
        "delta": pair(delta), "threshold": [1, len(velocities) + 1],
        "velocity_gcd": reduce(gcd, velocities), "source": source or {},
        "intervals": selected, "ordering": list(range(len(selected))),
        "inequalities": inequalities,
    }
    result["payload_sha256"] = sha256(json.dumps(
        result, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")).hexdigest()
    return result


def poliakova_configuration(N: int):
    """Section 3, arXiv:2609.23952v1, scale b=1; N >= 96 only.

    Returns N-1 runners at radius 1/(N+1). This is a published control,
    not a newly discovered construction.
    """
    if type(N) is not int or N < 96:
        raise ValueError("published rule requires N >= 96")
    delta = Fraction(1, N + 1)
    velocities, shifts = [], []
    for v in range(2, 2 * N + 1, 2):
        if v in (8, 32, 192):
            continue
        shift = ((1 + delta) / 2 if v in (12, 24, 48, 96)
                 else -delta if v in (16, 64) else Fraction(0))
        velocities.append(v)
        shifts.append(shift % 1)
    velocities += [3, 9]
    shifts += [Fraction(1, 4), Fraction(1, 4)]
    return velocities, shifts, delta


def bcs_five_configuration():
    """BCS arXiv:2603.24784v4, Fig. 1 / Proposition 5.11 data."""
    return list(range(1, 6)), [Fraction(k, 94) for k in (0, 46, 38, 47, 72)], Fraction(15, 94)
