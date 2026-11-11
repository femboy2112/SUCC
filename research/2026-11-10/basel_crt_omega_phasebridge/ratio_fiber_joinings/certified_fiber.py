"""Exact rational BBP bounds and certified trigonometric 3/2 fiber means.
No pi digit oracle, floating phase or zeta-zero inputs.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial
from functools import lru_cache
import json


def bbp_r(n:int)->F:
    if n<1: raise ValueError('n must be >=1')
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

@lru_cache(maxsize=4)
def bbp_pi_enclosure(K:int):
    """[integer/16**K, (integer+K+1)/16**K] encloses pi rigorously."""
    if K<2: raise ValueError('K>=2')
    q=16**K
    L=0
    for n in range(1,K+1):
        a=120*n*n-89*n+16
        b=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
        L+=(16**(K+1-n)*a)//b
    # Floor loss <K, BBP positive-tail contribution < 16/[(8K+1)(8K+2)]<1
    return L, L+K+1, q


def fiber_indices(A):
    if A<2: raise ValueError('A>=2')
    return list(range((A+1)//2, (2*A-1)//3+1))


def K32(ell):
    return 16**(2*ell-1)*(16**ell-1)


def phase_fraction_ticks(ell,h,lo_pi,hi_pi,Q,scale=10**32):
    c=h*K32(ell)
    if c<0: raise ValueError('h positive in this evaluator')
    l,u=c*lo_pi,c*hi_pi
    a,b=l//Q,u//Q
    if a!=b:
        raise ValueError(f'phase may straddle an integer at ell={ell}: increase K')
    lower=(l%Q)*scale//Q
    upper=((u%Q)*scale+Q-1)//Q
    return lower,upper,scale


def atan_interval_recip(d:int,T=22):
    if d<=1 or T<1: raise ValueError
    s=sum(((-1)**j)*F(1,(2*j+1)*d**(2*j+1)) for j in range(T))
    err=F(1,(2*T+1)*d**(2*T+1))
    if T%2==0: return s,s+err
    return s-err,s

@lru_cache(maxsize=1)
def pi_machin():
    a,b=atan_interval_recip(5)
    c,d=atan_interval_recip(239)
    return 16*a-4*d,16*b-4*c

@lru_cache(maxsize=1)
def pi_mid():
    p,q=pi_machin()
    assert F(3)<p<q<F(22,7)
    return (p+q)/2, (q-p)


def trig_interval(lo_tick,hi_tick,scale,T=17):
    """Certified (cos lower,upper),(sin lower,upper) with exact rational arithmetic."""
    assert 0<=lo_tick<=hi_tick<=scale
    m=F(lo_tick+hi_tick,2*scale)
    rad=F(hi_tick-lo_tick,2*scale)
    if m>F(1,2): m-=1
    p,spread=pi_mid()
    angle=2*p*m
    delta=2*F(22,7)*rad+abs(m)*spread
    theta2=angle*angle
    cos=F(1);sin=angle;power_even=F(1);power_odd=angle
    for k in range(1,T):
        power_even*=theta2
        power_odd*=theta2
        cos+=((-1)**k)*power_even/factorial(2*k)
        sin+=((-1)**k)*power_odd/factorial(2*k+1)
    e_cos=delta+F(22,7)**(2*T)/factorial(2*T)
    e_sin=delta+F(22,7)**(2*T+1)/factorial(2*T+1)
    return (cos-e_cos,cos+e_cos),(sin-e_sin,sin+e_sin)


def certified_mean(A,h=8,guard=12,precision=10**32):
    J=fiber_indices(A)
    K=2*A+guard
    p0,p1,Q=bbp_pi_enclosure(K)
    cr=F(0);ci=F(0);er=F(0);ei=F(0)
    for ell in J:
        t0,t1,sc=phase_fraction_ticks(ell,h,p0,p1,Q,precision)
        (cl,ch),(sl,sh)=trig_interval(t0,t1,sc)
        cr+=(cl+ch)/2;ci+=(sl+sh)/2
        er+=(ch-cl)/2;ei+=(sh-sl)/2
    q=len(J)
    # Integer outward rounding proves the public decimal enclosures exactly.
    outward=10**12
    def flo(fr): return fr.numerator//fr.denominator
    def ceil(fr): return -flo(-fr)
    real_ticks=[flo((cr-er)*outward/q),ceil((cr+er)*outward/q)]
    imag_ticks=[flo((ci-ei)*outward/q),ceil((ci+ei)*outward/q)]
    return {'real_outward_ticks_12dp':real_ticks,'imag_outward_ticks_12dp':imag_ticks,'A':A,'h':h,'J_length':q,'ell_first':J[0], 'ell_last':J[-1],
            'pi_enclosure_hex_digits':K,
            'real_mid':float(cr/q),'imag_mid':float(ci/q),
            'real_error_bound':float(er/q),'imag_error_bound':float(ei/q),
            'norm_mid':(float(cr/q)**2+float(ci/q)**2)**.5}

if __name__=='__main__':
    import sys
    A=int(sys.argv[1]) if len(sys.argv)>1 else 257
    print(json.dumps(certified_mean(A),indent=2))


def certified_hex_digit(n:int,L:int,U:int,Q:int, K:int):
    """Exact nth fractional hexadecimal digit of pi, if both rational endpoints agree."""
    if not 1<=n<=K: raise ValueError('index out of range')
    base=16**(K-n)
    a=(L//base)%16
    b=(U//base)%16
    if a!=b:
        raise ValueError(f'digit n={n} unresolved by source interval')
    return a


def source_digit_correlations(A:int, guard=12):
    K=2*A+guard
    lo,hi,Q=bbp_pi_enclosure(K)
    J=fiber_indices(A)
    matched1=matched2=parity_same=0
    for ell in J:
        m,n=2*ell,3*ell
        ds=[certified_hex_digit(j,lo,hi,Q,K) for j in (m,n,m+1,n+1)]
        m0,n0,m1,n1=ds
        matched1+=m0==n0
        matched2+=m0==n0 and m1==n1
        parity_same+=(m0-n0)%2==0
    return {'A':A,'N':len(J),'same_first_digit':matched1,
            'same_first_two_digits':matched2,'same_parity_first_digit':parity_same}
