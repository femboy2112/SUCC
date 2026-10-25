"""Rigorous rational rectangles for authentic finite BBP cyclotomic Weyl sums.

Source phases are exact rationals on the N-anchored BBP orbit.  The angle pi
is enclosed by independent Machin alternating arctangent brackets; Taylor's
real derivative remainder bounds enclose cos and sin.  This is a *finite*
certificate, not asymptotic cancellation or pi normality.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import factorial


def machin_pi_interval(pairs: int = 20) -> tuple[Q,Q]:
    if type(pairs) is not int or pairs < 1 or pairs>120:
        raise ValueError("1..120 positive Machin pairs required")
    terms=2*pairs
    def at(q):
        low=sum((Q((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms)),Q())
        return low,low+Q(1,(2*terms+1)*q**(2*terms+1))
    al,ah=at(5);bl,bh=at(239)
    return 16*al-4*bh,16*ah-4*bl


def characteristic_interval(turns: Q, pi_range: tuple[Q,Q], order: int=12) -> tuple[Q,Q,Q,Q]:
    """(cos_lower,cos_upper,sin_lower,sin_upper) for e(2*pi*i*turns)."""
    if type(turns) is not Q or type(pi_range) is not tuple or len(pi_range)!=2:
        raise ValueError("exact turn Fraction and pi bracket required")
    if type(order) is not int or order<1 or order>50:
        raise ValueError("Taylor order must lie in 1..50")
    lo,hi=pi_range
    if not (Q(3)<lo<hi<Q(4)):
        raise ValueError("valid rational pi bracket within (3,4) required")
    turns=turns%1
    if turns>Q(1,2):turns-=1
    # Certified finite-grid evaluation: round *outward* both the angle
    # constant and exact rational turns, paying an explicit Lipschitz cost.
    # This prevents a vast historical denominator from inflating Taylor powers.
    digits=10**16
    L=(lo*digits).numerator//(lo*digits).denominator
    V=hi*digits
    H=-((-V.numerator)//V.denominator)
    lo_q,hi_q=Q(L,digits),Q(H,digits)
    center=(lo_q+hi_q)/2
    radius=(hi_q-lo_q)/2
    grid=1<<48
    tscaled=turns*grid
    turns_q=Q(tscaled.numerator//tscaled.denominator,grid)
    x=2*center*turns_q
    cos=sum((Q((-1)**k, factorial(2*k))*x**(2*k)
             for k in range(order+1)),Q())
    sin=sum((Q((-1)**k,factorial(2*k+1))*x**(2*k+1)
             for k in range(order+1)),Q())
    cos_err=abs(x)**(2*order+2)/factorial(2*order+2)
    sin_err=abs(x)**(2*order+3)/factorial(2*order+3)
    angle_err=2*abs(turns_q)*radius+2*hi_q*abs(turns-turns_q)
    return (cos-cos_err-angle_err,cos+cos_err+angle_err,
            sin-sin_err-angle_err,sin+sin_err+angle_err)


def fourier_rect(phases: tuple[Q,...], frequency: int,
                 pi_range: tuple[Q,Q] | None = None, order: int=12) -> tuple[tuple[Q,Q],tuple[Q,Q]]:
    """Certified rectangle for N^-1 sum exp(2*pi*i*h*y_n)."""
    if not phases or any(type(x) is not Q for x in phases):
        raise ValueError("nonempty exact rational phases required")
    if type(frequency) is not int or frequency==0:
        raise ValueError("nonzero integer mode required")
    if pi_range is None:pi_range=machin_pi_interval()
    cs=ss=Q(); cr=sr=Q()
    for phase in phases:
        clo,chi,slo,shi=characteristic_interval(frequency*phase,pi_range,order)
        cs+=clo;cr+=chi;ss+=slo;sr+=shi
    n=len(phases)
    return (max(Q(-1),cs/n),min(Q(1),cr/n)),(max(Q(-1),ss/n),min(Q(1),sr/n))


def square_interval(lo: Q,hi: Q) -> tuple[Q,Q]:
    return (Q() if lo<=0<=hi else min(lo*lo,hi*hi),max(lo*lo,hi*hi))


def fourier_squared_interval(phases: tuple[Q,...],frequency: int,
                             pi_range: tuple[Q,Q] | None=None,order: int=12) -> tuple[Q,Q]:
    re,im=fourier_rect(phases,frequency,pi_range,order)
    a=square_interval(*re);b=square_interval(*im)
    return a[0]+b[0],min(Q(1),a[1]+b[1])


def outward_e8(x: Q) -> int:
    """Floor 1e8*x so [floor lo, floor hi+1]/1e8 encloses interval."""
    return (x*10**8).numerator//(x*10**8).denominator


def magnitude_decimal_bounds(square_range: tuple[Q,Q],places: int=6) -> tuple[str,str]:
    """Rigorous outward decimal magnitude endpoints (integer sqrt bounds)."""
    from math import isqrt
    if type(places) is not int or not 1<=places<=12:
        raise ValueError("1..12 decimal places required")
    lo,hi=square_range
    if not Q()<=lo<=hi<=1:raise ValueError("unit squared interval required")
    scale=10**places
    low=isqrt((lo*scale*scale).numerator//(lo*scale*scale).denominator)
    val=hi*scale*scale
    top=(val.numerator+val.denominator-1)//val.denominator
    upper=isqrt(top)+1
    return (f"{low//scale}.{low%scale:0{places}d}",
            f"{upper//scale}.{upper%scale:0{places}d}")
