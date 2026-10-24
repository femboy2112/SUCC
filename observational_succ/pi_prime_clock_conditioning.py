"""Exact simultaneous BBP clocks and finite conditional cell laws.

No independence, normality, or selected-collision asymptotic is inferred.
The source is the existing authentic y_0=0 four-pole recurrence. Only common
first-birth source-free windows are admitted; later prime impulses are not
silently treated as the same homogeneous clock.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, isqrt, lcm, prod
from typing import Sequence

from observational_succ.pi_source_collision import bbp_states, order16


def _positive_integer(value: int) -> int:
    if type(value) is not int or value < 1:
        raise ValueError("positive integer required")
    return value


def _first_window_prime(value: int) -> int:
    _positive_integer(value)
    if value < 2 or any(value % k == 0 for k in range(2, isqrt(value) + 1)):
        raise ValueError("prime required")
    if value % 8 != 1:
        raise ValueError("first-window source contract requires p = 1 mod 8")
    return value


def clock_pair_count(length: int, period: int) -> int:
    """Ordered pairs of times in [0,length) equal modulo period, diagonal included."""
    _positive_integer(length)
    _positive_integer(period)
    quotient, remainder = divmod(length, period)
    return remainder * (quotient + 1)**2 + (period - remainder) * quotient**2


@dataclass(frozen=True)
class PrimeClockWindow:
    """An exact finite source certificate, constructed by common_prime_window."""

    primes: tuple[int, ...]
    start: int
    stop: int  # inclusive state indices y_start,...,y_stop
    orders: tuple[int, ...]
    period: int
    states: tuple[Q, ...]
    local: tuple[tuple[Q, ...], ...]  # time-major, preserving each prime label
    complement: tuple[Q, ...]

    def conjugate(self, embedding: Sequence[int]) -> tuple[Q, ...]:
        values = tuple(embedding)
        if len(values) != len(self.primes):
            raise ValueError("one nonzero residue per source prime is required")
        if any(type(a) is not int or not 1 <= a < p
               for a, p in zip(values, self.primes)):
            raise ValueError("embedding residues must satisfy 1 <= a < p")
        return tuple((sum((a*v for a, v in zip(values, row)), Q(0)) + w) % 1
                     for row, w in zip(self.local, self.complement))

    def fibers(self) -> tuple[tuple[int, ...], ...]:
        """Actual primary-vector fibers; indices are offsets from self.start."""
        groups: dict[tuple[Q, ...], list[int]] = {}
        for index, row in enumerate(self.local):
            groups.setdefault(row, []).append(index)
        return tuple(tuple(indices) for indices in groups.values())


def common_prime_window(primes: Sequence[int]) -> PrimeClockWindow:
    """Authenticate the intersection of distinct first prime-birth windows.

    A user-supplied arbitrary complement is never accepted as the BBP source.
    Empty intersections raise rather than extrapolate a local clock law.
    """
    values = tuple(_first_window_prime(p) for p in primes)
    if not values or len(set(values)) != len(values):
        raise ValueError("a nonempty sequence of distinct source primes is required")
    starts = tuple((p - 1)//8 for p in values)
    start, stop = max(starts) + 1, 4*min(starts)
    if start > stop:
        raise ValueError("source-free first-birth windows have empty intersection")
    states = bbp_states(stop)[start:stop + 1]
    orders = tuple(order16(p) for p in values)
    period = lcm(*orders)
    local = tuple(tuple(Q(4*pow(16, n-u-1, p) % p, p)
                        for p, u in zip(values, starts))
                  for n in range(start, stop + 1))
    complement = tuple((y - sum(row, Q(0))) % 1 for y, row in zip(states, local))
    product = prod(values)
    if any(gcd(w.denominator, product) != 1 for w in complement):
        raise ArithmeticError("complete source complement is not prime-to all clocks")
    result = PrimeClockWindow(values, start, stop, orders, period,
                              states, local, complement)
    if result.conjugate((1,)*len(values)) != states:
        raise ArithmeticError("selected source reconstruction failed")
    if sum(len(fiber)**2 for fiber in result.fibers()) != clock_pair_count(len(states), period):
        raise ArithmeticError("source clock fiber cardinalities violated")
    return result


def conditional_cell_counts(
    window: PrimeClockWindow, cells: int, embedding: Sequence[int] | None = None,
) -> tuple[tuple[tuple[int, int], ...], ...]:
    """Exact empirical cell law in every actual clock fiber.

    A fiber law with one occupied label has zero conditional entropy exactly.
    Counts are retained instead of using floating logarithms as a certificate.
    """
    _positive_integer(cells)
    phases = window.states if embedding is None else window.conjugate(embedding)
    return tuple(tuple(sorted(Counter(int(phases[i]*cells) for i in fiber).items()))
                 for fiber in window.fibers())


def aligned_complement_control(window: PrimeClockWindow, cells: int) -> tuple[int, tuple[Q, ...]]:
    """FAKE source retaining all declared local clocks, with selected cells aligned.

    This deliberately changes the authentic complement; it is only a hostile
    control against prime-to-conductor or clock-independence shortcuts.
    """
    _positive_integer(cells)
    denominator = 2*cells*prod(window.primes) + 1
    result = []
    for row in window.local:
        target = (-sum(row, Q(0))) % 1
        ceiling = -((-denominator*target).__floor__())
        result.append(Q(ceiling, denominator) % 1)
    return denominator, tuple(result)
