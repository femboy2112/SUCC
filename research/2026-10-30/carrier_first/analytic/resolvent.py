"""Exact source-moment to boundary transport; no selected cancellation claim."""
from fractions import Fraction as Q
from math import factorial, comb

AUTHENTIC = (4, -2, -1, -1)
OFFSETS = (1, 4, 5, 6)


def source(n, coefficients=AUTHENTIC):
    if n < 1:
        raise ValueError('source clock starts at 1')
    return sum((Q(c, 8*n-8+a) for a, c in zip(OFFSETS, coefficients)), Q())


def moments(count, coefficients=AUTHENTIC):
    return [source(j+1, coefficients) for j in range(count)]


def evaluate(p, x):
    result = Q()
    for c in reversed(p):
        result = result*x+c
    return result


def inner(p, q, mu):
    return sum((a*b*mu[i+j] for i,a in enumerate(p)
                for j,b in enumerate(q)), Q())


def solve(a, b):
    """Fraction Gaussian elimination, deliberately separate from oracle."""
    n = len(b)
    rows = [[Q(x) for x in row]+[Q(y)] for row,y in zip(a,b)]
    for j in range(n):
        k = next(k for k in range(j,n) if rows[k][j])
        rows[j],rows[k] = rows[k],rows[j]
        pivot = rows[j][j]
        rows[j] = [x/pivot for x in rows[j]]
        for k in range(n):
            if k != j:
                multiple = rows[k][j]
                rows[k] = [x-multiple*y for x,y in zip(rows[k],rows[j])]
    return [row[-1] for row in rows]


def monic_orthogonal(mu, d):
    if d < 1 or len(mu) < 2*d:
        raise ValueError('degree d needs moments 0 through 2d-1')
    h = [[mu[i+j] for j in range(d)] for i in range(d)]
    return solve(h, [-mu[d+i] for i in range(d)])+[Q(1)]


def numerator(p, mu, t):
    # Integral of (p(t)-p(x))/(t-x): coefficient identity, no roots needed.
    return sum((p[k]*t**(k-1-j)*mu[j]
                for k in range(1,len(p)) for j in range(k)), Q())


def resolvent(mu, d, t=Q(16)):
    p = monic_orthogonal(mu, d)
    return numerator(p,mu,t)/evaluate(p,t)


def certificate(d, coefficients=AUTHENTIC):
    mu = moments(2*d+1,coefficients)
    p = monic_orthogonal(mu,d)
    norm = inner(p,p,mu)
    denom = evaluate(p,Q(16))**2
    center = numerator(p,mu,Q(16))/evaluate(p,Q(16))
    return {'d':d, 'polynomial':p, 'norm':norm, 'center':center,
            'lower':center+norm/(16*denom),
            'upper':center+norm/(15*denom),
            'uniform_error':4*mu[0]/(15*3600**d)}


def bbp_interval(terms):
    partial = sum((source(n)/16**n for n in range(1,terms+1)),Q())
    return partial, partial+source(terms+1)/(15*16**terms)


def atomic_moments(p, initial, count):
    """Rational continuation of Gaussian source, not original BBP law."""
    d = len(p)-1
    out = list(initial[:d])
    for n in range(d,count):
        out.append(-sum((p[j]*out[n-d+j] for j in range(d)),Q()))
    return out[:count]


def atomic_tail_budget(mu, d):
    return (resolvent(mu,d,Q(1))-16*resolvent(mu,d,Q(16)))/15


def theta_germ_tail_bound(M, K, derivative=0):
    """Rational bound for omitted completed-theta tail on a declared strip.

    K>=max(Re(s)/2-1, -(Re(s)+1)/2, 0) throughout the strip.
    This bounds derivatives of the analytic tail, not rounding error.
    """
    if min(M,K,derivative) < 0:
        raise ValueError('nonnegative integers required')
    C = 3*(M+1)**2
    degree = K+derivative
    polynomial = sum((Q(factorial(degree),factorial(degree-j)*C**(j+1))
                      for j in range(degree+1)),Q())
    return Q(4,2**derivative)*Q(1,2**C)*polynomial


def prime_jet_fake(K):
    """Mass coefficients after factoring out log(2); changed source law."""
    if K<1:
        raise ValueError('at least one matched derivative')
    epsilon=Q(1,2*4**(K+1)*2**K)
    return [(j+1,Q(1,4**(j+1)),epsilon*(-1)**j*comb(K,j))
            for j in range(K+1)]
