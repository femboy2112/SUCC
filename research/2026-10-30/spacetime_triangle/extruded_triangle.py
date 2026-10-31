"""Exact four-pole SUCC zero-spine/Pascal spacetime triangle (research only).

The positive Bernoulli sensor is auxiliary; it does not sample pi's digits.
All finite source and grade calculations use exact rational arithmetic.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb

POLES = ((0, 4), (3, -2), (4, -1), (5, -1))

@lru_cache(None)
def R(a):
    a = F(a)
    if a <= 0:
        raise ValueError("a must be positive")
    return sum((F(c, 1) / (a+d) for d, c in POLES), F(0))

R1 = R(1)
C_SPINE = F(225, 3008)

def r(n):
    if n < 1:
        raise ValueError("n must be positive")
    return R(8*n-7)

def spine_mass(n):
    """Probability of n-1 zero outcomes under the retained X~mu_1 law."""
    return r(n) / R1

def spine_next(n):
    """Posterior predictive P(next zero | n-1 observed zeros)."""
    return r(n+1) / r(n)

def spine_hazard(n):
    return 1-spine_next(n)

@lru_cache(None)
def word_mass(a, m, j):
    """One ordered word of length m with j successes, given X~mu_a."""
    if m < 0:
        raise ValueError("m must be nonnegative")
    if j < 0 or j > m:
        return F(0)
    return sum(((-1)**k * comb(j,k)*R(a+8*(m-j+k))
                for k in range(j+1)), F(0)) / R(a)

def endpoint_mass(a, m, j):
    if not 0 <= j <= m:
        return F(0)
    return comb(m,j)*word_mass(a,m,j)

def posterior_transition(a,m,j):
    """Failure and success probabilities retaining the latent posterior."""
    if not 0 <= j <= m:
        raise ValueError("invalid grade")
    p = word_mass(a,m,j)
    return word_mass(a,m+1,j)/p, word_mass(a,m+1,j+1)/p

def fan_mass(n,j):
    """One spine of n-1 zeros, followed by n trials with j successes."""
    return spine_mass(n)*endpoint_mass(8*n-7,n,j)

def fan_mass_independent(n,j):
    """Independent Pascal expansion directly from four native BBP poles."""
    if not 0 <= j <= n:
        return F(0)
    return F(comb(n,j),1)*sum(((-1)**k*comb(j,k)*r(2*n-j+k)
                              for k in range(j+1)),F(0))/R1

def fan_fourier(n,z):
    """Exact grade character for any rational z, including parity z=-1."""
    z=F(z)
    a=8*n-7
    return sum((F(comb(n,k),1)*z**(n-k)*(1-z)**k*r(n+k)
                for k in range(n+1)),F(0))/R1

def fan_fourier_by_endpoints(n,z):
    z=F(z)
    return sum((fan_mass(n,j)*z**j for j in range(n+1)),F(0))

def moment_bound(n,z):
    """Chernoff moment bound E[z^J_n] <= R(a-8n(z-1))/R(a)."""
    z=F(z)
    a=8*n-7
    if z < 1 or a-8*n*(z-1) <= 0:
        raise ValueError("z must be >=1 with a-8n(z-1)>0")
    return R(a-8*n*(z-1))/R(a)

def high_grade_bound(L):
    """Uniform bound for P(J_n>=L), ALL n>=1, L>=4.

    For n<L the probability is zero. Otherwise use z=2-2/L and
    R(a)<=15/a^2, R(a)>=15/(a+5)^2, plus Chernoff.
    """
    if L < 4:
        raise ValueError("L must be >=4")
    return F(256,81)*L*L/F(2**L)

def spine_boundary_moment(n,k):
    """Exact E[(n*(1-exp(-8X)))**k | n-1 previous zeros], k>=0."""
    if n < 1 or k < 0:
        raise ValueError("n must be positive and k nonnegative")
    return F(n**k)*sum(((-1)**ell*comb(k,ell)*r(n+ell)
                        for ell in range(k+1)),F(0))/r(n)

def native_row(n):
    return tuple(endpoint_mass(8*n-7,n,j) for j in range(n+1))

def source_R_bounds(a):
    """15/(a+5)^2 <= R(a) <= 15/a^2, for a>0."""
    a=F(a)
    return F(15)/(a+5)**2, F(15)/a**2
