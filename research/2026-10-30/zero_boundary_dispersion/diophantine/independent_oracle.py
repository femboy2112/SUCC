"""Separate direct-prefix, digit-sum and Machin route; imports no probe code."""
from fractions import Fraction as F
from pathlib import Path
from json import loads,dumps
import sympy as sp


def direct(n):
    return sum((16**(n-j)*(F(4,8*j-7)-F(2,8*j-4)-F(1,8*j-3)-F(1,8*j-2))
                for j in range(1,n+1)),F(0))


def norm(x):
    return abs(x-round(x))


def atan_remainder(q,k):
    val=sum((F((-1)**i,(2*i+1)*q**(2*i+1)) for i in range(k)),F(0))
    other=val+F((-1)**k,(2*k+1)*q**(2*k+1))
    return min(val,other),max(val,other)


def beta_bounds(m,cutoff):
    powers=[];v=1
    while v<=cutoff:
        powers.append(v);v*=m
    val=sum((F(1,16**d) for d in powers),F(0))
    return val,val+F(16,15*16**v),powers,v


def run():
    a,d=sp.symbols('a d',positive=True)
    derivative=sp.diff(1/(a*(a+d)),a)
    assert sp.cancel(2/a**3+derivative-d*(3*a+2*d)/(a**3*(a+d)**2))==0
    source=4/a-2/(a+3)-1/(a+4)-1/(a+5)
    assert sp.cancel(source-6/(a*(a+3))-4/(a*(a+4))-5/(a*(a+5)))==0
    prior=loads((Path(__file__).parent/'receipts/probes.log').read_text())
    witnesses=[]
    for row in prior['authentic_windows']:
        n=row['first_slip'];h=row['h'];ell=row['ell']
        value=norm(h*(direct(n+ell)-direct(n)))
        assert value>=F(1,20)
        witnesses.append(dict(A=row['A'],h=h,ell=ell,n=n,exact_distance=str(value)))
    lo5,hi5=atan_remainder(5,220);lo239,hi239=atan_remainder(239,66)
    pl=16*lo5-4*hi239;ph=16*hi5-4*lo239
    green=[]
    for n in (11,23,47,83):
        lag=direct(n+1)-direct(n)
        dl=lag-15*16**(n-1)*ph
        dh=lag-15*16**(n-1)*pl
        assert 0<dl<dh<F(16,(8*n+1)**3)
        green.append(dict(n=n,positive=True,cubic_bound=True))
    separation=[]
    for m in (3,4,5):
        for q in (16**(m-1)//4,16**(m-1)//4+1,16**m,16**m+101):
            bl,bh,_,_=beta_bounds(m,1000)
            p=(bl*q).numerator//(bl*q).denominator
            for numerator in (p,p+1):
                x=F(numerator,q)
                gap=min(abs(bl-x),abs(bh-x)) if x<bl or x>bh else F(0)
                assert gap>=F(1,16*q**m),(m,numerator,q)
                separation.append(dict(m=m,q=q,side=numerator-p,lower_bound=True))
    budgets=[]
    for m in (3,4,5):
        for N in (83,257,733):
            bl,bh,powers,nxt=beta_bounds(m,N+20)
            # Direct per-time digit convolution, plus the infinite remainder.
            total=sum((sum((F(1,16**(d-n+1)) for d in powers if d>=n),F(0))
                       for n in range(1,N+1)),F(0))
            upper=total+(bh-bl)*F(16**N-1,15)
            J=sum(d<=N for d in powers)
            bound=F(J,15)+F(1,225)
            assert upper<bound,(m,N)
            budgets.append(dict(m=m,N=N,J=J,upper_below_analytic_bound=True))
    return dict(sympy_version=sp.__version__,symbolic_identities=2,
                direct_prefix_witnesses=witnesses,machin_green_checks=green,
                rational_separation_checks=separation,digit_budget_checks=budgets,
                independent_of_probe_imports=True,
                authority='finite exact checks, not universal or external proof')

if __name__=='__main__':print(dumps(run(),indent=2))
