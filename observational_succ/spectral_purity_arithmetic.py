"""Relative cyclotomic traces of authentic BBP matrix innovations.

The source is the original four signed poles and U_0=0. Relative traces
fix the complete previous cyclotomic history; they are NOT estimates at
the selected complex embedding. A trace is evaluated in the cyclotomic
quotient, not asserted equal to its preimage in Q[Q/Z].
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt, lcm

from .pi_joint_prime_carrier import denominator_primes, local_primary, primes_through
from .succ_internal_matrix_walk import PhasePoly, authentic_r


def _integer(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"integer >= {minimum} required")
    return value


def _prime(p: int) -> int:
    _integer(p, 3)
    if p % 2 == 0 or denominator_primes(p) != {p: 1}:
        raise ValueError("genuine odd prime required")
    return p


def _depth(denominator: int, p: int) -> int:
    answer = 0
    while denominator % p == 0:
        denominator //= p
        answer += 1
    return answer


def fejer_overlap(history: tuple[Q, ...], arrival: Q, width: int) -> PhasePoly:
    """Exact formal overlap with the specified rational history.

    A generic algebraic instrument; source membership is checked separately
    by source_trace_certificate. No evaluation or sign decision is made.
    """
    _integer(width, 1)
    if not history or any(type(x) is not Q for x in history) or type(arrival) is not Q:
        raise ValueError("nonempty exact Fraction history and arrival required")
    result = PhasePoly.monomial(0, width)
    for frequency in range(1, width):
        coefficient = Q(width-frequency, len(history))
        for old in history:
            result += PhasePoly.monomial(frequency*(arrival-old), coefficient)
            result += PhasePoly.monomial(-frequency*(arrival-old), coefficient)
    return result


def relative_cyclotomic_trace(polynomial: PhasePoly, p: int,
                              old_depth: int) -> PhasePoly:
    """Representative for normalized trace fixing p**old_depth and all p-free roots.

    If old_depth>=1, the p-power kernel kills phases deeper than old_depth.
    If old_depth=0, a nontrivial p-root has unit-average -1/(p-1), and
    primitive p**a roots for a>=2 have unit-average zero. These are exact
    cyclotomic relations, not formal group-algebra equalities.
    """
    if type(polynomial) is not PhasePoly:
        raise ValueError("formal phase polynomial required")
    _prime(p)
    _integer(old_depth)
    result = PhasePoly.zero()
    for phase, coefficient in polynomial.terms:
        primary = local_primary(phase, p)
        depth = _depth(primary.denominator, p)
        if depth <= old_depth:
            result += PhasePoly.monomial(phase, coefficient)
        elif old_depth == 0 and depth == 1:
            result += PhasePoly.monomial(phase-primary, -coefficient/Q(p-1))
    return result


@dataclass(frozen=True)
class SourceTraceCertificate:
    source_id: str
    arrival_index: int
    width: int
    prime: int
    old_depth: int
    new_depth: int
    old_conductor: int
    new_conductor: int
    original_lift: Q
    p_primary_phase: Q
    p_free_complement: Q
    selected_innovation: PhasePoly
    traced_innovation: PhasePoly
    predicted_trace: PhasePoly
    evaluated_trace_upper: Q
    selected_bound_proved: bool = False


def source_trace_certificate(n: int, width: int, p: int) -> SourceTraceCertificate:
    """Authenticate one conductor-birth trace without replacing the original source.

    Requires n>=2, 1<=H<=p and a new p layer at n. The prior observations
    are U_1,...,U_(n-1); the arrival is U_n. Other new prime channels are
    FIXED, not averaged independently or discarded.
    """
    _integer(n, 2)
    _integer(width, 1)
    _prime(p)
    if n > 2000 or width > min(p, 64):
        raise ValueError("declared finite budget or H<=p violated")
    history = []
    state, old_conductor = Q(), 1
    for time in range(1, n):
        force = authentic_r(time)
        state = 16*state+force
        history.append(state)
        old_conductor = lcm(old_conductor, force.denominator)
    force = authentic_r(n)
    new_conductor = lcm(old_conductor, force.denominator)
    arrival = 16*state+force
    old_depth = _depth(old_conductor, p)
    new_depth = _depth(new_conductor, p)
    if new_depth != old_depth+1:
        raise ValueError("a single new authentic p-power layer is required")
    if _depth(arrival.denominator, p) != new_depth:
        raise ArithmeticError("new source layer canceled unexpectedly")
    primary = local_primary(arrival, p)
    complement = arrival-primary
    selected = fejer_overlap(tuple(history), arrival, width)
    traced = relative_cyclotomic_trace(selected, p, old_depth)
    if old_depth:
        predicted = PhasePoly.monomial(0, width)
        upper = Q(width)
    else:
        complement_overlap = fejer_overlap(tuple(history), complement, width)
        predicted = (PhasePoly.monomial(0, p*width)-complement_overlap)/(p-1)
        upper = Q(p*width, p-1)
    if traced != predicted:
        raise ArithmeticError("relative trace and matrix formula disagree")
    return SourceTraceCertificate(
        "Q:Coherent-Main-X-four-pole-BBP", n, width, p, old_depth, new_depth,
        old_conductor, new_conductor, arrival, primary, complement,
        selected, traced, predicted, upper,
    )


@dataclass(frozen=True)
class ConductorGrowthCertificate:
    horizon: int
    growth_times: tuple[int, ...]
    layers: tuple[tuple[int, int, int], ...]
    available_prime_power_count: int
    weighted_flat_steps: int
    total_step_weight: int


def prescribed_width(horizon: int) -> int:
    """Predetermined H_N=max(2,1+floor(sqrt(floor(log_2 N))))."""
    _integer(horizon, 1)
    return max(2, 1+isqrt(horizon.bit_length()-1))


def conductor_growth_count_upper(horizon: int) -> Q:
    """Universal rational Chebyshev bound; no source spectrum is measured.

    For X=8N, L=floor(log_2 X), K=ceil(log_2 X), the total prime-power
    count is <= L*floor(sqrt(X)) + 4*(2**K-1)/L. See paper AR-5.
    The min with N is the trivial number-of-time-steps bound.
    """
    _integer(horizon, 1)
    x = 8*horizon
    lower_log = x.bit_length()-1
    upper_log = (x-1).bit_length()
    cap = Q(lower_log*isqrt(x)) + Q(4*(2**upper_log-1), lower_log)
    return min(Q(horizon), cap)


def conductor_birth_innovation_budget(horizon: int) -> Q:
    """All-N upper bound for absolute normalized innovation on birth steps.

    At the prescribed width this tends to zero by an elementary all-N
    proof. This is an AUTHENTIC SOURCE partial-timeline saving, not a
    bound for conductor-flat steps or for total spectral excess.
    """
    width = prescribed_width(horizon)
    return Q(2*(width-1), horizon)*conductor_growth_count_upper(horizon)


def conductor_locked_countermodel(horizon: int) -> dict:
    """Positive WRONG source with exactly the authentic conductor tower.

    U*_n=16**n-1/Q_n and r*_n=16/Q_(n-1)-1/Q_n. The initial state
    remains zero and all selected circle phases converge to zero. This
    deliberately changes the four-pole law and the carry history.
    """
    _integer(horizon, 1)
    if horizon > 2000:
        raise ValueError("countermodel finite budget exceeded")
    states, forcing, conductors = [Q()], [], [1]
    for n in range(1, horizon+1):
        q = lcm(conductors[-1], authentic_r(n).denominator)
        force = Q(16, conductors[-1])-Q(1, q)
        state = Q(16**n)-Q(1, q)
        if force <= 0 or state != 16*states[-1]+force or state.denominator != q:
            raise ArithmeticError("exact-conductor counterfeit failed")
        conductors.append(q)
        forcing.append(force)
        states.append(state)
    return {"source_id": "COUNTERMODEL:authentic-conductor-positive-forcing",
            "authentic_four_pole_source": False,
            "states": tuple(states), "forcing": tuple(forcing),
            "conductors": tuple(conductors)}


def conductor_growth_certificate(horizon: int) -> ConductorGrowthCertificate:
    """Exact source classification independent of measured Fejer defects.

    Growth at arrival n is Q_n>Q_(n-1). For innovations m=n-1, flat
    steps have total weight sum(m). The prime-power injection proves the
    all-N count bound in the paper; this function verifies finite cases.
    """
    _integer(horizon, 1)
    if horizon > 10000:
        raise ValueError("finite conductor certificate budget exceeded")
    previous: dict[int, int] = {}
    growth, layers = [], []
    candidate_primes = primes_through(8*horizon)
    for n in range(1, horizon+1):
        factors = denominator_primes(authentic_r(n).denominator,
                                     candidate_primes)
        changed = False
        for p, a in factors.items():
            old = previous.get(p, 0)
            for depth in range(old+1, a+1):
                layers.append((n, p, depth))
                if p**depth > 8*horizon:
                    raise ArithmeticError("source prime-power size bound failed")
                changed = True
            previous[p] = max(old, a)
        if changed:
            growth.append(n)
    available = 0
    for p in candidate_primes:
        if p == 2:
            continue
        power = p
        while power <= 8*horizon:
            available += 1
            power *= p
    if len(growth) > len(layers) or len(layers) > available:
        raise ArithmeticError("prime-power injection bound failed")
    total = horizon*(horizon-1)//2
    weighted_growth = sum(n-1 for n in growth)
    return ConductorGrowthCertificate(horizon, tuple(growth), tuple(layers),
                                     available, total-weighted_growth, total)
