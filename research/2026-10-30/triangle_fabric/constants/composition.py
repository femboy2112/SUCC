"""Exact BBP sum/proportion diagnostics and rigorous logarithm enclosures.

All mathematical claims concern positive source composition, not selected digits.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial

SOURCE = ((F(0), F(4)), (F(3), F(-2)), (F(4), F(-1)), (F(5), F(-1)))
SIGMA2 = F(1379, 900)


def source(a, derivative=0, source=SOURCE):
    a = F(a)
    if a <= 0 or derivative < 0:
        raise ValueError("positive a and nonnegative derivative required")
    return sum((c * (-1)**derivative * factorial(derivative) /
                (a+d)**(derivative+1) for d, c in source), F(0))


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def scale(x, c):
    c = F(c)
    return (c*x[0], c*x[1]) if c >= 0 else (c*x[1], c*x[0])


def point(q):
    return F(q), F(q)


def ln_interval(q, terms=128):
    """Exact rational enclosure via range-reduced atanh; no floating arithmetic."""
    q = F(q)
    if q <= 0 or terms < 1:
        raise ValueError("positive argument and at least one term required")
    if q < 1:
        return scale(ln_interval(1/q, terms), -1)
    exponent = 0
    while q >= 2:
        q /= 2
        exponent += 1
    def reduced(x):
        z = (x-1)/(x+1)
        partial = 2*sum((z**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
        remainder = 2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return partial, partial+remainder
    return add(reduced(q), scale(reduced(F(2)), exponent))


def j_integral(b, c, power):
    """Integral_0^1 u(1-u)/(c+(b-c)u)^power du, powers2,3."""
    b, c = F(b), F(c)
    if min(b, c) <= 0 or power not in (2, 3):
        raise ValueError("positive rates, power2 or3")
    if b == c:
        return point(1/(6*b**power))
    d = b-c
    log = ln_interval(b/c)
    if power == 2:
        return scale(add(scale(log, b+c), point(-2*d)), 1/d**3)
    return scale(add(scale(log, -1), point(d*(b+c)/(2*b*c))), 1/d**3)


def proportion_moments(a, source_terms=SOURCE):
    """Enclosures for E B and E[a(X+Y)B]; exact mean of a(X+Y)."""
    a=F(a)
    norm=source(a, source=source_terms)
    eb=point(0)
    esb=point(0)
    for di, ci in source_terms:
        for dj, cj in source_terms:
            eb=add(eb, scale(j_integral(a+di,a+dj,2),ci*cj/norm**2))
            esb=add(esb, scale(j_integral(a+di,a+dj,3),2*a*ci*cj/norm**2))
    es=-2*a*source(a,1,source_terms)/norm
    covariance=add(esb,scale(eb,-es))
    return {"EB":eb,"ESB":esb,"ES":es,"covariance":covariance}


def log_increment(a, source_terms=SOURCE):
    """Gamma-free E log(X+Y)-E log X; convolution partial fractions."""
    a=F(a)
    norm=source(a,source=source_terms)
    one=point(0)
    two=point(0)
    for d,c in source_terms:
        b=a+d
        one=add(one,scale(ln_interval(b),-c/(b*norm)))
    for di,ci in source_terms:
        for dj,cj in source_terms:
            b,c=a+di,a+dj
            if b==c:
                term=scale(add(point(1),scale(ln_interval(b),-1)),1/b**2)
            else:
                term=scale(add(scale(ln_interval(c),-1/c),
                               scale(ln_interval(b),1/b)),1/(b-c))
            two=add(two,scale(term,ci*cj/norm**2))
    return add(two,scale(one,-1))


def rational_lower_bounds(a):
    a=F(a)
    r=source(a)
    b=a+10
    v=(source(b,1)**2+source(b)*source(b,2))/r**2
    return {"proportion_gap":SIGMA2*v/175,"harmonic_gap":SIGMA2*v/50}


# Q(lambda), lambda^2=1-lambda; pairs are rational coefficients of1,lambda.
def gadd(x,y):
    return x[0]+y[0], x[1]+y[1]


def gscale(x,c):
    return x[0]*c,x[1]*c


def gmul(x,y):
    a,b=x; c,d=y
    return a*c+b*d,a*d+b*c-b*d


def ginv(x):
    a,b=x
    norm=a*a-a*b-b*b
    if norm==0:
        raise ZeroDivisionError("zero golden field element")
    return (a-b)/norm,-b/norm


def gpower(x,n):
    result=(F(1),F(0))
    for _ in range(n):
        result=gmul(result,x)
    return result


def golden_laplace(a):
    a=F(a)
    result=(F(0),F(0))
    for d,c in SOURCE:
        result=gadd(result,gscale(ginv((a+d,a)),c))
    return gscale(result,1/source(a))


def golden_excess(a):
    lam=(F(0),F(1)); l2=(F(1),F(-1))
    l=golden_laplace(a)
    return gmul(gadd(l,gscale(l2,-1)),gadd(lam,gscale(l,-1)))


def golden_interval(x,bits=192):
    """Exact interval for a+b lambda using integer square-root bounds."""
    from math import isqrt
    den=2**bits
    k=isqrt(5*den*den)
    lam=((F(k,den)-1)/2,(F(k+1,den)-1)/2)
    return add(point(x[0]),scale(lam,x[1]))


def jets(source_terms=SOURCE, depth=4):
    """Taylor coefficients of sum c exp(-d x)."""
    return [sum((c*(-d)**j/F(factorial(j)) for d,c in source_terms),F(0))
            for j in range(depth+1)]


def jet_variance(source_terms=SOURCE):
    _,c1,c2,c3=jets(source_terms,3)
    return 2*c3/c1-(c2/c1)**2


def dyadic_outward(interval,bits=160):
    scale_=2**bits
    lo,hi=interval
    low=(lo.numerator*scale_)//lo.denominator
    upper=-((-hi.numerator*scale_)//hi.denominator)
    return str(F(low,scale_)),str(F(upper,scale_))


def harmonic(n):
    return sum((F(1,j) for j in range(1,n+1)),F(0))


def convolution_partial_fractions(k):
    """Coefficients of R(a+t)^k at poles t=−a−d, independent of a."""
    if k<1:raise ValueError('positive convolution count required')
    result=[]
    for dj,cj in SOURCE:
        # u R(a−a−dj+u) near u=0.
        base=[cj]+[sum((ci*(-1)**(j-1)/(di-dj)**j
                       for di,ci in SOURCE if di!=dj),F(0))
                   for j in range(1,k)]
        power=[F(1)]+[F(0)]*(k-1)
        for _ in range(k):
            power=[sum((power[i]*base[j-i] for i in range(j+1)),F(0))
                   for j in range(k)]
        result.extend((dj,k-j,value) for j,value in enumerate(power))
    return result


def log_increment_k(a,k):
    """Rigorous gamma-free log composition increment for k native copies."""
    a=F(a); norm=source(a)**k
    total=point(0); mass=F(0)
    for d,m,c in convolution_partial_fractions(k):
        weight=c/(a+d)**m/norm
        mass+=weight
        term=add(point(harmonic(m-1)),scale(ln_interval(a+d),-1))
        total=add(total,scale(term,weight))
    assert mass==1
    one=point(0)
    for d,c in SOURCE:
        one=add(one,scale(ln_interval(a+d),-c/((a+d)*source(a))))
    return add(total,scale(one,-1))


def rank_harmonic_bound(a,k):
    if k<2:raise ValueError('at least two native copies required')
    a=F(a)
    return F(k-1,2*k+1)*SIGMA2*a**4/(a+5)**6


def golden_excess_k(a,k):
    lam=(F(0),F(1)); l=golden_laplace(a)
    return gadd(gadd(l,gscale(gpower(l,k),-1)),
                gadd(gscale(gpower(lam,2),-1),gpower(lam,2*k)))
