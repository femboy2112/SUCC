"""Exact finite clock/Ramanujan transport and certified singular-series tails.

Independent cloud lane; no imports from Claude's goldbach_circle implementation.
The universal proofs and scope are in CLOUD_RAMANUJAN_TRANSPORT.md.  Infinite
series APIs require N != 0; finite arithmetic functions allow N = 0.  These
objects do not count prime representations and do not prove binary Goldbach.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt


def _integer(n: int, name: str, minimum: int | None = None) -> None:
    if type(n) is not int or (minimum is not None and n < minimum):
        raise ValueError(f"{name} must be an integer" +
                         (f" >= {minimum}" if minimum is not None else ""))


def _nonzero(N: int) -> None:
    _integer(N, "N")
    if N == 0:
        raise ValueError("N=0 has a divergent singular series")


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    """Trial-division factorization; exact, intended for certificate sizes."""
    _integer(n, "n", 1)
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def primes_upto(P: int) -> tuple[int, ...]:
    _integer(P, "P", 0)
    sieve = bytearray(b"\x01") * (P + 1)
    sieve[:min(2, P + 1)] = bytes(min(2, P + 1))
    for p in range(2, isqrt(P) + 1):
        if sieve[p]:
            start = p * p
            sieve[start::p] = bytes(len(sieve[start::p]))
    return tuple(p for p in range(2, P + 1) if sieve[p])


def divisors(n: int) -> tuple[int, ...]:
    _integer(n, "n", 1)
    ds = [1]
    for p, e in factorization(n):
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return tuple(sorted(ds))


def mobius(n: int) -> int:
    fs = factorization(n)
    return 0 if any(e > 1 for _, e in fs) else (-1) ** len(fs)


def totient(n: int) -> int:
    out = n
    for p, _ in factorization(n):
        out = out // p * (p - 1)
    return out


def ramanujan_sum(q: int, N: int) -> int:
    """c_q(N) = sum_{d | gcd(q,N)} d mu(q/d), including N=0."""
    _integer(q, "q", 1)
    _integer(N, "N")
    return sum(d * mobius(q // d) for d in divisors(gcd(q, N)))


def singular_coefficient(q: int, N: int) -> Fraction:
    """Finite coefficient mu(q)^2 c_q(N)/phi(q)^2; N=0 allowed."""
    _integer(q, "q", 1)
    _integer(N, "N")
    return Fraction(mobius(q) ** 2 * ramanujan_sum(q, N), totient(q) ** 2)


def unit_pair_density(q: int, N: int) -> Fraction:
    """Direct finite-clock census, normalized by independent unit densities."""
    _integer(q, "q", 1)
    _integer(N, "N")
    count = sum(gcd(x, q) == gcd(N - x, q) == 1 for x in range(q))
    return Fraction(q * count, totient(q) ** 2)


def divisor_clock_expansion(q: int, N: int) -> Fraction:
    """Exact harmonic identity: unit_pair_density(q,N) = sum_{d|q} a_d(N)."""
    _integer(q, "q", 1)
    _integer(N, "N")
    return sum((singular_coefficient(d, N) for d in divisors(q)), Fraction())


def local_factor(p: int, N: int) -> Fraction:
    _integer(p, "p", 2)
    _integer(N, "N")
    if factorization(p) != ((p, 1),):
        raise ValueError("p must be a genuine prime")
    return 1 + singular_coefficient(p, N)


def prime_product(N: int, P: int) -> Fraction:
    """Finite product over p <= P; no assumption that all p|N were seen."""
    _integer(N, "N")
    _integer(P, "P", 2)
    out = Fraction(1)
    for p in primes_upto(P):
        out *= local_factor(p, N)
    return out


@dataclass(frozen=True)
class PrimeProductEnclosure:
    N: int
    P: int
    finite_product: Fraction
    lower: Fraction
    upper: Fraction
    residual_after_small_primes: int
    unseen_distinct_prime_count_bound: int
    generic_tail_defect_bound: Fraction


def prime_product_enclosure(N: int, P: int) -> PrimeProductEnclosure:
    """Enclose S(N) without factoring the residual with all prime factors > P.

    Let R be |N| after removing all p <= P, and k=floor(log_{P+1} R),
    computed by integer comparisons. For even nonzero N and P >= 2:
      F_P (1-E_P) <= S(N) <= F_P (P/(P-1))^k,
    E_P = 1/(4 ceil(P/2)-2). Odd nonzero N gives exactly [0,0].
    """
    _nonzero(N)
    _integer(P, "P", 2)
    ps = primes_upto(P)
    residual = abs(N)
    finite = Fraction(1)
    for p in ps:
        finite *= local_factor(p, N)
        while residual % p == 0:
            residual //= p
    k, power = 0, P + 1
    while power <= residual:
        k += 1
        power *= P + 1
    defect = Fraction(1, 4 * ((P + 1) // 2) - 2)
    lower = finite * (1 - defect)
    upper = finite * Fraction(P, P - 1) ** k
    return PrimeProductEnclosure(N, P, finite, lower, upper, residual, k, defect)


def modulus_partial_sum(N: int, Q: int) -> Fraction:
    _integer(N, "N")
    _integer(Q, "Q", 1)
    return sum((singular_coefficient(q, N) for q in range(1, Q + 1)), Fraction())


def modulus_tail_bound(N: int, Q: int) -> Fraction:
    """sum_{q>Q}|a_q(N)| <= (12/Q) prod_{p|N}(1+p/(p-1)).

    Requires factoring |N|, unlike prime_product_enclosure. It bounds the
    ordinary modulus-ordered series, not a product over prime cutoffs.
    """
    _nonzero(N)
    _integer(Q, "Q", 1)
    bound = Fraction(12, Q)
    for p, _ in factorization(abs(N)):
        bound *= 1 + Fraction(p, p - 1)
    return bound


def modulus_enclosure(N: int, Q: int) -> tuple[Fraction, Fraction]:
    _nonzero(N)
    _integer(Q, "Q", 1)
    if N % 2:
        return Fraction(), Fraction()
    center = modulus_partial_sum(N, Q)
    radius = modulus_tail_bound(N, Q)
    return max(Fraction(), center - radius), center + radius
