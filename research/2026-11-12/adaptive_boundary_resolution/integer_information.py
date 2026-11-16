"""Exact integer histogram twins and channel bounds for damped observations.

This is a source-blind information boundary. No witness is asserted to be
an arithmetic grade histogram. All computations use integers and Fraction.
Running this module prints a report; it does not modify a receipt file.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
from math import prod


def _integer(value, minimum, name):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an exact integer >= {minimum}")
    return value


def _parameters(base, channels):
    return (_integer(base, 2, "base"),
            _integer(channels, 0, "channels"))


def _histogram(values):
    values = tuple(values)
    if not values or any(type(x) is not int or x < 0 for x in values):
        raise ValueError("a nonempty nonnegative integer histogram is required")
    return values


def _multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return tuple(result)


def annihilator(base: int, channels: int) -> tuple[int, ...]:
    """Ascending coefficients of (1-z) prod_{r=1}^d (1-b^r z)."""
    base, channels = _parameters(base, channels)
    result = (1, -1)
    for r in range(1, channels + 1):
        result = _multiply(result, (1, -(base ** r)))
    return result


def responses(histogram, base: int, channels: int) -> tuple[Fraction, ...]:
    """F(b^-r), r=1,...,d. Mass is deliberately a separate observation."""
    base, channels = _parameters(base, channels)
    histogram = _histogram(histogram)
    return tuple(sum((Fraction(c, base ** (r * h))
                      for h, c in enumerate(histogram)), Fraction())
                 for r in range(1, channels + 1))


@dataclass(frozen=True)
class IntegerTwins:
    base: int
    channels: int
    left: tuple[int, ...]
    right: tuple[int, ...]

    @property
    def mass(self):
        return sum(self.left)

    @property
    def zero_gap(self):
        return self.left[0] - self.right[0]


def twins(base: int, channels: int, *, multiplier=(1,),
          total_mass: int | None = None) -> IntegerTwins:
    """Split an integer annihilator multiple; optionally add common mass.

    A nonzero constant in the multiplier ensures that the zero counts
    differ. The sign is oriented to make the left zero count larger.
    Common padding is placed at grade one and preserves the zero gap.
    """
    base, channels = _parameters(base, channels)
    multiplier = tuple(multiplier)
    if (not multiplier or multiplier[0] == 0
            or any(type(x) is not int for x in multiplier)):
        raise ValueError("an integer multiplier with nonzero constant is required")
    polynomial = _multiply(annihilator(base, channels), multiplier)
    if polynomial[0] < 0:
        polynomial = tuple(-x for x in polynomial)
    left = [max(x, 0) for x in polynomial]
    right = [max(-x, 0) for x in polynomial]
    mass = sum(left)
    if total_mass is not None:
        total_mass = _integer(total_mass, mass, "total_mass")
        left[1] += total_mass - mass
        right[1] += total_mass - mass
    return IntegerTwins(base, channels, tuple(left), tuple(right))


def verify_twins(witness: IntegerTwins) -> bool:
    """Check the actual observations and target difference, not a label."""
    try:
        base, channels = _parameters(witness.base, witness.channels)
        left, right = _histogram(witness.left), _histogram(witness.right)
    except (ValueError, AttributeError, TypeError):
        return False
    return (sum(left) == sum(right) and left[0] != right[0]
            and responses(left, base, channels) == responses(right, base, channels))


def ambiguity_mass_bounds(base: int, channels: int) -> tuple[int, int]:
    """Proved lower bound and explicit upper witness; not an exact optimum.

    The lower bound for d>=1 follows from integer divisibility and the
    positive root. At d=0, one unit of mass already permits ambiguity.
    """
    base, channels = _parameters(base, channels)
    if channels == 0:
        return 1, 1
    triangular = channels * (channels + 1) // 2
    return base ** triangular + 1, prod(base ** r + 1
                                       for r in range(1, channels + 1))


def channel_bounds(base: int, mass: int) -> tuple[int, int]:
    """Lower/upper bounds on channels needed for every mass-M integer source.

    The lower bound uses explicit equal-mass twins and padding. The upper
    bound proves uniqueness of the entire histogram, without an algorithmic
    efficiency claim. For positive mass these bounds differ by at most one.
    """
    base, _ = _parameters(base, 0)
    mass = _integer(mass, 0, "mass")
    if mass == 0:
        return 0, 0
    upper = 1
    while base ** (upper * (upper + 1) // 2) < mass:
        upper += 1
    d, witness_mass = 0, 1
    while witness_mass <= mass:
        d += 1
        witness_mass *= base ** d + 1
    return d, upper


def prior_even_channels(base: int, mass: int) -> int:
    """Previous sufficient rule: even d>=2 and b^[d(d+1)/2]>M."""
    base, _ = _parameters(base, 0)
    mass = _integer(mass, 0, "mass")
    if mass == 0:
        return 0
    d = 2
    while base ** (d * (d + 1) // 2) <= mass:
        d += 2
    return d


def zero_count_from_adaptive_sample(mass: int, value) -> int:
    """Conditional one-sample recovery when the node may depend on mass.

    The caller must authenticate value = F(1/(M+1)) for an integer-count
    source of total mass M. This different access model is not subject to
    the fixed-base prefix channel lower bound. No oracle cost is asserted.
    """
    mass = _integer(mass, 0, "mass")
    if type(value) not in (int, Fraction):
        raise ValueError("an exact integer or Fraction response is required")
    value = Fraction(value)
    if not 0 <= value <= mass:
        raise ValueError("response contradicts the supplied mass")
    return value.numerator // value.denominator


def noise_packet(left, right, base: int, channels: int):
    """Common midpoint packet for normalized responses, with exact radius.

    Both integer sources have the same known positive mass and different
    zero counts. Each genuine normalized response is within radius of the
    returned midpoint in every coordinate. This is a deterministic
    indistinguishability witness, not a probabilistic noise model.
    """
    base, channels = _parameters(base, channels)
    if channels == 0:
        raise ValueError("at least one noisy response channel is required")
    left, right = _histogram(left), _histogram(right)
    mass = sum(left)
    if mass == 0 or mass != sum(right) or left[0] == right[0]:
        raise ValueError("equal positive mass and different zero counts required")
    a = tuple(x / mass for x in responses(left, base, channels))
    b = tuple(x / mass for x in responses(right, base, channels))
    return {"left": left, "right": right, "mass": mass,
            "left_responses": a, "right_responses": b,
            "midpoint": tuple((x + y) / 2 for x, y in zip(a, b)),
            "radius": max(abs(x - y) for x, y in zip(a, b)) / 2}


def unit_noise_witness(base: int, channels: int, mass: int):
    """One zero-grade count moved to grade one, with common mass padding."""
    mass = _integer(mass, 1, "mass")
    return noise_packet((1, mass - 1), (0, mass), base, channels)


def last_channel_noise_witness(base: int, channels: int,
                               mass: int | None = None):
    """First d-1 channels match exactly; only the final one separates."""
    _integer(channels, 1, "channels")
    witness = twins(base, channels - 1, total_mass=mass)
    return noise_packet(witness.left, witness.right, base, channels)


def report():
    rows = []
    for base in (2, 3, 5):
        for d in range(1, 7):
            witness = twins(base, d)
            lower, upper = ambiguity_mass_bounds(base, d)
            rows.append({"base": base, "channels": d,
                         "ambiguity_mass_lower": lower,
                         "product_witness_mass": upper,
                         "left": witness.left, "right": witness.right,
                         "zero_gap": witness.zero_gap,
                         "responses": [str(x) for x in responses(witness.left, base, d)],
                         "verified": verify_twins(witness)})
    improved = twins(2, 2, multiplier=(1, 1))
    return {"scope": "source-blind integer histograms; no arithmetic realization claim",
            "witnesses": rows,
            "product_is_not_optimal_control": {
                "base": 2, "channels": 2, "product_mass": 15,
                "improved_mass": improved.mass,
                "left": improved.left, "right": improved.right,
                "verified": verify_twins(improved)},
            "channel_examples": [
                {"mass": mass, "bounds": channel_bounds(2, mass),
                 "prior_even_channels": prior_even_channels(2, mass)}
                for mass in (1, 2, 3, 8, 9, 14, 15, 1000, 1024, 1025,
                             10 ** 6, 10 ** 12)]}


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
