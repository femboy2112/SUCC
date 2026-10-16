"""Exact finite cylinders for the normalized-Haar Hilbert direct limit.

PH-01--PH-08 in PROFINITE_HILBERT_RECONSTRUCTION.md supply the paper proofs.
This bounded cyclotomic evaluator does not construct arbitrary L2 functions.
Inner products are linear in the FIRST variable. Positive-phase characters
therefore have negative-phase, 1/n-normalized Fourier coefficients.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import gcd, lcm
from typing import Callable, Sequence

from .classical_haar_clock import PrimeHaarClock, haar_inner
from .classical_unit_origin import chart_multiplier, chart_successor
from .dynamic_fourier_tower import lift_character, sum_fibers
from .finite_fourier_carrier import CyclotomicElement, exact_dft
from .finite_quotient_retract import FiniteQuotientRetract
from .pontryagin_source_duality import RationalCircleCharacter


class ProfiniteHilbertError(ValueError):
    """An invalid exact cylinder, source arrow, or finite computation budget."""


def _integer(value: int, name: str) -> int:
    if type(value) is not int:
        raise ProfiniteHilbertError(f"{name} must be an exact integer")
    return value


def _modulus(n: int) -> int:
    if type(n) is not int or not 1 <= n <= 100:
        raise ProfiniteHilbertError("Explicit carrier and coefficient field must lie in 1..100")
    return n


def _embed(z: CyclotomicElement, field: int) -> CyclotomicElement:
    _modulus(field)
    if field % z.modulus:
        raise ProfiniteHilbertError("Coefficient transport requires a divisible root order")
    if z.modulus == field:
        return z
    if z.modulus == 1:
        return CyclotomicElement.scalar(field, z.polynomial[0])
    return lift_character(z, field)


def conjugate(z: CyclotomicElement) -> CyclotomicElement:
    """Complex conjugation in the declared cyclotomic embedding."""
    total = CyclotomicElement.scalar(z.modulus, 0)
    for j, coefficient in enumerate(z.polynomial):
        if coefficient:
            total = total + CyclotomicElement.root(z.modulus, -j).scale(coefficient)
    return total


def _linear_map(values: tuple[CyclotomicElement, ...],
                operation: Callable[[tuple[Q, ...]], tuple[Q, ...]]) -> tuple[CyclotomicElement, ...]:
    """Extend an existing rational kernel coefficientwise, without a second kernel."""
    width = max(len(z.polynomial) for z in values)
    columns = tuple(operation(tuple(z.polynomial[j] if j < len(z.polynomial) else Q()
                                    for z in values)) for j in range(width))
    return tuple(CyclotomicElement(values[0].modulus, tuple(c[i] for c in columns))
                 for i in range(len(columns[0])))


@dataclass(frozen=True)
class HaarCylinder:
    """A source-indexed function on Z/n, with exact cyclotomic sample values.

    Its coefficient field is separate from its carrier: averaging a constant
    zeta_3 from Z/6 to Z/2 must retain zeta_3. All roots use the canonical
    complex embedding. Carrier/field least common multiples above 100 refuse.
    Equal L2 cylinders can have different representations; use equivalent().
    """

    modulus: int
    values: tuple[int | Q | CyclotomicElement, ...]
    source_id: str = "Z-integer-modular-source"
    epoch: int = 0

    def __post_init__(self) -> None:
        n = _modulus(self.modulus)
        if (type(self.source_id) is not str or not self.source_id.strip()
                or type(self.epoch) is not int or self.epoch < 0):
            raise ProfiniteHilbertError("Declare a nonempty source and nonnegative exact epoch")
        if not isinstance(self.values, (list, tuple)) or len(self.values) != n:
            raise ProfiniteHilbertError("One exact amplitude per declared source residue required")
        if any(type(v) not in (int, Q, CyclotomicElement) for v in self.values):
            raise ProfiniteHilbertError("Amplitudes must be integers, Fractions or cyclotomic elements")
        field = _modulus(lcm(n, *(v.modulus for v in self.values
                                  if isinstance(v, CyclotomicElement))))
        object.__setattr__(self, "values", tuple(
            _embed(v, field) if isinstance(v, CyclotomicElement)
            else CyclotomicElement.scalar(field, v) for v in self.values))

    @property
    def field(self) -> int:
        return self.values[0].modulus

    def _new(self, n: int, values: Sequence) -> "HaarCylinder":
        return HaarCylinder(n, tuple(values), self.source_id, self.epoch)

    def _same_source(self, other: "HaarCylinder") -> None:
        if not isinstance(other, HaarCylinder) or (
                self.source_id, self.epoch) != (other.source_id, other.epoch):
            raise ProfiniteHilbertError("Hilbert arrows require the same source ID and epoch")

    @classmethod
    def character(cls, character: RationalCircleCharacter,
                  modulus: int | None = None) -> "HaarCylinder":
        if not isinstance(character, RationalCircleCharacter):
            raise ProfiniteHilbertError("A source-typed Q/Z character is required")
        n = _modulus(character.frequency.denominator if modulus is None else modulus)
        finite = character.on_finite_clock(n)
        return cls(n, tuple(finite.character_root(x) for x in range(n)),
                   character.source_id, character.epoch)

    def refine(self, fine: int) -> "HaarCylinder":
        """U_(fine,n): isometric cylinder pullback; identities and n=1 included."""
        fine = _modulus(fine)
        if fine % self.modulus:
            raise ProfiniteHilbertError("Cylinder pullback requires n | fine")
        _modulus(lcm(self.field, fine))
        if fine == self.modulus:
            return self
        if self.modulus == 1:
            values = self.values * fine
        else:
            retract = FiniteQuotientRetract(fine, self.modulus, self.source_id, self.epoch)
            values = _linear_map(self.values, retract.pullback)
        return self._new(fine, values)

    def condition(self, coarse: int) -> "HaarCylinder":
        """A_(n,coarse)=U*: normalized fiber average, retaining coefficient field."""
        coarse = _modulus(coarse)
        if self.modulus % coarse:
            raise ProfiniteHilbertError("Conditional average requires coarse | n")
        if coarse == self.modulus:
            return self
        if coarse == 1:
            average = lambda column: (sum(column, Q()) / self.modulus,)
        else:
            average = FiniteQuotientRetract(
                self.modulus, coarse, self.source_id, self.epoch).average
        return self._new(coarse, _linear_map(self.values, average))

    def project(self, level: int) -> "HaarCylinder":
        """Global P_level on this finite cylinder, even for incomparable moduli."""
        level = _modulus(level)
        common = _modulus(lcm(self.modulus, level))
        return self.refine(common).condition(level).refine(common)

    def equivalent(self, other: "HaarCylinder") -> bool:
        self._same_source(other)
        common = _modulus(lcm(self.modulus, other.modulus))
        field = _modulus(lcm(self.field, other.field, common))
        left, right = self.refine(common), other.refine(common)
        return all(_embed(a, field) == _embed(b, field)
                   for a, b in zip(left.values, right.values))

    def inner(self, other: "HaarCylinder") -> CyclotomicElement:
        """Integral self * conjugate(other), using normalized Haar probability."""
        self._same_source(other)
        common = _modulus(lcm(self.modulus, other.modulus))
        field = _modulus(lcm(self.field, other.field, common))
        left, right = self.refine(common), other.refine(common)
        total = CyclotomicElement.scalar(field, 0)
        for a, b in zip(left.values, right.values):
            total = total + _embed(a, field) * conjugate(_embed(b, field))
        return total.scale(Q(1, common))

    def norm_squared(self) -> CyclotomicElement:
        return self.inner(self)

    def fourier(self) -> tuple[CyclotomicElement, ...]:
        """F_H(f)(a/n) = (1/n) sum_x f(x) exp(-2*pi*i*a*x/n).

        Uses the existing PLUS DFT on rational polynomial columns, reverses
        its frequency index, then normalizes by n. No square roots or floats.
        """
        if self.modulus == 1:
            return self.values
        n, field = self.modulus, self.field
        result = [CyclotomicElement.scalar(field, 0) for _ in range(n)]
        for j in range(max(len(z.polynomial) for z in self.values)):
            column = tuple(z.polynomial[j] if j < len(z.polynomial) else Q()
                           for z in self.values)
            transformed = exact_dft(column)
            root = CyclotomicElement.root(field, j)
            for a in range(n):
                result[a] = result[a] + root * _embed(transformed[-a % n], field)
        return tuple(z.scale(Q(1, n)) for z in result)

    @classmethod
    def from_fourier(cls, spectrum: Sequence, *,
                     source_id: str = "Z-integer-modular-source", epoch: int = 0) -> "HaarCylinder":
        """Synthesize sum_a c_a chi_(a/n); coefficients use counting ell2."""
        coefficients = cls(len(spectrum), tuple(spectrum), source_id, epoch)
        n, field = coefficients.modulus, coefficients.field
        values = []
        for x in range(n):
            total = CyclotomicElement.scalar(field, 0)
            for a, value in enumerate(coefficients.values):
                total = total + value * CyclotomicElement.root(field, (field // n) * a * x)
            values.append(total)
        return cls(n, tuple(values), source_id, epoch)

    def translate(self, step: int) -> "HaarCylinder":
        """Koopman T_step f(x)=f(x+step); permits any integer step."""
        step = _integer(step, "Translation")
        return self._new(self.modulus, tuple(self.values[(x + step) % self.modulus]
                                             for x in range(self.modulus)))

    def multiply(self, multiplier: int, offset: int = 0) -> "HaarCylinder":
        """Koopman f(x)->f(multiplier*x+offset), not an inverse permutation."""
        multiplier = _integer(multiplier, "Multiplier")
        offset = _integer(offset, "Affine offset")
        if multiplier < 1:
            raise ProfiniteHilbertError("Positive multiplication required; zero has no L2 extension")
        return self._new(self.modulus, tuple(
            self.values[(multiplier*x + offset) % self.modulus] for x in range(self.modulus)))

    def source_multiply(self, multiplier: int, chart: str = "n_minus_one") -> "HaarCylinder":
        """Reuse the authentic positive-integer source affine chart law."""
        return self.multiply(multiplier, chart_multiplier(0, multiplier, chart))

    def source_successor(self, step: int, chart: str = "n_minus_one") -> "HaarCylinder":
        return self.translate(chart_successor(0, step, chart))


def finite_commutation_witness(fine: int, coarse: int, multiplier: int,
                               offset: int = 0) -> dict:
    """PH-06: A M = M A iff gcd(multiplier, fine/coarse)=1.

    The supplied delta detects every failing case. A successful specimen is
    not a universal test; the iff is proved by a permutation of each fiber.
    """
    fine, coarse = _modulus(fine), _modulus(coarse)
    if fine % coarse:
        raise ProfiniteHilbertError("A genuine quotient is required")
    multiplier = _integer(multiplier, "Multiplier")
    offset = _integer(offset, "Affine offset")
    if multiplier < 1:
        raise ProfiniteHilbertError("Positive multiplier required")
    delta = HaarCylinder(fine, tuple(int(x == offset % fine) for x in range(fine)))
    left = delta.multiply(multiplier, offset).condition(coarse)
    right = delta.condition(coarse).multiply(multiplier, offset)
    expected = gcd(multiplier, fine // coarse) == 1
    if left.equivalent(right) != expected:
        raise AssertionError("Conditional-multiplier discriminating delta failed")
    return {"fine": fine, "coarse": coarse, "multiplier": multiplier, "offset": offset,
            "fiber_gcd": gcd(multiplier, fine // coarse),
            "commutes_for_all_vectors_by_PH_06": expected,
            "delta": tuple(v.polynomial[0] for v in delta.values),
            "average_after_multiply": tuple(v.polynomial[0] for v in left.values),
            "multiply_after_average": tuple(v.polynomial[0] for v in right.values)}


def norm_obstruction(level: int) -> dict:
    """PH-05 exact specimen: unit chi_(1/(2n)) has P_n chi=0."""
    level = _modulus(level)
    _modulus(2 * level)
    frequency = RationalCircleCharacter(Q(1, 2*level))
    witness = HaarCylinder.character(frequency)
    projected = witness.project(level)
    if witness.norm_squared().polynomial != (Q(1),) or any(
            z.polynomial != (Q(0),) for z in projected.values):
        raise AssertionError("Unit character did not obstruct norm convergence")
    return {"level": level, "frequency": frequency.frequency,
            "witness_norm_squared": Q(1), "projection_norm_squared": Q(0),
            "error_norm_squared": Q(1), "operator_norm_I_minus_P_by_PH_05": 1,
            "universal_proof_from_samples": False}


def profinite_hilbert_probe() -> dict:
    """Deterministic exact receipts with source and normalization controls."""
    source, epoch = "proof-teeth-haar-source", 7
    g = HaarCylinder(12, tuple(Q((7*x) % 11 - 5, 3) for x in range(12)), source, epoch)
    a = g.condition(3)
    if not g.condition(6).condition(3).equivalent(a):
        raise AssertionError("Average tower composition failed")
    if g.inner(a.refine(12)) != a.refine(12).norm_squared():
        raise AssertionError("Haar projection adjoint failed")
    sp = g.fourier()
    if not HaarCylinder.from_fourier(sp, source_id=source, epoch=epoch).equivalent(g):
        raise AssertionError("Exact normalized Fourier inversion failed")
    energy = CyclotomicElement.scalar(g.field, 0)
    for z in sp:
        energy = energy + z * conjugate(z)
    if energy != g.norm_squared():
        raise AssertionError("Haar/ell2 Parseval failed")
    rational = tuple(z.polynomial[0] for z in g.values)
    raw = sum_fibers(rational, 3)
    if tuple(v / 4 for v in raw) != tuple(z.polynomial[0] for z in a.values):
        raise AssertionError("Dynamic raw pushforward normalization bridge failed")
    clock = PrimeHaarClock(3, 1)
    local = HaarCylinder(3, (Q(1, 2), Q(-2, 3), Q(3, 4)))
    if local.norm_squared().polynomial != (haar_inner(clock, (Q(1, 2), Q(-2, 3), Q(3, 4)),
                                                                    (Q(1, 2), Q(-2, 3), Q(3, 4))),):
        raise AssertionError("Existing prime Haar inner product disagrees")
    # A fixed prime tower is not cofinal in all integer moduli.
    invisible = HaarCylinder.character(RationalCircleCharacter(Q(1, 3)))
    hidden = [invisible.project(n).norm_squared().polynomial[0] for n in (2, 4, 8)]
    if hidden != [Q(0)] * 3:
        raise AssertionError("Noncofinal prime-tower negative control failed")
    return {
        "kind": "PROFINITE_HILBERT_EXACT_FINITE_RECEIPT", "source_id": source, "epoch": epoch,
        "theorem_ids": [f"PH-{i:02d}" for i in range(1, 9)],
        "carrier_measure": "normalized real Haar probability; complex amplitudes",
        "spectral_measure": "counting measure on Q/Z",
        "positive_character_negative_coefficient_phase": True,
        "source_vector_12": rational, "average_at_3": tuple(z.polynomial[0] for z in a.values),
        "haar_energy": energy.polynomial, "tower_adjoint_inversion_parseval": True,
        "nonunit_failure_4_to_2": finite_commutation_witness(4, 2, 2, 1),
        "nonunit_on_carrier_but_commuting_6_to_2": finite_commutation_witness(6, 2, 2, 1),
        "norm_obstructions": [norm_obstruction(n) for n in (1, 2, 3, 6, 12)],
        "chi_one_third_energy_after_levels_2_4_8": hidden,
        "common_provenance": "Shared cyclotomic arithmetic; tests are not independent proof",
        "universal_theorems_proved_by_finite_tests": False,
        "physical_source_authenticated": False, "RH_proved": False,
    }
