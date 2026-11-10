"""Fourier reconstruction of the parity mean from Weyl means (Front F, F-11).

Theorem F-10 gives the exact Fourier support of the parity character:
    (-1)^{floor(16x)} = sum_{m ≡ 8 (mod 16)} (16/(pi i m)) e(m x)   (in L^2).
For each fixed finite epoch of irrational completed phases, the parity mean
is the limit of SYMMETRIC Fourier partial sums:

    P_A = lim_{H->infinity} sum_{|m|<=H, m ≡ 8 (mod 16)} (16/(pi i m)) c_A(m),

where c_A(m) = A^{-1} sum_{n=A}^{2A-1} e(m {16^{n-1} pi}) is the Weyl mean on the
COMPLETED orbit.  An L^2 tail bound does NOT control evaluation on an atomic
empirical measure, and these coefficients are not absolutely summable.  There
is no uniform O(1/H) error near digit boundaries.  This module's exponential
evaluations are numerical diagnostics, not certified Fourier values.  Use
parity_boundary_certificate for exact interval, boundary and Fejer payments.

This is a reduction, not a bound on c_A(m): normality/parity stay OPEN.
"""
from __future__ import annotations

import mpmath as mp
from fractions import Fraction as Q

from observational_succ import duck_bbp, selected_orbit as so
from observational_succ.parity_boundary_certificate import certified_source_digit


def completed_digit(n: int) -> int:
    """Exact hex digit d_n = floor(16 {U_n + T_n}) via rigorous interval."""
    return certified_source_digit(n)[0]


def parity(n: int) -> int:
    return 1 if completed_digit(n) % 2 == 0 else -1


def c_A_completed(A: int, m: int, dps: int = 40) -> mp.mpc:
    """Numerical Weyl-mean approximation using depth-eight midpoint phases.

    Precision dps controls arithmetic rounding, not the omitted source tail.
    The associated phase error grows with |m| and is not certified here.
    """
    o = so.SelectedOrbit()
    with mp.workdps(dps):
        acc = mp.mpc(0)
        for n in range(A, 2 * A):
            U = o.state(n)
            lo, hi = duck_bbp.tail_interval(n, 8)
            mid = (U + (lo + hi) / 2) % 1
            acc += mp.expjpi(2 * m * mid)
        return acc / A


def fourier_reconstruct(A: int, H: int, dps: int = 40) -> mp.mpf:
    """P_A reconstructed from Weyl means at |m| <= H, m ≡ 8 (mod 16)."""
    with mp.workdps(dps):
        total = mp.mpc(0)
        for m in range(8, H + 1, 16):
            total += (16 / (mp.pi * 1j * m)) * c_A_completed(A, m, dps)
            total += (16 / (mp.pi * 1j * (-m))) * c_A_completed(A, -m, dps)
        return total.real


if __name__ == '__main__':
    for A in [16, 32, 64]:
        P_direct = mp.mpf(sum(parity(n) for n in range(A, 2 * A))) / A
        P_fourier = fourier_reconstruct(A, 192)
        print(f'A={A:3d}  P_direct={float(P_direct):+.5f}  '
              f'P_fourier(|m|<=192)={float(P_fourier):+.5f}')
