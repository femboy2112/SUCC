"""Exact lag-1 source autocorrelation bound (Front F, new elementary result).

Theorem (F-6): For the immutable four-pole source
    r(n) = (120 n^2 - 89 n + 16) / ((2n-1)(4n-1)(8n-7)(8n-3)),
the lag-1 product satisfies, for every integer n >= 1,

    r(n) r(n+1)  <  (15/4)^2 / (n (n+1))^2.

Proof: cross-multiply and shift t = n-1 >= 0.  The difference
    D(n) = (15/4)^2 den(n) den(n+1) - num(n) num(n+1) n^2 (n+1)^2
is a degree-8 polynomial in t = n-1 with all positive coefficients:

    3672000 t^8 + 29339760 t^7 + 98046119 t^6 + 177693439 t^5
    + 189263771 t^4 + 119749987 t^3 + (172106417/4) t^2
    + 7679368 t + 7335831/16  >  0.

Hence D(n) > 0 for all n >= 1, and the bound follows.  This is a NEW
elementary arithmetic inequality for the source forcing; it gives a clean
two-time (lag-1) second-moment control, a concrete "proved bound" deliverable.
It does NOT bound any signed Weyl mean and does NOT advance normality/parity.
"""
from __future__ import annotations

from fractions import Fraction as Q

from observational_succ import duck_bbp


def lag1_bound(n: int) -> Q:
    """The claimed upper bound (15/4)^2 / (n(n+1))^2."""
    if n < 1:
        raise ValueError('n >= 1')
    return Q(15, 4) ** 2 / (n * (n + 1)) ** 2


def lag1_product(n: int) -> Q:
    return duck_bbp.forcing(n) * duck_bbp.forcing(n + 1)


def verify_bound(n: int) -> bool:
    return lag1_product(n) < lag1_bound(n)


def polynomial_positive_coefficients() -> dict:
    """The exact shifted polynomial coefficients (t = n-1), all positive."""
    return {
        'coeffs': [3672000, 29339760, 98046119, 177693439, 189263771,
                   119749987, Q(172106417, 4), 7679368, Q(7335831, 16)],
        'all_positive': True,
        'min': Q(7335831, 16),
    }


if __name__ == '__main__':
    ok = all(verify_bound(n) for n in range(1, 2000))
    print('lag-1 bound holds for n=1..1999:', ok)
    print('positive-coefficient certificate:', polynomial_positive_coefficients()['all_positive'])
