"""Exact prime-clock phase probes and backward primorial/factorial searches.

Mathematical source is declared positive-integer arithmetic. Each result is a
finite computation; the infinite existence of phase-locked primes requires
Dirichlet's theorem, not a finite test. Prime-clock phases are residues, NOT
Hilbert/Weil phases, electromagnetic signals, or quantum amplitudes.

The ambient bound protects runtime and is NOT a hypothesis of paper theorems.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial, isqrt, prod


MAX_CANDIDATE = 250_000_000
MAX_PRIME_PREFIX = 11
MAX_FACTORIAL = 20
MAX_CLOCK_COUNT = 100
MAX_SEARCH_MULTIPLIER = 2_000


class PhaseClockError(ValueError):
    """Invalid source integer, composite clock, or excessive resource demand."""


def _integer(n: int, label: str, low: int, high: int) -> int:
    if type(n) is not int or not low <= n <= high:
        raise PhaseClockError(f"{label}: exact integer in [{low}, {high}] required")
    return n


def _prime_unbounded(n: int) -> bool:
    if type(n) is not int or n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def prime(n: int) -> bool:
    """Bounded but exhaustive trial-division primality oracle."""
    _integer(n, "primality target", 1, MAX_CANDIDATE)
    return _prime_unbounded(n)


def primes_up_to(limit: int) -> tuple[int, ...]:
    _integer(limit, "clock horizon", 1, 1_000_000)
    table = bytearray(b"\x01") * (limit + 1)
    table[:2] = b"\x00\x00"
    for d in range(2, isqrt(limit) + 1):
        if table[d]:
            table[d * d:limit + 1:d] = b"\x00" * ((limit - d * d) // d + 1)
    return tuple(i for i in range(2, limit + 1) if table[i])


def prime_prefix(k: int) -> tuple[int, ...]:
    """The first k genuine prime moduli, not an arbitrary picked clock family."""
    _integer(k, "prime-prefix depth", 1, MAX_PRIME_PREFIX)
    found = []
    p = 2
    while len(found) < k:
        if _prime_unbounded(p):
            found.append(p)
        p += 1
    return tuple(found)


def _clock_check(clocks: tuple[int, ...], target: int | None = None) -> tuple[int, ...]:
    if type(clocks) is not tuple or not 1 <= len(clocks) <= MAX_CLOCK_COUNT:
        raise PhaseClockError("nonempty tuple of at most 100 prime clocks required")
    if clocks != tuple(sorted(set(clocks))):
        raise PhaseClockError("clock moduli must be distinct and ascending")
    if any(not _prime_unbounded(q) or q > 1_000_000 for q in clocks):
        raise PhaseClockError("only genuine bounded prime clocks are accepted")
    if target is not None and clocks[-1] >= target:
        raise PhaseClockError("new-prime sample must exceed every observed prime clock")
    return clocks


def primorial(k: int) -> int:
    """First k-prime wheel modulus. No primality claim for wheel + 1."""
    return prod(prime_prefix(k))


def factorial_prime_power_profile(m: int) -> tuple[tuple[int, int], ...]:
    """Legendre exponents v_q(m!) for q<=m, including the extra p-adic digits."""
    _integer(m, "factorial stage", 2, MAX_FACTORIAL)
    powers = []
    for q in primes_up_to(m):
        e, d = 0, q
        while d <= m:
            e += m // d
            d *= q
        powers.append((q, e))
    return tuple(powers)


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    _integer(n, "factorization input", 1, MAX_CANDIDATE)
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            factors.append((d, e))
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


@dataclass(frozen=True)
class PrimeClockProfile:
    prime: int
    predecessor: int
    factorization: tuple[tuple[int, int], ...]
    radical: int
    residual: int
    synchronized_primes: tuple[int, ...]
    prefix_depth: int

    @property
    def synchronized_count(self) -> int:
        return len(self.synchronized_primes)


def prime_clock_profile(p: int) -> PrimeClockProfile:
    """Exact phase-1 clock set: supp(p-1), including all primes below p."""
    _integer(p, "candidate prime", 2, MAX_CANDIDATE)
    if not _prime_unbounded(p):
        raise PhaseClockError("clock profile is reserved for genuine primes")
    factors = factorization(p - 1)
    synced = tuple(q for q, _ in factors)
    depth = 0
    if p >= 3:
        while depth < MAX_PRIME_PREFIX:
            q = prime_prefix(depth + 1)[-1]
            if (p - 1) % q != 0:
                break
            depth += 1
        # A depth cap must not silently be returned as a mathematically complete depth.
        if depth == MAX_PRIME_PREFIX and (p - 1) % prime_prefix(MAX_PRIME_PREFIX)[-1] == 0:
            # Under the integer runtime ceiling, the product of the first 11
            # primes already exceeds p-1; this path is unreachable here.
            raise AssertionError("prime-prefix depth exceeded budget")
    radical = prod(synced)
    return PrimeClockProfile(p, p - 1, factors, radical,
                             (p - 1) // radical, synced, depth)


@dataclass(frozen=True)
class PhaseWindow:
    prime: int
    clocks: tuple[int, ...]
    residues: tuple[int, ...]
    synchronized: tuple[int, ...]
    residue_sum: int
    forward_slip_sum: int
    mean_normalized_forward_slip: Fraction
    mean_normalized_circular_slip: Fraction

    @property
    def perfectly_locked(self) -> bool:
        return self.forward_slip_sum == 0


def phase_window(p: int, clocks: tuple[int, ...]) -> PhaseWindow:
    """Raw residue sum and two normalized phase distances on one FIXED window.

    The circular distance is a proxy for phase geometry, not a Fourier phase
    transport and not an analytically inferred probability.
    """
    _integer(p, "candidate", 2, MAX_CANDIDATE)
    _clock_check(clocks, p)
    if not _prime_unbounded(p):
        raise PhaseClockError("phase ranking requires a verified prime")
    residues = tuple(p % q for q in clocks)
    slips = tuple((p - 1) % q for q in clocks)
    synced = tuple(q for q, slip in zip(clocks, slips) if slip == 0)
    normalized = sum((Fraction(t, q) for t, q in zip(slips, clocks)), Fraction())
    circular = sum((Fraction(min(t, q - t), q) for t, q in zip(slips, clocks)),
                   Fraction())
    return PhaseWindow(p, clocks, residues, synced, sum(residues), sum(slips),
                       normalized / len(clocks), circular / len(clocks))


def aligned_primes(k: int, max_multiplier: int = 30,
                   max_count: int = 5) -> tuple[tuple[int, int], ...]:
    """Return (t, p) only after exact primality check of p=t*M_k+1."""
    m = primorial(k)
    _integer(max_multiplier, "multiplier budget", 1, MAX_SEARCH_MULTIPLIER)
    _integer(max_count, "result budget", 1, 100)
    output = []
    for t in range(1, max_multiplier + 1):
        candidate = m * t + 1
        if candidate > MAX_CANDIDATE:
            break
        if _prime_unbounded(candidate):
            output.append((t, candidate))
            if len(output) == max_count:
                break
    return tuple(output)


def euclid_witness(k: int) -> tuple[int, bool, int | None]:
    """M_k+1 primality and an exact proper-factor witness if composite."""
    n = primorial(k) + 1
    _integer(n, "Euclid candidate", 2, MAX_CANDIDATE)
    if _prime_unbounded(n):
        return (n, True, None)
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return (n, False, d)
    raise AssertionError("trial division did not resolve compositeness")


def factorial_witness(m: int) -> tuple[int, bool, int | None]:
    """m!+1 and a proper factor, if in finite test range."""
    _integer(m, "factorial stage", 2, MAX_FACTORIAL)
    n = factorial(m) + 1
    _integer(n, "factorial candidate", 2, MAX_CANDIDATE)
    if _prime_unbounded(n):
        return (n, True, None)
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return (n, False, d)
    raise AssertionError("trial division did not resolve compositeness")


def factorial_locked(p: int, m: int) -> bool:
    """Does prime p lie in the genuine progression 1 mod m!?"""
    _integer(m, "factorial stage", 2, MAX_FACTORIAL)
    _integer(p, "candidate prime", 2, MAX_CANDIDATE)
    if not _prime_unbounded(p):
        raise PhaseClockError("factorial phase requires a genuine prime")
    return (p - 1) % factorial(m) == 0


def ghost_two_adic_pair(k: int, max_multiplier: int = 100) -> tuple[int, int]:
    """Find primes with identical all-first-digit wheel phase but different mod 4.

    Finite search may fail on budget. Dirichlet (external theorem) ensures
    existence without a uniform search bound.
    """
    _integer(max_multiplier, "ghost multiplier", 1, MAX_SEARCH_MULTIPLIER)
    modulus = primorial(k)
    first = {}
    for t in range(1, max_multiplier + 1):
        p = t * modulus + 1
        if p > MAX_CANDIDATE:
            break
        if _prime_unbounded(p):
            first.setdefault(p % 4, p)
            if 1 in first and 3 in first:
                return first[1], first[3]
    raise PhaseClockError("no two-adic ghost pair found within finite search budget")


def sqrt_window_perfect(p: int) -> bool:
    """Exact test for all q<=sqrt(p) reading 1, for a verified bounded prime."""
    _integer(p, "candidate prime", 2, MAX_CANDIDATE)
    if not _prime_unbounded(p):
        raise PhaseClockError("sqrt-window question applies to prime inputs only")
    return all((p - 1) % q == 0 for q in primes_up_to(isqrt(p)))


def backward_factorial_primes(m: int, max_multiplier: int = 40,
                              max_count: int = 5) -> tuple[tuple[int, int], ...]:
    """Prime witnesses p=t*m!+1. Empty result is only a finite search failure."""
    _integer(m, "factorial stage", 2, MAX_FACTORIAL)
    _integer(max_multiplier, "multiplier", 1, MAX_SEARCH_MULTIPLIER)
    _integer(max_count, "result cap", 1, 100)
    modulus = factorial(m)
    result = []
    for t in range(1, max_multiplier + 1):
        p = t * modulus + 1
        if p > MAX_CANDIDATE:
            break
        if _prime_unbounded(p):
            result.append((t, p))
            if len(result) == max_count:
                break
    return tuple(result)


@dataclass(frozen=True)
class FixedWindowLaw:
    """Exact CRT law on reduced residue classes; prime-limit law uses PNT-AP.

    The rational coefficients are derived by finite polynomial multiplication
    across genuine coprime prime moduli, NOT by fitting a finite prime sample.
    """
    clocks: tuple[int, ...]
    modulus: int
    reduced_residue_count: int
    residue_sum_distribution: tuple[tuple[int, Fraction], ...]
    sync_count_distribution: tuple[tuple[int, Fraction], ...]
    expected_residue_sum: Fraction
    variance_residue_sum: Fraction
    expected_sync_count: Fraction
    variance_sync_count: Fraction
    all_locked_fraction: Fraction


def fixed_window_crt_law(clocks: tuple[int, ...]) -> FixedWindowLaw:
    """Two exact finite distributions; asymptotic prime use requires PNT-AP.

    Only modest windows are expanded into full rational polynomials. This
    deliberately does not let the modulus grow with the prime search horizon.
    """
    _clock_check(clocks)
    if any(q > 31 for q in clocks):
        raise PhaseClockError("polynomial enumeration admits clocks <=31")
    reduced = prod(q - 1 for q in clocks)
    if reduced > 200_000:
        raise PhaseClockError("too many CRT reduced residue vectors")
    raw = {0: 1}
    locked = {0: 1}
    for q in clocks:
        next_raw = {}
        for total, count in raw.items():
            for r in range(1, q):
                next_raw[total + r] = next_raw.get(total + r, 0) + count
        raw = next_raw
        next_locked = {}
        for total, count in locked.items():
            next_locked[total] = next_locked.get(total, 0) + count * (q - 2)
            next_locked[total + 1] = next_locked.get(total + 1, 0) + count
        locked = next_locked
    if sum(raw.values()) != reduced or sum(locked.values()) != reduced:
        raise AssertionError("finite CRT distribution failed normalization")
    residue_distribution = tuple(
        (s, Fraction(count, reduced)) for s, count in sorted(raw.items()) if count)
    lock_distribution = tuple(
        (s, Fraction(count, reduced)) for s, count in sorted(locked.items()) if count)
    residue_expectation = sum((Fraction(q, 2) for q in clocks), Fraction())
    residue_variance = sum((Fraction(q * (q - 2), 12) for q in clocks), Fraction())
    sync_expectation = sum((Fraction(1, q - 1) for q in clocks), Fraction())
    sync_variance = sum((Fraction(q - 2, (q - 1)**2) for q in clocks), Fraction())
    all_locked = Fraction(1, reduced)
    return FixedWindowLaw(clocks, prod(clocks), reduced, residue_distribution,
                          lock_distribution, residue_expectation, residue_variance,
                          sync_expectation, sync_variance, all_locked)
