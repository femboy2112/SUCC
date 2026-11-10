"""Fourier reconstruction of the parity mean from Weyl means (Front F, F-11).

Theorem F-10 gives the exact Fourier support of the parity character:
    (-1)^{floor(16x)} = sum_{m ≡ 8 (mod 16)} (16/(pi i m)) e(m x)   (in L^2).
Therefore the epoch parity mean satisfies the EXACT identity

    P_A = sum_{m ≡ 8 (mod 16)} (16/(pi i m)) c_A(m),

where c_A(m) = A^{-1} sum_{n=A}^{2A-1} e(m {16^{n-1} pi}) is the Weyl mean on the
COMPLETED orbit.  Truncating to |m| <= H leaves an L^2 tail bounded by the
Fourier tail of the step function (O(1/H) in a weighted-l1 sense).  This module
verifies the truncated reconstruction against the exact completed-digit parity
at finite A using rigorous rational digit certificates (duck_bbp + selected_orbit).

This is a reduction, not a bound on c_A(m): normality/parity stay OPEN.
"""
from __future__ import annotations

import mpmath as mp
from fractions import Fraction as Q

from observational_succ import duck_bbp, selected_orbit as so


def completed_digit(n: int) -> int:
    """Exact hex digit d_n = floor(16 {U_n + T_n}) via rigorous interval."""
    o = so.SelectedOrbit()
    U = o.state(n)
    lo, hi = duck_bbp.tail_interval(n, 8)
    frac_lo = (U + lo) % 1
    frac_hi = (U + hi) % 1
    d_lo = int((16 * frac_lo) % 16)
    d_hi = int((16 * frac_hi) % 16)
    assert d_lo == d_hi, (n, d_lo, d_hi)
    return d_lo


def parity(n: int) -> int:
    return 1 if completed_digit(n) % 2 == 0 else -1


def c_A_completed(A: int, m: int, dps: int = 40) -> mp.mpc:
    """Weyl mean over the completed orbit {16^{n-1} pi} = {U_n + T_n}."""
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
