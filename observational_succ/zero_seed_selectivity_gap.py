"""Zero-seed selectivity: the exact separation gap between the true orbit and
the p-integral rational shadow (PPP-08).

Front F, the crux obstruction.  The zero seed U_0=0 selects the completed orbit
  16^(n-1) pi,   while the PPP-08 shadow seed s_A selects
  16^n (s_A + pi/16)  with  s_A = -floor(D alpha_N)/D  rational.

Both completed orbits are IRRATIONAL (pi/16 is irrational; s_A + pi/16 is
rational + irrational).  The shadow is not literally the zero orbit: it is an
astronomically close rational-approximation shadow whose completed digits vanish
on the epoch.  This module supplies an EXACT upper gap bound.  The original
assertion that every separation requires an effective irrationality measure
is withdrawn: lifted orbit differences are exactly 16**n times the seed
difference, and finite digit certification terminates by shrinking source
intervals and irrationality.  A quantitative uniform rate is a distinct
question.  Original-zero parity balance stays OPEN.
"""
from __future__ import annotations

from fractions import Fraction as Q

from observational_succ import duck_bbp


def shadow_gap_bound(A: int, p: int) -> Q:
    """Exact bound on |s_A + pi/16| for the PPP-08 shadow.

    s_A + pi/16 = (pi/16 - alpha_N) + (alpha_N - floor(D alpha_N)/D)
                = tail_error          + {D alpha_N}/D
    so  0 < |s_A + pi/16| <= r(N+1)/(15*16^N) + 1/D.
    """
    if type(A) is not int or A < 1 or type(p) is not int or p < 2:
        raise ValueError('positive epoch A and integer p>=2 required')
    N = 2 * A + 16
    D = p * 16 ** (2 * A + 48) + 1
    tail = duck_bbp.source_tail_budget(N) / 16 ** N
    return tail + Q(1, D)


def completed_digit_gap(A: int, p: int) -> Q:
    """Exact bound on |16^n (s_A + pi/16)| for n in [A, 2A+8)."""
    # scaled by 16^n <= 16^(2A+7); the gap stays < 1/16 on the epoch.
    gap = shadow_gap_bound(A, p)
    return 16 ** (2 * A + 7) * gap


def separation_requires_irrationality_measure() -> str:
    """Historical API name retained; return the explicit correction to F-9."""
    return (
        'F-9 necessity claim WITHDRAWN. An effective irrationality measure '
        'is not required to distinguish known seeds: the lifted difference '
        'is exactly 16**n times their difference. Diophantine estimates may '
        'supply a priori uniform resolution rates for specific tasks; neither '
        'finite distinguishability nor such a rate proves signed cancellation.'
    )


def exact_seed_separation(n: int, seed: Q) -> Q:
    """U_n(seed)-U_n(0)=16**n*seed, with no pi value or measure input."""
    if type(n) is not int or n < 0 or type(seed) not in (int, Q):
        raise ValueError('nonnegative integer n and exact rational seed required')
    return 16**n*Q(seed)


if __name__ == '__main__':
    for A, p in [(100, 1217), (512, 1217)]:
        gap = shadow_gap_bound(A, p)
        dgap = completed_digit_gap(A, p)
        print(f'A={A}: |s_A+pi/16| <= {float(gap):.3e}, '
              f'scaled digit gap <= {float(dgap):.3e}')
    print(separation_requires_irrationality_measure())
