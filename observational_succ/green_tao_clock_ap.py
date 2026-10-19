"""Exact synchronized prime clocks and finite Green--Tao-style AP witnesses.

The *W-trick* and dense-primes Green--Tao theorem are EXTERNAL mathematical
results; this module provides deterministic finite arithmetic checks and exact
local obstruction/character calculations. It proves neither the Green--Tao
theorem nor fixed-gap prime-tuple conjectures, ABC, RH or Weil positivity.

All integer caps limit executable resources, never universal mathematics.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, isqrt, prod


MAX_PRIME_INPUT = 10**12
MAX_CLOCK = 100_000
MAX_CLOCKS = 10
MAX_GRID_LENGTH = 8
MAX_FINITE_SEARCH_ENDPOINT = 2_000


class ClockAPError(ValueError):
    """Invalid genuine-prime clock, progression, or explicit compute budget."""


def _typed(n: int, label: str, low: int, high: int) -> int:
    if type(n) is not int or not low <= n <= high:
        raise ClockAPError(f"{label} must be an integer in {low}..{high}")
    return n


def is_prime_exact(n: int) -> bool:
    """Independent bounded primality by complete trial division."""
    _typed(n, "primality input", 1, MAX_PRIME_INPUT)
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def small_primes(bound: int) -> tuple[int, ...]:
    _typed(bound, "small prime ceiling", 1, 1000)
    return tuple(n for n in range(2, bound + 1) if is_prime_exact(n))


def clock_check(clocks: tuple[int, ...]) -> tuple[int, ...]:
    if type(clocks) is not tuple or not 1 <= len(clocks) <= MAX_CLOCKS:
        raise ClockAPError("require nonempty bounded tuple of genuine clocks")
    if clocks != tuple(sorted(set(clocks))):
        raise ClockAPError("distinct prime clocks must be strictly increasing")
    if any(type(q) is not int or q > MAX_CLOCK or not is_prime_exact(q)
           for q in clocks):
        raise ClockAPError("nonprime or oversized clock source rejected")
    if prod(clocks) > MAX_PRIME_INPUT:
        raise ClockAPError("clock product exceeds finite integer budget")
    return clocks


def prime_clock_progression(first: int, increment: int, count: int) -> tuple[int, ...]:
    _typed(first, "first clock prime", 2, MAX_CLOCK)
    _typed(increment, "clock step", 1, MAX_CLOCK)
    _typed(count, "clock count", 2, MAX_CLOCKS)
    clocks = tuple(first + j * increment for j in range(count))
    return clock_check(clocks)


@dataclass(frozen=True)
class WheelArithmetic:
    clocks: tuple[int, ...]
    modulus: int
    totient: int
    first_return: int
    wheel_enrichment: Fraction
    relative_prime_density: Fraction
    faithful_character_multiplier: int
    minimum_distinguishing_bits: int


def wheel_arithmetic(clocks: tuple[int, ...]) -> WheelArithmetic:
    clocks = clock_check(clocks)
    W = prod(clocks)
    totient = prod(q - 1 for q in clocks)
    h = sum(W // q for q in clocks) % W
    if gcd(h, W) != 1:
        raise AssertionError("CRT composite character unexpectedly nonfaithful")
    return WheelArithmetic(
        clocks, W, totient, W + 1, Fraction(W, totient),
        Fraction(1, totient), h, (W - 1).bit_length())


def exact_character_label(n: int, clocks: tuple[int, ...]) -> tuple[int, int]:
    """Faithful integer label for product of declared standard clock characters.

    The complex character is exp(2*pi*i*label/W). No floating-point phase
    equality is used for a primality, lock, or certification decision.
    """
    _typed(n, "integer being clocked", 1, MAX_PRIME_INPUT)
    wheel = wheel_arithmetic(clocks)
    return ((n - 1) * wheel.faithful_character_multiplier % wheel.modulus,
            wheel.modulus)


def all_clocks_at_one(n: int, clocks: tuple[int, ...]) -> bool:
    _typed(n, "clocked integer", 1, MAX_PRIME_INPUT)
    wheel = wheel_arithmetic(clocks)
    locked = all(n % q == 1 for q in wheel.clocks)
    if locked != (exact_character_label(n, clocks)[0] == 0):
        raise AssertionError("CRT phase compression lost a residue")
    return locked


def local_step_requirement(clocks: tuple[int, ...], progression_length: int) -> int:
    """Necessary multiplier-step divisor for a long-enough prime progression.

    For p_j=1+W(t+j*d), all prime endpoints strictly > progression_length:
    each prime r<=length not in W must divide d, or one endpoint is
    divisible by r. This is a LOCAL obstruction, not a sufficiency theorem.
    """
    wheel = wheel_arithmetic(clocks)
    _typed(progression_length, "number of prime endpoints", 2, MAX_GRID_LENGTH)
    return prod(r for r in small_primes(progression_length)
                if wheel.modulus % r != 0)


@dataclass(frozen=True)
class LocalPrimeFactor:
    prime: int
    forbidden_start_classes: int
    admissible_start_classes: int
    singular_series_factor: Fraction


def local_prime_factors(clocks: tuple[int, ...], count: int,
                        multiplier_step: int, cutoff: int = 31
                        ) -> tuple[LocalPrimeFactor, ...]:
    """Exact local obstruction factors, NOT a proved prime-pattern asymptotic.

    For a varying start t, the linear forms 1+W(t+j*d), 0<=j<count,
    have nu_r distinct roots mod r. Classical Hardy--Littlewood would
    predict a full singular series, but finite positive factors do not
    prove infinitely many fixed-d prime tuples.
    """
    wheel = wheel_arithmetic(clocks)
    _typed(count, "progression length", 2, MAX_GRID_LENGTH)
    _typed(multiplier_step, "multiplier step", 1, MAX_FINITE_SEARCH_ENDPOINT)
    _typed(cutoff, "prime cutoff", 2, 997)
    local = []
    for r in small_primes(cutoff):
        if wheel.modulus % r == 0:
            nu = 0
        elif multiplier_step % r == 0:
            nu = 1
        else:
            nu = min(count, r)
        local.append(LocalPrimeFactor(
            r, nu, r - nu,
            Fraction(r - nu, r) * Fraction(r, r - 1) ** count))
    return tuple(local)


@dataclass(frozen=True)
class PrimeClockGrid:
    """Two verified arithmetic progressions of genuine primes, with all-one incidence."""

    clock_primes: tuple[int, ...]
    endpoint_primes: tuple[int, ...]
    clock_step: int
    endpoint_step: int
    wheel_modulus: int
    multiplier_start: int
    multiplier_step: int
    local_minimum_step: int

    @property
    def incidence_count(self) -> int:
        return len(self.clock_primes) * len(self.endpoint_primes)


def verify_prime_clock_grid(clocks: tuple[int, ...], start: int, step: int,
                            count: int) -> PrimeClockGrid:
    """Exact finite prime rectangle, never a claimed universal construction."""
    wheel = wheel_arithmetic(clocks)
    if len(clocks) < 2 or any(
            clocks[j+1] - clocks[j] != clocks[1] - clocks[0]
            for j in range(len(clocks) - 1)):
        raise ClockAPError("clock primes themselves must form an arithmetic progression")
    _typed(start, "starting wheel multiplier", 1, MAX_FINITE_SEARCH_ENDPOINT)
    _typed(step, "step between wheel multipliers", 1, MAX_FINITE_SEARCH_ENDPOINT)
    _typed(count, "endpoint count", 2, MAX_GRID_LENGTH)
    last = 1 + wheel.modulus * (start + (count - 1) * step)
    _typed(last, "last prime endpoint", 2, MAX_PRIME_INPUT)
    endpoints = tuple(1 + wheel.modulus * (start + j * step)
                      for j in range(count))
    if endpoints[0] <= max(clocks) or endpoints[0] <= count:
        raise ClockAPError("endpoint primes must exceed clocks and progression length")
    required = local_step_requirement(clocks, count)
    if step % required != 0:
        raise ClockAPError("prime progression violates a necessary small-prime gate")
    if not all(is_prime_exact(p) for p in endpoints):
        raise ClockAPError("one or more purported prime endpoints is composite")
    if not all(all_clocks_at_one(p, clocks) for p in endpoints):
        raise AssertionError("verified affine wheel failed exact clock phase")
    return PrimeClockGrid(clocks, endpoints, clocks[1] - clocks[0],
                          wheel.modulus * step, wheel.modulus,
                          start, step, required)


def search_first_grid(clocks: tuple[int, ...], count: int,
                      endpoint_multiplier_cap: int) -> PrimeClockGrid | None:
    """Search all grids by increasing LAST multiplier, then increasing d.

    At this fixed budget the returned grid has minimum greatest endpoint
    among all legal starts/steps for this clock set and target length.
    It does NOT bound the first such grid for any other clocks or length.
    """
    wheel = wheel_arithmetic(clocks)
    _typed(count, "endpoint length", 2, MAX_GRID_LENGTH)
    _typed(endpoint_multiplier_cap, "last multiplier cap", 2,
           MAX_FINITE_SEARCH_ENDPOINT)
    required = local_step_requirement(clocks, count)
    for last_t in range(2, endpoint_multiplier_cap + 1):
        last_p = 1 + wheel.modulus * last_t
        if last_p > MAX_PRIME_INPUT:
            break
        if not is_prime_exact(last_p):
            continue
        for d in range(required, (last_t - 1) // (count - 1) + 1, required):
            start = last_t - (count - 1) * d
            if start < 1:
                continue
            endpoints = tuple(1 + wheel.modulus * (start + j * d)
                              for j in range(count))
            if endpoints[0] <= max(clocks) or endpoints[0] <= count:
                continue
            if all(is_prime_exact(p) for p in endpoints[:-1]):
                return verify_prime_clock_grid(clocks, start, d, count)
    return None


def prime_predecessor_factorization(p: int) -> tuple[tuple[int, int], ...]:
    """Exact multiplicity support of p-1; admits only proven finite primes."""
    _typed(p, "candidate", 2, MAX_PRIME_INPUT)
    if not is_prime_exact(p):
        raise ClockAPError("predecessor chart requires an actual prime")
    n = p - 1
    output = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            output.append((d, k))
        d = 3 if d == 2 else d + 2
    if n > 1:
        output.append((n, 1))
    return tuple(output)


def exact_factorization(n: int) -> tuple[tuple[int, int], ...]:
    """All prime exponents of any positive bounded n, without primality assumptions."""
    _typed(n, "integer being factored", 1, MAX_PRIME_INPUT)
    output = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            output.append((d, k))
        d = 3 if d == 2 else d + 2
    if n > 1:
        output.append((n, 1))
    return tuple(output)


def exact_rad(n: int) -> int:
    return prod(q for q, _ in exact_factorization(n))


def flat_rad_ladder_condition(radical: int, length: int) -> bool:
    """iff for all j=1,...,length: rad(radical*j)=radical.

    This pure factorization condition DOES NOT assert that any 1+j*radical
    is prime. Equivalence needs squarefree radical and every prime <=length.
    """
    _typed(radical, "proposed fixed radical", 1, MAX_PRIME_INPUT)
    _typed(length, "ladder length", 2, MAX_GRID_LENGTH)
    factors = exact_factorization(radical)
    support = {q for q, _ in factors}
    return all(e == 1 for _, e in factors) and all(
        q in support for q in small_primes(length))


@dataclass(frozen=True)
class FlatRadPrimeLadder:
    """Finite source-certified prime ladder, constant RAD and linear RIS."""
    radical: int
    prime_endpoints: tuple[int, ...]
    radical_factors: tuple[tuple[int, int], ...]
    residual_values: tuple[int, ...]

    @property
    def length(self) -> int:
        return len(self.prime_endpoints)


def verify_flat_rad_prime_ladder(radical: int, length: int
                                 ) -> FlatRadPrimeLadder:
    """Check ALL primes p_j=1+j*radical, RAD(p_j-1)=R, RIS(p_j-1)=j."""
    _typed(radical, "fixed radical", 2, MAX_PRIME_INPUT)
    _typed(length, "ladder length", 2, MAX_GRID_LENGTH)
    _typed(1+radical*length, "largest prime endpoint", 3, MAX_PRIME_INPUT)
    if not flat_rad_ladder_condition(radical, length):
        raise ClockAPError("flat RAD needs squarefree R containing every prime <=length")
    endpoints = tuple(1+j*radical for j in range(1, length+1))
    if not all(is_prime_exact(p) for p in endpoints):
        raise ClockAPError("locally admissible flat RAD does not guarantee prime endpoints")
    for j in range(1, length+1):
        if exact_rad(j*radical) != radical or (j*radical)//radical != j:
            raise AssertionError("flat RAD/RIS witness violated factorization theorem")
    return FlatRadPrimeLadder(radical, endpoints,
                              exact_factorization(radical),
                              tuple(range(1, length+1)))


def search_flat_rad_ladder(length: int, radical_cap: int
                           ) -> FlatRadPrimeLadder | None:
    """Exhaustive bounded first RAD; no claim of unbounded or infinite existence.

    Only multiples of squarefree product of genuine primes <=length need
    examination, by the independently proved flat-RAD support criterion.
    """
    _typed(length, "prime ladder length", 2, MAX_GRID_LENGTH)
    _typed(radical_cap, "bounded radical search cap", 2, 1_000_000)
    baseline = prod(small_primes(length))
    for R in range(baseline, radical_cap+1, baseline):
        if not flat_rad_ladder_condition(R, length):
            continue
        if all(is_prime_exact(1+j*R) for j in range(1, length+1)):
            return verify_flat_rad_prime_ladder(R, length)
    return None


@dataclass(frozen=True)
class MaynardClockFamily:
    """Only finite algebraic admissibility; prime-rich infinitude is EXTERNAL."""
    prescribed_clocks: tuple[int, ...]
    form_count: int
    anchor_modulus: int
    linear_coefficients: tuple[int, ...]


def maynard_clock_family(clocks: tuple[int, ...], form_count: int
                         ) -> MaynardClockFamily:
    """Construct exact finite admissible forms 1+j*A*t, j=1..K.

    Each finite prime r has witness t=0 mod r making ALL forms 1 mod r.
    That local theorem is elementary; MAYNARD--TAO external theory is needed
    to assert infinitely many t with >=m prime forms for sufficient K.
    """
    wheel = wheel_arithmetic(clocks)
    _typed(form_count, "finite affine family length", 2, 12)
    required = set(wheel.clocks) | set(small_primes(form_count))
    anchor = prod(sorted(required))
    _typed(anchor * form_count, "largest affine coefficient", 2, MAX_PRIME_INPUT)
    return MaynardClockFamily(wheel.clocks, form_count, anchor,
                              tuple(j*anchor for j in range(1, form_count+1)))


@dataclass(frozen=True)
class ObservedClockFiber:
    """Exact data for one t, never an asymptotic proof or prime-count guarantee."""
    anchor_modulus: int
    parameter: int
    step_R: int
    full_radical: int
    full_ris: int
    endpoints: tuple[int, ...]
    prime_positions: tuple[int, ...]
    ris_values: tuple[int, ...]


def observe_maynard_clock_fiber(family: MaynardClockFamily,
                                parameter: int) -> ObservedClockFiber:
    if not isinstance(family, MaynardClockFamily):
        raise ClockAPError("family must be a source-validated Maynard clock chart")
    _typed(parameter, "positive affine parameter", 1, MAX_PRIME_INPUT)
    R = family.anchor_modulus * parameter
    _typed(1 + R * family.form_count, "largest endpoint", 2, MAX_PRIME_INPUT)
    base_radical = exact_rad(R)
    base_ris = R // base_radical
    endpoints = tuple(1+j*R for j in range(1, family.form_count+1))
    for j, p in enumerate(endpoints, start=1):
        if exact_rad(p-1) != base_radical or (p-1) // base_radical != j*base_ris:
            raise AssertionError("Maynard-clock support or depth identity failed")
    return ObservedClockFiber(
        family.anchor_modulus, parameter, R, base_radical, base_ris,
        endpoints,
        tuple(j for j, p in enumerate(endpoints, start=1)
              if is_prime_exact(p)),
        tuple(j*base_ris for j in range(1, family.form_count+1)),
    )
