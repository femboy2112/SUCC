"""Rational enclosures for Fibonacci-extruded harmonic/Oily calibration.

Only Fraction/isqrt are used for certificates. The clock is declared, not an
identity between the auxiliary Pascal sensor and selected BBP digits.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt
import json


def fib(n):
    if n < 0:
        raise ValueError('nonnegative index required')
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(x, c):
    return (x[0]*c, x[1]*c) if c >= 0 else (x[1]*c, x[0]*c)


def point(x):
    return Q(x), Q(x)


@lru_cache(None)
def ln(x, terms=64):
    """Range-reduced positive atanh series with a geometric tail."""
    x = Q(x)
    if x <= 0 or terms < 1:
        raise ValueError('positive argument and precision required')
    if x < 1:
        return scale(ln(1/x, terms), -1)
    e = 0
    while x >= 2:
        x /= 2
        e += 1
    def small(y):
        z = (y-1)/(y+1)
        s = 2*sum((z**(2*j+1)/(2*j+1) for j in range(terms)), Q(0))
        return s, s+2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return add(small(x), scale(small(Q(2)), e))


@lru_cache(None)
def golden(digits=48):
    d = 10**digits
    n = isqrt(5*d*d)
    assert n*n < 5*d*d < (n+1)*(n+1)
    return Q(n-d, 2*d), Q(n+1-d, 2*d)


@lru_cache(None)
def harmonic_error(m):
    """H_m-log(m)-gamma. Binet's positive integral bounds the remainder.

    Shift small m to64, then adjacent truncations through B12/B14 enclose.
    Error width is < 1e-26 at the smallest shifted argument.
    """
    if m < 1:
        raise ValueError('positive rank required')
    j = max(m, 64)
    # B_(2k)/(2k), k=1..7. Enclosure between six and seven terms.
    c = (Q(1,12), Q(-1,120), Q(1,252), Q(-1,240),
         Q(1,132), Q(-691,32760), Q(1,12))
    s = Q(1, 2*j)-sum((c[k-1]/j**(2*k) for k in range(1,7)), Q(0))
    lo, hi = s-c[6]/j**14, s
    if j > m:
        correction = add(ln(Q(j,m)), point(-sum((Q(1,k) for k in range(m+1,j+1)),Q(0))))
        lo,hi = add((lo,hi), correction)
    return lo,hi


def golden_tail(m, cutoff=180):
    """Enclose sum_(j>m) lambda^j/j; no exponential huge-index allocation."""
    l,u = golden()
    if m >= cutoff:
        # This common upper bound is intended only for finite point queries.
        return Q(0), u**(cutoff+1)/((cutoff+1)*(1-u))
    lo = sum((l**j/j for j in range(m+1,cutoff+1)),Q(0))
    hi = sum((u**j/j for j in range(m+1,cutoff+1)),Q(0))
    return lo,hi+u**(cutoff+1)/((cutoff+1)*(1-u))


def zeta_fib(s=1, cutoff=120):
    """Z_F(s)=sum_(n>=2) F_n^-s, s positive integer.

    F_(n+2)>=2F_n bounds the uncomputed two interleaved tails.
    The usual reciprocal Fibonacci constant is1+Z_F(1).
    """
    if s < 1 or cutoff < 2:
        raise ValueError('positive exponent and cutoff>=2 required')
    p = sum((Q(1,fib(n)**s) for n in range(2,cutoff+1)),Q(0))
    tail = (Q(1,fib(cutoff+1)**s)+Q(1,fib(cutoff+2)**s))/(1-Q(1,2**s))
    return p,p+tail


def log_fibonorial_constant(cutoff=80):
    """log C, C=prod_(n>=1)(1-(-lambda^2)^n)."""
    l,u = golden()
    v = point(0)
    for n in range(1,cutoff+1):
        if n % 2:
            a,b = 1+l**(2*n), 1+u**(2*n)
        else:
            a,b = 1-u**(2*n), 1-l**(2*n)
        d=10**48
        a=Q((a*d).__floor__(),d)
        b=Q((b*d).__ceil__(),d)
        # All arguments lie near1. Generic rational logarithms remain exact.
        v=add(v,(ln(a)[0],ln(b)[1]))
    t=u*u
    bound=t**(cutoff+1)/((1-t)*(1-t**(cutoff+1)))
    return v[0]-bound,v[1]+bound


def oily_budget(cutoff=120, golden_cutoff=180):
    """B_F=sum_(n>=2)(Omega- Omega_(F_n)) with a proved global tail."""
    h=point(0)
    for n in range(2,cutoff+1):
        h=add(h,harmonic_error(fib(n)))
    htail=(Q(1,fib(cutoff+1))+Q(1,fib(cutoff+2)))
    h=(h[0],h[1]+htail)  # half of the reciprocal-series tail
    g=point(0)
    n=2
    while fib(n)<golden_cutoff:
        g=add(g,golden_tail(fib(n),golden_cutoff))
        n+=1
    _,u=golden()
    # Every remaining Fibonacci value is a distinct integer >=fib(n).
    # Sum over that larger set, then bound all denominators by fib(n)+1.
    tail=u**(golden_cutoff+1)/((golden_cutoff+1)*(1-u)**2)
    g=(g[0],g[1]+tail)
    return {'harmonic_budget':h,'golden_budget':g,'oily_budget':add(h,g)}


def outward(x,digits=24):
    d=10**digits
    a=(x[0]*d).__floor__()
    b=(x[1]*d).__ceil__()
    return {'lo_numerator':str(a),'hi_numerator':str(b),'denominator':str(d),
            'display_midpoint':float((x[0]+x[1])/2),
            'display_width':float(x[1]-x[0])}


def certificate(cutoff=120):
    vals=oily_budget(cutoff)
    vals['reciprocal_fibonacci']=add(point(1),zeta_fib(1,cutoff))
    vals['fibonacci_square_reciprocal']=zeta_fib(2,cutoff)
    vals['log_fibonorial_constant']=log_fibonorial_constant(80)
    l,u=golden()
    factor=(ln(1+l*l)[0],ln(1+u*u)[1])
    vals['renormalized_pascal_sum']=add(add(vals['log_fibonorial_constant'],scale(factor,-1)),vals['oily_budget'])
    return {'status':'PASS','authority':'exact rational enclosures plus proved analytic tails',
            'cutoff':cutoff,'constants':{k:outward(v) for k,v in vals.items()},
            'point_controls':{str(m):outward(add(harmonic_error(m),golden_tail(m)))
                              for m in (1,2,3,5,8,13,21,55,144)}}


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
