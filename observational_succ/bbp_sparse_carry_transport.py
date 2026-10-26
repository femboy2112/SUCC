"""Exact instruments for source-labelled sparse carry censoring.

The source stays the original four signed BBP poles and zero initial lift.
Censoring defines a NONCAUSAL derived observable, not an alternate source.
The all-N theorem bounds transport error, not either history's Fourier energy.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt, lcm

from .spectral_purity_arithmetic import conductor_growth_count_upper
from .succ_internal_matrix_walk import authentic_r


def _nat(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"ordinary integer >= {minimum} required")
    return value


@dataclass(frozen=True)
class CarryKernelBudget:
    frequency: int
    cutoff: int
    mass_upper: Q
    first_moment_upper: Q


def carry_kernel_budget(frequency: int) -> CarryKernelBudget:
    """Bound sum w_j and sum j*w_j for w_j=min(2,112*|h|/16**j).

    The first moment pays for EVERY unknown carry after the horizon.
    The cutoff is computed with integers, with no logarithm rounding.
    """
    if type(frequency) is not int:
        raise ValueError("ordinary integer frequency required")
    h = abs(frequency)
    if not h:
        return CarryKernelBudget(0, 0, Q(), Q())
    cutoff, power = 0, 1
    while power < 56*h:
        cutoff, power = cutoff+1, 16*power
    mass = Q(2*cutoff)+Q(2, 15)
    moment = Q(cutoff*(cutoff+1))+Q(2*(cutoff+1), 15)+Q(2, 225)
    return CarryKernelBudget(h, cutoff, mass, moment)


def sparse_carry_width(horizon: int) -> int:
    """Predeclared H=max(2,1+floor(floor(log_2 N)**(3/2)))."""
    _nat(horizon, 1)
    t = horizon.bit_length()-1
    return max(2, 1+isqrt(t**3))


def sparse_carry_mode_upper(horizon: int, frequency: int,
                           changed_count: int) -> Q:
    """Normalized character error for <=16 carry changes on E.

    changed_count counts E in [1,N]; future E is unrestricted. This is
    a generic conditional instrument, not a source-membership assertion.
    """
    _nat(horizon, 1)
    _nat(changed_count)
    if changed_count > horizon:
        raise ValueError("changed-count exceeds horizon")
    budget = carry_kernel_budget(frequency)
    return (budget.mass_upper*changed_count+budget.first_moment_upper)/horizon


@dataclass(frozen=True)
class BirthCarryBudget:
    horizon: int
    width: int
    birth_count_upper: Q
    mode_error_upper: Q
    root_energy_error_squared_upper: Q
    purity_proved: bool = False


def birth_carry_budget(horizon: int, width: int | None = None) -> BirthCarryBudget:
    """All-N arithmetic upper bound on root-energy TRANSPORT error squared.

    It tends to zero at sparse_carry_width(N). No small-energy assertion
    is made for the original or birth-censored selected history.
    """
    _nat(horizon, 1)
    h = sparse_carry_width(horizon) if width is None else _nat(width, 1)
    count = conductor_growth_count_upper(horizon)
    kernel = carry_kernel_budget(h-1)
    mode = (kernel.mass_upper*count+kernel.first_moment_upper)/horizon
    return BirthCarryBudget(horizon, h, count, mode, (h-1)*mode**2)


def truncation_depth(horizon: int, width: int) -> int:
    """Smallest J with 16**J >= N*H**2; deterministic future-read budget."""
    _nat(horizon, 1)
    _nat(width, 1)
    j, power = 0, 1
    while power < horizon*width**2:
        j, power = j+1, 16*power
    return j


def carry_tail_upper(depth: int) -> Q:
    """Uniform remainder of a nonnegative carry profile with c_t<=16."""
    _nat(depth)
    return Q(16, 15*16**depth)


def truncation_root_error_squared(width: int, depth: int) -> Q:
    """Minkowski error squared for truncating any such carry profile."""
    _nat(width, 1)
    _nat(depth)
    return Q(112, 15*16**depth)**2 * Q(width*(width**2-1), 6)


def finite_carry_profile(carries, start: int, depth: int,
                         removed_times=()) -> Q:
    """Generic exact sum of c_(start+j)/16**j, j=1..depth.

    carries[t-1] means c_t. This helper authenticates no source; callers
    must retain the original tape when using the source-specific theorem.
    """
    _nat(start)
    _nat(depth)
    tape = tuple(carries)
    removed = frozenset(removed_times)
    if (len(tape) < start+depth or
            any(type(c) is not int or not 0 <= c <= 16 for c in tape) or
            any(type(t) is not int or t < 1 for t in removed)):
        raise ValueError("bounded integer carry tape and positive removal indices required")
    return sum((Q(tape[start+j-1], 16**j)
                for j in range(1, depth+1) if start+j not in removed), Q())


@dataclass(frozen=True)
class AuthenticCarryPoint:
    time: int
    forcing: Q
    lift: Q
    conductor: int
    carry: int
    conductor_birth: bool


@dataclass(frozen=True)
class AuthenticCarryProfiles:
    source_id: str
    horizon: int
    depth: int
    source: tuple[AuthenticCarryPoint, ...]
    full_prefixes: tuple[Q, ...]
    birth_censored_prefixes: tuple[Q, ...]
    uniform_tail_upper: Q


def authentic_carry_profiles(horizon: int, depth: int) -> AuthenticCarryProfiles:
    """Exact original-source profiles at n=1..N using carries through N+J.

    The output prefixes alone are NOT the infinite observable: every
    omitted future tail is enclosed by uniform_tail_upper.
    """
    _nat(horizon, 1)
    _nat(depth)
    if horizon+depth > 2000:
        raise ValueError("declared exact source prefix budget exceeded")
    source, state, conductor = [], Q(), 1
    for n in range(1, horizon+depth+1):
        forcing = authentic_r(n)
        arrival = 16*state+forcing
        next_conductor = lcm(conductor, forcing.denominator)
        carry = arrival.__floor__()-16*state.__floor__()
        if not 0 <= carry <= 16:
            raise ArithmeticError("authentic carry bound failed")
        source.append(AuthenticCarryPoint(n, forcing, arrival, next_conductor,
                                          carry, next_conductor != conductor))
        state, conductor = arrival, next_conductor
    carries = tuple(point.carry for point in source)
    births = frozenset(point.time for point in source if point.conductor_birth)
    full = tuple(finite_carry_profile(carries, n, depth)
                 for n in range(1, horizon+1))
    censored = tuple(finite_carry_profile(carries, n, depth, births)
                     for n in range(1, horizon+1))
    return AuthenticCarryProfiles("Q:Coherent-Main-X-four-pole-BBP", horizon,
                                  depth, tuple(source), full, censored,
                                  carry_tail_upper(depth))
