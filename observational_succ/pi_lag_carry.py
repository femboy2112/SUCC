"""Exact authentic BBP lag/carry diagnostics; no normality certificate.

Paper statements: research/2026-10-24/PI_LAG_ARITHMETIC_TRACK.md.
All decisions use Fraction arithmetic. The selected initial condition is zero.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from observational_succ.pi_source_collision import bbp_forcing


def _int(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def _radius(value: Q) -> Q:
    if type(value) not in (int, Q) or not 0 <= value < Q(1, 2):
        raise ValueError("exact radius in [0, 1/2) required")
    return Q(value)


def centered(value: Q) -> Q:
    """Representative in [-1/2,1/2), with the antipode assigned -1/2."""
    if type(value) not in (int, Q):
        raise ValueError("exact rational required")
    return Q(value) - (Q(value)+Q(1, 2)).__floor__()


@dataclass(frozen=True)
class CarryPath:
    states: tuple[Q, ...]
    carries: tuple[int, ...]  # carries[n-1] is c_n


def bbp_carry_path(last: int) -> CarryPath:
    _int(last)
    states, carries = [Q(0)], []
    for n in range(1, last+1):
        lift = 16*states[-1]+bbp_forcing(n)
        carry = lift.__floor__()
        carries.append(carry)
        states.append(lift-carry)
    return CarryPath(tuple(states), tuple(carries))


def forcing_gap(n: int, lag: int) -> Q:
    _int(n)
    _int(lag, 1)
    return bbp_forcing(n+1)-bbp_forcing(n+lag+1)


def forcing_gap_bounds(n: int, lag: int) -> tuple[Q, Q]:
    """Positive beta-integral lower and upper bounds, valid for n>=0, lag>=1."""
    _int(n)
    _int(lag, 1)
    a, b = 8*(n+lag), 8*n+1
    return Q(64*lag, a*(a+1)*(a+2)), Q(240*lag, b*(b+1)*(b+2))


@dataclass(frozen=True)
class LagStep:
    index: int
    lag: int
    raw: Q
    raw_next: Q
    centered: Q
    centered_next: Q
    centering_offset: int
    next_centering_offset: int
    source_carry_difference: int
    centered_carry: int
    forcing_gap: Q


def lag_step(path: CarryPath, n: int, lag: int) -> LagStep:
    _int(n)
    _int(lag, 1)
    if n+lag+1 >= len(path.states):
        raise ValueError("path does not include both lag endpoints and successors")
    raw = path.states[n+lag]-path.states[n]
    raw_next = path.states[n+lag+1]-path.states[n+1]
    eta = (raw+Q(1, 2)).__floor__()
    eta_next = (raw_next+Q(1, 2)).__floor__()
    difference = path.carries[n+lag]-path.carries[n]
    return LagStep(n, lag, raw, raw_next, raw-eta, raw_next-eta_next,
                   eta, eta_next, difference, difference+eta_next-16*eta,
                   forcing_gap(n, lag))


def close_run_gate(n: int, lag: int, radius: Q) -> bool:
    radius = _radius(radius)
    f = forcing_gap(n, lag)
    return f <= 15*radius and 17*radius+f < 1


def close_run_interval(n: int, lag: int, steps: int, radius: Q) -> tuple[Q, Q]:
    """Exact initial interval for steps+1 consecutive close lag observations.

    Requires the stated small-arc carry gate. Monotonic forcing makes the
    first-time check sufficient. The interval concerns a centered lag state;
    the actual selected state must still be tested for membership.
    """
    _int(steps)
    radius = _radius(radius)
    if not close_run_gate(n, lag, radius):
        raise ValueError("requires f_n<=15 radius and 17 radius+f_n<1")
    middle = sum((forcing_gap(n+i, lag)/16**(i+1) for i in range(steps)), Q(0))
    halfwidth = radius/16**steps
    return middle-halfwidth, middle+halfwidth


def nonpositive_escape_bound(n: int, lag: int, steps: int, radius: Q) -> bool:
    """True certifies impossibility of this close run starting at centered lag<=0.

    A sufficient strict beta-integral inequality is checked. False means the
    bound is inconclusive, not that the authentic trajectory realizes the run.
    """
    _int(steps, 1)
    radius = _radius(radius)
    if not close_run_gate(n, lag, radius):
        raise ValueError("close-run gate failed")
    lower, _ = forcing_gap_bounds(n+steps-1, lag)
    return (16**steps-1)*lower > 15*radius


@dataclass(frozen=True)
class LagCounts:
    length: int
    per_lag: tuple[int, ...]  # index lag-1

    @property
    def ordered_pairs(self) -> int:
        return self.length+2*sum(self.per_lag)


def lag_close_counts(path: CarryPath, start: int, length: int, radius: Q) -> LagCounts:
    _int(start)
    _int(length, 1)
    radius = _radius(radius)
    if start+length > len(path.states):
        raise ValueError("window exceeds source path")
    values = path.states[start:start+length]
    counts = tuple(sum(abs(centered(values[i+lag]-values[i])) <= radius
                       for i in range(length-lag)) for lag in range(1, length))
    return LagCounts(length, counts)


def repeated_clock_pairs(length: int, period: int) -> int:
    """Ordered index pairs with equal clock phase; includes diagonal."""
    _int(length, 1)
    _int(period, 1)
    quotient, remainder = divmod(length, period)
    return remainder*(quotient+1)**2+(period-remainder)*quotient**2
