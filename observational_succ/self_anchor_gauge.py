"""Finite source-map ambiguity, self-relative observation and calibration.

A *candidate world* is a complete, STIPULATED finite source table, not a
measurement or a certified physical source.  Calibration readings are licensed
only when their source/epoch relation is supplied as part of the world family.

This module extends the existing per-source fiber criterion to the disjoint
union of rival source interpretations.  It NEVER creates a calibration event.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations
from typing import Hashable, Mapping, Sequence


class SourceGaugeError(ValueError):
    """A malformed candidate-world family or gauge transport."""


@dataclass(frozen=True)
class CandidateWorld:
    """One source-map hypothesis about a common target task.

    ``reports[i]`` is the later report at ``states[i]``; ``targets[i]`` is
    the claim about that *original* source. ``references[j]`` is the earlier
    report obtained by deliberately preparing the known reference state j,
    if that intervention is truly available. The shared model label is hidden
    from the decoder. Source histories must be stated, never inferred from a
    reference and a later observation having the same spelling.
    """

    name: str
    source_id: str
    target_epoch: int
    states: tuple[Hashable, ...]
    reports: tuple[Hashable, ...]
    targets: tuple[Hashable, ...]
    references: tuple[Hashable, ...]
    reference_epoch: int = 0

    def __post_init__(self) -> None:
        n = len(self.states)
        if not self.name or not self.source_id or n == 0:
            raise SourceGaugeError("a world needs a name, source and states")
        if len(set(self.states)) != n:
            raise SourceGaugeError("state names must be distinct")
        if len(self.reports) != n or len(self.targets) != n or len(self.references) != n:
            raise SourceGaugeError("reports, targets and references must index all states")
        if self.reference_epoch > self.target_epoch:
            raise SourceGaugeError("a future reference cannot calibrate an earlier report")
        for item in (*self.reports, *self.targets, *self.references):
            try:
                hash(item)
            except TypeError as exc:
                raise SourceGaugeError("reports and targets must be hashable") from exc


@dataclass(frozen=True)
class SourceCase:
    world: str
    state: Hashable
    report: tuple[Hashable, ...]
    target: Hashable


@dataclass(frozen=True)
class DecoderAudit:
    sufficient: bool
    decoder: Mapping[tuple[Hashable, ...], Hashable]
    witness: tuple[SourceCase, SourceCase] | None
    analyzed_cases: int


def _validate_worlds(worlds: Sequence[CandidateWorld]) -> tuple[CandidateWorld, ...]:
    ws = tuple(worlds)
    if not ws:
        raise SourceGaugeError("the candidate source class must be nonempty")
    first = ws[0]
    if len({w.name for w in ws}) != len(ws):
        raise SourceGaugeError("each hypothetical world must have a unique name")
    for w in ws[1:]:
        if (w.source_id, w.target_epoch, w.reference_epoch, w.states) != (
            first.source_id, first.target_epoch, first.reference_epoch, first.states
        ):
            raise SourceGaugeError("source, epochs and reference-state basis must match")
    return ws


def decoder_audit(worlds: Sequence[CandidateWorld], anchors: Sequence[int] = ()) -> DecoderAudit:
    """Exact cross-world factorization criterion with a concrete obstruction pair.

    A single decoder D(report, reference-readouts) -> target exists on the
    *realizable* signatures iff target is constant on every cross-world fiber.
    A witness does NOT prove the world is wrong; it proves current information
    cannot decide the target across the stipulated rival worlds.
    """
    ws = _validate_worlds(worlds)
    chosen = tuple(anchors)
    n = len(ws[0].states)
    if len(set(chosen)) != len(chosen) or any(type(a) is not int or a < 0 or a >= n for a in chosen):
        raise SourceGaugeError("anchors must be distinct valid reference indices")
    if chosen != tuple(sorted(chosen)):
        raise SourceGaugeError("anchors must be sorted into a declared common basis")
    by_report: dict[tuple[Hashable, ...], SourceCase] = {}
    decoder: dict[tuple[Hashable, ...], Hashable] = {}
    for w in ws:
        calibration = tuple(w.references[j] for j in chosen)
        for i, state in enumerate(w.states):
            key = (w.reports[i], *calibration)
            case = SourceCase(w.name, state, key, w.targets[i])
            previous = by_report.get(key)
            if previous is not None and previous.target != case.target:
                return DecoderAudit(False, {}, (previous, case), sum(len(v.states) for v in ws))
            by_report[key] = case
            decoder[key] = case.target
    return DecoderAudit(True, decoder, None, sum(len(v.states) for v in ws))


def minimal_calibrations(worlds: Sequence[CandidateWorld]) -> tuple[tuple[int, ...], ...]:
    """All minimum-cardinality reference sets, or empty if none is sufficient.

    Searches only *declared* preparable reference states; a set of imaginary
    anchors is not an executed experimental program. For large n exponential.
    """
    ws = _validate_worlds(worlds)
    n = len(ws[0].states)
    for count in range(n + 1):
        solutions = tuple(subset for subset in combinations(range(n), count)
                          if decoder_audit(ws, subset).sufficient)
        if solutions:
            return solutions
    return ()


def permutation_worlds(n: int) -> tuple[CandidateWorld, ...]:
    """All n! stable bijective sensor dictionaries for the same n-state task."""
    if type(n) is not int or n < 1 or n > 7:
        raise SourceGaugeError("finite permutation oracle restricted to 1 <= n <= 7")
    states = tuple(range(n))
    return tuple(CandidateWorld(
        name=f"dictionary:{','.join(map(str, p))}", source_id=f"alien-{n}",
        target_epoch=1, states=states, reports=p, targets=states,
        references=p, reference_epoch=0,
    ) for p in permutations(states))


def equality_signature(readings: Sequence[Hashable]) -> tuple[int, ...]:
    """Canonical names for first appearances; invariant under stable bijections.

    Example: ('red','blue','red') -> (0,1,0). Two finite words over
    equally sized alphabets have the same signature exactly when a *single*
    permutation of the alphabet sends one word to the other.
    """
    seen: dict[Hashable, int] = {}
    signature: list[int] = []
    for item in readings:
        try:
            if item not in seen:
                seen[item] = len(seen)
            signature.append(seen[item])
        except TypeError as exc:
            raise SourceGaugeError("a sensor report must be hashable") from exc
    return tuple(signature)


def sensor_transport(old_dictionary: Sequence[int], new_dictionary: Sequence[int]) -> tuple[int, ...]:
    """Explicit label-frame transport new_dictionary o old_dictionary^{-1}.

    The two dictionaries must be externally supplied and certified to refer
    to the same abstract source alphabet. This function cannot attest that.
    """
    old, new = tuple(old_dictionary), tuple(new_dictionary)
    n = len(old)
    if sorted(old) != list(range(n)) or sorted(new) != list(range(n)):
        raise SourceGaugeError("both dictionaries must be permutations of the same alphabet")
    return tuple(new[old.index(label)] for label in range(n))


def transported_change(old_report: int, new_report: int, transport: Sequence[int]) -> bool:
    """Frame-aligned inequality; raw inequality is invalid under frame drift."""
    t = tuple(transport)
    if sorted(t) != list(range(len(t))) or type(old_report) is not int or type(new_report) is not int or not (0 <= old_report < len(t) and 0 <= new_report < len(t)):
        raise SourceGaugeError("reports and transport must share one finite alphabet")
    return t[old_report] != new_report


@dataclass(frozen=True)
class SignatureDiagnosis:
    """Conditional finite interpretation of a *supplied* report signature.

    IDENTIFIED: all admitted source cases share the same target.
    AMBIGUOUS: compatible source cases have different original targets.
    OUT_OF_MODEL: no admitted source case produces the report signature.

    None certifies that the report was physically actualized, nor that the
    world family contains reality. In particular, OUT_OF_MODEL is a request
    to audit receipt, instrument and model class; it is not a new ontology.
    """

    status: str
    compatible_cases: tuple[SourceCase, ...]
    possible_targets: tuple[Hashable, ...]


def diagnose_signature(worlds: Sequence[CandidateWorld],
                       observed: Sequence[Hashable],
                       anchors: Sequence[int] = ()) -> SignatureDiagnosis:
    """Separate prediction failure from ambiguity and conditional identification."""
    ws = _validate_worlds(worlds)
    chosen = tuple(anchors)
    # Reuse the certified finite anchor-basis type guard.
    decoder_audit(ws, chosen)
    observation = tuple(observed)
    if len(observation) != len(chosen) + 1:
        raise SourceGaugeError("observation needs one unknown-state report plus each anchor")
    cases = []
    for w in ws:
        calibration = tuple(w.references[j] for j in chosen)
        for i, state in enumerate(w.states):
            key = (w.reports[i], *calibration)
            if observation == key:
                cases.append(SourceCase(w.name, state, key, w.targets[i]))
    if not cases:
        return SignatureDiagnosis("OUT_OF_MODEL", (), ())
    targets = tuple(dict.fromkeys(case.target for case in cases))
    if len(targets) == 1:
        return SignatureDiagnosis("IDENTIFIED", tuple(cases), targets)
    return SignatureDiagnosis("AMBIGUOUS", tuple(cases), targets)
