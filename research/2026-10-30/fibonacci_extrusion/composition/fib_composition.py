"""Exact source/Fibonacci composition diagnostics; no selected-phase claims."""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from math import comb, factorial, isqrt
from pathlib import Path
import importlib.util

_PARENT = Path(__file__).resolve().parents[2] / 'triangle_fabric/constants/composition.py'
_spec = importlib.util.spec_from_file_location('inherited_source_composition', _PARENT)
_parent = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_parent)
SIGMA2 = F(1379, 900)
UNIFORM_C = F(1627, 45)
SOURCE = ((0,4),(3,-2),(4,-1),(5,-1))


def fib(n):
    if n < 0: raise ValueError('nonnegative index')
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a


def r(a, derivative=0):
    a=F(a)
    if a<=0 or derivative<0:raise ValueError('positive age, nonnegative derivative')
    return sum((F(c)*(-1)**derivative*factorial(derivative)/(a+d)**(derivative+1)
                for d,c in SOURCE),F(0))


def moment(a,j):
    return (-1)**j*r(a,j)/r(a)


def variance(a):
    return moment(a,2)-moment(a,1)**2


def harmonic(n):
    return sum((F(1,i) for i in range(1,n+1)),F(0))


def iadd(x,y):return x[0]+y[0],x[1]+y[1]
def iscale(x,c):return (x[0]*c,x[1]*c) if c>=0 else (x[1]*c,x[0]*c)
def ipoint(x):return F(x),F(x)
def imul(x,y):
    vals=[a*b for a in x for b in y]
    return min(vals),max(vals)


@lru_cache(None)
def log_interval(q,terms=384):
    return _parent.ln_interval(F(q),terms)


@lru_cache(None)
def partial_fractions(k):
    return _parent.convolution_partial_fractions(k)


def harmonic_gap_interval(a,k,terms=384):
    """Inherited partial-fraction algorithm with enlarged exact log budget."""
    if k<1:raise ValueError('positive convolution rank')
    a=F(a);norm=r(a)**k;total=ipoint(0);mass=F(0)
    for d,m,c in partial_fractions(k):
        w=c/(a+d)**m/norm
        mass+=w
        term=iadd(ipoint(harmonic(m-1)),iscale(log_interval(a+d,terms),-1))
        total=iadd(total,iscale(term,w))
    assert mass==1
    one=ipoint(0)
    for d,c in SOURCE:
        one=iadd(one,iscale(log_interval(a+d,terms),-F(c)/((a+d)*r(a))))
    return iadd(iadd(total,iscale(one,-1)),ipoint(1-harmonic(2*k-1)))


def uniform_center(k):return SIGMA2*F(k-1,2*k+1)
def uniform_error(a):return UNIFORM_C/F(a)


def fresh_variance(a,n):return fib(n)*variance(a)
def reused_variance(a,n):
    if n==1:return variance(a)
    return (fib(n-2)**2+fib(n-1)**2)*variance(a)


def laplace(a,t):return r(F(a)+F(t))/r(a)
def fresh_laplace(a,t,n):return laplace(a,t)**fib(n)
def reused_laplace(a,t,n):
    if n==1:return laplace(a,t)
    return laplace(a,fib(n-2)*F(t))*laplace(a,fib(n-1)*F(t))


def reciprocal_interval(n):
    if n<1:raise ValueError('positive cutoff')
    total=sum((F(1,fib(j)) for j in range(1,n+1)),F(0))
    return total,total+F(2,fib(n+1))+F(2,fib(n+2))


# Exact Q(lambda), lambda²=1-lambda, reusing parent's declared field basis.
ga=_parent.gadd;gm=_parent.gmul;gs=_parent.gscale;gp=_parent.gpower;gi=_parent.ginv
LAMBDA=(F(0),F(1));LAMBDA2=(F(1),F(-1))

def golden_reused_moment(a,j):
    return sum_field(gs(gm(gp(LAMBDA2,i),gp(LAMBDA,j-i)),
                        F(comb(j,i))*moment(a,i)*moment(a,j-i)) for i in range(j+1))


def sum_field(items):
    out=(F(0),F(0))
    for x in items:out=ga(out,x)
    return out


def jensen_lower(a):
    m=moment(a,1)
    v=ga(golden_reused_moment(a,2),(-m*m,F(0)))
    den=gs(ga(ga(golden_reused_moment(a,4),gs(golden_reused_moment(a,2),-2*m*m)),
              (m**4,F(0))),2)
    return gm(gm(v,v),gi(den))


def golden_interval(q,bits=240):return _parent.golden_interval(q,bits)


def gamma_gap_interval(n_gamma=512,terms=384):
    """Rigorous (17), using H_n-log n-1/(2n)<gamma<H_n-log n."""
    den=2**256;k=isqrt(5*den*den)
    sqrt5=(F(k,den),F(k+1,den))
    phi=iscale(iadd(ipoint(1),sqrt5),F(1,2))
    logphi=(log_interval(phi[0],terms)[0],log_interval(phi[1],terms)[1])
    gam=iadd(ipoint(harmonic(n_gamma)),iscale(log_interval(F(n_gamma),terms),-1))
    gam=(gam[0]-F(1,2*n_gamma),gam[1])
    q=iadd(iadd(log_interval(F(2),terms),gam),iscale(iadd(ipoint(5),iscale(sqrt5,2)),-1))
    coeff=iscale(iadd(ipoint(19),iscale(sqrt5,7)),F(1,2))
    return iadd(q,imul(coeff,logphi))


def dyadic(interval,bits=160):
    return _parent.dyadic_outward(interval,bits)


def clock_defect(a,s,n):
    if n<3 or s<=0:raise ValueError('n>=3, positive clock shift')
    a,s=F(a),F(s);c,d=fib(n-2),fib(n-1)
    return (c+d)*moment(a+s,1)-c*moment(a+c*s,1)-d*moment(a+d*s,1)


def clock_defect_lower(a,s,n):
    if n<3 or s<=0:raise ValueError('n>=3, positive clock shift')
    a,s=F(a),F(s);c,d=fib(n-2),fib(n-1)
    return 2*c*(1/(a+s+5)-1/(a+c*s+5))+2*d*(1/(a+s+5)-1/(a+d*s+5))
