"""Certified finite BBP prime-window signed phases, EXACT rational enclosure.

Only fixed horizon N=128, prime p=257, original source U0=0. Uses independent
Machin arctangent enclosure of pi, dyadic floor, Taylor derivative bounds.
No pi digits, float phase evaluations, or asymptotic extrapolation.
"""
from __future__ import annotations
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from prime_phase import source,state,birth
from independent_oracle import u_convolution


def arctan_bounds(x:F,terms:int=15)->tuple[F,F]:
    assert F(0)<x<F(1) and terms>0
    s=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    rem=x**(2*terms+1)/F(2*terms+1)
    return (s,s+rem) if terms%2==0 else (s-rem,s)


def pi_bounds()->tuple[F,F]:
    a,b=arctan_bounds(F(1,5))
    c,d=arctan_bounds(F(1,239))
    low,up=16*a-4*d,16*b-4*c
    assert F(3)<low<up<F(22,7)
    return low,up


def floor_rational(x:F)->int:
    return x.numerator//x.denominator


def ceil_rational(x:F)->int:
    return -floor_rational(-x)


def exp_phase_interval(x:F,h:int,pi_interval:tuple[F,F],bits:int=32,terms:int=12):
    """Return (cos center,sin center,absolute per-component error), all Fraction."""
    assert isinstance(x,F) and h>=1 and bits>=16 and terms>=5
    ph=(h*x)%1
    if ph>F(1,2):ph-=1
    grid=F(floor_rational(ph*2**bits),2**bits)
    lo,hi=pi_interval
    theta=2*((lo+hi)/2)*grid
    assert abs(theta)<F(22,7)
    # Independent Taylor polynomials and derivative-based Lagrange bounds.
    cos=sum(((-1)**j*theta**(2*j)/F(factorial(2*j)) for j in range(terms+1)),F(0))
    sin=sum(((-1)**j*theta**(2*j+1)/F(factorial(2*j+1)) for j in range(terms+1)),F(0))
    rcos=(F(22,7)**(2*terms+1))/F(factorial(2*terms+1))
    rsin=(F(22,7)**(2*terms+2))/F(factorial(2*terms+2))
    # |2 pi (ph-grid)| < (44/7)*2^-bits; midpoint pi error <= hi-lo.
    err=rcos+rsin+(hi-lo)+F(44,7*2**bits)
    return cos,sin,err


def certify(N:int=128,p:int=257,h_values:tuple[int,...]=(1,3,5))->dict:
    b=birth(p)
    assert (N,p,b.n,b.first_reuse)==(128,257,33,129)
    us=[];u=F(0)
    for j in range(1,N+1):
        u=16*u+source(j)
        if j>=b.n:
            assert u==u_convolution(j)
            us.append(u)
    assert len(us)==96
    pit=pi_bounds()
    cases=[]
    scale=10**9
    for h in h_values:
        rec=F(0);imc=F(0);E=F(0)
        for u in us:
            co,si,err=exp_phase_interval(u,h,pit)
            rec+=co;imc+=si;E+=err
        L=F(len(us))
        re_lo=(rec-E)/L;re_up=(rec+E)/L
        im_lo=(imc-E)/L;im_up=(imc+E)/L
        bound=(abs(rec)+abs(imc)+2*E)/L
        target=F(1,16) if h==1 else F(1,8)
        assert bound<target,(h,float(bound),float(target))
        # Outward rational intervals; exact compare before round, and after.
        rounded={
            'real_interval':[str(F(floor_rational(re_lo*scale),scale)),
                             str(F(ceil_rational(re_up*scale),scale))],
            'imag_interval':[str(F(floor_rational(im_lo*scale),scale)),
                             str(F(ceil_rational(im_up*scale),scale))],
            'upper_L1':str(F(ceil_rational(bound*scale),scale)),
            'certified_strict_less_than':str(target),
        }
        assert F(rounded['upper_L1'])<target
        cases.append({'N':N,'prime':p,'h':h,'window':[b.n,N],
                      'sample_count':len(us),**rounded})
    return {'status':'CERTIFIED_EXACT_RATIONAL_INTERVAL','not_asymptotic':True,
            'pi_source':'Machin arctangent rational alternating series; not digits of pi',
            'phase_method':'dyadic floor + Taylor derivative remainder + source Fraction',
            'bits':32,'terms':12,'pi_terms':15,'cases':cases}


if __name__=='__main__':
    receipt=certify()
    path=Path(__file__).with_name('FINITE_SIGNED_INTERVAL_RECEIPT.json')
    path.write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
