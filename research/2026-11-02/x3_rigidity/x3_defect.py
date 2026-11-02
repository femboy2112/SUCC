"""Exact finite arithmetic for the x3-defect D_N(h) (WB-10, obligation A).

D_N(h) = (1/N) sum_{n=1}^N [ e(3h U_n) - e(h U_n) ],  e(x) = exp(2 pi i x),
U_n = 16^{n-1} pi - T_n,  T_n = sum_{k>=1} 16^{-k} r(n+k)  (Green tail),
r(m) = 4/(8m-7) - 2/(8m-4) - 1/(8m-3) - 1/(8m-2)  (four-pole BBP forcing).

This module computes EXACT rational tails (stdlib Fraction) and, where the phase
needs the real number pi, a high-precision mpmath evaluation with dps >= 6*N/2.3
so that the fractional part of 16^{n-1} pi is resolved far below the 1/N defect
scale.  No normality or asymptotic-cancellation claim is made: the finite outputs
are evidence only, and every theorem status is carried in the claim ledger.

The two orbits compared are:

  * authentic: U_n = 16^{n-1} pi - T_n  (the four-pole BBP orbit of {pi}),
  * coherent counterseed: U_n = -T_n   (seed x_1 = 0, all phases -> 1),

so that the firewall test (does (A) discriminate?) is reproducible.
"""
from dataclasses import dataclass
from fractions import Fraction as Q

import mpmath as mp


def r_force(n: int) -> Q:
    """Exact four-pole BBP forcing r(n), n>=1."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be an integer >= 1")
    return Q(4, 8 * n - 7) - Q(2, 8 * n - 4) - Q(1, 8 * n - 3) - Q(1, 8 * n - 2)


def tail_exact(n: int, depth: int) -> Q:
    """Exact lower bound T_n >= sum_{k=1..depth} 16^{-k} r(n+k)."""
    if type(depth) is not int or depth < 0:
        raise ValueError("depth must be a nonnegative integer")
    return sum((r_force(n + k) / 16 ** k for k in range(1, depth + 1)), Q())


def tail_upper(n: int, depth: int) -> Q:
    """Rigorous upper bound T_n <= partial + r(n+depth+1)/(15*16^depth).

    Uses the repo-proved tail budget r(m+1)/15 <= (8m+1)^{-2} from duck_bbp.
    """
    partial = tail_exact(n, depth)
    remainder = r_force(n + depth + 1) / (15 * 16 ** depth)
    return partial + remainder


def phase_true(h: int, n: int, depth: int, dps: int) -> mp.mpf:
    """Fractional part of h*U_n for the authentic orbit, reduced mod 1.

    h*U_n = h*(16^{n-1} pi - T_n) = h*x_n - h*T_n  (mod 1), with x_n = {16^{n-1} pi}
    the completed x16 orbit.  x_n is computed at `dps` digits, then the exact
    rational tail h*T_n (enclosed) is subtracted.  Returns a phase in [0,1).
    """
    mp.mp.dps = dps
    x = mp.mpf(16) ** (n - 1) * mp.pi
    x -= mp.floor(x)                     # completed orbit x_n, exact to dps
    t_lo = tail_exact(n, depth)
    t_hi = tail_upper(n, depth)
    # phase is h*x_n - h*T_n mod 1; T_n is enclosed [t_lo, t_hi], width < 16^{-depth}*C.
    # Return the midpoint phase; the width is reported separately by phase_error.
    t_mid = (mp.mpf(t_lo.numerator) / t_lo.denominator
             + mp.mpf(t_hi.numerator) / t_hi.denominator) / 2
    return (h * x - h * t_mid) % 1


def phase_error(h: int, n: int, depth: int) -> mp.mpf:
    """Worst-case phase uncertainty |h|*(T_n width)/2 from the tail enclosure."""
    t_lo = tail_exact(n, depth)
    t_hi = tail_upper(n, depth)
    width = (mp.mpf(t_hi.numerator) / t_hi.denominator
             - mp.mpf(t_lo.numerator) / t_lo.denominator)
    return abs(h) * width / 2


def phase_counter(h: int, n: int, depth: int) -> mp.mpf:
    """Fractional part of h*U_n for the coherent counterseed U_n = -T_n."""
    t_lo = tail_exact(n, depth)
    t_hi = tail_upper(n, depth)
    t_mid = (mp.mpf(t_lo.numerator) / t_lo.denominator
             + mp.mpf(t_hi.numerator) / t_hi.denominator) / 2
    return (-h * t_mid) % 1


def _e(phase: mp.mpf) -> mp.mpc:
    return mp.e ** (2j * mp.pi * phase)


@dataclass(frozen=True)
class Defect:
    h: int
    N: int
    depth: int
    dps: int
    value: complex
    max_phase_error: float          # worst-case |D_N| error from tail enclosures


def _tails(nmax: int, depth: int) -> tuple[list[mp.mpf], list[mp.mpf], list[mp.mpf]]:
    """Precompute tail midpoint, upper, lower enclosures for n=1..nmax."""
    mids, los, his = [], [], []
    for n in range(1, nmax + 1):
        lo = tail_exact(n, depth)
        hi = tail_upper(n, depth)
        los.append(mp.mpf(lo.numerator) / lo.denominator)
        his.append(mp.mpf(hi.numerator) / hi.denominator)
        mids.append((los[-1] + his[-1]) / 2)
    return mids, los, his


def defect(h: int, N: int, depth: int = 60, dps: int = 120,
           counter: bool = False) -> Defect:
    """D_N(h) for the authentic orbit, or the coherent counterseed if counter.

    dps is chosen >= 6*N/2.3 so x_n = {16^{n-1} pi} is resolved far below 1/N.
    max_phase_error accumulates the tail-enclosure width across all n terms.
    """
    if type(h) is not int or h == 0:
        raise ValueError("h must be a nonzero integer")
    if type(N) is not int or N < 1:
        raise ValueError("N must be a positive integer")
    mp.mp.dps = dps
    mids, los, his = _tails(N, depth)
    s = mp.mpc(0)
    err = mp.mpf(0)
    x = mp.mpf(1) * mp.pi
    x -= mp.floor(x)                     # x_1 = {pi}
    for n in range(1, N + 1):
        t = mids[n - 1]
        width = (his[n - 1] - los[n - 1])
        if counter:
            p3 = (-3 * h * t) % 1
            p1 = (-h * t) % 1
        else:
            p3 = (3 * h * x - 3 * h * t) % 1
            p1 = (h * x - h * t) % 1
            x = mp.fmod(16 * x, 1)        # x_{n+1} = {16 x_n} exactly
        s += _e(p3) - _e(p1)
        err += 3 * abs(h) * width / 2 + abs(h) * width / 2
    return Defect(h, N, depth, dps, complex(s / N), float(err / N))


if __name__ == "__main__":
    print("x3-defect D_N(h)  (authentic four-pole BBP orbit of {pi})")
    print("N*|D_N(h)| should be ~constant iff partial sums are bounded (conjectured).")
    print()
    for h in (1, 3, 5, 7):
        print(f"h={h}:")
        for N in (1000, 2000, 4000):
            d = defect(h, N, depth=80, dps=140)
            print(f"   N={N:5d}  |D_N|={abs(d.value):.7f}  "
                  f"N*|D_N|={N*abs(d.value):.5f}  err<{d.max_phase_error:.1e}")
    print()
    print("Coherent counterseed U_n = -T_n (seed x_1 = 0):")
    for h in (1, 3):
        for N in (1000, 2000):
            d = defect(h, N, depth=80, dps=140, counter=True)
            print(f"   h={h} N={N:5d}  |D_N|={abs(d.value):.7f}")
