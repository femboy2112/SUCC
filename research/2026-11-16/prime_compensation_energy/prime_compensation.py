"""Exact finite-stage prime compensation and zero-seeded BBP sieve joining.

Mathematical scope: finitely many *authenticated* rational primes, s=-1
and a separate s=2 insertion register. No global convergence or RH claim.

This module intentionally does not import the PPN draft: it re-derives
finite formulae so the complementary audit has an independent implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd, isqrt, prod
from typing import Mapping


ZETA_MINUS_ONE = Fraction(-1, 12)


def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("integer required")
    if n < 2:
        return False
    return not any(n % d == 0 for d in range(2, isqrt(n) + 1))


def validate_primes(primes) -> tuple[int, ...]:
    p = tuple(primes)
    if len(set(p)) != len(p):
        raise ValueError("prime labels must be distinct")
    if not all(is_prime(v) for v in p):
        raise ValueError("source labels must be genuine rational primes")
    return p


def Q_from_primes(primes) -> int:
    return prod(validate_primes(primes))


def sieve_projector(n: int, primes) -> int:
    if n < 1 or type(n) is not int:
        raise ValueError("positive integer state required")
    ps = validate_primes(primes)
    return int(all(n % p != 0 for p in ps))


def signed_path_sum(n: int, primes) -> int:
    ps = validate_primes(primes)
    divisors = [p for p in ps if n % p == 0]
    total = 0
    for k in range(len(divisors) + 1):
        total += (-1)**k * sum(1 for _ in combinations(divisors, k))
    return total


def new_prime_predicate(n: int) -> int:
    if n < 2:
        return 0
    return sieve_projector(n, [p for p in range(2, isqrt(n) + 1) if is_prime(p)])


def bernoulli_two(t: Fraction) -> Fraction:
    return t*t - t + Fraction(1, 6)


def euler_minus_one(primes) -> Fraction:
    return prod((Fraction(1, 1-p) for p in validate_primes(primes)), start=Fraction(1))


def hurwitz_residue_minus_one(primes) -> Fraction:
    Q = Q_from_primes(primes)
    return -Fraction(Q, 2) * sum(
        (bernoulli_two(Fraction(a, Q)) for a in range(1, Q+1) if gcd(a, Q) == 1),
        Fraction(0))


def coprime_residue_from_factors(primes) -> Fraction:
    result = ZETA_MINUS_ONE
    for p in validate_primes(primes):
        result *= (1-p)
    return result


def chi_at(p: int, s: int) -> Fraction:
    if not is_prime(p):
        raise ValueError("genuine prime required")
    if s not in (-1, 2):
        raise ValueError("exact rational calibration available only at s=-1 or 2")
    return Fraction(1) - (Fraction(p) if s == -1 else Fraction(1, p*p))


def normalized_mixed(p: int, s: int) -> Fraction:
    chi = chi_at(p, s)
    return (1/chi-1)*(chi-1)


def normalized_linear(p: int, s: int) -> Fraction:
    chi = chi_at(p, s)
    return (1/chi-1)+(chi-1)


def signed_path_action(primes) -> Fraction:
    return sum((normalized_mixed(p, -1) for p in validate_primes(primes)), Fraction(0))


def prime_transport_pair(e: Fraction, r: Fraction, p: int, s: int=-1):
    chi = chi_at(p, s)
    return (e / chi, r * chi)


def add_formal(a: Mapping[str, Fraction], b: Mapping[str, Fraction],
               c: Fraction=Fraction(1)) -> dict[str, Fraction]:
    out = dict(a)
    for k,v in b.items():
        out[k] = out.get(k, Fraction(0)) + c*v
    return {k:v for k,v in out.items() if v}


def scale_formal(a: Mapping[str, Fraction], c: Fraction) -> dict[str, Fraction]:
    return {k:c*v for k,v in a.items() if c*v}


@dataclass(frozen=True)
class PrimeJetMinusOne:
    """E,R and exact first jets in formal symbols zeta_prime, log(p).

    dE and dR are coefficient maps, never numerical approximations to logs.
    """
    E: Fraction
    R: Fraction
    dE: Mapping[str, Fraction]
    dR: Mapping[str, Fraction]

    @staticmethod
    def root() -> "PrimeJetMinusOne":
        return PrimeJetMinusOne(Fraction(1), ZETA_MINUS_ONE, {}, {"zeta_prime":Fraction(1)})

    def insert(self, p: int) -> "PrimeJetMinusOne":
        chi = chi_at(p, -1)
        chip = {f"log_{p}": Fraction(p)}
        e = self.E/chi
        r = self.R*chi
        de = add_formal(scale_formal(self.dE, 1/chi),
                        scale_formal(chip, -self.E/(chi*chi)))
        dr = add_formal(scale_formal(self.dR, chi),
                        scale_formal(chip, self.R))
        return PrimeJetMinusOne(e,r,de,dr)

    def invariant_jet(self) -> dict[str, Fraction]:
        return add_formal(scale_formal(self.dE,self.R),
                          scale_formal(self.dR,self.E))


def bbp_forcing(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer n required")
    return (Fraction(4,8*n-7)-Fraction(2,8*n-4)
            -Fraction(1,8*n-3)-Fraction(1,8*n-2))


def bbp_carry_sign(n: int) -> int:
    if type(n) is not int or n < 0:
        raise ValueError("n must be nonnegative")
    u = Fraction(0)
    for j in range(1,n+1):
        u = 16*u + bbp_forcing(j)
    c = u.numerator//u.denominator
    return 1 if (c % 4) in (0,3) else -1


def bbp_joint_shell(start: int, length: int, primes):
    """Return (density of coprime clock, signed joining, selected clock density).

    All terms are rational; complete BBP Weyl phase is intentionally absent.
    """
    if type(start) is not int or start < 1 or type(length) is not int or length < 1:
        raise ValueError("positive shell start and length required")
    ps = validate_primes(primes)
    a = 0
    j = 0
    u = Fraction(0)
    for n in range(1, start+length):
        u=16*u+bbp_forcing(n)
        if n < start: continue
        c=u.numerator//u.denominator
        sig=1 if c % 4 in (0,3) else -1
        rho=int(all(n%p for p in ps))
        a += rho
        j += rho*sig
    return (Fraction(a,length), Fraction(j,length), Fraction(a-j,2*length))


# PCE-11: exact fictitious-force / forgetting calibration.
def boost_coeffs_minus_one(p: int) -> tuple[Fraction, Fraction]:
    """Return cosh(log(p-1)), sinh(log(p-1)), exactly and without logs.

    The declared insertion chart is -B(log(p-1)); it is *not* a
    physical Lorentz boost and the sign -I is a separate discrete flip.
    """
    if not is_prime(p):
        raise ValueError("genuine prime required")
    a = Fraction(p-1)
    return ((a + 1/a)/2, (a - 1/a)/2)


def signed_boost_minus_one(u: Fraction, v: Fraction, p: int) -> tuple[Fraction, Fraction]:
    """Source-defined signed O(1,1) presentation map (u,v) -> -B(t_p)(u,v)."""
    c, s = boost_coeffs_minus_one(p)
    return (-c*u + s*v, s*u - c*v)


def projected_two_prime_paths(u: Fraction, p: int, q: int) -> tuple[Fraction, Fraction, Fraction]:
    """Return (full, forget-after-first, gap) for a declared P/J observer.

    P(u,v)=u and J(u)=(u,0).  J is a *chosen ambient linear
    calibration* and is not a section of the source hyperbola ER=-1/12.
    Distinct genuine primes p,q must be inserted.
    """
    if p == q:
        raise ValueError("prime insertion labels must be distinct")
    # Validation occurs through both signed boosts.
    a, b = signed_boost_minus_one(Fraction(u), Fraction(0), p)
    full, _ = signed_boost_minus_one(a, b, q)
    truncated, _ = signed_boost_minus_one(a, Fraction(0), q)
    return full, truncated, full - truncated


def projected_two_prime_gap(u: Fraction, p: int, q: int) -> Fraction:
    return projected_two_prime_paths(u, p, q)[2]
