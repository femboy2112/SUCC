"""Exact finite categorical experiments for SWM-A01--A08.

No imported SUCC quotient, gluing or transport implementation is used here.
Complete declared tables are a mathematical source contract, not empirical
authentication. The proofs and scope are in the individual swarm dossiers.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import product


class CategoryError(ValueError):
    """An exact finite source or typed composition contract failed."""


def _nat(value, limit=None):
    if type(value) is not int or value < 0 or (limit is not None and value >= limit):
        raise CategoryError("Expected an exact nonnegative state address")


def canonical_labels(labels):
    """Canonical representatives of a complete equivalence-class table."""
    if type(labels) is not tuple or not labels:
        raise CategoryError("A nonempty immutable complete partition is required")
    seen = {}
    answer = []
    for label in labels:
        _nat(label)
        if label not in seen:
            seen[label] = len(seen)
        answer.append(seen[label])
    return tuple(answer)


@dataclass(frozen=True)
class FiniteDynamics:
    source_id: str
    reports: tuple[int, ...]
    actions: tuple[str, ...]
    transitions: tuple[tuple[int, ...], ...]
    declared_actions: tuple[str, ...]

    def __post_init__(self):
        if not isinstance(self.source_id, str) or not self.source_id:
            raise CategoryError("Declare the mathematical source identity")
        canonical_labels(self.reports)
        if (type(self.actions) is not tuple or not self.actions
                or len(set(self.actions)) != len(self.actions)
                or any(type(a) is not str or not a for a in self.actions)
                or self.declared_actions != self.actions
                or type(self.transitions) is not tuple
                or len(self.transitions) != len(self.actions)):
            raise CategoryError("Every declared action needs exactly one total table")
        for table in self.transitions:
            if type(table) is not tuple or len(table) != self.count:
                raise CategoryError("Missing source states in a transition table")
            for state in table:
                _nat(state, self.count)

    @property
    def count(self):
        return len(self.reports)

    def step(self, state, action):
        _nat(state, self.count)
        if action not in self.actions:
            raise CategoryError("Unavailable action")
        return self.transitions[self.actions.index(action)][state]

    def word_state(self, state, word):
        _nat(state, self.count)
        for action in word:
            state = self.step(state, action)
        return state

    def transcript(self, state, word):
        """Current report, then each actually changed carrier's report."""
        _nat(state, self.count)
        answer = [self.reports[state]]
        for action in word:
            state = self.step(state, action)
            answer.append(self.reports[state])
        return tuple(answer)


def refines(fine, coarse):
    if len(fine) != len(coarse):
        raise CategoryError("Different partition domains")
    return all(fine[x] != fine[y] or coarse[x] == coarse[y]
               for x in range(len(fine)) for y in range(len(fine)))


def stable(source, labels):
    labels = canonical_labels(labels)
    if len(labels) != source.count:
        raise CategoryError("Partition omits source states")
    return all(labels[x] != labels[y]
               or all(labels[t[x]] == labels[t[y]] for t in source.transitions)
               for x in range(source.count) for y in range(source.count))


def stable_refinement(source, labels=None):
    """Greatest action-stable equivalence contained in the declared relation.

    With labels=reports this is the behavioral quotient. With a finer initial
    label (report, original-target) it retains that target too. It is an
    interior operator under relation inclusion, not a closure operator there.
    """
    initial = canonical_labels(source.reports if labels is None else labels)
    if len(initial) != source.count:
        raise CategoryError("Partition omits source states")
    current = initial
    steps = 0
    while True:
        signatures = tuple((current[x],)
                           + tuple(current[t[x]] for t in source.transitions)
                           for x in range(source.count))
        signature_ids = {}
        nxt = tuple(signature_ids.setdefault(s, len(signature_ids)) for s in signatures)
        if nxt == current:
            return current, steps
        if len(set(nxt)) <= len(set(current)):
            raise ArithmeticError("Partition repair failed to strictly refine")
        current = nxt
        steps += 1


def quotient(source, labels):
    """Build the exact quotient only after both action and report gates pass."""
    labels = canonical_labels(labels)
    if not stable(source, labels) or not refines(labels, source.reports):
        raise CategoryError("Action/report law does not descend to this quotient")
    representatives = tuple(labels.index(k) for k in range(len(set(labels))))
    return FiniteDynamics(source.source_id + ":quotient",
                          tuple(source.reports[x] for x in representatives),
                          source.actions,
                          tuple(tuple(labels[t[x]] for x in representatives)
                                for t in source.transitions), source.actions)


def source_morphism(left, right, mapping):
    """Strict common-action, report-preserving map; surjectivity not assumed."""
    if type(mapping) is not tuple or len(mapping) != left.count:
        raise CategoryError("Incomplete original-source map")
    for state in mapping:
        _nat(state, right.count)
    if left.actions != right.actions:
        return False
    return (all(left.reports[x] == right.reports[mapping[x]] for x in range(left.count))
            and all(mapping[left.step(x, action)] == right.step(mapping[x], action)
                    for x in range(left.count) for action in left.actions))


def repair_base_change(left, right, mapping, right_labels):
    """Fibred coreflection: I_X(f*R) = f*(I_Y R), for strict source maps."""
    if not source_morphism(left, right, mapping):
        raise CategoryError("Base change needs every common-action square")
    right_labels = canonical_labels(right_labels)
    if len(right_labels) != right.count:
        raise CategoryError("Incomplete right equivalence relation")
    pulled = tuple(right_labels[mapping[x]] for x in range(left.count))
    lhs = stable_refinement(left, pulled)[0]
    repaired = stable_refinement(right, right_labels)[0]
    rhs = canonical_labels(tuple(repaired[mapping[x]] for x in range(left.count)))
    return lhs, rhs


def belief_update(source, belief, action, report):
    """Origin/current pairs; report is read BEFORE the destructive action."""
    if action not in source.actions:
        raise CategoryError("Unavailable action")
    answer = set()
    for origin, current in belief:
        _nat(origin, source.count)
        _nat(current, source.count)
        if source.reports[current] == report:
            answer.add((origin, source.step(current, action)))
    return frozenset(answer)


def map_belief(belief, labels):
    labels = canonical_labels(labels)
    answer = set()
    for origin, current in belief:
        _nat(origin, len(labels))
        _nat(current, len(labels))
        answer.add((labels[origin], labels[current]))
    return frozenset(answer)


def saturated_subset(subset, labels):
    labels = canonical_labels(labels)
    for x in subset:
        _nat(x, len(labels))
    image = {labels[x] for x in subset}
    return frozenset(x for x in range(len(labels)) if labels[x] in image)


def finite_relation_glue(variables, alphabet, local_tables):
    """Literal inverse image intersection; empty is a failed global section."""
    if len(set(variables)) != len(variables) or len(set(alphabet)) != len(alphabet):
        raise CategoryError("Distinct global coordinates and exact alphabet required")
    lookup = {v: i for i, v in enumerate(variables)}
    for context, rows in local_tables:
        if len(set(context)) != len(context) or any(v not in lookup for v in context):
            raise CategoryError("Local context outside global source coordinates")
        if any(len(row) != len(context) or any(v not in alphabet for v in row)
               for row in rows):
            raise CategoryError("Malformed local relation")
    return tuple(row for row in product(alphabet, repeat=len(variables))
                 if all(tuple(row[lookup[v]] for v in context) in rows
                        for context, rows in local_tables))


def compose_permutation(after, before):
    if sorted(after) != list(range(len(after))) or sorted(before) != list(range(len(after))):
        raise CategoryError("Permutation types differ")
    return tuple(after[before[x]] for x in range(len(after)))


def inverse_permutation(p):
    if sorted(p) != list(range(len(p))):
        raise CategoryError("Noninvertible transport")
    return tuple(p.index(x) for x in range(len(p)))


def holonomy_sections(vertices, edges, degree, declared_edge_ids):
    """Exact root values of parallel sections on a connected finite graph.

    Edges are (id, tail, head, permutation). Declared coverage is mandatory;
    a source declaration remains a model contract, not authentication.
    """
    _nat(degree)
    if degree == 0 or not vertices or len(set(vertices)) != len(vertices):
        raise CategoryError("Finite nonempty graph/fiber required")
    ids = tuple(e[0] for e in edges)
    if len(set(ids)) != len(ids) or set(ids) != set(declared_edge_ids):
        raise CategoryError("Incomplete or duplicate source-edge coverage")
    identity = tuple(range(degree))
    adj = {v: [] for v in vertices}
    for _, u, v, p in edges:
        if u not in adj or v not in adj or len(p) != degree:
            raise CategoryError("Source-edge endpoint/fiber mismatch")
        inv = inverse_permutation(p)
        adj[u].append((v, p))
        adj[v].append((u, inv))
    transport = {vertices[0]: identity}
    pending = deque([vertices[0]])
    while pending:
        u = pending.popleft()
        for v, p in adj[u]:
            if v not in transport:
                transport[v] = compose_permutation(p, transport[u])
                pending.append(v)
    if len(transport) != len(vertices):
        raise CategoryError("This theorem requires a connected source graph")
    loops = tuple(compose_permutation(inverse_permutation(transport[v]),
                                     compose_permutation(p, transport[u]))
                  for _, u, v, p in edges)
    fixed = tuple(x for x in range(degree) if all(g[x] == x for g in loops))
    sections = tuple(tuple(transport[v][x] for v in vertices) for x in fixed)
    return {"root_values": fixed, "sections": sections, "root_holonomies": loops}


def discrete_kan(mapping, fibers, target_count):
    """Left tagged sums and right products along a map of discrete categories."""
    if len(mapping) != len(fibers):
        raise CategoryError("Incomplete old-language model")
    _nat(target_count)
    for p in mapping:
        _nat(p, target_count)
    left, right = [], []
    for p in range(target_count):
        old = [o for o, image in enumerate(mapping) if image == p]
        left.append(tuple((o, value) for o in old for value in fibers[o]))
        right.append(tuple(product(*(fibers[o] for o in old))))
    return tuple(left), tuple(right)


@dataclass(frozen=True)
class InstrumentArrow:
    domain: int
    codomain: int
    transition: tuple[int, ...]
    alphabet: tuple[tuple[int, ...], ...]
    reports: tuple[tuple[int, ...], ...]
    width: int

    def __post_init__(self):
        for n in (self.domain, self.codomain, self.width):
            _nat(n)
        if (not self.domain or not self.codomain or len(self.transition) != self.domain
                or len(self.reports) != self.domain or not self.alphabet
                or any(type(x) is not tuple for x in
                       (self.transition, self.alphabet, self.reports))
                or any(type(x) is not tuple for x in self.alphabet)
                or len(set(self.alphabet)) != len(self.alphabet)):
            raise CategoryError("Complete typed deterministic instrument required")
        for x in self.transition:
            _nat(x, self.codomain)
        if any(len(o) != self.width or any(type(x) is not int for x in o)
               for o in self.alphabet) or any(o not in self.alphabet for o in self.reports):
            raise CategoryError("Report word type/coverage mismatch")

    @classmethod
    def identity(cls, size):
        return cls(size, size, tuple(range(size)), ((),), ((),) * size, 0)

    def then(self, after):
        if self.codomain != after.domain:
            raise CategoryError("Causal endpoints do not compose")
        return InstrumentArrow(self.domain, after.codomain,
                               tuple(after.transition[y] for y in self.transition),
                               tuple(a + b for a in self.alphabet for b in after.alphabet),
                               tuple(self.reports[x] + after.reports[self.transition[x]]
                                     for x in range(self.domain)), self.width + after.width)


@dataclass(frozen=True)
class ReportComparison:
    before: InstrumentArrow
    after: InstrumentArrow
    label_map: tuple[int, ...]

    def __post_init__(self):
        if (self.before.domain != self.after.domain
                or self.before.codomain != self.after.codomain
                or self.before.transition != self.after.transition
                or type(self.label_map) is not tuple
                or len(self.label_map) != len(self.before.alphabet)):
            raise CategoryError("2-cell must preserve the actual carrier arrow")
        for i in self.label_map:
            _nat(i, len(self.after.alphabet))
        if any(self.after.alphabet[self.label_map[self.before.alphabet.index(r)]] != s
               for r, s in zip(self.before.reports, self.after.reports)):
            raise CategoryError("Report comparison square does not commute")

    def then(self, after):
        if self.after != after.before:
            raise CategoryError("Vertical comparison endpoints do not compose")
        return ReportComparison(self.before, after.after,
                                tuple(after.label_map[i] for i in self.label_map))

    def horizontal(self, after):
        return ReportComparison(self.before.then(after.before), self.after.then(after.after),
                                tuple(a * len(after.after.alphabet) + b
                                      for a in self.label_map for b in after.label_map))


def separation_depth(source, x, y):
    """Minimum probe-count: present report costs 1, each action adds 1.

    Returns None for behaviorally inseparable pairs, including the diagonal.
    This raw cost is NOT a Lawvere distance.
    """
    _nat(x, source.count)
    _nat(y, source.count)
    pending = deque([(x, y, 1)])
    seen = {(x, y)}
    while pending:
        a, b, depth = pending.popleft()
        if source.reports[a] != source.reports[b]:
            return depth
        for table in source.transitions:
            pair = (table[a], table[b])
            if pair not in seen:
                seen.add(pair)
                pending.append((*pair, depth + 1))
    return None


def observational_ultrametric(source, x, y):
    depth = separation_depth(source, x, y)
    return Fraction(0) if depth is None else Fraction(1, 2 ** (depth - 1))


def directed_resource_distance(vertex_count, edges):
    """Free shortest-path Lawvere geometry, using exact nonnegative costs."""
    _nat(vertex_count)
    dist = [[None] * vertex_count for _ in range(vertex_count)]
    for i in range(vertex_count):
        dist[i][i] = Fraction(0)
    for u, v, cost in edges:
        _nat(u, vertex_count)
        _nat(v, vertex_count)
        if type(cost) is not int and not isinstance(cost, Fraction):
            raise CategoryError("Exact rational resource costs required")
        cost = Fraction(cost)
        if cost < 0:
            raise CategoryError("Negative debt is outside this nonnegative geometry")
        if dist[u][v] is None or cost < dist[u][v]:
            dist[u][v] = cost
    for k in range(vertex_count):
        for u in range(vertex_count):
            for v in range(vertex_count):
                if dist[u][k] is not None and dist[k][v] is not None:
                    candidate = dist[u][k] + dist[k][v]
                    if dist[u][v] is None or candidate < dist[u][v]:
                        dist[u][v] = candidate
    return tuple(tuple(row) for row in dist)
