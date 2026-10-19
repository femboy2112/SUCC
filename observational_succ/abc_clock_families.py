"""ABC radical/ris energy, source-labelled prime clocks, and exact finite envelopes.

New-to-project elementary arithmetic. No abc conjecture, Weil sign, or RH proof.
The clock probabilities are conditional p-adic Haar proportions, NOT
independence assertions for growing sets of primes in bounded integer boxes.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import gcd, isqrt


class ABCClockError(ValueError):
    """Inadmissible primitive triple, prime, or finite search request."""


def prime(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


@lru_cache(maxsize=32768)
def prime_factors(n: int) -> tuple[tuple[int, int], ...]:
    """Canonical prime-power source, with n=1 represented by empty support."""
    if type(n) is not int or n < 1:
        raise ABCClockError("factorization needs a positive integer")
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            factors.append((d, k))
        d += 1 if d == 2 else 2
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def radical(n: int) -> int:
    out = 1
    for p, _ in prime_factors(n):
        out *= p
    return out


def ris(n: int) -> int:
    return n // radical(n)


def valuation(n: int, p: int) -> int:
    if type(n) is not int or n < 1 or not prime(p):
        raise ABCClockError("valuation needs n>0 and an actual prime")
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


@dataclass(frozen=True)
class ABCTriple:
    a: int
    b: int
    c: int

    def __post_init__(self) -> None:
        if any(type(n) is not int or n < 1 for n in (self.a, self.b, self.c)):
            raise ABCClockError("triple entries must be positive integers")
        if self.a + self.b != self.c or gcd(self.a, self.b) != 1:
            raise ABCClockError("a+b=c and gcd(a,b)=1 are required")

    @property
    def radical(self) -> int:
        # Pairwise coprimality follows from a+b=c, gcd(a,b)=1.
        return radical(self.a) * radical(self.b) * radical(self.c)

    @property
    def ris(self) -> int:
        return self.a * self.b * self.c // self.radical

    @property
    def width(self) -> int:
        return len(self.clock_signature())

    @property
    def depth(self) -> int:
        return sum(k-1 for _, _, k in self.clock_signature())

    def clock_signature(self) -> tuple[tuple[int, str, int], ...]:
        """(actual prime, only occupied slot, exact valuation), no ghost clocks."""
        result = []
        for slot, n in (("a", self.a), ("b", self.b), ("c", self.c)):
            result.extend((p, slot, k) for p, k in prime_factors(n))
        result.sort()
        return tuple(result)

    def family_key(self) -> tuple[int, int, int, int, int]:
        """(support width, repeated depth, occupied slot counts a,b,c)."""
        signature = self.clock_signature()
        return (len(signature), sum(k-1 for _, _, k in signature),
                *(sum(slot == s for _, slot, _ in signature) for s in "abc"))

    def abc_quality_excess(self, epsilon: Fraction) -> Fraction:
        """Exact [c/rad(abc)^(1+eps)]^denominator(eps).

        Values for different denominators require corresponding roots when
        comparing *across* epsilon, although maximizers at fixed eps are exact.
        """
        if not isinstance(epsilon, Fraction) or epsilon < 0:
            raise ABCClockError("epsilon must be a nonnegative Fraction")
        p, q = epsilon.numerator, epsilon.denominator
        return Fraction(self.c**q, self.radical**(q+p))

    def is_exceptional(self, epsilon: Fraction = Fraction(0)) -> bool:
        return self.abc_quality_excess(epsilon) > 1


def exact_local_clock(p: int, depth: int = 1) -> dict[str, Fraction]:
    """Conditional Haar law given (a,b) not both divisible by p.

    For each of a,b,c: slot_exact_k=(p-1)/((p+1)*p**k),
    slot_ge_k=p**(1-k)/(p+1), k>=1. None=(p-2)/(p+1).
    Independent across any FIXED finite set of p in the conditioned
    profinite product. This is not independence of integers a,b,c.
    """
    if not prime(p) or type(depth) is not int or depth < 1:
        raise ABCClockError("actual prime and positive valuation depth required")
    return {
        "no_occupied_slot": Fraction(p-2, p+1),
        "each_slot_occupied": Fraction(1, p+1),
        "each_slot_exact_depth": Fraction(p-1, (p+1) * p**depth),
        "each_slot_at_least_depth": Fraction(p, (p+1) * p**depth),
    }


def residue_clock_indicator(a: int, b: int, modulus: int) -> int:
    """Exact root-of-unity orthogonality value: 1 if a+b=0 mod m, else 0.

    Represents (1/m) sum_{j=0}^{m-1} exp(2*pi*i*j*(a+b)/m)
    without rounding complex roots of unity.
    """
    if any(type(n) is not int for n in (a, b, modulus)) or modulus < 1:
        raise ABCClockError("integer residues and positive modulus required")
    return int((a+b) % modulus == 0)


def prime_progression_lifts(p_minus: int, p_mid: int, p_plus: int) -> tuple[ABCTriple, ABCTriple]:
    """Linear 3-AP -> squarefree and square-completed primitive ABC triples.

    Green--Tao supplies infinitely many prime 3-APs, but is an EXTERNAL
    theorem. This local function establishes only the exact identity.
    """
    if not (all(prime(p) and p > 2 for p in (p_minus, p_mid, p_plus))
            and p_minus < p_mid < p_plus
            and p_minus + p_plus == 2*p_mid):
        raise ABCClockError("three distinct odd primes in arithmetic progression required")
    d = p_mid-p_minus
    return (ABCTriple(p_minus, p_plus, 2*p_mid),
            ABCTriple(p_minus*p_plus, d*d, p_mid*p_mid))


def radical_sieve(limit: int) -> tuple[int, ...]:
    """Exact least-prime-independent radical sieve; bound is deliberate."""
    if type(limit) is not int or not 3 <= limit <= 10000:
        raise ABCClockError("finite experiment must have 3<=limit<=10000")
    r = [1] * (limit+1)
    for p in range(2, limit+1):
        if r[p] != 1:
            continue
        for k in range(p, limit+1, p):
            r[k] *= p
    return tuple(r)


def primitive_triples(limit: int, lower_c: int = 3):
    """Exact bounded enumeration, no conclusions about unbounded ABC."""
    r = radical_sieve(limit)
    if type(lower_c) is not int or not 3 <= lower_c <= limit:
        raise ABCClockError("invalid lower bound")
    for c in range(lower_c, limit+1):
        for a in range(1, (c+1)//2):
            b = c-a
            if gcd(a, b) == 1:
                yield ABCTriple(a, b, c), r[a]*r[b]*r[c]


def finite_envelope(limit: int, epsilons: tuple[Fraction, ...], lower_c: int = 3):
    """The exact FINITE max of (c/rad^(1+eps))^den(eps).

    Grouped maxima are computed independently and checked against global;
    no missing family is assumed bounded.
    """
    if not epsilons or any(not isinstance(e, Fraction) or e < 0 or e.denominator > 32
                           for e in epsilons):
        raise ABCClockError("use a nonempty tuple of nonnegative rational epsilons (den<=32)")
    maxima = {e: (Fraction(0), None) for e in epsilons}
    families = {e: {} for e in epsilons}
    count = hits = 0
    for t, R in primitive_triples(limit, lower_c):
        count += 1
        hits += t.c > R
        key = t.family_key()
        for e in epsilons:
            v = Fraction(t.c**e.denominator, R**(e.denominator+e.numerator))
            if v > maxima[e][0]:
                maxima[e] = (v, t)
            if key not in families[e] or v > families[e][key][0]:
                families[e][key] = (v, t)
    assert all(max(val for val, _ in groups.values()) == maxima[e][0]
               for e, groups in families.items())
    return {"count": count, "hits_eps0": hits, "maxima": maxima, "families": families}
