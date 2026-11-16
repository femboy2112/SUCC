"""Original BBP chiral 2-adic return loop and time-labelled circle interference.

Only exact Fraction arithmetic is used for theorem-bearing modular claims.
Complex phase calculations are illustrative finite smoke, never interval certificates.
No π normality or signed all-shell saving is inferred.
"""
from __future__ import annotations
from fractions import Fraction
from functools import lru_cache
from cmath import exp, pi

WEIGHTS = (4, -2, -1, -1)
POLES = (7, 4, 3, 2)


def forcing(t: int) -> Fraction:
    """The original four-pole BBP forcing, on all integer t in Z_2."""
    return sum((Fraction(c, 8*t-p) for c, p in zip(WEIGHTS, POLES)), Fraction(0))


def forcing_compact(t: int) -> Fraction:
    return Fraction(120*t*t-89*t+16, (2*t-1)*(4*t-1)*(8*t-7)*(8*t-3))


def source_states(N: int) -> list[Fraction]:
    if N < 0:
        raise ValueError('N must be nonnegative')
    out = [Fraction(0)]
    for n in range(1, N+1):
        out.append(16*out[-1]+forcing(n))
    return out


def mod_fraction(x: Fraction, q: int) -> int:
    if q < 1 or (q & (q-1)):
        raise ValueError('q must be a positive power of two')
    if x.denominator % 2 == 0:
        raise ValueError('2-adic fractional denominator must be odd')
    return x.numerator*pow(x.denominator, -1, q) % q


def return_jet(states: list[Fraction], n: int, k: int, m: int = 4) -> int:
    """Return displacement /16**k modulo 2**m, requiring UNREDUCED U."""
    q = 16**k
    if n < 0 or k < 1 or n+q >= len(states):
        raise ValueError('insufficient original states')
    return mod_fraction((states[n+q]-states[n])/q, 2**m)


def source_chirality(n: int) -> int:
    return 1 if n % 4 in (0, 1) else -1


def expected_jet16(n: int) -> int:
    return 7 + 4 * source_chirality(n)


def expected_jet32(n: int) -> int:
    table = [27, 11, 19, 19, 11, 27, 3, 3]
    return table[n % 8]


def expected_ratio32(n: int) -> int:
    """(J_(n+2)-J_n) mod32: 24 even, 8 odd."""
    return 24 if n % 2 == 0 else 8


def phase(J: int, q: int = 16) -> complex:
    return exp(2j*pi*J/q)


def time_projection(n: int) -> tuple[int, int]:
    """The two source-selected Walsh bits on the 4-clock."""
    return (1 if n%2 == 0 else -1, source_chirality(n))


def four_walsh_channels(values: list[complex]) -> dict[str, complex]:
    """The 4 independent characters for a single 4-state source clock."""
    if len(values) != 4:
        raise ValueError('need exactly four chronological values')
    return {
        'dc': sum(values)/4,
        'low': sum((1 if n%2==0 else -1)*values[n] for n in range(4))/4,
        'high': sum(source_chirality(n)*values[n] for n in range(4))/4,
        'joint': sum((1 if n%2==0 else -1)*source_chirality(n)*values[n] for n in range(4))/4,
    }


def invert_walsh_channels(ch: dict[str, complex]) -> list[complex]:
    return [ch['dc'] + (1 if n%2==0 else -1)*ch['low']
            + source_chirality(n)*ch['high']
            + (1 if n%2==0 else -1)*source_chirality(n)*ch['joint']
            for n in range(4)]


def g(t: int) -> int:
    return 2*t*t


def forcing_mutant(t: int) -> Fraction:
    """Exact coboundary mutation preserving U0=0 and 2-adic isometry."""
    return forcing(t) + g(t) - 16*g(t-1)


def mutant_states(N: int) -> list[Fraction]:
    out = [Fraction(0)]
    for n in range(1,N+1):
        out.append(16*out[-1]+forcing_mutant(n))
    return out


def tail_interval(n: int, depth: int = 12) -> tuple[Fraction, Fraction]:
    """Rigorous real T_n interval using unchanged original source positive tail."""
    if n < 0 or depth < 0:
        raise ValueError('nonnegative n and depth required')
    lo = sum((forcing(n+j)/16**j for j in range(1, depth+1)), Fraction(0))
    return lo, lo+forcing(n+depth+1)/(15*16**depth)


def circle_midpoint(states: list[Fraction], n: int, depth: int = 12) -> float:
    a, b = tail_interval(n,depth)
    z = (states[n] + (a+b)/2) % 1
    return float(z)


def complex_loop_signal(states: list[Fraction], n: int, k: int, h: int = 1,
                        depth: int = 12) -> complex:
    """Smoke only; 4-time source-coupled loop, not a certified complex interval."""
    q = 16**k
    if n+q >= len(states):
        raise ValueError('insufficient states')
    j = return_jet(states,n,k)
    z0 = circle_midpoint(states,n,depth)
    z1 = circle_midpoint(states,n+q,depth)
    return phase(j)*exp(2j*pi*h*(z1-z0))


def squared_two_path_output(v0: complex, v2: complex) -> float:
    return abs(v0+v2)**2


def v2_fraction(a: Fraction) -> int:
    if not a:
        raise ValueError('v2(0) is infinity')
    def v(x: int) -> int:
        x=abs(x)
        return (x & -x).bit_length()-1
    return v(a.numerator)-v(a.denominator)
