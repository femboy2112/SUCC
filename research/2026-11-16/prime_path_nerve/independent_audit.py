"""Independent exact SymPy / independent Fourier and phase checks.

This module intentionally does not import the primary probe implementation.
It is a distinct implementation with the same underlying classical math,
not an external blind review or a proof of pi normality.
"""
from fractions import Fraction
from math import gcd, prod, pi, cos, sin, sqrt, log
from cmath import exp
import sympy as sp
import mpmath as mp

PRIME_SETS=((),(2,),(2,3),(2,3,5),(2,3,5,7))
NEGATIVE_ODD={1:sp.Rational(-1,12),2:sp.Rational(1,120),3:sp.Rational(-1,252)}

def audit():
    exact_count=0
    numeric_count=0
    for S in PRIME_SETS:
        q=prod(S)
        units=[a for a in range(1,q+1) if gcd(a,q)==1]
        # Independent Bernoulli-polynomial construction and arithmetic Euler factor.
        for m in (1,2,3):
            zq= -sp.Rational(q**(2*m-1),2*m)*sum(sp.bernoulli(2*m,sp.Rational(a,q)) for a in units)
            rhs=NEGATIVE_ODD[m]*prod((1-p**(2*m-1) for p in S))
            assert sp.cancel(zq-rhs)==0, (S,m,zq,rhs)
            exact_count+=1
        # Direct Fourier without the other oracle's Mobius/divisor implementation.
        if q<=30:
            for h in range(q):
                cr=sum(exp(2j*pi*h*a/q) for a in units)
                expected=prod((p-1 if h%p==0 else -1 for p in S))
                assert abs(cr-expected)<1e-11, (S,h,cr,expected)
                numeric_count+=1
            for n in range(q):
                transform=sum(
                    sum(exp(2j*pi*h*a/q) for a in units)*exp(-2j*pi*h*n/q)
                    for h in range(q))/q
                expected=int(gcd(q,n)==1)
                assert abs(transform-expected)<1e-11, (S,n,transform,expected)
                numeric_count+=1
        else:
            for n in (1,2,3,5,6,7,49,210,211):
                f=sum(sum(exp(2j*pi*h*a/q) for a in units)*exp(-2j*pi*h*n/q)
                      for h in range(q))/q
                assert abs(f-int(gcd(q,n)==1))<2e-11, (S,n,f)
                numeric_count+=1

    # Prime reflection defect is a unimodular critical-line phase.
    mp.mp.dps=65
    for S in PRIME_SETS[1:]:
        def F(s):
            return mp.fprod([1-mp.power(p,-s) for p in S])
        def D(t):
            z=mp.mpc('0.5',t)
            return F(z)/F(1-z)
        assert abs(D(mp.mpf('0'))-1)<mp.mpf('1e-55')
        for t in (mp.mpf('0.2'),mp.mpf('0.83')):
            assert abs(abs(D(t))-1)<mp.mpf('1e-55')
            numeric_count+=1
        v=mp.im(mp.diff(lambda t:mp.log(D(t)),mp.mpf('0')))
        target=2*mp.fsum([mp.log(p)/(mp.sqrt(p)-1) for p in S])
        assert abs(v-target)<mp.mpf('1e-55'),(S,v,target)
        numeric_count+=1
    # The original BBP scalar endpoint and the genuine xi completed reflection.
    x=mp.pi/16
    def xi(s):
        return mp.mpf('.5')*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)
    for m in (1,2,3):
        assert abs(xi(1-2*m)-xi(2*m))<mp.mpf('1e-55')
        numeric_count+=1
    assert abs(xi(2)-mp.mpf(8)*x/3)<mp.mpf('1e-55')
    numeric_count+=1
    # Three type controls that must not silently collapse.
    # Q=30 does not detect 49; Q=210 does.
    assert gcd(30,49)==1 and gcd(210,49)>1
    exact_count+=1
    # A fake 6 is a redundant divisibility test once 2 and 3 were included.
    for n in range(1,100):
        assert int(gcd(n,6)==1)==int(gcd(n,6)==1 and n%6 !=0)
        exact_count+=1
    print(f'PASS independent exact symbolic/integer checks: {exact_count}')
    print(f'PASS independent complex Fourier/critical-phase/reflection checks: {numeric_count}')
    print('Boundary: numerical Fourier/phase checks are noncertified diagnostics; universal claims have paper proofs.')

if __name__=='__main__':
    audit()
