"""Exact finite instruments for BBP extreme-coherence exclusion.

The companion paper derives an unconditional *logarithmic absolute* loss
from maximal Fourier reinforcement, using the authentic zero anchor and
the classical bound mu(pi) < 15/2. It does not prove Weyl cancellation.
The existence of a uniform threshold is proved; its numerical value is
not computed. ``conditional_budget`` deliberately records that distinction.

The inverse arc theorem is inherited from PR #297, source commit
eca4462ee4d62642b15c4af672136aa5bcacd00b. This is an independent small
implementation; it imports no code from that unmerged branch.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt

from .succ_internal_matrix_walk import authentic_r, original_state


ARC_PARAMETER = Q(1, 100)
BLOCK_LOSS = Q(1, 1250)
INVERSE_SOURCE_COMMIT = "eca4462ee4d62642b15c4af672136aa5bcacd00b"
IRRATIONALITY_SOURCE = "https://arxiv.org/abs/1912.06345v2"


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("an exact integer or Fraction is required")
    return Q(value)


def _integer(value, minimum=1, maximum=None):
    if type(value) is not int or value < minimum:
        raise ValueError("ordinary integer outside the declared domain")
    if maximum is not None and value > maximum:
        raise ValueError("finite certificate budget exceeded")
    return value


def _frequency(value):
    if type(value) is not int or value == 0:
        raise ValueError("a nonzero integer Fourier frequency is required")
    return value


def circle_distance(value):
    """Exact distance to Z, distinct from complex/cyclotomic evaluation."""
    value = _rational(value) % 1
    return min(value, 1-value)


@dataclass(frozen=True)
class InverseSeedCertificate:
    """Rational arc-membership test; membership does NOT imply coherence.

    With the verified branch condition, ``outside_arcs`` certifies
    D - abs(sum exp(2*pi*i*h*X_t)) > ``absolute_loss_threshold``.
    This analytic implication is paper-proved, not computed trigonometrically.
    No generic certificate is labelled an authenticated BBP source.
    """
    initial: Q
    forcing: tuple[Q, ...]
    frequency: int
    arc_parameter: Q
    branch_span: Q
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
        return 8*self.arc_parameter**2

    @property
    def normalized_loss_threshold(self):
        return self.absolute_loss_threshold/self.observations


def inverse_seed_certificate(initial, forcing, frequency=1,
                             arc_parameter=ARC_PARAMETER):
    """Check the finite inverse theorem entirely in rational arithmetic.

    ``forcing[j-1]`` is the forcing of transition j, beginning at j=1.
    There must be at least one transition. The initial input is the start
    of this finite block, not necessarily the source's time-zero state.
    """
    initial = _rational(initial)
    forcing = tuple(_rational(x) for x in forcing)
    _integer(len(forcing), 1, 2000)
    frequency = _frequency(frequency)
    a = _rational(arc_parameter)
    if a <= 0:
        raise ValueError("positive arc parameter required")
    h = abs(frequency)
    span = 34*a+h*(max(forcing)-min(forcing))
    if span >= 1:
        raise ValueError("constant integer branch condition is not certified")
    source = sum((r/Q(16**j) for j, r in enumerate(forcing, 1)), Q())
    radius = (32*a+h*abs(forcing[-1]))/(15*h*16**len(forcing))
    distance = circle_distance(15*h*(initial+source))/(15*h)
    return InverseSeedCertificate(initial, forcing, frequency, a, span,
                                  source, radius, distance)


@dataclass(frozen=True)
class BBPBlockCertificate:
    m: int
    source_initial: Q
    terminal_state: Q
    inverse: InverseSeedCertificate

    @property
    def authentic_zero_anchor(self):
        return self.source_initial == 0

    @property
    def backward_identity_defect(self):
        return (self.inverse.initial+self.inverse.weighted_source
                -self.terminal_state/Q(16**(7*self.m-1)))


def _bbp_block(m, frequency, source_initial):
    _integer(m, 1, 128)
    _frequency(frequency)
    source_initial = _rational(source_initial)
    if abs(frequency) > m*m:
        raise ValueError("the uniform source band requires abs(h) <= m squared")
    start = original_state(m+1)+16**(m+1)*source_initial
    terminal = original_state(8*m)+16**(8*m)*source_initial
    forcing = tuple(authentic_r(n) for n in range(m+2, 8*m+1))
    inverse = inverse_seed_certificate(start, forcing, frequency)
    result = BBPBlockCertificate(m, source_initial, terminal, inverse)
    if result.backward_identity_defect:
        raise ArithmeticError("full lifted BBP backward identity failed")
    return result


def authentic_block_certificate(m, frequency=1):
    """Finite (m,8m] arc rejection with literal forcing and source U_0=0."""
    return _bbp_block(m, frequency, Q())


def terminal_zero_control(m, frequency=1):
    """Same four-pole forcing, changed rational initial, exact endpoint zero.

    One control is chosen separately for each m. It is rejected by the
    original source passport solely at initialization. It is not a claim
    that one fixed rational initial state stays coherent for all m.
    """
    _integer(m, 1, 128)
    initial = -original_state(8*m)/Q(16**(8*m))
    return _bbp_block(m, frequency, initial)


def terminal_control_loss_upper(m, frequency=1):
    """Strict upper bound on the terminal-zero control's absolute block loss.

    From abs(X_n)<1/[64(m+1)^2] and 1-cos(2*pi*x)<=968*x²/49.
    It certifies near coherence for fixed h and large m; it does not
    authenticate the changed initial state.
    """
    _integer(m)
    h = abs(_frequency(frequency))
    return Q(121*m*h*h, 3584*(m+1)**4)


def approximation_coefficient_bound(m, frequency=1):
    """Coefficient B<1 in the inverse consequence abs(pi-p/q)<B*16^(-8m).

    Uses r(8m)/15 < 1/[64(8m-1)^2] and T_(8m)<1/[64(8m)^2].
    This checks the rational bound; it does not approximate pi.
    """
    _integer(m)
    h = abs(_frequency(frequency))
    return 16*(32*ARC_PARAMETER/(15*h)
               +Q(1, 64*(8*m-1)**2)+Q(1, 64*(8*m)**2))


def diophantine_scale_comparison(m, frequency, constant):
    """Exact comparison 16^(-8m)<C*(15*abs(h)*16^m)^(-15/2).

    C is only a supplied rational number. This function does NOT certify
    that it is a valid global irrationality lower-bound constant for pi.
    Squaring removes the half-integer exponent without rounding.
    """
    _integer(m, 1, 100000)
    h = abs(_frequency(frequency))
    constant = _rational(constant)
    if not 0 < constant <= 1:
        raise ValueError("the supplied comparison constant must lie in (0,1]")
    return constant**2*16**m > (15*h)**15


def uniform_threshold_comparison(m0, constant):
    """Arithmetic sufficiency at m0, hence every m>=m0 and 1<=abs(h)<=m².

    The monotonicity for m>=64 is proved in the paper. Validity of the
    supplied irrationality constant is deliberately a separate obligation.
    """
    _integer(m0, 64, 100000)
    return diophantine_scale_comparison(m0, m0*m0, constant)


def floor_log(value, base):
    _integer(value)
    _integer(base, 2)
    result = 0
    while value >= base:
        value //= base
        result += 1
    return result


def ceil_log(value, base):
    _integer(value)
    _integer(base, 2)
    result = floor_log(value, base)
    return result+(base**result < value)


def usable_block_count(observations, maximum_frequency, threshold_exponent):
    """Count complete blocks (8^j,8^(j+1)] with j>=J0 and 64^j>=h.

    J0 must be justified by the analytic theorem, not fitted to this count.
    This is an integer combinatorial identity for any supplied J0>=0.
    """
    _integer(observations)
    _integer(maximum_frequency)
    _integer(threshold_exponent, 0)
    first = max(threshold_exponent, ceil_log(maximum_frequency, 64))
    return max(0, floor_log(observations, 8)-first)


def prescribed_width(observations):
    _integer(observations)
    return 1+isqrt(observations)


@dataclass(frozen=True)
class ConditionalCoherenceBudget:
    observations: int
    width: int
    threshold_exponent: int
    usable_blocks: int
    fourier_modulus_upper: Q
    normalized_purity_upper: Q
    threshold_numerically_certified: bool = False
    authority: str = "conditional on the supplied uniform threshold; no pi constant computed"


def conditional_budget(observations, width, threshold_exponent):
    """Evaluate the theorem's all-N formula, keeping its threshold conditional.

    The paper proves that SOME fixed threshold exists. A caller-provided
    numerical threshold is not certified by this function or by finite tests.
    ``normalized_purity_upper`` bounds D_(N,H)/H, not D_(N,H).
    """
    _integer(observations)
    _integer(width, 2)
    count = usable_block_count(observations, width-1, threshold_exponent)
    upper = Q(observations)-BLOCK_LOSS*count
    purity = (width-1)*(upper/observations)**2
    return ConditionalCoherenceBudget(observations, width, threshold_exponent,
                                      count, upper, purity)
