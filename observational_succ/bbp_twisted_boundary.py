"""Exact affine seams for the unchanged BBP recurrence.

A finite endpoint seam selects an initial state; it does not make the
nonperiodic forcing cyclic.  These routines preserve exact rational arithmetic
and report source-selection failures explicitly.  Infinite-tail enclosures
come from the inherited source-only rational interval theorem.

Proofs and scope: research/2026-10-25/BBP_TWISTED_BOUNDARY.md.
"""
from __future__ import annotations

from fractions import Fraction as Q

from .bbp_resonance_controls import exact_forced_history
from .bbp_source_memory import forcing, tail_interval


def _natural(value: int, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError("integer in the declared domain required")
    return value


def _exact(value: Q | int) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def solve_affine_seam(horizon: int, multiplier: Q | int,
                      offset: Q | int = 0) -> dict:
    """Solve X_N = multiplier*X_0 + offset, with authentic forcing.

    kind is 'unique', 'all', or 'none'.  In the singular all-solutions case,
    initial=None means every real initial value, not a preferred seed.
    Authentic U_0=0 is compatible exactly when offset=U_N.
    """
    _natural(horizon, 1)
    multiplier, offset = _exact(multiplier), _exact(offset)
    terminal = exact_forced_history(horizon)[-1]
    denominator = 16**horizon - multiplier
    numerator = offset - terminal
    if denominator:
        kind, initial = "unique", numerator / denominator
    else:
        kind, initial = ("all" if numerator == 0 else "none"), None
    return {"horizon": horizon, "multiplier": multiplier, "offset": offset,
            "terminal_source": terminal, "kind": kind, "initial": initial,
            "authentic_compatible": offset == terminal}


def affine_repeat_defect(horizon: int, multiplier: Q | int,
                         offset: Q | int = 0, step: int = 1) -> Q:
    """Forcing defect for repeating X_(N+n)=multiplier*X_n+offset.

    If the previous seam holds, this is its exact failure at the next step.
    A single vanishing defect does not certify repetition at later steps.
    """
    _natural(horizon, 1)
    _natural(step, 1)
    multiplier, offset = _exact(multiplier), _exact(offset)
    return forcing(horizon + step) - multiplier * forcing(step) + 15 * offset


def source_commuting_affine(index: int, slope: Q | int,
                            initial_offset: Q | int = 0) -> tuple[Q, Q]:
    """Coefficients of every affine H_n commuting with the forced recurrence.

    H_n(x)=a*x+(1-a)*U_n+16^n*b0.  A map preserving the initial origin
    has b0=0 and therefore fixes every authentic U_n pointwise.
    This classifies affine commuting maps, not arbitrary nonlinear/time-mixing
    transforms.  Zero slope is allowed as a map, not an invertible conjugacy.
    """
    _natural(index)
    slope, initial_offset = _exact(slope), _exact(initial_offset)
    source = exact_forced_history(index)[-1]
    return slope, (1 - slope) * source + 16**index * initial_offset


def twisted_boundary_certificate(horizon: int, index: int,
                                  terms: int = 8) -> dict:
    """Exact twisted state and rational bounds on its two limiting regimes.

    c_N=-U_N/(16^N+1).  Put alpha=T_0 and T_n=sum 16^-j*r(n+j).
    Then X_n+T_n=16^n*(alpha+T_N)/(16^N+1)>0.
    The bounds are strict enclosures, not evaluated irrational tails.
    At fixed n this error vanishes; at n=N-j, X_n tends to alpha*16^-j.
    """
    _natural(horizon, 1)
    _natural(index)
    _natural(terms, 1)
    if index > horizon:
        raise ValueError("index must lie in the finite seam interval")
    seam = solve_affine_seam(horizon, -1)
    state = exact_forced_history(index, seam["initial"])[-1]
    alpha_lo, alpha_hi = tail_interval(0, terms)
    tail_lo, tail_hi = tail_interval(index, terms)
    end_lo, end_hi = tail_interval(horizon, terms)
    factor = Q(16**index, 16**horizon + 1)
    shadow_error = (factor * (alpha_lo + end_lo),
                    factor * (alpha_hi + end_hi))
    profile_factor = Q(16**index, 16**horizon)
    profile_error = (state - profile_factor * alpha_hi,
                     state - profile_factor * alpha_lo)
    profile_budget = tail_hi + profile_factor * (end_hi + alpha_hi / 16**horizon)
    return {**seam, "source": "changed-initial-twisted-seam", "index": index,
            "state": state, "authentic_source": False,
            "alpha_interval": (alpha_lo, alpha_hi),
            "tail_interval": (tail_lo, tail_hi),
            "bounded_shadow_error_interval": shadow_error,
            "initial_limit_error_interval": (
                (alpha_lo + end_lo) / (16**horizon + 1),
                (alpha_hi + end_hi) / (16**horizon + 1)),
            "terminal_profile_error_interval": profile_error,
            "terminal_profile_error_budget": profile_budget,
            "first_twisted_repeat_defect": affine_repeat_defect(horizon, -1)}


def generating_identity_certificate(horizon: int, initial: Q | int,
                                    argument: Q | int) -> dict:
    """Finite polynomial identity, including its indispensable endpoint term.

    (1-16z)*sum_(n=0)^N X_n*z^n
      = c + sum_(n=1)^N r(n)*z^n - 16*X_N*z^(N+1).
    Unlike the infinite generating series, this polynomial identity holds
    at every rational argument, including z=1/16.
    """
    _natural(horizon)
    initial, argument = _exact(initial), _exact(argument)
    history = exact_forced_history(horizon, initial)
    left = (1 - 16 * argument) * sum(
        (state * argument**n for n, state in enumerate(history)), Q())
    numerator = initial + sum(
        (forcing(n) * argument**n for n in range(1, horizon + 1)), Q())
    boundary = 16 * history[-1] * argument**(horizon + 1)
    return {"left": left, "numerator": numerator,
            "endpoint_term": boundary, "right": numerator - boundary,
            "residual": left - numerator + boundary}


def generating_pole_residue_interval(initial: Q | int,
                                     terms: int = 8) -> tuple[Q, Q]:
    """Strict enclosure of residue -(c+alpha)/16 at z=1/16.

    The infinite source generating function is analytic at z=1/16.  Its
    quotient by 1-16z has a removable singularity only for c=-alpha.
    No circle-distribution conclusion is implied by this pole.
    """
    initial = _exact(initial)
    _natural(terms, 1)
    lo, hi = tail_interval(0, terms)
    return -(initial + hi) / 16, -(initial + lo) / 16


def reciprocal_reversal_certificate(value: Q | int) -> dict:
    """Check JFJ=F^-1 on the nonzero rational chart, F(y)=16y, J(y)=1/y.

    Also report whether F respects this particular reciprocal pair.  The
    global quotient y~1/y fails, even though the reversal identity holds.
    """
    value = _exact(value)
    if value == 0:
        raise ValueError("zero belongs to the other projective chart")
    image = 16 * value
    paired_image = 16 / value
    return {"value": value, "JFJ": 1 / (16 / value), "inverse_F": value / 16,
            "F_value": image, "F_reciprocal": paired_image,
            "quotient_pair_preserved": paired_image in (image, 1 / image)}
