"""Rational Machin/Taylor certificate for the source sum in MF-03B.

Uses separately written forcing; no floating-point trigonometry or fitted pi.
All output bounds are outward rounded to rationals with denominator 10^12.
"""
from fractions import Fraction as F
from math import factorial
import json


def atan_sum(q,n):
    return sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(n)),F())


PI_LO=16*atan_sum(5,30)-4*atan_sum(239,9)
PI_HI=16*atan_sum(5,31)-4*atan_sum(239,8)


def source(k):
    return F(4,8*k-7)-F(2,8*k-4)-F(1,8*k-3)-F(1,8*k-2)


def cosine_upper(t):
    t=t%1
    d=min(t,1-t)
    x=2*PI_LO*d  # cos decreases on [0,pi]; x is a lower angle.
    # Degree24 alternating truncation ends positive and bounds cos above.
    return sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(13)),F())


def rounded_up(x):
    scale=10**12
    return F(-((-x.numerator*scale)//x.denominator),scale)


def run():
    assert F(3)<PI_LO<PI_HI<F(22,7)
    rows=[]
    for a in (40,76):
        for h in ((512*a*a+14)//15, a**3//2, a**3):
            if not (F(512*a*a,15)<=h<=a**3): continue
            phases=[h*source(n+1) for n in range(a,2*a)]
            upper=F(a)
            for i,x in enumerate(phases):
                for y in phases[i+1:]: upper+=2*cosine_upper(x-y)
            bound=F(256*a**3,15*h)
            assert upper<bound*bound,(a,h,'monotone phase certificate')
            assert upper<F(a*a,4),(a,h,'source modulus <= A/2')
            rows.append({'A':a,'h':h,'source_modulus_squared_upper':str(rounded_up(upper)),
                         'analytic_modulus_bound':str(bound),'signed_deficit_lower':str(F(a,578))})
    return {'status':'PASS','machin_pi_width_upper':str(rounded_up(PI_HI-PI_LO)),
            'rows':rows,'scope':'finite rational source sum certificates, not pi normality'}


if __name__=='__main__': print(json.dumps(run(),indent=2))
