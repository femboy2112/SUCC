"""Exact opaque-table discovery; no source-family formulas enter this module.

The supplied complete table is a mathematical oracle, not an empirical receipt.
Word growth and quotient/action-algebra constructors use a fixed metagrammar.
Counterexamples can refine representations but cannot manufacture instruments.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from typing import Hashable


class DiscoveryError(ValueError):
    pass


def partition(values):
    codes, labels = {}, []
    for value in values:
        try:
            hash(value)
        except TypeError as exc:
            raise DiscoveryError("Readouts must be hashable") from exc
        if value not in codes:
            codes[value] = len(codes)
        labels.append(codes[value])
    return tuple(labels)


@dataclass(frozen=True)
class TableSource:
    source_id: str
    actions: tuple[tuple[str, tuple[int, ...]], ...]
    readouts: tuple[tuple[Hashable, ...], ...]

    def __post_init__(self):
        if (not isinstance(self.source_id, str) or not self.source_id or
                type(self.actions) is not tuple or type(self.readouts) is not tuple or
                not self.actions or not self.readouts or
                any(type(a) is not tuple or len(a) != 2 or type(a[1]) is not tuple for a in self.actions) or
                any(type(r) is not tuple for r in self.readouts)):
            raise DiscoveryError("Declare source and nonempty signatures")
        n = len(self.readouts[0])
        if not 1 <= n <= 512 or len({a for a, _ in self.actions}) != len(self.actions):
            raise DiscoveryError("Finite distinct action signature required")
        for name, table in self.actions:
            if (not isinstance(name, str) or not name or len(table) != n or
                    any(type(x) is not int or not 0 <= x < n for x in table)):
                raise DiscoveryError("Action table must be total on declared carrier")
        if any(len(r) != n for r in self.readouts):
            raise DiscoveryError("Readout table must be total")
        for r in self.readouts:
            partition(r)

    @property
    def count(self):
        return len(self.readouts[0])

    @property
    def digest(self):
        return sha256(repr((self.source_id, self.actions, self.readouts)).encode()).hexdigest()

    def run(self, state, word):
        if type(state) is not int or not 0 <= state < self.count:
            raise DiscoveryError("Undeclared state")
        for action in word:
            if action not in dict(self.actions):
                raise DiscoveryError("Unlicensed action")
            state = dict(self.actions)[action][state]
        return state


@dataclass(frozen=True)
class Probe:
    word: tuple[str, ...]
    readout: int

    def values(self, source):
        if type(self.readout) is not int or not 0 <= self.readout < len(source.readouts):
            raise DiscoveryError("Unlicensed readout")
        return tuple(source.readouts[self.readout][source.run(x, self.word)]
                     for x in range(source.count))


@dataclass(frozen=True)
class DiscoveredQuotient:
    source_digest: str
    labels: tuple[int, ...]
    experiments: tuple[Probe, ...]
    actions: tuple[tuple[str, tuple[int, ...]], ...]
    readouts: tuple[tuple[Hashable, ...], ...]

    @property
    def count(self):
        return len(set(self.labels))


def shortest_separators(source):
    """Reverse pair-graph BFS constructs shortest word/readout separators.

    This is independent of sibling's incremental defect/test refinement.
    No coordinates, prime, order, commutator or target family are inputs.
    """
    predecessors, separating, todo = {}, {}, deque()
    for x in range(source.count):
        for y in range(x + 1, source.count):
            for r, table in enumerate(source.readouts):
                if table[x] != table[y]:
                    separating[x, y] = Probe((), r)
                    todo.append((x, y))
                    break
            for name, table in source.actions:
                a, b = sorted((table[x], table[y]))
                if a != b:
                    predecessors.setdefault((a, b), []).append(((x, y), name))
    while todo:
        pair = todo.popleft()
        for earlier, name in predecessors.get(pair, ()):
            if earlier not in separating:
                p = separating[pair]
                separating[earlier] = Probe((name,) + p.word, p.readout)
                todo.append(earlier)
    return separating


def discover_quotient(source):
    pairs = shortest_separators(source)
    experiments = tuple(dict.fromkeys([Probe((), r) for r in range(len(source.readouts))]
                                     + list(pairs.values())))
    columns = tuple(p.values(source) for p in experiments)
    labels = partition(tuple(column[x] for column in columns) for x in range(source.count))
    reps = tuple(labels.index(k) for k in range(len(set(labels))))
    q = DiscoveredQuotient(source.digest, labels, experiments,
        tuple((name, tuple(labels[table[x]] for x in reps)) for name, table in source.actions),
        tuple(tuple(table[x] for x in reps) for table in source.readouts))
    verify_quotient(source, q)
    return q


def verify_quotient(source, q):
    if q.source_digest != source.digest or len(q.labels) != source.count or partition(q.labels) != q.labels:
        raise DiscoveryError("Source, toolkit or canonical quotient changed")
    if tuple(name for name, _ in q.actions) != tuple(name for name, _ in source.actions):
        raise DiscoveryError("Action signature changed")
    if any(len(table) != q.count or any(type(x) is not int or not 0 <= x < q.count for x in table)
           for _, table in q.actions) or any(len(table) != q.count for table in q.readouts):
        raise DiscoveryError("Malformed quotient table")
    if len(q.readouts) != len(source.readouts):
        raise DiscoveryError("Readout signature changed")
    for (_, a), (_, b) in zip(source.actions, q.actions):
        if any(q.labels[a[x]] != b[q.labels[x]] for x in range(source.count)):
            raise DiscoveryError("Quotient action square fails")
    for a, b in zip(source.readouts, q.readouts):
        if any(a[x] != b[q.labels[x]] for x in range(source.count)):
            raise DiscoveryError("Readout does not descend")
    # Independent forward Moore refinement checks minimality, not merely stability.
    labels = partition(tuple(r[x] for r in source.readouts) for x in range(source.count))
    while True:
        finer = partition((labels[x], tuple(labels[a[x]] for _, a in source.actions))
                          for x in range(source.count))
        if finer == labels:
            break
        labels = finer
    if labels != q.labels:
        raise DiscoveryError("Stable but nonminimal quotient")
    columns = tuple(p.values(source) for p in q.experiments)
    if partition(tuple(column[x] for column in columns) for x in range(source.count)) != q.labels:
        raise DiscoveryError("Experiment constructor lacks claimed semantics")
    return True


def compose(left, right):
    """Execute left then right; retain this declared orientation everywhere."""
    return tuple(right[x] for x in left)


def action_algebra(q, *, cap=4096):
    if type(cap) is not int or cap < 1:
        raise DiscoveryError("Positive finite algebra cap required")
    identity = tuple(range(q.count))
    elements, todo = {identity}, deque([identity])
    while todo:
        f = todo.popleft()
        for _, a in q.actions:
            new = compose(f, a)
            if new not in elements:
                if len(elements) >= cap:
                    raise DiscoveryError("OPEN_ALGEBRA_BUDGET")
                elements.add(new)
                todo.append(new)
    generators = tuple(a for _, a in q.actions)
    center = {f for f in elements if all(compose(f, a) == compose(a, f) for a in generators)}
    group = all(len(set(f)) == q.count for f in elements)
    answer = {"size": len(elements), "group": group, "center_size": len(center)}
    if group and len(generators) >= 2:
        a, b = generators[:2]
        ai, bi = tuple(a.index(i) for i in identity), tuple(b.index(i) for i in identity)
        h = compose(compose(compose(a, b), ai), bi)
        answer.update({"commuting": h == identity, "central_commutator": h in center,
                       "commutator_order": element_order(h),
                       "generator_orders": [element_order(a), element_order(b)]})
    return answer


def element_order(f):
    if len(set(f)) != len(f) or set(f) != set(range(len(f))):
        raise DiscoveryError("Order needs a permutation")
    identity, current, n = tuple(range(len(f))), tuple(range(len(f))), 0
    while True:
        current, n = compose(current, f), n + 1
        if current == identity:
            return n


def factor_map(fine, coarse):
    if len(fine) != len(coarse) or partition(fine) != fine or partition(coarse) != coarse:
        raise DiscoveryError("Canonical shared-carrier quotient types required")
    answer = tuple(coarse[fine.index(k)] for k in range(len(set(fine))))
    if any(answer[x] != y for x, y in zip(fine, coarse)):
        raise DiscoveryError("No factor map exists")
    return answer


def target_factors(labels, target):
    """All permitted words can identify T iff T is constant on behavior classes.

    This checks the finite complete-table criterion, not single-carrier policy
    realizability. No amount of word growth reaches a target failing this test.
    """
    if len(labels) != len(target):
        raise DiscoveryError("Target outside declared carrier")
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            if labels[i] == labels[j] and target[i] != target[j]:
                return False, (i, j)
    return True, None


def invariant_under_label_change(source, permutation):
    """Checked conjugation constructor, not random labels as evidence."""
    n = source.count
    if set(permutation) != set(range(n)) or len(permutation) != n:
        raise DiscoveryError("Relabelling must be a bijection")
    inverse = tuple(permutation.index(i) for i in range(n))
    return TableSource(source.source_id + ":relabeled",
        tuple((name, tuple(permutation[a[inverse[y]]] for y in range(n))) for name, a in source.actions),
        tuple(tuple(r[inverse[y]] for y in range(n)) for r in source.readouts))
