"""Independent SymPy/mpmath oracle: no imports from seam_model.

Finite checks calibrate the source algebra, prime clocks, rank receipts,
root-of-unity Fourier alias, and the analytic tail. They do NOT prove Fabry,
Bertrand, pi normality, or global source adequacy.
"""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime,timezone
import hashlib
from fractions import Fraction
from math import isqrt
import sympy as sp
import mpmath as mp

D=Path(__file__).resolve().parent
mp.mp.dps=105


def source(j):
    return sp.Rational(4,8*j-7)-sp.Rational(2,8*j-4)-sp.Rational(1,8*j-3)-sp.Rational(1,8*j-2)


def clock(p):return (p*p+7)//8


def first_pole_mark(j,mark):
    a=8*j-7
    if a<49:return 0
    p=isqrt(a)
    return mark if p*p==a and sp.isprime(p) else 0


def gamma_q(j):
    return source(j)/sp.Integer(16)**j


def p_primary(x,p):
    x=sp.cancel(x)
    u,v=map(int,sp.fraction(x))
    pp=1
    while v%p==0:
        pp*=p
        v//=p
    return sp.Rational((u*pow(v,-1,pp))%pp,pp) if pp>1 else sp.Rational(0)


def mpc_from_rational(q):
    q=sp.Rational(q)
    return mp.mpf(int(q.p))/mp.mpf(int(q.q))


def run():
    results={}
    primes=list(sp.primerange(7,60))
    marked_count=0
    for p in primes:
        j=clock(p)
        assert 8*j-7==p*p
        assert p_primary(source(j),p)==sp.Rational(4,p*p)
        delta=sp.Rational(2,(8*j-7)*(8*j-6)*(8*j-5))
        assert p_primary(source(j)+delta,p)==sp.Rational(5,p*p)
        marked_count+=2
    results['original_mutant_primary_exact_checks']=marked_count

    determinants=[]
    for p,q in ((7,11),(11,13),(17,19),(13,17)):
        L=clock(q)-clock(p)
        t=clock(p)+1
        for mark in (1,4,5):
            H=sp.Matrix(L,L,lambda i,j:first_pole_mark(t+i+j,mark))
            predicted=(-1)**(L*(L-1)//2)*mark**L
            actual=int(H.det(method='domain-ge'))
            assert actual==predicted,(p,q,mark,actual,predicted)
            determinants.append({'p':p,'q':q,'size':L,'mark':mark,'det':str(actual)})
    results['hankel_det_oracle']=determinants

    exact_mellin=sp.integrate(4-2*sp.Symbol('t')**3-sp.Symbol('t')**4-sp.Symbol('t')**5,
                             (sp.Symbol('t'),0,1))
    assert exact_mellin==sp.Rational(47,15)
    results['mellin_r1_exact']=str(exact_mellin)
    Q=lambda t:4-2*t**3-t**4-t**5
    comparisons=[]
    for n,z in [(0,mp.mpf('0.4')),(0,mp.mpf(1)),
                (2,mp.mpc('0.3','0.4')),(7,mp.mpf(1)),
                (11,mp.mpc('-0.6','0.5'))]:
        integral=(mp.mpf(16)**(-n))*mp.quad(lambda t: t**(8*n)*Q(t)/(16-z*t**8),[0,1])
        truncated=mp.fsum(mpc_from_rational(gamma_q(n+k+1))*z**k for k in range(88))
        error=abs(integral-truncated)
        assert error<mp.mpf('1e-98'),(n,z,mp.nstr(error,15))
        comparisons.append({'n':n,'z':str(z),'absolute_error':mp.nstr(error,12)})
    results['mellin_backward_germ_numeric']=comparisons

    Fourier=[]
    for q in (3,5,7):
        omega=mp.e**(2j*mp.pi/q)
        P=[mp.fsum(mpc_from_rational(gamma_q(k))*omega**(a*k) for k in range(1,87))
           for a in range(q)]
        for j in range(1,q+1):
            estimate=mp.fsum(P[a]*omega**(-a*j) for a in range(q))/q
            exact=sum((gamma_q(k) for k in range(j,87,q)),sp.Rational(0))
            error=abs(estimate-mpc_from_rational(exact))
            assert error<mp.mpf('1e-98'),(q,j,mp.nstr(error))
            Fourier.append({'q':q,'j':j,'absolute_error':mp.nstr(error,9)})
    results['root_of_unity_DFT_inverse_numeric']=Fourier

    t=sp.symbols('t')
    H=4+4*t+4*t*t+2*t**3+t**4
    f=H/(16-t**8)
    assert f.subs(t,1)==1 and sp.diff(f,t).subs(t,1)==2
    n=sp.symbols('n',positive=True)
    k=8*n+1
    approximation=1/(k*(k+1))-4/(k*(k+1)*(k+2))
    u=sp.symbols('u')
    series=sp.series(approximation.subs(n,1/u),u,0,4)
    assert series.removeO()==u**2/sp.Integer(64)-7*u**3/sp.Integer(512)
    results['tail_asymptotic_jet']={ 'f_at_one':str(f.subs(t,1)),
         'f_prime_at_one':str(sp.diff(f,t).subs(t,1)),
         'first_terms':'1/(64n^2)-7/(512n^3)+O(n^-4)' }

    # A calibration of the quantitative prefix machine-size bound, NOT a proof.
    for N in (100, 500, 2000, 10000):
        X=isqrt(8*N-7)
        lo=X//4
        candidates=[int(p) for p in sp.primerange(lo+1,X//2+1)]
        assert candidates
        p=candidates[0]
        q=int(sp.nextprime(p))
        assert q<X
        assert clock(q)<=N
        assert clock(q)-clock(p) > (8*N-7)**0.5/8
    results['prefix_bertrand_checks']=4

    hashfiles=['seam_model.py','test_seam_model.py','independent_audit.py']
    results['sha256']={f:hashlib.sha256((D/f).read_bytes()).hexdigest() for f in hashfiles}
    results['oracle']='SymPy exact determinant/primary/Mellin jet + independent mpmath Fourier/quadrature'
    results['boundary']='Finite checks only; Fabry/Euclid/Bertrand are external or paper theorems; R0 and pi normality OPEN.'
    (D/'independent_audit_receipt.json').write_text(json.dumps(results,indent=2,sort_keys=True)+'\n')
    print('INDEPENDENT AUDIT PASS')
    print('p-primary:',marked_count,'Hankel determinants:',len(determinants),
          'analytic integrals:',len(comparisons),'DFT coefficients:',len(Fourier),
          'Bertrand finite calibrations:',4)
    print('receipt:',D/'independent_audit_receipt.json')


if __name__=='__main__':run()
