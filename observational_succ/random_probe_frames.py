"""Exact budgets for independent random phase-frame rows.

This is a conditional matrix-Chernoff certificate, not a sampler, a certificate
for a realized matrix, or a statement about the source's normality. Each row
v has B unit-modulus entries and population Gram G with (1-eta)I <= G <=
(1+eta)I. Rows must be independently drawn from that declared law.
"""

from dataclasses import dataclass
from fractions import Fraction


Q = Fraction


def _rational(value: int | Q, name: str) -> Q:
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise ValueError(name + " must be an exact integer or Fraction")
    return Q(value)


def _ceil(value: Q) -> int:
    return -((-value.numerator) // value.denominator)


def ceil_log2_ratio(value: int | Q) -> int:
    """Least nonnegative integer L with 2**L >= value, for value >= 1."""
    value = _rational(value, "ratio")
    if value < 1:
        raise ValueError("ratio must be at least one")
    level = max(0, value.numerator.bit_length() - value.denominator.bit_length())
    if (1 << level) * value.denominator < value.numerator:
        level += 1
    return level


@dataclass(frozen=True)
class FrameSamplingCertificate:
    dimension: int
    population_error: Q
    relative_error: Q
    requested_failure_probability: Q
    binary_log_budget: int
    independent_rows: int
    failure_probability_upper: Q
    gram_eigenvalue_lower: Q
    gram_eigenvalue_upper: Q
    gram_condition_upper: Q
    normalized_echo_vector_noise_gain_squared: Q
    normalized_echo_mean_noise_gain_squared: Q


def frame_sampling_certificate(
    dimension: int,
    population_error: int | Q,
    relative_error: int | Q = Q(1, 2),
    failure_probability: int | Q = Q(1, 64),
) -> FrameSamplingCertificate:
    """Return conservative rational row and stability budgets.

    With eta=population_error and epsilon=relative_error, whitening and
    matrix Chernoff give failure <= 2B exp(-s epsilon**2 (1-eta)/(3B)).
    We take s >= 3B L/((1-eta)epsilon**2), 2**L >= 2B/delta, and use e>2.

    Echo values are F_j=B**(-1) sum_n c_n exp(2pi i K_j t_n). The error
    norm is the RMS over j. Full-vector noise amplification is <= B/sqrt(l),
    and mean B**(-1)sum c_n amplification is <= sqrt(B/l), where l is the
    certified empirical Gram lower bound. A condition number of the sampling
    matrix itself is the square root of the Gram condition number.
    """
    if isinstance(dimension, bool) or not isinstance(dimension, int) or not 1 <= dimension <= 4096:
        raise ValueError("implemented dimension budget is 1..4096")
    eta = _rational(population_error, "population_error")
    epsilon = _rational(relative_error, "relative_error")
    delta = _rational(failure_probability, "failure_probability")
    if not 0 <= eta < 1:
        raise ValueError("population_error must lie in [0,1)")
    if not 0 < epsilon < 1:
        raise ValueError("relative_error must lie in (0,1)")
    if not 0 < delta < 1:
        raise ValueError("failure_probability must lie in (0,1)")
    level = ceil_log2_ratio(Q(2 * dimension) / delta)
    count = _ceil(Q(3 * dimension * level) / ((1 - eta) * epsilon**2))
    lower = (1 - epsilon) * (1 - eta)
    upper = (1 + epsilon) * (1 + eta)
    return FrameSamplingCertificate(
        dimension, eta, epsilon, delta, level, count,
        Q(2 * dimension, 1 << level), lower, upper, upper / lower,
        Q(dimension**2) / lower, Q(dimension) / lower,
    )
