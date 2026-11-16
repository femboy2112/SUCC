"""Original four-pole BBP Green-time, moving-frequency signed source experiment.

This is a *source tail* theorem, NOT the original completed real pi-circle Weyl
sum. All stochastic/normality comparisons must retain the rational U_n phase.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction
from math import comb
import mpmath as mp
from gamma_phase import source_r

@lru_cache(maxsize=None)
def tail_rational(n: int, depth: int=45) -> Fraction:
    if n<0 or depth<1: raise ValueError('n>=0 and depth>=1')
    return sum((source_r(n+j)/16**j for j in range(1,depth+1)),Fraction(0))

def tail_interval(n: int, depth: int=45):
    """Genuine source Green tail enclosed without any pi digits/constants."""
    partial=tail_rational(n,depth)
    return partial, partial + source_r(n+depth+1)/(15*16**depth)

def positive_step_difference(n: int,k: int,ell: int=2,depth:int=45):
    """Certified interval of (-1)^k Delta_ell^k T_n.

    For alternating finite coefficients, interval endpoints swap as needed.
    """
    if n<0 or k<0 or ell<1: raise ValueError('n,k>=0 and ell>=1')
    lo=Fraction(0);hi=Fraction(0)
    for j in range(k+1):
        a,b=tail_interval(n+j*ell,depth)
        weight=(-1)**j*comb(k,j)
        if weight>=0:
            lo+=weight*a;hi+=weight*b
        else:
            lo+=weight*b;hi+=weight*a
    return lo,hi

def shell_response(B: int,k: int,ell: int=2,exponent=0.5,depth=45,dps=55):
    """Complex signed mean at prescribed h_B ~ B^(k+2+exponent).

    For finite exact certification, phase error is bounded separately by
    source tail intervals; returned value is a high-precision diagnostic.
    """
    if B<1 or k<0 or ell<1: raise ValueError('B>0,k>=0,ell>0')
    with mp.workdps(dps):
        h=int(mp.nint(mp.power(B,k+2+mp.mpf(exponent))))
        total=mp.mpc(0);max_phase_budget=mp.mpf(0);max_phase_budget_exact=Fraction(0)
        for n in range(B,2*B):
            lo,hi=positive_step_difference(n,k,ell,depth)
            mid=(mp.mpf(lo.numerator)/lo.denominator+mp.mpf(hi.numerator)/hi.denominator)/2
            width=mp.mpf(hi.numerator)/hi.denominator-mp.mpf(lo.numerator)/lo.denominator
            max_phase_budget=max(max_phase_budget,mp.mpf(7)*h*width/2)
            max_phase_budget_exact=max(max_phase_budget_exact,Fraction(7*h,2)*(hi-lo))
            total+=mp.exp(2j*mp.pi*h*mid)
        return {'h':h,'B':B,'k':k,'ell':ell,
                'value':total/B,'max_phase_halfwidth_bound':max_phase_budget,
                'rigorous_phase_halfwidth_bound_fraction':str(max_phase_budget_exact)}

def limiting_integral(B,k,ell=2,exponent=0.5,dps=55):
    with mp.workdps(dps):
        h=int(mp.nint(mp.power(B,k+2+mp.mpf(exponent))))
        c=mp.mpf(h)/mp.power(B,k+2)
        p=k+2
        A=mp.mpf(ell)**k*mp.gamma(p)/64
        return +mp.quad(lambda y:mp.exp(2j*mp.pi*c*A/y**p),[1,2])
