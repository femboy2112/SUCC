"""Source-attested prime-window arithmetic (research only; no normality claim)."""
from __future__ import annotations
import cmath
import math
from fractions import Fraction as F


def source(n: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError('source index must be positive integer')
    return F(4, 8*n-7)-F(2, 8*n-4)-F(1, 8*n-3)-F(1, 8*n-2)


def combined_source(n: int) -> F:
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def edge(n: int, m: int) -> F:
    if m not in (3,4,5) or n < 1:
        raise ValueError('edge m in 3,4,5; n positive')
    a=8*n-7
    return F(1,a)-F(1,a+m)


def states_through(N: int) -> list[F]:
    if type(N) is not int or N < 0: raise ValueError('N nonnegative integer')
    states=[F(0)]
    for n in range(1,N+1): states.append(16*states[-1]+source(n))
    return states


def prime(p: int) -> bool:
    if type(p) is not int or p < 2: return False
    if p%2 == 0: return p == 2
    return all(p%d for d in range(3, math.isqrt(p)+1, 2))


def primes5(X: int) -> list[int]:
    return [p for p in range(13, X+1, 8) if prime(p)]


def window(p: int) -> tuple[int,int,int]:
    if p<=5 or p%8!=5 or not prime(p): raise ValueError('p>5 prime p=5 mod8 required')
    k=(p-5)//8
    return k+1,4*k+2,3*k+2


def order16(p: int) -> int:
    if not prime(p) or p<=5 or p%8!=5: raise ValueError('p>5 prime p=5 mod8')
    x=16%p
    d=1
    while x!=1:
        x=(16*x)%p;d+=1
    assert (p-1)%(4*d)==0
    return d


def period_split(p: int) -> tuple[int,int,int,int]:
    d=order16(p)
    t=(p-1)//(4*d)
    assert t%2 == 1
    full=(3*t-1)//2
    remainder=(d+1)//2
    assert full*d+remainder==window(p)[2]
    return d,t,full,remainder


def phase(u:F,h:int=1) -> complex:
    """Exact rational modulo 1 before floating trig; numerical diagnostic only."""
    q=(h*u)%1
    return cmath.exp(2j*math.pi*float(q))


def original_window(p:int, states:list[F],h:int=1)->complex:
    a,b,L=window(p)
    if b>=len(states): raise ValueError('not enough source states')
    return sum(phase(states[n],h) for n in range(a,b+1))


def split_window(p:int, states:list[F],h:int=1)->tuple[complex,complex,complex]:
    a,b,L=window(p)
    if b>=len(states):raise ValueError('not enough source states')
    primary=cofactor=joint=0j
    for n in range(a,b+1):
        q=F(pow(16,n-a,p),p)
        v=states[n]+F(16**(n-a),p) # exact v_p-integral, no rational phase rounding
        assert (v.denominator%p)!=0
        prim=phase(-q,h)
        cof=phase(v,h)
        primary+=prim;cofactor+=cof;joint+=prim*cof
    return primary,cofactor,joint


def kernel(X:int,n:int,m:int)->int:
    if n<1 or m<1: raise ValueError('n,m positive')
    upper=min(X,8*min(n,m)-3)
    lower=2*max(n,m)
    return sum(p>lower and p<=upper for p in primes5(upper))


def energy_direct(X:int,z:list[complex])->float:
    return sum(abs(sum(z[n] for n in range(window(p)[0],window(p)[1]+1)))**2
               for p in primes5(X))


def energy_kernel(X:int,z:list[complex])->complex:
    N=(X-1)//2
    return sum(kernel(X,n,m)*z[n]*z[m].conjugate()
               for n in range(1,N+1) for m in range(1,N+1))
