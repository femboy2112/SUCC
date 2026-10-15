"""Sharp periodic-tail enclosure for the zero-centered residue-clock L2 error.

The residue clock r_n(k) = (k mod n)/n is n-periodic, so any finite
combination F(k) = sum_n a_n r_n(k) is L-periodic with L = lcm(moduli).
The squared global L2(w) error  E = sum_k |1 - F(k)|^2 / (k(k+1))  then has
a tail whose |1-F(k)|^2 factor is L-periodic, and the weights telescope:
sum_{k>K} 1/(k(k+1)) = 1/(K+1).  This yields a two-sided enclosure

    P_K + m/(K+1)  <=  E  <=  P_K + M/(K+1)

where P_K is the exact finite prefix and (m, M) are the exact min/max of
|1-F(k)|^2 over one full period.  Since |r_n(k)| <= (n-1)/n < 1, we get
M <= (1 + sum|a_n|)^2 with STRICT inequality whenever at least one coefficient
is nonzero (equality M == (1 + sum|a_n|)^2 == 1 occurs only for the all-zero
family, where F == 0).  So this enclosure is strictly sharper than the prior
ZCR-07 bound  E <= P_K + (1 + sum|a_n|)^2/(K+1)  for every family with a
nonzero coefficient, and it supplies a strictly positive lower bound in the
generic case.

Pure exact rational arithmetic.  No float, no zeta zero, no Gamma/pole input.
This is a finite certificate improvement, NOT a global L2 convergence proof
and NOT an RH result.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import lcm


class PeriodicTailError(ValueError):
    pass


def _integer(n: int, lo: int, hi: int) -> int:
    if type(n) is not int or not lo <= n <= hi:
        raise PeriodicTailError(f"expected an integer in [{lo},{hi}]")
    return n


def residue(k: int, n: int) -> Q:
    """r_n(k) = (k mod n)/n, exact rational in [0,1)."""
    _integer(k, 1, 1_000_000)
    _integer(n, 2, 1_000_000)
    return Q(k % n, n)


def value(k: int, a: dict[int, Q]) -> Q:
    """F(k) = sum_n a_n r_n(k)."""
    if not a:
        raise PeriodicTailError("nonempty coefficient family required")
    for n, c in a.items():
        _integer(n, 2, 1_000_000)
        if type(c) not in (int, Q):
            raise PeriodicTailError("only exact rational coefficients")
    return sum((Q(c) * residue(k, n) for n, c in a.items()), Q())


def defect_extremes(a: dict[int, Q]) -> tuple[Q, Q]:
    """(min, max) of |1 - F(k)|^2 over one full period k=1..L.

    By L-periodicity of F, sampling the single period 1..L gives the exact
    global min/max of the defect over ALL k>=1.
    """
    if not a:
        raise PeriodicTailError("nonempty coefficient family required")
    for n, c in a.items():
        _integer(n, 2, 1_000_000)
        if type(c) not in (int, Q):
            raise PeriodicTailError("only exact rational coefficients")
    L = lcm(*a.keys())
    # L is capped at the residue-clock k-budget (1e6): defect_extremes samples
    # k=1..L through residue(k,n), which itself enforces k <= 1e6.
    _integer(L, 2, 1_000_000)
    d = [(Q(1) - value(k, a)) ** 2 for k in range(1, L + 1)]
    return min(d), max(d)


def prefix_sum(a: dict[int, Q], K: int) -> Q:
    """P_K = sum_{k=1..K} |1 - F(k)|^2 / (k(k+1)), exact."""
    _integer(K, 1, 100_000)
    return sum(((Q(1) - value(k, a)) ** 2 * Q(1, k * (k + 1))
                for k in range(1, K + 1)), Q())


def sharp_distance_interval(a: dict[int, Q], K: int = 128) -> tuple[Q, Q]:
    """Certified [lower, upper] for the global squared L2(w) error.

    Returns (P_K + m/(K+1), P_K + M/(K+1)) with (m, M) the exact periodic
    defect extremes.  Both sides are exact rationals.
    """
    _integer(K, 1, 100_000)
    P = prefix_sum(a, K)
    m, M = defect_extremes(a)
    return P + m / Q(K + 1), P + M / Q(K + 1)


def crude_sum_abs(a: dict[int, Q]) -> Q:
    """1 + sum|a_n|: the coefficient of the prior ZCR-07 upper bound."""
    return Q(1) + sum((abs(Q(c)) for c in a.values()), Q())


def sharpening_report(a: dict[int, Q], K: int = 128) -> dict:
    """Compare the sharp periodic enclosure against the prior ZCR-07 bound.

    Reports the old upper coefficient (1+sum|a_n|)^2, the new one M (the exact
    periodic max defect), the exact ratio M/(1+sum|a_n|)^2, and a lower bound
    that the prior enclosure could not supply.
    """
    m, M = defect_extremes(a)
    old_c = crude_sum_abs(a) ** 2
    P = prefix_sum(a, K)
    lo, hi = P + m / Q(K + 1), P + M / Q(K + 1)
    return {
        "period": lcm(*a.keys()),
        "exact_prefix_P": str(P),
        "min_defect_m": str(m),
        "max_defect_M": str(M),
        "old_upper_coeff": str(old_c),
        "new_upper_coeff": str(M),
        "sharpening_ratio": str(M / old_c),
        "strictly_sharper_upper": M < old_c,
        "lower_bound": str(lo),
        "upper_bound": str(hi),
        "strictly_positive_lower": lo > 0,
        "zero_independent": True,
        "RH_proved": False,
    }
