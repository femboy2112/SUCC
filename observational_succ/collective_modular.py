"""Exact collective observable algebras on one declared uniform cyclic carrier.

Rational matrix layer only; source authentication and operational access remain
with source_lambda/consensus_lambda. Paper proofs: COLLECTIVE_MODULAR_ALGEBRA.md.
The explicit clock budget is 100; this is not an implementation of all Zhat.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations
from math import gcd, lcm
from typing import Iterable

from .all_places_zeta import divisors, mobius, totient
from .classical_unit_origin import chart_multiplier, chart_successor
from .consensus_lambda import EDevice, LambdaPort, Portfolio, World, exact_portfolio
from .finite_fourier_carrier import CyclotomicElement
from .pontryagin_source_duality import FiniteCyclicCharacter
from .source_lambda import Read

Matrix = tuple[tuple[Q, ...], ...]
MAX_CLOCK = 100
MAX_MENUS = 12


class CollectiveModularError(ValueError):
    """Invalid exact carrier or exceeded explicit finite budget."""


def _integer(value: int) -> int:
    if type(value) is not int:
        raise CollectiveModularError("exact integer required")
    return value


def _clock(n: int) -> int:
    if not 1 <= _integer(n) <= MAX_CLOCK:
        raise CollectiveModularError("explicit clock must lie in 1..100")
    return n


def _divisor(n: int, d: int) -> int:
    _clock(n)
    if _integer(d) < 1 or n % d:
        raise CollectiveModularError("observation modulus must divide ambient clock")
    return d


def _menu(n: int, moduli: Iterable[int]) -> tuple[int, ...]:
    out = tuple(moduli)
    if not out or len(out) > MAX_MENUS:
        raise CollectiveModularError("declare 1..12 simultaneously accessible menus")
    return tuple(_divisor(n, m) for m in out)


def conditional_expectation(n: int, modulus: int) -> Matrix:
    """E_m[x,y] = m/n if x=y mod m, else zero; Haar mean, not sum."""
    m = _divisor(n, modulus)
    weight = Q(m, n)
    return tuple(tuple(weight if (x-y) % m == 0 else Q(0)
                       for y in range(n)) for x in range(n))


def conductor_projector(n: int, conductor: int) -> Matrix:
    """P_d = sum_(e|d) mu(d/e) E_e, with rational rank phi(d)."""
    d = _divisor(n, conductor)
    terms = tuple((mobius(d//e), conditional_expectation(n, e))
                  for e in divisors(d) if mobius(d//e))
    return tuple(tuple(sum((c*a[x][y] for c, a in terms), Q(0))
                       for y in range(n)) for x in range(n))


@dataclass(frozen=True)
class ConductorSector:
    conductor: int
    dimension: int
    visible_in: tuple[int, ...]
    minimum_joint_menus: int


@dataclass(frozen=True)
class CollectiveSectors:
    ambient: int
    moduli: tuple[int, ...]
    joint_modulus: int
    sectors: tuple[ConductorSector, ...]

    @property
    def linear_dimension(self) -> int:
        return sum(s.dimension for s in self.sectors if s.visible_in)

    @property
    def joint_dimension(self) -> int:
        return self.joint_modulus

    @property
    def missing_conductors(self) -> tuple[int, ...]:
        return tuple(s.conductor for s in self.sectors if not s.visible_in)

    @property
    def missing_dimension(self) -> int:
        return self.joint_dimension - self.linear_dimension


def collective_sectors(n: int, moduli: Iterable[int]) -> CollectiveSectors:
    """Classify joint vs linear sectors, including minimum interaction order.

    Each entry is one menu algebra A_m. For a menu containing several reads,
    first use its lcm. Repeated entries retain their indices but add no rank.
    Constants have order zero. Sectors outside A_lcm are not joint sectors.
    """
    ms = _menu(n, moduli)
    joint = lcm(*ms)
    # Enumeration is bounded by MAX_MENUS; it is not the portfolio solver.
    subjoins = tuple((k, lcm(*subset)) for k in range(len(ms)+1)
                     for subset in combinations(ms, k))
    sectors = tuple(ConductorSector(
        d, totient(d), tuple(i for i, m in enumerate(ms) if m % d == 0),
        next(k for k, j in subjoins if j % d == 0),
    ) for d in divisors(joint))
    return CollectiveSectors(n, ms, joint, sectors)


def _sector_sum(n: int, conductors: Iterable[int]) -> Matrix:
    terms = tuple(conductor_projector(n, d) for d in conductors)
    return tuple(tuple(sum((p[x][y] for p in terms), Q(0))
                       for y in range(n)) for x in range(n))


def linear_pool_projector(n: int, moduli: Iterable[int]) -> Matrix:
    """Orthogonal projector onto sum_i A_mi; generally not an algebra."""
    sectors = collective_sectors(n, moduli)
    return _sector_sum(n, (s.conductor for s in sectors.sectors if s.visible_in))


def missing_joint_projector(n: int, moduli: Iterable[int]) -> Matrix:
    """Project onto A_lcm orthogonal to the linear pool, not all its ambient loss."""
    return _sector_sum(n, collective_sectors(n, moduli).missing_conductors)


def compatible_crt_image(moduli: Iterable[int]) -> tuple[tuple[int, ...], ...]:
    """Actual simultaneous residue tuples in source order; no Cartesian fiction.

    No new CRT solver: enumerate the bounded common carrier. Report joining
    with passports remains the responsibility of source_lambda.Join.
    """
    ms = tuple(moduli)
    if not ms or len(ms) > MAX_MENUS:
        raise CollectiveModularError("declare 1..12 residue moduli")
    for m in ms:
        _clock(m)
    joint = _clock(lcm(*ms))
    return tuple(tuple(x % m for m in ms) for x in range(joint))


def conductor_six_basis() -> tuple[tuple[Q, ...], tuple[Q, ...]]:
    """Orthogonal rational basis of ker(E_2) intersect ker(E_3) in A_6."""
    return (tuple(map(Q, (2, 1, -1, -2, -1, 1))),
            tuple(map(Q, (0, 1, 1, 0, -1, -1))))


def affine_pullback(n: int, multiplier: int, offset: int) -> Matrix:
    """Koopman U_(a,b) f(x)=f(a*x+b); nonunits are allowed, never inverted."""
    _clock(n)
    a, b = _integer(multiplier), _integer(offset)
    return tuple(tuple(Q(y == (a*x+b) % n) for y in range(n)) for x in range(n))


def succ_pullback(n: int, step: int = 1, chart: str = "n_minus_one") -> Matrix:
    return affine_pullback(n, 1, chart_successor(0, step, chart))


def fucc_pullback(n: int, multiplier: int, chart: str = "n_minus_one") -> Matrix:
    """Reuse the source chart's affine FUCC law; composites are allowed words."""
    return affine_pullback(n, multiplier, chart_multiplier(0, multiplier, chart))


def affine_character(n: int, label: int, multiplier: int, offset: int
                     ) -> tuple[CyclotomicElement, FiniteCyclicCharacter]:
    """U chi_k = zeta_n^(k*b) chi_(a*k), in ONE exact cyclotomic field."""
    _clock(n)
    k, a, b = _integer(label), _integer(multiplier), _integer(offset)
    ch = FiniteCyclicCharacter(n, k)
    return ch.character_root(b), FiniteCyclicCharacter(n, a*k)


def affine_norm_squared(n: int, multiplier: int) -> int:
    """Exact Haar L2 operator norm squared, including constant maps (a=0)."""
    return gcd(_integer(multiplier), _clock(n))


def target_pair_cover(world: World, moduli: Iterable[int]
                      ) -> tuple[tuple[str, str, tuple[int, ...]], ...]:
    """Cross-target pairs and indices of raw modular reads separating them.

    This computes a model table; it does not perform observations. Empty cover
    rows witness impossibility with this menu (even allowing postprocessing).
    """
    if not isinstance(world, World):
        raise CollectiveModularError("source-indexed finite World required")
    ms = tuple(moduli)
    if len(ms) > MAX_MENUS:
        raise CollectiveModularError("at most 12 menu entries")
    for m in ms:
        _clock(m)
    return tuple((a.name, b.name, tuple(i for i, m in enumerate(ms)
                                     if (a.integer-b.integer) % m))
                 for a, b in combinations(world.candidates, 2) if a.target != b.target)


def minimum_target_portfolio(world: World, moduli: Iterable[int]) -> Portfolio:
    """Adapter to the existing exact solver: one jointly ready modular device.

    Minimize number of reads, with no costs, destructive actions, or scheduling.
    General E constraints must use consensus_lambda.exact_portfolio directly.
    """
    ms = tuple(moduli)
    target_pair_cover(world, ms)  # Validate before constructing ports.
    ports = tuple(LambdaPort(f"read-{i}-mod-{m}", Read(m))
                  for i, m in enumerate(ms) if m > 1)
    devices = () if not ports else (EDevice(
        "collective-modular", world.passport, ("ready",), "ready", ports,
        {"ready": tuple(p.name for p in ports)}, {},
    ),)
    return exact_portfolio(world, devices, radius=0, max_programs=MAX_MENUS)


@dataclass(frozen=True)
class BoundedCylinder:
    """One rational bounded cylinder on Zhat, represented by its residue values.

    This is an algebraic model, not source evidence or an infinite-point oracle.
    Every cylinder is bounded; no uniform bound on all cylinder functions is
    imposed. The computational modulus cap is distinct from either statement.
    """
    values: tuple[Q, ...]

    def __post_init__(self) -> None:
        if type(self.values) is not tuple:
            raise CollectiveModularError("immutable exact cylinder values required")
        _clock(len(self.values))
        if any(type(x) not in (int, Q) for x in self.values):
            raise CollectiveModularError("only int/Fraction cylinder values allowed")
        object.__setattr__(self, "values", tuple(map(Q, self.values)))

    @property
    def modulus(self) -> int:
        return len(self.values)

    @property
    def sup_norm(self) -> Q:
        return max(map(abs, self.values))

    def refine(self, modulus: int) -> BoundedCylinder:
        _divisor(modulus, self.modulus)
        return BoundedCylinder(tuple(self.values[x % self.modulus]
                                     for x in range(modulus)))

    def add(self, other: BoundedCylinder) -> BoundedCylinder:
        if not isinstance(other, BoundedCylinder):
            raise CollectiveModularError("another bounded cylinder required")
        n = _clock(lcm(self.modulus, other.modulus))
        return BoundedCylinder(tuple(self.values[x % self.modulus]
                                     + other.values[x % other.modulus] for x in range(n)))

    def multiply(self, other: BoundedCylinder) -> BoundedCylinder:
        if not isinstance(other, BoundedCylinder):
            raise CollectiveModularError("another bounded cylinder required")
        n = _clock(lcm(self.modulus, other.modulus))
        return BoundedCylinder(tuple(self.values[x % self.modulus]
                                     * other.values[x % other.modulus] for x in range(n)))
