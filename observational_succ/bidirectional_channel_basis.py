"""Exact, source-agnostic two-root observer and graded typed channel adapter.

Terms, hyperedges and Walsh coefficients model finite independent observation
channels. All integers/rational coefficients are exact; neither a Hilbert
completion nor signed pi normality is deduced from these finite models.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import prod
from typing import Mapping, Sequence


@dataclass(frozen=True)
class Unit:
    """Free abelian dimension group, e.g. length^1 time^-2; dimensionless=()."""
    powers: tuple[tuple[str, int], ...] = ()

    def __post_init__(self) -> None:
        d: dict[str, int] = {}
        for name, degree in self.powers:
            if not isinstance(name, str) or not name or type(degree) is not int:
                raise ValueError("unit labels must be strings and degrees integers")
            d[name] = d.get(name, 0) + degree
        object.__setattr__(self, "powers", tuple(sorted((k, v) for k, v in d.items() if v)))

    @staticmethod
    def generator(label: str) -> Unit:
        return Unit(((label, 1),))

    def __mul__(self, other: Unit) -> Unit:
        if not isinstance(other, Unit):
            return NotImplemented
        return Unit(self.powers + other.powers)

    def __pow__(self, n: int) -> Unit:
        if type(n) is not int:
            raise TypeError("unit exponent must be integral")
        return Unit(tuple((k, n * v) for k, v in self.powers))

    def __truediv__(self, other: Unit) -> Unit:
        return self * (other ** -1)


@dataclass(frozen=True)
class Quantity:
    coefficient: Fraction
    unit: Unit = Unit()

    def __post_init__(self) -> None:
        object.__setattr__(self, "coefficient", Fraction(self.coefficient))
        if not isinstance(self.unit, Unit):
            raise TypeError("quantity.unit must be Unit")

    def __add__(self, other: Quantity) -> Quantity:
        if self.unit != other.unit:
            raise TypeError("cannot add quantities with different unit types")
        return Quantity(self.coefficient + other.coefficient, self.unit)

    def __neg__(self) -> Quantity:
        return Quantity(-self.coefficient, self.unit)

    def __sub__(self, other: Quantity) -> Quantity:
        return self + -other

    def __mul__(self, other: Quantity) -> Quantity:
        if not isinstance(other, Quantity):
            return NotImplemented
        return Quantity(self.coefficient * other.coefficient, self.unit * other.unit)


@dataclass(frozen=True)
class Channel:
    """Independent channel is a hypothesis to test, not inferred from count.

    Complexity grade has (interaction arity, path depth, resource cost) only
    as declared metadata. Never equate it with Kolmogorov/proof complexity.
    """
    name: str
    unit: Unit
    grade: tuple[int, int, int] = (1, 0, 0)

    def __post_init__(self) -> None:
        if not self.name or not isinstance(self.name, str):
            raise ValueError("a channel needs a nonempty name")
        if not isinstance(self.unit, Unit):
            raise TypeError("channel unit must be typed")
        if (len(self.grade) != 3 or
                any(type(v) is not int or v < 0 for v in self.grade)):
            raise ValueError("complexity grades must be nonnegative integer triples")


@dataclass(frozen=True)
class HyperCoupling:
    """A typed multilinear map from input channels to an output channel.

    For values x_i in units U_i and output in U_o, gain must have unit
    U_o / product_i U_i; arity can exceed 2, retaining higher-order defects.
    """
    inputs: tuple[str, ...]
    output: str
    gain: Quantity

    def evaluate(self, channels: Mapping[str, Channel], values: Mapping[str, Quantity]) -> Quantity:
        if not self.inputs or len(set(self.inputs)) != len(self.inputs):
            raise ValueError("independent labelled input channels required")
        if self.output not in channels or any(name not in channels for name in self.inputs):
            raise KeyError("coupling references an unknown channel")
        source_unit = Unit()
        value = self.gain
        for name in self.inputs:
            if name not in values or values[name].unit != channels[name].unit:
                raise TypeError("input values must carry their channel's unit")
            source_unit = source_unit * channels[name].unit
            value = value * values[name]
        if self.gain.unit != channels[self.output].unit / source_unit:
            raise TypeError("coupling gain has wrong domain-to-codomain unit")
        assert value.unit == channels[self.output].unit
        return value


def observation_rank(rows: Sequence[Sequence[Fraction | int]]) -> int:
    """Exact rank over Q; a test of linear channel independence *of these rows*."""
    if not rows:
        return 0
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("observation rows must be rectangular")
    a = [[Fraction(x) for x in row] for row in rows]
    pivot_row = 0
    for col in range(width):
        candidate = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if candidate is None:
            continue
        a[pivot_row], a[candidate] = a[candidate], a[pivot_row]
        pivot = a[pivot_row][col]
        for j in range(col, width):
            a[pivot_row][j] /= pivot
        for i in range(len(a)):
            if i != pivot_row and a[i][col]:
                multiple = a[i][col]
                for j in range(col, width):
                    a[i][j] -= multiple * a[pivot_row][j]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def walsh_coefficients(states: Sequence[Sequence[int]]) -> dict[tuple[int, ...], Fraction]:
    """All interaction moments E[product_{i in S} X_i], X_i in {-1,+1}.

    States can repeat (empirical multiset). The EMPTY-set coefficient is 1.
    Exact Walsh/Fourier inversion recovers the entire joint distribution;
    coefficients of size <=2 alone can fail to recover ternary parity.
    """
    if not states:
        raise ValueError("at least one state required")
    dimension = len(states[0])
    if not dimension:
        raise ValueError("at least one channel required")
    if any(len(row) != dimension or any(type(x) is not int or x not in (-1, 1)
                                       for x in row) for row in states):
        raise ValueError("states are uniform-length arrays of -1 or +1")
    return {
        indices: Fraction(sum(prod(row[i] for i in indices) for row in states), len(states))
        for size in range(dimension + 1)
        for indices in combinations(range(dimension), size)
    }


def walsh_inverse_at(coefficients: Mapping[tuple[int, ...], Fraction],
                     point: Sequence[int]) -> Fraction:
    """Probability of a given +-1 tuple by exact full Walsh inversion."""
    if not point or any(type(x) is not int or x not in (-1, 1) for x in point):
        raise ValueError("point must have positive length and entries ±1")
    dimension = len(point)
    expected = {subset for r in range(dimension + 1)
                for subset in combinations(range(dimension), r)}
    if set(coefficients) != expected:
        raise ValueError("complete normalized coefficient family required")
    return sum((Fraction(coefficients[s]) * prod(point[i] for i in s)
                for s in expected), Fraction(0)) / (2 ** dimension)


def parity_states(dimension: int, parity: int) -> tuple[tuple[int, ...], ...]:
    """Support X_0...X_(d-1)=parity, with 2^(d-1) equal-weight states."""
    if type(dimension) is not int or dimension < 1 or parity not in (-1, 1):
        raise ValueError("positive dimension and signed parity required")
    return tuple(row for row in product((-1, 1), repeat=dimension)
                 if prod(row) == parity)


def global_fourier_second_moment(base: int, frequency: int, length: int) -> Fraction:
    """Haar ∫|N^-1 Σ_{n<N} exp(2πi frequency*base^n*x)|² dx.

    Uses exact character orthogonality, not a sample or cancellation guess.
    """
    if type(base) is not int or base < 2 or type(frequency) is not int or type(length) is not int or length < 1:
        raise ValueError("base>=2, integer frequency, positive length required")
    frequencies = [frequency * (base ** n) for n in range(length)]
    return Fraction(sum(a == b for a in frequencies for b in frequencies), length**2)


def selected_orbit_phase(base: int, seed: Fraction | int, length: int) -> tuple[Fraction, ...]:
    """Exact phase exponents modulo 1; no complex approximation or normality."""
    if type(base) is not int or base < 2 or type(length) is not int or length < 1:
        raise ValueError("base>=2 and positive length required")
    x = Fraction(seed) % 1
    out = []
    for _ in range(length):
        out.append(x)
        x = (base*x) % 1
    return tuple(out)


def certificate_constant_phase(phases: Sequence[Fraction | int], frequency: int) -> bool:
    """Prove |mean exp(2π i h x_n)|=1 WHEN all phase exponents coincide.

    False is UNKNOWN; in particular it does not certify positive cancellation.
    """
    if not phases or type(frequency) is not int:
        raise ValueError("nonempty phase sequence and integer frequency required")
    exponents = [(frequency * Fraction(x)) % 1 for x in phases]
    return all(v == exponents[0] for v in exponents)


@dataclass(frozen=True)
class LaggedForces:
    """One time-slice of a chosen interpretation of the Aphex Twin title.

    D[n] has a typed value; incoming[j][n-1] and external[n-1] must
    share units. 'n^-1' in some reproductions is ambiguous, not silently
    repaired. The model explicitly elects n-1 as an interpretation.
    """
    envelope: Quantity
    incoming_previous: tuple[Quantity, ...]
    external_previous: Quantity


def aphex_style_update(alpha: Quantity, terms: Sequence[LaggedForces],
                       target_unit: Unit) -> Quantity:
    """-alpha sum_n D_i[n] (sum_j F_ji[n-1]+F_ext,i[n-1]); typed.

    This is an algebraic *interpretation*, not an identification of the
    composition's historical formula with physics, DSP or SUCC dynamics.
    """
    if not terms:
        raise ValueError("nonempty update history required")
    acc = Quantity(0, target_unit)
    for term in terms:
        previous = term.external_previous
        for force in term.incoming_previous:
            previous = previous + force  # explicitly reject mismatched dimensions
        update = alpha * term.envelope * previous
        if update.unit != target_unit:
            raise TypeError("update has incorrect inverse-mass target dimension")
        acc = acc - update
    return acc


def finite_grid_fourier_second_moment(base: int, frequency: int,
                                      length: int, grid_depth: int) -> Fraction:
    """Exact average of |W_N(x)|² on x=j/base**grid_depth, uniform j.

    Works for all frequencies, including aliases; this is a grid observer,
    not Haar on the full circle. Computed by modular orthogonality.
    """
    if (type(base) is not int or base < 2 or type(frequency) is not int
            or type(length) is not int or length < 1
            or type(grid_depth) is not int or grid_depth < 0):
        raise ValueError("base>=2; integer h; N>=1; grid depth>=0 required")
    modulus = base ** grid_depth
    frequencies = [frequency * pow(base, n, modulus) % modulus for n in range(length)]
    counts = {}
    for f in frequencies:
        counts[f] = counts.get(f, 0) + 1
    return Fraction(sum(v * v for v in counts.values()), length**2)


def grid_alias_closed_form(base: int, frequency: int, length: int,
                           grid_depth: int) -> Fraction:
    """For gcd(h, base)=1, E = [min(N,K)+max(N-K,0)^2]/N^2.

    Finite-resolution and temporal limits do NOT commute for this experiment.
    """
    from math import gcd
    if (type(base) is not int or base < 2 or type(frequency) is not int
            or gcd(frequency, base) != 1
            or type(length) is not int or length < 1
            or type(grid_depth) is not int or grid_depth < 0):
        raise ValueError("base>=2, gcd(h,b)=1, N>=1 and K>=0 required")
    early = min(length, grid_depth)
    late = max(0, length-grid_depth)
    return Fraction(early+late*late, length*length)


def seed_grid_energy_formal(phase_by_index: Mapping[int, Fraction | int],
                            base: int, frequency: int,
                            grid_depth: int) -> dict[Fraction, int]:
    """Exact Q[Q/Z] numerator of Haar energy over 1/base^K seed shifts.

    For the inhomogeneous source orbit U_n(s)=U_n(0)+base^n*s, let
    a_n=e(h U_n(0)). Average |sum_n a_n e(h base^n*s)|² over
    s=j/base^K. Group algebra retains signed rational phases BEFORE
    complex evaluation. Divide coefficients by N² to get energy.

    Character orthogonality kills pairs except where
    h*(base^n-base^m) == 0 (mod base^K). No unsigned positivity
    inference is made about the original source's selected signed sum.
    """
    if (type(base) is not int or base < 2 or type(frequency) is not int
            or type(grid_depth) is not int or grid_depth < 0
            or not phase_by_index
            or any(type(n) is not int or n < 0 for n in phase_by_index)):
        raise ValueError("base>=2, integer h, K>=0, nonempty nonnegative time labels")
    modulus = base ** grid_depth
    classes: dict[int, list[Fraction]] = {}
    for n, phase in phase_by_index.items():
        label = (frequency * pow(base, n, modulus)) % modulus
        classes.setdefault(label, []).append(Fraction(phase) % 1)
    out: dict[Fraction, int] = {}
    for phases in classes.values():
        for x in phases:
            for y in phases:
                exponent = (frequency * (x-y)) % 1
                out[exponent] = out.get(exponent, 0) + 1
    return {exponent:count for exponent,count in out.items() if count}


def seed_grid_energy_shell_form(base: int, frequency: int, start: int,
                                length: int, grid_depth: int) -> tuple[int, tuple[int, ...]]:
    """For gcd(h,b)=1, symbolic energy = early_count + |late Weyl sum|².

    Early n<K each contribute 1, late n>=K alias into one block.
    Returns (early_count, late_indices). Divide by length².
    """
    from math import gcd
    if (type(base) is not int or base < 2 or type(frequency) is not int
            or gcd(frequency,base) != 1 or type(start) is not int
            or start < 0 or type(length) is not int or length < 1
            or type(grid_depth) is not int or grid_depth < 0):
        raise ValueError("base>=2, h coprime, nonnegative start and K, positive length")
    early = max(0, min(start+length,grid_depth)-start)
    late = tuple(range(max(start,grid_depth), start+length))
    return early, late
