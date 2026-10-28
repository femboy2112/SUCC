"""Integer-branch coercivity improves the selected BBP logarithmic constant.

This module provides exact finite certificates for the paper theorem in
research/2026-10-26/OILY_DIRECT_ARITHMETIC.md. The new block loss is 1/29,
not a relative loss and not a normality theorem. Its eventual all-N threshold
exists by the published irrationality bound but is not numerically certified.
The authentic arithmetic engine is imported unchanged from the native source.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .bbp_diophantine_coherence import (
    ceil_log, circle_distance, floor_log,
)
from .succ_internal_matrix_walk import authentic_r, original_state


BLOCK_LOSS = Q(1, 29)
LIFT_RADIUS = Q(1, 15)
COSINE_COERCIVITY = Q(19)
BRANCH_NORM_SQUARED = 546
UNIFORM_FORCING_SPAN = Q(15, 4096)
IRRATIONALITY_SOURCE = "https://arxiv.org/abs/1912.06345v2"


def _integer(value, minimum=1, maximum=None):
    if type(value) is not int or value < minimum:
        raise ValueError("ordinary integer outside declared domain")
    if maximum is not None and value > maximum:
        raise ValueError("finite certificate budget exceeded")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


def _frequency(value):
    if type(value) is not int or value == 0:
        raise ValueError("nonzero integer frequency required")
    return value


def transition_difference_coefficients(observations, left, right):
    """Coefficients of (q[l+1]-16q[l])-(q[r+1]-16q[r]).

    Adjacent distinct transitions have squared norm 546; separated ones 514.
    This is the exact finite linear algebra behind integer-branch coercivity.
    """
    _integer(observations, 3, 2001)
    _integer(left, 0, observations-2)
    _integer(right, 0, observations-2)
    if left == right:
        raise ValueError("distinct transitions required")
    coefficients = [0]*observations
    coefficients[left+1] += 1
    coefficients[left] -= 16
    coefficients[right+1] -= 1
    coefficients[right] += 16
    return tuple(coefficients)


def coercivity_floor(forcing_span):
    """Conditional minimum deficit if two integer branches differ.

    Valid in the small-deficit regime L<=1/29, which provides |q|<1/15
    and hence the coefficient 19. The result is not a global cosine bound.
    """
    span = _rational(forcing_span)
    if not 0 <= span < 1:
        raise ValueError("forcing span must be in [0,1)")
    return COSINE_COERCIVITY*(1-span)**2/BRANCH_NORM_SQUARED


def exact_margins():
    """Positive rational margins used by the analytic proof, no pi oracle."""
    cosine = 2*Q(25, 8)**2-Q(2, 3)*Q(22, 7)**4/225
    return {
        "lift_radius_squared_margin": LIFT_RADIUS**2-BLOCK_LOSS/8,
        "cosine_margin": cosine-COSINE_COERCIVITY,
        "branch_margin": coercivity_floor(UNIFORM_FORCING_SPAN)-BLOCK_LOSS,
        "adjacent_norm_squared": 16**2+17**2+1,
        "separated_norm_squared": 2*(16**2+1),
    }


@dataclass(frozen=True)
class CoerciveInverseCertificate:
    initial: Q
    forcing: tuple[Q, ...]
    frequency: int
    forcing_span: Q
    weighted_source: Q
    arc_radius: Q
    distance_to_centers: Q

    @property
    def observations(self):
        return len(self.forcing)+1

    @property
    def outside_arcs(self):
        return self.distance_to_centers > self.arc_radius

    @property
    def absolute_loss_threshold(self):
        return BLOCK_LOSS

    @property
    def distinct_branch_deficit_floor(self):
        return coercivity_floor(self.forcing_span)


def coercive_inverse_certificate(initial, forcing, frequency=1):
    """Exact necessary arc for L<=1/29; outside the arc certifies L>1/29.

    Rational inputs supply finite certificates, not evaluations of complex
    sums. Arc membership is NOT sufficient for coherence. This generic
    certificate does not authenticate either the forcing or the initial state.
    """
    initial = _rational(initial)
    forcing = tuple(_rational(value) for value in forcing)
    _integer(len(forcing), 2, 2000)
    frequency = _frequency(frequency)
    h = abs(frequency)
    span = h*(max(forcing)-min(forcing))
    if span >= 1 or coercivity_floor(span) <= BLOCK_LOSS:
        raise ValueError("integer-branch coercivity margin is not certified")
    weighted = sum((r/Q(16**j) for j, r in enumerate(forcing, 1)), Q())
    radius = (32*LIFT_RADIUS+h*abs(forcing[-1]))/(15*h*16**len(forcing))
    distance = circle_distance(15*h*(initial+weighted))/(15*h)
    return CoerciveInverseCertificate(initial, forcing, frequency, span,
                                      weighted, radius, distance)


@dataclass(frozen=True)
class CoerciveBBPBlock:
    m: int
    source_initial: Q
    terminal_state: Q
    inverse: CoerciveInverseCertificate

    @property
    def authentic_zero_anchor(self):
        return self.source_initial == 0

    @property
    def backward_identity_defect(self):
        return (self.inverse.initial+self.inverse.weighted_source
                -self.terminal_state/Q(16**(7*self.m-1)))


def _bbp_block(m, frequency, source_initial):
    _integer(m, 8, 128)
    frequency = _frequency(frequency)
    source_initial = _rational(source_initial)
    if 64*abs(frequency) > m*m:
        raise ValueError("uniform band requires 64*abs(h) <= m squared")
    start = original_state(m+1)+16**(m+1)*source_initial
    end = original_state(8*m)+16**(8*m)*source_initial
    forcing = tuple(authentic_r(n) for n in range(m+2, 8*m+1))
    inverse = coercive_inverse_certificate(start, forcing, frequency)
    result = CoerciveBBPBlock(m, source_initial, end, inverse)
    if result.backward_identity_defect:
        raise ArithmeticError("literal BBP backward identity failed")
    return result


def authentic_block_certificate(m, frequency=1):
    return _bbp_block(m, frequency, Q())


def terminal_zero_control(m, frequency=1):
    """Same forcing, rational changed initial, terminal state zero; one per m."""
    _integer(m, 8, 128)
    initial = -original_state(8*m)/Q(16**(8*m))
    return _bbp_block(m, frequency, initial)


def approximation_coefficient_bound(m, frequency=1):
    """B<3 in the inverse consequence |pi-p/q|<B*16^(-8m)."""
    _integer(m)
    h = abs(_frequency(frequency))
    return 16*(32*LIFT_RADIUS/(15*h)
               +Q(1, 64*(8*m-1)**2)+Q(1, 64*(8*m)**2))


def diophantine_scale_comparison(m, frequency, constant):
    """Compare 3*16^(-8m) with C*(15*abs(h)*16^m)^(-15/2).

    This does not certify that the supplied C is valid for pi.
    """
    _integer(m, 1, 100000)
    h = abs(_frequency(frequency))
    constant = _rational(constant)
    if not 0 < constant <= 1:
        raise ValueError("supplied constant must belong to (0,1]")
    return constant**2*16**m > 9*(15*h)**15


def usable_block_count(observations, maximum_frequency, threshold_exponent):
    """Exact count; numerical J0 remains a separately unverified input."""
    _integer(observations)
    _integer(maximum_frequency)
    _integer(threshold_exponent, 0)
    first = max(threshold_exponent, 1+ceil_log(maximum_frequency, 64))
    return max(0, floor_log(observations, 8)-first)


def conditional_budget(observations, maximum_frequency, threshold_exponent):
    count = usable_block_count(observations, maximum_frequency, threshold_exponent)
    return {
        "observations": observations,
        "maximum_frequency": maximum_frequency,
        "threshold_exponent": threshold_exponent,
        "usable_blocks": count,
        "fourier_modulus_upper": Q(observations)-BLOCK_LOSS*count,
        "threshold_numerically_certified": False,
        "authority": "conditional on a supplied valid threshold; no pi constant computed",
    }
