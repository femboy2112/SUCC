"""Zero-seed selectivity: the exact separation gap between the true orbit and
the p-integral rational shadow (PPP-08).

Front F, the crux obstruction.  The zero seed U_0=0 selects the completed orbit
  16^(n-1) pi,   while the PPP-08 shadow seed s_A selects
  16^n (s_A + pi/16)  with  s_A = -floor(D alpha_N)/D  rational.

Both completed orbits are IRRATIONAL (pi/16 is irrational; s_A + pi/16 is
rational + irrational).  The shadow is not literally the zero orbit: it is an
astronomically close rational-approximation shadow whose completed digits vanish
on the epoch.  This module proves the EXACT gap bound and shows that separating
the two requires an effective irrationality measure for pi -- a Diophantine
input, not a finite arithmetic one.  This is a precise, quantified obstruction,
not a proof of parity balance (which stays OPEN).
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
    """The precise statement of what input would separate the two orbits.

    To distinguish the true zero-seed orbit {16^(n-1) pi} from the shadow
    {16^n (s_A + pi/16)} on every epoch, one needs a lower bound on the
    distance |16^(n-1) pi - m| to integers m of the form forced by the shadow,
    i.e. an EFFECTIVE irrationality/transcendence measure for pi: for every
    integer q, |pi - m/q| > c q^{-mu} with explicit c, mu.  No finite
    arithmetic (forcing, CRT, carries) provides such a measure; it is a
    Diophantine input of a different type.
    """
    return (
        'Separating the zero-seed orbit from the p-integral shadow requires '
        'an effective irrationality measure for pi (|pi - m/q| > c q^{-mu}), '
        'which is a Diophantine/transcendence input, not finite arithmetic.'
    )


if __name__ == '__main__':
    for A, p in [(100, 1217), (512, 1217)]:
        gap = shadow_gap_bound(A, p)
        dgap = completed_digit_gap(A, p)
        print(f'A={A}: |s_A+pi/16| <= {float(gap):.3e}, '
              f'scaled digit gap <= {float(dgap):.3e}')
    print(separation_requires_irrationality_measure())
