"""Independent finite incidence-algebra reconstruction of clock prime jets.

The quotient ordering C_m -> C_d (d|m) gives the divisor incidence algebra.
The integer Mobius function is derived by inverting its zeta element on
ACTUAL period indices, without querying primality or lcm growth.

This is an independent algorithmic cross-check of the lcm-jet source, not an
independent empirical observation or an RH/Weil-positivity proof.
"""
from __future__ import annotations

from fractions import Fraction
from .orbit_clock_genesis import ClockSourceError, _nat


def clock_divisors(n:int) -> tuple[int,...]:
    _nat(n,"finite rooted cycle period",maximum=10000)
    return tuple(d for d in range(1,n+1) if n%d==0)


def incidence_mobius(horizon:int) -> dict[int,int]:
    """Compute mu(1)=1, sum_(d|n)mu(d)=0 for n>1, purely by divisibility."""
    _nat(horizon,"finite incidence clock horizon",maximum=500)
    mu={1:1}
    for n in range(2,horizon+1):
        mu[n]=-sum(mu[d] for d in range(1,n) if n%d==0)
    for n in range(1,horizon+1):
        expected=1 if n==1 else 0
        if sum(mu[d] for d in clock_divisors(n)) != expected:
            raise AssertionError("incidence-zeta inversion failed")
    return mu


def clock_log_increment_ratio(n:int, mu:dict[int,int]) -> Fraction:
    """exp((mu*log)(n)) as an exact fraction, no logarithm evaluated.

    Product_(d|n) (n/d)^mu(d) equals p if n=p^k and 1 otherwise.
    All divisions and negative powers are exact rationals.
    """
    _nat(n,"clock period",maximum=500)
    if type(mu) is not dict or any(d not in mu for d in clock_divisors(n)):
        raise ClockSourceError("missing source divisor incidence coefficients")
    out=Fraction(1)
    for d in clock_divisors(n):
        k=mu[d]
        if type(k) is not int:
            raise ClockSourceError("untrusted incidence weight")
        out*=Fraction(n,d)**k
    return out


def incidence_prime_jets(horizon:int) -> tuple[dict,...]:
    """Every finite quotient index emits one symbolic exact log-weight."""
    mu=incidence_mobius(horizon)
    return tuple({"n":n,"ratio":clock_log_increment_ratio(n,mu),
                  "finite_divisor_count":len(clock_divisors(n)),
                  "source":"divisibility incidence algebra"}
                 for n in range(1,horizon+1))


def incidence_lcm_compatibility(horizon:int) -> dict:
    """Derive L_H as the product of incidence-jet ratios, independently of lcm()."""
    mu=incidence_mobius(horizon)
    product=Fraction(1)
    for n in range(1,horizon+1):
        product*=clock_log_increment_ratio(n,mu)
        if product.denominator!=1:
            raise AssertionError("an authentic clock lcm cannot have a fractional index")
    return {"horizon":horizon,"reconstructed_joint_index":int(product),
            "no_prime_or_lcm_oracle_in_source_algorithm":True,
            "is_full_universal_clock":False}


def missing_incidence_arrow_mutation(n:int,divisor:int)->dict:
    """A purported omitted quotient arrow cannot be an authentic clock diagram.

    E.g. erase C6->C2 while retaining C6->C1 and C2->C1. The relation
    is then not the source-preserving full quotient category of cyclic clocks.
    """
    _nat(n,"source period",maximum=500)
    _nat(divisor,"declared quotient",maximum=500)
    if n%divisor !=0 or divisor==n:
        raise ClockSourceError("only an actual proper divisor arrow can be mutated")
    actual=set(clock_divisors(n))
    mutated=actual-{divisor}
    return {"n":n,"missing_actual_factor_period":divisor,
            "arrow_was_required":divisor in actual,
            "source_is_full_quotient_diagram": mutated==actual,
            "mutation_rejected_by_canonical_divisor_oracle": mutated!=actual}
