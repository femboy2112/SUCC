"""Formal q=0 / logarithmic q=1 BBP boundary-character research laboratory.

NOT literal 0-adic or 1-adic integers. Those bases degenerate.

0-side: finite coefficient jets of Q[[q]] and their additive characters.
1-side: finite jets of polynomials at q=1; BBP itself has a logarithmic
        germ whose leading values are proved in the companion dossier.

The source-selected real evaluation q=1/16 is not continuous in either
purely formal jet topology; preserve analytic growth and the zero selector.
All exact probes use Fraction. No finite test proves pi normality.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb
from typing import Sequence

SOURCE_TAG = "authentic-signed-four-pole-zero-seeded-BBP"
BETA = Q(1, 16)
ASYMPTOTIC_MASS = Q(15, 64)
MOMENT_KERNEL = (Q(4), Q(0), Q(0), Q(-2), Q(-1), Q(-1))


def _integer(value: int, name: str, lower: int = 0, upper: int = 1000) -> int:
    if type(value) is not int or not lower <= value <= upper:
        raise ValueError(f"{name}: integer in [{lower},{upper}] required")
    return value


def _rational(value, name: str) -> Q:
    if type(value) not in (Q,int):
        raise ValueError(f"{name}: exact rational required")
    return Q(value)


def authentic_r(n: int) -> Q:
    _integer(n,"positive BBP time",1,100000)
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


def canceled_r(n: int) -> Q:
    _integer(n,"positive BBP time",1,100000)
    return Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def source_moment(n: int) -> Q:
    """Exact ∫_0^1 x^(8(n-1))*(4-2x^3-x^4-x^5) dx."""
    _integer(n,"source moment time",1,100000)
    return sum((t/Q(8*(n-1)+j+1) for j,t in enumerate(MOMENT_KERNEL)),Q())


def source_at_zero_jet(depth: int) -> tuple[Q,...]:
    _integer(depth,"zero jet depth",1,1000)
    return tuple(authentic_r(j+1) for j in range(depth))


def polynomial_evaluate(coefficients: Sequence[Q|int], x) -> Q:
    z=_rational(x,"evaluation coordinate")
    ans=Q(0)
    for a in reversed(coefficients):
        ans=ans*z+_rational(a,"polynomial coefficient")
    return ans


def one_jet_of_polynomial(coefficients: Sequence[Q|int], depth:int) -> tuple[Q,...]:
    """Coefficient jet for f(1-s), s=1-q; (1-q)-adic coordinate."""
    _integer(depth,"one jet depth",1,1000)
    coeffs=tuple(_rational(a,"polynomial coefficient") for a in coefficients)
    return tuple(Q((-1)**j)*sum((coeffs[n]*comb(n,j) for n in range(j,len(coeffs))),Q())
                 for j in range(depth))


def zero_jet_of_polynomial(coefficients: Sequence[Q|int], depth:int) -> tuple[Q,...]:
    _integer(depth,"zero jet depth",1,1000)
    coeffs=tuple(_rational(a,"polynomial coefficient") for a in coefficients)
    return coeffs[:depth]+(Q(0),)*max(0,depth-len(coeffs))


def jet_character_phase(jet:Sequence[Q|int],weights:Sequence[Q|int]) -> Q:
    """Exact phase in Q/Z of an additive finite-jet character.

    Character is exp(2*pi*i*phase). For real-germ characters, replace
    rational jets/weights with real coefficient functionals; the proof
    is the same linearity identity. This oracle is exact-rational only.
    """
    if len(jet)!=len(weights):
        raise ValueError("character needs exactly one weight per jet")
    return sum((_rational(x,"jet")*_rational(t,"character weight")
                for x,t in zip(jet,weights)),Q())%1


def mutant_multiplier(K:int,J:int) -> tuple[Q,...]:
    """M(z)=1-C*z^K*(1-z)^J, C=16^(K+J)/15^J.

    M(1/16)=0, M≡1 (mod z^K) and M≡1 (mod (1-z)^J).
    """
    _integer(K,"zero-jet depth",1,64)
    _integer(J,"one-jet depth",1,64)
    C=Q(16**(K+J),15**J)
    coeff=[Q(0)]*(K+J+1)
    coeff[0]=Q(1)
    for j in range(J+1):
        coeff[K+j]-=C*(-1)**j*comb(J,j)
    return tuple(coeff)


def mutant_source(n:int,K:int,J:int) -> Q:
    """n-th authentic-source-filtered coefficient [z^(n-1)] M(z)G(z).

    This mutant is NOT the original four-pole source. The early missing
    terms use the *causal convention* r(n)=0 for n<=0.
    """
    _integer(n,"positive mutant time",1,10000)
    mult=mutant_multiplier(K,J)
    return sum((mult[j]*authentic_r(n-j)
                for j in range(min(len(mult),n)) if mult[j]),Q())


def mutant_rational_extension(x:int,K:int,J:int)->Q:
    """Late-time rational 2-adic extension; x may be any signed integer.

    For x>=K+J+1, equals the actual causal coefficient mutant_source.
    Each shifted original canceled r has odd denominator everywhere in Z2.
    """
    _integer(K,"K",1,64)
    _integer(J,"J",1,64)
    if type(x) is not int:
        raise ValueError("integer input required for exact oracle")
    mult=mutant_multiplier(K,J)
    def r_ext(t):
        return Q(120*t*t-89*t+16,(2*t-1)*(4*t-1)*(8*t-7)*(8*t-3))
    return sum((mult[j]*r_ext(x-j) for j in range(len(mult)) if mult[j]),Q())


def mutant_state(n:int,K:int,J:int)->Q:
    """True zero-initial state for changed source; NOT an authentic BBP state."""
    _integer(n,"mutant orbit time",0,500)
    u=Q()
    for j in range(1,n+1):
        u=16*u+mutant_source(j,K,J)
    return u


def two_adic_unit(x:Q|int)->bool:
    v=_rational(x,"unit")
    return v.numerator%2!=0 and v.denominator%2!=0


def source_prefix_at_beta(depth:int)->Q:
    """Finite BBP source evaluation at beta=1/16, rational not pi."""
    _integer(depth,"prefix depth",1,1000)
    return sum((authentic_r(n)*BETA**(n-1) for n in range(1,depth+1)),Q())


def discontinuity_witness(depth:int,at_one:bool=False)->tuple[tuple[Q,...],Q]:
    """Polynomial tends to zero in the chosen adic jet topology but
    evaluates to EXACTLY 1/2 at beta=1/16.
    """
    _integer(depth,"depth",1,64)
    if not at_one:
        poly=(Q(0),)*depth+(Q(16**depth,2),)
    else:
        poly=tuple(Q(1,2)*Q(16,15)**depth *(-1)**j*comb(depth,j)
                   for j in range(depth+1))
    if polynomial_evaluate(poly,BETA)!=Q(1,2):
        raise AssertionError("invalid noncontinuous evaluation witness")
    return poly,Q(1,2)


def regularized_slope_rational_certificate(depth:int)->tuple[Q,Q]:
    """Exact rational center +/- bound for one-log-germ slope d.

    d=15/64 + sum_{n>=1}[(n-1)r(n)-(15/64)/n].
    For n>=2, |r(n)-c/n^2|<=1/n^3. Thus omitted terms
    are ≤(1+c)/depth for depth>=2 (integral tail of 1/n²).
    This does NOT certify Gamma cancellation without the paper derivation.
    """
    _integer(depth,"slope certificate depth",2,100000)
    c=ASYMPTOTIC_MASS
    center=c+sum(((n-1)*authentic_r(n)-c/Q(n) for n in range(1,depth+1)),Q())
    radius=(1+c)/depth
    return center,radius


def residual_weighted_norm_prefix(depth:int)->Q:
    """Partial weighted Wiener norm of b_n=r(n)-c/n².

    Finite prefix only. The full sum converges by b_n=O(n^-3).
    """
    _integer(depth,"Wiener prefix depth",1,10000)
    return sum((Q(n)*abs(authentic_r(n)-ASYMPTOTIC_MASS/Q(n*n))
                for n in range(1,depth+1)),Q())


def rational_eval_tail_bound(depth:int)->Q:
    """Certified absolute error of the *original* pi BBP prefix.

    Original r(n)<1/[15 n(n-1)] for n>1 is unnecessarily strong;
    use elementary r(n)<=4/(8n-7)<=4/n for all n>=1.
    Then Σ_{n>depth} r(n)*beta^(n-1)
         <=[4/(depth+1)]*beta^depth/(1-beta).
    """
    _integer(depth,"prefix depth",1,100000)
    return Q(4,depth+1)*BETA**depth/(1-BETA)


def modadic_odd_rational(value:Q|int,depth:int)->int:
    """Canonical element of Z2 reduced modulo 16**depth."""
    _integer(depth,"hexadecimal depth",1,12)
    u=_rational(value,"odd-denominator rational")
    if u.denominator%2==0:
        raise ValueError("requires 2-adic integer with odd denominator")
    modulus=16**depth
    return u.numerator*pow(u.denominator,-1,modulus)%modulus


def mutant_stationary_clock(n:int,depth:int,K:int,J:int)->int:
    """Late-time exact source-history window, modulo 16**depth.

    Applicable to actual mutant states only if n-depth+1>=K+J+1.
    Otherwise negative/nonrational-extension source history differs.
    """
    _integer(n,"clock time",0,100000)
    _integer(depth,"hexadecimal depth",1,12)
    if n-depth+1<K+J+1:
        raise ValueError("window crosses early exceptional source prefix")
    return sum((16**j*modadic_odd_rational(mutant_rational_extension(n-j,K,J),depth)
                for j in range(depth)))%(16**depth)


def mutant_modular_states(max_time:int,depth:int,K:int,J:int)->tuple[int,...]:
    """Actual U0=0 recurrence in Z/(16**depth), exact no float."""
    _integer(max_time,"last time",0,10000)
    _integer(depth,"hexadecimal depth",1,12)
    mod=16**depth
    u=0
    seq=[0]
    for n in range(1,max_time+1):
        u=(16*u+modadic_odd_rational(mutant_source(n,K,J),depth))%mod
        seq.append(u)
    return tuple(seq)
