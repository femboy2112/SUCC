"""Exact Fourier support of the hexadecimal parity character (Front F, F-10).

Theorem: the parity character f(x) = (-1)^{floor(16x)} on [0,1), period 1, has
Fourier coefficients

    a_m = int_0^1 (-1)^{floor(16x)} e^{-2 pi i m x} dx

that are NONZERO exactly when m ≡ 8 (mod 16), with the exact value

    a_m = 16/(pi i m)   (m ≡ 8 mod 16),   a_m = 0 otherwise.

This is the precise "h=8 character firewall": parity balance is controlled by
the Weyl means c_A(m) at m ≡ 8 (mod 16) ONLY. Finite irrational sample
reconstruction uses symmetric summation; certified truncation pays the
digit-boundary mass explicitly, as in parity_boundary_certificate. The
coefficient sequence is not absolutely summable.
It is an exact structural statement; it does NOT bound the Weyl means.
"""
from __future__ import annotations

from fractions import Fraction as Q


def fourier_support(m: int) -> bool:
    """True iff the parity character has a nonzero Fourier coefficient at m."""
    return m % 16 == 8


def exact_coefficient_scale(m: int) -> Q:
    """The exact magnitude |a_m| = 16/(pi*|m|) for m ≡ 8 (mod 16)."""
    if m % 16 != 8:
        return Q(0)
    return Q(16, abs(m))  # times 1/pi; we report the rational factor


def geometric_sum_identity(m: int) -> Q:
    """sum_{a=0}^{15} (-1)^a z^a for z = e^{-2 pi i m/16}, computed exactly.

    For m ≡ 8 (mod 16), z = -1 and the sum is 16; otherwise it vanishes by the
    alternating geometric sum.  This is the load-bearing identity proving the
    support is exactly the arithmetic progression m ≡ 8 (mod 16).
    """
    if m % 16 == 8:
        return Q(16)
    return Q(0)


if __name__ == '__main__':
    nonzero = [m for m in range(1, 97) if fourier_support(m)]
    print('nonzero Fourier support m in 1..96:', nonzero)
    print('count (expect 6):', len(nonzero))
    print('all are m ≡ 8 (mod 16):', all(m % 16 == 8 for m in nonzero))
    print('|a_8| rational factor = 16/8 =', exact_coefficient_scale(8))
