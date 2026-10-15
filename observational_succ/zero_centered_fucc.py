"""Exact SUCC/FUCC pullbacks on the zero-centered residue observation space.

Reciprocal-cell Hilbert weights w_k=1/[k(k+1)]. Source-first finite arithmetic:
no nontrivial zeta zero inputs, no global RH or Weil conclusion.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import gcd, isqrt


class PullbackError(ValueError):
    pass


def _n(x, minimum=1):
    if type(x) is not int or not minimum <= x <= 1_000_000:
        raise PullbackError("bounded positive integer required")
    return x


def modulus_transport(k: int, n: int, q: int) -> dict:
    """T_q r_n(k)=r_(n/d)((q/d)k), d=gcd(q,n); r_1=0."""
    _n(k)
    _n(n,2)
    _n(q,2)
    d=gcd(n,q)
    left=Q((q*k)%n,n)
    modulus=n//d
    right=Q(((q//d)*k)%modulus,modulus)
    if left!=right:
        raise ArithmeticError("integer quotient transport failed")
    return {"cell":k,"modulus":n,"dilator":q,"common_divisor":d,
            "reduced_modulus":modulus,"rescaled_dilator":q//d,
            "original_value":left,"reduced_value":right,"exact":True}


def prime_power_drop(p: int, a: int, k: int) -> Q:
    """For actual prime p: T_p r_(p^a)=r_(p^(a-1)), r_1=0."""
    _n(p,2)
    _n(a)
    _n(k)
    if any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise PullbackError("prime jet demands a genuine prime")
    if a>16:
        raise PullbackError("prime exponent budget exceeded")
    return modulus_transport(k,p**a,p)["original_value"]


def dilation_weight_ratio(k: int, q: int) -> Q:
    """w_k/w_(qk)=q(qk+1)/(k+1) < q²; ||T_q||=q."""
    _n(k)
    _n(q,2)
    return Q(q*(q*k+1),k+1)


def additive_weight_ratio(k: int) -> Q:
    """w_k/w_(k+1)=(k+2)/k; ||T_S||=sqrt(3)."""
    _n(k)
    return Q(k+2,k)


def composition(k: int,p: int,q: int) -> dict:
    """Exact affine SUCC/FUCC carrier and contravariant pullback laws."""
    _n(k)
    _n(p,2)
    _n(q,2)
    return {"multiplier_commutation":p*(q*k)==q*(p*k),
            "affine_carrier_identity":p*(k+1)==p*k+p,
            "pullback_law":"T_S T_p = T_p T_S^p",
            "physical_transport_identified":False,
            "RH_proved":False}
