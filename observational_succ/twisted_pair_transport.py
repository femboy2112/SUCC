"""Exact two-wire transport and the even-radix antiphase obstruction.

Gaussian values are pairs of Fractions, never floating-point complex numbers.
Rational circle phases stay rational; only quarter-turn phases are converted
to Gaussian values. In particular this module does not numerically evaluate
the authentic BBP Fourier sums or assert their asymptotic cancellation.

The wire connection reconstructs signed correlations despite an unknown
initial wire identity. A separate exact certificate shows that two synchronous
trajectories with identical even-radix forcing cannot remain antipodal.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence

from .bbp_source_memory import forcing

Rational = int | Q
Gaussian = tuple[Q, Q]
GaussianInput = tuple[Rational, Rational]
ZERO: Gaussian = (Q(0), Q(0))


def _integer(value: int, minimum: int | None = None) -> int:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("expected an integer in the stated domain")
    return value


def _rational(value: Rational) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("expected an exact int or Fraction")
    return Q(value)


def _sign(value: int) -> int:
    if type(value) is not int or value not in (-1, 1):
        raise ValueError("wire signs must be the integers -1 or +1")
    return value


def _gaussian(value: GaussianInput) -> Gaussian:
    if type(value) is not tuple or len(value) != 2:
        raise ValueError("Gaussian value must be an exact (real, imag) tuple")
    return _rational(value[0]), _rational(value[1])


def _add(first: Gaussian, second: Gaussian) -> Gaussian:
    return first[0] + second[0], first[1] + second[1]


def _scale(sign: int, value: Gaussian) -> Gaussian:
    return sign * value[0], sign * value[1]


def _multiply(first: Gaussian, second: Gaussian) -> Gaussian:
    a, b = first
    c, d = second
    return a * c - b * d, a * d + b * c


def _conjugate(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def _norm_squared(value: Gaussian) -> Q:
    return value[0] ** 2 + value[1] ** 2


def gaussian(real: Rational = 0, imag: Rational = 0) -> Gaussian:
    """Construct a Gaussian rational, rejecting floats, bools and strings."""
    return _rational(real), _rational(imag)


def gaussian_product(first: GaussianInput, second: GaussianInput) -> Gaussian:
    return _multiply(_gaussian(first), _gaussian(second))


def gaussian_conjugate(value: GaussianInput) -> Gaussian:
    return _conjugate(_gaussian(value))


def gaussian_norm_squared(value: GaussianInput) -> Q:
    return _norm_squared(_gaussian(value))


def rational_phase(value: Rational) -> Q:
    """Canonical representative in [0,1), with a strict exact-input gate."""
    return _rational(value) % 1


def circle_distance(value: Rational, target: Rational = 0) -> Q:
    residue = (_rational(value) - _rational(target)) % 1
    return min(residue, 1 - residue)


def quarter_turn_phase(value: Rational) -> Gaussian:
    """Exact e(value) ONLY when 4*value is an integer; no rounding."""
    index = 4 * rational_phase(value)
    if index.denominator != 1:
        raise ValueError("Gaussian phase conversion requires a quarter turn")
    return (gaussian(1), gaussian(0, 1), gaussian(-1), gaussian(0, -1))[
        index.numerator
    ]


def wire_twists(orientations: Sequence[int]) -> tuple[int, ...]:
    """Edge transport a_t=s_(t+1)*s_t; the initial sign is unrecorded."""
    signs = tuple(_sign(value) for value in orientations)
    return tuple(right * left for left, right in zip(signs, signs[1:]))


def apply_wire_orientation(
    signal: Sequence[GaussianInput], orientations: Sequence[int]
) -> tuple[Gaussian, ...]:
    samples = tuple(_gaussian(value) for value in signal)
    signs = tuple(_sign(value) for value in orientations)
    if len(samples) != len(signs):
        raise ValueError("one orientation is required for every sample")
    return tuple(_scale(sign, value) for sign, value in zip(signs, samples))


def path_transport(twists: Sequence[int], start: int, stop: int) -> int:
    """Z2 transport in either direction along the vertices 0,...,len(twists)."""
    edges = tuple(_sign(value) for value in twists)
    _integer(start, 0)
    _integer(stop, 0)
    if start > len(edges) or stop > len(edges):
        raise ValueError("transport endpoint is outside the path")
    product = 1
    for edge in edges[min(start, stop):max(start, stop)]:
        product *= edge
    return product


def _connected_samples(
    observed: Sequence[GaussianInput], twists: Sequence[int]
) -> tuple[tuple[Gaussian, ...], tuple[int, ...]]:
    samples = tuple(_gaussian(value) for value in observed)
    edges = tuple(_sign(value) for value in twists)
    if len(edges) != max(0, len(samples) - 1):
        raise ValueError("the path must have exactly one twist between samples")
    return samples, edges


def recover_signal(
    observed: Sequence[GaussianInput], twists: Sequence[int],
    initial_orientation: int = 1,
) -> tuple[Gaussian, ...]:
    """Recover up to one global sign; supplying the actual s_0 recovers exactly.

    With the default initial orientation the result is s_0*z_t. Neither
    signed lag correlations nor the squared sum depend on this ambiguity.
    """
    samples, edges = _connected_samples(observed, twists)
    orientation = _sign(initial_orientation)
    recovered = []
    for index, sample in enumerate(samples):
        if index:
            orientation *= edges[index - 1]
        recovered.append(_scale(orientation, sample))
    return tuple(recovered)


def signed_lag_correlation(signal: Sequence[GaussianInput], lag: int) -> Gaussian:
    """Sum z_(t+lag)*conjugate(z_t), including signed imaginary parts."""
    samples = tuple(_gaussian(value) for value in signal)
    _integer(lag, 0)
    result = ZERO
    for index in range(max(0, len(samples) - lag)):
        result = _add(result, _multiply(samples[index + lag],
                                       _conjugate(samples[index])))
    return result


def transported_lag_correlation(
    observed: Sequence[GaussianInput], twists: Sequence[int], lag: int
) -> Gaussian:
    """Sum P_(t,t+lag)*d_(t+lag)*conjugate(d_t), using the recorded path."""
    samples, edges = _connected_samples(observed, twists)
    _integer(lag, 0)
    result = ZERO
    for index in range(max(0, len(samples) - lag)):
        transport = 1
        for edge in edges[index:index + lag]:
            transport *= edge
        term = _multiply(samples[index + lag], _conjugate(samples[index]))
        result = _add(result, _scale(transport, term))
    return result


def quadratic_sum(signal: Sequence[GaussianInput]) -> Q:
    """Exact |sum z_t|^2, not a proof of asymptotic cancellation."""
    total = ZERO
    for value in signal:
        total = _add(total, _gaussian(value))
    return _norm_squared(total)


def transported_quadratic_sum(
    observed: Sequence[GaussianInput], twists: Sequence[int]
) -> Q:
    """The source sum magnitude, invariant under the unknown starting wire."""
    return quadratic_sum(recover_signal(observed, twists))


def quadrature_mismatch_energy(
    local: Sequence[GaussianInput], complement: Sequence[GaussianInput],
    quadrature: int,
) -> Q:
    """Mean |U-i^quadrature*conjugate(V)|^2 for exact UNIT phases.

    E_0=2-2*Re(mean U*V), E_1=2-2*Im(mean U*V). Small E_0 means
    coherence, not cancellation. This is an observation identity only.
    """
    first = tuple(_gaussian(value) for value in local)
    second = tuple(_gaussian(value) for value in complement)
    _integer(quadrature, 0)
    if quadrature > 3 or not first or len(first) != len(second):
        raise ValueError("use quadrature 0..3 and nonempty matching signals")
    if any(_norm_squared(value) != 1 for value in first + second):
        raise ValueError("quadrature identity requires unit phases")
    rotation = quarter_turn_phase(Q(quadrature, 4))
    total = Q()
    for u, v in zip(first, second):
        rotated = _multiply(rotation, _conjugate(v))
        total += _norm_squared((u[0] - rotated[0], u[1] - rotated[1]))
    return total / len(first)


@dataclass(frozen=True)
class AntiphaseCertificate:
    """Finite exact evaluation of the proved two-transition inequality."""

    base: int
    frequency: int
    difference: Q
    forcing_difference: Q
    next_difference: Q
    first_error: Q
    next_error: Q
    forcing_error: Q
    lower_bound: Q

    @property
    def observed_maximum(self) -> Q:
        return max(self.first_error, self.next_error)

    @property
    def bound_verified(self) -> bool:
        return self.observed_maximum >= self.lower_bound

    @property
    def attains_bound(self) -> bool:
        return self.observed_maximum == self.lower_bound


def antiphase_certificate(
    base: int, difference: Rational, frequency: int = 1,
    forcing_difference: Rational = 0,
) -> AntiphaseCertificate:
    """Certify max antiphase error >= (1/2-beta)/(b+1), for EVEN b.

    beta=dist(h*forcing_difference,0). Identical forcing gives beta=0
    and the sharp bound 1/[2(b+1)]. Both transitions and phase errors
    are computed exactly; no complex exponentials are approximated.
    """
    _integer(base, 2)
    _integer(frequency)
    if base % 2:
        raise ValueError("the antiphase obstruction requires an even radix")
    delta = rational_phase(difference)
    eta = rational_phase(forcing_difference)
    next_delta = (base * delta + eta) % 1
    beta = circle_distance(frequency * eta)
    certificate = AntiphaseCertificate(
        base, frequency, delta, eta, next_delta,
        circle_distance(frequency * delta, Q(1, 2)),
        circle_distance(frequency * next_delta, Q(1, 2)), beta,
        (Q(1, 2) - beta) / (base + 1),
    )
    if not certificate.bound_verified:
        raise ArithmeticError("the exact antiphase inequality failed")
    return certificate


def sharp_antiphase_cycle(base: int) -> tuple[Q, Q]:
    """The equality two-cycle: at b=16 it is (9/17,8/17)."""
    _integer(base, 2)
    if base % 2:
        raise ValueError("the sharp obstruction cycle requires an even radix")
    error = Q(1, 2 * (base + 1))
    return Q(1, 2) + error, Q(1, 2) - error


def verify_bbp_path(states: Sequence[Rational], initial: Rational = 0) -> bool:
    """Check the exact forcing and initial value from n=0; no phase rounding.

    With initial=0 this checks the authentic finite BBP path. An explicitly
    different initial value describes a control, not the selected pi source.
    """
    values = tuple(_rational(value) for value in states)
    start = rational_phase(initial)
    if not values or values[0] != start:
        return False
    if any(not 0 <= value < 1 for value in values):
        return False
    return all(values[n] == (16 * values[n - 1] + forcing(n)) % 1
               for n in range(1, len(values)))


@dataclass(frozen=True)
class BBPSynchronousPair:
    """Authentic y_0=0 path plus an explicitly changed-initial control."""

    selected: tuple[Q, ...]
    control: tuple[Q, ...]
    differences: tuple[Q, ...]
    source: tuple[Q, ...]
    selected_carries: tuple[int, ...]
    control_carries: tuple[int, ...]


def bbp_synchronous_pair(steps: int, control_initial: Rational) -> BBPSynchronousPair:
    """Retain the literal BBP forcing, rational phases, and BOTH carry histories."""
    _integer(steps, 0)
    control_start = rational_phase(control_initial)
    selected = [Q()]
    control = [control_start]
    selected_carries = []
    control_carries = []
    source = []
    for n in range(1, steps + 1):
        impulse = forcing(n)
        source.append(impulse)
        for path, carries in ((selected, selected_carries),
                              (control, control_carries)):
            unwrapped = 16 * path[-1] + impulse
            carry = unwrapped.numerator // unwrapped.denominator
            carries.append(carry)
            path.append(unwrapped - carry)
    differences = tuple((v - u) % 1 for u, v in zip(selected, control))
    if not verify_bbp_path(selected) or not verify_bbp_path(control, control_start):
        raise ArithmeticError("BBP source recurrence did not authenticate")
    if any(differences[n] != (16 * differences[n - 1]) % 1
           for n in range(1, steps + 1)):
        raise ArithmeticError("same-forcing difference failed radix transport")
    return BBPSynchronousPair(tuple(selected), tuple(control), differences,
                              tuple(source), tuple(selected_carries),
                              tuple(control_carries))
