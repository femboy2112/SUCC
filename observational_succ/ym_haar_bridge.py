"""Source-weighted, detail-preserving Haar coordinates with exact arithmetic.

This is a finite real-rational specialization of a Hilbert-space change of
basis.  The source weights and transformed observables remain part of the
representation.  Neither a quantum field construction nor an arithmetic
equidistribution estimate is inferred from these identities.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from typing import Sequence

from observational_succ.carry_safe_polyphase import polyphase_coords, tensor_unitary


Rational = int | Q


def _q(value: Rational) -> Q:
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise TypeError("exact int or Fraction required")
    return Q(value)


def _weights(values: Sequence[Rational]) -> tuple[Q, ...]:
    result = tuple(_q(value) for value in values)
    if not result or any(value <= 0 for value in result):
        raise ValueError("a nonempty list of strictly positive source weights is required")
    return result


def weighted_energy(values: Sequence[Rational], weights: Sequence[Rational]) -> Q:
    data, mass = tuple(_q(x) for x in values), _weights(weights)
    if len(data) != len(mass):
        raise ValueError("one source weight per value is required")
    return sum((w * x * x for w, x in zip(mass, data)), Q())


@dataclass(frozen=True)
class WeightedSplit:
    """Binary Haar coordinates in the metric diag(p,q), without square roots."""

    p: Rational
    q: Rational

    def __post_init__(self) -> None:
        p, q = _weights((self.p, self.q))
        object.__setattr__(self, "p", p)
        object.__setattr__(self, "q", q)

    @property
    def mass(self) -> Q:
        return self.p + self.q

    @property
    def coefficient_weights(self) -> tuple[Q, Q]:
        return self.mass, self.p * self.q / self.mass

    def analyze(self, left: Rational, right: Rational) -> tuple[Q, Q]:
        left, right = _q(left), _q(right)
        return (self.p * left + self.q * right) / self.mass, left - right

    def synthesize(self, mean: Rational, detail: Rational) -> tuple[Q, Q]:
        mean, detail = _q(mean), _q(detail)
        return mean + self.q * detail / self.mass, mean - self.p * detail / self.mass

    def multiplication_matrix(self, left_value: Rational, right_value: Rational):
        """T diag(left_value,right_value) T^-1 in the weighted Haar basis."""
        left, right = _q(left_value), _q(right_value)
        s, p, q, delta = self.mass, self.p, self.q, left - right
        return (
            ((p * left + q * right) / s, p * q * delta / (s * s)),
            (delta, (q * left + p * right) / s),
        )


def _weight_levels(weights: Sequence[Rational]) -> tuple[tuple[Q, ...], ...]:
    mass = _weights(weights)
    if len(mass) & (len(mass) - 1):
        raise ValueError("a dyadic number of leaves is required")
    levels = [mass]
    while len(mass) > 1:
        mass = tuple(mass[i] + mass[i + 1] for i in range(0, len(mass), 2))
        levels.append(mass)
    return tuple(levels)


def haar_coefficient_weights(weights: Sequence[Rational]) -> tuple[Q, ...]:
    """Root mass, then coarse-to-fine detail masses matching the stored order."""
    levels = _weight_levels(weights)
    result = [levels[-1][0]]
    for level in reversed(levels[:-1]):
        result.extend(level[i] * level[i + 1] / (level[i] + level[i + 1])
                      for i in range(0, len(level), 2))
    return tuple(result)


@dataclass(frozen=True)
class WeightedHaarPacket:
    leaf_weights: tuple[Q, ...]
    coefficients: tuple[Q, ...]

    def __post_init__(self) -> None:
        levels = _weight_levels(self.leaf_weights)
        coefficients = tuple(_q(c) for c in self.coefficients)
        if len(coefficients) != len(levels[0]):
            raise ValueError("all detail coefficients must be retained")
        object.__setattr__(self, "leaf_weights", levels[0])
        object.__setattr__(self, "coefficients", coefficients)

    @property
    def coefficient_weights(self) -> tuple[Q, ...]:
        return haar_coefficient_weights(self.leaf_weights)

    @property
    def energy(self) -> Q:
        return weighted_energy(self.coefficients, self.coefficient_weights)


def haar_analyze(values: Sequence[Rational], weights: Sequence[Rational]) -> WeightedHaarPacket:
    """Root mean followed by every detail, in coarse-to-fine level order."""
    levels = _weight_levels(weights)
    current = tuple(_q(x) for x in values)
    if len(current) != len(levels[0]):
        raise ValueError("one source weight per value is required")
    details = []
    for mass in levels[:-1]:
        means, level_details = [], []
        for i in range(0, len(current), 2):
            mean, detail = WeightedSplit(mass[i], mass[i + 1]).analyze(current[i], current[i + 1])
            means.append(mean)
            level_details.append(detail)
        details.append(tuple(level_details))
        current = tuple(means)
    coefficients = current + tuple(value for level in reversed(details) for value in level)
    return WeightedHaarPacket(levels[0], coefficients)


def haar_synthesize(packet: WeightedHaarPacket) -> tuple[Q, ...]:
    levels = _weight_levels(packet.leaf_weights)
    current = packet.coefficients[:1]
    position = 1
    for mass in reversed(levels[:-1]):
        details = packet.coefficients[position:position + len(current)]
        values = []
        for index, (mean, detail) in enumerate(zip(current, details)):
            values.extend(WeightedSplit(mass[2 * index], mass[2 * index + 1]).synthesize(mean, detail))
        position += len(current)
        current = tuple(values)
    return current


@dataclass(frozen=True)
class PolyphasePacket:
    radix: int
    prefix: int
    blocks: tuple[tuple[Q, ...], ...]


def polyphase_pack(values: Sequence[Rational], radix: int) -> PolyphasePacket:
    """Use SUCC's established one-based coordinates; retain horizon padding."""
    data = tuple(_q(x) for x in values)
    layout = tensor_unitary(len(data), radix)
    blocks = [[Q() for _ in range(radix)] for _ in range(layout.blocks)]
    for n, value in enumerate(data, start=1):
        m, r = polyphase_coords(n, radix)
        blocks[m - 1][r] = value
    return PolyphasePacket(radix, len(data), tuple(tuple(row) for row in blocks))


def polyphase_unpack(packet: PolyphasePacket) -> tuple[Q, ...]:
    layout = tensor_unitary(packet.prefix, packet.radix)
    if len(packet.blocks) != layout.blocks or any(len(row) != packet.radix for row in packet.blocks):
        raise ValueError("block dimensions disagree with the original finite horizon")
    blocks = tuple(tuple(_q(x) for x in row) for row in packet.blocks)
    if any(blocks[m - 1][r] for m, r in layout.unhit):
        raise ValueError("an unhit horizon slot has acquired an unsupported amplitude")
    return tuple(blocks[m - 1][r] for m, r in
                 (polyphase_coords(n, packet.radix) for n in range(1, packet.prefix + 1)))


def z2_wilson_weights(contrast: Rational) -> tuple[Q, Q]:
    """One-plaquette finite-group Wilson law on (+1,-1), t=tanh(beta).

    This exact compact finite-group analogue is not the nonabelian simple Lie
    gauge-group continuum theorem.  Its source probabilities are fully known.
    """
    contrast = _q(contrast)
    if not -1 < contrast < 1:
        raise ValueError("finite-coupling contrast must lie strictly between -1 and 1")
    return (1 + contrast) / 2, (1 - contrast) / 2
