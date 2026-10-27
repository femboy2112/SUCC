"""Exact instruments for the whole-block integer-branch coercivity theorem.

The paper improves the eventual logarithmic ABSOLUTE BBP Fourier loss from
1/29 to 1/14 per eligible geometric block. Neither the Diophantine constant
nor the numerical onset is computed. No function below proves normality,
evaluates a floating Fourier sum, or authenticates a supplied generic seed.

The earlier two-transition theorem is credited to PR #311, source commit
a34c4484059e667202b97d5ab4102560987b1406. This module does not import it.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .bbp_diophantine_coherence import circle_distance, ceil_log, floor_log
from .succ_internal_matrix_walk import authentic_r


BLOCK_LOSS = Q(1, 14)
QUIET_SQRT_UPPER = Q(1, 100)
MIN_TRANSITIONS = 20000
MIN_SOURCE_SCALE = 4096
PRIOR_SOURCE_COMMIT = "a34c4484059e667202b97d5ab4102560987b1406"
IRRATIONALITY_SOURCE = "https://arxiv.org/abs/1912.06345v2"


def _integer(value, minimum=1, maximum=None):
    if type(value) is not int or value < minimum:
        raise ValueError("ordinary integer outside the declared domain")
    if maximum is not None and value > maximum:
        raise ValueError("finite certificate budget exceeded")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("an exact integer or Fraction is required")
    return Q(value)


def _frequency(value):
    if type(value) is not int or value == 0:
        raise ValueError("a nonzero integer Fourier frequency is required")
    return value


def machin_pi_interval():
    """Strict rational pi bounds from the classical Machin identity.

    Alternating arctan bounds prove this interval; the identity itself is
    classical mathematical input, not inferred from a numerical pi value.
    """
    lower = 16*(Q(1, 5)-Q(1, 375))-Q(4, 239)
    upper = (16*(Q(1, 5)-Q(1, 375)+Q(1, 15625))
             -4*(Q(1, 239)-Q(1, 3*239**3)))
    return lower, upper


def local_cosine_coefficient():
    """Taylor coefficient valid for q squared <= 1/112, not globally."""
    return 2*Q(157, 50)**2-Q(2, 3)*Q(22, 7)**4*Q(1, 112)


@dataclass(frozen=True)
class WholeBlockParameters:
    transitions: int
    forcing_span: Q
    quiet_sqrt_upper: Q
    nonconstant_loss_lower: Q

    @property
    def constant_branch_if_loss_at_most(self):
        return BLOCK_LOSS


def whole_block_parameters(transitions, forcing_span,
                           quiet_sqrt_upper=QUIET_SQRT_UPPER):
    """Certify the rational hypotheses of the finite constant-branch lemma.

    The span is abs(h)*(max forcing-min forcing). The rational u must satisfy
    u squared >= 2/T. The lemma is conditional on a Fourier loss <= 1/14.
    """
    _integer(transitions, 2)
    span = _rational(forcing_span)
    upper = _rational(quiet_sqrt_upper)
    if not 0 <= span < 1 or upper < 0:
        raise ValueError("invalid forcing span or square-root upper bound")
    if upper**2*transitions < 2:
        raise ValueError("the quiet-transition square-root bound is false")
    lower = 19*(1-span)**2/(257*(1+upper)**2)
    if lower <= BLOCK_LOSS:
        raise ValueError("constant-branch loss margin is not certified")
    return WholeBlockParameters(transitions, span, upper, lower)


def authentic_forcing_parameters(m, frequency=1):
    """Exact original four-pole range on (m,8m], in the proved frequency band.

    This verifies the forcing conditions, not any supplied initial state.
    The infinite selected theorem additionally requires exactly U_0=0.
    It does not expand the huge rational state at time 8m.
    """
    _integer(m, MIN_SOURCE_SCALE)
    h = abs(_frequency(frequency))
    if 64*h > m*m:
        raise ValueError("the source band requires 64*abs(h) <= m squared")
    span = h*(authentic_r(m+2)-authentic_r(8*m))
    if not 0 < span < Q(15, 4096):
        raise ArithmeticError("the original source range bound failed")
    return whole_block_parameters(7*m-1, span)


@dataclass(frozen=True)
class QuietTransitionWitness:
    energy: Q
    quiet_index: int
    other_branch_index: int | None
    transition_values: tuple[Q, ...]
    branch_residuals: tuple[Q, ...]
    forcing_span: Q


def quiet_transition_witness(centered_offsets, forcing, frequency=1):
    """Inspect exact lifted branch data without assigning a source passport.

    Integer differences of residuals are checked explicitly. The returned
    witness is a finite algebraic certificate; it is not a trigonometric
    evaluation of the resultant or a proof that this center is its direction.
    """
    offsets = tuple(_rational(x) for x in centered_offsets)
    forcing = tuple(_rational(x) for x in forcing)
    _integer(len(forcing), 2, 100000)
    if len(offsets) != len(forcing)+1 or any(abs(x) > Q(1, 2) for x in offsets):
        raise ValueError("centered offsets and forcing have incompatible domains")
    frequency = _frequency(frequency)
    values = tuple(offsets[t+1]-16*offsets[t] for t in range(len(forcing)))
    residuals = tuple(a-frequency*r for a, r in zip(values, forcing))
    if any((d-residuals[0]).denominator != 1 for d in residuals):
        raise ValueError("the lifted integer-branch compatibility is false")
    quiet = min(range(len(forcing)), key=lambda t: offsets[t]**2+offsets[t+1]**2)
    other = next((t for t, d in enumerate(residuals)
                  if d != residuals[quiet]), None)
    energy = sum((q*q for q in offsets), Q())
    return QuietTransitionWitness(energy, quiet, other, values, residuals,
                                  abs(frequency)*(max(forcing)-min(forcing)))


@dataclass(frozen=True)
class WholeBlockInverseCertificate:
    initial: Q
    forcing: tuple[Q, ...]
    frequency: int
    parameters: WholeBlockParameters
    weighted_source: Q
    arc_radius: Q
    distance_to_centers: Q

    @property
    def outside_arcs(self):
        """If true, the generic finite loss is strictly greater than 1/14."""
        return self.distance_to_centers > self.arc_radius


def inverse_seed_certificate(initial, forcing, frequency=1,
                             quiet_sqrt_upper=QUIET_SQRT_UPPER):
    """Exact inverse arc; being inside it does not imply coherence."""
    initial = _rational(initial)
    forcing = tuple(_rational(x) for x in forcing)
    _integer(len(forcing), 2, 100000)
    frequency = _frequency(frequency)
    h = abs(frequency)
    parameters = whole_block_parameters(
        len(forcing), h*(max(forcing)-min(forcing)), quiet_sqrt_upper)
    source = Q()
    # Backward Horner evaluation preserves the literal source ordering.
    for r in reversed(forcing):
        source = (source+r)/16
    radius = (Q(16, 5)+h*abs(forcing[-1]))/(15*h*16**len(forcing))
    distance = circle_distance(15*h*(initial+source))/(15*h)
    return WholeBlockInverseCertificate(initial, forcing, frequency,
                                         parameters, source, radius, distance)


def approximation_coefficient_bound(m, frequency=1):
    """Certified B<4 for abs(pi-p/q)<B*16^(-8m), conditional on coherence."""
    _integer(m)
    h = abs(_frequency(frequency))
    return 16*(Q(16, 75*h)+Q(1, 64*(8*m-1)**2)+Q(1, 64*(8*m)**2))


def diophantine_scale_comparison(m, frequency, constant):
    """Exact C²16^m>16(15|h|)^15; validity of C for pi is NOT certified."""
    _integer(m, 1, 100000)
    h = abs(_frequency(frequency))
    constant = _rational(constant)
    if not 0 < constant <= 1:
        raise ValueError("the supplied comparison constant must lie in (0,1]")
    return constant**2*16**m > 16*(15*h)**15


def uniform_threshold_comparison(m0, constant):
    """Conditional sufficient comparison for every m>=m0 and |h|<=m²/64."""
    _integer(m0, MIN_SOURCE_SCALE, 100000)
    return diophantine_scale_comparison(m0, m0*m0, constant)


@dataclass(frozen=True)
class ConditionalLogarithmicBudget:
    observations: int
    maximum_frequency: int
    threshold_exponent: int
    eligible_blocks: int

    @property
    def modulus_upper(self):
        return self.observations-BLOCK_LOSS*self.eligible_blocks

    @property
    def numerical_onset_certified(self):
        return False


def conditional_logarithmic_budget(observations, maximum_frequency, threshold_exponent):
    """Combinatorial budget only; a supplied J is not a proved pi onset."""
    _integer(observations)
    _integer(maximum_frequency)
    _integer(threshold_exponent, 4)
    first = max(threshold_exponent, 1+ceil_log(maximum_frequency, 64))
    count = max(0, floor_log(observations, 8)-first)
    return ConditionalLogarithmicBudget(observations, maximum_frequency,
                                        threshold_exponent, count)


def boundary_excursion_squared_modulus(transitions, cosine):
    """Formal |T+e(1/16)|²=T²+2T*cos(pi/8)+1 with supplied exact cosine.

    A rational cosine argument is a symbolic evaluation, not a claim that
    cos(pi/8) is rational. It supports exact interval bounds in the tests.
    """
    _integer(transitions, 2)
    cosine = _rational(cosine)
    if not -1 <= cosine <= 1:
        raise ValueError("cosine argument lies outside [-1,1]")
    return transitions**2+2*transitions*cosine+1
