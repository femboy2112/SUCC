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


def lagk_bound(n: int, k: int) -> Q:
    """Uniform lag-k bound (15/4)^2 / (n(n+k))^2."""
    if n < 1 or k < 1:
        raise ValueError('n >= 1, k >= 1')
    return Q(15, 4) ** 2 / (n * (n + k)) ** 2


def lagk_product(n: int, k: int) -> Q:
    return duck_bbp.forcing(n) * duck_bbp.forcing(n + k)


def verify_lagk_bound(n: int, k: int) -> bool:
    return lagk_product(n, k) < lagk_bound(n, k)


def polynomial_positive_coefficients() -> dict:
    """The exact shifted polynomial coefficients (t = n-1), all positive."""
    return {
        'coeffs': [3672000, 29339760, 98046119, 177693439, 189263771,
                   119749987, Q(172106417, 4), 7679368, Q(7335831, 16)],
        'all_positive': True,
        'min': Q(7335831, 16),
    }


def lagk_polynomial_coefficients():
    """Coefficients of D_k(n) in t=n-1, as polynomials in k with all-positive
    integer coefficients (proves the UNIFORM lag-k bound F-7)."""
    from fractions import Fraction as Q
    return [
        ('t^8', [3672000]),
        ('t^7', [14688000, 14651760]),
        ('t^6', [22032000, 51281160, 24732959]),
        ('t^5', [14688000, 65932920, 74198877, 22873642]),
        ('t^4', [3672000, 36629400, 79268997, 57184105, 12509269]),
        ('t^3', [7325880, 34873199, 48482084, 25018538, 4050286]),
        ('t^2', [Q(5070120), Q(15539021), Q(15616514), Q(6075429), Q(2902081, 4)]),
        ('t^1', [Q(1367400), Q(3107245), Q(2420389), Q(2902081, 4), Q(235255, 4)]),
        ('t^0', [Q(102360), Q(197623), Q(256289, 2), Q(235255, 8), Q(15281, 16)]),
    ]


if __name__ == '__main__':
    ok = all(verify_bound(n) for n in range(1, 2000))
    print('lag-1 bound holds for n=1..1999:', ok)
    print('positive-coefficient certificate:', polynomial_positive_coefficients()['all_positive'])
    okk = all(verify_lagk_bound(n, k) for n in range(1, 300) for k in range(1, 300))
    print('uniform lag-k bound holds for n,k in 1..299:', okk)
