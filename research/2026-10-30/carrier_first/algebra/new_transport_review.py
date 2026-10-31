"""Independent rational review of the analytic and high-order frame formulas."""
from fractions import Fraction as Q
from pathlib import Path
from math import comb, factorial
import hashlib
import json
import sympy as S

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
t,x=S.symbols('t x')


def approximation(moments,d):
    h=S.Matrix(d,d,lambda i,j:moments[i+j])
    rhs=S.Matrix([-moments[d+i] for i in range(d)])
    low=list(h.inv()*rhs)
    poly=x**d+sum(low[i]*x**i for i in range(d))
    quotient=S.div(poly.subs(x,t)-poly,t-x,x)[0]
    coeff=S.Poly(quotient,x)
    q=sum(v*moments[k[0]] for k,v in coeff.terms())
    norm=sum(v*moments[k[0]] for k,v in S.Poly(poly**2,x).terms())
    return poly,q,S.factor(norm)


markov=0
# Exactly known finite measures give an independent rational-function check.
nodes=[S.Rational(1,7),S.Rational(2,5),S.Rational(5,6)]
weights=[S.Rational(3,4),S.Rational(2,9),S.Rational(7,8)]
mom=[sum(w*u**k for u,w in zip(nodes,weights)) for k in range(8)]
transform=sum(w/(t-u) for u,w in zip(nodes,weights))
for d in (1,2):
    p,q,norm=approximation(mom,d)
    right=sum(w*p.subs(x,u)**2/(t-u) for u,w in zip(nodes,weights))/p.subs(x,t)**2
    assert S.factor(transform-q/p.subs(x,t)-right)==0
    markov+=1

# Authentic rational moments and an independently unrolled BBP interval.
r=lambda n:S.Rational(4,8*n-7)-S.Rational(2,8*n-4)-S.Rational(1,8*n-3)-S.Rational(1,8*n-2)
J=80
alpha_lo=sum(r(j)/16**j for j in range(1,J+1))
alpha_hi=alpha_lo+r(J+1)/(15*16**J)
pade=[]
for d in (2,4,6):
    mom=[r(k+1) for k in range(2*d+1)]
    p,q,norm=approximation(mom,d)
    p16=p.subs(x,16)
    lower=q.subs(t,16)/p16+norm/(16*p16*p16)
    upper=q.subs(t,16)/p16+norm/(15*p16*p16)
    assert lower<alpha_lo<alpha_hi<upper
    assert alpha_hi-q.subs(t,16)/p16<S.Rational(188,225)/3600**d
    # The Gaussian next-moment defect is exactly the orthogonal norm.
    coefficients=[p.coeff(x,i) for i in range(d)]
    fake=list(mom[:d])
    for k in range(d,2*d+1):
        fake.append(-sum(coefficients[i]*fake[k-d+i] for i in range(d)))
    assert fake[:2*d]==mom[:2*d]
    assert mom[2*d]-fake[2*d]==norm>0
    pade.append(d)

germ=0
for K in range(1,13):
    epsilon=Q(1,2*4**(K+1)*2**K)
    for j in range(K+1):
        mass=Q(1,4**(j+1))+epsilon*(-1)**j*comb(K,j)
        assert mass>0
    for power in range(K+1):
        value=sum((-1)**j*comb(K,j)*(j+1)**power for j in range(K+1))
        assert value==(0 if power<K else (-1)**K*factorial(K))
        germ+=1

stencils=0
for m in range(1,13):
    h=Q(1,2*m)
    weights=[Q(2*m*(-1)**(j+1)*factorial(m)**2,
               j*factorial(m-j)*factorial(m+j)) for j in range(1,m+1)]
    for degree in range(2*m+2):
        got=sum(w*((j*h)**degree-(-j*h)**degree) for j,w in enumerate(weights,1))
        true=Q(degree==1)
        if degree<=2*m:assert got==true
        else:assert true-got==(-1)**m*h**(2*m)*factorial(m)**2
        stencils+=1

paths=['analytic/ANALYTIC_TRANSPORT.md','selected/HIGH_ORDER_FRAMES.md','OBSERVER_THEOREMS.md','observer.py']
print(json.dumps({'status':'PASS','rational_markov_function_identities':markov,
    'authentic_Pade_degrees':pade,'prime_germ_exact_moment_cases':germ,
    'Hermite_stencil_monomials':stencils,
    'reviewed_inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
    'authority':'separate derivation/code, same model lineage; paper proofs not inferred from probes'},indent=2))
