"""An actual N-successor carrier with an internal, exact BBP state machine.

A BBP orbit is a single deterministic embedded copy of (N, succ), not a
selection among local prime histories.  The machine is total on N^3 and
can be coded into one N by Cantor pairing.  Its integer state retains the
lift that is lost under circle or prime-torsion quotients.

This construction does NOT bound equidistribution of pi's hexadecimal orbit.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


def _nat(x: int, name: str) -> int:
    if type(x) is not int or x < 0:
        raise ValueError(f"{name} must be a natural number")
    return x


def forcing_numerator(index: int) -> int:
    """P(j), j>=1: the combined authentic four-pole numerator."""
    if _nat(index, "index") == 0:
        raise ValueError("forcing index starts at one")
    return 120 * index * index - 89 * index + 16


def forcing_denominator(index: int) -> int:
    """D(j)>0 odd, j>=1, all four source poles retained exactly."""
    if _nat(index, "index") == 0:
        raise ValueError("forcing index starts at one")
    return (2 * index - 1) * (4 * index - 1) * (8 * index - 7) * (8 * index - 3)


def exact_forcing(index: int) -> Fraction:
    return Fraction(forcing_numerator(index), forcing_denominator(index))


@dataclass(frozen=True)
class NaturalBBPState:
    """(n,a,t) in N^3 means unwrapped rational U=a/(2*t+1)."""

    time: int
    numerator: int
    odd_denominator_half: int

    def __post_init__(self) -> None:
        _nat(self.time, "time")
        _nat(self.numerator, "numerator")
        _nat(self.odd_denominator_half, "odd_denominator_half")

    @property
    def denominator(self) -> int:
        return 2 * self.odd_denominator_half + 1

    @property
    def rational(self) -> Fraction:
        return Fraction(self.numerator, self.denominator)


ORIGIN = NaturalBBPState(0, 0, 0)


def machine_step(state: NaturalBBPState) -> NaturalBBPState:
    """Total N^3 map with exactly the original 16U+r(n+1) quotient."""
    if type(state) is not NaturalBBPState:
        raise TypeError("expected a NaturalBBPState")
    j = state.time + 1
    p, d = forcing_numerator(j), forcing_denominator(j)
    a = 16 * state.numerator * d + state.denominator * p
    b = state.denominator * d
    # Both source and state denominators are odd. No truncation/reduction.
    return NaturalBBPState(j, a, (b - 1) // 2)


def orbit_state(index: int) -> NaturalBBPState:
    """The canonical source section i(n) = machine_step^n(ORIGIN)."""
    _nat(index, "index")
    s = ORIGIN
    for _ in range(index):
        s = machine_step(s)
    return s


def orbit_prefix(count: int) -> tuple[NaturalBBPState, ...]:
    _nat(count, "count")
    s = ORIGIN
    result = []
    for _ in range(count):
        result.append(s)
        s = machine_step(s)
    return tuple(result)


def cantor_pair(a: int, b: int) -> int:
    _nat(a, "a")
    _nat(b, "b")
    return (a + b) * (a + b + 1) // 2 + b


def cantor_unpair(z: int) -> tuple[int, int]:
    _nat(z, "z")
    w = (isqrt(8 * z + 1) - 1) // 2
    t = w * (w + 1) // 2
    return w - (z - t), z - t


def encode_state(s: NaturalBBPState) -> int:
    if type(s) is not NaturalBBPState:
        raise TypeError("expected an N^3 state")
    return cantor_pair(s.time, cantor_pair(s.numerator, s.odd_denominator_half))


def decode_state(z: int) -> NaturalBBPState:
    n, other = cantor_unpair(z)
    a, t = cantor_unpair(other)
    return NaturalBBPState(n, a, t)


def encoded_machine_step(z: int) -> int:
    """A total self-map of N representing the same autonomous BBP machine."""
    return encode_state(machine_step(decode_state(z)))


def dyadic_view(s: NaturalBBPState, bits: int) -> int:
    """Natural-state observation in Z/2^bits, not 2-primary Q/Z torsion."""
    if type(s) is not NaturalBBPState:
        raise TypeError("expected a state")
    _nat(bits, "bits")
    if bits == 0:
        raise ValueError("positive bit depth required")
    modulus = 1 << bits
    return s.numerator * pow(s.denominator, -1, modulus) % modulus


def dyadic_observer_step(index: int, residue: int, bits: int) -> int:
    """Commuting local factor of N^3 machine, using the same source time."""
    _nat(index, "index")
    _nat(residue, "residue")
    _nat(bits, "bits")
    if bits == 0:
        raise ValueError("positive bit depth required")
    m = 1 << bits
    j = index + 1
    d = forcing_denominator(j)
    p = forcing_numerator(j)
    return (16 * residue + p * pow(d, -1, m)) % m


def rational_partial_alpha(index: int) -> Fraction:
    """Finite rational approximation U_n / 16^n to alpha=pi/16 (BBP input)."""
    s = orbit_state(index)
    return s.rational / 16**index


def alpha_enclosure(index: int) -> tuple[Fraction, Fraction]:
    """Rational-only strict upper interval assuming the classical BBP identity.

    For j>=1, 0<r(j)<8/j^2. Hence its series tail at n has
    0<T_n<8/[15(n+1)^2]. The upper bound is deliberately nonoptimal.
    """
    _nat(index, "index")
    lo = rational_partial_alpha(index)
    error = Fraction(8, 15 * (index + 1)**2 * 16**index)
    return lo, lo + error


def source_tail_enclosure(index: int, terms: int) -> tuple[Fraction, Fraction]:
    """Independent rational enclosure for T_n (requires decreasing r(j))."""
    _nat(index, "index")
    _nat(terms, "terms")
    if terms == 0:
        raise ValueError("at least one term required")
    lo = sum((exact_forcing(index + j) / 16**j
              for j in range(1, terms + 1)), Fraction())
    hi = lo + exact_forcing(index + terms + 1) / (15 * 16**terms)
    return lo, hi


def certified_hex_digit(index: int, max_tail_terms: int = 80) -> tuple[int, int] | None:
    """Exact finite proof of a single base-16 digit of alpha=pi/16, if found.

    Returns (digit, number_of_tail_terms) when rational lower/upper
    enclosures fall within one digit cell; None when budget is exhausted.
    This proves no frequency estimate.  Classical irrationality of pi
    implies an unbounded version terminates at every fixed index.
    """
    _nat(index, "index")
    _nat(max_tail_terms, "max_tail_terms")
    if max_tail_terms == 0:
        raise ValueError("positive tail term budget required")
    u = orbit_state(index).rational
    for terms in range(1, max_tail_terms + 1):
        lo, hi = source_tail_enclosure(index, terms)
        x, y = 16 * (u + lo), 16 * (u + hi)
        a, b = x.numerator // x.denominator, y.numerator // y.denominator
        if a == b:
            return a % 16, terms
    return None
