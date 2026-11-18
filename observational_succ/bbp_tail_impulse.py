"""Source-paid positive chronological impulse differences of BBP future tail.

The exact tail T_N is a positive Hausdorff moment, not random digits.
The finite rational bounds are rigorous; pi normality is not claimed.
"""
from fractions import Fraction as F
from math import comb, factorial
from .borwein_quantitative_certificate import source_r


def source_difference(n,k):
    """(-1)^k forward k-th difference of original signed four-pole r(n)."""
    if type(n) is not int or n<1 or type(k) is not int or k<0:
        raise ValueError('source time>=1 and difference order>=0')
    return sum((F((-1)**j*comb(k,j))*source_r(n+j)
                for j in range(k+1)),F(0))


def tail_impulse_rational_bounds(N,k,M):
    """Exact lower/upper rational certificates for positive tail impulse.

    S_(N,k) = sum_{j>=1} 16^-j (-1)^k Delta^k r(N+j)
    and M-term truncation is the lower bound. The remaining monotone
    positive source sequence gives upper error <=16^-M*d_k r(N+M+1)/15.
    """
    if type(N) is not int or N<0 or type(k) is not int or k<0 or type(M) is not int or M<1:
        raise ValueError('N>=0, k>=0, M>=1 all integers')
    lower=sum((source_difference(N+j,k)/16**j for j in range(1,M+1)),F(0))
    remainder=source_difference(N+M+1,k)/F(15*16**M)
    return lower,lower+remainder


def gamma_leading_constant(k):
    """The rigorously derived limit lim N^(k+2)*S_(N,k)."""
    if type(k) is not int or k<0:raise ValueError
    return F(factorial(k+1),64)


def locked_positive_mellin_kernel(t):
    """Alternate source K_lock=(1-t)(1+3/2(1-t)), mass exactly one."""
    t=F(t)
    return (1-t)*(1+F(3,2)*(1-t))


def locked_source_r(n):
    """Changed forcing with same positive moment asymptotics but locked x=1."""
    if type(n) is not int or n<1:raise ValueError
    h=(F(5,2),F(-4),F(3,2))
    return sum((v*(F(16,8*n-7+j)-F(1,8*n+1+j)) for j,v in enumerate(h)),F(0))


def locked_source_difference(n,k):
    if type(n) is not int or n<1 or type(k) is not int or k<0:
        raise ValueError
    return sum((F((-1)**j*comb(k,j))*locked_source_r(n+j)
                for j in range(k+1)),F(0))


def finite_source_endpoint(M):
    """The strictly positive rational P_M of literal original four-pole BBP."""
    if type(M) is not int or M<1:raise ValueError('positive finite depth')
    return sum((source_r(j)/16**j for j in range(1,M+1)),F(0))


def pascal_source_layer(M,level):
    """Rational binomial-mixture mass vector for the finite source measure.

    Layer m contains p_{m,n}=binom(m,n) S^{[M]}_{n,m-n}/P_M.
    All entries are positive rational; they sum EXACTLY to one. No
    stochastic data are inserted into the original BBP chronology.
    """
    if type(M) is not int or M<1 or type(level) is not int or level<0:
        raise ValueError('finite source M>=1 and observer layer>=0')
    mass=finite_source_endpoint(M)
    return tuple(F(comb(level,n))*tail_impulse_rational_bounds(n,level-n,M)[0]/mass
                 for n in range(level+1))


def source_moment_y(M,j):
    """Exact moment of y=t^8 for the normalized finite source ν_M/P_M."""
    if type(j) is not int or j<0:raise ValueError
    return tail_impulse_rational_bounds(j,0,M)[0]/finite_source_endpoint(M)


def certified_source_lift_error(M,level):
    """(rational tail component, rational upper ceiling for total W1 error).

    W1(lift, true normalized source pushforward under y=t^8)
      <= 1/(2 sqrt(level)) + 16^-M r(M+1)/(15 P_M).
    Uses the inequality 1/(2 sqrt(level)) <= 1/(2 isqrt(level))
    for level>=1, for a fully rational conservative upper bound.
    """
    from math import isqrt
    if type(level) is not int or level<1: raise ValueError('layer>=1')
    p=finite_source_endpoint(M)
    tail=source_r(M+1)/F(15*16**M*p)
    root=isqrt(level)
    return tail,tail+F(1,2*root)
