"""Exact Möbius cancellation of full Euler source, leaving Tate's real Gamma.

In Re(s)>1, Dirichlet convolution 1*mu=delta and the Euler identity
zeta(s)*(sum mu(n)n^-s)=1. Multiplying completed Lambda(s)=Gamma_R(s)
zeta(s) by 1/zeta(s) yields Gamma_R(s), but this is an analytic identity
on the CONVERGENT domain, not bounded inversion on the critical line.

Compare genuine Tate finite Euler factors, single real Gamma even-integer
monomials and exact pole residues. Reject squarefree positive norm,
full-valence (-1)^k twist, missing primes and fake p6 replacements.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt,prod


class MobiusGammaError(ValueError):
    """Invalid arithmetic source or analytic-domain claim."""


def _prime(p):
    if type(p) is not int or p<2 or p>100000 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        raise MobiusGammaError("genuine prime source required")
    return p


def _integer(n):
    if type(n) is not int or not 1<=n<=2000:
        raise MobiusGammaError("finite positive integer source <=2000")
    return n


def factor_support(n):
    n=_integer(n)
    ps=[]
    d=2
    while d*d<=n:
        if n%d==0:
            ps.append(d)
            while n%d==0:n//=d
        d+=1 if d==2 else 2
    if n>1:ps.append(n)
    return tuple(ps)


def independent_mobius(n):
    """Squarefree sign from independently enumerated prime-power divisor test."""
    n=_integer(n)
    seen=0
    rem=n
    for p in factor_support(n):
        if rem%(p*p)==0:
            return 0
        rem//=p
        seen+=1
    return (-1)**seen


def exact_divisor_cancel(n):
    """All-divisor arithmetic cancellation, WITHOUT assuming zeta zeros."""
    n=_integer(n)
    div=tuple(d for d in range(1,n+1) if n%d==0)
    signed=tuple((d,independent_mobius(d)) for d in div)
    total=sum((w for _,w in signed),0)
    theorem=1 if n==1 else 0
    # Positive proof independent of enumeration is product over distinct p
    # of (1-1); count the distinct prime support from independent trial factor.
    ps=factor_support(n)
    factor=prod((1-1 for _ in ps),start=1)
    if total!=theorem or factor!=theorem:
        raise AssertionError("MOBIUS_DISTRIBUTION_INVERSE_FAILED")
    return {
        "n":n,"divisor_source":signed,
        "arithmetic_convolution_sum":total,"factorized_prime_cancellation":factor,
        "is_unit_delta":total==theorem,
        "completed_Weil_PSD_proved":False,
    }


def finite_tate_gamma_remainder(primes,beta,depth=5):
    """True finite-prime Tate zeta × FULL Möbius inverse = real Γ_R.

    Exact gamma is returned as coefficient*pi^exponent for positive even
    integer beta, never as a rounded transcendental number.
    """
    if type(primes) is not tuple or primes != tuple(sorted(set(primes))) or not primes or len(primes)>10:
        raise MobiusGammaError("ordered nonempty distinct prime stage required")
    if type(beta) is not int or beta not in (2,4,6,8,10,12):
        raise MobiusGammaError("exact even integer convergent Mellin exponent")
    if type(depth) is not int or not 0<=depth<=15:
        raise MobiusGammaError("finite source shell depth required")
    for p in primes:_prime(p)
    from .tate_idelic_zeta import finite_euler_stage,real_gamma_even_integer,TateZeroModes
    true=finite_euler_stage(primes,beta,depth)
    local=tuple((p,Q(1,p**beta)) for p in primes)
    mobius=prod((1-r for _,r in local),start=Q(1))
    zeta=true["complete_finite_place_product"]
    wrong_positive_squarefree=prod((1+r for _,r in local),start=Q(1))
    wrong_all_negative_towers=prod((1/(1+r) for _,r in local),start=Q(1))
    if zeta*mobius!=1 or zeta*wrong_positive_squarefree==1 or zeta*wrong_all_negative_towers==1:
        raise AssertionError("Euler factor/countermodel contract failed")
    coefficient,pi_exponent=real_gamma_even_integer(beta)
    if TateZeroModes().residues != (Q(-1),Q(1)):
        raise AssertionError("completed pole normalization mutated")
    return {
        "prime_source":primes,"beta":beta,"genuine_Tate_finite_zeta":zeta,
        "genuine_Mobius_convolution_inverse":mobius,
        "finite_places_exactly_cancel":zeta*mobius==1,
        "remaining_archimedean_Gamma_R_monomial":(coefficient,pi_exponent),
        "completed_Lambda_times_Mobius_symbolic":f"{coefficient}*pi^({pi_exponent})",
        "wrong_squarefree_positive_norm":wrong_positive_squarefree,
        "wrong_full_negative_towers":wrong_all_negative_towers,
        "Tate_pole_residues":(Q(-1),Q(1)),
        "convergent_domain_only":"Re(s)>1",
        "can_invert_zeta_at_every_critical_zero":False,
        "completed_Weil_trace_identified":False,
        "RH_proved":False,
    }


def omitted_prime_mutant(p,beta):
    """If genuine zeta place p is omitted but μ includes p, Gamma is
    multiplied by (1-p^-beta), exposing missing source.
    """
    _prime(p)
    if type(beta) is not int or not 2<=beta<=12:
        raise MobiusGammaError("integer beta >=2 required")
    return {"omitted_p":p,"missing_Euler_source_residual":1-Q(1,p**beta),
            "equals_Arch_Gamma_only":False,"RH_proved":False}
