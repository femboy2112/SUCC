"""Exact arithmetic probes for the Fibonacci/radix arrow distinction.

Finite witnesses accompany paper proofs. No pi-normality premise is imported.
"""
from fractions import Fraction as Q
from math import gcd, isqrt


def fibonacci(n):
    if n < 0:
        raise ValueError('nonnegative index')
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def forcing(n, coefficients=(4,-2,-1,-1)):
    if n<1: raise ValueError('n >= 1')
    return sum((Q(c,8*n-d) for c,d in zip(coefficients,(7,4,3,2))),Q())


def states(n,seed=Q(),coefficients=(4,-2,-1,-1)):
    u=[Q(seed)]
    for j in range(1,n+1): u.append(16*u[-1]+forcing(j,coefficients))
    return u


def residue(q,p):
    q=Q(q)
    if q.denominator%p==0: raise ValueError('not p-integral')
    return q.numerator*pow(q.denominator,-1,p)%p


def intertwiners(m):
    if m<1: raise ValueError('positive modulus')
    d=gcd(m,239)
    return [(16*t%m,t) for t in range(0,m,m//d)]


def intertwines(row,m):
    x,y=row
    return ((x+y-16*x)%m,(x-16*y)%m)==(0,0)


def hensel_roots(levels):
    """Unique x²-x-1 root congruent16 mod239; not a change of native clock."""
    p=239
    x=16
    modulus=p
    out=[(modulus,x)]
    for _ in range(1,levels):
        value=x*x-x-1
        assert value%modulus==0
        digit=-(value//modulus)*pow(2*x-1,-1,p)%p
        x+=modulus*digit
        modulus*=p
        assert (x*x-x-1)%modulus==0
        out.append((modulus,x))
    return out


def scalar_order(x,p):
    v=1
    for j in range(1,p):
        v=v*x%p
        if v==1:return j
    raise ValueError('not a unit of a prime field')


def matrix_mul(a,b,m):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))%m
                       for j in range(2)) for i in range(2))


def matrix_order(m):
    ident=((1,0),(0,1))
    mat=((1,1),(1,0)); v=ident
    for j in range(1,2*m*m+1):
        v=matrix_mul(v,mat,m)
        if v==ident:return j
    raise ValueError('order search limit')


def zeckendorf(n):
    """Greedy lengths using F2=1,F3=2, descending, no duplicate F1."""
    if n<0: raise ValueError('nonnegative horizon')
    vals=[1,2]
    while vals[-1]<=n: vals.append(sum(vals[-2:]))
    out=[]
    for v in reversed(vals):
        if v<=n:
            out.append(v); n-=v
    return out


def sqrt_bounds(n,scale=10**12):
    q=isqrt(n*scale*scale)
    lo=Q(q,scale)
    hi=lo if q*q==n*scale*scale else Q(q+1,scale)
    return lo,hi


def zeckendorf_sqrt_certificate(n):
    """Use coarse exact factor4 > 1/(1-1/sqrt2), never float certification."""
    blocks=zeckendorf(n)
    upper=sum((sqrt_bounds(j)[1] for j in blocks),Q())
    lower=sqrt_bounds(n)[0]
    return upper <= 4*lower


def snapshot_positions(horizon):
    """0-based digit positions F_k,...,F_k+k²-1, k>=2, below horizon."""
    positions=set()
    k=2
    while fibonacci(k)<horizon:
        positions.update(range(fibonacci(k), min(horizon,fibonacci(k)+k*k)))
        k+=1
    return positions


def overwrite_snapshots(digits):
    out=list(digits)
    positions=snapshot_positions(len(out))
    for i in positions: out[i]=0
    return out,positions


def word_counts(digits,width):
    counts={}
    for i in range(len(digits)-width+1):
        word=tuple(digits[i:i+width]); counts[word]=counts.get(word,0)+1
    return counts


def distance(q):
    q=Q(q); f=q-q.numerator//q.denominator
    return min(f,1-f)


def lambda_interval(decimal_places=50):
    scale=10**decimal_places
    a=isqrt(5*scale*scale)
    return Q(a-scale,2*scale), Q(a+1-scale,2*scale)


def golden_lag_intervals(k,decimal_places=100):
    lo,hi=lambda_interval(decimal_places)
    fk=fibonacci(k); prev=fibonacci(k-1)
    a,b=fk*lo-prev,fk*hi-prev
    if k%2==0:a,b=-b,-a
    return a,b
