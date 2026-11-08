"""Origin-locked BBP invariants, rational seed spectral sidebands, and digit strata.

Research-only: original four signed BBP poles; no claim about π normality.
Exact arithmetic uses fractions.Fraction. Complex spectral values are explicitly
finite numerical diagnostics, never rigorous Fourier enclosures.
"""
from __future__ import annotations

import cmath
import math
from collections import Counter
from fractions import Fraction
from typing import Callable, Iterable, Sequence

BASE = 16
Source = Callable[[int], Fraction]


def original_forcing(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("original source needs integer n>=1")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def iterate(n: int, seed: Fraction = Fraction(0), forcing: Source = original_forcing) -> Fraction:
    """Unwrapped, exact source state. The seeded integer-lift is never omitted."""
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer")
    state = Fraction(seed)
    for j in range(1, n+1):
        state = 16 * state + forcing(j)
    return state


def partial_source(m: int, forcing: Source = original_forcing) -> Fraction:
    if type(m) is not int or m < 0:
        raise ValueError("m must be a nonnegative integer")
    return sum((forcing(j) / (16 ** j) for j in range(1, m+1)), Fraction(0))


def split_completed_source(n: int, future_length: int, seed: Fraction = Fraction(0),
                           forcing: Source = original_forcing) -> Fraction:
    """Exact finite invariant: 16^-n(U_n + truncated tail)-s = partial_source(n+L).

    No π oracle, convergence premise, or floating-point approximation.
    """
    if type(n) is not int or n < 0 or type(future_length) is not int or future_length < 0:
        raise ValueError("n, future_length must be nonnegative integers")
    tail = sum((forcing(n+j) / (16 ** j) for j in range(1, future_length+1)), Fraction(0))
    return (iterate(n, seed, forcing) + tail) / (16 ** n) - Fraction(seed)


def original_tail_upper(m: int) -> Fraction:
    """For m>=1, 0 < π/16 - partial_source(m) < 16^-m/(64 m²)."""
    if type(m) is not int or m < 1:
        raise ValueError("m must be an integer >=1")
    return Fraction(1, (16 ** m) * 64 * m * m)


def certified_hex_digits(m: int, depth: int) -> str:
    """Return the first `depth` base-16 digits of π/16 from rational bounds.

    Raise if original BBP truncation and the proved tail bound straddle a digit
    cylinder. π digits are not supplied as inputs.
    """
    if type(depth) is not int or depth < 1 or depth > m:
        raise ValueError("require 1<=depth<=m")
    lower = partial_source(m)
    upper = lower + original_tail_upper(m)
    factor = 16 ** depth
    lo = (lower * factor).__floor__()
    hi = (upper * factor).__floor__()
    if lo != hi:
        raise ValueError("original source interval does not isolate this prefix")
    return f"{lo:0{depth}x}"


def exact_phase_fraction(q: Fraction, n: int, h: int = 1) -> Fraction:
    """Residue of h*16^n*q modulo 1, computed without large powers."""
    if n < 0 or type(n) is not int or type(h) is not int:
        raise ValueError("n>=0 and integer frequency h required")
    q = Fraction(q)
    return Fraction((h * pow(16, n, q.denominator) * q.numerator) % q.denominator,
                    q.denominator)


def rational_clock(q: Fraction, *, max_period: int = 100000) -> tuple[int, int, tuple[Fraction, ...]]:
    """Return preperiod, minimal period, and exact phase residues for a rational shift.

    For q=a/(2^v*m) reduced, with odd m, preperiod ceil(v/4),
    period ord_m(16), or 1 for m=1. Does NOT represent irrational seeds.
    """
    q = Fraction(q)
    v = 0
    odd = q.denominator
    while odd % 2 == 0:
        odd //= 2
        v += 1
    preperiod = (v+3)//4
    if odd == 1:
        period = 1
    else:
        if odd > max_period:
            raise ValueError("odd denominator exceeds the finite period budget")
        state = 16 % odd
        period = 1
        while state != 1:
            period += 1
            if period > max_period:
                raise ValueError("finite period budget exhausted")
            state = (state * 16) % odd
    residues = tuple(exact_phase_fraction(q, preperiod+j) for j in range(period))
    return preperiod, period, residues


def seed_alias(q: Fraction, earliest_time: int, frequencies: Iterable[int] = (1,)) -> bool:
    """Exactly unchanged every n>=N circle character for the frequency set.

    This is a test for a *rational seed difference* q. For a frequency gcd g,
    aliases form the finite group (1/(g*16^N))Z/Z; no source positivity claim.
    """
    if type(earliest_time) is not int or earliest_time < 0:
        raise ValueError("earliest_time must be nonnegative integer")
    fs = tuple(frequencies)
    if not fs or any(type(h) is not int or h == 0 for h in fs):
        raise ValueError("nonempty nonzero integer frequency set required")
    return all(exact_phase_fraction(q, earliest_time, h) == 0 for h in fs)


def phase(q: Fraction, n: int, h: int = 1) -> complex:
    angle = float(exact_phase_fraction(q, n, h))
    return cmath.exp(2j * math.pi * angle)


def sideband_coefficients(q: Fraction, h: int) -> tuple[complex, ...]:
    """DFT of eventual rational-seed modulation; complex diagnostic values."""
    if type(h) is not int:
        raise ValueError("integer frequency")
    _, d, residues = rational_clock(q)
    return tuple(sum(cmath.exp(2j*math.pi*float((h*r) % 1))
                     * cmath.exp(-2j*math.pi*l*j/d)
                     for j, r in enumerate(residues))/d for l in range(d))


def stratum_character_means(A: int, period: int, h: int,
                            seed: Fraction = Fraction(0),
                            forcing: Source = original_forcing) -> tuple[tuple[int, complex], ...]:
    """A-stage dyadic epoch fingerprint, grouped by chronological n mod period.

    Each tuple is (count, normalized complex Fourier mean) for nonempty strata.
    Numerical character phases are diagnostics, not rational interval proofs.
    """
    if type(A) is not int or A < 1 or type(period) is not int or period < 1 or A < period:
        raise ValueError("require integer A>=period>=1")
    if type(h) is not int:
        raise ValueError("integer Fourier frequency required")
    state = Fraction(seed)
    sums = [0j] * period
    counts = [0] * period
    for n in range(1, 2*A):
        state = 16*state + forcing(n)
        if n >= A:
            sums[n % period] += cmath.exp(2j*math.pi*float((h*state)%1))
            counts[n % period] += 1
    return tuple((count, value/count) for count, value in zip(counts, sums))


def stratum_energy(means: Sequence[tuple[int, complex]]) -> float:
    n = sum(c for c, _ in means)
    if n <= 0:
        raise ValueError("positive epoch size required")
    return sum(c * abs(z)**2 for c, z in means) / n


def p_primary_part(value: Fraction, p: int) -> Fraction:
    """Canonical p-primary Q/Z summand; caller must supply a genuine prime p."""
    if type(p) is not int or p < 2:
        raise ValueError("prime p>=2 required")
    value = Fraction(value)
    unit = value.denominator
    p_power = 1
    while unit % p == 0:
        unit //= p
        p_power *= p
    if p_power == 1:
        return Fraction(0)
    return Fraction((value.numerator * pow(unit, -1, p_power)) % p_power, p_power)


def decaying_g(n: int) -> Fraction:
    """Odd-denominator source coboundary for a same-π positive mutant."""
    if type(n) is not int or n < 0:
        raise ValueError("n must be nonnegative")
    return Fraction(n, 257 * (2*n+1)**3)


def mutant_forcing(n: int) -> Fraction:
    if type(n) is not int or n < 1:
        raise ValueError("n>=1")
    return original_forcing(n) + decaying_g(n) - 16 * decaying_g(n-1)


def word_counts(digits: Sequence[int], depth: int, *, cyclic: bool = True) -> Counter[tuple[int,...]]:
    """Finite word histogram, cyclic option makes adjacent-depth marginals exact."""
    if not digits or type(depth) is not int or depth < 1 or depth > len(digits):
        raise ValueError("nonempty digits, 1<=depth<=len")
    if any(type(x) is not int or x < 0 or x > 15 for x in digits):
        raise ValueError("hex digit values in [0,15] required")
    length = len(digits)
    indices = range(length) if cyclic else range(length-depth+1)
    return Counter(tuple(digits[(i+j) % length] for j in range(depth)) for i in indices)


def word_energy(counts: Counter[tuple[int,...]], depth: int) -> Fraction:
    """E_k = 16^k sum_w (p(w)-16^-k)^2 = 16^k sum p(w)^2-1."""
    total = sum(counts.values())
    if total == 0 or depth < 1 or any(len(w) != depth for w in counts):
        raise ValueError("valid nonzero counts with uniform word length")
    return Fraction((16**depth)*sum(v*v for v in counts.values()), total*total)-1


def word_fourier(counts: Counter[tuple[int,...]], tau: Sequence[int]) -> complex:
    """Finite Fourier character over (Z/16Z)^k; numerical diagnostic."""
    if not tau or any(type(t) is not int for t in tau):
        raise ValueError("nonempty integer character multiindex")
    total = sum(counts.values())
    if total <= 0 or any(len(w) != len(tau) for w in counts):
        raise ValueError("histogram and character depth mismatch")
    return sum(c * cmath.exp(2j*math.pi*((sum(t*d for t, d in zip(tau, w))) % 16)/16)
               for w, c in counts.items()) / total


def machin_pi_over_16_interval(terms: int = 60) -> tuple[Fraction, Fraction]:
    """Independent exact Machin-arctangent interval for π/16, for finite tests.

    π/16 = arctan(1/5) - arctan(1/239)/4. No decimal/digit oracle.
    """
    if type(terms) is not int or terms < 1:
        raise ValueError("positive Taylor term count")

    def arctan_bracket(q: int) -> tuple[Fraction, Fraction]:
        s = sum((Fraction((-1)**k, (2*k+1) * q**(2*k+1)) for k in range(terms)), Fraction())
        error = Fraction(1, (2*terms+1) * q**(2*terms+1))
        return (s, s+error) if terms % 2 == 0 else (s-error, s)

    lo1, hi1 = arctan_bracket(5)
    lo2, hi2 = arctan_bracket(239)
    return lo1 - hi2/4, hi1 - lo2/4


def critical_relative_phase(A: int) -> complex:
    """Critical relative spectrum for positive same-π mutant vs original.

    h_A = 2056*A**2 is an exact integer. For every A>=24 the paper proof
    gives Re(mean) <= 13/16, while fixed h has vanishing relative contrast.
    Float evaluations here are diagnostic; the inequality is analytic.
    """
    if type(A) is not int or A < 1:
        raise ValueError("integer A>=1")
    h = 2056 * A * A
    return sum(cmath.exp(2j * math.pi * float((h*decaying_g(n))%1))
               for n in range(A, 2*A)) / A


def critical_profile_point(x: float) -> complex:
    """Continuum profile e(1/x^2), x in [1,2], for reference only."""
    if not 1.0 <= x <= 2.0:
        raise ValueError("1<=x<=2")
    return cmath.exp(2j*math.pi/(x*x))


def relative_phase_arg(A: int, n: int) -> Fraction:
    """The *unreduced*, exact critical phase h_A*g_n; no π oracle."""
    if type(A) is not int or A < 1 or type(n) is not int or n < A or n >= 2*A:
        raise ValueError("n must be in the integer epoch [A,2A)")
    return 2056*A*A*decaying_g(n)
