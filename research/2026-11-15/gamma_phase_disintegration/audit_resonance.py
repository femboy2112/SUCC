#!/usr/bin/env python3
"""Independent Gamma residual resonance audit: no SUCC module imports.
Finite diagnostics do not prove asymptotic limits. Universal proofs are in
RESONANCE_THEOREMS.md. Classical mpmath approximations are not intervals.
"""
from fractions import Fraction as F
from math import comb
import json
import mpmath as mp

mp.mp.dps = 70
DEPTH = 48
PAIRS = ((3,2),(4,1),(5,1))


def moment(order):
    # K geometric on nonnegative integers, ratio 1/16.
    q=F(1,16)
    gm=[F(1)]
    for r in range(1,order+1):
        gm.append(q/(1-q)*sum((comb(r,l)*gm[l] for l in range(r)),F()))
    vm=[sum((F(v*((1+d)**(r+1)-1),15*(r+1))
                    for d,v in PAIRS),F()) for r in range(order+1)]
    return sum((comb(order,r)*8**r*gm[r]*vm[order-r]
                    for r in range(order+1)),F())


def residual(n,k,detuning,tilt=True):
    a=mp.mpf(8*n)
    c=2*mp.pi*k
    omega=a*c+detuning
    exponent=(-1 if tilt else 1)-1j*omega
    numerator=mp.mpc(0)
    denominator=mp.mpf(0)
    for j in range(1,DEPTH+1):
        start=8*j-7
        for length,v in PAIRS:
            left=1+mp.mpf(start)/a
            right=1+mp.mpf(start+length)/a
            weight=mp.mpf(v)/(16**j)
            numerator+=weight*a*(right**exponent-left**exponent)/exponent
            denominator+=(weight*a*(1/left-1/right) if tilt else weight*length)
    return numerator/denominator


def complex_output(z):
    return {'real':mp.nstr(z.real,18),'imag':mp.nstr(z.imag,18)}


def main():
    moments=[moment(j) for j in range(5)]
    assert moments==[F(1),F(7,2),F(55,3),F(595,4),F(8551,5)]
    # Four-pole regrouping, independent exact rational implementation.
    exact_checks=0
    for n in (0,1,2,7,31,97,257):
        for j in (1,2,4,13,37):
            a=8*n+8*j-7
            original=F(4,a)-F(2,a+3)-F(1,a+4)-F(1,a+5)
            positive=sum((F(v,a)-F(v,a+d) for d,v in PAIRS),F())
            assert original==positive
            exact_checks+=1
    rows=[]
    diagnostic_checks=0
    for k in (1,2,5):
        c=2*mp.pi*k
        for offset in (-1,0,1):
            detuning=mp.mpf(7)/2*c+offset
            expected=offset/c-1j/c
            previous=None
            for n in (4,16,64,256,1024,16384,262144):
                a=8*n
                value=a*residual(n,k,detuning)
                error=abs(value-expected)
                D=abs(detuning)
                m1,m2,m3,m4=[mp.mpf(q.numerator)/q.denominator for q in moments[1:]]
                C=(3+5*D/2+D*D/2)*m2+abs(c)*(mp.mpf(4)/3+D/2)*m3+c*c*m4/8
                bound=(1+m1/a)**2*(C+2*m1*abs(expected))/a
                assert error<=bound
                diagnostic_checks+=1
                if n==262144:
                    assert error<mp.mpf('0.001')
                    diagnostic_checks+=1
                previous=error
                rows.append({'n':n,'k':k,'offset':offset,
                             'a_residual':complex_output(value),
                             'predicted_limit':complex_output(expected),
                             'error':mp.nstr(error,12)})
    # Calibration: removing tilt flips the surviving imaginary first-order term.
    k=1;n=262144;c=2*mp.pi;d=mp.mpf(7)/2*c
    authentic=8*n*residual(n,k,d,True)
    mutant=8*n*residual(n,k,d,False)
    assert authentic.imag<0<mutant.imag
    assert abs(authentic+1j/c)<mp.mpf('0.001')
    assert abs(mutant-1j/c)<mp.mpf('0.001')
    diagnostic_checks+=3
    # Algebraic factorization of the lattice K polynomial, exact integers.
    p=[2,0,1];q=[2,2,1]
    product=[sum(p[i]*q[r-i] for i in range(3) if 0<=r-i<3) for r in range(5)]
    assert product==[4,4,4,2,1]
    exact_checks+=1
    print(json.dumps({'status':'FINITE_DIAGNOSTICS_NOT_PROOF',
        'mpmath_decimal_digits':mp.mp.dps,'interval_depth':DEPTH,
        'exact_checks':exact_checks,'diagnostic_checks':diagnostic_checks,
        'moments':[str(x) for x in moments],
        'omitted_mu_mass':str(F(1,16**DEPTH)),
        'rows':rows,'tilt_control':{'authentic':complex_output(authentic),
             'no_tilt_mutant':complex_output(mutant)}},indent=2))

if __name__=='__main__':main()
