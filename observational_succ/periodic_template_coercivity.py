"""Exact finite instruments for simultaneous periodic-template coercivity.

The analytic theorem bounds the sum of absolute residue-class Fourier sums,
uniformly over every periodic unit template. It retains the 1/14 logarithmic
absolute loss and its unknown onset; it does not establish normality.

The generic inverse lemma accepts arbitrary real forcing in the paper. This
finite instrument accepts exact rationals and assigns no BBP source passport
to generic initial states, templates, or branch data.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .bbp_diophantine_coherence import circle_distance, ceil_log, floor_log
from .global_branch_coercivity import BLOCK_LOSS, whole_block_parameters
from .succ_internal_matrix_walk import authentic_r


MIN_SCALE_PER_PERIOD = 4096
PRIOR_SOURCE_COMMIT = "848bad224fef455a9f87ed19e947c936d309c965"
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


def residue_transition_counts(transitions, period):
    """Exact counts for transition indices 0,...,T-1 modulo p."""
    _integer(transitions, 1)
    _integer(period, 1)
    return tuple((transitions+period-1-s)//period for s in range(period))


@dataclass(frozen=True)
class PeriodicBranchParameters:
    transitions: int
    period: int
    minimum_residue_count: int
    forcing_span: Q
    quiet_sqrt_upper: Q
    nonperiodic_loss_lower: Q


def periodic_branch_parameters(transitions, period, forcing_span,
                               quiet_sqrt_upper=Q(1, 100)):
    """Generic finite lemma, independent of authentic forcing or zero seed.

    If the template-weighted loss is <=1/14, these hypotheses force the
    lifted integer branch word to be p-periodic. No bound on frequency is
    implicit: forcing_span already equals abs(h)*(max forcing-min forcing).
    """
    _integer(transitions, 2)
    _integer(period, 1)
    count = transitions//period
    core = whole_block_parameters(count, forcing_span, quiet_sqrt_upper)
    return PeriodicBranchParameters(transitions, period, count,
                                     core.forcing_span, core.quiet_sqrt_upper,
                                     core.nonconstant_loss_lower)


def authentic_forcing_parameters(m, period=1, frequency=1):
    """Original pole-range conditions only; U_0=0 is an additional theorem input."""
    _integer(period)
    _integer(m, MIN_SCALE_PER_PERIOD*period)
    h = abs(_frequency(frequency))
    if 64*h > m*m:
        raise ValueError("the authentic band requires 64*abs(h) <= m squared")
    span = h*(authentic_r(m+2)-authentic_r(8*m))
    if not 0 < span < Q(15, 4096):
        raise ArithmeticError("the literal four-pole source range failed")
    return periodic_branch_parameters(7*m-1, period, span)


def periodic_integer_solution(branch_pattern):
    """Unique p-periodic f with f_(t+1)=16*f_t+k_t, in (16^p-1)^-1 Z.

    The input is the actual integer branch word; arbitrary template phases
    do not enter the rational periodic solution or its conductor.
    """
    pattern = tuple(branch_pattern)
    _integer(len(pattern), 1, 4096)
    if any(type(k) is not int for k in pattern):
        raise ValueError("the periodic branch word must contain exact integers")
    numerator = 0
    for k in pattern:
        numerator = 16*numerator+k
    first = -Q(numerator, 16**len(pattern)-1)
    values = [first]
    for k in pattern[:-1]:
        values.append(16*values[-1]+k)
    if 16*values[-1]+pattern[-1] != first:
        raise ArithmeticError("periodic rational branch solution failed")
    return tuple(values)


@dataclass(frozen=True)
class PeriodicLiftWitness:
    energy: Q
    period: int
    branches: tuple[int, ...]
    quiet_transition_indices: tuple[int, ...]
    incompatible_branch_pair: tuple[int, int] | None


def periodic_lift_witness(centered_offsets, forcing, template_phases,
                          frequency=1, center=0):
    """Check the exact integer lifts and find a quiet pair in each residue.

    Rational template phases repeat exactly. This instrument does not claim
    that the supplied center is the direction of a complex resultant.
    """
    offsets = tuple(_rational(x) for x in centered_offsets)
    forcing = tuple(_rational(x) for x in forcing)
    template = tuple(_rational(x) for x in template_phases)
    frequency = _frequency(frequency)
    center = _rational(center)
    _integer(len(forcing), 2, 100000)
    _integer(len(template), 1, len(forcing))
    if len(offsets) != len(forcing)+1 or any(abs(q) > Q(1, 2) for q in offsets):
        raise ValueError("centered offsets and forcing have incompatible domains")
    period = len(template)
    branches = []
    for t, r in enumerate(forcing):
        k = (template[(t+1) % period]-16*template[t % period]-15*center
             +offsets[t+1]-16*offsets[t]-frequency*r)
        if k.denominator != 1:
            raise ValueError("the proposed source/template lift has a noninteger branch")
        branches.append(int(k))
    quiet = tuple(min(range(s, len(forcing), period),
                      key=lambda t: offsets[t]**2+offsets[t+1]**2)
                  for s in range(period))
    bad_pair = next(((quiet[t % period], t) for t in range(len(forcing))
                     if branches[t] != branches[quiet[t % period]]), None)
    return PeriodicLiftWitness(sum((q*q for q in offsets), Q()), period,
                               tuple(branches), quiet, bad_pair)


@dataclass(frozen=True)
class PeriodicInverseCertificate:
    initial: Q
    forcing: tuple[Q, ...]
    frequency: int
    period: int
    parameters: PeriodicBranchParameters
    weighted_source: Q
    terminal_period_forcing: Q
    center_denominator: int
    arc_radius: Q
    distance_to_centers: Q

    @property
    def outside_arcs(self):
        """If true, EVERY period-p unit template has loss strictly >1/14."""
        return self.distance_to_centers > self.arc_radius


def inverse_periodic_certificate(initial, forcing, period=1, frequency=1,
                                 quiet_sqrt_upper=Q(1, 100)):
    """Generic ordered-source inverse arc, without a frequency-band restriction."""
    initial = _rational(initial)
    forcing = tuple(_rational(x) for x in forcing)
    _integer(len(forcing), 2, 100000)
    _integer(period, 1, len(forcing))
    frequency = _frequency(frequency)
    h = abs(frequency)
    parameters = periodic_branch_parameters(
        len(forcing), period, h*(max(forcing)-min(forcing)), quiet_sqrt_upper)
    source = Q()
    for r in reversed(forcing):
        source = (source+r)/16
    terminal = Q()
    for r in forcing[-period:]:
        terminal = 16*terminal+r
    base = 16**period
    denominator = (base-1)*h
    radius = (Q(base, 5)+h*abs(terminal))/(denominator*16**len(forcing))
    distance = circle_distance(denominator*(initial+source))/denominator
    return PeriodicInverseCertificate(initial, forcing, frequency, period,
                                       parameters, source, terminal, denominator,
                                       radius, distance)


def approximation_coefficient_bound(m, period=1, frequency=1):
    """B<4 for the authentic inverse approximation B*16^(-8m), if p<=m."""
    _integer(m)
    _integer(period, 1, m)
    h = abs(_frequency(frequency))
    return 16*(Q(16, 75*h)+Q(1, 64*(8*m-period)**2)+Q(1, 64*(8*m)**2))


def diophantine_scale_comparison(m, period, frequency, constant):
    """Exact sufficient comparison; it does NOT certify C as valid for pi."""
    _integer(m, 1, 100000)
    _integer(period, 1, 100000)
    h = abs(_frequency(frequency))
    constant = _rational(constant)
    if not 0 < constant <= 1:
        raise ValueError("the supplied comparison constant must lie in (0,1]")
    return constant**2*16**m > 16*(h*(16**period-1))**15


def uniform_threshold_comparison(m0, constant):
    """Conditional uniform onset for p<=m/4096 and |h|<=m²/64, m>=m0.

    The stronger sufficient rational comparison is C^4*16^m>256*m^60.
    Supplied C and the numerical onset remain separately uncertified.
    """
    _integer(m0, MIN_SCALE_PER_PERIOD, 100000)
    constant = _rational(constant)
    if not 0 < constant <= 1:
        raise ValueError("the supplied comparison constant must lie in (0,1]")
    return constant**4*16**m0 > 256*m0**60


@dataclass(frozen=True)
class ConditionalPeriodicBudget:
    observations: int
    period: int
    maximum_frequency: int
    threshold_exponent: int
    eligible_blocks: int

    @property
    def residue_modulus_sum_upper(self):
        return self.observations-BLOCK_LOSS*self.eligible_blocks

    @property
    def numerical_onset_certified(self):
        return False


def conditional_periodic_budget(observations, period, maximum_frequency,
                                threshold_exponent):
    """All-N combinatorial budget with a supplied, not certified, onset J."""
    _integer(observations)
    _integer(period)
    _integer(maximum_frequency)
    _integer(threshold_exponent, 4)
    first = max(threshold_exponent, 4+ceil_log(period, 8),
                1+ceil_log(maximum_frequency, 64))
    count = max(0, floor_log(observations, 8)-first)
    return ConditionalPeriodicBudget(observations, period, maximum_frequency,
                                      threshold_exponent, count)
