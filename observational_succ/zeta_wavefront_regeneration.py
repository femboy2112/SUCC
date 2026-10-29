"""Zeta Gibbs wavefront: exact finite-prime certificates and source contracts.

Everything implemented here is finite/exact rational arithmetic. The universal
Hilbert and critical-scaling theorems are in the accompanying paper dossier.
This is not an implementation of ζ analytic continuation, quantum dynamics,
or a source map from the authenticated zero-seeded BBP orbit.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import isqrt
from dataclasses import dataclass

SOURCE = "genuine-rational-prime-zeta-Gibbs-wavefront-v1"


def check_beta(beta: int) -> int:
    if type(beta) is not int or beta < 2:
        raise ValueError("integer beta >= 2 required for exact rational normalization")
    return beta


def is_prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def prime_set(ps: tuple[int, ...]) -> tuple[int, ...]:
    if type(ps) is not tuple or not ps:
        raise ValueError("nonempty ordered tuple of genuine primes required")
    if tuple(sorted(set(ps))) != ps or any(not is_prime(p) for p in ps):
        raise ValueError("primes must be strictly increasing, unique and genuine")
    return ps


def beta_prime_ratio(p: int, beta: int) -> F:
    check_beta(beta)
    if not is_prime(p):
        raise ValueError("genuine prime required")
    return F(1, p**beta)


def finite_euler_partition(ps: tuple[int, ...], beta: int) -> F:
    ps = prime_set(ps)
    check_beta(beta)
    z = F(1)
    for p in ps:
        q = beta_prime_ratio(p, beta)
        z /= (1-q)
    return z


def prime_exponents(n: int, ps: tuple[int, ...]) -> tuple[int, ...] | None:
    ps = prime_set(ps)
    if type(n) is not int or n < 1:
        raise ValueError("positive integer source index required")
    v = []
    for p in ps:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        v.append(k)
    return tuple(v) if n == 1 else None


def smooth_probability(n: int, ps: tuple[int, ...], beta: int) -> F:
    """Exact Gibbs probability in the infinite F-smooth subcarrier."""
    if prime_exponents(n, ps) is None:
        return F(0)
    return F(1, n**check_beta(beta)) / finite_euler_partition(ps, beta)


def finite_prime_event_probability(p: int, ps: tuple[int, ...], beta: int) -> F:
    """Exact P(p|N) under F-smooth Gibbs prior; p must be one of F."""
    ps = prime_set(ps)
    if p not in ps:
        raise ValueError("conditioning on inactive prime is not available")
    return beta_prime_ratio(p, beta)


def regenerated_probability(m: int, p: int, ps: tuple[int, ...], beta: int) -> F:
    """P(N/p=m | p|N), using the SAME labelled F-smooth source."""
    return smooth_probability(p*m, ps, beta) / finite_prime_event_probability(p, ps, beta)


def regenerated_word_probability(m: int, word: tuple[int, ...], ps: tuple[int, ...], beta: int) -> F:
    """Condition/divide repeatedly on an arbitrary genuine-prime word."""
    if type(word) is not tuple or not word or any(p not in prime_set(ps) for p in word):
        raise ValueError("nonempty word of available genuine primes required")
    prod = 1
    for p in word:
        prod *= p
    denominator = F(1)
    for p in word:
        denominator *= beta_prime_ratio(p, beta)
    return smooth_probability(prod*m, ps, beta)/denominator


def prime_energy_base(p: int) -> int:
    """The arithmetic base p, NOT the numerical energy increment log(p)."""
    if not is_prime(p):
        raise ValueError("not prime")
    return p


def additive_up_rate(n: int, beta: int) -> F:
    if type(n) is not int or n < 1:
        raise ValueError("positive n required")
    return F(n, n+1)**check_beta(beta)


def prime_up_rate(p: int, beta: int) -> F:
    return beta_prime_ratio(p, beta)


def raw_probability_ratio(n: int, m: int, beta: int) -> F:
    if type(n) is not int or type(m) is not int or min(n,m)<1:
        raise ValueError("positive n,m required")
    return F(n, m)**check_beta(beta)


def additive_detailed_balance_ratio(n: int, beta: int) -> F:
    """π(n)q(n,n+1)/π(n+1)q(n+1,n) exactly equals 1."""
    return raw_probability_ratio(n, n+1, beta)**(-1)*additive_up_rate(n, beta)


def prime_detailed_balance_ratio(n: int, p: int, beta: int) -> F:
    return raw_probability_ratio(n, p*n, beta)**(-1)*prime_up_rate(p, beta)


def local_mode_probability(p: int, beta: int, occupation: int) -> F:
    if type(occupation) is not int or occupation < 0:
        raise ValueError("nonnegative occupation required")
    q = beta_prime_ratio(p,beta)
    return (1-q)*q**occupation


def local_resolvent_coefficient(p: int, beta: int, occupation: int) -> F:
    """Exact squared amplitude of unnormalized pumped prime mode at occupation k."""
    if type(occupation) is not int or occupation < 0:
        raise ValueError("nonnegative occupation required")
    return beta_prime_ratio(p,beta)**occupation


def finite_pump_normalization(ps: tuple[int, ...], beta: int) -> F:
    """Tensor product of local L2 mode norms squared == finite Euler Z."""
    return finite_euler_partition(ps,beta)


def counterfeit_composite_amplitude_multiplicity(n: int, bases: tuple[int, ...]) -> int:
    """Count multiple encodings n=prod bases[i]^k_i for small countermodels.

    A composite base is a distinct coordinate here *deliberately*; the result
    exposes source-map duplication and is not a second prime.
    """
    if type(n) is not int or n < 1 or type(bases) is not tuple or not bases:
        raise ValueError("positive index and nonempty base tuple required")
    if any(type(p) is not int or p < 2 for p in bases):
        raise ValueError("bases must >=2")
    count=0
    def count_paths(i: int, remaining: int):
        nonlocal count
        if i==len(bases):
            count += int(remaining==1)
            return
        k=remaining
        while True:
            count_paths(i+1,k)
            if k%bases[i]:
                break
            k//=bases[i]
    count_paths(0,n)
    return count


def exact_prior_mass_below(n: int, beta: int) -> F:
    """Finite unnormalized Dirichlet mass; no fabricated zeta tail certainty."""
    check_beta(beta)
    if type(n) is not int or n<1:
        raise ValueError("positive finite cutoff")
    return sum((F(1,k**beta) for k in range(1,n+1)),F(0))


def exact_tail_integral_bracket(n: int, beta: int) -> tuple[F,F]:
    """Integral-test bounds for tail sum_{k>n}k^-beta.

    lower = (n+1)^(1-beta)/(beta-1), upper = n^(1-beta)/(beta-1)
    """
    check_beta(beta)
    if type(n) is not int or n<1:
        raise ValueError("positive n required")
    return (F(1,(beta-1)*(n+1)**(beta-1)),F(1,(beta-1)*n**(beta-1)))


@dataclass(frozen=True)
class ZetaSourcePassport:
    source: str
    beta: int
    primes: tuple[int, ...]
    def __post_init__(self) -> None:
        if self.source!=SOURCE:
            raise ValueError("unaligned source identifier")
        check_beta(self.beta)
        prime_set(self.primes)
    @property
    def partition(self)->F:
        return finite_euler_partition(self.primes,self.beta)
    def probability(self,n:int)->F:
        return smooth_probability(n,self.primes,self.beta)
    def regeneration(self,n:int,p:int)->F:
        return regenerated_probability(n,p,self.primes,self.beta)
