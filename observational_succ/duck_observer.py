"""Exact finite observers, distinguishing probes and observable quotients.

The universally quantified closed-relation and quotient laws are formalized
in formal/DuckObserver.lean.  This Python implementation is separately checked
finite arithmetic, not an admitted Lean-to-Python refinement proof.  Declared
source tags bind certificates to their models; they do not authenticate an
external source.  No registry, callback or caller-written Boolean is authority.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass


class ObserverError(ValueError):
    """Malformed finite model, mistyped interface or stale certificate."""


class ProbeBudgetExceeded(ObserverError):
    """Search stopped without an equivalence or difference verdict."""


def _labels(value, *, unique=True):
    return (type(value) is tuple and all(type(x) is str and x for x in value)
            and (not unique or len(set(value)) == len(value)))


@dataclass(frozen=True)
class FiniteObserver:
    source_id: str
    epoch: int
    basis: str
    states: tuple[str, ...]
    actions: tuple[str, ...]
    transitions: tuple[tuple[int, ...], ...]
    outputs: tuple[str, ...]

    def __post_init__(self):
        n = len(self.states) if type(self.states) is tuple else -1
        if (type(self.source_id) is not str or not self.source_id
                or type(self.epoch) is not int or self.epoch < 0
                or type(self.basis) is not str or not self.basis
                or not _labels(self.states) or not _labels(self.actions)
                or not _labels(self.outputs, unique=False) or len(self.outputs) != n
                or type(self.transitions) is not tuple
                or len(self.transitions) != len(self.actions)
                or any(type(row) is not tuple or len(row) != n
                       or any(type(i) is not int or not 0 <= i < n for i in row)
                       for row in self.transitions)):
            raise ObserverError("Require immutable, total, exactly typed finite data")

    def run(self, state: int, word: tuple[str, ...]) -> int:
        _state(self, state)
        if type(word) is not tuple or any(type(a) is not str or a not in self.actions for a in word):
            raise ObserverError("Word outside declared action alphabet")
        for a in word:
            state = self.transitions[self.actions.index(a)][state]
        return state


def _state(model, state):
    if type(model) is not FiniteObserver or type(state) is not int or not 0 <= state < len(model.states):
        raise ObserverError("State outside exact finite model")


def _compatible(left, right):
    if (type(left) is not FiniteObserver or type(right) is not FiniteObserver
            or left.actions != right.actions or left.basis != right.basis):
        raise ObserverError("Declare a common ordered action and output interface")


@dataclass(frozen=True)
class DistinguishingWord:
    left: FiniteObserver
    right: FiniteObserver
    initial: tuple[int, int]
    word: tuple[str, ...]


@dataclass(frozen=True)
class ClosedRelation:
    left: FiniteObserver
    right: FiniteObserver
    initial: tuple[int, int]
    pairs: tuple[tuple[int, int], ...]


def _initial(cert):
    if type(cert.initial) is not tuple or len(cert.initial) != 2:
        raise ObserverError("Expected exactly two initial states")
    _state(cert.left, cert.initial[0])
    _state(cert.right, cert.initial[1])


def verify_certificate(left: FiniteObserver, right: FiniteObserver,
                       cert: DistinguishingWord | ClosedRelation) -> bool:
    """Independent final checker: exact model binding plus witness/closure laws.

    A valid difference certifies its supplied word, not shortestness.  A valid
    closed relation proves agreement for all words by the Lean closure theorem.
    Running Python does not itself confer installed formal proof authority.
    """
    _compatible(left, right)
    if type(cert) not in (DistinguishingWord, ClosedRelation):
        raise ObserverError("Unknown certificate type")
    if cert.left != left or cert.right != right:
        raise ObserverError("Certificate is bound to different exact models")
    _initial(cert)
    x, y = cert.initial
    if type(cert) is DistinguishingWord:
        return left.outputs[left.run(x, cert.word)] != right.outputs[right.run(y, cert.word)]
    if (type(cert.pairs) is not tuple
            or any(type(p) is not tuple or len(p) != 2 for p in cert.pairs)):
        raise ObserverError("Expected an immutable relation table")
    for a, b in cert.pairs:
        _state(left, a)
        _state(right, b)
    relation = set(cert.pairs)
    if len(relation) != len(cert.pairs) or cert.initial not in relation:
        return False
    return all(left.outputs[a] == right.outputs[b]
               and all((lt[a], rt[b]) in relation
                       for lt, rt in zip(left.transitions, right.transitions))
               for a, b in relation)


def distinguish(left: FiniteObserver, right: FiniteObserver, x: int, y: int,
                *, max_pairs: int | None = None) -> DistinguishingWord | ClosedRelation:
    """BFS returns a shortest distinguishing word or a complete closed relation.

    At most |X|*|Y| pairs are inserted; a shortest witness has length at most
    |X|*|Y|-1.  Resource exhaustion raises; it never certifies equivalence.
    """
    _compatible(left, right)
    _state(left, x)
    _state(right, y)
    if max_pairs is None:
        max_pairs = len(left.states) * len(right.states)
    if type(max_pairs) is not int or max_pairs < 1:
        raise ObserverError("Positive exact pair budget required")
    queue = deque([((x, y), ())])
    seen = {(x, y)}
    while queue:
        (a, b), word = queue.popleft()
        if left.outputs[a] != right.outputs[b]:
            return DistinguishingWord(left, right, (x, y), word)
        for action, lt, rt in zip(left.actions, left.transitions, right.transitions):
            pair = (lt[a], rt[b])
            if pair not in seen:
                if len(seen) >= max_pairs:
                    raise ProbeBudgetExceeded("No complete verdict within pair budget")
                seen.add(pair)
                queue.append((pair, word + (action,)))
    return ClosedRelation(left, right, (x, y), tuple(sorted(seen)))


def is_morphism(source: FiniteObserver, target: FiniteObserver,
                projection: tuple[int, ...], *, onto: bool = False) -> bool:
    _compatible(source, target)
    if (type(projection) is not tuple or len(projection) != len(source.states)
            or any(type(i) is not int or not 0 <= i < len(target.states) for i in projection)
            or type(onto) is not bool):
        raise ObserverError("Projection must be an exact total finite map")
    if onto and set(projection) != set(range(len(target.states))):
        return False
    return (all(source.outputs[i] == target.outputs[j] for i, j in enumerate(projection))
            and all(projection[st[i]] == tt[projection[i]]
                    for st, tt in zip(source.transitions, target.transitions)
                    for i in range(len(source.states))))


def _partition(signatures):
    names = {}
    return tuple(names.setdefault(s, len(names)) for s in signatures)


@dataclass(frozen=True)
class ObservableQuotient:
    source: FiniteObserver
    target: FiniteObserver
    projection: tuple[int, ...]
    classes: tuple[tuple[int, ...], ...]
    strict_refinements: int


def observable_quotient(source: FiniteObserver) -> ObservableQuotient:
    """Coarsest observation-preserving action congruence by finite refinement.

    This is a deterministic Moore observer, the total stationary specialization
    of SUCC's existing partial/cost-aware source interfaces.  Empty carriers and
    empty action alphabets have their literal mathematical meanings here.
    """
    if type(source) is not FiniteObserver:
        raise ObserverError("Exact finite observer required")
    labels = _partition(source.outputs)
    strict = 0
    while True:
        new = _partition((labels[i], tuple(labels[tr[i]] for tr in source.transitions))
                         for i in range(len(source.states)))
        if new == labels:
            break
        strict += 1
        labels = new
    classes = tuple(tuple(i for i, q in enumerate(labels) if q == k)
                    for k in range(len(set(labels))))
    reps = tuple(c[0] for c in classes)
    target = FiniteObserver(source.source_id + "/observable-quotient", source.epoch,
                            source.basis, tuple("q" + str(i) for i in range(len(classes))),
                            source.actions,
                            tuple(tuple(labels[tr[i]] for i in reps) for tr in source.transitions),
                            tuple(source.outputs[i] for i in reps))
    if not is_morphism(source, target, labels, onto=True):
        raise ArithmeticError("Refinement did not produce an exact quotient")
    return ObservableQuotient(source, target, labels, classes, strict)


@dataclass(frozen=True)
class CommonObservableFactor:
    left: FiniteObserver
    right: FiniteObserver
    common: FiniteObserver
    left_projection: tuple[int, ...]
    right_projection: tuple[int, ...]


def common_observable_factor(left: FiniteObserver, right: FiniteObserver,
                             *, require_nontrivial: bool = True) -> CommonObservableFactor | None:
    """Find the common separated observable quotient, with BOTH maps onto.

    Nontrivial means at least two behaviorally distinguishable common states.
    None does not rule out a hidden nonseparated common factor or a different
    output interface.  The trivial erased factor is explicitly rejected by default.
    """
    _compatible(left, right)
    if type(require_nontrivial) is not bool:
        raise ObserverError("Boolean nontriviality policy required")
    lq, rq = observable_quotient(left), observable_quotient(right)
    if len(lq.classes) != len(rq.classes) or (require_nontrivial and len(lq.classes) < 2):
        return None
    match = []
    for i in range(len(rq.classes)):
        choices = [j for j in range(len(lq.classes))
                   if type(distinguish(rq.target, lq.target, i, j)) is ClosedRelation]
        if len(choices) != 1:
            return None
        match.append(choices[0])
    rp = tuple(match[i] for i in rq.projection)
    if not is_morphism(right, lq.target, rp, onto=True):
        raise ArithmeticError("Behavioral match failed common-factor laws")
    return CommonObservableFactor(left, right, lq.target, lq.projection, rp)


def from_causal_endo(chart, instruments: tuple) -> FiniteObserver:
    """Reuse SourceChart/CausalInstrument, only on a fixed stationary chart.

    Time-changing charts cannot be silently interpreted as autonomous actions.
    Only the constant unit-cost slice is accepted; no variable costs are erased.
    No reset availability is inferred by this mathematical adapter.
    """
    from .causal_nerode_succ import SourceChart, CausalInstrument
    if (type(chart) is not SourceChart or type(instruments) is not tuple
            or any(type(a) is not CausalInstrument or a.before != chart or a.after != chart or a.cost != 1
                   for a in instruments)):
        raise ObserverError("Require actual endomorphisms of one fixed source chart")
    return FiniteObserver(chart.source_id, chart.epoch, chart.basis, chart.states,
                          tuple(a.name for a in instruments),
                          tuple(tuple(chart.states.index(a.step(s)) for s in chart.states)
                                for a in instruments), chart.observations)


def as_eos_morphism(source: FiniteObserver, target: FiniteObserver,
                    projection: tuple[int, ...], *, target_id: str):
    """Refine a checked onto morphism into the existing EOS coalgebra interface.

    Outputs encode post-state readouts in ONE shared alphabet; current readouts
    remain the original-source target table.  EOS's 1..128/nonempty-menu domain
    is respected.  The adapter transports declared laws, not physical identity.
    """
    from .noncommuting_proof_transport import FiniteCarrier, Instrument
    from .operational_yoneda_descent import CertifiedSourceMorphism
    if not is_morphism(source, target, projection, onto=True):
        raise ObserverError("Existing EOS adapter requires an onto observed morphism")
    alphabet = tuple(sorted(set(source.outputs + target.outputs)))
    def carrier(m):
        return FiniteCarrier(len(m.states), tuple(
            Instrument(a, tuple(alphabet.index(m.outputs[j]) for j in row), row,
                       (True,) * len(m.states)) for a, row in zip(m.actions, m.transitions)),
            m.source_id + "/epoch=" + str(m.epoch), m.basis)
    result = CertifiedSourceMorphism(carrier(source), carrier(target),
                                     tuple(range(len(source.states))), tuple(range(len(target.states))),
                                     projection, source.outputs, target.outputs, target_id)
    result.verify()
    return result
