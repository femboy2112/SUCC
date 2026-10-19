"""Exact partial-source descent and certificates for one consistent history.

This is a declared finite deterministic model. ``source_id``/``basis`` identify
the model, and ``original`` is immutable *private* source metadata. No real
sensor, performed event, probability distribution or coupling is manufactured.
The public-safe transcript audit is separate from existential path support.
"""
from __future__ import annotations

from dataclasses import dataclass
from collections import deque
from fractions import Fraction as Q
from types import MappingProxyType
from typing import Mapping


class CausalError(ValueError):
    """A malformed source declaration or certificate request."""


def _name(value):
    return type(value) is str and bool(value)


def _cost(value):
    if type(value) not in (int, Q) or value < 0:
        raise CausalError("Cost must be a nonnegative exact int/Fraction")
    return Q(value)


@dataclass(frozen=True)
class Step:
    target: str
    outcome: str
    cost: Q

    def __post_init__(self):
        if not _name(self.target) or not _name(self.outcome):
            raise CausalError("Named target and public outcome required")
        object.__setattr__(self, "cost", _cost(self.cost))


@dataclass(frozen=True)
class SourceSystem:
    source_id: str
    basis: str
    states: tuple[str, ...]
    actions: tuple[str, ...]
    original: Mapping[str, str]
    observation: Mapping[str, str]
    transitions: Mapping[tuple[str, str], Step]

    def __post_init__(self):
        if not _name(self.source_id) or not _name(self.basis):
            raise CausalError("Explicit source ID and basis required")
        for seq in (self.states, self.actions):
            if (type(seq) is not tuple or not seq or
                    any(not _name(s) for s in seq) or len(set(seq)) != len(seq)):
                raise CausalError("Nonempty distinct named carrier/actions required")
        for name in ("original", "observation"):
            data = dict(getattr(self, name))
            if set(data) != set(self.states) or any(not _name(v) for v in data.values()):
                raise CausalError("Total source metadata and observations required")
            object.__setattr__(self, name, MappingProxyType(data))
        transitions = dict(self.transitions)
        for key, edge in transitions.items():
            if (type(key) is not tuple or len(key) != 2 or
                    key[0] not in self.states or key[1] not in self.actions or
                    type(edge) is not Step or edge.target not in self.states):
                raise CausalError("Transition outside declared carrier/grammar")
            if self.original[key[0]] != self.original[edge.target]:
                raise CausalError("Transition changes immutable original source")
        object.__setattr__(self, "transitions", MappingProxyType(transitions))


@dataclass(frozen=True)
class ReportStep:
    action: str
    outcome: str
    cost: Q
    observation: str

    def __post_init__(self):
        if any(not _name(v) for v in (self.action, self.outcome, self.observation)):
            raise CausalError("Named action/outcome/observation required")
        object.__setattr__(self, "cost", _cost(self.cost))


def _request(model, initial, transcript):
    if type(initial) is not frozenset or not initial <= set(model.states):
        raise CausalError("Initial support must be a frozenset of declared states")
    if (type(transcript) is not tuple or any(type(r) is not ReportStep or
            r.action not in model.actions for r in transcript)):
        raise CausalError("Transcript must use the declared public probe grammar")


def _match(model, state, report):
    edge = model.transitions.get((state, report.action))
    if (edge is not None and edge.outcome == report.outcome and
            edge.cost == report.cost and
            model.observation[edge.target] == report.observation):
        return edge.target
    return None


@dataclass(frozen=True)
class QuotientAudit:
    lawful: bool
    reason: str
    witness: tuple[str, str, str | None] | None = None


def audit_quotient(model: SourceSystem, quotient: Mapping[str, str]) -> QuotientAudit:
    """Necessary/sufficient finite criterion; image of q is the target carrier.

    Current observations must descend, and each partial labelled action must
    be constant after projection on every complete q-fiber. Original labels
    remain private path metadata; no public access to them is assumed.
    """
    q = dict(quotient)
    if set(q) != set(model.states) or any(not _name(v) for v in q.values()):
        raise CausalError("A total quotient map on the exact carrier is required")
    for i, s in enumerate(model.states):
        for t in model.states[i + 1:]:
            if q[s] != q[t]:
                continue
            if model.observation[s] != model.observation[t]:
                return QuotientAudit(False, "CURRENT_REPORT_LOSS", (s, t, None))
            for action in model.actions:
                left = model.transitions.get((s, action))
                right = model.transitions.get((t, action))
                if (left is None) != (right is None):
                    return QuotientAudit(False, "AVAILABILITY_LOSS", (s, t, action))
                if left is None:
                    continue
                if (left.outcome, left.cost) != (right.outcome, right.cost):
                    return QuotientAudit(False, "LABEL_OR_COST_LOSS", (s, t, action))
                if q[left.target] != q[right.target]:
                    return QuotientAudit(False, "FUTURE_FIBER_LOSS", (s, t, action))
    return QuotientAudit(True, "ALL_FIBERS_CONGRUENT")


def source_run(model: SourceSystem, state: str, word: tuple[str, ...]):
    """Return retained public labels and actual endpoint, or unavailable None."""
    if state not in model.states or type(word) is not tuple or not set(word) <= set(model.actions):
        raise CausalError("Run outside source carrier/grammar")
    labels = []
    for action in word:
        edge = model.transitions.get((state, action))
        if edge is None:
            return None
        labels.append((edge.outcome, edge.cost))
        state = edge.target
    return tuple(labels), state


def distinguishing_word(model: SourceSystem, left: str, right: str):
    """Shortest differing finite experiment by complete pair-graph BFS.

    None means the finite declared pair graph was exhausted, not that a finite
    physical observation proves a theorem about an unknown/infinite source.
    Each returned action word distinguishes a current report, availability,
    public outcome or exact cost. Private original-state labels are not probes.
    """
    if left not in model.states or right not in model.states:
        raise CausalError("Pair outside declared carrier")
    pending = deque([(left, right, ())])
    seen = {(left, right)}
    while pending:
        s, t, prefix = pending.popleft()
        if model.observation[s] != model.observation[t]:
            return prefix
        for action in model.actions:
            a = model.transitions.get((s, action))
            b = model.transitions.get((t, action))
            if (a is None) != (b is None):
                return prefix + (action,)
            if a is None:
                continue
            if ((a.outcome, a.cost, model.observation[a.target]) !=
                    (b.outcome, b.cost, model.observation[b.target])):
                return prefix + (action,)
            pair = (a.target, b.target)
            if pair not in seen:
                seen.add(pair)
                pending.append((*pair, prefix + (action,)))
    return None


def refine_quotient(model: SourceSystem):
    """Complete finite counterexample-guided Moore refinement.

    Returns the coarsest lawful refinement of current public observations and
    one actual distinguishing word for each failed intermediate quotient.
    Termination is by a strictly increasing number of finite partition blocks.
    The BFS witness engine is independent of the partition-update algorithm.
    """
    quotient = dict(model.observation)
    failures = []
    while True:
        audit = audit_quotient(model, quotient)
        if audit.lawful:
            return MappingProxyType(quotient), tuple(failures)
        s, t, _ = audit.witness
        witness = distinguishing_word(model, s, t)
        if witness is None:
            raise AssertionError("Finite quotient failure lacks an observable separator")
        failures.append((s, t, witness))
        signatures, refined = {}, {}
        for state in model.states:
            row = []
            for action in model.actions:
                edge = model.transitions.get((state, action))
                row.append(None if edge is None else
                           (edge.outcome, edge.cost, quotient[edge.target]))
            signature = quotient[state], tuple(row)
            signatures.setdefault(signature, "class_" + str(len(signatures)))
            refined[state] = signatures[signature]
        if len(set(refined.values())) <= len(set(quotient.values())):
            raise AssertionError("A noncongruent partition must strictly refine")
        quotient = refined


@dataclass(frozen=True)
class HistoryCertificate:
    status: str
    source_id: str
    basis: str
    path: tuple[str, ...] | None = None
    excluded: tuple[frozenset[str], ...] | None = None


def forward_history_oracle(model: SourceSystem, initial: frozenset[str],
                           transcript: tuple[ReportStep, ...]) -> HistoryCertificate:
    """Construct one complete source path, or return NO_PATH without a proof.

    Failure gets independent certification from ``backward_exclusion_oracle``.
    Search has no numeric tolerances and never guesses a missing source state.
    """
    _request(model, initial, transcript)
    paths = {s: (s,) for s in model.states if s in initial}
    for report in transcript:
        following = {}
        for state, path in paths.items():
            target = _match(model, state, report)
            if target is not None:
                following.setdefault(target, path + (target,))
        paths = following
    if paths:
        path = next(iter(paths.values()))
        return HistoryCertificate("SOURCE_HISTORY_EXISTS", model.source_id, model.basis, path=path)
    return HistoryCertificate("NO_PATH_FOUND", model.source_id, model.basis)


def backward_exclusion_oracle(model: SourceSystem, initial: frozenset[str],
                              transcript: tuple[ReportStep, ...]) -> HistoryCertificate:
    """Independent backward algorithm constructing a universal exclusion cut.

    C_m is empty. C_i contains a state if there is no matching edge, or its
    matching successor lies in C_(i+1). I subset C_0 certifies impossibility.
    This is a logical dual certificate, not a probabilistic/Farkas dual.
    """
    _request(model, initial, transcript)
    cuts = [frozenset()]
    for report in reversed(transcript):
        excluded = set()
        for state in model.states:
            edge = model.transitions.get((state, report.action))
            if (edge is None or edge.outcome != report.outcome or
                    edge.cost != report.cost or
                    model.observation[edge.target] != report.observation or
                    edge.target in cuts[-1]):
                excluded.add(state)
        cuts.append(frozenset(excluded))
    cuts.reverse()
    if initial <= cuts[0]:
        return HistoryCertificate("SOURCE_HISTORY_IMPOSSIBLE", model.source_id, model.basis,
                                  excluded=tuple(cuts))
    return HistoryCertificate("NOT_EXCLUDED", model.source_id, model.basis)


def verify_history_certificate(model: SourceSystem, initial: frozenset[str],
                               transcript: tuple[ReportStep, ...],
                               certificate: HistoryCertificate) -> bool:
    """Check raw edges/cuts directly; neither search routine is trusted."""
    try:
        _request(model, initial, transcript)
        if (type(certificate) is not HistoryCertificate or
                certificate.source_id != model.source_id or certificate.basis != model.basis):
            return False
        if certificate.status == "SOURCE_HISTORY_EXISTS":
            path = certificate.path
            if (certificate.excluded is not None or type(path) is not tuple or
                    len(path) != len(transcript) + 1 or path[0] not in initial or
                    any(s not in model.states for s in path)):
                return False
            for before, after, report in zip(path, path[1:], transcript):
                edge = model.transitions.get((before, report.action))
                if (edge is None or edge.target != after or edge.outcome != report.outcome or
                        edge.cost != report.cost or model.observation[after] != report.observation or
                        model.original[before] != model.original[after]):
                    return False
            return True
        if certificate.status == "SOURCE_HISTORY_IMPOSSIBLE":
            cuts = certificate.excluded
            if (certificate.path is not None or type(cuts) is not tuple or
                    len(cuts) != len(transcript) + 1 or
                    any(type(c) is not frozenset or not c <= set(model.states) for c in cuts) or
                    cuts[-1] or not initial <= cuts[0]):
                return False
            for i, report in enumerate(transcript):
                for state in cuts[i]:
                    edge = model.transitions.get((state, report.action))
                    if (edge is not None and edge.outcome == report.outcome and
                            edge.cost == report.cost and
                            model.observation[edge.target] == report.observation and
                            edge.target not in cuts[i + 1]):
                        return False
            return True
        return False
    except (CausalError, TypeError, AttributeError, KeyError):
        return False


@dataclass(frozen=True)
class PublicAudit:
    status: str
    at_step: int | None = None
    witness_path: tuple[str, ...] | None = None


def audit_public_transcript(model: SourceSystem, initial: frozenset[str],
                            transcript: tuple[ReportStep, ...]) -> PublicAudit:
    """Audit one possible branch of a public policy allowed to stop off-branch.

    Before each requested action, it must be available at EVERY state compatible
    with the complete public prefix. A future report cannot erase an unsafe
    choice. This is not synthesis of a total fixed-horizon policy on all branches.
    """
    _request(model, initial, transcript)
    if len({model.observation[s] for s in initial}) > 1:
        raise CausalError("A public decision starts from one observation fiber")
    paths = {s: (s,) for s in model.states if s in initial}
    if not paths:
        return PublicAudit("IMPOSSIBLE_PREFIX", 0)
    for i, report in enumerate(transcript):
        for state, path in paths.items():
            if (state, report.action) not in model.transitions:
                return PublicAudit("PUBLIC_ACTION_UNAVAILABLE", i, path)
        following = {}
        for state, path in paths.items():
            target = _match(model, state, report)
            if target is not None:
                following.setdefault(target, path + (target,))
        paths = following
        if not paths:
            return PublicAudit("IMPOSSIBLE_PREFIX", i + 1)
    return PublicAudit("SAFE_POSSIBLE_TRANSCRIPT", witness_path=next(iter(paths.values())))


def splice_counterexample():
    """An acyclic two-edge PUBLIC report chain with no global source lift.

    a: left0 -> left1 and b: right1 -> right2. Both middle states report
    'middle', but neither is the other. Original-source tags cannot be reset.
    """
    model = SourceSystem(
        "institute-hidden-source-splice-v1", "immutable-root-and-public-report",
        ("left0", "left1", "right1", "right2"), ("a", "b"),
        {"left0": "L", "left1": "L", "right1": "R", "right2": "R"},
        {"left0": "start", "left1": "middle", "right1": "middle", "right2": "end"},
        {("left0", "a"): Step("left1", "ok", 1),
         ("right1", "b"): Step("right2", "ok", 1)})
    transcript = (ReportStep("a", "ok", 1, "middle"), ReportStep("b", "ok", 1, "end"))
    return model, frozenset({"left0"}), transcript
