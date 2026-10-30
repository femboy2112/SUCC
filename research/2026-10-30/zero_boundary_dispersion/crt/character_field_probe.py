"""Exact extension-degree and annihilator-polynomial certificates."""
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
import json
import sys
import sympy as S
from crt_probe import orbit,primary,birth


def factor_small(n,bound):
    factors={}
    for p in range(2,bound+1):
        if n%p==0:
            a=0
            while n%p==0:n//=p;a+=1
            factors[p]=a
    assert n==1,(n,bound)
    return factors


def exact_order(a,D,factors):
    if D==1:return 1,[]
    order=1;components=[]
    for q,e in factors.items():
        Q=q**e;phi=(q-1)*q**(e-1)
        phi_factors=factor_small(phi,Q)
        o=phi
        for ell in phi_factors:
            while o%ell==0 and pow(a,o//ell,Q)==1:o//=ell
        assert pow(a,o,Q)==1
        components.append({'prime':q,'exponent':e,'order':o})
        order=lcm(order,o)
    assert pow(a,order,D)==1
    # Every prime divisor of order occurs among q or q-1 in the components.
    primes=set()
    for q,e in factors.items():
        primes.update(factor_small((q-1)*q**(e-1),q**e))
    for ell in primes:
        if order%ell==0:assert pow(a,order//ell,D)!=1
    return order,components


def run():
    sys.set_int_max_str_digits(0)
    u=orbit(600)
    field=[]
    for p,n in ((13,2),(19,5),(73,10),(1033,130),(1061,133)):
        co=u[n]-primary(u[n],p)
        D=co.denominator
        assert D%2 and gcd(D,p)==1
        fac=factor_small(D,8*n)
        f,components=exact_order(p,D,fac)
        assert pow(p,f,D)==1
        field.append({'p':p,'n':n,'cofiber_denominator':str(D),'denominator_bits':D.bit_length(),
            'minimal_extension_degree':str(f),'extension_degree_bits':f.bit_length(),
            'components':components,'f1_and_f2_fail':all(pow(p,k,D)!=1 for k in (1,2)),
            'scope':'exact ordinary finite-field character field; not approximate or arbitrary coefficient-field transport'})
    X=S.symbols('n')
    P=lambda t:120*t*t-89*t+16
    D=lambda t:(2*t-1)*(4*t-1)*(8*t-7)*(8*t-3)
    ann=[]
    for q in ([1],[1,1],[1,-1],[1,0,1]):
        support=[j for j,c in enumerate(q) if c]
        denominator=S.Poly(S.prod(D(X+j+1) for j in support),X)
        numerator=S.Poly(sum(q[j]*P(X+j+1)*S.prod(D(X+k+1) for k in support if k!=j) for j in support),X)
        resultant=int(S.resultant(numerator,denominator,X))
        assert resultant!=0
        rows=[]
        for n in (17,43,101,233,509):
            N=int(numerator.eval(n));den=int(denominator.eval(n));g=gcd(N,den)
            assert resultant%g==0
            y=sum((q[j]*(u[n+j+1]-16*u[n+j]) for j in range(len(q))),F())
            assert y.denominator==den//g
            rows.append({'n':n,'evaluation_gcd':str(g),'denominator_bits':y.denominator.bit_length()})
        ann.append({'quotient_coefficients':q,'support_count':len(support),'denominator_degree':denominator.degree(),
            'numerator_coefficients':[str(z) for z in numerator.all_coeffs()],
            'denominator_coefficients':[str(z) for z in denominator.all_coeffs()],
            'resultant':str(resultant),'rows':rows})
    print(json.dumps({'character_field':field,'annihilator_resultants':ann,
        'authority':'exact finite certificates; asymptotic proofs in CRT_DOSSIER.md'},indent=2))

if __name__=='__main__':run()
