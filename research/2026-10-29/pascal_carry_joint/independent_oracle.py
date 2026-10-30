"""Independent SymPy/mpmath oracle for exact Green/Pascal/BBP source gluing.

No imports from joint_carry_probe or SUCC production code. This is NOT a blind
second implementation or full native SUCC validation. Exact algebra and
high-precision conditional-integral holds are separate checks.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb
import sympy as sp
import mpmath as mp


def source(n):
    a=8*n
    return F(4,a-7)-F(2,a-4)-F(1,a-3)-F(1,a-2)


def direct_q(n,j):
    total=F(0)
    for i in range(j+1):
        total+=F((-1)**i*comb(j,i)*comb(n,j))*source(2*n-j+i)/source(n)
    return total


def direct_composite(n,D):
    # Independent positive mixture of original four-pole r and finite binomial
    green=[F(1,16**ell)*source(n+ell) for ell in range(1,D+1)]
    green=[g/sum(green) for g in green]
    out={}
    for ell,pl in enumerate(green,1):
        t=n+ell
        for j in range(t+1):
            r=ell+j
            out[r]=out.get(r,F(0))+pl*direct_q(t,j)
    return out


def main():
    z=sp.symbols('z')
    k=15*z/((16-z)*(2-z)**2)
    expected=(16-z)*(2-z)**2
    assert sp.expand(expected)==64-68*z+20*z*z-z**3
    assert sp.simplify(expected*k-15*z)==0
    assert sp.simplify(k.subs(z,1))==1
    seq={i:sp.Rational(0) for i in range(-3,1)}
    for j in range(1,26):
        seq[j]=(68*seq[j-1]-20*seq[j-2]+seq[j-3]+(15 if j==1 else 0))/64
        compact=sp.Rational(15,196)*(sp.Rational(1,16**j)+sp.Rational(7*j-1,2**j))
        assert seq[j] == compact
    for n in range(0,4):
        for D in (1,3,5):
            C=direct_composite(n,D)
            assert sum(C.values(),F(0))==1
            assert min(C.values())>0
            print('RATIONAL_COMPOSITE',n,D,'rows',len(C),'lag1',C.get(1,F(0)))
    print('RATIONAL_POLYNOMIAL_AND_COMPOSITION PASS')

    # Independent geometric-derivative identities, avoiding slow generic summation.
    def S0(x):return x/(1-x)
    def S1(x):return x/(1-x)**2
    def S2(x):return x*(1+x)/(1-x)**3
    c=sp.Rational(15,196)
    norm=c*(S0(sp.Rational(1,16))+7*S1(sp.Rational(1,2))-S0(sp.Rational(1,2)))
    avg=c*(S1(sp.Rational(1,16))+7*S2(sp.Rational(1,2))-S1(sp.Rational(1,2)))
    variance=c*c*(S0(sp.Rational(1,256))+2*(7*S1(sp.Rational(1,32))-S0(sp.Rational(1,32)))+
                  49*S2(sp.Rational(1,4))-14*S1(sp.Rational(1,4))+S0(sp.Rational(1,4)))
    assert sp.simplify(norm)==1 and sp.simplify(avg)==sp.Rational(46,15)
    assert sp.simplify(variance)==sp.Rational(8845,49011)
    print('COMPOSITE_NORM',norm,'MEAN',avg,'HAAR_0_LAG',variance,flush=True)
    for lag in range(0,12):
        x16=sp.Rational(1,16)**lag
        x2=sp.Rational(1,2)**lag
        direct=c*c*(x16*(S0(sp.Rational(1,256))+7*S1(sp.Rational(1,32))-S0(sp.Rational(1,32)))
                    +x2*((7*lag-1)*S0(sp.Rational(1,32))+7*S1(sp.Rational(1,32))
                         +(49*S2(sp.Rational(1,4))-14*S1(sp.Rational(1,4))+S0(sp.Rational(1,4)))
                         +7*lag*(7*S1(sp.Rational(1,4))-S0(sp.Rational(1,4)))))
        closed=sp.Rational(225,196**2)*(
            sp.Rational(1,16**lag)*(sp.Rational(1,255)+sp.Rational(193,961))
           +sp.Rational(1,2**lag)*(sp.Rational(821,27)-sp.Rational(1,31)+sp.Rational(224,961)
                                    +lag*(sp.Rational(175,9)+sp.Rational(7,31))))
        assert sp.simplify(direct-closed)==0
    print('COMPOSITE_HAAR_CORRELATION PASS lags0..11',flush=True)

    mp.mp.dps=65
    for n,j in [(2,0),(2,2),(3,1),(4,3)]:
        a=8*n-7
        def Q(x):return 4-2*mp.exp(-3*x)-mp.exp(-4*x)-mp.exp(-5*x)
        def g(x):return mp.binomial(n,j)*(1-mp.exp(-8*x))**j*mp.exp(-8*(n-j)*x)
        integral=mp.quad(lambda x:mp.exp(-a*x)*Q(x)*g(x),[0,1,3,10,mp.inf])
        exact=direct_q(n,j)
        delta=abs(integral/mp.mpf(source(n).numerator)*source(n).denominator-
                  mp.mpf(exact.numerator)/exact.denominator)
        print('INDEPENDENT_MELLIN_BINOMIAL',n,j,'residual',mp.nstr(delta,5))
        assert delta<mp.mpf('1e-56')
    print('INDEPENDENT_SOURCE_INTEGRALS PASS')

    for theta in (mp.mpf('0.2'),mp.mpf('1.1'),mp.mpf('2.7')):
        v=mp.exp(1j*theta)
        left=15*v/((16-v)*(2-v)**2)
        right=mp.fsum([mp.mpf(15)/196*(mp.power(16,-j)+(7*j-1)*mp.power(2,-j))*v**j
                       for j in range(1,140)])
        assert abs(left-right)<mp.mpf('1e-30')
        spec=abs(left)**2
        target=225/((257-32*mp.cos(theta))*(5-4*mp.cos(theta))**2)
        assert abs(spec-target)<mp.mpf('1e-57')
    print('INDEPENDENT_COMPLEX_SPECTRAL_ORACLE PASS')

if __name__=='__main__':main()
