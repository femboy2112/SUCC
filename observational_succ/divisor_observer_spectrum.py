"""Exact finite core for the divisor observer's spectral/commutator obstruction.

The operator is the existing T = J* S_A J, with coefficient
1/sqrt(d(n)d(m)) on m=n+b, b|n.  Rational vectors below use the weighted
frame x(n)=sqrt(d(n))*g(n); their norm is sum d(n)|g(n)|^2.  This frame is
not a probability law.  Formal phase sums are group-algebra identities;
no approximate complex evaluation or normality certification is performed.

Proofs: research/2026-10-28/BBP_SIGNED_OBSERVER_AUDIT.md.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
from typing import Mapping, Sequence

from observational_succ.bbp_natural_carrier import exact_forcing
from observational_succ.origin_fiber_arithmetic_observer import d, divisors


def _natural(value: int, name: str, *, positive: bool = False) -> int:
    if type(value) is not int or value < int(positive):
        raise ValueError(f"{name} must be a {'positive ' if positive else ''}integer")
    return value


def divisor_summatory(limit: int) -> int:
    """D(N)=#{(a,b)>0: ab<=N}, by grouped floor quotients."""
    _natural(limit, "limit")
    total, left = 0, 1
    while left <= limit:
        quotient = limit // left
        right = limit // quotient
        total += (right - left + 1) * quotient
        left = right + 1
    return total


def boundary_multiplicities(limit: int) -> tuple[int, ...]:
    """c_N(n)=#{b|n: n+b>N}, indexed by n-1, via fiber endpoints."""
    _natural(limit, "limit", positive=True)
    counts = [0] * limit
    for b in range(1, limit + 1):
        counts[b * (limit // b) - 1] += 1
    return tuple(counts)


def sharp_commutator_bound(limit: int) -> Q:
    """Exact supremum of |<x_N,[M_f,T]x_N>| over |f|<=1."""
    _natural(limit, "limit", positive=True)
    return Q(2 * (limit // 2), divisor_summatory(limit))


def hyperbolic_shell_receipt(limit: int, cutoff: int = 0) -> dict:
    """Exact finite Rayleigh receipt for sqrt(d(n))*1_{cutoff<n<=limit}.

    The residual bounds apply to both (I-T)x and Lx, L=I-Re(T).
    For limit>=2*cutoff every b<=limit is active, including hard origin pins.
    """
    _natural(limit, "limit", positive=True)
    _natural(cutoff, "cutoff")
    if cutoff >= limit:
        raise ValueError("cutoff must be smaller than limit")
    mass = divisor_summatory(limit) - divisor_summatory(cutoff)
    active = sum(limit // b > cutoff // b for b in range(1, limit + 1))
    return {
        "limit": limit,
        "cutoff": cutoff,
        "squared_unnormalized_norm": mass,
        "active_pair_fibers": active,
        "internal_edges": mass - active,
        "T_rayleigh": Q(mass - active, mass),
        "L_rayleigh": Q(active, mass),
        "residual_squared_upper": Q(2 * active, mass),
    }


def _rational_vector(values: Mapping[int, Q]) -> dict[int, Q]:
    result = {}
    for n, value in values.items():
        _natural(n, "source index", positive=True)
        if not isinstance(value, (int, Q)) or isinstance(value, bool):
            raise TypeError("exact rational weighted-frame amplitudes required")
        if value:
            result[n] = Q(value)
    return result


def apply_compressed_rational(values: Mapping[int, Q]) -> dict[int, Q]:
    """Apply T in its rational weighted frame; this is NOT a Markov kernel."""
    result = defaultdict(Q)
    for n, value in _rational_vector(values).items():
        for b in divisors(n):
            m = n + b
            result[m] += value / d(m)
    return {n: value for n, value in result.items() if value}


def apply_adjoint_rational(values: Mapping[int, Q]) -> dict[int, Q]:
    """Apply T* in the SAME weighted frame (not an unweighted transpose)."""
    result = defaultdict(Q)
    for m, value in _rational_vector(values).items():
        for b in divisors(m):
            if b < m:
                n = m - b
                result[n] += value / d(n)
    return {n: value for n, value in result.items() if value}


def weighted_inner(left: Mapping[int, Q], right: Mapping[int, Q]) -> Q:
    """Real rational inner product in x(n)=sqrt(d(n))*g(n) coordinates."""
    lhs, rhs = _rational_vector(left), _rational_vector(right)
    return sum((d(n) * value * rhs.get(n, Q()) for n, value in lhs.items()), Q())


def exact_shell_residuals(limit: int, cutoff: int = 0) -> dict[str, Q]:
    """Explicit compressed residuals, independent of the fiber count bound."""
    receipt = hyperbolic_shell_receipt(limit, cutoff)
    vector = {n: Q(1) for n in range(cutoff + 1, limit + 1)}
    forward = apply_compressed_rational(vector)
    backward = apply_adjoint_rational(vector)
    support = vector.keys() | forward.keys() | backward.keys()
    residual_t = {n: vector.get(n, Q()) - forward.get(n, Q()) for n in support}
    residual_l = {
        n: vector.get(n, Q()) - (forward.get(n, Q()) + backward.get(n, Q())) / 2
        for n in support
    }
    mass = receipt["squared_unnormalized_norm"]
    return {
        "I_minus_T_squared_norm": weighted_inner(residual_t, residual_t) / mass,
        "L_squared_norm": weighted_inner(residual_l, residual_l) / mass,
        "L_rayleigh": weighted_inner(vector, residual_l) / mass,
    }


def original_bbp_turns(limit: int, frequency: int = 1, *, seed: Q = Q()) -> tuple[Q, ...]:
    """Actual original forcing; seed=0 is authentic, other seeds are controls.

    Returns h*U_n modulo 1 for n=1,...,limit.  Integer 16 permits reducing
    each step modulo 1 without changing any phase.  No pi digits are inputs.
    """
    _natural(limit, "limit", positive=True)
    if type(frequency) is not int:
        raise ValueError("integer Fourier frequency required")
    if not isinstance(seed, (int, Q)) or isinstance(seed, bool):
        raise TypeError("rational seed required; the coherent irrational seed is analytic")
    state, turns = Q(seed) % 1, []
    for n in range(1, limit + 1):
        state = (16 * state + exact_forcing(n)) % 1
        turns.append((frequency * state) % 1)
    return tuple(turns)


def _turns(values: Sequence[Q]) -> tuple[Q, ...]:
    if not values:
        raise ValueError("nonempty exact rational phase turns required")
    if any(not isinstance(v, (int, Q)) or isinstance(v, bool) for v in values):
        raise TypeError("phase turns must be exact rationals")
    return tuple(Q(value) % 1 for value in values)


def formal_phase_sum(turns: Sequence[Q], coefficients: Sequence[int | Q]) -> dict[Q, Q]:
    """Finite sum c_t*[t] in Q[Q/Z]; evaluation [t]->exp(2 pi i t) is separate."""
    phase = _turns(turns)
    if len(phase) != len(coefficients):
        raise ValueError("one coefficient per phase required")
    result = defaultdict(Q)
    for turn, coefficient in zip(phase, coefficients):
        if not isinstance(coefficient, (int, Q)) or isinstance(coefficient, bool):
            raise TypeError("exact rational coefficients required")
        result[turn] += Q(coefficient)
    return {turn: value for turn, value in result.items() if value}


def formal_commutator_numerator(turns: Sequence[Q]) -> dict[Q, Q]:
    """D(N)<x_N,[M_f,T]x_N>, computed directly from internal edges."""
    phase = _turns(turns)
    limit = len(phase)
    result = defaultdict(Q)
    for n in range(1, limit + 1):
        for b in divisors(n):
            m = n + b
            if m <= limit:
                result[phase[m - 1]] += 1
                result[phase[n - 1]] -= 1
    return {turn: value for turn, value in result.items() if value}


def formal_boundary_minus_weyl(turns: Sequence[Q]) -> dict[Q, Q]:
    """Same signed numerator from the independently enumerated fiber boundary."""
    phase = _turns(turns)
    return formal_phase_sum(phase, tuple(c - 1 for c in boundary_multiplicities(len(phase))))


def gauge_cycle_turn(turns: Sequence[Q], cycle: Sequence[int]) -> Q:
    """Holonomy turn of an actual undirected divisor-graph closed walk.

    Edge label is phase(target)-phase(source); every such holonomy is zero.
    This checks phase transport, not the source's signed Weyl sum.
    """
    phase = _turns(turns)
    if len(cycle) < 2 or cycle[0] != cycle[-1]:
        raise ValueError("a closed walk including its repeated endpoint is required")
    total = Q()
    for n, m in zip(cycle, cycle[1:]):
        for index in (n, m):
            _natural(index, "cycle index", positive=True)
            if index > len(phase):
                raise ValueError("cycle index exceeds phase horizon")
        low, high = sorted((n, m))
        if low == high or low % (high - low):
            raise ValueError("walk uses a non-divisor edge")
        total += phase[m - 1] - phase[n - 1]
    return total % 1
