"""Arithmetic RH statement carrier: Lagarias criterion with rational intervals.

For n>=1, Lagarias (2002) proves RH equivalent to the inequalities
  sigma(n) <= H_n + exp(H_n)*log(H_n) for all n,
equality only at n=1. This is an EXTERNAL CLASSICAL equivalence theorem.
The following finite checks use exact sigma/H_n and previously tested
outward-rounded rational intervals. Neither the first N passing, nor
a deliberately counterfeit divisor sum, certifies RH or its failure.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import isqrt

from .source_weil_hierarchy import exp_pos, log_iv, iv


class ArithmeticCarrierError(ValueError):
    pass


def _bound(n: int) -> int:
    if type(n) is not int or not 1 <= n <= 128:
        raise ArithmeticCarrierError("One exact integer 1<=n<=128 per probe")
    return n


def harmonic_number(n: int) -> F:
    n = _bound(n)
    return sum((F(1,k) for k in range(1,n+1)), F(0))


def divisor_sum(n: int) -> int:
    n = _bound(n)
    result = 0
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            result += d
            if d*d != n:
                result += n//d
    return result


def lagarias_source_inequality(n: int, *,
                               counterfeit_sigma_increment: int = 0) -> dict:
    """Finite exact arithmetic + rigorous intervals, no zero locations.

    Lifting to the RH universal statement requires verifying the condition
    for EVERY n, not checking a finite prefix. A mutant is NOT true sigma.
    """
    n = _bound(n)
    if type(counterfeit_sigma_increment) is not int or counterfeit_sigma_increment<0:
        raise ArithmeticCarrierError("Declared nonnegative exact source mutation only")
    H, sigma = harmonic_number(n), divisor_sum(n)
    delta = counterfeit_sigma_increment
    bound = iv(H) + exp_pos(H)*log_iv(H)
    comparison = sigma + delta
    if bound.lo >= comparison:
        verdict = "FINITE_CERTIFIED_HOLDS"
    elif bound.hi < comparison:
        verdict = "FINITE_CERTIFIED_VIOLATION"
    else:
        verdict = "INCONCLUSIVE_INTERVAL"
    return {
        "n": n, "H": H, "true_sigma": sigma, "delta_fake": delta,
        "actual_source": delta == 0,
        "inequality_rhs_rational_interval": (bound.lo, bound.hi),
        "status": verdict, "only_equality_at_n1_in_classical_statement": n==1,
        "universal_all_n_verified": False,
        "Lagarias_equivalence": "EXTERNAL_CLASSICAL_THEOREM",
        "RH_proved": False,
    }


def low_carrier_prefix_receipt(max_n: int) -> dict:
    """Bounded finite list, explicitly not a mathematical RH decision."""
    max_n = _bound(max_n)
    rows=tuple(lagarias_source_inequality(n) for n in range(1,max_n+1))
    return {
        "max_n": max_n,
        "checked": len(rows),
        "statuses": tuple(r["status"] for r in rows),
        "all_checked_finite_inequalities_certified":
            all(r["status"] == "FINITE_CERTIFIED_HOLDS" for r in rows),
        "first_unchecked_integer": max_n+1,
        "global_RH_classification_from_prefix": "UNRESOLVED",
        "no_nontrivial_zeros_used": True,
        "RH_proved": False,
    }
