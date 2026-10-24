"""Exact finite circle couplings for the selected BBP base-transfer question.

The functions certify a specified finite coupling and a lower bound from a
Lipschitz observable. They do not certify asymptotic tripling invariance or
normality, and the sorting coupling is not asserted to be optimal on a circle.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence

from .pi_source_collision import bbp_forcing, tail_upper


def _rational(value: Q | int) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _integer(value: int, minimum: int = 1) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def circular_distance(x: Q | int, y: Q | int = 0) -> Q:
    difference = (_rational(x) - _rational(y)) % 1
    return min(difference, 1 - difference)


def _phases(values: Sequence[Q | int]) -> tuple[Q, ...]:
    if not values:
        raise ValueError("nonempty source sample required")
    return tuple(_rational(x) % 1 for x in values)


@dataclass(frozen=True)
class MultiplicationCoupling:
    multiplier: int
    permutation: tuple[int, ...]
    cost: Q
    observable_lower_bound: Q


def multiplication_coupling(
    values: Sequence[Q | int], multiplier: int, permutation: Sequence[int]
) -> MultiplicationCoupling:
    """Certify the mean cost of q*x_i -> x_permutation[i] on the circle.

    The cost upper-bounds W1(mu, (times q)_*mu). The lower bound uses the
    1-Lipschitz function f(x)=circular_distance(x,0), via the coupling inequality.
    A genuine permutation is required so the destination marginal stays mu.
    """
    source = _phases(values)
    _integer(multiplier)
    n = len(source)
    if (len(permutation) != n or any(type(i) is not int for i in permutation)
            or sorted(permutation) != list(range(n))):
        raise ValueError("a permutation of every source index is required")
    perm = tuple(permutation)
    cost = sum((circular_distance(multiplier*x, source[perm[i]])
                for i, x in enumerate(source)), Q(0))/n
    difference = sum((circular_distance(multiplier*x)
                      - circular_distance(x) for x in source), Q(0))/n
    lower = abs(difference)
    if lower > cost:
        raise ArithmeticError("coupling/Lipschitz inequality failed")
    return MultiplicationCoupling(multiplier, perm, cost, lower)


def sorted_multiplication_coupling(
    values: Sequence[Q | int], multiplier: int
) -> MultiplicationCoupling:
    """Match sorted multiplied phases to sorted original phases, with ties.

    This supplies an explicit admissible source-index permutation. It makes
    no assertion about a source-independent rule, optimal circle transport,
    or a decay rate as the number of samples grows.
    """
    source = _phases(values)
    _integer(multiplier)
    original_order = sorted(range(len(source)), key=lambda i: (source[i], i))
    multiplied_order = sorted(range(len(source)),
                              key=lambda i: ((multiplier*source[i]) % 1, i))
    permutation = [0]*len(source)
    for i, j in zip(multiplied_order, original_order):
        permutation[i] = j
    return multiplication_coupling(source, multiplier, permutation)


def source_successor_transport_bound(start: int, length: int) -> Q:
    """An unconditional W1 upper bound for mu_y versus (times16)_*mu_y.

    Source samples are y_start,...,y_(start+length-1). Match each interior
    multiplied sample to its successor and the last to the first. The final
    circular distance costs at most 1/2, not an omitted endpoint.
    """
    _integer(start)
    _integer(length)
    return (Q(1, 2) + sum((min(Q(1, 2), bbp_forcing(n + 1))
                          for n in range(start, start + length - 1)), Q(0)))/length


def source_to_pi_coupling_budget(start: int, length: int, multiplier: int) -> Q:
    """Extra cost for transporting the same coupling to the pi shadow.

    On source indices n the actual pi orbit is {16^(n-1)*pi}={y_n+T_n},
    with 0<T_n<tail_upper(n). Multiplication is q-Lipschitz on the circle,
    and a permutation uses every destination once. The added mean cost is
    at most (q+1) times the mean tail bound, including wraparound.
    """
    _integer(start)
    _integer(length)
    _integer(multiplier)
    return Q(multiplier + 1, length)*sum(
        (tail_upper(n) for n in range(start, start + length)), Q(0))


def outward_decimal(value: Q | int, digits: int = 12) -> tuple[Q, Q]:
    """Exact decimal-grid enclosure; display helper, never a floating decision."""
    value = _rational(value)
    _integer(digits, 0)
    scale = 10**digits
    lo = (value*scale).__floor__()
    hi = lo if value*scale == lo else lo + 1
    return Q(lo, scale), Q(hi, scale)


def cantor_two_digit_sample(depth: int) -> tuple[Q, ...]:
    """Finite prefixes of the fair base16 digit law {0,1}; a changed source."""
    _integer(depth, 0)
    values = [Q(0)]
    for k in range(1, depth + 1):
        values = values + [x + Q(1, 16**k) for x in values]
    return tuple(values)
