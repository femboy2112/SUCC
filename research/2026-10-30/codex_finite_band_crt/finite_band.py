"""Finite-band cylinder certificate. Research calibration, not a pi-normality proof.

The associated paper proofs are in FINITE_BAND_CERTIFICATE.md.
This implementation tests finite identities numerically; Python floats are not
interval-proof authority for arbitrary sizes.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from math import pi, sin, sqrt
from cmath import exp

COEFFS = (4, -2, -1, -1)
OFFSETS = (1, 4, 5, 6)


def r(n: int) -> Fraction:
    assert n >= 1
    return sum((Fraction(c, 8 * (n - 1) + d) for c, d in zip(COEFFS, OFFSETS)), Fraction(0))


def prefix(N: int) -> list[Fraction]:
    u = Fraction(0)
    out = []
    for n in range(1, N + 1):
        u = 16*u + r(n)
        out.append(u % 1)
    return out


def tail_truncated(n: int, R: int = 10) -> Fraction:
    return sum((Fraction(1, 16**j) * r(n+j) for j in range(1, R+1)), Fraction(0))


def hard_collision(points: list[Fraction], q: int) -> Fraction:
    assert q > 1 and points
    n = len(points)
    cells = Counter((q * (x % 1)).numerator // (q * (x % 1)).denominator for x in points)
    # The preceding ratio computes floor(q*x) for exact fractions.
    return Fraction(q * sum(v*v for v in cells.values()), n*n)


def fejer(t: float, H: int) -> float:
    assert H >= 2
    t = t % 1.0
    if min(t, 1-t) < 1e-12:
        return float(H)
    return sin(pi*H*t)**2 / (H*sin(pi*t)**2)


def fejer_pair_kernel(points: list[Fraction], H: int) -> float:
    xs = [float(x % 1) for x in points]
    n = len(xs)
    return sum(fejer(x-y, H) for x in xs for y in xs) / (n*n)


def fejer_pair_fourier(points: list[Fraction], H: int) -> float:
    xs = [float(x % 1) for x in points]
    n = len(xs)
    value = 1.0
    for h in range(1,H):
        w = 1.0 - h/H
        s = sum(exp(2j*pi*h*x) for x in xs) / n
        value += 2*w*(s.real*s.real+s.imag*s.imag)
    return value


def max_unit_arc_mass(points: list[Fraction], H: int) -> Fraction:
    """Exact maximum number of points in any (closed) circle arc of length 1/H.

    Closed endpoints make this an upper bound for half-open intervals.
    """
    xs = sorted((x % 1 for x in points))
    n = len(xs)
    ys = xs + [x + 1 for x in xs]
    maxcount = 0
    j = 0
    for i in range(n):
        if j < i: j = i
        while j < i+n and ys[j] - ys[i] <= Fraction(1, H):
            j += 1
        maxcount = max(maxcount, j-i)
    return Fraction(maxcount, n)


def stoneham_surrogate(conductor: int, p: int) -> list[Fraction]:
    """Exact source-rational Stoneham stage, from the pulse recurrence."""
    assert conductor in (3, 5)
    limit=conductor**(p+1)
    x=Fraction(0)
    pulse_times={conductor**j:j for j in range(1, p+1)}
    out=[]
    for n in range(1,limit):
        x=(16*x+Fraction(1,n) if n in pulse_times else 16*x) % 1
        if n>=conductor**p: out.append(x)
    return out


def test_summary() -> dict:
    points = prefix(48)
    q = 16
    H = q//2
    return {
        "N":len(points), "q":q, "H":H,
        "hard_Q":float(hard_collision(points,q)),
        "Fejer_band":fejer_pair_fourier(points,H),
        "hard_bound":(pi*pi/2)*fejer_pair_fourier(points,H),
        "calibration_status":"numerical check only"
    }

if __name__ == "__main__":
    import json
    print(json.dumps(test_summary(), indent=2))
