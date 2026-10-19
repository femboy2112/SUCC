"""Finite-height primitive additive contacts: exact CRT + Möbius cancellation.

For EVERY positive modulus m, including moving and enormous m,
N_H(m) = H²*zeta(2)^(-1)*prod_{p^e||m}p^(1-e)/(p+1)
         + O(H log(2H)), absolute implied constant independent of m.
No ABC/RH claim; this is elementary arithmetic with exact finite tests.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from math import gcd, prod

MAX_HEIGHT = 100_000
MAX_CERT_HEIGHT = 2_000
MAX_MODULUS = 10**12


class HeightError(ValueError):
    pass


def typed(n: int, name: str, low: int, high: int) -> int:
    if type(n) is not int or not low <= n <= high:
        raise HeightError(f"{name} must be exact integer in {low}..{high}")
    return n


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    typed(n, "modulus", 1, MAX_MODULUS)
    out, d = [], 2
    while d*d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            out.append((d, k))
        d = 3 if d == 2 else d+2
    if n > 1:
        out.append((n, 1))
    return tuple(out)


@lru_cache(maxsize=32)
def mobius_sieve(H: int) -> tuple[int, ...]:
    typed(H, "height", 1, MAX_HEIGHT)
    mu, spf, primes = [0]*(H+1), [0]*(H+1), []
    mu[1] = 1
    for n in range(2, H+1):
        if not spf[n]:
            spf[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > spf[n] or n*p > H:
                break
            spf[n*p] = p
            if n % p == 0:
                mu[n*p] = 0
                break
            mu[n*p] = -mu[n]
    return tuple(mu)


def box_sum_contacts(U: int, m: int) -> int:
    """Number of 1<=x,y<=U with m|x+y, in O(1) exact operations.

    For U=qm+r: F=mq²+2qr+max(0,2r-m+1).
    Consequently |F-U²/m| <= min(U,m-1), uniformly in m.
    """
    typed(U, "box side", 0, MAX_HEIGHT)
    typed(m, "modulus", 1, MAX_MODULUS)
    q, r = divmod(U, m)
    return m*q*q + 2*q*r + max(0, 2*r-m+1)


def primitive_sum_contacts(H: int, m: int) -> int:
    """Exact count of primitive 1<=a,b<=H with m|a+b."""
    typed(H, "height", 1, MAX_HEIGHT)
    typed(m, "modulus", 1, MAX_MODULUS)
    mu = mobius_sieve(H)
    return sum(mu[d]*box_sum_contacts(H//d, m//gcd(d,m))
               for d in range(1, H+1) if mu[d])


def local_conditional_limit(m: int) -> Q:
    """Conditional probability among primitive pairs as H->infinity.

    The absolute main term is H² * this / zeta(2). No numerical zeta
    approximation is used as proof.
    """
    return prod((Q(1, p**(e-1)*(p+1))
                 for p,e in factorization(m)), start=Q(1))


def height_error_bound(H: int) -> int:
    """Certified |N_H(m)-H²*D(m)/zeta(2)|, uniform ALL m>=1."""
    typed(H, "height", 1, MAX_HEIGHT)
    return H*(4+3*(H-1).bit_length())


def partial_main(H: int, m: int) -> Q:
    """Exact truncated Möbius main, no floating zeta approximation."""
    typed(H, "certificate height", 1, MAX_CERT_HEIGHT)
    typed(m, "modulus", 1, MAX_MODULUS)
    mu=mobius_sieve(H)
    return H*H*sum((Q(mu[d]*gcd(d,m),m*d*d)
                    for d in range(1,H+1) if mu[d]),Q())


@dataclass(frozen=True)
class HeightReceipt:
    H: int
    modulus: int
    primitive_pairs: int
    simultaneous_contacts: int
    actual_fraction: Q
    limiting_fraction: Q
    partial_main: Q
    finite_error_upper: int
    infinite_error_upper: int
    height_forbidden: bool


def receipt(H: int, m: int) -> HeightReceipt:
    typed(H,"certificate height",1,MAX_CERT_HEIGHT)
    observed=primitive_sum_contacts(H,m)
    total=primitive_sum_contacts(H,1)
    approx=partial_main(H,m)
    limit=height_error_bound(H)
    if abs(Q(observed)-approx)>limit-H:
        raise AssertionError("finite CRT/Mobius enclosure failed")
    if m>2*H and observed:
        raise AssertionError("impossible Archimedean contact survived")
    return HeightReceipt(H,m,total,observed,Q(observed,total),
                         local_conditional_limit(m),approx,limit-H,
                         limit,m>2*H)
