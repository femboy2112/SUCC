"""Exact positive BBP finite-prefix/jet controls. No normality decision oracle."""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and not a[-1]:
        a.pop()
    return tuple(a)


def add(a, b):
    return trim([(a[k] if k < len(a) else 0) + (b[k] if k < len(b) else 0)
                 for k in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([Q(c) * x for x in a])


def mul(a, b):
    v = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            v[i+j] += x*y
    return trim(v)


def evaluate(a, z):
    v = Q(0)
    for x in reversed(a):
        v = v*z + x
    return v


def derivative(a, k=1):
    for _ in range(k):
        a = tuple(i*a[i] for i in range(1, len(a))) or (Q(0),)
    return a


@lru_cache(None)
def force(n):
    if n < 1:
        raise ValueError('source index >=1 required')
    return Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2)


@lru_cache(None)
def moment(k, m):
    return sum(((-1)**j*comb(m,j)*force(k+j+1) for j in range(m+1)), Q(0))


def solve(a, b):
    """Fraction Gauss-Jordan, not symbolic/numerical matrix routines."""
    n = len(b)
    rows = [list(a[i])+[b[i]] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k,n) if rows[i][k])
        rows[k], rows[pivot] = rows[pivot], rows[k]
        p = rows[k][k]
        rows[k] = [x/p for x in rows[k]]
        for i in range(n):
            if i != k:
                p = rows[i][k]
                rows[i] = [x-p*y for x,y in zip(rows[i],rows[k])]
    return tuple(row[-1] for row in rows)


@lru_cache(None)
def orthogonal(n, m):
    if n < 0 or m < 1:
        raise ValueError('N>=0,M>=1 required')
    return solve([[moment(i+j,m) for j in range(n)] for i in range(n)],
                 [-moment(i+n,m) for i in range(n)]) + (Q(1),)


@lru_cache(None)
def matched_filter(n,m):
    p = orthogonal(n,m)
    zm1 = tuple(Q(comb(m,j)*(-1)**(m-j)) for j in range(m+1))
    return add((Q(1),),scale(mul(zm1,p), -Q(1,15**m)/evaluate(p,16)))


def apply_filter(f,n):
    return sum((c*force(n+j) for j,c in enumerate(f)),Q(0))


def quotient(f):
    """Return F(16), B where F(z)=F(16)+(16-z)B(z)."""
    a = evaluate(f,16)
    g = list(add(f,(-a,)))
    if len(g)==1:
        return a,(Q(0),)
    b = [Q(0)]*(len(g)-1)
    for j in range(len(g)-1,0,-1):
        b[j-1] = -g[j]
        g[j-1] -= 16*b[j-1]
    assert g[0]==0
    return a,trim(b)


def tail_from_filter(f,n):
    a,b = quotient(f)
    if a:
        raise ValueError('rational tail requires F(16)=0')
    return apply_filter(b,n+1)


def boundary(f):
    a,b = quotient(f)
    return a,16*apply_filter(b,1)


def orbit(f,length):
    u = Q(0)
    result = [u]
    for n in range(1,length+1):
        u = 16*u+apply_filter(f,n)
        result.append(u)
    return result


def dyadic_between(lo,hi):
    assert lo < hi
    k = 0
    while True:
        numerator = (lo*(2**k)).numerator//(lo*(2**k)).denominator+1
        d = Q(numerator,2**k)
        if d < hi:
            return d,k
        k += 1


def dyadic_filter(n,even_m):
    if even_m%2 or even_m<2:
        raise ValueError('positive even M required')
    f_lo = matched_filter(n,even_m)
    f_hi = matched_filter(n,even_m+1)
    a,lo = boundary(f_lo)
    b,hi = boundary(f_hi)
    assert a==b==0 and lo<hi
    d,k = dyadic_between(lo,hi)
    theta = (d-lo)/(hi-lo)
    f = add(scale(f_lo,1-theta),scale(f_hi,theta))
    assert boundary(f)==(0,d)
    return f,dict(N=n,M=even_m,dyadic=d,denominator_power=k,theta=theta,lo=lo,hi=hi)


def bbp_pi_interval(terms):
    partial = sum((Q(16,16**n)*force(n) for n in range(1,terms+1)),Q(0))
    tail = Q(16,15*16**terms)*force(terms+1)
    return partial,partial+tail


def square_norm(p,m):
    return sum((x*y*moment(i+j,m) for i,x in enumerate(p) for j,y in enumerate(p)),Q(0))


def sign_error_bounds(n,m):
    """Positive magnitude |pi-alpha| between exact norm-based bounds."""
    p=orthogonal(n,m)
    norm=square_norm(p,m)
    base=norm/(15**m*evaluate(p,16)**2)
    return base,Q(16,15)*base


def pole_jet(f,k):
    """Q_f(x)=Q(x)F(exp(-8x)): exact kth derivative at x=0."""
    poles=((0,4),(3,-2),(4,-1),(5,-1))
    return sum((c*a*(-8*j-d)**k for j,c in enumerate(f) for d,a in poles),Q(0))
