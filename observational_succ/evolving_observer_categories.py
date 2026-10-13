"""Counterexamples that construct experiments and minimal dynamical quotients.

The complete finite carrier is an explicitly declared mathematical source,
not authenticated physical data. Exact closure certificates quantify over that
whole source; sampled checks receive a different status. The object language
(words/observations/quotients) grows, but the composition metagrammar is fixed.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
from random import Random
from typing import Hashable, Iterable


class SynthesisError(ValueError):
    """Ill-typed source, stale certificate, unsound exclusion, or resource cap."""


def partition(values: Iterable[Hashable]) -> tuple[int, ...]:
    """Canonical quotient labels; no metric or arithmetic on source labels."""
    codes: dict[Hashable, int] = {}
    answer = []
    for value in values:
        try:
            hash(value)
        except TypeError as exc:
            raise SynthesisError('Observation values must be hashable') from exc
        if value not in codes:
            codes[value] = len(codes)
        answer.append(codes[value])
    return tuple(answer)


def refines(fine: tuple[int, ...], coarse: tuple[int, ...]) -> bool:
    if len(fine) != len(coarse):
        raise SynthesisError('Partitions need the same declared source')
    seen = {}
    for x, y in zip(fine, coarse):
        if x in seen and seen[x] != y:
            return False
        seen[x] = y
    return True


@dataclass(frozen=True)
class Action:
    name: str
    after: tuple[int, ...]


@dataclass(frozen=True)
class Readout:
    name: str
    values: tuple[Hashable, ...]


@dataclass(frozen=True)
class FiniteDynamics:
    source_id: str
    version: int
    basis_id: str
    actions: tuple[Action, ...]
    readouts: tuple[Readout, ...]

    def __post_init__(self):
        if not self.source_id or not self.basis_id or type(self.version) is not int or self.version < 0:
            raise SynthesisError('Source, version, and basis are mandatory')
        if not self.actions or not self.readouts:
            raise SynthesisError('Nonempty action and observation signatures required')
        n = len(self.readouts[0].values)
        if not 1 <= n <= 1024:
            raise SynthesisError('Finite carrier audit bound is 1..1024 states')
        if len({a.name for a in self.actions}) != len(self.actions) or len({r.name for r in self.readouts}) != len(self.readouts):
            raise SynthesisError('Generator/readout names must be distinct')
        for a in self.actions:
            if not a.name or type(a.after) is not tuple or len(a.after) != n or any(type(x) is not int or not 0 <= x < n for x in a.after):
                raise SynthesisError('Action must be a total typed finite source map')
        for r in self.readouts:
            if not r.name or type(r.values) is not tuple or len(r.values) != n:
                raise SynthesisError('Readout must cover the source exactly')
            partition(r.values)

    @property
    def count(self):
        return len(self.readouts[0].values)

    @property
    def digest(self):
        # JSON primitive source descriptions, not external identity attestation.
        payload = [self.source_id, self.version, self.basis_id,
                   [(a.name, a.after) for a in self.actions],
                   [(r.name, [repr(x) for x in r.values]) for r in self.readouts]]
        return sha256(json.dumps(payload, separators=(',', ':')).encode()).hexdigest()

    def act(self, name: str) -> Action:
        for a in self.actions:
            if a.name == name:
                return a
        raise SynthesisError('Unauthorized source action: ' + name)

    def read(self, name: str) -> Readout:
        for r in self.readouts:
            if r.name == name:
                return r
        raise SynthesisError('Unauthorized source observation: ' + name)

    def run(self, state: int, word: tuple[str, ...]) -> int:
        if type(state) is not int or not 0 <= state < self.count:
            raise SynthesisError('Undeclared source preparation')
        for name in word:
            state = self.act(name).after[state]
        return state


@dataclass(frozen=True)
class Experiment:
    """Execute word left-to-right, then read; a proposed experiment is not a receipt."""
    word: tuple[str, ...]
    readout: str

    def values(self, source: FiniteDynamics) -> tuple[Hashable, ...]:
        read = source.read(self.readout).values
        return tuple(read[source.run(s, self.word)] for s in range(source.count))

    @property
    def cost(self):
        return 1 + len(self.word)


def observed_partition(source: FiniteDynamics, tests: tuple[Experiment, ...]) -> tuple[int, ...]:
    columns = tuple(t.values(source) for t in tests)
    return partition(tuple(c[s] for c in columns) for s in range(source.count))


@dataclass(frozen=True)
class SeparationWitness:
    source_digest: str
    left: int
    right: int
    experiment: Experiment
    outcomes: tuple[Hashable, Hashable]

    def verify(self, source: FiniteDynamics) -> bool:
        if self.source_digest != source.digest:
            raise SynthesisError('Counterexample from a different source/toolkit epoch')
        if not (0 <= self.left < source.count and 0 <= self.right < source.count):
            raise SynthesisError('Counterexample states outside carrier')
        v = self.experiment.values(source)
        if (v[self.left], v[self.right]) != self.outcomes or self.outcomes[0] == self.outcomes[1]:
            raise SynthesisError('Forged separating experiment')
        return True


class ObstructionArchive:
    """Every rejection is a necessary separation in ALL valid dynamic repairs."""
    def __init__(self, source: FiniteDynamics):
        self.source = source
        self.witnesses: list[SeparationWitness] = []

    def learn(self, w: SeparationWitness):
        w.verify(self.source)
        if w not in self.witnesses:
            self.witnesses.append(w)

    def admits(self, labels: tuple[int, ...]) -> bool:
        if len(labels) != self.source.count:
            raise SynthesisError('Candidate quotient has wrong carrier')
        return all(labels[w.left] != labels[w.right] for w in self.witnesses)


def first_defect(source: FiniteDynamics, tests: tuple[Experiment, ...]) -> SeparationWitness | None:
    """A complete finite verification query, not a sample-based validity claim."""
    labels = observed_partition(source, tests)
    columns = tuple(t.values(source) for t in tests)
    for x in range(source.count):
        for y in range(x + 1, source.count):
            if labels[x] != labels[y]:
                continue
            for r in source.readouts:
                if r.values[x] != r.values[y]:
                    return SeparationWitness(source.digest, x, y, Experiment((), r.name),
                                             (r.values[x], r.values[y]))
            for a in source.actions:
                if labels[a.after[x]] != labels[a.after[y]]:
                    for t, c in zip(tests, columns):
                        if c[a.after[x]] != c[a.after[y]]:
                            probe = Experiment((a.name,) + t.word, t.readout)
                            return SeparationWitness(source.digest, x, y, probe,
                                                     (c[a.after[x]], c[a.after[y]]))
                    raise AssertionError('Partition differs without a distinguishing coordinate')
    return None


@dataclass(frozen=True)
class QuotientCertificate:
    source_digest: str
    tests: tuple[Experiment, ...]
    labels: tuple[int, ...]
    actions: tuple[Action, ...]
    readouts: tuple[Readout, ...]
    witnesses: tuple[SeparationWitness, ...]
    block_counts: tuple[int, ...]
    candidate_trace: tuple[tuple[int, bool], ...]

    @property
    def states(self):
        return len(set(self.labels))


def _quotient_tables(source, labels):
    representatives = [labels.index(j) for j in range(len(set(labels)))]
    actions = tuple(Action(a.name, tuple(labels[a.after[x]] for x in representatives)) for a in source.actions)
    readouts = tuple(Readout(r.name, tuple(r.values[x] for x in representatives)) for r in source.readouts)
    return actions, readouts


def discover_representation(source: FiniteDynamics, *, seed: int = 0,
                            proposal_audits: int = 8, max_refinements: int = 1024) -> QuotientCertificate:
    """Stochastic test-subset audits + persistent no-goods + complete refinement.

    The audits measure pruning only; the refinement policy is deterministic.
    Counterexample-guided genetic bridge search is a separate module. A defect prepends
    an action to a known readout word, growing the test language. Any final result
    is the coarsest action-stable refinement of the initial readout partition.
    The fallback is deterministic and is NOT counted as genetic success.
    """
    if type(seed) is not int or not 0 <= proposal_audits <= 100 or not 0 <= max_refinements <= 1024:
        raise SynthesisError('Finite reproducible search budget required')
    tests = tuple(Experiment((), r.name) for r in source.readouts)
    archive = ObstructionArchive(source)
    initial = observed_partition(source, tests)
    counts = [len(set(initial))]
    trace = []
    rng = Random(seed)
    while True:
        # Diagnostic candidate masks operate on semantic test genes; the archive forbids
        # forgetting a distinction already proved to be required.
        for _ in range(proposal_audits):
            candidate = tuple(t for t in tests if rng.randrange(2))
            q = observed_partition(source, candidate)
            trace.append((len(candidate), archive.admits(q) and refines(q, initial)))
        bad = first_defect(source, tests)
        if bad is None:
            labels = observed_partition(source, tests)
            actions, reads = _quotient_tables(source, labels)
            result = QuotientCertificate(source.digest, tests, labels, actions, reads,
                                         tuple(archive.witnesses), tuple(counts), tuple(trace))
            verify_quotient(source, result)
            return result
        if len(archive.witnesses) >= max_refinements:
            raise SynthesisError('UNRESOLVED_REFINEMENT_BUDGET: no impossibility theorem')
        archive.learn(bad)
        before = observed_partition(source, tests)
        tests = tests + (bad.experiment,)
        after = observed_partition(source, tests)
        if not refines(after, before) or len(set(after)) <= counts[-1] or not archive.admits(after):
            raise AssertionError('Repair must preserve all learned necessities and strictly refine')
        counts.append(len(set(after)))


def verify_quotient(source: FiniteDynamics, q: QuotientCertificate) -> bool:
    """Independent EDGE checks plus independent pair-automaton minimality oracle."""
    if q.source_digest != source.digest or len(q.labels) != source.count:
        raise SynthesisError('Certificate source fingerprint mismatch')
    if partition(q.labels) != q.labels or observed_partition(source, q.tests) != q.labels:
        raise SynthesisError('Wrong or fabricated quotient labels')
    expected_a, expected_o = _quotient_tables(source, q.labels)
    if q.actions != expected_a or q.readouts != expected_o:
        raise SynthesisError('Wrong descended generator tables')
    for a, a2 in zip(source.actions, q.actions):
        if any(q.labels[a.after[x]] != a2.after[q.labels[x]] for x in range(source.count)):
            raise SynthesisError('Action square does not commute')
    for r, r2 in zip(source.readouts, q.readouts):
        if any(r.values[x] != r2.values[q.labels[x]] for x in range(source.count)):
            raise SynthesisError('Readout meaning not preserved')
    initial = tuple(Experiment((), r.name) for r in source.readouts)
    if q.tests[:len(initial)] != initial:
        raise SynthesisError('Primitive readout seeds were altered')
    for i, w in enumerate(q.witnesses):
        w.verify(source)
        before = observed_partition(source, q.tests[:len(initial)+i])
        if q.tests[len(initial)+i] != w.experiment or before[w.left] != before[w.right]:
            raise SynthesisError('Counterexample did not justify this grammar expansion')
    actual_counts = tuple(len(set(observed_partition(source, q.tests[:len(source.readouts)+i])))
                          for i in range(len(q.witnesses)+1))
    if q.block_counts != actual_counts or len(q.tests) != len(source.readouts)+len(q.witnesses):
        raise SynthesisError('Invalid discovery/complexity receipt')
    if any(b <= a for a, b in zip(q.block_counts, q.block_counts[1:])):
        raise SynthesisError('Nonprogressing refinement')
    oracle = pair_automaton_partition(source)
    if q.labels != oracle:
        raise SynthesisError('Quotient sufficient but not minimal, or missing future behavior')
    return True


def pair_automaton_partition(source: FiniteDynamics) -> tuple[int, ...]:
    """Different implementation: backwards reachability of separating state pairs."""
    n = source.count
    pairs = [(x, y) for x in range(n) for y in range(x+1, n)]
    predecessors: dict[tuple[int, int], list[tuple[int, int]]] = {}
    bad = {p for p in pairs if any(r.values[p[0]] != r.values[p[1]] for r in source.readouts)}
    todo = deque(sorted(bad))
    for p in pairs:
        for a in source.actions:
            x, y = sorted((a.after[p[0]], a.after[p[1]]))
            if x != y:
                predecessors.setdefault((x, y), []).append(p)
    while todo:
        p = todo.popleft()
        for other in predecessors.get(p, ()):
            if other not in bad:
                bad.add(other)
                todo.append(other)
    labels = []
    for x in range(n):
        equivalent = next((y for y in range(x) if (y, x) not in bad), None)
        labels.append(labels[equivalent] if equivalent is not None else max(labels, default=-1)+1)
    return tuple(labels)


def factor_map(fine: tuple[int, ...], coarse: tuple[int, ...]) -> tuple[int, ...]:
    """Unique natural comparison map q_fine -> q_coarse on reachable classes."""
    fine, coarse = partition(fine), partition(coarse)
    if not refines(fine, coarse):
        raise SynthesisError('Requested natural transformation does not factor')
    return tuple(coarse[fine.index(k)] for k in range(len(set(fine))))


def join_partitions(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    if len(a) != len(b):
        raise SynthesisError('Shared-source product requires same carrier')
    return partition(zip(a, b))


def existential_image(mapping: tuple[int, ...], subset: frozenset[int]) -> frozenset[int]:
    if any(type(i) is not int or not 0 <= i < len(mapping) for i in subset):
        raise SynthesisError('Predicate outside source')
    return frozenset(mapping[i] for i in subset)


def predicate_pullback(mapping: tuple[int, ...], subset: frozenset[int]) -> frozenset[int]:
    return frozenset(i for i, value in enumerate(mapping) if value in subset)


def adjunction_holds(mapping, source_predicate, target_predicate) -> bool:
    """Finite powerset adjunction exists_image ⊣ preimage, actually computed."""
    left = existential_image(mapping, source_predicate) <= target_predicate
    right = source_predicate <= predicate_pullback(mapping, target_predicate)
    return left == right


def transformation_monoid(q: QuotientCertificate, *, max_elements: int = 4096) -> dict:
    """Invent the finite action-composition table from learned generator maps.

    No commutativity, group law, or family-specific invariant is supplied.
    The multiplication below means execute the left word then the right word.
    """
    identity = tuple(range(q.states))
    elements = {identity: ()}
    todo = deque([identity])
    while todo:
        f = todo.popleft()
        for a in q.actions:
            composed = tuple(a.after[f[x]] for x in range(q.states))
            if composed not in elements:
                if len(elements) >= max_elements:
                    raise SynthesisError('UNRESOLVED_MONOID_BUDGET')
                elements[composed] = elements[f] + (a.name,)
                todo.append(composed)
    permutations = all(len(set(f)) == q.states for f in elements)
    inverses = {}
    if permutations:
        for f in elements:
            inv = tuple(f.index(i) for i in range(q.states))
            if inv not in elements:
                raise AssertionError('Finite permutation monoid must contain inverses')
            inverses[f] = inv
    center = tuple(f for f in elements if all(
        tuple(a.after[f[x]] for x in range(q.states)) == tuple(f[a.after[x]] for x in range(q.states))
        for a in q.actions))
    return {'elements': elements, 'center': center, 'is_group': permutations,
            'inverses': inverses, 'identity': identity}

@dataclass(frozen=True)
class PartialTransitionTable:
    """Partial exact observations of an assumed finite, addressable source.

    Each known transition is a simulator/experiment assertion. Exhausting a
    finite state/address domain is a model assumption, not physical attestation.
    Missing entries NEVER mean self-loops or impossible transitions.
    """
    source_id: str
    version: int
    basis_id: str
    state_count: int
    action_names: tuple[str, ...]
    readouts: tuple[Readout, ...]
    known: tuple[tuple[str, int, int], ...] = ()

    def __post_init__(self):
        if (not self.source_id or not self.basis_id or type(self.version) is not int or self.version < 0 or
                type(self.state_count) is not int or not 1 <= self.state_count <= 1024 or
                not self.action_names or len(set(self.action_names)) != len(self.action_names) or
                not self.readouts or any(len(r.values) != self.state_count for r in self.readouts)):
            raise SynthesisError('Partial source still needs typed domain and readout contracts')
        seen = set()
        for a, x, y in self.known:
            if a not in self.action_names or (a, x) in seen or any(type(z) is not int or not 0 <= z < self.state_count for z in (x, y)):
                raise SynthesisError('Contradictory/duplicate/malformed transition observation')
            seen.add((a, x))

    def next_unobserved_query(self) -> tuple[str, int] | None:
        seen = {(a, x) for a, x, _ in self.known}
        return next(((a, x) for a in self.action_names for x in range(self.state_count) if (a, x) not in seen), None)

    def compatible(self, candidate: FiniteDynamics) -> bool:
        if (candidate.source_id, candidate.version, candidate.basis_id, candidate.count) != (
                self.source_id, self.version, self.basis_id, self.state_count):
            raise SynthesisError('Candidate changed partial-source scope')
        if candidate.readouts != self.readouts or tuple(a.name for a in candidate.actions) != self.action_names:
            raise SynthesisError('Candidate changed experiment meaning')
        return all(candidate.act(a).after[x] == y for a, x, y in self.known)

    def completion(self) -> FiniteDynamics:
        if self.next_unobserved_query() is not None:
            raise SynthesisError('UNRESOLVED_PARTIAL_SOURCE: sampled checks are not universal certificates')
        table = {(a, x): y for a, x, y in self.known}
        return FiniteDynamics(self.source_id, self.version, self.basis_id,
            tuple(Action(a, tuple(table[a, x] for x in range(self.state_count))) for a in self.action_names), self.readouts)

    def remaining_completions(self) -> int:
        # Total deterministic action maps, no additional structural restrictions.
        return self.state_count ** (self.state_count*len(self.action_names)-len(self.known))
