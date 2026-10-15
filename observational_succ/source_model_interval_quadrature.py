"""Fully rational interval enclosures for xi at REAL non-Euler arguments.

Unlike the numeric oracle, this supplies both certified finite-integral
quadrature bounds and analytic infinite theta-mode/time tails. Supported real
s are 1/2 and -2/3, whose source integrands are monotonically decreasing
for all t>=1. This is classical theta continuation, not an RH proof.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import factorial,isqrt
from .source_model_interaction import (
    SourceInteractionError, _nat, _rational, analytic_theta_tail,
)


def atan_interval(x:Q, count:int=18)->tuple[Q,Q]:
    if not 0<x<1: raise SourceInteractionError("atan input in (0,1) required")
    _nat(count,2,100)
    part=sum((Q((-1)**k)*x**(2*k+1)/Q(2*k+1) for k in range(count)),Q())
    nextterm=Q((-1)**count)*x**(2*count+1)/Q(2*count+1)
    return min(part,part+nextterm),max(part,part+nextterm)


def pi_bounds()->tuple[Q,Q]:
    a,b=atan_interval(Q(1,5))
    c,d=atan_interval(Q(1,239))
    return 16*a-4*d,16*b-4*c


def _down(x:Q, precision:int=28)->Q:
    scale=10**precision
    return Q(x.numerator*scale//x.denominator,scale)


def _up(x:Q,precision:int=28)->Q:
    scale=10**precision
    return Q(-(-x.numerator*scale//x.denominator),scale)


def sqrt_rational(x:Q, precision:int=28)->tuple[Q,Q]:
    x=_rational(x)
    if x<=0:raise SourceInteractionError("positive rational sqrt required")
    scale=10**precision
    k=isqrt(x.numerator*scale**2//x.denominator)
    lo=Q(k,scale)
    hi=Q(k if Q(k*k,scale*scale)==x else k+1,scale)
    if lo*lo>x or hi*hi<x:
        raise ArithmeticError("root interval unsound")
    return lo,hi


def fourth_root_rational(x:Q,precision:int=28)->tuple[Q,Q]:
    lo,hi=sqrt_rational(x,precision)
    a,_=sqrt_rational(lo,precision)
    _,b=sqrt_rational(hi,precision)
    return a,b


def exp_neg_bounds(xlo:Q,xhi:Q,precision:int=28)->tuple[Q,Q]:
    """Exact exp(-xhi)<=e^-x<=exp(-xlo) using rigorous Taylor tails."""
    xlo,xhi=_rational(xlo),_rational(xhi)
    if not Q()<=xlo<=xhi:
        raise SourceInteractionError("ordered positive exponent interval required")
    m=max(60, (2*xhi.numerator)//xhi.denominator+20)
    if m>750:raise SourceInteractionError("only bounded source exponent values")
    def series(x):
        power,acc=Q(1),Q(1)
        for k in range(1,m+1):
            power*=x/k
            acc+=power
        nxt=power*x/(m+1)
        ratio=x/(m+2)
        if ratio>=1:raise ArithmeticError("exp tail no geometric majorant")
        return acc,acc+nxt/(1-ratio)
    _,exp_hi_upper=series(xhi)
    exp_lo_lower,_=series(xlo)
    return _down(1/exp_hi_upper,precision),_up(1/exp_lo_lower,precision)


def _weight_bounds(t:Q, s:Q)->tuple[Q,Q]:
    """Both source powers t^(s/2-1)+t^((1-s)/2-1)."""
    if s==Q(1,2):
        a,b=fourth_root_rational(t)
        return 2*b**(-3),2*a**(-3)
    if s in (Q(-2),Q(3)):
        a,b=sqrt_rational(t)
        return Q(1,t*t)+a,Q(1,t*t)+b
    raise SourceInteractionError("certified real quadrature only supports 1/2 and -2/3")


def _gaussian_sequence(N:int,T:int,intervals:int,precision:int=28)->list[tuple[Q,Q]]:
    dt=Q(T-1,intervals)
    pilo,pihi=pi_bounds()
    # g_n(t_j) for t_j=1+j*dt from recurrence with step exp(-pi*n²*dt).
    start=[];ratio=[]
    for n in range(1,N+1):
        start.append(exp_neg_bounds(pilo*n*n,pihi*n*n,precision))
        ratio.append(exp_neg_bounds(pilo*n*n*dt,pihi*n*n*dt,precision))
    current=list(start)
    sequence=[]
    for j in range(intervals+1):
        lo=sum((x for x,y in current),Q())
        hi=sum((y for x,y in current),Q())
        sequence.append((lo,hi))
        if j<intervals:
            current=[(_down(x*c,precision),_up(y*d,precision))
                     for (x,y),(c,d) in zip(current,ratio)]
    return sequence


def certified_real_xi(s:int|Q,modes:int=2,endpoint:int=8,intervals:int=1024,
                      precision:int=28,steps:int=128)->dict:
    """Rigorous finite rational enclosure of xi(s), for s=-2,1/2,3.

    With t>=1 each Gaussian-weighted monomial is strictly decreasing;
    use right-grid lower and left-grid upper, then add theta omitted-tail upper.
    The original lattice/Poisson identity is a classical analytic theorem import.
    """
    s=_rational(s)
    if s not in (Q(1,2),Q(-2),Q(3)):
        raise SourceInteractionError("supported exact real sources are -2, 1/2, 3")
    N=_nat(modes,1,8)
    T=_nat(endpoint,2,20)
    M=_nat(intervals,8,10000)
    prec=_nat(precision,12,60)
    dt=Q(T-1,M)
    gaussians=_gaussian_sequence(N,T,M,prec)
    lower=upper=Q()
    for j,(plo,phi) in enumerate(gaussians):
        t=Q(1)+dt*j
        wlo,whi=_weight_bounds(t,s)
        if j>0:lower+=dt*plo*wlo
        if j<M:upper+=dt*phi*whi
    theta_tail=Q(analytic_theta_tail(s,s,N,T,0,steps)['rational_upper'])
    Jlo,Jhi=lower,upper+theta_tail
    if Jhi<Jlo:
        raise ArithmeticError("finite Riemann envelope unsound")
    pref=s*(s-1)/2
    if pref>=0:
        xi_lo,xi_hi=Q(1,2)+pref*Jlo,Q(1,2)+pref*Jhi
    else:
        xi_lo,xi_hi=Q(1,2)+pref*Jhi,Q(1,2)+pref*Jlo
    if not xi_lo<xi_hi:
        raise ArithmeticError("certified xi interval collapsed unexpectedly")
    return {"s":str(s),"modes":N,"endpoint":T,"intervals":M,
            "pi_Machin_terms":18,"rational_rounding_places":prec,
            "theta_quadrature_lower":str(_down(Jlo,prec)),
            "theta_quadrature_upper":str(_up(Jhi,prec)),
            "xi_lower":str(_down(xi_lo,prec)),
            "xi_upper":str(_up(xi_hi,prec)),
            "xi_width_upper":str(_up(xi_hi-xi_lo,prec)),
            "theta_omitted_tail_upper":str(_up(theta_tail,prec)),
            "source_proof_import":"Jacobi/adelic Poisson and Mellin identity",
            "fully_rational_numerical_enclosure":True,
            "no_zero_lookup":True,"RH_proved":False}
