"""Exact Fourier pin surfaces and carrier-relative certificates.

Classical finite Fourier analysis, Bernoulli kernels and discounted observability
applied to source-labelled SUCC. Probability laws are not individual states.
Paper theorems: research/2026-11-07/fourier_yoneda_pinbed/THEOREMS.md.
No floating approximation, physical attestation, or normality proof is supplied.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb
from typing import Sequence

from .carrier_relative_targets import (
    Carrier, CarrierError, Target, behavioral_partition, rational, resolve_target,
)
from .finite_fourier_carrier import CyclotomicElement, exact_dft
from .integer_bbp_carrier import IntegerState, source_states


def _integer(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise CarrierError(f"integer >= {minimum} required")
    return n


@dataclass(frozen=True)
class CircleLaw:
    """A realized rational probability law, with merged circle-equivalent atoms."""

    atoms: tuple[tuple[Q, Q], ...]

    def __post_init__(self):
        if type(self.atoms) is not tuple or not self.atoms:
            raise CarrierError("a nonempty tuple of exact atoms is required")
        merged: dict[Q, Q] = {}
        for atom in self.atoms:
            if type(atom) is not tuple or len(atom) != 2:
                raise CarrierError("each atom is (position, probability)")
            x, p = (rational(v) for v in atom)
            if p < 0:
                raise CarrierError("negative probability is not realizable")
            merged[x % 1] = merged.get(x % 1, Q(0)) + p
        if sum(merged.values(), Q(0)) != 1:
            raise CarrierError("probability mass must be exactly one")
        object.__setattr__(self, "atoms", tuple(sorted(
            (x, p) for x, p in merged.items() if p)))

    @classmethod
    def empirical(cls, points: Sequence[Q]) -> "CircleLaw":
        points = tuple(points)
        if not points:
            raise CarrierError("an empty sample is not a probability law")
        return cls(tuple((rational(x), Q(1, len(points))) for x in points))


def bernoulli2(x: Q) -> Q:
    t = rational(x) % 1
    return t*t - t + Q(1, 6)


def bernoulli4(x: Q) -> Q:
    t = rational(x) % 1
    return t**4 - 2*t**3 + t*t - Q(1, 30)


def pin_surface(law: CircleLaw, t: Q) -> Q:
    """Centered continuous pin height; raw nonnegative height is this + 1/12."""
    t = rational(t)
    return sum((p * bernoulli2(t-x) for x, p in law.atoms), Q(0))


def affine_push(law: CircleLaw, multiplier: int, offset: Q = Q(0)) -> CircleLaw:
    b, a = _integer(multiplier, 1), rational(offset)
    return CircleLaw(tuple(((b*x+a) % 1, p) for x, p in law.atoms))


def transported_pin(law: CircleLaw, multiplier: int, offset: Q, t: Q) -> Q:
    """Explicit L_(b,a)F(t)=b sum_j F((t-a+j)/b), not a refit to output."""
    b, a, t = _integer(multiplier, 1), rational(offset), rational(t)
    return b * sum((pin_surface(law, (t-a+j)/b) for j in range(b)), Q(0))


def surface_covariance(x: Q) -> Q:
    return -bernoulli4(x)/6


def surface_energy_pairs(law: CircleLaw) -> Q:
    """Exact O(n^2) spatial covariance oracle, including diagonal pairs."""
    return sum((p*q*surface_covariance(x-y)
                for x, p in law.atoms for y, q in law.atoms), Q(0))


def surface_energy(law: CircleLaw) -> Q:
    """Exact sorted weighted prefix-moment formula; O(n) arithmetic after sort.

    Fraction bit complexity can grow with the input denominators. CircleLaw has
    already sorted/merged atoms. This is not an O(n) bit-complexity claim.
    """
    moments = [Q(0)] * 5
    correction = Q(0)
    for x, p in law.atoms:
        def difference_power(k):
            return sum((Q(comb(k, j)) * (-1)**j * x**(k-j) * moments[j]
                        for j in range(k+1)), Q(0))
        correction += p * (difference_power(4) - 2*difference_power(3)
                           + difference_power(2))
        for j in range(5):
            moments[j] += p*x**j
    value = Q(1, 180) - correction/3
    if value < 0:
        raise AssertionError("exact Bernoulli energy cannot be negative")
    return value


def surface_distance_squared(left: CircleLaw, right: CircleLaw) -> Q:
    cross = sum((p*q*surface_covariance(x-y)
                 for x, p in left.atoms for y, q in right.atoms), Q(0))
    value = surface_energy(left) + surface_energy(right) - 2*cross
    if value < 0:
        raise AssertionError("exact pin distance cannot be negative")
    return value


def bbp_epoch(epoch: int) -> tuple[CircleLaw, tuple[IntegerState, ...]]:
    """Original source only: integer engine, literal zero, epoch [A,2A)."""
    a = _integer(epoch, 1)
    states = source_states(2*a-1)
    law = CircleLaw.empirical(tuple(Q(s.remainder, s.conductor)
                                   for s in states[a:2*a]))
    return law, states


def verify_bbp_trace(states: tuple[IntegerState, ...]) -> bool:
    """Bind a proposed finite receipt to original exact state values, not a name."""
    if type(states) is not tuple or not states:
        raise CarrierError("a nonempty full trace including U0 is required")
    if any(type(s) is not IntegerState for s in states):
        raise CarrierError("integer source states required")
    return states == source_states(len(states)-1)


def bbp_surface_norm_error_squared(epoch: int) -> Q:
    """Squared upper bound (1/(30 sqrt(3) A^2))^2 for completed-pi transport.

    Uses the PAPER all-n tail bound, never sampled pi digits. Bound does not
    assert the authentic surface itself tends to zero.
    """
    a = _integer(epoch, 1)
    return Q(1, 2700*a**4)


def completed_surface_translation_bound_squared(displacement: Q, multiplier: int,
                                                discount: Q, depth: int) -> Q:
    """Uniform bound for the discounted B2 bed; retains the exact future tail."""
    delta, rho = rational(displacement), rational(discount)
    b, jmax = _integer(multiplier, 2), _integer(depth)
    if not 0 <= delta <= 1 or not 0 < rho < 1:
        raise CarrierError("displacement in [0,1] and discount in (0,1) required")
    if delta == 0:
        return Q(0)
    return (delta**2/3 * sum(((rho*b*b)**j for j in range(jmax+1)), Q(0))
            + rho**(jmax+1)/(45*(1-rho)))


def finite_convolution(profile: Sequence[Q], law: Sequence[Q]) -> tuple[Q, ...]:
    k, p = tuple(map(rational, profile)), tuple(map(rational, law))
    if len(k) != len(p) or not 2 <= len(k) <= 100:
        raise CarrierError("same finite cyclic clock, length 2..100, required")
    if min(p) < 0 or sum(p) != 1:
        raise CarrierError("exact probability law required")
    m = len(k)
    return tuple(sum((p[x]*k[(t-x) % m] for x in range(m)), Q(0))
                 for t in range(m))


def finite_affine_push(law: Sequence[Q], multiplier: int,
                       offset: int = 0) -> tuple[Q, ...]:
    p = tuple(map(rational, law))
    b = _integer(multiplier, 1)
    if type(offset) is not int or not 2 <= len(p) <= 100:
        raise CarrierError("integral offset and finite cyclic clock required")
    if min(p) < 0 or sum(p) != 1:
        raise CarrierError("exact probability law required")
    out = [Q(0)]*len(p)
    for x, weight in enumerate(p):
        out[(b*x+offset) % len(p)] += weight
    return tuple(out)


def finite_pin_support(profile: Sequence[Q]) -> tuple[int, ...]:
    """Observable law moments; fixed probability mass supplies frequency zero."""
    spectrum = exact_dft(profile)
    zero = CyclotomicElement.scalar(len(spectrum), 0)
    return tuple(sorted({0} | {h for h, value in enumerate(spectrum) if value != zero}))


def law_support_closure(modulus: int, support: Sequence[int],
                        multipliers: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    """Least future-closed MOMENT support, without adding unjustified products."""
    m = _integer(modulus, 2)
    if m > 100:
        raise CarrierError("finite calibration modulus is at most 100")
    hs = tuple(support)
    bs = tuple(multipliers)
    if any(type(h) is not int for h in hs) or not bs:
        raise CarrierError("integer support and at least one action required")
    bs = tuple(_integer(b, 1) for b in bs)
    current = {0} | {h % m for h in hs} | {(-h) % m for h in hs}
    stages = [tuple(sorted(current))]
    while True:
        next_set = current | {(b*h) % m for b in bs for h in current}
        if next_set == current:
            return tuple(stages)
        current = next_set
        stages.append(tuple(sorted(current)))


@dataclass(frozen=True)
class FuturePinBed:
    """Finite-support base weights; exact evaluation of an INFINITE completion.

    w need not be characteristic. Completion adds future pullbacks, not unknown
    frequencies outside the generated rays. No future measurement is executed.
    """

    base: tuple[tuple[int, Q], ...]
    multiplier: int
    discount: Q

    def __post_init__(self):
        _integer(self.multiplier, 2)
        rho = rational(self.discount)
        if not 0 < rho < 1:
            raise CarrierError("discount must lie strictly between zero and one")
        if type(self.base) is not tuple or not self.base:
            raise CarrierError("a nonzero exact base weight family is required")
        weights = {}
        for pair in self.base:
            if type(pair) is not tuple or len(pair) != 2:
                raise CarrierError("each base entry is (integer frequency, exact weight)")
            h, weight = pair
            if type(h) is not int or h == 0 or h in weights:
                raise CarrierError("distinct nonzero integer frequencies required")
            weight = rational(weight)
            if weight <= 0:
                raise CarrierError("stored base weights must be positive")
            weights[h] = weight
        if any(weights.get(-h) != w for h, w in weights.items()):
            raise CarrierError("a real pin geometry needs symmetric weights")
        object.__setattr__(self, "base", tuple(sorted(weights.items())))
        object.__setattr__(self, "discount", rho)

    @property
    def total_base_weight(self) -> Q:
        return sum((w for _, w in self.base), Q(0))

    @property
    def total_completed_weight(self) -> Q:
        return self.total_base_weight/(1-self.discount)

    @property
    def squared_lipschitz_bound(self) -> Q:
        return 1/self.discount

    def weight(self, frequency: int, *, least_envelope: bool = False) -> Q:
        if type(frequency) is not int or frequency == 0:
            raise CarrierError("nonzero integer frequency required")
        weights = dict(self.base)
        h, factor, terms = frequency, Q(1), []
        while True:
            terms.append(factor*weights.get(h, Q(0)))
            if h % self.multiplier:
                break
            h //= self.multiplier
            factor *= self.discount
        return max(terms) if least_envelope else sum(terms, Q(0))

    def finite_weights(self, future_depth: int) -> tuple[tuple[int, Q], ...]:
        jmax = _integer(future_depth)
        result: dict[int, Q] = {}
        for h, w in self.base:
            for j in range(jmax+1):
                k = self.multiplier**j*h
                result[k] = result.get(k, Q(0)) + self.discount**j*w
        return tuple(sorted(result.items()))

    def squared_distance_tail(self, future_depth: int) -> Q:
        j = _integer(future_depth)
        return 4*self.total_base_weight*self.discount**(j+1)/(1-self.discount)


def relative_truth_certificate(carrier: Carrier, target: Target,
                               state: int) -> dict:
    """Prove TRUE_COMPATIBLE as its own statement on a completed behavior fiber.

    Reuses SUCC's all-finite-experiment partition and target resolver. This is
    not a claim that the observer has physically performed every experiment.
    """
    target.validate(carrier)
    if any(value not in (0, 1) for value in target.values):
        raise CarrierError("Boolean target required for truth certificate")
    if type(state) is not int or not 0 <= state < carrier.size:
        raise CarrierError("a realized state in the declared carrier is required")
    block = next(b for b in behavioral_partition(carrier) if state in b)
    resolution = resolve_target(carrier, target, block)
    yes = tuple(x for x in block if target.values[x] == 1)
    no = tuple(x for x in block if target.values[x] == 0)
    return {
        "source_fingerprint": carrier.fingerprint,
        "target_fingerprint": sha256(json.dumps((carrier.fingerprint, target.name,
            tuple(str(v) for v in target.values)), separators=(",", ":")).encode()).hexdigest(),
        "target": target.name,
        "fiber": block,
        "relative_truth": "TRUE_COMPATIBLE" if yes else "NO_TRUE_REPRESENTATIVE",
        "true_witness": yes[0] if yes else None,
        "false_witness": no[0] if no else None,
        "target_resolution": resolution.status,
        "invariant_truth": True if not no else False if not yes else None,
        "scope": "declared carrier, all finite lawful experiment words",
        "physical_source_attestation": False,
    }
