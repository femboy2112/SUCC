"""NUMERICAL ONLY. Independent direct Weil explicit-formula scout on sine tests.

No zero coordinates; not a spectral enclosure or all-function-space proof.
Source: Suzuki arXiv:2606.09096v3 eq (1.0) Weil functional.
"""
from __future__ import annotations
import json, math
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from observational_succ.suzuki_prime_boundary import prime_power


def simpson(f,a,b,steps=8192):
    """NO ERROR CERTIFICATE; float sampling for reconnaissance only."""
    h=(b-a)/steps
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*k-1)*h) for k in range(1,steps//2+1))
                +2*sum(f(a+2*k*h) for k in range(1,steps//2)))


def source_prime_jets(a:float):
    from math import log,sqrt,exp
    upper=math.exp(2*a)
    jets=[]
    for n in range(2,int(math.floor(upper))+1):
        pp=prime_power(n)
        if pp is None:continue
        prime,k=pp
        ell=math.log(n)
        if ell<2*a:
            jets.append((n,ell,math.log(prime)/math.sqrt(n)))
    return jets


def sine_result(a:float,j:int):
    """H0^1 Dirichlet sine v_j(x)=sin(j*pi*(x+a)/(2a)); ||v||²=a."""
    k=j*math.pi/(2*a)
    ell=2*a
    def f(t):
        return ((2*a-t)*math.cos(k*t)+math.sin(k*t)/k)/2
    f0=a
    def boundary(t):
        if abs(t)<1.e-6:
            # (f(t)e^(t/2)-f(0))/sinh(t) -> a/2.
            # evaluate with a linear correction negligible under scipy quad.
            return a/2
        return (f(t)*math.exp(t/2)-a)/math.sinh(t)
    jets=source_prime_jets(a)
    q_pole=simpson(lambda t:4*f(t)*math.cosh(t/2),0,ell)
    q_prime=-2*sum(c*f(d) for n,d,c in jets)
    q_const=-(math.log(4*math.pi)+0.5772156649015329)*f0
    q_gamma=-simpson(boundary,0,ell)
    q_tail=2*f0*math.atanh(math.exp(-ell))
    q=q_pole+q_prime+q_const+q_gamma+q_tail
    return dict(a=a,j=j,rayleigh=q/a, Q_W=q, prime_q=q_prime,prime_jets=[n for n,d,c in jets],
                qualified=False,zero_locations_read=False,RH_proved=False,
                algorithm='stdlib Simpson quadrature of Weil explicit formula; NO certified error')


def receipt():
    vals=[1/12, 1/4, math.log(2)/2, 3*math.log(2)/5, .45, .5]
    return {'date':'2026-10-13', 'evidence':'NUMERICAL_SCOUT_NOT_A_CERTIFICATE',
            'source_formula':'Suzuki arXiv:2606.09096v3 Weil functional',
            'results':[sine_result(a,j) for a in vals for j in (1,2,3,4,6)],
            'no_nontrivial_zero_inputs':True,'all_function_space_positivity_certified':False,'RH_proved':False}

if __name__=='__main__':
    print(json.dumps(receipt(),indent=2,sort_keys=True))
