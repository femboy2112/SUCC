"""Seed-alias classification for the authentic BBP orbit (Operation Main XVI).

Research-only. Not a pi digit sampler and not a proof of normality or RH. Python >= 3.10.

Authentic four-pole source and native clock (unchanged, U_0 = s, authentic s = 0):

    R(a) = 4/a - 2/(a+3) - 1/(a+4) - 1/(a+5),   r(n) = R(8n-7),
    U_0(s) = s,   U_n(s) = 16 U_{n-1}(s) + r(n).

The affine recurrence gives, for every n >= 0,

    U_n(s) = U_n(0) + 16^n s        (SA-1, exact).

Hence the selected circle phase  e(h U_n(s)) = exp(2*pi*i*h*U_n(s))  depends on the changed seed
only through  16^n s (mod 1).  This module classifies seed distinguishability relative to the
circle-phase readout and the Weyl-sum magnitude, exactly over Q, and exhibits the literal carry
as the one datum that separates circle-aliased seeds (SA/OB obstruction).

Everything here is exact rational arithmetic except the explicit coherent counterseed s* = -pi/16,
which is handled in high-precision mpmath in independent_oracle_xvi.py.
"""
from __future__ import annotations
from fractions import Fraction as Fr
from math import gcd

POLES = ((0, 4), (3, -2), (4, -1), (5, -1))


def R(a) -> Fr:
    a = Fr(a)
    if a <= 0:
        raise ValueError('positive source parameter required')
    return sum((Fr(c) / (a + d) for d, c in POLES), Fr())


def r_clock(n) -> Fr:
    if n < 1:
        raise ValueError('native BBP clock starts at 1')
    return R(8 * n - 7)


def U(n, s=Fr(0)) -> Fr:
    """Exact selected orbit value U_n(s) (rational for rational s)."""
    if n < 0:
        raise ValueError('n must be nonnegative')
    x = Fr(s)
    for k in range(1, n + 1):
        x = 16 * x + r_clock(k)
    return x


def frac(x) -> Fr:
    x = Fr(x)
    return x - (x.numerator // x.denominator)


def displacement(n, s) -> Fr:
    """U_n(s) - U_n(0) = 16^n s  (SA-1), computed from the affine law (no orbit needed)."""
    return 16 ** n * Fr(s)


def phase_turn(n, h, s=Fr(0)) -> Fr:
    """The fractional turn of e(h U_n(s)); e(h U_n(s)) = exp(2*pi*i*phase_turn)."""
    return frac(Fr(h) * U(n, s))


def circle_aliased(s, s2=Fr(0), n_from=1, n_to=8, hmax=4) -> bool:
    """True iff e(h U_n(s)) == e(h U_n(s2)) for all n in [n_from, n_to], |h| in [1, hmax]."""
    for n in range(n_from, n_to + 1):
        for h in range(1, hmax + 1):
            if frac(Fr(h) * (U(n, s) - U(n, s2))) != 0:
                return False
    return True


def alias_onset(s) -> int | None:
    """Least N0 with 16^N0 * s in Z (so e(h U_n(s)) = e(h U_n(0)) for all n >= N0, all h in Z).

    Returns the 16-adic onset for s in Z[1/16]; None if s is not in Z[1/16] (no finite onset).
    """
    s = Fr(s)
    d = s.denominator
    # d must be a power of 2 (16-adic); 16^N0 kills it when 2^(4*N0) >= 2-adic valuation of d
    if d & (d - 1) != 0:            # d not a power of two -> not in Z[1/16]
        return None
    v2 = d.bit_length() - 1          # d = 2^v2
    N0 = (v2 + 3) // 4               # least N0 with 4*N0 >= v2
    assert (16 ** N0 * s).denominator == 1
    return N0


def constant_twist_value(s) -> Fr | None:
    """If s=p/q with gcd(q,16)=1 and 16==1 (mod q) (i.e. q | 15), the displacement 16^n s has a
    constant fractional part c = frac(s) for every n; returns c. Otherwise None.
    """
    s = Fr(s)
    q = s.denominator
    if gcd(q, 16) != 1:
        return None
    if 15 % q != 0:                  # need 16 == 1 (mod q), i.e. q | 15
        return None
    return frac(s)


def twist_period(s) -> int:
    """Period of the fractional part of 16^n s in n (eventual period of the circle twist).

    For s = p/q with gcd(q,16)=1 it is ord_q(16); = 1 exactly for the constant twists (q | 15).
    """
    s = Fr(s)
    q = s.denominator
    base = frac(s)
    seen = []
    n = 1
    cur = frac(16 * base)
    # iterate the map t -> frac(16 t) until a cycle closes
    vals = [base]
    t = base
    while True:
        t = frac(16 * t)
        if t in vals:
            return len(vals) - vals.index(t)
        vals.append(t)
        if len(vals) > 10000:
            raise RuntimeError('no period found (seed not eventually periodic under x16)')


def weyl_magnitude_invariant(s, s2=Fr(0), N=12, h=1) -> bool:
    """Exact test that |sum_{n<=N} e(h U_n(s))| == |sum e(h U_n(s2))| for a CONSTANT twist.

    True iff the per-n displacement turn h*(U_n(s)-U_n(s2)) is the SAME constant c for all n,
    in which case the two sums differ by the global unit factor e(c) and share their modulus.
    """
    turns = {frac(Fr(h) * (U(n, s) - U(n, s2))) for n in range(1, N + 1)}
    return len(turns) == 1


def carry(n, s=Fr(0)) -> int:
    """Literal carry kappa_n(s) = 16{U_{n-1}(s)} + r(n) - {U_n(s)} in Z (integer-lift mark)."""
    if n < 1:
        raise ValueError('carry only for n>=1')
    b = 16 * frac(U(n - 1, s)) + r_clock(n) - frac(U(n, s))
    if b.denominator != 1:
        raise AssertionError('noninteger carry')
    return int(b)


def carry_distinguishes(s, s2=Fr(0), n_to=8) -> bool:
    """True iff the literal carry separates two circle-aliased seeds (the OB obstruction)."""
    return [carry(n, s) for n in range(1, n_to + 1)] != [carry(n, s2) for n in range(1, n_to + 1)]


def classify(s) -> dict:
    """Full seed-distinguishability fingerprint of a rational changed seed s, relative to s=0."""
    s = Fr(s)
    onset = alias_onset(s)
    ctw = constant_twist_value(s)
    return {
        'seed': s,
        'in_Z[1/16]': onset is not None,
        'circle_alias_onset_N0': onset,                 # SA-2/SA-3: exact/eventual alias
        'constant_twist_value': ctw,                    # SA-4: constant character twist (q|15)
        'twist_period': (twist_period(s) if gcd(s.denominator, 16) == 1 else None),
        'weyl_magnitude_invariant': (ctw is not None),  # SA-5: magnitude-blind iff constant twist
        'carry_distinguishes_from_authentic': (onset is not None and carry_distinguishes(s)),
    }


if __name__ == '__main__':
    for s in (Fr(1, 16), Fr(1, 256), Fr(1, 3), Fr(2, 5), Fr(1, 7), Fr(-5, 3)):
        print(classify(s))
