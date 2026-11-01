"""Exact rational enclosure for a circle path quotient and authentic BBP certificates.

Classical geometry: after k successive arc bisections, the unit-semicircle
inscribed polyline has 2**k chords. Pi_k = 2**k*c_k where c_0=2 and
c_(k+1)^2 = c_k^2/[2*(1+sqrt(1-c_k^2/4))].

Unlike floating sqrt, this module uses guaranteed outward Fraction bounds
via integer isqrt. Geometry and BBP are distinct inputs; their shared limit
is the standard circle-to-BBP identity, NOT a digit-normality proof.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt


class CarrierError(ValueError):
    pass


def _int_at_least(x, lower=1, upper=80):
    if type(x) is not int or not lower <= x <= upper:
        raise CarrierError("exact bounded integer required")
    return x


def sqrt_out(x: F, digits: int = 85) -> tuple[F,F]:
    """Exact enclosure sqrt(x) between neighboring multiples of 10^-digits."""
    _int_at_least(digits, 10, 300)
    x=F(x)
    if x<0: raise CarrierError("negative radical")
    q=10**digits
    floor=isqrt(x.numerator*q*q//x.denominator)
    l=F(floor,q)
    u=l if l*l==x else F(floor+1,q)
    assert l*l<=x<=u*u
    return l,u


@dataclass(frozen=True)
class Bound:
    lo:F
    hi:F
    def __post_init__(self):
        if F(self.lo)>F(self.hi):raise CarrierError("inverted rational interval")
    def contains(self, x):return self.lo<=x<=self.hi


def chord_square_intervals(k: int, digits=85) -> Bound:
    """Outward exact nested Pythagorean intervals for squared chord lengths."""
    _int_at_least(k,0,80)
    _int_at_least(digits,10,300)
    low=high=F(4)
    for _ in range(k):
        # f(y) = y/(2(1+sqrt(1-y/4))) is strictly increasing on [0,4].
        up_sqrt=sqrt_out(1-low/4,digits)[1]
        low2=low/(2*(1+up_sqrt))
        low_sqrt=sqrt_out(1-high/4,digits)[0]
        high2=high/(2*(1+low_sqrt))
        low,high=low2,high2
        if not F(0)<low<=high<=4: raise ArithmeticError("invalid polygon enclosure")
    return Bound(low,high)


def polygon_pi_interval(k: int,digits=85) -> Bound:
    """Pi_lower=inscribed semicircle/diameter quotient.

    Returns a certified interval of this algebraic *lower approximation*,
    NOT an enclosure of pi itself (see polygon_bracket).
    """
    sq=chord_square_intervals(k,digits)
    scale=2**k
    lo=sqrt_out(sq.lo,digits)[0]*scale
    hi=sqrt_out(sq.hi,digits)[1]*scale
    return Bound(lo,hi)


def polygon_bracket(k:int,digits=85)->Bound:
    """Rigorous [lower,upper] enclosure for pi from inscribed/circumscribed paths.

    At k=0 the circumscribed bound diverges; require k>=1.
    """
    _int_at_least(k,1,80)
    sq=chord_square_intervals(k,digits)
    inscribed=polygon_pi_interval(k,digits).lo
    coslo=sqrt_out(1-sq.hi/4,digits)[0]
    if coslo<=0:raise ArithmeticError("positive tangent angle needed")
    # The upper bound uses upper rounded c and lower rounded cosine.
    circumscribed=(2**k)*sqrt_out(sq.hi,digits)[1]/coslo
    return Bound(inscribed,circumscribed)


def polygon_error_bound(k:int)->F:
    """Pi-Pi_k < (8/3)*4^-k, using sin x > x-x^3/6 and pi<4."""
    _int_at_least(k,0,80)
    return F(8,3*4**k)


def bbp_r(n:int)->F:
    _int_at_least(n,1,150)
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)


def bbp_r_combined(n:int)->F:
    _int_at_least(n,1,150)
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def bbp_lower(n:int)->F:
    _int_at_least(n,1,80)
    return sum((F(16,16**j)*bbp_r(j) for j in range(1,n+1)),F())


def wilson_defect(n:int)->F:
    _int_at_least(n,1,120)
    return 15*(bbp_r(n)-bbp_r(n+1))


def wilson_upper(n:int)->F:
    _int_at_least(n,1,80)
    return F(16,225)*(47-sum((wilson_defect(j)/16**j for j in range(1,n+1)),F()))


def wilson_upper_faster(n:int)->F:
    _int_at_least(n,1,80)
    return bbp_lower(n)+F(16,15*16**n)*bbp_r(n+1)


def bbp_tail_upper(n:int)->F:
    _int_at_least(n,1,80)
    return F(1,4*n*n*16**n)


def bbp_tail_lower(n:int)->F:
    _int_at_least(n,1,80)
    return F(4,16**n*(8*n+1)*(8*n+2))


def curvature_tail_bound(n:int)->F:
    _int_at_least(n,1,80)
    return F(16,3375)*wilson_defect(n+1)/16**n


def bridge_certificate(n:int,digits=85)->dict:
    """Classical independent-geometric vs authentic source finite double bracket.

    For n>=2 the inequality Pi_(4n)>BBP_lower(n) follows from
      3*16**n > 2*(8n+1)*(8n+2),
    the absolute geometric error bound and one source term lower bound.
    For n=1 the rational-arithmetic interval directly proves the inequality.
    """
    _int_at_least(n,1,16)
    poly=polygon_pi_interval(4*n,digits)
    geo=polygon_bracket(4*n,digits)
    b=bbp_lower(n)
    w=wilson_upper(n)
    if not (b<poly.lo and poly.hi<min(geo.hi,w)):
        raise ArithmeticError("attempted finite geometric/source bracket did not certify")
    if n>=2 and not 3*16**n>2*(8*n+1)*(8*n+2):
        raise ArithmeticError("insufficient universal tail separation")
    if wilson_upper_faster(n)!=w:raise ArithmeticError("Wilson telescoping invalid")
    return dict(n=n,k=4*n,bbp_lower=b,polygon_lower_interval=poly,
                polygon_upper=geo.hi,wilson_upper=w, certified_upper=min(geo.hi,w),
                polygon_error=polygon_error_bound(4*n),
                bbp_tail_upper=bbp_tail_upper(n),
                bbp_tail_lower=bbp_tail_lower(n))


def affine_orbit(n:int,seed=F(0))->F:
    _int_at_least(n,0,80)
    x=F(seed)
    for j in range(1,n+1):x=16*x+bbp_r(j)
    return x


def common_phase_echo(n:int,seed=F(0))->F:
    """Exact rational phase in cycles; e(phase) recovered by independent echoes."""
    return affine_orbit(n,seed)


def source_step_laurent_poles()->tuple[F,...]:
    return (F(7,8),F(1,2),F(3,8),F(1,4))


def odd_bbp_conductor(n:int)->int:
    """Exact minimal common denominator of original zero-seeded states U_1..U_n."""
    from math import lcm
    _int_at_least(n,1,35)
    d=1
    x=F()
    for j in range(1,n+1):
        x=16*x+bbp_r(j)
        d=lcm(d,x.denominator)
    assert d%2==1
    return d


def crt_joint_carrier(k:int,n:int)->dict:
    """Coprime geometry and original BBP circle finite phase conductors."""
    _int_at_least(k,0,60)
    _int_at_least(n,1,35)
    a=2**(k+2) # geometrical half-angle phase e^(i*pi/2^(k+1))
    b=odd_bbp_conductor(n)
    assert b%2==1
    return {'geometry_2power':a,'bbp_odd':b,'combined':a*b}


def crt_reconstruct(a:int,b:int,m:int,n:int)->int:
    """Inverse of Z/(mn) -> Z/m x Z/n when gcd(m,n)=1."""
    from math import gcd
    if type(a) is not int or type(b) is not int or type(m) is not int or type(n) is not int or m<=0 or n<=0 or gcd(m,n)!=1:
        raise CarrierError("CRT requires coprime positive moduli and integer labels")
    return (a*n*pow(n,-1,m)+b*m*pow(m,-1,n))%(m*n)
