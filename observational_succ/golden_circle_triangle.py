"""Exact Fibonacci/golden-circle mesh and source-faithful triangle observer.

Research-only. All gap and chronology combinatorics are integer exact in
Z[alpha] (alpha**2 + alpha == 1). Trigonometric/surrogate routines are
floating diagnostics; paper proofs give their universally valid budgets.
Source contract: original BBP r(n), U0=0. Do not treat the auxiliary
Pascal triangle as the arithmetic pi orbit.
"""
from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass
from fractions import Fraction
from functools import cmp_to_key
from math import cos, isfinite, isqrt, pi, sin


@dataclass(frozen=True)
class ZGolden:
    """a+b*alpha, alpha=(sqrt(5)-1)/2, exact integral arithmetic."""

    a: int
    b: int

    def __add__(self, other: 'ZGolden') -> 'ZGolden':
        return ZGolden(self.a+other.a, self.b+other.b)

    def __sub__(self, other: 'ZGolden') -> 'ZGolden':
        return ZGolden(self.a-other.a, self.b-other.b)

    def __mul__(self, other: 'ZGolden') -> 'ZGolden':
        return ZGolden(self.a*other.a+self.b*other.b,
                       self.a*other.b+self.b*other.a-self.b*other.b)

    def sign(self) -> int:
        """Sign from (2a-b)+b*sqrt(5), using integer squares only."""
        u,v=2*self.a-self.b,self.b
        if u==0:
            return (v>0)-(v<0)
        if v==0 or (u>0)==(v>0):
            return (u>0)-(u<0)
        d=u*u-5*v*v
        assert d!=0  # irrational sqrt(5) forbids nontrivial equality
        return (u>0)-(u<0) if d>0 else (v>0)-(v<0)

    def value(self) -> float:
        return self.a+self.b*((5**0.5-1)/2)


ZERO=ZGolden(0,0)
ONE=ZGolden(1,0)
ALPHA=ZGolden(0,1)


def fibonacci(k: int)->int:
    if type(k) is not int or k<0:
        raise ValueError('Fibonacci index must be a nonnegative integer')
    a,b=0,1
    for _ in range(k):
        a,b=b,a+b
    return a


def alpha_power(k: int)->ZGolden:
    if type(k) is not int or k<0:
        raise ValueError('power must be nonnegative integer')
    out=ONE
    for _ in range(k):
        out=out*ALPHA
    return out


def golden_phase(n:int)->ZGolden:
    """Exact {n*alpha}; no real floating-point reduction."""
    if type(n) is not int or n<0:
        raise ValueError('time index must be nonnegative integer')
    lower=(isqrt(5*n*n)-n)//2
    return ZGolden(-lower,n)


def _compare(a:tuple[ZGolden,int],b:tuple[ZGolden,int])->int:
    return (a[0]-b[0]).sign()


def ordered_orbit(k:int)->list[tuple[ZGolden,int]]:
    if type(k) is not int or k<3:
        raise ValueError('need k>=3 so F_k>=2')
    N=fibonacci(k)
    return sorted(((golden_phase(n),n) for n in range(N)), key=cmp_to_key(_compare))


def arc_gap(a:ZGolden,b:ZGolden)->ZGolden:
    """Counterclockwise circle gap from distinct points a to b."""
    t=b-a
    if t.sign()<=0:
        t=t+ONE
    assert t.sign()>0 and (ONE-t).sign()>0
    return t


def mesh_gaps(k:int)->list[tuple[int,int,ZGolden]]:
    orbit=ordered_orbit(k)
    return [(orbit[i][1],orbit[(i+1)%len(orbit)][1],
             arc_gap(orbit[i][0],orbit[(i+1)%len(orbit)][0]))
            for i in range(len(orbit))]


def insertions_and_parents(k:int)->list[tuple[int,int,int]]:
    """For N=F_k, each new n=F_k+j splits the unique long parent gap.

    Returns (old endpoint j, new time F_k+j, opposite old endpoint).
    Exact verification of the orientation-dependent parent algorithm.
    """
    if k<3:
        raise ValueError('k>=3')
    N=fibonacci(k)
    old=mesh_gaps(k)
    forward=(k%2==1)  # epsilon_k = (-1)^(k-1) alpha^k
    lookup={a if forward else b:(a,b,gap) for a,b,gap in old}
    big=alpha_power(k-2)
    result=[]
    for j in range(fibonacci(k-1)):
        a,b,gap=lookup[j]
        assert gap==big
        new=golden_phase(N+j)
        start=golden_phase(j)
        # The forward/backward alpha^k step lies strictly inside the parent.
        assert (new-start if forward else start-new).sign()!=0
        result.append((j,N+j,b if forward else a))
    return result


def golden_area_constant() ->float:
    """C=lim F_k^2*(pi R^2-polygon_area)/R^2 for unit R."""
    phi=(1+5**0.5)/2
    return (2*pi**3/(15*5**0.5))*(phi**5+phi)


def circle_mesh_nodes(k:int)->list[float]:
    return [v.value() for v,_ in ordered_orbit(k)]


def triangle_signed_weyl(points:list[float],h:int,k:int)->tuple[complex,complex,float]:
    """Circle finite-element surrogate for empirical-minus-Haar signed mode.

    (true mode, signed nodal surrogate, rigorous analytic error budget).
    The implementation uses floating sin/cos and is NOT an interval cert.
    Its universal paper bound is pi**2*h**2*max_gap**2, plus floating error.
    """
    if type(h) is not int or h==0:
        raise ValueError('require fixed nonzero integer frequency')
    if not points:
        raise ValueError('need at least one carrier phase')
    if not all(isfinite(x) and 0<=x<1 for x in points):
        raise ValueError('phases must be finite and in [0,1)')
    xs=circle_mesh_nodes(k)
    m=len(xs)
    gaps=[xs[j+1]-xs[j] for j in range(m-1)]+[1-xs[-1]+xs[0]]
    assert min(gaps)>0
    obs=[0.0]*m
    for x in points:
        j=bisect_right(xs,x)-1
        if j<0:j=m-1
        arc=(x-xs[j])%1
        t=arc/gaps[j]
        obs[j]+=(1-t)/len(points)
        obs[(j+1)%m]+=t/len(points)
    expected=[(gaps[(j-1)%m]+gaps[j])/2 for j in range(m)]
    def e(x):return complex(cos(2*pi*h*x),sin(2*pi*h*x))
    true=sum((e(x) for x in points),0j)/len(points)
    surrogate=sum(((obs[j]-expected[j])*e(xs[j]) for j in range(m)),0j)
    return true,surrogate,pi*pi*h*h*max(gaps)**2


def original_four_pole(n:int)->Fraction:
    """Independent exact oracle, not a replacement for SUCC duck_bbp."""
    if type(n) is not int or n<=0:
        raise ValueError('n must be positive integer')
    return Fraction(4,8*n-7)-Fraction(2,8*n-4)-Fraction(1,8*n-3)-Fraction(1,8*n-2)


def zero_seed_epoch(A:int)->list[Fraction]:
    """Exact lifted states U_n, A<=n<2A; for small finite checks only."""
    if type(A) is not int or A<1:
        raise ValueError('A must be a positive integer')
    u=Fraction(0)
    out=[]
    for n in range(1,2*A):
        u=16*u+original_four_pole(n)
        if n>=A:out.append(u % 1)
    return out


def source_R(a: int)->Fraction:
    """Four-pole Laplace function R(a), a>0; r(n)=R(8n-7)."""
    if type(a) is not int or a<=0:
        raise ValueError('positive integral Laplace clock required')
    return Fraction(4,a)-Fraction(2,a+3)-Fraction(1,a+4)-Fraction(1,a+5)


def pascal_source_grade_weights(a:int,m:int)->tuple[Fraction,...]:
    """Exact grade law of the declared positive Bernoulli/Gamma observer.

    Model: X~exp(-a*x) Q(x)dx/R(a), m conditionally independent
    Bernoulli trials, failure f=e^-8X, success g=1-f. This does NOT
    sample digits of pi. Every weight is exact rational and >=0.
    """
    from math import comb
    if type(m) is not int or m<0:
        raise ValueError('nonnegative integer observer depth required')
    denom=source_R(a)
    weights=[]
    for j in range(m+1):
        q=comb(m,j)*sum(((-1)**t*comb(j,t)*source_R(a+8*(m-j+t))
                          for t in range(j+1)),Fraction(0))/denom
        assert q>=0
        weights.append(q)
    assert sum(weights)==1
    return tuple(weights)


def pascal_circle_character(a:int,m:int,h:int)->complex:
    """Complex Fourier readout after grade-to-golden-circle quotient."""
    if type(h) is not int:
        raise ValueError('integral circle harmonic required')
    alpha=(5**0.5-1)/2
    w=pascal_source_grade_weights(a,m)
    return sum((float(t)*complex(cos(2*pi*h*j*alpha),sin(2*pi*h*j*alpha))
                for j,t in enumerate(w)),0j)


def triangle_lag_energy(points:list[float],h:int,k:int,H:int)->tuple[float,float,float]:
    """Exact-sign Fejer/lag Gram energy versus temporal triangle surrogate.

    An O_h(max_gap**2) approximation uniform in 1<=H<=A. Does not
    estimate either energy by o(1). Phase readouts are floating diagnostics.
    """
    if type(h) is not int or h==0 or type(H) is not int or H<1 or H>len(points):
        raise ValueError('need nonzero h and 1<=H<=number of phases')
    if not all(isfinite(x) and 0<=x<1 for x in points):
        raise ValueError('phase out of range')
    xs=circle_mesh_nodes(k)
    gs=[xs[j+1]-xs[j] for j in range(len(xs)-1)]+[1-xs[-1]+xs[0]]
    def e(x): return complex(cos(2*pi*h*x),sin(2*pi*h*x))
    z=[e(x) for x in points]
    y=[]
    for x in points:
        j=bisect_right(xs,x)-1
        if j<0:j=len(xs)-1
        t=((x-xs[j])%1)/gs[j]
        y.append((1-t)*e(xs[j])+t*e(xs[(j+1)%len(xs)]))
    def energy(a):
        accum=0.
        for t in range(-H+1,len(a)):
            s=sum((a[j] for j in range(max(0,t),min(len(a),t+H))),0j)
            accum+=abs(s)**2
        return accum/(len(a)*H**2)
    return energy(z),energy(y),pi*pi*h*h*max(gs)**2