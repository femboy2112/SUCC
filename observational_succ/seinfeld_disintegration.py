"""Exact source-labelled null residuals and rational 16-branch resolution.

Classical finite disintegration splits a law into its pushforward and a
fibre-null signed residual. Keeping that residual permits reconstruction;
its evaluated zero does not. The rational branch residual has dimension
15, resolved by Q(zeta16), Q(zeta8), Q(i), and Q at modes 1, 2, 4, and 8.
These are FOUR FIELD ELEMENTS, not four rational coordinates.

General rational observation/annihilator recovery is inherited from
shadow_source_inference. Odd inverse uniqueness is inherited from
selected_branch_operator. The authentic wrapper imports the original
four-pole recurrence and zero-seed verifier without changing either.

This finite interface supplies no selected-Weyl decay or pi normality.
Source labels in a generic law are metadata; only authentic_branch_law
performs the original-source authentication.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd

from .beck_chevalley_source import FiniteMap, finite_map
from .lambda_source_duality import (
    Cyclo16, branch_fourier, exact_int, fraction, witness_selected_branches,
)
from .seinfeld_succ import ZeroWitness
from .selected_branch_operator import exact_odd_inverse


class DisintegrationError(ValueError):
    """Missing labels, incompatible exact data, or an illegal source claim."""


def _vector(values, size):
    if type(values) not in (tuple, list) or len(values) != size:
        raise DisintegrationError("one exact rational value per declared atom required")
    return tuple(fraction(x) for x in values)


def _fibres(projection):
    if not isinstance(projection, FiniteMap) or not projection.domain:
        raise DisintegrationError("a nonempty native finite map is required")
    lookup = {y: [] for y in projection.codomain}
    for i, (_, y) in enumerate(projection.pairs):
        lookup[y].append(i)
    return tuple(tuple(lookup[y]) for y in projection.codomain)


@dataclass(frozen=True)
class ObservableSplit:
    total: Q
    uniform_lift: Q
    null_pairing: Q


@dataclass(frozen=True)
class FiberDisintegration:
    """A probability law as pushforward plus a labelled zero-sum residual.

    Uniform lifting is a declared reference section of pushforward, not an
    inference that the original conditional distribution was uniform.
    Codomain points with empty fibres must have marginal mass zero.
    """
    projection: FiniteMap
    source_id: str
    marginal: tuple[Q, ...]
    residual: tuple[Q, ...]

    def __post_init__(self):
        fibres = _fibres(self.projection)
        if type(self.source_id) is not str or not self.source_id:
            raise DisintegrationError("an explicit nonempty source label is required")
        m = _vector(self.marginal, len(fibres))
        z = _vector(self.residual, len(self.projection.domain))
        object.__setattr__(self, "marginal", m)
        object.__setattr__(self, "residual", z)
        if any(x < 0 for x in m) or sum(m) != 1:
            raise DisintegrationError("pushforward must be a probability law")
        for mass, indices in zip(m, fibres):
            if (not indices and mass) or sum((z[i] for i in indices), Q()):
                raise DisintegrationError("residual must vanish in every labelled fibre")
        if any(x < 0 for x in self.reconstruct()):
            raise DisintegrationError("lift plus residual is not a probability law")

    @property
    def null_dimension(self):
        """Dimension over Q, independent of positivity/boundary restrictions."""
        return len(self.projection.domain) - sum(bool(f) for f in _fibres(self.projection))

    @property
    def generator_labels(self):
        """Stable labels associated, in order, with projection.domain."""
        return tuple(f"{self.source_id}:atom:{i}" for i in range(len(self.residual)))

    def uniform_lift(self):
        result = [Q()] * len(self.residual)
        for mass, indices in zip(self.marginal, _fibres(self.projection)):
            for i in indices:
                result[i] = mass / len(indices)
        return tuple(result)

    def reconstruct(self):
        return tuple(u + z for u, z in zip(self.uniform_lift(), self.residual))

    def null_witness(self):
        """Formal provenance survives although every fibre evaluation is zero.

        To evaluate a pullback g after projection, assign atom i the value
        g(projection(domain[i])). This witness then evaluates to zero for
        EVERY rational g; a non-fibre-constant assignment need not vanish.
        """
        return ZeroWitness(f"fibre-null:{self.source_id}",
                           tuple(zip(self.generator_labels, self.residual)))

    def observable(self, values):
        f = _vector(values, len(self.residual))
        uniform = sum((u * x for u, x in zip(self.uniform_lift(), f)), Q())
        null = sum((z * x for z, x in zip(self.residual, f)), Q())
        total = sum((p * x for p, x in zip(self.reconstruct(), f)), Q())
        if total != uniform + null:
            raise ArithmeticError("signed source reconstruction failed")
        return ObservableSplit(total, uniform, null)


def disintegrate_law(projection, weights, *, source_id):
    """Exact disintegration, retaining the full joint source labels."""
    fibres = _fibres(projection)
    p = _vector(weights, len(projection.domain))
    if any(x < 0 for x in p) or sum(p) != 1:
        raise DisintegrationError("a nonnegative rational law of mass one is required")
    m = tuple(sum((p[i] for i in indices), Q()) for indices in fibres)
    z = list(p)
    for mass, indices in zip(m, fibres):
        for i in indices:
            z[i] -= mass / len(indices)
    return FiberDisintegration(projection, source_id, m, tuple(z))


@dataclass(frozen=True)
class MarginalAlias:
    """Two probability laws with identical pushforward and different outputs."""
    left: tuple[Q, ...]
    right: tuple[Q, ...]
    left_expectation: Q
    right_expectation: Q


def marginal_obstruction(projection, values):
    """Return a Dirac-pair receipt, or None exactly for fibre-constant values.

    The expectation of f is recoverable from pushforward for EVERY law iff
    f is constant on each fibre. This is the finite special case of the
    existing shadow-source annihilator theorem, not a new general theorem.
    """
    fibres = _fibres(projection)
    f = _vector(values, len(projection.domain))
    for indices in fibres:
        if not indices:
            continue
        i = indices[0]
        for j in indices[1:]:
            if f[i] != f[j]:
                left = tuple(Q(int(k == i)) for k in range(len(f)))
                right = tuple(Q(int(k == j)) for k in range(len(f)))
                return MarginalAlias(left, right, f[i], f[j])
    return None


DYADIC_MODES = (1, 2, 4, 8)
DYADIC_COORDINATES = (tuple(range(8)), (0, 2, 4, 6), (0, 4), (0,))


@dataclass(frozen=True)
class DyadicFourier:
    """Lossless Q-linear codec for a signed rational row of sixteen weights.

    mass plus 15 rational coordinates are necessary and sufficient for
    arbitrary rows. For probability rows mass=1 is already known. No
    minimality claim is made for nonlinear encodings or restricted laws.
    """
    mass: Q
    channels: tuple[Cyclo16, ...]

    def __post_init__(self):
        object.__setattr__(self, "mass", fraction(self.mass))
        if type(self.channels) is not tuple or len(self.channels) != 4:
            raise DisintegrationError("four typed dyadic field channels are required")
        for value, allowed in zip(self.channels, DYADIC_COORDINATES):
            if not isinstance(value, Cyclo16):
                raise DisintegrationError("evaluated Q(zeta16) field elements are required")
            if any(c and i not in allowed for i, c in enumerate(value.coefficients)):
                raise DisintegrationError("channel lies outside its declared dyadic subfield")

    @classmethod
    def from_weights(cls, weights):
        w = _vector(weights, 16)
        return cls(sum(w, Q()), tuple(branch_fourier(w, h) for h in DYADIC_MODES))

    @classmethod
    def from_coordinates(cls, mass, coordinates):
        packed = _vector(coordinates, 15)
        cursor, channels = 0, []
        for allowed in DYADIC_COORDINATES:
            field = [Q()] * 8
            for i in allowed:
                field[i] = packed[cursor]
                cursor += 1
            channels.append(Cyclo16(tuple(field)))
        return cls(fraction(mass), tuple(channels))

    @property
    def coordinates(self):
        return tuple(v.coefficients[i] for v, indices in
                     zip(self.channels, DYADIC_COORDINATES) for i in indices)

    def reconstruct(self):
        """Successive antipodal splits; no floating Fourier inversion."""
        folded = (self.mass,)
        for value, indices in reversed(tuple(zip(self.channels, DYADIC_COORDINATES))):
            differences = tuple(value.coefficients[i] for i in indices)
            if len(folded) != len(differences):
                raise ArithmeticError("dyadic source dimensions are inconsistent")
            folded = (tuple((s + d) / 2 for s, d in zip(folded, differences)) +
                      tuple((s - d) / 2 for s, d in zip(folded, differences)))
        return folded

    def character(self, frequency):
        """Every Fourier mode from its one Galois stratum, with sign intact."""
        exact_int(frequency, "branch character frequency")
        h = frequency % 16
        if h == 0:
            return Cyclo16.one() * self.mass
        base = h & -h
        channel = self.channels[DYADIC_MODES.index(base)]
        odd = h // base
        out = Cyclo16.zero()
        for i, coefficient in enumerate(channel.coefficients):
            out += Cyclo16.zeta(odd * i) * coefficient
        return out

    def stratum_energies(self):
        """Trace sums, not replacements for the signed Fourier channels."""
        energies = []
        for base in DYADIC_MODES:
            value = Cyclo16.zero()
            for h in range(base, 16, 2 * base):
                f = self.character(h)
                value += f * f.conjugate()
            if any(value.coefficients[1:]):
                raise ArithmeticError("Galois trace did not return a rational")
            energies.append(value.coefficients[0])
        return tuple(energies)


def branch_law(labels, rows, *, source_id):
    """Joint law on (source label, branch); row masses need not be equal."""
    if type(labels) is not tuple or not labels or len(set(labels)) != len(labels):
        raise DisintegrationError("distinct nonempty finite source labels are required")
    if type(rows) not in (tuple, list) or len(rows) != len(labels):
        raise DisintegrationError("one complete branch row per source label is required")
    checked = tuple(_vector(row, 16) for row in rows)
    atoms = tuple((s, j) for s in labels for j in range(16))
    mapping = finite_map(atoms, labels, lambda atom: atom[0])
    return disintegrate_law(mapping, tuple(x for row in checked for x in row),
                           source_id=source_id)


def branch_channels(law):
    """Keep each source label attached to its complete Fourier packet."""
    if not isinstance(law, FiberDisintegration):
        raise DisintegrationError("a labelled branch disintegration is required")
    labels = law.projection.codomain
    expected = tuple((s, j) for s in labels for j in range(16))
    if law.projection.domain != expected or any(y != s for (s, _), y in law.projection.pairs):
        raise DisintegrationError("the map must be the declared source/branch projection")
    p = law.reconstruct()
    return tuple((s, DyadicFourier.from_weights(p[16*i:16*(i+1)]))
                 for i, s in enumerate(labels))


def labelled_character_pairing(law, frequency, source_weights):
    """Sum_s a_s F_s(h), retaining rational signed source correlations.

    This is a branch-character observable. The real BBP character also has
    the source-dependent tail phase, which must be retained separately;
    this function does not identify the two observables.
    """
    packets = branch_channels(law)
    a = _vector(source_weights, len(packets))
    result = Cyclo16.zero()
    for coefficient, (_, packet) in zip(a, packets):
        result += packet.character(frequency) * coefficient
    return result


@dataclass(frozen=True)
class OddSelectorTag:
    digit: int
    character_order: int
    numerator_residue: int
    conductor_residue: int
    character_residue: int


def odd_selector_tag(tail, frequency=1, *, conductor=None):
    """Inherited odd inverse expressed as the minimal deterministic mode tag.

    If t=a/q and q is odd, j=-a*q^(-1) mod16. For mode h only
    j mod d is required, d=16/gcd(16,h). Every such residue is needed
    to distinguish all deterministic selectors at that mode. This does
    not assert that all residues occur in any authentic finite prefix.
    An odd enlargement of the conductor leaves the tag unchanged.
    """
    inverse = exact_odd_inverse(tail)
    exact_int(frequency, "branch character frequency")
    q = inverse.tail.denominator if conductor is None else conductor
    exact_int(q, "odd source conductor", 1)
    a = q * inverse.tail
    if q % 2 == 0 or a.denominator != 1:
        raise DisintegrationError("odd conductor must contain the exact tail denominator")
    order = 16 // gcd(16, frequency)
    residue = (-a.numerator * pow(q, -1, order)) % order
    if residue != inverse.digit % order:
        raise ArithmeticError("source denominator enlargement changed the selected character")
    return OddSelectorTag(inverse.digit, order, a.numerator % order,
                          q % order, residue)


def authentic_branch_law(states):
    """Authenticate U0=0, all original four poles, and each tagged transition.

    The source labels are the existing immutable BranchWitness records,
    including time, forcing, current/successor, literal carry and conductor.
    The induced law samples those finite source times uniformly; it is not
    an asserted stochastic generation mechanism for the original orbit.
    """
    witnesses = witness_selected_branches(states)
    if not witnesses:
        raise DisintegrationError("at least two authentic positive-time states are required")
    mass = Q(1, len(witnesses))
    rows = []
    for w in witnesses:
        tag = odd_selector_tag(w.remainder, conductor=w.conductor)
        if tag.digit != w.digit or (tag.digit + w.remainder) / 16 != w.current:
            raise ArithmeticError("authentic odd selected support failed")
        rows.append(tuple(mass if j == w.digit else Q() for j in range(16)))
    return branch_law(witnesses, tuple(rows), source_id="original-four-pole-zero-seed")

def status_flags():
    return {"finite_labelled_reconstruction": True,
            "rational_null_coordinates_per_branch_fibre": 15,
            "averaging_alone_invertible": False,
            "selected_weyl_saving_proved": False,
            "pi_base16_normality_proved": False}
