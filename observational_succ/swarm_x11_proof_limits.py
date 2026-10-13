"""Finite supports for source/basis-indexed positive certification.

This exact finite laboratory does not execute an ideal limit. Scott openness
and the converse support representation are proved in SWARM_ATLAS/X11.md.
Rules and source semantics are declared inputs, not authenticated here.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from typing import Iterable

from .swarm_completion import PartialEvidence


class CertificationError(ValueError):
    """A finite certificate lost an evidence, license, or context premise."""


def _name(value: object) -> bool:
    return isinstance(value, str) and bool(value)


def observation_atom(address: int, value: int) -> str:
    if type(address) is not int or address < 0 or type(value) is not int or value not in (0, 1):
        raise CertificationError("Use exact nonnegative addresses and binary reports")
    return f"obs:{address}:{value}"


@dataclass(frozen=True)
class CertificationContext:
    source_id: str
    basis_id: str

    def __post_init__(self):
        if not _name(self.source_id) or not _name(self.basis_id):
            raise CertificationError("An unchanged source and semantic basis are required")


@dataclass(frozen=True)
class LicensedStage:
    context: CertificationContext
    evidence: PartialEvidence
    licenses: frozenset[str]

    def __post_init__(self):
        if not isinstance(self.context, CertificationContext) or not isinstance(self.evidence, PartialEvidence):
            raise CertificationError("Typed context and finite partial evidence required")
        if type(self.licenses) is not frozenset or any(not _name(x) for x in self.licenses):
            raise CertificationError("Rule availability is an explicit immutable finite set")
        for address, value in self.evidence.entries:
            observation_atom(address, value)

    def extends(self, older: LicensedStage) -> bool:
        return (self.context == older.context and self.evidence.extends(older.evidence)
                and self.licenses >= older.licenses)

    def join(self, other: LicensedStage) -> LicensedStage:
        if self.context != other.context:
            raise CertificationError("A source or basis change needs its own transport proof")
        return LicensedStage(self.context, self.evidence.join(other.evidence),
                             self.licenses | other.licenses)


@dataclass(frozen=True)
class LicensedRule:
    license_id: str
    premises: tuple[str, ...]
    conclusion: str

    def __post_init__(self):
        if (not _name(self.license_id) or type(self.premises) is not tuple
                or any(not _name(p) for p in self.premises)
                or len(set(self.premises)) != len(self.premises)
                or not _name(self.conclusion)):
            raise CertificationError("A rule has one name, finite distinct premises, and a conclusion")


@dataclass(frozen=True)
class Certificate:
    support: LicensedStage
    conclusion: str
    steps: tuple[tuple[str, str, tuple[str, ...]], ...]


def _catalog(rules: tuple[LicensedRule, ...]) -> dict[str, LicensedRule]:
    if (type(rules) is not tuple or any(not isinstance(r, LicensedRule) for r in rules)
            or len({r.license_id for r in rules}) != len(rules)):
        raise CertificationError("Use a fixed catalog with unique rule license identifiers")
    return {r.license_id: r for r in rules}


def derive(stage: LicensedStage, rules: tuple[LicensedRule, ...], conclusion: str) -> Certificate | None:
    """Finite positive closure; missing support returns UNRESOLVED via None."""
    _catalog(rules)
    if not _name(conclusion):
        raise CertificationError("A named target conclusion is required")
    known = {observation_atom(n, v) for n, v in stage.evidence.entries}
    steps = []
    while conclusion not in known:
        changed = False
        for rule in rules:
            if (rule.license_id in stage.licenses and rule.conclusion not in known
                    and set(rule.premises) <= known):
                known.add(rule.conclusion)
                steps.append((rule.conclusion, rule.license_id, rule.premises))
                changed = True
        if not changed:
            return None
    receipt = Certificate(stage, conclusion, tuple(steps))
    if not verify_certificate(receipt, stage, rules):
        raise AssertionError("Generated proof failed independent replay")
    return receipt


def verify_certificate(receipt: Certificate, available: LicensedStage,
                       rules: tuple[LicensedRule, ...]) -> bool:
    """Replay against supplied evidence; a receipt cannot authorize its own leaves."""
    catalog = _catalog(rules)
    if not isinstance(receipt, Certificate) or not available.extends(receipt.support):
        return False
    known = {observation_atom(n, v) for n, v in receipt.support.evidence.entries}
    for conclusion, license_id, premises in receipt.steps:
        rule = catalog.get(license_id)
        if (rule is None or license_id not in receipt.support.licenses
                or conclusion != rule.conclusion or premises != rule.premises
                or not set(premises) <= known):
            return False
        known.add(conclusion)
    return receipt.conclusion in known


def all_binary_evidence(addresses: tuple[int, ...]) -> tuple[PartialEvidence, ...]:
    if (type(addresses) is not tuple or len(set(addresses)) != len(addresses)
            or any(type(n) is not int or n < 0 for n in addresses)):
        raise CertificationError("Distinct exact nonnegative addresses required")
    return tuple(PartialEvidence.from_mapping({n: v for n, v in zip(addresses, values) if v is not None})
                 for values in product((None, 0, 1), repeat=len(addresses)))


def restrictions(evidence: PartialEvidence) -> tuple[PartialEvidence, ...]:
    return tuple(PartialEvidence(entries) for size in range(len(evidence.entries) + 1)
                 for entries in combinations(evidence.entries, size))


def finite_completions(evidence: PartialEvidence,
                       sources: tuple[PartialEvidence, ...]) -> tuple[PartialEvidence, ...]:
    """Compatibility with a declared COMPLETE finite source enumeration."""
    return tuple(source for source in sources if source.extends(evidence))


def certify_finite_source(evidence: PartialEvidence, sources: tuple[PartialEvidence, ...],
                          positive: frozenset[PartialEvidence]) -> int | None:
    """The flat partial Boolean report; reject empty fibers, never certify by vacuity."""
    if not sources or len(set(sources)) != len(sources) or not positive <= set(sources):
        raise CertificationError("A nonempty complete source set and its property subset are required")
    domain = tuple(n for n, _ in sources[0].entries)
    if any(tuple(n for n, _ in source.entries) != domain for source in sources):
        raise CertificationError("Every source has the same declared complete coordinate domain")
    completions = finite_completions(evidence, sources)
    if not completions:
        raise CertificationError("Inadmissible evidence has no original-source witness")
    values = {int(source in positive) for source in completions}
    return values.pop() if len(values) == 1 else None


def finite_ideals(basis: tuple[PartialEvidence, ...]) -> tuple[frozenset[PartialEvidence], ...]:
    """Exhaustive finite domain audit with an explicit small resource bound."""
    if len(basis) > 12 or len(set(basis)) != len(basis):
        raise CertificationError("Ideal enumeration is bounded to 12 distinct basis elements")
    answer = []
    for size in range(1, len(basis) + 1):
        for chosen in combinations(basis, size):
            ideal = frozenset(chosen)
            downward = all(not p.extends(q) or q in ideal for p in ideal for q in basis)
            directed = all(any(r.extends(p) and r.extends(q) for r in ideal)
                           for p in ideal for q in ideal)
            if downward and directed:
                answer.append(ideal)
    return tuple(answer)


def first_zero_parity_witnesses(addresses: Iterable[int]) -> tuple[int, int]:
    """Two eventual-zero streams fitting finite all-one evidence, opposite parity.

    Returned k represents the exact stream 1^k 0^infinity, not an observed
    source. Every listed address is strictly before both possible first zeros.
    """
    observed = tuple(addresses)
    if any(type(n) is not int or n < 0 for n in observed):
        raise CertificationError("Only actual finite nonnegative evidence addresses are accepted")
    first = max(observed, default=-1) + 1
    even = first + first % 2
    odd = first + (1 - first % 2)
    return even, odd
