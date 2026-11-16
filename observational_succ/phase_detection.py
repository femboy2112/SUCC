"""Exact bounded controls for randomized phase readouts and detection dose.

Gamma response uses integer shape and rational angular frequency/rate, so
its complex multiplier has exact rational real and imaginary parts. The
module does not evaluate transcendental source phases numerically. Finite
circle laws, propensity identities, and repetition probabilities are exact.

The only BBP-specific function bounds the explicitly CHANGED seed -pi/16,
using the unmodified original-source tail enclosure. It cannot authenticate
the zero-seeded escape estimate. Proofs and scope:
research/2026-11-15/pi_carrier_collision/ADVERSARY_NOTES.md.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from .duck_bbp import tail_interval


MAX_SHAPE = 64
MAX_CIRCLE = 64
MAX_TRIALS = 4096
MAX_SHELL = 128
MAX_TAIL_DEPTH = 32
GaussianRational = tuple[Q, Q]


def _q(value, name="value") -> Q:
    if type(value) not in (int, Q):
        raise ValueError(f"{name} must be an exact int or Fraction")
    return Q(value)


def _integer(value, name, minimum=0, maximum=None) -> int:
    if type(value) is not int or value < minimum or (maximum is not None and value > maximum):
        raise ValueError(f"{name} is outside its declared integer domain")
    return value


def _gamma_parameters(shape, rate, angular_frequency):
    shape = _integer(shape, "shape", 1, MAX_SHAPE)
    rate, omega = _q(rate, "rate"), _q(angular_frequency, "angular frequency")
    if rate <= 0:
        raise ValueError("Gamma rate must be positive")
    return shape, rate, omega


def _complex_product(a: GaussianRational, b: GaussianRational) -> GaussianRational:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def gamma_rotation_response(shape: int, rate, angular_frequency) -> GaussianRational:
    """E exp(i*omega*T)=(rate/(rate-i*omega))**shape, T Gamma(shape,rate).

    The return value is (real,imaginary), both Fractions. Omega is angular
    frequency, not an integer turns-frequency with an omitted 2*pi.
    """
    shape, rate, omega = _gamma_parameters(shape, rate, angular_frequency)
    denominator = rate*rate+omega*omega
    step = (rate*rate/denominator, rate*omega/denominator)
    result = (Q(1), Q())
    for _ in range(shape):
        result = _complex_product(result, step)
    return result


def gamma_inverse_squared(shape: int, rate, angular_frequency) -> Q:
    """Squared condition number for recovering a mean after forgetting its clock."""
    shape, rate, omega = _gamma_parameters(shape, rate, angular_frequency)
    return (1+(omega/rate)**2)**shape


def gamma_recovery_mse(shape: int, rate, angular_frequency, samples: int) -> Q:
    """Exact MSE of (sum Y_n)/(samples*m), for deterministic unit phases.

    The clocks must be mutually independent, with the declared common law;
    m is gamma_rotation_response. This concerns that unbiased estimator,
    not a lower bound for every conceivable recovery procedure.
    """
    samples = _integer(samples, "samples", 1)
    return (gamma_inverse_squared(shape, rate, angular_frequency)-1)/samples


def retained_clock_error_bound(angular_frequency, clock_error) -> Q:
    """Unit-phase demodulation error <=min(2,abs(omega)*clock_error)."""
    omega, error = _q(angular_frequency), _q(clock_error)
    if error < 0:
        raise ValueError("clock error must be nonnegative")
    return min(Q(2), abs(omega)*error)


def _law(value) -> tuple[Q, ...]:
    if not isinstance(value, (tuple, list)) or not 1 <= len(value) <= MAX_CIRCLE:
        raise ValueError("require a bounded finite probability law")
    result = tuple(_q(x, "probability") for x in value)
    if any(x < 0 for x in result) or sum(result, Q()) != 1:
        raise ValueError("probabilities must be nonnegative and sum to one")
    return result


def phase_rotation_law(source, clock) -> tuple[tuple[Q, ...], ...]:
    """Joint law (Y,C), Y=S+C mod q, for independent supplied source/clock laws.

    Rows index rotated output Y; columns retain the clock C. Uniform clocks
    make Y uniform for every source when C is forgotten.
    """
    source, clock = _law(source), _law(clock)
    if len(source) != len(clock):
        raise ValueError("source and clock must use the same finite circle")
    size = len(source)
    return tuple(tuple(source[(y-c) % size]*clock[c] for c in range(size))
                 for y in range(size))


def _joint(value) -> tuple[tuple[Q, ...], ...]:
    if not isinstance(value, (tuple, list)) or not 1 <= len(value) <= MAX_CIRCLE:
        raise ValueError("require a bounded square joint law")
    size = len(value)
    if any(not isinstance(row, (tuple, list)) or len(row) != size for row in value):
        raise ValueError("joint law must be square")
    result = tuple(tuple(_q(x, "joint probability") for x in row) for row in value)
    if any(x < 0 for row in result for x in row) or sum((sum(row, Q()) for row in result), Q()) != 1:
        raise ValueError("joint probabilities must be nonnegative and sum to one")
    return result


def forget_clock(joint) -> tuple[Q, ...]:
    """Rotated-output marginal of a retained finite (Y,C) law."""
    return tuple(sum(row, Q()) for row in _joint(joint))


def recover_retained_phase(joint) -> tuple[Q, ...]:
    """Recover S=Y-C mod q from the full joint law, even for dependent clocks."""
    law = _joint(joint)
    size = len(law)
    return tuple(sum((law[(s+c) % size][c] for c in range(size)), Q())
                 for s in range(size))


@dataclass(frozen=True)
class PropensityCertificate:
    target_mean: Q
    selected_mean: Q
    corrected_mean: Q
    corrected_second_moment: Q
    corrected_variance: Q


def propensity_certificate(values, sampling_probabilities) -> PropensityCertificate:
    """Uniform finite-population target with exact inverse-propensity recovery.

    One sampled index I has probability q_I; the corrected observation is
    values[I]/(N*q_I). Every propensity must be positive and known. Values
    are real rational observables; complex Fourier parts can be separate.
    """
    probabilities = _law(sampling_probabilities)
    if not isinstance(values, (tuple, list)) or len(values) != len(probabilities):
        raise ValueError("one observable value per sampling index is required")
    values = tuple(_q(x, "observable") for x in values)
    if any(p == 0 for p in probabilities):
        raise ValueError("zero propensity prevents general source recovery")
    size = len(values)
    target = sum(values, Q())/size
    selected = sum((p*x for p, x in zip(probabilities, values)), Q())
    corrected = tuple(x/(size*p) for p, x in zip(probabilities, values))
    mean = sum((p*x for p, x in zip(probabilities, corrected)), Q())
    second = sum((p*x*x for p, x in zip(probabilities, corrected)), Q())
    if mean != target:
        raise ArithmeticError("inverse-propensity identity failed")
    return PropensityCertificate(target, selected, mean, second, second-target*target)


def detection_probability(escape_mean, trials: int) -> Q:
    """Fresh-trial success probability 1-(1-A/2)**trials, 0<=A<=2.

    For a shell, first sample a source index uniformly, then accept with
    probability (1-cos(2*pi*phase))/2. A is the unmodified shell escape
    mean. Reusing a single recorded trial does not obey this formula.
    """
    escape = _q(escape_mean, "escape mean")
    trials = _integer(trials, "trials", 0, MAX_TRIALS)
    if not 0 <= escape <= 2:
        raise ValueError("escape mean must lie in [0,2]")
    return 1-(1-escape/2)**trials


def detection_probability_bounds(escape_lower, escape_upper, trials: int) -> tuple[Q, Q]:
    lower, upper = _q(escape_lower), _q(escape_upper)
    if lower > upper:
        raise ValueError("reversed escape interval")
    return detection_probability(lower, trials), detection_probability(upper, trials)


def minimum_detection_trials(escape_mean, failure_tolerance, *, max_trials=MAX_TRIALS) -> int | None:
    """Least fresh-trial budget within the bound, or None if not certified.

    All decisions compare exact rational powers. No logarithmic rounding.
    """
    escape, tolerance = _q(escape_mean), _q(failure_tolerance)
    maximum = _integer(max_trials, "max trials", 0, MAX_TRIALS)
    if not 0 < tolerance < 1:
        raise ValueError("failure tolerance must lie strictly between zero and one")
    target = 1-tolerance
    if detection_probability(escape, maximum) < target:
        return None
    low, high = 0, maximum
    while low < high:
        middle = (low+high)//2
        if detection_probability(escape, middle) >= target:
            high = middle
        else:
            low = middle+1
    return low


def counterseed_escape_interval(shell: int, *, tail_depth=4) -> tuple[Q, Q]:
    """Exact escape enclosure for U_n(-pi/16)=-T_n, n in [B,2B).

    This keeps the original four-pole forcing but changes the initial seed.
    Inherited rational tail intervals and 3<pi<22/7 give, when 2*pi*T<=1,
    12*T_lower**2 <=1-cos(2*pi*T)<= (968/49)*T_upper**2.
    The range check is exact; no transcendental numerical evaluation occurs.
    """
    shell = _integer(shell, "shell", 1, MAX_SHELL)
    depth = _integer(tail_depth, "tail depth", 1, MAX_TAIL_DEPTH)
    lower, upper = Q(), Q()
    for n in range(shell, 2*shell):
        lo, hi = tail_interval(n, depth)
        if not (0 < lo <= hi and Q(44, 7)*hi <= 1):
            raise ArithmeticError("source tail left the proved small-angle domain")
        lower += 12*lo*lo
        upper += Q(968, 49)*hi*hi
    return lower/shell, upper/shell
