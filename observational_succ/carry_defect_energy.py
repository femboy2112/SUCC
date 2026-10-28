"""Exact all-center carry counts and finite signed Green energy.

These are finite instruments. The all-cut count lower bound does not prove
that the authentic counts grow. Full Green minimization is exactly circular
quadratic variance, not an independent arithmetic saving or normality proof.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q

from .succ_internal_matrix_walk import authentic_r


def _integer(value, minimum=0, maximum=None):
    if type(value) is not int or value < minimum:
        raise ValueError("ordinary integer outside the declared domain")
    if maximum is not None and value > maximum:
        raise ValueError("finite exact certificate budget exceeded")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _floor(value):
    return value.numerator // value.denominator


def fractional_part(value):
    value = _rational(value)
    return value - _floor(value)


def authentic_window(start, transitions):
    """Replay U_start,...,U_(start+T), with the literal zero seed and poles."""
    _integer(start, 0, 2000)
    _integer(transitions, 1, 128)
    if start + transitions > 2000:
        raise ValueError("finite exact source budget exceeded")
    value = Q()
    states = [value] if start == 0 else []
    for n in range(1, start + transitions + 1):
        value = 16 * value + authentic_r(n)
        if n >= start:
            states.append(value)
    forcing = tuple(authentic_r(start + i + 1) for i in range(transitions))
    return tuple(states), forcing


def authenticate_window(states, forcing, start):
    """Generic recurrence validity alone does not authenticate the zero seed."""
    states = tuple(_rational(x) for x in states)
    forcing = tuple(_rational(x) for x in forcing)
    expected = authentic_window(start, len(forcing))
    if (states, forcing) != expected:
        raise ValueError("window fails the original four-pole zero-source passport")


def green_kernel(transitions):
    """Exact inverse of diag(257), offdiag(-16), with both finite boundaries."""
    t = _integer(transitions, 1, 128)
    denominator = 255 * (16 ** (2 * (t + 1)) - 1)
    return tuple(tuple(
        Q(16 ** abs(j-i) * (16 ** (2 * (min(i, j)+1)) - 1)
          * (16 ** (2 * (t-max(i, j))) - 1), denominator)
        for j in range(t)) for i in range(t))


@dataclass(frozen=True)
class GreenEnergy:
    squared_norm: Q
    signed_forcing_energy: Q
    homogeneous_boundary_energy: Q
    weighted_endpoint_remainder: Q


def green_energy(offsets):
    """Exact decomposition, including the homogeneous direction 16^i."""
    q = tuple(_rational(x) for x in offsets)
    t = _integer(len(q)-1, 1, 128)
    a = tuple(q[i+1]-16*q[i] for i in range(t))
    kernel = green_kernel(t)
    signed = sum((a[i]*kernel[i][j]*a[j]
                  for i in range(t) for j in range(t)), Q())
    v = tuple(16**i for i in range(t+1))
    boundary = sum((x*y for x, y in zip(q, v)), Q())**2 / sum(x*x for x in v)
    norm = sum((x*x for x in q), Q())
    remainder = 16*sum(((q[i+1]+q[i])**2 for i in range(t)), Q())
    if norm != signed + boundary:
        raise ArithmeticError("signed Green/boundary decomposition failed")
    if 289*norm-17*q[0]**2-272*q[-1]**2-sum((x*x for x in a), Q()) != remainder:
        raise ArithmeticError("signed endpoint identity failed")
    return GreenEnergy(norm, signed, boundary, remainder)


@dataclass(frozen=True)
class CutSlice:
    left: Q
    right: Q
    lifted_phases: tuple[Q, ...]
    integer_branches: tuple[int, ...]
    nonmodal_count: int
    unequal_pairs: int
    minimizing_center: Q
    minimum_squared_distance: Q


@dataclass(frozen=True)
class CutCertificate:
    frequency: int
    fractional_phases: tuple[Q, ...]
    literal_carries: tuple[int, ...]
    forcing_span: Q
    cuts: tuple[CutSlice, ...]

    @property
    def transitions(self):
        return len(self.literal_carries)

    @property
    def minimum_nonmodal_count(self):
        return min(c.nonmodal_count for c in self.cuts)

    @property
    def minimum_unequal_pairs(self):
        return min(c.unequal_pairs for c in self.cuts)

    @property
    def circular_squared_distance(self):
        return min(c.minimum_squared_distance for c in self.cuts)

    @property
    def modal_loss_lower(self):
        gap = max(Q(), 1-self.forcing_span)
        return Q(4, 289)*gap**2*self.minimum_nonmodal_count

    @property
    def pair_loss_lower(self):
        gap = max(Q(), 1-self.forcing_span)
        return Q(8, 289*self.transitions)*gap**2*self.minimum_unequal_pairs

    @property
    def quadratic_loss_lower(self):
        return 8*self.circular_squared_distance


def all_center_certificate(states, forcing, frequency=1):
    """Enumerate all rational cut intervals, never estimate a complex center.

    The input must satisfy every exact ordered recurrence. This is a generic
    finite theorem; use authenticate_window separately for the BBP zero seed.
    Cut endpoints admit both centered lifts. Both adjacent closed intervals
    are retained, so no boundary observation or phase tie is discarded.
    """
    states = tuple(_rational(x) for x in states)
    forcing = tuple(_rational(x) for x in forcing)
    t = _integer(len(forcing), 1, 128)
    if type(frequency) is not int or frequency == 0:
        raise ValueError("nonzero integer frequency required")
    if len(states) != t+1 or any(states[i+1] != 16*states[i]+forcing[i]
                                for i in range(t)):
        raise ValueError("ordered exact recurrence fails")
    h = frequency
    phases = tuple(fractional_part(h*x) for x in states)
    carries_q = tuple(16*phases[i]+h*forcing[i]-phases[i+1] for i in range(t))
    if any(x.denominator != 1 for x in carries_q):
        raise ArithmeticError("literal frequency carry is not integral")
    carries = tuple(int(x) for x in carries_q)
    endpoints = sorted({fractional_part(s+Q(1, 2)) for s in phases})
    intervals = zip(endpoints, endpoints[1:]+[endpoints[0]+1])
    cuts = []
    for left, right in intervals:
        midpoint = (left+right)/2
        shifts = tuple(_floor(s-midpoint+Q(1, 2)) for s in phases)
        b = tuple(s-j for s, j in zip(phases, shifts))
        branches = tuple(-carries[i]-shifts[i+1]+16*shifts[i] for i in range(t))
        if any(b[i+1]-16*b[i]-h*forcing[i] != branches[i] for i in range(t)):
            raise ArithmeticError("carry/cut sign identity failed")
        counts = Counter(branches)
        nonmodal = t-max(counts.values())
        pairs = (t*t-sum(n*n for n in counts.values()))//2
        center = min(right, max(left, sum(b, Q())/len(b)))
        cost = sum(((x-center)**2 for x in b), Q())
        cuts.append(CutSlice(left, right, b, branches, nonmodal, pairs, center, cost))
    span = abs(h)*(max(forcing)-min(forcing))
    return CutCertificate(h, phases, carries, span, tuple(cuts))
