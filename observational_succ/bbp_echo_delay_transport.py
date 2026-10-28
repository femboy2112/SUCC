"""Exact finite-delay/Green transport for the original four-pole BBP recurrence.

Theorems and error bounds: research/2026-10-27/BBP_ECHO_DELAY_TRANSPORT.md.
No claim of pi normality.  Never uses floating point for identity checks.
The original forcing comes from the unmodified source_verified adapter.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence

from .bbp_binwindow_conjugacy import source_verified

BASE = 16


def _index(n: int, minimum: int = 0, maximum: int = 4096) -> int:
    if type(n) is not int or not minimum <= n <= maximum:
        raise ValueError("integer index outside declared exact-test budget")
    return n


def _coefficients(coefficients: Sequence[int]) -> tuple[int, ...]:
    if not coefficients or len(coefficients) > 128:
        raise ValueError("finite nonempty filter of length at most 128 required")
    result = tuple(coefficients)
    if any(type(c) is not int for c in result):
        raise TypeError("integer filter coefficients required")
    return result


def filter_symbol(coefficients: Sequence[int]) -> int:
    """Evaluate P(16), P(E)=sum_j coefficients[j] E**j."""
    cs = _coefficients(coefficients)
    return sum(c * BASE**j for j, c in enumerate(cs))


def division_by_characteristic(coefficients: Sequence[int]) -> tuple[int, tuple[int, ...]]:
    """Exact polynomial identity P(X)=P(16)+(X-16)Q(X)."""
    cs = _coefficients(coefficients)
    q = [0] * (len(cs) - 1)
    if q:
        q[-1] = cs[-1]
        for j in range(len(q) - 2, -1, -1):
            q[j] = cs[j + 1] + BASE * q[j + 1]
    symbol = cs[0] + (BASE * q[0] if q else 0)
    if symbol != filter_symbol(cs):
        raise ArithmeticError("synthetic division inconsistency")
    return symbol, tuple(q)


@dataclass(frozen=True)
class ExactBBPWindow:
    """Finite rational truncation, not a numerical approximation certificate."""
    cutoff: int
    forcing: tuple[Q, ...]  # r(0) placeholder 0; entries 1..cutoff authenticated
    states: tuple[Q, ...]   # U_0=0, U_n=16 U_(n-1)+r(n)
    tails: tuple[Q, ...]    # T_(n,M)=sum_(a=n+1)^M 16^(n-a)r(a)
    pi_prefix: Q            # sum_(a=1)^M 16^(1-a)r(a)


def exact_window(cutoff: int) -> ExactBBPWindow:
    m = _index(cutoff, 1, 512)
    r = [Q(0)] + [source_verified(n) for n in range(1, m + 1)]
    states = [Q(0)]
    for n in range(1, m + 1):
        states.append(BASE * states[-1] + r[n])
    tails = [Q(0)] * (m + 1)
    for n in range(m - 1, -1, -1):
        tails[n] = (r[n + 1] + tails[n + 1]) / BASE
    # At n=0: 16*T_0 is precisely the finite BBP series for pi.
    return ExactBBPWindow(m, tuple(r), tuple(states), tuple(tails), BASE * tails[0])


def filtered_state(window: ExactBBPWindow, n: int, coefficients: Sequence[int]) -> Q:
    cs = _coefficients(coefficients)
    _index(n, 0, window.cutoff)
    if n + len(cs) - 1 > window.cutoff:
        raise ValueError("filter extends beyond the authenticated finite window")
    return sum((Q(c) * window.states[n + j] for j, c in enumerate(cs)), Q(0))


def filtered_tail(window: ExactBBPWindow, n: int, coefficients: Sequence[int]) -> Q:
    cs = _coefficients(coefficients)
    _index(n, 0, window.cutoff)
    if n + len(cs) - 1 > window.cutoff:
        raise ValueError("filter extends beyond the authenticated finite window")
    return sum((Q(c) * window.tails[n + j] for j, c in enumerate(cs)), Q(0))


def exact_transport_residual(window: ExactBBPWindow, n: int, coefficients: Sequence[int]) -> Q:
    """Should be exactly -filtered_tail; no floating point, no pi oracle."""
    _index(n, 1, window.cutoff)
    carrier = Q(filter_symbol(coefficients) * BASE**(n - 1)) * window.pi_prefix
    return filtered_state(window, n, coefficients) - carrier


def source_only_filter(window: ExactBBPWindow, n: int, coefficients: Sequence[int]) -> Q:
    """Independent identity P(E)U = P(16)U+Q(E)r(n+1)."""
    cs = _coefficients(coefficients)
    _index(n, 0, window.cutoff)
    if n + len(cs) - 1 > window.cutoff:
        raise ValueError("filter extends beyond finite window")
    symbol, quotient = division_by_characteristic(cs)
    return (Q(symbol) * window.states[n] +
            sum((Q(q) * window.forcing[n + j + 1]
                 for j, q in enumerate(quotient)), Q(0)))


def tail_upper(n: int) -> Q:
    """Rigorous infinite-future upper bound T_n < 1/[15(n+1)^2], n>=1."""
    _index(n, 1)
    return Q(1, 15 * (n + 1)**2)


def phase_difference_budget_pi_units(h: int, coefficients: Sequence[int]) -> Q:
    """Uniform-in-N-and-lags bound divided by pi: 2|h| ||c||_1/15.

    To recover a bound in complex absolute value, multiply this exact
    rational by pi.  Source positivity and r(n)<1/n^2 for n>=2 are proved
    on paper, not by the finite execution of this method.
    """
    if type(h) is not int or h == 0:
        raise ValueError("nonzero integer Fourier frequency required")
    return Q(2 * abs(h) * sum(map(abs, _coefficients(coefficients))), 15)


def nonnormal_decay_control(n: int) -> tuple[Q, Q, Q]:
    """Hostile zero-seeded O(n^-2) source with rational, nonnormal carrier.

    alpha=15/64, forcing alpha/n^2-alpha/[16(n+1)^2]; state is
    16^(n-1)alpha-alpha/[16(n+1)^2].  This matches the authentic leading
    15/64 coefficient but NOT the authentic four-pole source or 2-adic clock.
    """
    _index(n, 1)
    alpha = Q(15, 64)
    forcing = alpha * (Q(1, n*n) - Q(1, BASE * (n+1)**2))
    tail = alpha / (BASE * (n+1)**2)
    state = BASE**(n - 1) * alpha - tail
    return forcing, tail, state
