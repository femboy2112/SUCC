"""Bounded source-relative gluing; finite receipts never discharge analysis.

Grammar: id(X), instrument(X,Y,a), then(f,g). Existing InstrumentArrow and
StochasticInstrument implement composition; passports guard its source epoch.
Paper proofs and hypothesis countermodels: SOURCE_GLUING_PROOF_TEETH.md.
All source names are declarations, not authentication. No analytic truth flags.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from fractions import Fraction as Q

from .field_limit_trichotomy import (
    bounded_binary_turing_diagonal, kleene_source_tree_accepts,
)
from .recursive_operator_gluing import matrix, principal_minors, product, transpose
from .source_field_inverse_limits import FieldSourcePassport
from .swarm_categories import InstrumentArrow
from .swarm_probability import StochasticInstrument, compose
from .tate_adele_quotient_descent import FiniteAdeleCoset


class ProofGluingError(ValueError):
    """An exact finite guard failed; never an infinite impossibility verdict."""


class ProofDebt(Enum):
    SOURCE_IDENTIFICATION = "Identify the declared maps with the intended source"
    COMMON_OPERATOR = "Identify every stage with a compression of ONE operator"
    BOUNDED_SELF_ADJOINT = "Prove A=A* on H and a finite global norm bound"
    DENSE_PROJECTORS = "Prove increasing orthogonal projectors converge strongly to I"
    ALL_STAGE_POSITIVITY = "Prove positivity for EVERY stage, beyond this finite receipt"


def _passport(value: FieldSourcePassport) -> None:
    if type(value) is not FieldSourcePassport:
        raise ProofGluingError("Use an existing FieldSourcePassport")


def _same_source(left: FieldSourcePassport, right: FieldSourcePassport) -> None:
    _passport(left)
    _passport(right)
    if left != right:
        raise ProofGluingError("Source, observer closure, or epoch mismatch")


def _name(value: str) -> None:
    if type(value) is not str or not value.strip():
        raise ProofGluingError("Nonempty declared carrier/operator/basis name required")


@dataclass(frozen=True)
class FiniteObject:
    source: FieldSourcePassport
    carrier: str
    size: int

    def __post_init__(self) -> None:
        _passport(self.source)
        _name(self.carrier)
        if type(self.size) is not int or not 1 <= self.size <= 256:
            raise ProofGluingError("Finite complete carrier size must be 1..256")


@dataclass(frozen=True)
class LawfulOperation:
    """A declared deterministic instrument, with complete source/report tables.

    Epoch changes need a separate authenticated transport outside this grammar.
    Matching source strings alone do not discharge SOURCE_IDENTIFICATION.
    """
    before: FiniteObject
    after: FiniteObject
    instrument: InstrumentArrow

    def __post_init__(self) -> None:
        if type(self.before) is not FiniteObject or type(self.after) is not FiniteObject:
            raise ProofGluingError("Typed finite endpoints required")
        _same_source(self.before.source, self.after.source)
        a = self.instrument
        if (type(a) is not InstrumentArrow or
                (a.domain, a.codomain) != (self.before.size, self.after.size)):
            raise ProofGluingError("Instrument does not cover its declared endpoints")
        if a.width > 64 or len(a.alphabet) > 256:
            raise ProofGluingError("Finite report budget exceeded")

    @classmethod
    def identity(cls, obj: FiniteObject) -> LawfulOperation:
        if type(obj) is not FiniteObject:
            raise ProofGluingError("Typed identity endpoint required")
        return cls(obj, obj, InstrumentArrow.identity(obj.size))

    def then(self, after: LawfulOperation) -> LawfulOperation:
        if type(after) is not LawfulOperation or self.after != after.before:
            raise ProofGluingError("Composition requires the same full middle object")
        if (self.instrument.width + after.instrument.width > 64 or
                len(self.instrument.alphabet) * len(after.instrument.alphabet) > 256):
            raise ProofGluingError("Composition exceeds finite report budget")
        return LawfulOperation(self.before, after.after,
                               self.instrument.then(after.instrument))

    @property
    def unresolved_debts(self) -> tuple[ProofDebt, ...]:
        return (ProofDebt.SOURCE_IDENTIFICATION,)


@dataclass(frozen=True)
class CommutingSquare:
    """Verified square: right after top = bottom after left on EVERY source.

    Both actual carrier states and ordered report words must agree. Equal
    present reports alone cannot hide a different future carrier.
    """
    top: LawfulOperation
    right: LawfulOperation
    left: LawfulOperation
    bottom: LawfulOperation

    def __post_init__(self) -> None:
        if any(type(a) is not LawfulOperation
               for a in (self.top, self.right, self.left, self.bottom)):
            raise ProofGluingError("Four typed operations required")
        a, b = self.top.then(self.right), self.left.then(self.bottom)
        if (a.before, a.after) != (b.before, b.after):
            raise ProofGluingError("Square endpoints disagree")
        for x in range(a.before.size):
            if (a.instrument.transition[x], a.instrument.reports[x]) != (
                    b.instrument.transition[x], b.instrument.reports[x]):
                raise ProofGluingError(f"Noncommuting carrier/report square at source {x}")

    @property
    def unresolved_debts(self) -> tuple[ProofDebt, ...]:
        return (ProofDebt.SOURCE_IDENTIFICATION,)


@dataclass(frozen=True)
class SourceKernel:
    """Epoch guard around the existing JOINT report/post-carrier kernel."""
    source: FieldSourcePassport
    kernel: StochasticInstrument

    def __post_init__(self) -> None:
        _passport(self.source)
        if type(self.kernel) is not StochasticInstrument or self.kernel.source_id != self.source.source:
            raise ProofGluingError("Joint kernel source differs from its passport")
        if (self.kernel.before_count > 64 or self.kernel.after_count > 64 or
                any(len(row) > 256 for row in self.kernel.rows)):
            raise ProofGluingError("Joint kernel exceeds finite budget")

    def then(self, after: SourceKernel) -> SourceKernel:
        if type(after) is not SourceKernel:
            raise ProofGluingError("Typed source kernel required")
        _same_source(self.source, after.source)
        # Bound expansion BEFORE calling the existing Cartesian composer.
        if (self.kernel.output_space != after.kernel.input_space or
                self.kernel.after_count != after.kernel.before_count):
            raise ProofGluingError("Joint kernel middle carrier mismatch")
        if any(sum(len(after.kernel.rows[y]) for _, y, _ in row) > 256
               for row in self.kernel.rows):
            raise ProofGluingError("Joint composition exceeds finite row budget")
        return SourceKernel(self.source, compose(self.kernel, after.kernel))

    @property
    def unresolved_debts(self) -> tuple[ProofDebt, ...]:
        return (ProofDebt.SOURCE_IDENTIFICATION,)


def check_same_joint_law(actual: SourceKernel, proposed: SourceKernel) -> None:
    """Exact full-law guard; equal report and carrier marginals do NOT suffice.

    Names/costs are not asserted equal: this guard concerns conditional laws.
    Returning normally checks only these declared finite laws, not authenticity.
    """
    if type(actual) is not SourceKernel or type(proposed) is not SourceKernel:
        raise ProofGluingError("Two source-indexed kernels required")
    _same_source(actual.source, proposed.source)
    a, b = actual.kernel, proposed.kernel
    if (a.input_space, a.output_space, a.before_count, a.after_count) != (
            b.input_space, b.output_space, b.before_count, b.after_count):
        raise ProofGluingError("Joint law endpoint mismatch")
    for x, (row, other) in enumerate(zip(a.rows, b.rows)):
        if {(r, y): p for r, y, p in row} != {(r, y): p for r, y, p in other}:
            raise ProofGluingError(f"Joint probability coupling mismatch at source {x}")


@dataclass(frozen=True)
class CompressionStage:
    """Real rational form in a declared orthonormal basis; dimension <= 8."""
    source: FieldSourcePassport
    operator: str
    basis: str
    coefficients: tuple[tuple[Q, ...], ...]

    def __post_init__(self) -> None:
        _passport(self.source)
        _name(self.operator)
        _name(self.basis)
        if (type(self.coefficients) is not tuple or not 1 <= len(self.coefficients) <= 8 or
                any(type(row) is not tuple or len(row) != len(self.coefficients)
                    for row in self.coefficients)):
            raise ProofGluingError("Exact square rational compression, dimension 1..8")
        a = matrix(self.coefficients)
        if a != transpose(a):
            raise ProofGluingError("Finite compression must be self-adjoint")
        object.__setattr__(self, "coefficients", a)


@dataclass(frozen=True)
class PositiveCompressionChain:
    """Finite PSD matrices, isometries J, and J* A_next J = A_previous.

    inclusions[k] maps stage k coordinates into stage k+1 coordinates.
    This is a form-compression square, NOT A_next J = J A_previous.
    Even a successful constructor leaves every infinite/source debt below.
    """
    stages: tuple[CompressionStage, ...]
    inclusions: tuple[tuple[tuple[Q, ...], ...], ...]

    def __post_init__(self) -> None:
        if (type(self.stages) is not tuple or not 1 <= len(self.stages) <= 16 or
                any(type(s) is not CompressionStage for s in self.stages) or
                type(self.inclusions) is not tuple or len(self.inclusions) != len(self.stages)-1):
            raise ProofGluingError("Finite stages and every adjacent inclusion required")
        for stage in self.stages:
            _same_source(self.stages[0].source, stage.source)
            if stage.operator != self.stages[0].operator:
                raise ProofGluingError("Common declared operator required")
            for indices, det in principal_minors(stage.coefficients):
                if det < 0:
                    raise ProofGluingError(f"Negative principal minor {indices}: {det}")
        normalized = []
        for low, high, raw in zip(self.stages, self.stages[1:], self.inclusions):
            n, m = len(low.coefficients), len(high.coefficients)
            if (m < n or type(raw) is not tuple or len(raw) != m or
                    any(type(row) is not tuple or len(row) != n for row in raw)):
                raise ProofGluingError("Inclusion needs every coordinate of its typed bases")
            j = matrix(raw)
            identity = tuple(tuple(Q(int(a == b)) for b in range(n)) for a in range(n))
            if product(transpose(j), j) != identity:
                raise ProofGluingError("Inclusion is not isometric in the declared metric")
            if product(transpose(j), product(high.coefficients, j)) != low.coefficients:
                raise ProofGluingError("Source form compression square does not commute")
            normalized.append(j)
        object.__setattr__(self, "inclusions", tuple(normalized))

    @property
    def unresolved_debts(self) -> tuple[ProofDebt, ...]:
        # No caller-provided booleans or empty debt list can discharge these.
        return tuple(ProofDebt)


@dataclass(frozen=True)
class KleeneLevelReceipt:
    depth: int
    prefix: tuple[int, ...]
    observed_diagonal_halts: tuple[tuple[int, int], ...]


def kleene_level_receipt(depth: int) -> KleeneLevelReceipt:
    """Actual enumeration execution, not a supplied synthetic halting trace.

    None means no halt seen WITHIN depth steps; it is not nonhalting evidence.
    The unbounded numbering and diagonal proof are in the paper, not this cap.
    """
    if type(depth) is not int or not 0 <= depth <= 64:
        raise ProofGluingError("Finite diagonal depth must be 0..64")
    outputs = tuple(bounded_binary_turing_diagonal(e, depth) for e in range(depth))
    prefix = tuple(0 if bit is None else 1-bit for bit in outputs)
    if not kleene_source_tree_accepts(prefix):
        raise ArithmeticError("Actual bounded TM enumeration violates tree law")
    return KleeneLevelReceipt(depth, prefix,
                              tuple((e, bit) for e, bit in enumerate(outputs) if bit is not None))


@dataclass(frozen=True)
class RationalLiftObstruction:
    quotient_class: Q
    torsion_order: int
    rational_lift: Q
    multiplied_lift: Q


def adele_lift_obstruction(coset: FiniteAdeleCoset) -> RationalLiftObstruction:
    """Exact witness that the displayed rational lift is not additive on torsion.

    The paper proves NO group section at all. A finite witness only rejects
    this displayed lift on the cyclic subgroup generated by the given class.
    """
    if type(coset) is not FiniteAdeleCoset:
        raise ProofGluingError("Use the existing finite adele quotient source")
    coset.check()
    residue = coset.class_mod_integers
    if not residue:
        raise ProofGluingError("A nonzero torsion class is needed for this obstruction")
    order = residue.denominator
    lift = coset.rational_lift
    multiple = order * lift
    if multiple.denominator != 1 or not multiple:
        raise ArithmeticError("Nonzero rational lift did not expose torsion obstruction")
    return RationalLiftObstruction(residue, order, lift, multiple)
