"""Three independent constructions of pi with exact rational enclosures.

1. Dyadic inscribed/circumscribed polygon by rational radical interval arithmetic.
2. Gaussian lattice disk count with outward rational square-tile enclosure.
3. Authentic four-pole BBP series with positive rational tail bound.
No transcendental numerical oracle is invoked in assertions.
"""
from __future__ import annotations
from fractions import Fraction as Q
from math import isqrt
from gaussian_circle_probe import gauss_pi_rational_enclosure,bbp_pi_enclosure

SCALE=10**42

def sqrt_enclose(x:Q):
    assert x>=0
    x=Q(x)
    a=isqrt((x.numerator*SCALE*SCALE)//x.denominator)
    l=Q(a,SCALE);u=Q(a+1,SCALE)
    assert l*l<=x<u*u
    return l,u

def viete_polygon_intervals(depth:int):
    """At m=0, N=4 regular inscribed square; at m>0, angle bisects.

    Each finite rational interval encloses pi by elementary polygon geometry.
    """
    assert depth>=0
    slo,shi=sqrt_enclose(Q(1,2));clo,chi=slo,shi
    result=[]
    for m in range(depth+1):
        N=4*(2**m)
        lower=N*slo
        upper=N*shi/clo
        assert 0<lower<upper
        result.append((N,lower,upper))
        # cos(theta/2)=sqrt((1+cos theta)/2),
        # sin(theta/2)=sqrt((1-cos theta)/2).
        newslo,newshi=sqrt_enclose(Q(1,2)*(1-chi))[0],sqrt_enclose(Q(1,2)*(1-clo))[1]
        newclo,newchi=sqrt_enclose(Q(1,2)*(1+clo))[0],sqrt_enclose(Q(1,2)*(1+chi))[1]
        slo,shi,clo,chi=newslo,newshi,newclo,newchi
    return result

def three_way():
    ell=bbp_pi_enclosure(12)
    out=[]
    for (N,a,b) in viete_polygon_intervals(9):
        g=gauss_pi_rational_enclosure(max(4,N//4))
        assert max(a,g[0],ell[0])<min(b,g[1],ell[1])
        out.append((N,a,b))
    assert out[-1][2]-out[-1][1] <out[0][2]-out[0][1]
    return out

def run():
    data=three_way()
    print('PASS: 10 exact Viete polygon interval stages, cross-checked with independent BBP and Gaussian disk rational enclosures')
    for N,a,b in (data[0],data[2],data[5],data[-1]):
        print(f'N={N} lower={float(a):.12f} upper={float(b):.12f} width<{float(b-a):.6g}')
    print('Scope: exact real-number completion; no statistical distribution or normality theorem.')
if __name__=='__main__':run()
