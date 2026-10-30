"""Exact instruments for recursive carrier composition and the authentic BBP field.

Paper authority is in research/2026-10-29/recursive_carrier_triangle/.
All outputs below are rational finite quantities.  The source field is a
Laplace representation of the original forcing, not a stochastic law for the
selected BBP orbit.  No normality, RH, physical gauge theory, or cognitive
mechanism is inferred.  Existing source code is imported without modification.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from math import factorial
from typing import Callable, Iterable, Sequence

from .oily_macaroni_transfer import r_at_a, authentic_r


def rational(value, *, positive=False, nonnegative=False) -> F:
    if type(value) not in (int, F):
        raise ValueError("an exact integer or Fraction is required")
    q = F(value)
    if positive and q <= 0:
        raise ValueError("positive parameter required")
    if nonnegative and q < 0:
        raise ValueError("nonnegative parameter required")
    return q


def natural(value, *, positive=False) -> int:
    if type(value) is not int or value < int(positive):
        raise ValueError("exact natural number required")
    return value


def source_factorization(a) -> F:
    """R(a), evaluated through its factorized rational numerator."""
    a = rational(a, positive=True)
    return (15*a*a + 121*a + 240) / (a*(a+3)*(a+4)*(a+5))


def tilt_normalizer(a, increment) -> F:
    a = rational(a, positive=True)
    s = rational(increment, nonnegative=True)
    return r_at_a(a+s)/r_at_a(a)


def atomic_laplace(a, increment) -> F:
    """Independent-atom Laplace product, with conjugate radicals eliminated.

    alpha+beta=121/15, alpha*beta=16.  The first two factors correspond
    to Exp(a), Exp(a+5).  The paired factor is the product of the two
    Bernoulli-gated exponential transforms.  The oracle checks the individual
    irrational probabilities separately in Q(sqrt(241)).
    """
    a = rational(a, positive=True)
    s = rational(increment, nonnegative=True)
    numerator = lambda x: x*x + F(121, 15)*x + 16
    mandatory = a/(a+s) * (a+5)/(a+5+s)
    gated_pair = ((a+3)*(a+4)/((a+3+s)*(a+4+s))
                  * numerator(a+s)/numerator(a))
    return mandatory*gated_pair


def source_cumulant(a, order: int) -> F:
    """Exact cumulant of X under e^(-a*x)Q(x)/R(a), for any order>=1.

    Root reciprocal power sums obey a second-order rational recurrence;
    no floating-point roots or cancellation tolerance are used.
    """
    a = rational(a, positive=True)
    natural(order, positive=True)
    denominator = a*a + F(121, 15)*a + 16
    root_sum = (2*a + F(121, 15))/denominator
    root_product = 1/denominator
    previous, current = F(2), root_sum
    for _ in range(2, order+1):
        previous, current = current, root_sum*current-root_product*previous
    poles = sum((1/(a+c)**order for c in (0, 3, 4, 5)), F())
    return factorial(order-1)*(poles-current)


def cumulant_bounds(a, order: int) -> tuple[F, F]:
    """Strict lower/upper bounds, valid for every a>0 and order>=1."""
    a = rational(a, positive=True)
    natural(order, positive=True)
    scale = factorial(order-1)
    return (scale*(1/a**order+1/(a+5)**order),
            scale*(1/a**order+1/(a+3)**order))


def interaction_ratio(a, increments: Iterable) -> F:
    """exp(Delta_s1 ... Delta_sm log R(a)), exact at rational inputs.

    The theorem permits every finite order; this enumerating instrument has
    an explicit 12-direction budget.  A zero direction makes the ratio one.
    """
    a = rational(a, positive=True)
    steps = tuple(rational(s, nonnegative=True) for s in increments)
    if not 1 <= len(steps) <= 12:
        raise ValueError("instrument requires 1..12 increment directions")
    answer = F(1)
    for bits in product((0, 1), repeat=len(steps)):
        offset = sum((s*b for s, b in zip(steps, bits)), F())
        exponent = (-1)**(len(steps)-sum(bits))
        answer *= r_at_a(a+offset)**exponent
    return answer


def pair_ratio_bounds(a, s, t) -> tuple[F, F]:
    """Strict bounds on exp of the two-direction interaction, s,t>0.

    At a zero increment both bounds and the interaction are one.
    """
    a = rational(a, positive=True)
    s, t = (rational(v, nonnegative=True) for v in (s, t))
    def basic(c):
        x = a+c
        return (x+s)*(x+t)/(x*(x+s+t))
    return basic(0)*basic(5), basic(0)*basic(3)


def overlap_square(a, b) -> F:
    """Exact squared Hilbert/Hellinger affinity of the authentic fields."""
    a, b = (rational(v, positive=True) for v in (a, b))
    return r_at_a((a+b)/2)**2/(r_at_a(a)*r_at_a(b))


def overlap_square_bounds(a, b) -> tuple[F, F]:
    a, b = (rational(v, positive=True) for v in (a, b))
    middle = (a+b)/2
    factor = lambda c: (a+c)*(b+c)/(middle+c)**2
    return factor(0)*factor(3), factor(0)*factor(5)


def overlap_deficit_bound(a, b) -> F:
    """1-H(a,b) <= this exact rational bound, all positive parameters."""
    a, b = (rational(v, positive=True) for v in (a, b))
    return ((a-b)/(a+b))**2


def block_transport_budget(horizon: int, block_size: int) -> dict:
    """All-time signed transport budget without a discarded initial prefix.

    For any |z_n|<=1, compare N^-1 sum z_n with N^-1 sum
    z_n H(a_n,a_start_of_block).  The endpoint bound below is rational
    and costs only O(number_of_blocks) operations.  It is bounded above
    by 3*block_size/(2*horizon).  This is not a cancellation bound.
    """
    natural(horizon, positive=True)
    natural(block_size, positive=True)
    if block_size > horizon:
        raise ValueError("block_size must not exceed horizon")
    bound, blocks = F(), 0
    for start in range(1, horizon+1, block_size):
        length = min(block_size, horizon-start+1)
        bound += length*overlap_deficit_bound(8*start-7, 8*(start+length-1)-7)
        blocks += 1
    return {"horizon": horizon, "block_size": block_size, "blocks": blocks,
            "discarded": 0, "absolute_mean_error_upper": bound/horizon,
            "simple_upper": min(F(1), F(3*block_size, 2*horizon)),
            "signed_cancellation_proved": False}


def integer_cuberoot(value: int) -> int:
    """Floor cube root without a floating-point rounding boundary."""
    natural(value)
    lo, hi = 0, 1 << ((value.bit_length()+2)//3)
    while lo+1 < hi:
        middle = (lo+hi)//2
        if middle**3 <= value:
            lo = middle
        else:
            hi = middle
    return lo


def cubic_transport_budget(horizon: int) -> dict:
    """Exact O(N^(-2/3)) transport using O(N^(1/3)) windows.

    Blocks start at 1+j^3 and end at (j+1)^3, truncated at N. The first
    block is the singleton {1}. Every later block contributes <27/4 to
    the unnormalized error. This is a representation error, not decay
    of the represented signed sum.
    """
    natural(horizon, positive=True)
    last = integer_cuberoot(horizon-1)
    budget = F()
    for j in range(last+1):
        start, stop = 1+j**3, min(horizon, (j+1)**3)
        length = stop-start+1
        budget += length*overlap_deficit_bound(8*start-7, 8*stop-7)
    return {"horizon": horizon, "blocks": last+1, "last_block_index": last,
            "discarded": 0, "absolute_mean_error_upper": budget/horizon,
            "simple_upper": min(F(1), F(27*last, 4*horizon)),
            "signed_cancellation_proved": False}


def posterior_transport(mu: Sequence, kernel: Sequence[Sequence]) -> tuple[tuple[F, ...], F]:
    """Return normalized row-vector transport and its retained mass."""
    weights = tuple(rational(x, nonnegative=True) for x in mu)
    rows = tuple(tuple(rational(x, nonnegative=True) for x in row) for row in kernel)
    if not weights or sum(weights) != 1 or len(rows) != len(weights):
        raise ValueError("probability vector and matching nonempty kernel required")
    if not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("rectangular nonempty kernel required")
    raw = tuple(sum((weights[i]*rows[i][j] for i in range(len(weights))), F())
                for j in range(len(rows[0])))
    mass = sum(raw)
    if not mass:
        raise ValueError("zero-mass path has no normalized posterior")
    return tuple(x/mass for x in raw), mass


def polya_left(left: int, right: int, alpha=1, beta=1) -> F:
    natural(left); natural(right)
    a, b = (rational(v, positive=True) for v in (alpha, beta))
    return (a+left)/(a+b+left+right)


def harmonic_left(left: int, right: int, length: int = 3) -> F:
    natural(left); natural(right); natural(length, positive=True)
    if left >= length or right >= length:
        raise ValueError("two-arm field stops at a completed connection")
    return F(length-right, 2*length-left-right)


def exponential_left(left: int, right: int) -> F:
    natural(left); natural(right)
    return F(2**left, 2**left+2**right)


def word_probability(word: str, left_probability: Callable[[int, int], F]) -> F:
    if not isinstance(word, str) or any(c not in "LR" for c in word):
        raise ValueError("word must contain only L and R")
    left = right = 0
    probability = F(1)
    for letter in word:
        p = rational(left_probability(left, right), nonnegative=True)
        if p > 1:
            raise ValueError("transition probability exceeds one")
        probability *= p if letter == "L" else 1-p
        left += letter == "L"
        right += letter == "R"
    return probability


def diamond_ratio(left: int, right: int, left_probability: Callable[[int, int], F]) -> F:
    """Weight(LR)/weight(RL) for one reachable count-lattice diamond."""
    natural(left); natural(right)
    ps = [rational(left_probability(l, r), positive=True)
          for l, r in ((left, right), (left+1, right), (left, right+1))]
    if any(p >= 1 for p in ps):
        raise ValueError("strictly positive probabilities in both directions required")
    p, after_left, after_right = ps
    return p*(1-after_left)/((1-p)*after_right)


def word_sheet_ratio(word: str, left_probability: Callable[[int, int], F]) -> F:
    """Discrete Stokes product relative to canonical L...LR...R path.

    For each L step at height r, include inverse diamond weights below
    it.  This evaluates an area product, independently of a word product.
    """
    if not isinstance(word, str) or any(c not in "LR" for c in word):
        raise ValueError("word must contain only L and R")
    left = right = 0
    ratio = F(1)
    for letter in word:
        if letter == "L":
            for row in range(right):
                ratio /= diamond_ratio(left, row, left_probability)
            left += 1
        else:
            right += 1
    return ratio


def all_left_atom_lower_bound(prefix: int) -> F:
    """Rational lower bound for the infinite all-L atom in exponential feedback.

    After a prefix of length N>=2, the remaining product is at least
    1-sum_(n>=N) 2^-n = 1-2^(1-N).  The paper also proves >=1/(2e).
    """
    natural(prefix, positive=True)
    if prefix < 2:
        raise ValueError("use prefix>=2 for a positive rational tail bound")
    return word_probability("L"*prefix, exponential_left)*(1-F(1, 2**(prefix-1)))


def affine_source_history(forcing: Iterable, seed=0) -> tuple[F, ...]:
    state = rational(seed)
    history = [state]
    for value in forcing:
        state = 16*state+rational(value)
        history.append(state)
    return tuple(history)


def authentic_history(horizon: int) -> tuple[F, ...]:
    natural(horizon)
    return affine_source_history(authentic_r(n) for n in range(1, horizon+1))


def affine_phase_rectangle(forcing: Sequence, first: Sequence, second: Sequence,
                           alpha=1, beta=1, seed=0) -> tuple[F, ...]:
    """Exact exponents of the multiplicative mixed-phase null control.

    Every returned U11+U00-U10-U01 must be zero.  An exponential
    readout can have nonzero additive mixed differences despite this.
    """
    if not (len(forcing) == len(first) == len(second)):
        raise ValueError("all source sequences must have the same length")
    a, b = rational(alpha), rational(beta)
    streams = [tuple(rational(r)+i*a*rational(f)+j*b*rational(g)
                     for r, f, g in zip(forcing, first, second))
               for i, j in ((0, 0), (1, 0), (0, 1), (1, 1))]
    u00, u10, u01, u11 = [affine_source_history(s, seed) for s in streams]
    return tuple(d+a-b-c for a, b, c, d in zip(u00, u10, u01, u11))
