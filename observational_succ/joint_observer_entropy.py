"""Exact joint-observer collision and trimmed-entropy instruments.

All arithmetic in this module is rational.  Logarithmic inequalities are
returned as exact symbolic terms, never as floating-point certificates.
The paper bridge keeps the original consecutive N-window when it passes
from retained d-blocks to short-block frequencies.  Arbitrary retained
subsets are not silently treated as stationary samples.

Proofs and boundaries: research/2026-10-24/PI_TRIMMED_JOINT_ENTROPY.md.
No finite output certifies an asymptotic BBP estimate or pi normality.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as Q
from math import isqrt
from typing import Mapping, Sequence


def _integer(value, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"strict integer >= {minimum} required")
    return value


def _rational(value):
    if type(value) not in (int, Q):
        raise ValueError("exact integer or Fraction required")
    return Q(value)


@dataclass(frozen=True)
class WordLaw:
    """A probability on a finite b-symbol, fixed-depth word space."""

    base: int
    depth: int
    atoms: tuple[tuple[tuple[int, ...], Q], ...]

    def __post_init__(self):
        _integer(self.base, 2)
        _integer(self.depth)
        if type(self.atoms) not in (tuple, list) or not self.atoms:
            raise ValueError("nonempty (word,mass) atom sequence required")
        masses = defaultdict(Q)
        for atom in self.atoms:
            if type(atom) not in (tuple, list) or len(atom) != 2:
                raise ValueError("each atom must be a (word,mass) pair")
            word, mass = atom
            if type(word) not in (tuple, list) or len(word) != self.depth:
                raise ValueError("word length must equal the declared depth")
            if any(type(a) is not int or not 0 <= a < self.base for a in word):
                raise ValueError("word symbols must be strict base-b digits")
            mass = _rational(mass)
            if mass < 0:
                raise ValueError("nonnegative probability masses required")
            masses[tuple(word)] += mass
        if sum(masses.values(), Q()) != 1:
            raise ValueError("probability masses must sum exactly to one")
        object.__setattr__(self, "atoms", tuple(sorted(
            (word, mass) for word, mass in masses.items() if mass)))

    def prefix(self, depth: int) -> "WordLaw":
        _integer(depth)
        if depth > self.depth:
            raise ValueError("prefix depth exceeds the word depth")
        return WordLaw(self.base, depth, tuple(
            (word[:depth], mass) for word, mass in self.atoms))

    @property
    def collision(self) -> Q:
        """b^d sum_w P(w)^2, including diagonal self-pairs."""
        return self.base**self.depth * sum(
            (mass*mass for _, mass in self.atoms), Q())


def _compatible(actual, reference=None):
    if type(actual) is not WordLaw:
        raise ValueError("validated WordLaw required")
    if reference is not None:
        if type(reference) is not WordLaw or (
                reference.base, reference.depth) != (actual.base, actual.depth):
            raise ValueError("reference must use the same word space")
        reference_mass = dict(reference.atoms)
        if any(not reference_mass.get(word, Q()) for word, _ in actual.atoms):
            raise ValueError("actual law must be absolutely continuous in reference")


def relative_second_moment(actual: WordLaw, reference: WordLaw) -> Q:
    """sum P^2/R, equal to one plus chi-square divergence."""
    _compatible(actual, reference)
    ref = dict(reference.atoms)
    return sum((mass*mass/ref[word] for word, mass in actual.atoms), Q())


@dataclass(frozen=True)
class ConditionalCollisionStep:
    prefix_depth: int
    second_moment: Q
    next_second_moment: Q
    ratio: Q
    escort_conditional_excess: Q


def conditional_collision_chain(actual: WordLaw,
                                reference: WordLaw | None = None
                                ) -> tuple[ConditionalCollisionStep, ...]:
    """Exact escort-conditioned product, allowing correlated references.

    With no reference, R is uniform on the whole declared word space;
    it is not a product approximation to the actual marginal laws.
    A supplied reference retains its own conditional probabilities.
    """
    _compatible(actual, reference)
    result = []
    for k in range(actual.depth):
        p = dict(actual.prefix(k).atoms)
        pn = dict(actual.prefix(k+1).atoms)
        if reference is None:
            r = {v: Q(1, actual.base**k) for v in p}
            rn = {w: Q(1, actual.base**(k+1)) for w in pn}
        else:
            r = dict(reference.prefix(k).atoms)
            rn = dict(reference.prefix(k+1).atoms)
        moment = sum((mass*mass/r[v] for v, mass in p.items()), Q())
        next_moment = sum((mass*mass/rn[w] for w, mass in pn.items()), Q())
        conditional_ratio = Q()
        for v, mass in p.items():
            escort = mass*mass/(r[v]*moment)
            local = sum((child*child*r[v]/(mass*mass*rn[w])
                         for w, child in pn.items() if w[:-1] == v), Q())
            conditional_ratio += escort*local
        ratio = next_moment/moment
        if ratio != conditional_ratio or ratio < 1:
            raise AssertionError("conditional second-moment identity failed")
        result.append(ConditionalCollisionStep(
            k, moment, next_moment, ratio, conditional_ratio-1))
    return tuple(result)


@dataclass(frozen=True)
class CollisionDataProcessing:
    before: Q
    after: Q
    actual_image: tuple[tuple[int, Q], ...]
    reference_image: tuple[tuple[int, Q], ...]


def collision_data_processing(actual: WordLaw, reference: WordLaw,
                              decoder: Mapping[tuple[int, ...], int]
                              ) -> CollisionDataProcessing:
    """Push both laws through the same authenticated finite decoder."""
    _compatible(actual, reference)
    p_image, r_image = defaultdict(Q), defaultdict(Q)
    for word, mass in reference.atoms:
        if word not in decoder:
            raise ValueError("decoder must cover reference support")
        label = decoder[word]
        _integer(label)
        r_image[label] += mass
    for word, mass in actual.atoms:
        p_image[decoder[word]] += mass
    before = relative_second_moment(actual, reference)
    after = sum((mass*mass/r_image[label]
                 for label, mass in p_image.items()), Q())
    if after > before:
        raise AssertionError("chi-square data processing failed")
    return CollisionDataProcessing(before, after, tuple(sorted(p_image.items())),
                                   tuple(sorted(r_image.items())))


def empirical_block_law(word: Sequence[int], starts: Sequence[int],
                        depth: int, base: int) -> WordLaw:
    """Actual overlapping blocks; callers must supply their future digits."""
    _integer(base, 2)
    _integer(depth, 1)
    if type(word) not in (tuple, list) or not word:
        raise ValueError("nonempty finite digit sequence required")
    if any(type(a) is not int or not 0 <= a < base for a in word):
        raise ValueError("strict base-b digits required")
    if type(starts) not in (tuple, list, range) or not starts:
        raise ValueError("nonempty starting-position sequence required")
    for start in starts:
        _integer(start)
        if start+depth > len(word):
            raise ValueError("missing actual future digits for a sampled block")
    return WordLaw(base, depth, tuple(
        (tuple(word[start:start+depth]), Q(1, len(starts))) for start in starts))


@dataclass(frozen=True)
class TrimmedEntropyBudget:
    """An exact symbolic upper bound on original-window short-block KL.

    ``log_terms`` encodes sum coefficient*log(argument) in natural logs.
    It is a paper-justified bound, not a floating logarithm certificate.
    """

    base: int
    horizon: int
    depth: int
    block_length: int
    retained_count: int
    discarded_mass: Q
    retained_collision: Q
    chunks: int
    continuity_delta: Q
    log_terms: tuple[tuple[Q, Q], ...]
    original_short_law: WordLaw


def trimmed_entropy_budget(word: Sequence[int], horizon: int, depth: int,
                           block_length: int, retained: Sequence[int],
                           base: int = 16) -> TrimmedEntropyBudget:
    """Bound using an arbitrary retained subset of the ORIGINAL N-window.

    The original short-block law is always sampled at every start 0..N-1.
    Offset stationarity is used only for that full window in the proof.
    """
    _integer(horizon, 1)
    _integer(depth, 1)
    _integer(block_length, 1)
    if block_length > depth or 2*depth > horizon:
        raise ValueError("requires 1 <= k <= d <= N/2")
    if type(retained) not in (tuple, list, range) or not retained:
        raise ValueError("nonempty retained-index sequence required")
    if any(type(n) is not int or not 0 <= n < horizon for n in retained):
        raise ValueError("retained indices must lie in the original N-window")
    if len(set(retained)) != len(retained):
        raise ValueError("retained positions must be distinct")
    # Full-depth evaluation validates all actual future digits, including
    # those not used by the retained sample.
    empirical_block_law(word, range(horizon), depth, base)
    good = empirical_block_law(word, retained, depth, base)
    short = empirical_block_law(word, range(horizon), block_length, base)
    delta = 1-Q(len(retained), horizon)
    t = Q(depth, horizon)
    chunks = depth//block_length
    terms = [(delta*depth/chunks, Q(base)),
             ((1-delta)/chunks, good.collision),
             (-t, t), (-(1-t), 1-t),
             (t, Q(base**block_length-1))]
    return TrimmedEntropyBudget(
        base, horizon, depth, block_length, len(retained), delta,
        good.collision, chunks, t,
        tuple((coefficient, argument) for coefficient, argument in terms
              if coefficient and argument != 1), short)


@dataclass(frozen=True)
class OneCellCollisionTransport:
    cells: int
    before: Q
    after: Q
    source_cell_masses: tuple[tuple[int, Q], ...]
    target_cell_masses: tuple[tuple[int, Q], ...]
    staying_masses: tuple[tuple[int, Q], ...]
    advancing_masses: tuple[tuple[int, Q], ...]


def one_cell_collision_transport(phases: Sequence[Q | int],
                                 forward_shifts: Sequence[Q | int],
                                 cells: int,
                                 weights: Sequence[Q | int] | None = None
                                 ) -> OneCellCollisionTransport:
    """Certify factor-two transport under exact shifts in [0,1/cells)."""
    _integer(cells, 1)
    if (type(phases) not in (tuple, list) or not phases or
            type(forward_shifts) not in (tuple, list) or
            len(phases) != len(forward_shifts)):
        raise ValueError("equal nonempty phase and shift sequences required")
    if weights is None:
        weights = (Q(1, len(phases)),)*len(phases)
    if type(weights) not in (tuple, list) or len(weights) != len(phases):
        raise ValueError("one exact probability weight per phase required")
    masses = tuple(_rational(w) for w in weights)
    if any(w < 0 for w in masses) or sum(masses, Q()) != 1:
        raise ValueError("nonnegative weights summing exactly to one required")
    before, after, stay, advance = (defaultdict(Q) for _ in range(4))
    for point, shift, mass in zip(phases, forward_shifts, masses):
        point, shift = _rational(point) % 1, _rational(shift)
        if not 0 <= shift < Q(1, cells):
            raise ValueError("forward displacement must be less than one cell")
        j = int(cells*point)
        unwrapped = int(cells*(point+shift))
        if unwrapped not in (j, j+1):
            raise AssertionError("one-cell displacement lost its literal lift")
        before[j] += mass
        after[unwrapped % cells] += mass
        (stay if unwrapped == j else advance)[j] += mass
    for j in set(before) | set(after) | set(stay) | set(advance):
        if before[j] != stay[j]+advance[j]:
            raise AssertionError("source split lost probability mass")
        if after[j] != stay[j]+advance[(j-1) % cells]:
            raise AssertionError("target split lost cyclic carry")
    c_before = cells*sum((v*v for v in before.values()), Q())
    c_after = cells*sum((v*v for v in after.values()), Q())
    if c_after > 2*c_before or c_before > 2*c_after:
        raise AssertionError("one-cell collision transport violated factor two")
    return OneCellCollisionTransport(
        cells, c_before, c_after,
        tuple(sorted((j,v) for j,v in before.items() if v)),
        tuple(sorted((j,v) for j,v in after.items() if v)),
        tuple(sorted((j,v) for j,v in stay.items() if v)),
        tuple(sorted((j,v) for j,v in advance.items() if v)))


def bbp_safe_start(depth: int) -> int:
    """Least n>=0 with (8n+1)(8n+2)>=16^depth, using integers only."""
    _integer(depth)
    cells = 16**depth
    n = max(0, (isqrt(1+4*cells)-3)//16)
    while (8*n+1)*(8*n+2) < cells:
        n += 1
    if n and (8*(n-1)+1)*(8*(n-1)+2) >= cells:
        raise AssertionError("integer BBP cutoff is not minimal")
    return n


def bbp_safe_retained_indices(start: int, horizon: int, depth: int) -> tuple[int, ...]:
    """Positions in an authentic n-window whose Green tails are subcell."""
    _integer(start)
    _integer(horizon, 1)
    cutoff = max(0, bbp_safe_start(depth)-start)
    return tuple(range(min(cutoff, horizon), horizon))
