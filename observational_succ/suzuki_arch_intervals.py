"""Rigorous Fraction bounds for Suzuki's complete Archimedean screw kernel.

For t>=0, Suzuki arXiv:2606.09096v3 (1.3), equivalently:
  g_inf(t)=-4(e^(t/2)+e^(-t/2)-2)
    +(t/2)*(gamma+pi/2+3 log 2+log pi)
    -sum_{j>=0}(1-e^{-(2j+1/2)t})/(2j+1/2)^2.

All returned intervals are rational and mathematically outward enclosures.
No nontrivial zero locations, and *no numerical special-function oracle*.
Only a first genuine-prime window is supported for the completed kernel.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt
from .suzuki_prime_boundary import exact_fraction


class ArchIntervalError(ValueError):
    pass


def atan_interval(x: Q, count: int = 8) -> tuple[Q, Q]:
    x=exact_fraction(x)
    if not Q(0)<x<=Q(1):
        raise ArchIntervalError("arctan Taylor bound requires 0<x<=1")
    if type(count) is not int or not 1<=count<=100:
        raise ArchIntervalError("invalid Taylor count")
    s=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(count)),Q())
    next_term=(-1)**count*x**(2*count+1)/Q(2*count+1)
    return min(s,s+next_term),max(s,s+next_term)


def pi_interval(count: int = 8) -> tuple[Q,Q]:
    a,b=atan_interval(Q(1,5),count)
    c,d=atan_interval(Q(1,239),count)
    return 16*a-4*d,16*b-4*c


def log_interval(x: Q, count: int = 16) -> tuple[Q,Q]:
    x=exact_fraction(x)
    if not x>=1:
        raise ArchIntervalError("logx uses x>=1")
    if type(count) is not int or not 1<=count<=150:
        raise ArchIntervalError("invalid log count")
    z=(x-1)/(x+1)
    if z==0:
        return Q(),Q()
    s=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(count)),Q())
    tail=2*z**(2*count+1)/((2*count+1)*(1-z*z))
    return s,s+tail


def log2_interval(count: int = 16) -> tuple[Q,Q]:
    return log_interval(Q(2),count)


def log_pi_interval(count: int = 24) -> tuple[Q,Q]:
    lo,hi=pi_interval(9)
    return log_interval(lo,count)[0],log_interval(hi,count)[1]


def gamma_interval(power: int = 8) -> tuple[Q,Q]:
    # Classic H_N-log(N)-gamma in (1/(2(N+1)),1/(2N)); N=2^power.
    if type(power) is not int or not 1<=power<=11:
        raise ArchIntervalError("invalid harmonic power")
    N=2**power
    harmonic=sum((Q(1,k) for k in range(1,N+1)),Q())
    l2_lo,l2_hi=log2_interval(18)
    return harmonic-power*l2_hi-Q(1,2*N), harmonic-power*l2_lo-Q(1,2*(N+1))


def exp_interval(x: Q, extra_terms: int = 15) -> tuple[Q,Q]:
    """Rational enclosure e^x for x>=0 by positive Taylor/geometric tail."""
    x=exact_fraction(x)
    if x<0 or x>100:
        raise ArchIntervalError("exp argument must lie in [0,100]")
    if type(extra_terms) is not int or not 6<=extra_terms<=100:
        raise ArchIntervalError("invalid exp remainder budget")
    N=(x.numerator+x.denominator-1)//x.denominator+extra_terms
    term,s=Q(1),Q(1)
    for k in range(1,N+1):
        term=term*x/k
        s+=term
    next_term=term*x/(N+1)
    ratio=x/Q(N+2)
    if ratio>=1:
        raise ArithmeticError("invalid Taylor geometric-ratio certificate")
    return s,s+next_term/(1-ratio)


def exp_minus_interval(x:Q,extra_terms:int=15)->tuple[Q,Q]:
    lo,hi=exp_interval(x,extra_terms)
    return 1/hi,1/lo


def sqrt2_interval(places:int=15)->tuple[Q,Q]:
    if type(places) is not int or not 4<=places<=80:
        raise ArchIntervalError("invalid radical precision")
    scale=10**places
    m=isqrt(2*scale*scale)
    return Q(m,scale),Q(m+1,scale)


def arch_lerch_tail_interval(t:Q, terms:int=32,
                             exp_extra_terms:int=15)->tuple[Q,Q]:
    """Bounds H(t)=sum_(j>=0) (1-exp(-alpha_j*t))/alpha_j².

    For decreasing h(x)=(1-e^(-xt))/x², the tail for alpha_j=2j+1/2
    satisfies int_N^inf h(2x+1/2)dx <= sum_(j>=N) h(alpha_j)
       <= h(alpha_N)+int_N^inf h(2x+1/2)dx.
    With A=2N+1/2, 1-e^(-At) >= At/(1+At), and 1-e^(-At)<=1:
      tail in [ t/(2(1+At)),  1/(2A)+1/A² ].
    """
    t=exact_fraction(t)
    if not Q(0)<=t<=2 or type(terms) is not int or not 4<=terms<=500:
        raise ArchIntervalError("t in [0,2], 4<=terms<=500 required")
    if t==0:return Q(),Q()
    lo=hi=Q()
    for j in range(terms):
        alpha=Q(4*j+1,2)
        e_lo,e_hi=exp_minus_interval(alpha*t,exp_extra_terms)
        lo+=(1-e_hi)/(alpha*alpha)
        hi+=(1-e_lo)/(alpha*alpha)
    A=Q(4*terms+1,2)
    lo+=t/(2*(1+A*t))
    hi+=Q(1,2*A)+Q(1,A*A)
    return lo,hi


def arch_screw_interval(t:Q, terms:int=32,
                        exp_extra_terms:int=15)->tuple[Q,Q]:
    """FULL completed *Archimedean* term of source-specific Suzuki (1.3).

    Includes the e^{+/-t/2} pole terms, gamma/digamma term and infinite
    Hurwitz-Lerch series; rational certified bounds, no pi/gamma oracles.
    """
    t=exact_fraction(t)
    if not Q(0)<=t<=2:
        raise ArchIntervalError("only t in [0,2]")
    if t==0:return Q(),Q()
    ep_lo,ep_hi=exp_interval(t/2,exp_extra_terms)
    em_lo,em_hi=exp_minus_interval(t/2,exp_extra_terms)
    pole_lo=-4*(ep_hi+em_hi-2)
    pole_hi=-4*(ep_lo+em_lo-2)
    gam_lo,gam_hi=gamma_interval(8)
    pi_lo,pi_hi=pi_interval(9)
    l2_lo,l2_hi=log2_interval(18)
    lp_lo,lp_hi=log_pi_interval(24)
    linear_lo=t/2*(gam_lo+pi_lo/2+3*l2_lo+lp_lo)
    linear_hi=t/2*(gam_hi+pi_hi/2+3*l2_hi+lp_hi)
    H_lo,H_hi=arch_lerch_tail_interval(t,terms,exp_extra_terms)
    return pole_lo+linear_lo-H_hi,pole_hi+linear_hi-H_lo


def outward_decimal_interval(lo:Q,hi:Q,digits:int=12)->tuple[Q,Q]:
    """Exact outward rounding before printing otherwise enormous rational numerators.

    Computations remain Fraction-exact; rounded endpoints are necessarily wider.
    No numerical floating conversion is used in the proof certificate.
    """
    if type(digits) is not int or not 2<=digits<=30 or lo>hi:
        raise ArchIntervalError("invalid outward-rounding request")
    scale=10**digits
    lower=(lo.numerator*scale)//lo.denominator
    upper=-((-hi.numerator*scale)//hi.denominator)
    return Q(lower,scale),Q(upper,scale)


def first_source_screw_interval(t:Q, terms:int=32)->dict:
    """Full g(t) for 0<=t< (6/5)log 2, with a=(3/5)log2.

    The *only* arithmetic contribution is genuine prime n=2. The source
    threshold inequalities are checked using outward rational log2 bounds.
    """
    t=exact_fraction(t)
    if t<0:
        raise ArchIntervalError("nonnegative t only")
    l2_lo,l2_hi=log2_interval(18)
    if t>=Q(6,5)*l2_lo:
        raise ArchIntervalError("t lies outside the rigorously verified first-prime window")
    a,b=arch_screw_interval(t,terms)
    prime_lo=prime_hi=Q()
    if t>l2_lo:
        sq_lo,sq_hi=sqrt2_interval(18)
        prime_lo=l2_lo*max(Q(),t-l2_hi)/sq_hi
        prime_hi=l2_hi*max(Q(),t-l2_lo)/sq_lo
    a,b=outward_decimal_interval(a,b)
    prime_lo,prime_hi=outward_decimal_interval(prime_lo,prime_hi)
    full_lo,full_hi=outward_decimal_interval(a+prime_lo,b+prime_hi)
    return {"t":str(t),"arch_lower":str(a),"arch_upper":str(b),
            "prime_lower":str(prime_lo),"prime_upper":str(prime_hi),
            "full_lower":str(full_lo),"full_upper":str(full_hi),
            "pole_gamma_lerch_included":True,
            "true_prime_2_half_density_included":True,
            "fake_composite_six_included":False,
            "strict_first_source_interval":True,
            "zero_locations_read":False,"RH_proved":False}
