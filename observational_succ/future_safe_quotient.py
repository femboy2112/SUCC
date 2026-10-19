"""Exact future-safe forgetting for declared finite deterministic source models.

CLASSICAL: enriched Moore/Mealy minimization and kernel factorization. Source
tags are mandatory preserved outputs; task strings are declared outputs, not
proofs. An absent edge records unavailable action. A separating request word
is a physical experiment only if a lawful rejection/cost-report interface is
actually available. No source authentication is inferred from this table.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from heapq import heappop, heappush
from itertools import combinations, count
from typing import Mapping


class ForgettingError(ValueError):
    """Malformed model, false certificate, or explicit resource exhaustion."""


@dataclass(frozen=True)
class State:
    name: str
    source: str
    observation: str
    tasks: tuple[tuple[str, str], ...] = ()

    def output(self) -> tuple:
        return self.source, self.observation, self.tasks


@dataclass(frozen=True)
class Edge:
    start: str
    action: str
    target: str
    cost: Fraction


@dataclass(frozen=True)
class Machine:
    states: tuple[State, ...]
    actions: tuple[str, ...]
    edges: tuple[Edge, ...]

    def __post_init__(self) -> None:
        if (type(self.states) is not tuple or not self.states
                or any(type(s) is not State for s in self.states)
                or type(self.actions) is not tuple
                or any(type(a) is not str or not a for a in self.actions)
                or len(set(self.actions)) != len(self.actions)
                or type(self.edges) is not tuple):
            raise ForgettingError("Finite immutable states/actions/edges required")
        names = []
        task_schema = None
        for s in self.states:
            if (type(s.name) is not str or not s.name
                    or type(s.source) is not str or not s.source
                    or type(s.observation) is not str
                    or type(s.tasks) is not tuple
                    or any(type(t) is not tuple or len(t) != 2
                           or any(type(v) is not str for v in t) or not t[0]
                           for t in s.tasks)):
                raise ForgettingError("Typed source, report and task labels required")
            keys = tuple(k for k, _ in s.tasks)
            if len(set(keys)) != len(keys):
                raise ForgettingError("Duplicate task names")
            if task_schema is None:
                task_schema = keys
            if keys != task_schema:
                raise ForgettingError("Every state must declare the same ordered tasks")
            names.append(s.name)
        if len(set(names)) != len(names):
            raise ForgettingError("Distinct state names required")
        seen = set()
        for e in self.edges:
            if (type(e) is not Edge or e.start not in names
                    or e.target not in names or e.action not in self.actions
                    or type(e.cost) is not Fraction or e.cost < 0
                    or (e.start, e.action) in seen):
                raise ForgettingError("Partial deterministic nonnegative rational edges required")
            seen.add((e.start, e.action))

    def maps(self) -> tuple[dict[str, State], dict[tuple[str, str], Edge]]:
        return ({s.name: s for s in self.states},
                {(e.start, e.action): e for e in self.edges})


@dataclass(frozen=True)
class Separator:
    left: str
    right: str
    word: tuple[str, ...]


@dataclass(frozen=True)
class QuotientCertificate:
    blocks: tuple[tuple[str, ...], ...]
    separators: tuple[Separator, ...]


def trace(machine: Machine, start: str, word: tuple[str, ...]) -> tuple:
    """Exact specification trace; unavailable request stops without action.

    The tuple is an abstract interface value. Availability is not claimed
    observable in a physical system lacking a lawful rejection/menu oracle.
    """
    states, edges = machine.maps()
    if (start not in states or type(word) is not tuple
            or any(a not in machine.actions for a in word)):
        raise ForgettingError("Unknown state or request word")
    out = [("output", states[start].output())]
    current = start
    for a in word:
        e = edges.get((current, a))
        if e is None:
            out.append(("unavailable", a))
            break
        current = e.target
        out.append(("step", a, e.cost, states[current].output()))
    return tuple(out)


def distinguishing_word(machine: Machine, left: str,
                        right: str) -> tuple[str, ...] | None:
    """Breadth-first product search returns a shortest specification witness."""
    states, edges = machine.maps()
    if left not in states or right not in states:
        raise ForgettingError("Unknown comparison state")
    queue = deque([(left, right, ())])
    seen = {tuple(sorted((left, right)))}
    while queue:
        x, y, prefix = queue.popleft()
        if states[x].output() != states[y].output():
            return prefix
        for a in machine.actions:
            ex, ey = edges.get((x, a)), edges.get((y, a))
            if (ex is None) != (ey is None):
                return prefix + (a,)
            if ex is None:
                continue
            if ex.cost != ey.cost:
                return prefix + (a,)
            # Check the immediate output before returning a longer witness
            # from another same-depth queue node.
            if states[ex.target].output() != states[ey.target].output():
                return prefix + (a,)
            pair = tuple(sorted((ex.target, ey.target)))
            if pair not in seen:
                seen.add(pair)
                queue.append((ex.target, ey.target, prefix + (a,)))
    return None


def minimize(machine: Machine) -> QuotientCertificate:
    """Classical finite partition refinement, followed by replayable witnesses."""
    states, edges = machine.maps()

    def classes(signatures: Mapping[str, tuple]) -> dict[str, int]:
        assigned: dict[tuple, int] = {}
        return {s.name: assigned.setdefault(signatures[s.name], len(assigned))
                for s in machine.states}

    blocks = classes({s.name: s.output() for s in machine.states})
    while True:
        signatures = {}
        for s in machine.states:
            row = []
            for a in machine.actions:
                e = edges.get((s.name, a))
                row.append(None if e is None else (e.cost, blocks[e.target]))
            signatures[s.name] = (s.output(), tuple(row))
        refined = classes(signatures)
        if refined == blocks:
            break
        blocks = refined
    result = tuple(tuple(s.name for s in machine.states if blocks[s.name] == i)
                   for i in range(max(blocks.values()) + 1))
    separators = []
    for x, y in combinations(result, 2):
        word = distinguishing_word(machine, x[0], y[0])
        if word is None:
            raise AssertionError("Refinement split behaviorally equal states")
        separators.append(Separator(x[0], y[0], word))
    return QuotientCertificate(result, tuple(separators))


def _partition_map(machine: Machine,
                   blocks: tuple[tuple[str, ...], ...]) -> dict[str, int]:
    if (type(blocks) is not tuple or not blocks
            or any(type(b) is not tuple or not b for b in blocks)
            or any(type(s) is not str for b in blocks for s in b)):
        raise ForgettingError("Nonempty immutable partition blocks required")
    flat = tuple(s for b in blocks for s in b)
    if len(set(flat)) != len(flat) or set(flat) != {s.name for s in machine.states}:
        raise ForgettingError("Partition must be disjoint and cover exactly all states")
    return {s: i for i, b in enumerate(blocks) for s in b}


def _congruence_defect(machine: Machine, labels: Mapping[str, object]) -> tuple | None:
    states, edges = machine.maps()
    for x, y in combinations(states, 2):
        if labels[x] != labels[y]:
            continue
        if states[x].output() != states[y].output():
            return "output", x, y
        for a in machine.actions:
            ex, ey = edges.get((x, a)), edges.get((y, a))
            if (ex is None) != (ey is None):
                return "availability", x, y, a
            if ex is not None:
                if ex.cost != ey.cost:
                    return "cost", x, y, a
                if labels[ex.target] != labels[ey.target]:
                    return "successor", x, y, a
    return None


def verify_certificate(machine: Machine, cert: QuotientCertificate) -> bool:
    """Check local congruence + separating traces without running minimization.

    Local squares certify all words by induction. Pairwise separators certify
    maximal merging. This verifier shares trace/model code with the generator;
    the separate research checker is the implementation-independent route.
    """
    if type(cert) is not QuotientCertificate:
        raise ForgettingError("Typed quotient certificate required")
    labels = _partition_map(machine, cert.blocks)
    defect = _congruence_defect(machine, labels)
    if defect is not None:
        raise ForgettingError(f"Noncongruent quotient: {defect}")
    expected = {(x[0], y[0]) for x, y in combinations(cert.blocks, 2)}
    if (type(cert.separators) is not tuple
            or any(type(s) is not Separator for s in cert.separators)
            or len(cert.separators) != len(expected)
            or {(s.left, s.right) for s in cert.separators} != expected):
        raise ForgettingError("Exactly one oriented representative witness per block pair required")
    for s in cert.separators:
        if trace(machine, s.left, s.word) == trace(machine, s.right, s.word):
            raise ForgettingError("Forged distinguishing word")
        for length in range(len(s.word)):
            prefix = s.word[:length]
            if trace(machine, s.left, prefix) != trace(machine, s.right, prefix):
                raise ForgettingError("Witness has unused actions after first distinction")
    return True


def audit_representation(machine: Machine, labels: tuple[str, ...]) -> dict:
    """Separate future-task recoverability from autonomous updates of q itself.

    If safe, factor is the unique f on image(q) with canonical_projection=f*q.
    A finer safe representation need not have a well-defined state update.
    """
    if (type(labels) is not tuple or len(labels) != len(machine.states)
            or any(type(x) is not str for x in labels)):
        raise ForgettingError("One representation label per state required")
    cert = minimize(machine)
    canonical = _partition_map(machine, cert.blocks)
    q = dict(zip((s.name for s in machine.states), labels))
    factor = {}
    witness = None
    representative = {}
    for s in machine.states:
        label = q[s.name]
        if label in factor and factor[label] != canonical[s.name]:
            x = representative[label]
            word = distinguishing_word(machine, x, s.name)
            assert word is not None
            witness = Separator(x, s.name, word)
            break
        factor[label] = canonical[s.name]
        representative[label] = s.name
    defect = _congruence_defect(machine, q)
    return {"future_safe": witness is None, "autonomous": defect is None,
            "factor": tuple(factor.items()) if witness is None else (),
            "future_obstruction": witness, "update_obstruction": defect}


@dataclass(frozen=True)
class BudgetLift:
    machine: Machine
    # lifted name, original name, exact residual budget
    origins: tuple[tuple[str, str, Fraction], ...]

    def name(self, original: str, remaining: Fraction) -> str:
        for lifted, state, budget in self.origins:
            if (state, budget) == (original, remaining):
                return lifted
        raise ForgettingError("Residual state not reachable from declared initial budgets")


@dataclass(frozen=True)
class BudgetSeparator:
    budget: Fraction
    word: tuple[str, ...]


def minimum_distinguishing_budget(machine: Machine, left: str,
                                  right: str) -> BudgetSeparator | None:
    """Exact Dijkstra distance to a discrepancy in the state-pair graph.

    Under budget-lift semantics, inequivalence holds exactly when B >= this
    threshold. Cost mismatch can be seen when only the cheaper action is
    affordable; it need not wait until both prices are affordable. None means
    equivalent for every budget, not failure to find a finite witness.
    """
    states, edges = machine.maps()
    if left not in states or right not in states:
        raise ForgettingError("Unknown comparison state")
    serial = count()
    queue = [(Fraction(0), next(serial), left, right, ())]
    distance = {tuple(sorted((left, right))): Fraction(0)}
    while queue:
        spent, _, x, y, word = heappop(queue)
        if x is None:  # A terminal affordability/availability discrepancy.
            return BudgetSeparator(spent, word)
        pair = tuple(sorted((x, y)))
        if spent != distance[pair]:
            continue
        if states[x].output() != states[y].output():
            return BudgetSeparator(spent, word)
        for a in machine.actions:
            ex, ey = edges.get((x, a)), edges.get((y, a))
            if ex is None and ey is None:
                continue
            if ex is None or ey is None or ex.cost != ey.cost:
                available = [e.cost for e in (ex, ey) if e is not None]
                heappush(queue, (spent + min(available), next(serial), None, None,
                                word + (a,)))
                continue
            successor = tuple(sorted((ex.target, ey.target)))
            candidate = spent + ex.cost
            if successor not in distance or candidate < distance[successor]:
                distance[successor] = candidate
                heappush(queue, (candidate, next(serial), ex.target, ey.target,
                                word + (a,)))
    return None


def budget_lift(machine: Machine, budget: Fraction,
                *, max_states: int = 10000) -> BudgetLift:
    """Finite reachable (state,residual-budget) expansion; zero-cost loops allowed.

    Every original state starts at the same budget. Unaffordable and unavailable
    actions are both denied; no unaffordable price is revealed. Remaining budget
    is stored, not added to observable outputs. Exhaustion is UNKNOWN via error.
    """
    if (type(budget) is not Fraction or budget < 0
            or type(max_states) is not int or max_states < len(machine.states)):
        raise ForgettingError("Nonnegative rational budget and sufficient state cap required")
    states, edges = machine.maps()
    names = {(s.name, budget): f"b{i}" for i, s in enumerate(machine.states)}
    queue = deque(names)
    new_states, new_edges = [], []
    while queue:
        original, remaining = queue.popleft()
        s = states[original]
        current = names[(original, remaining)]
        new_states.append(State(current, s.source, s.observation, s.tasks))
        for a in machine.actions:
            e = edges.get((original, a))
            if e is None or e.cost > remaining:
                continue
            successor = (e.target, remaining - e.cost)
            if successor not in names:
                if len(names) >= max_states:
                    raise ForgettingError("UNKNOWN: residual state expansion exceeded cap")
                names[successor] = f"b{len(names)}"
                queue.append(successor)
            new_edges.append(Edge(current, a, names[successor], e.cost))
    return BudgetLift(Machine(tuple(new_states), machine.actions, tuple(new_edges)),
                      tuple((name, s, b) for (s, b), name in names.items()))


def certificate_payload(machine: Machine, cert: QuotientCertificate) -> dict:
    """Portable exact schema for a separately implemented checker."""
    return {
        "states": [{"name": s.name, "source": s.source,
                    "observation": s.observation,
                    "tasks": [list(t) for t in s.tasks]} for s in machine.states],
        "actions": list(machine.actions),
        "edges": [{"start": e.start, "action": e.action, "target": e.target,
                   "cost": [e.cost.numerator, e.cost.denominator]}
                  for e in machine.edges],
        "certificate": {
            "blocks": [list(b) for b in cert.blocks],
            "separators": [{"left": s.left, "right": s.right,
                            "word": list(s.word)} for s in cert.separators]},
    }
