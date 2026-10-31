"""Exact finite-arithmetic probes for SUCC N/Z-carrier research.

Pure stdlib. Classical identities are calibration; no pi-normality proof.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb, factorial, isqrt, log


def generalized_binom(n: int, k: int) -> int:
    """Polynomial continuation of binomial coefficient to integer n."""
    if k < 0:
        return 0
    out = 1
    for j in range(k):
        out *= n - j
    return out // factorial(k)


def pascal_delta(k: int, n: int) -> int:
    return generalized_binom(n + 1, k) - generalized_binom(n, k)


def pascal_polarization(a: int, b: int) -> int:
    return generalized_binom(a + b, 2) - generalized_binom(a, 2) - generalized_binom(b, 2)


def vandermonde_signed(a: int, b: int, k: int) -> int:
    """Convolution of two Pascal paths; valid for signed integer ages."""
    return sum(generalized_binom(a,j)*generalized_binom(b,k-j)
               for j in range(k+1))


def first_hex_digit(x: Fraction) -> int:
    """Observation map on the circle (not a closed next-state map)."""
    x=x - (x.numerator//x.denominator)
    return (16*x.numerator)//x.denominator


def falling_factorial(n: int, k: int) -> int:
    out = 1
    for j in range(k):
        out *= n-j
    return out


@lru_cache(None)
def stirling2(m: int, n: int) -> int:
    if m == 0:
        return int(n == 0)
    if n <= 0 or n > m:
        return 0
    return stirling2(m - 1, n - 1) + n * stirling2(m - 1, n)


def hasse_difference_at_negative(m: int, n: int) -> int:
    """Hasse inner signed n-th Pascal difference at s=-m."""
    return sum((-1)**k * comb(n, k) * (k+1)**m for k in range(n+1))


def zeta_negative_pascal(m: int) -> Fraction:
    """Finite Hasse/Pascal continuation at negative integer (classical)."""
    numerator = sum((Fraction(hasse_difference_at_negative(m, n), 2**(n+1))
                     for n in range(m+1)), Fraction(0))
    return numerator / (1 - 2**(m+1))


def zeta_negative_stirling(m: int) -> Fraction:
    numer = sum((Fraction((-1)**n*factorial(n)*stirling2(m+1,n+1),2**(n+1))
                 for n in range(m+1)), Fraction(0))
    return numer / (1 - 2**(m+1))


def bernoulli(n: int) -> Fraction:
    b = [Fraction(1)]
    for j in range(1, n+1):
        b.append(-sum((comb(j+1,k)*b[k] for k in range(j)), Fraction(0)) / (j+1))
    return b[-1]


def zeta_negative_bernoulli(m: int) -> Fraction:
    return (-1)**m * bernoulli(m+1) / (m+1)


def fibonacci_tiling_count(n: int) -> int:
    """Tilings by unit/length-2 pieces (Pascal graded sum)."""
    return sum(comb(n-k,k) for k in range(n//2+1))


def fibonacci(n: int) -> int:
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a


def gamma_moment_from_pascal(rank: int, k: int) -> int:
    """E Gamma(rank, 1)^k = k! * C(rank+k-1,k), integral rank."""
    assert rank>=1 and k>=0
    return factorial(k)*comb(rank+k-1,k)


def primes_upto(n: int) -> list[int]:
    if n < 2:
        return []
    sieve=bytearray(b'\x01')*(n+1)
    sieve[0]=sieve[1]=0
    for d in range(2,isqrt(n)+1):
        if sieve[d]:
            sieve[d*d:n+1:d]=b'\x00'*((n-d*d)//d+1)
    return [i for i in range(n+1) if sieve[i]]


def mangoldt_terms(n: int) -> list[tuple[int, int]]:
    """(prime-power n, underlying prime) for n<=N."""
    out=[]
    for p in primes_upto(n):
        x=p
        while x<=n:
            out.append((x,p))
            x*=p
    return sorted(out)


def arch_prime_partial(n: int) -> float:
    """Truncate the convergent prime-power sum sum Lambda(k)/k^2."""
    return sum(log(p)/(k*k) for k,p in mangoldt_terms(n))


def arch_prime_tail_bound(n: int) -> float:
    """Upper bound for omitted sum Lambda(k)/k^2, n>=3."""
    assert n>=3
    return (log(n)+1)/n


def bbp_r(n: int) -> Fraction:
    assert n>=1
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def bbp_r_grouped(n: int) -> Fraction:
    a=8*n-7
    return Fraction(6,a*(a+3))+Fraction(4,a*(a+4))+Fraction(5,a*(a+5))


def bbp_u(n: int, seed: Fraction = Fraction(0)) -> Fraction:
    u=seed
    for k in range(1,n+1):
        u=16*u+bbp_r(k)
    return u


def bbp_tail_interval(n: int, R: int) -> tuple[Fraction,Fraction]:
    """Certified T_n^R < T_n < T_n^R + 16^-R r(n+R+1)/15."""
    assert n>=0 and R>=1
    t=sum((Fraction(1,16**j)*bbp_r(n+j) for j in range(1,R+1)),Fraction(0))
    return t,t+Fraction(1,16**R)*bbp_r(n+R+1)/15


def bbp_digit_word(n: int, m: int, R: int = 28) -> str:
    """Certify m digits starting at n-th selected BBP radix circle state."""
    a,b=bbp_tail_interval(n,R)
    x=bbp_u(n)
    lo=(x+a)*16**m
    hi=(x+b)*16**m
    if lo.numerator//lo.denominator != hi.numerator//hi.denominator:
        raise ValueError("ambiguous: increase R")
    return format((lo.numerator//lo.denominator)%(16**m),f'0{m}X')


def bbp_conjugacy_residual(n: int, R: int) -> Fraction:
    """Finite-tail identity: T_(n+1)^R -16 T_n^(R+1)+r_(n+1)=0."""
    a,_=bbp_tail_interval(n+1,R)
    b,_=bbp_tail_interval(n,R+1)
    return a-16*b+bbp_r(n+1)


def theta_trunc(t: float, M: int) -> float:
    from math import exp,pi
    return sum(exp(-pi*j*j*t) for j in range(-M,M+1))


def theta_tail_bound(t: float, M: int) -> float:
    from math import exp,pi
    assert t>0 and M>=0
    return 2*exp(-pi*t*(M+1)**2)/(1-exp(-pi*t*(2*M+3)))
