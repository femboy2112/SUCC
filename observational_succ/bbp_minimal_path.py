"""A minimal-path audit: exact BBP gauge conjugacy and single-missing-prime countermodels.

This module makes FINITE, exact, source-certified rational constructions.
It does not decide pi normality. Universal statements in the mathematical
research dossier rely on density of Z[1/q] in R/Z.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt
from observational_succ.bbp_source_memory import forcing, forced_step, tail_interval


def _natural(n: int, lo: int = 0) -> int:
    if type(n) is not int or n < lo:
        raise ValueError(f"expected integer >= {lo}")
    return n


def _prime(p: int) -> int:
    _natural(p, 2)
    if any(p % j == 0 for j in range(2, isqrt(p)+1)):
        raise ValueError("prime required")
    return p


def nearest_integer(r: Q) -> int:
    """Exact nearest integer, half ties upward; no float."""
    r=Q(r)
    return (2*r.numerator + r.denominator)//(2*r.denominator)


def circle_distance(a: Q, b: Q) -> Q:
    d=(Q(a)-Q(b))%1
    return min(d,1-d)


def is_prime_power_denominator(q: Q, p: int) -> bool:
    _prime(p)
    d=Q(q).denominator
    while d%p==0:
        d//=p
    return d==1


def period_phase(period: int, terms: int | None=None) -> tuple[Q,Q]:
    """Certified nearest period-point z=k/(16^L-1) to t0=pi/16.

    Returns z, rational all-source interval upper bound on circle distance
    from z to t0 (NOT a pi-digit input).
    """
    _natural(period,1)
    terms=period+12 if terms is None else _natural(terms,1)
    lo,hi=tail_interval(0,terms)
    mid=(lo+hi)/2
    D=16**period-1
    z=Q(nearest_integer(D*mid),D)%1
    error=circle_distance(z,mid)+(hi-lo)/2
    return z,error


def rational_target_proxy(z: Q, n: int, terms: int) -> tuple[Q,Q]:
    """Rational midpoint and certified circle-error of z-t_n."""
    _natural(n,1);_natural(terms,1)
    lo,hi=tail_interval(n,terms)
    return (Q(z)-(lo+hi)/2)%1, (hi-lo)/2


def single_missing_prime_counterfeit(horizon: int, period: int = 9,
                                      missing_prime: int = 3,
                                      precision: Q = Q(1,10**6),
                                      frozen_prefix: int = 0) -> dict:
    """Construct y'_1..y'_N; preserve every p!=q torsion component of y_n.

    The constructed positive rational forcing differs from true BBP by a
    certified small error at each step, and selected y'_n shadows the chosen
    fixed periodic base-16 target z_n up to O(n^-2)+O(16^-n).

    This is an exact finite witness, not a proof by finite computation that
    the infinite counterfeit exists (the density argument supplies that).
    """
    _natural(horizon,1);_natural(period,1);_prime(missing_prime)
    _natural(frozen_prefix)
    precision=Q(precision)
    if not Q(0)<precision<Q(1,100):
        raise ValueError("precision must be positive and below 1/100")
    z,err0=period_phase(period)
    if err0>=precision/Q(16**(2*frozen_prefix+9)):
        raise ValueError("period too short to achieve requested source contact precision")
    # Source selected y0=0 exactly, unlike the fixed-point gauge countermodel.
    real=Q(0); fake=Q(0); errors=[err0]
    records=[]
    D=16**period-1
    K=(z.numerator*(D//z.denominator))%D
    # z_n is 16^n*z modulo 1, using an actual rational point of period | L.
    for n in range(1,horizon+1):
        real=forced_step(real,n)
        z_n=Q((K*pow(16,n,D))%D,D)
        # q-powered grid is dense in the circle while leaving p!=q torsion intact.
        target_error=precision/Q(16**(n+6))
        terms=n+max(16,period+12)
        target, tail_err=rational_target_proxy(z_n,n,terms)
        while tail_err>=target_error/4:
            terms+=4
            target,tail_err=rational_target_proxy(z_n,n,terms)
        Qn=1
        if n<=frozen_prefix:
            f=real # Preserve the first n authentic source values EXACTLY.
        else:
            Qn=missing_prime
            while Q(1,2*Qn)>=target_error/4:
                Qn*=missing_prime
            k=nearest_integer((target-real)*Qn)
            f=(real+Q(k,Qn))%1
        e=circle_distance(f,target)+tail_err
        assert e < target_error
        # Exact rational forcing chosen in the unique integer lift close to BBP.
        raw=f-16*fake
        fsource=raw+nearest_integer(forcing(n)-raw)
        discrepancy=abs(fsource-forcing(n))
        assert discrepancy<=e+16*errors[-1]
        assert fsource>0
        assert is_prime_power_denominator(f-real,missing_prime)
        assert is_prime_power_denominator(fsource-forcing(n),missing_prime)
        if n>=2:
            assert fsource<1
        records.append({"n":n,"authentic_phase":real,"counterfeit_phase":f,
                        "source":fsource,"forcing_error":discrepancy,
                        "forcing_bound":e+16*errors[-1],"target_error":e,
                        "period_phase":z_n,"tail_upper":tail_interval(n,terms)[1],
                        "missing_prime_q":missing_prime,
                        "grid_q_power":Qn})
        errors.append(e)
        fake=f
    return {"z0":z,"period":period,"initial_contact_bound":err0,
            "missing_prime":missing_prime,"source_precision":precision,"frozen_prefix":frozen_prefix,
            "records":tuple(records)}
