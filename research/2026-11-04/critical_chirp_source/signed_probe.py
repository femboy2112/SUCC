"""Exact rational certificates for finite critical maximal BBP sums.

No floating point, supplied pi digits, or asymptotic inference is used.
See INSTRUMENT.md for every approximation budget.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from math import factorial, isqrt, lcm
from pathlib import Path

GRID = 1 << 80
OUTPUT = 1 << 60
CHAR_ERROR = F(1, 1 << 50)


def forcing(n: int) -> F:
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def source_epoch(A: int) -> tuple[F, ...]:
    """Direct circle recurrence, retaining all four signed poles."""
    x = F(0)
    out = []
    for n in range(1, 2*A):
        x = (16*x+forcing(n)) % 1
        if n >= A:
            out.append(x)
    return tuple(out)


def integer_epoch(A: int) -> tuple[F, ...]:
    """Independent polynomial source and common integer LCM register."""
    pairs = []
    conductor = 1
    for n in range(1, 2*A):
        r = F(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
        pairs.append((r.numerator, r.denominator))
        conductor = lcm(conductor, r.denominator)
    v = 0
    out = []
    for n, (a, b) in enumerate(pairs, 1):
        v = (16*v+a*(conductor//b)) % conductor
        if n >= A:
            out.append(F(v, conductor))
    return tuple(out)


def critical_schedule(A: int, h: int) -> tuple[int, int]:
    """Certify floor(log_16(A^2 log A / |h|)) for dyadic A."""
    if type(A) is not int or A < 2 or A & (A-1) or type(h) is not int or not h:
        raise ValueError("dyadic A>=2 and nonzero integer h required")
    k = A.bit_length()-1
    terms = 40
    low = 2*sum((F(1, (2*j+1)*3**(2*j+1)) for j in range(terms)), F(0))
    high = low+F(9, 4*(2*terms+1)*3**(2*terms+1))
    low *= k*A*A
    high *= k*A*A
    H, depth = abs(h), 0
    if H > low:
        raise ValueError("no certified nonnegative depth")
    while 16*H <= low:
        H *= 16
        depth += 1
    if not H <= low <= high < 16*H:
        raise ArithmeticError("increase log precision to resolve radix boundary")
    return depth, H


def arctan_bounds(q: int, terms: int = 48) -> tuple[F, F]:
    s = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(terms)), F(0))
    other = s+F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(s, other), max(s, other)


@lru_cache(maxsize=1)
def pi_grid() -> F:
    a, b = arctan_bounds(5)
    c, d = arctan_bounds(239)
    low, high = 16*a-4*d, 16*b-4*c
    middle = (low+high)/2
    p = F((middle.numerator*GRID)//middle.denominator, GRID)
    assert 3 < low < high < F(22, 7)
    assert max(abs(p-low), abs(p-high)) < F(2, GRID)
    return p


def character_grid(phase: F, phase_radius: F = F(0)) -> tuple[int, int]:
    """A point within CHAR_ERROR of e(phase +/- phase_radius)."""
    if phase_radius < 0:
        raise ValueError("negative enclosure radius")
    x = (F(phase)+F(1, 2)) % 1-F(1, 2)
    q = F((x.numerator*GRID)//x.denominator, GRID)
    angle = 2*pi_grid()*q
    assert abs(angle) < 4
    # Degree 47 Taylor polynomial, recurrence independent of libm/mpmath.
    real, imag, term = F(0), F(0), F(1)
    for j in range(48):
        if j:
            term *= angle/j
        if j % 4 == 0:
            real += term
        elif j % 4 == 1:
            imag += term
        elif j % 4 == 2:
            real -= term
        else:
            imag -= term
    # Two component Lagrange errors, phase/pi rounding, output rounding.
    error = F(14, GRID)+2*F(4**48, factorial(48))+F(2, OUTPUT)+7*phase_radius
    if error > CHAR_ERROR:
        raise ArithmeticError("phase enclosure exceeds fixed character budget")
    return ((real.numerator*OUTPUT)//real.denominator,
            (imag.numerator*OUTPUT)//imag.denominator)


def maximal_certificate(points: list[tuple[int, int]]) -> dict:
    """Enumerate every prefix chord; integer square root encloses diameter."""
    A = len(points)
    if not A:
        raise ValueError("nonempty epoch required")
    prefixes = [(0, 0)]
    x = y = 0
    for dx, dy in points:
        x += dx
        y += dy
        prefixes.append((x, y))
    best, witness = -1, None
    for b in range(1, A+1):
        x, y = prefixes[b]
        for a in range(b):
            u, v = prefixes[a]
            square = (x-u)**2+(y-v)**2
            if square > best:
                best, witness = square, (a, b)
    root = isqrt(best)
    lower = max(F(0), F(root, A*OUTPUT)-CHAR_ERROR)
    upper = min(F(1), F(root+1, A*OUTPUT)+CHAR_ERROR)
    return {"M_lower": str(lower), "M_upper": str(upper),
            "grid_witness_offsets": list(witness),
            "grid_max_squared": str(best), "intervals_checked": A*(A+1)//2}


def tail_interval(n: int, terms: int = 24) -> tuple[F, F]:
    low = sum((forcing(n+k)/16**k for k in range(1, terms+1)), F(0))
    high = low+forcing(n+terms+1)*F(1, 15*16**terms)
    return low, high


def outward_decimal(x: F, places: int = 9, upper: bool = False) -> str:
    scale = 10**places
    scaled = x*scale
    v = scaled.numerator//scaled.denominator
    if upper and scaled != v:
        v += 1
    sign = "-" if v < 0 else ""
    v = abs(v)
    return f"{sign}{v//scale}.{v%scale:0{places}d}"


def run_case(A: int, h: int, phases: tuple[F, ...]) -> dict:
    j, H = critical_schedule(A, h)
    signed_H = H if h > 0 else -H
    authentic = maximal_certificate([character_grid(signed_H*x) for x in phases])
    coherent_points = []
    for n in range(A, 2*A):
        low, high = tail_interval(n)
        coherent_points.append(character_grid(-signed_H*(low+high)/2, H*(high-low)/2))
    coherent = maximal_certificate(coherent_points)
    for row in (authentic, coherent):
        low = F(row["M_lower"])*F(H, A*A)
        high = F(row["M_upper"])*F(H, A*A)
        row["R_lower"] = str(low)
        row["R_upper"] = str(high)
        row["R_decimal_outward"] = [outward_decimal(low), outward_decimal(high, upper=True)]
    phase_blob = "\n".join(str(x) for x in phases).encode()
    return {"A": A, "h": h, "j": j, "H": H, "Lambda": str(F(H, A*A)),
            "phase_sha256": hashlib.sha256(phase_blob).hexdigest(),
            "zero_seed": authentic, "coherent_changed_seed": coherent}


def receipt(epochs=(128, 256, 512), characters=(1, 3, -5, 17)) -> dict:
    rows = []
    for A in epochs:
        phases = source_epoch(A)
        assert phases == integer_epoch(A), "independent source oracles disagree"
        rows.extend(run_case(A, h, phases) for h in characters)
    return {"status": "EXACT_FINITE_MAXIMAL_SIGNED_CERTIFICATES_ONLY",
            "source_base": "c9dfcdf057c4870f113e898464e4821c2ff5fedf",
            "character_error": str(CHAR_ERROR), "rows": rows,
            "normality_proved": False, "critical_ratchet_proved": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    result = receipt()
    if args.write:
        args.write.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    else:
        if result != json.loads(args.verify.read_text()):
            raise SystemExit("FINITE_SIGNED_CERTIFICATE_MISMATCH")
        print("FINITE_SIGNED_MAXIMAL_CERTIFICATES_VERIFIED")
