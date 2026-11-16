"""Exact parameters and population frame bounds for authentic BBP echoes.

The source is U_0=0, U_(n+1)=16*U_n+r(n+1), with all four original poles.
The integer taps (h-16*K,K) give h*U_n+K*r(n+1): h stays fixed.  Source
nodes r(n+1), n=B..2B-1, are separated at scale B^-3.  Gamma-Poisson and
finite triangular clock laws yield quantitatively invertible population
frames at frequency spread of order B^3.

These are rational bounds, not exact trigonometric matrices or an empirical
random-frame certificate.  Stable reconstruction does not prove signed
cancellation.  In fact resolved raw output energy is about 1/B for EVERY
unit-modulus carrier, including a locked one.  Complex orientation and clock
labels must be retained.  Proofs and scope: the pi_carrier_collision dossier.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction as Q

from .bbp_binwindow_conjugacy import authentic_state, source_verified


MAX_SHELL = 100_000
MAX_ECHO_CLOCK = 512
MAX_PROBABILITY_INDEX = 4096


def _integer(value, name: str, minimum=None, maximum=None) -> int:
    if type(value) is not int:
        raise ValueError(f"{name} must be an exact integer, not bool or float")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} is below its declared domain")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name} exceeds its declared computation budget")
    return value


def _nonnegative(value, name: str, positive=False) -> Q:
    if type(value) not in (int, Q):
        raise ValueError(f"{name} must be an exact int/Fraction")
    result = Q(value)
    if result < 0 or (positive and result == 0):
        raise ValueError(f"{name} must be {'positive' if positive else 'nonnegative'}")
    return result


def _ceil(value: Q) -> int:
    return -(-value.numerator // value.denominator)


def matched_echo_coefficients(h: int, intensity: int) -> tuple[int, int]:
    """P(16)=h exactly.  h=0 is allowed as the explicit seed-erasure control."""
    h = _integer(h, "Target frequency")
    intensity = _integer(intensity, "Integer intensity")
    return h - 16 * intensity, intensity


@dataclass(frozen=True)
class EchoRecord:
    clock: int
    target_frequency: int
    intensity: int
    state: Q = field(init=False)
    next_state: Q = field(init=False)
    source_node: Q = field(init=False)
    coefficients: tuple[int, int] = field(init=False)
    phase_turns: Q = field(init=False)

    def __post_init__(self):
        n = _integer(self.clock, "Source clock", 0, MAX_ECHO_CLOCK)
        coefficients = matched_echo_coefficients(self.target_frequency, self.intensity)
        state = authentic_state(n)
        source = source_verified(n + 1)
        following = 16 * state + source
        phase = coefficients[0] * state + coefficients[1] * following
        if phase != self.target_frequency * state + self.intensity * source:
            raise ArithmeticError("Carrier-matched source identity failed")
        for name, value in (("state", state), ("next_state", following),
                            ("source_node", source), ("coefficients", coefficients),
                            ("phase_turns", phase)):
            object.__setattr__(self, name, value)

    @property
    def phase_mod_one(self) -> Q:
        """Reduce exactly before any optional numerical complex exponential."""
        return self.phase_turns % 1

    @property
    def retains_nonzero_carrier(self) -> bool:
        return self.target_frequency != 0


def matched_echo_record(clock: int, h: int, intensity: int) -> EchoRecord:
    return EchoRecord(clock, h, intensity)


@dataclass(frozen=True)
class SourceSpacing:
    """Authenticated nodes g_n=r(n+1) on n=B,...,2B-1, B>=2."""

    shell_start: int
    minimum_gap: Q = field(init=False)
    gap_lower: Q = field(init=False)
    gap_upper: Q = field(init=False)
    span: Q = field(init=False)
    span_upper: Q = field(init=False)

    def __post_init__(self):
        b = _integer(self.shell_start, "Shell start", 2, MAX_SHELL)
        last = source_verified(2 * b)
        gap = source_verified(2 * b - 1) - last
        lower = Q(240, (16 * b - 4) * (16 * b - 3) * (16 * b - 2))
        upper = Q(240, (16 * b - 15) * (16 * b - 14) * (16 * b - 13))
        span = source_verified(b + 1) - last
        span_upper = Q(15, (8 * b + 1) * (8 * b + 2))
        if not 0 < lower <= gap <= upper or not 0 < span < span_upper < Q(1, 2):
            raise ArithmeticError("Authentic source spacing certificate failed")
        for name, value in (("minimum_gap", gap), ("gap_lower", lower),
                            ("gap_upper", upper), ("span", span),
                            ("span_upper", span_upper)):
            object.__setattr__(self, name, value)


def source_spacing_certificate(shell_start: int) -> SourceSpacing:
    return SourceSpacing(shell_start)


def recommended_gamma_scale(shell_start: int) -> int:
    """ceil(1/d_B), certifying Gamma Gram deviation eta<=1/4."""
    return _ceil(1 / SourceSpacing(shell_start).gap_lower)


def recommended_fejer_width(shell_start: int) -> int:
    """ceil(2/d_B), for K=1+U+V with U,V uniform on 0..M-1."""
    return _ceil(2 / SourceSpacing(shell_start).gap_lower)


@dataclass(frozen=True)
class PopulationFrameCertificate:
    """Bounds for G_nm=E[e(K*(g_m-g_n))], retaining complex orientation.

    For F(K)=B^-1 sum c_n e(K*g_n), E|F|^2=c*G*c/B^2.
    The eigenvalue interval applies to all complex c.  The phase-energy
    interval applies only when every |c_n|=1.  A frequency offset conjugates
    G by a diagonal unitary and does not improve its condition number.
    """

    shell_start: int
    law: str
    scale: Q | int
    offset: int = 0
    source: SourceSpacing = field(init=False)
    deviation_upper: Q = field(init=False)
    frequency_mean: Q = field(init=False)
    frequency_variance: Q = field(init=False)

    def __post_init__(self):
        source = SourceSpacing(self.shell_start)
        offset = _integer(self.offset, "Nonnegative clock offset", 0)
        if self.law == "gamma_poisson":
            scale = _nonnegative(self.scale, "Gamma scale", positive=True)
            eta = 1 / (4 * scale * (1 + scale) * source.gap_lower ** 2)
            mean, variance = offset + 2 * scale, 2 * scale * (1 + scale)
        elif self.law == "finite_fejer":
            scale = _integer(self.scale, "Uniform clock width", 1)
            eta = 1 / (Q(scale) ** 2 * source.gap_lower ** 2)
            mean, variance = Q(offset + scale), Q(scale * scale - 1, 6)
        else:
            raise ValueError("Declare gamma_poisson or finite_fejer clock law")
        for name, value in (("source", source), ("scale", scale),
                            ("deviation_upper", eta), ("frequency_mean", mean),
                            ("frequency_variance", variance)):
            object.__setattr__(self, name, value)

    @property
    def stable(self) -> bool:
        return self.deviation_upper < 1

    @property
    def eigenvalue_interval(self) -> tuple[Q, Q]:
        return max(Q(0), 1 - self.deviation_upper), 1 + self.deviation_upper

    def _positive_lower(self) -> Q:
        if not self.stable:
            raise ValueError("This population bound does not certify stable reconstruction")
        return 1 - self.deviation_upper

    @property
    def condition_number_squared_upper(self) -> Q:
        """Squared condition number of the weighted analysis frame, not its Gram."""
        return (1 + self.deviation_upper) / self._positive_lower()

    @property
    def coefficient_recovery_squared_gain(self) -> Q:
        """||c_hat-c||_2^2 <= gain*E|readout_error(K)|^2 for the canonical inverse."""
        return Q(self.shell_start ** 2) / self._positive_lower()

    @property
    def mean_recovery_squared_gain(self) -> Q:
        """|mean(c_hat-c)|^2 <= gain*E|readout_error(K)|^2."""
        return Q(self.shell_start) / self._positive_lower()

    @property
    def unit_phase_energy_interval(self) -> tuple[Q, Q]:
        lower, upper = self.eigenvalue_interval
        return lower / self.shell_start, upper / self.shell_start

    @property
    def oriented_escape_multipliers(self) -> tuple[Q, Q]:
        """A_B lies between these multiples of E|F_c-F_ones|^2.

        A_B=mean(1-Re c_n), |c_n|=1.  Requires the oriented complex residual,
        not a difference of phase-blind energies.  This comparison transports
        an escape estimate; it does not provide one for the actual source.
        """
        return (Q(self.shell_start, 2) / (1 + self.deviation_upper),
                Q(self.shell_start, 2) / self._positive_lower())


def gamma_population_certificate(shell_start: int, scale, offset: int = 0):
    return PopulationFrameCertificate(shell_start, "gamma_poisson", scale, offset)


def fejer_population_certificate(shell_start: int, width: int, offset: int = 0):
    return PopulationFrameCertificate(shell_start, "finite_fejer", width, offset)


def gamma_clock_pmf(scale, index: int) -> Q:
    """K|T~Poisson(T), T~Gamma(shape=2,scale=scale); scale=0 is the point mass."""
    scale = _nonnegative(scale, "Gamma scale")
    k = _integer(index, "Probability index", 0, MAX_PROBABILITY_INDEX)
    ratio = scale / (1 + scale)
    return (k + 1) * ratio ** k / (1 + scale) ** 2


def gamma_clock_tail(scale, cutoff: int) -> Q:
    """Exact P(K>cutoff), without truncating an infinite sum."""
    scale = _nonnegative(scale, "Gamma scale")
    cutoff = _integer(cutoff, "Tail cutoff", 0, MAX_PROBABILITY_INDEX)
    ratio = scale / (1 + scale)
    return ratio ** (cutoff + 1) * (cutoff + 2 - (cutoff + 1) * ratio)


def fejer_clock_pmf(width: int, index: int, offset: int = 0) -> Q:
    """K=offset+1+U+V, independent uniforms U,V on 0..width-1.

    The support is the finite nonzero band offset+1..offset+2*width-1.
    Computing one weight is constant work; this helper does not enumerate it.
    """
    width = _integer(width, "Uniform clock width", 1)
    index = _integer(index, "Clock label")
    offset = _integer(offset, "Nonnegative clock offset", 0)
    return Q(max(0, width - abs(index - offset - width)), width * width)


def smallest_gram_eigenvalue_upper(shell_start: int, frequency_variance) -> Q:
    """Uniform linear reconstruction obstruction, using pi<22/7.

    For ANY clock law of finite variance V, lambda_min(G)<=2*pi^2*delta_B^2*V.
    Centering/offset cannot remove the adjacent-column obstruction.  This is
    a full-vector frame bound, not a lower bound for every estimator of one
    particular BBP statistic or for inference using additional source facts.
    """
    source = SourceSpacing(shell_start)
    variance = _nonnegative(frequency_variance, "Clock variance")
    return min(Q(1), Q(968, 49) * source.minimum_gap ** 2 * variance)


def source_phase_error_pi_units(intensity: int, source_error) -> Q:
    """Complex echo error <= pi*result when a source node errs by source_error."""
    intensity = _integer(intensity, "Integer intensity")
    error = _nonnegative(source_error, "Source-node error")
    return 2 * abs(intensity) * error


def echo_readout_error_pi_units(h: int, intensity: int, state_error, next_state_error) -> Q:
    """Raw two-tap readout error <= pi*result; exact recurrence avoids cancellation loss."""
    a, b = matched_echo_coefficients(h, intensity)
    first = _nonnegative(state_error, "Current-state error")
    second = _nonnegative(next_state_error, "Next-state error")
    return 2 * (abs(a) * first + abs(b) * second)
