"""Positive nonnormal countermodel with every BBP carry and common conductor.

This deliberately CHANGES the forcing. It retains the original source only
as a labelled input tape of carries and conductors. The universal proof is
in BBP_POSITIVE_CARRY_CONTROL.md; finite executions are not normality tests.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import lcm

from .succ_internal_matrix_walk import authentic_r


def _index(n, minimum=0, maximum=2000):
    if type(n) is not int or not minimum <= n <= maximum:
        raise ValueError("bounded ordinary integer required")
    return n


@dataclass(frozen=True)
class PositiveCarryPoint:
    time: int
    authentic_lift: Q
    authentic_forcing: Q
    common_conductor: int
    carry: int
    control_phase: Q
    control_lift: Q
    control_forcing: Q
    reset: bool
    authentic_zero_phase: bool


def positive_carry_control(horizon: int) -> tuple[PositiveCarryPoint, ...]:
    """Construct a finite prefix of ONE prescribed all-time changed source.

    If authentic x_n=0, set y_n=0. Otherwise set
      y_n=max(1/Q_n,16*y_(n-1)-c_n+1/Q_n).
    Every carry c_n, zero-phase event, and cumulative conductor Q_n is
    retained. The derived forcing is positive but has nonvanishing spikes.
    """
    _index(horizon)
    source = old_control = old_phase = Q()
    conductor = control_conductor = 1
    result = []
    for n in range(1, horizon+1):
        forcing = authentic_r(n)
        old_source = source
        source = 16*old_source+forcing
        conductor = lcm(conductor, forcing.denominator)
        carry = source.__floor__()-16*old_source.__floor__()
        phase = source % 1
        epsilon = Q(1, conductor)
        zero = phase == 0
        reset = zero or 16*old_phase <= carry
        control_phase = Q() if zero else max(epsilon, 16*old_phase-carry+epsilon)
        control = Q(source.__floor__())+control_phase
        control_forcing = control-16*old_control
        control_conductor = lcm(control_conductor, control_forcing.denominator)
        if not (0 <= control_phase <= phase < 1):
            raise ArithmeticError("phase domination failed")
        if control_forcing <= 0:
            raise ArithmeticError("positive-forcing control failed")
        if (16*old_phase+control_forcing).__floor__() != carry:
            raise ArithmeticError("authentic carry tape changed")
        if control_conductor != conductor:
            raise ArithmeticError("cumulative conductor tower changed")
        if control_phase == 0 and not zero:
            raise ArithmeticError("zero-phase event changed")
        result.append(PositiveCarryPoint(n, source, forcing, conductor, carry,
                                        control_phase, control, control_forcing,
                                        reset, zero))
        old_phase, old_control = control_phase, control
    return tuple(result)


def quartic_conductor_lower(n: int) -> Q:
    """All-n strict lower bound Q_n>(2n-1)^4/(7*11*13*17).

    For p in {7,11,13,17}, every p**a<=2n-1 appears at the source
    index (p**a+1)/2, in the pole 2j-1, without p cancellation.
    """
    _index(n, 1, 10**25)
    return Q((2*n-1)**4, 17017)


def positive_control_tail_constants() -> dict:
    """Exact constants for the paper's eventual y_n<=4B/n² theorem.

    A reset exists between A+1 and A+10. Thereafter zero-carry runs
    cannot amplify the conductor-grid floor enough to prevent resets.
    """
    a = 20000
    b = Q(16384*17017, 15)
    if not b/a**2 < Q(1, 16):
        raise ArithmeticError("zero-run reset threshold failed")
    if not Q(16**9, 32*(a+1)**2) > 1:
        raise ArithmeticError("ten-step bootstrap expansion failed")
    if a*a < 32*17017:
        raise ArithmeticError("forcing-minus-grid lower bound failed")
    return {"reset_threshold": a, "bootstrap_steps": 10,
            "zero_run_phase_constant": b, "eventual_phase_constant": 4*b,
            "eventual_start": a+10,
            "total_phase_mass_upper": Q(a+9)+4*b/Q(a+9),
            "authentic_four_pole_forcing": False,
            "vanishing_forcing_preserved": False}


def backward_phase_prefix(forcing_difference, depth: int) -> Q:
    """Finite backward Green sum for a specified difference tape.

    If two bounded fractional histories share carries, their phase
    difference equals this value plus a remainder at most 16**(-depth).
    Caller authenticates that common-carry premise; this is pure algebra.
    """
    _index(depth, 0, 2000)
    tape = tuple(forcing_difference)
    if len(tape) < depth or any(type(x) not in (int, Q) for x in tape):
        raise ValueError("enough exact rational forcing differences required")
    return -sum((Q(tape[j-1], 16**j) for j in range(1, depth+1)), Q())
