"""Carrier-relative target descent, observable algebra, and executable access.

Exact FINITE declared deterministic models only. Model truth tables and source
labels are not physical attestation. Algebraic identifiability across possible
experiments is distinct from a policy on ONE unresettable source instance.
Classical lineage: observational equivalence, Moore/Mealy refinement, quotient
factorization, finite function algebras and finite minimax decision trees.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from hashlib import sha256
from heapq import heappop, heappush
import json


class CarrierError(ValueError):
    """Invalid source, chart, exact arithmetic, or certificate."""


def rational(x):
    if type(x) not in (int, Q):
        raise CarrierError("exact int/Fraction required; no float or bool")
    return Q(x)


def label(x):
    if type(x) is not str or not x.strip():
        raise CarrierError("nonempty source/operation/chart label required")
    return x


@dataclass(frozen=True)
class Instrument:
    name: str
    chart: str
    outputs: tuple[Q, ...]
    next_states: tuple[int, ...]
    cost: int = 1


@dataclass(frozen=True)
class Carrier:
    source: str
    size: int
    instruments: tuple[Instrument, ...]

    def __post_init__(self):
        label(self.source)
        if type(self.size) is not int or not 1 <= self.size <= 24:
            raise CarrierError("finite source size must be 1..24")
        if type(self.instruments) is not tuple:
            raise CarrierError("immutable instrument family required")
        names = set()
        for a in self.instruments:
            if type(a) is not Instrument or a.name in names:
                raise CarrierError("distinct typed instruments required")
            label(a.name); label(a.chart); names.add(a.name)
            if (type(a.cost) is not int or not 1 <= a.cost <= 32 or
                type(a.outputs) is not tuple or type(a.next_states) is not tuple or
                len(a.outputs) != self.size or len(a.next_states) != self.size or
                any(type(v) is not Q for v in a.outputs) or
                any(type(v) is not int or not 0 <= v < self.size for v in a.next_states)):
                raise CarrierError("exact aligned outputs, total transition, positive cost required")

    def operation(self, name):
        for a in self.instruments:
            if a.name == name:
                return a
        raise CarrierError("instrument outside declared toolkit")

    @property
    def fingerprint(self):
        raw = (self.source, self.size, tuple((a.name, a.chart,
               tuple(str(v) for v in a.outputs), a.next_states, a.cost)
               for a in self.instruments))
        return sha256(json.dumps(raw, separators=(",", ":")).encode()).hexdigest()


@dataclass(frozen=True)
class Target:
    source: str
    name: str
    values: tuple[Q, ...]

    def validate(self, carrier):
        label(self.name)
        if (self.source != carrier.source or type(self.values) is not tuple or
                len(self.values) != carrier.size or any(type(v) is not Q for v in self.values)):
            raise CarrierError("target must be an exact table on the declared source")


def _classes(signatures):
    groups = {}
    for i, signature in enumerate(signatures):
        groups.setdefault(signature, []).append(i)
    return tuple(tuple(g) for g in groups.values())


def behavioral_partition(carrier):
    """All finite experiments; costs affect availability but not this closure.

    Stable partition = greatest output-compatible transition congruence.
    Distinct operation output charts are NEVER compared to each other.
    """
    blocks = (tuple(range(carrier.size)),)
    while True:
        owner = {x: j for j, b in enumerate(blocks) for x in b}
        keys = tuple(tuple((a.outputs[x], owner[a.next_states[x]])
                           for a in carrier.instruments) for x in range(carrier.size))
        refined = _classes(keys)
        if refined == blocks:
            return blocks
        blocks = refined


def trace(carrier, state, word):
    if type(state) is not int or not 0 <= state < carrier.size:
        raise CarrierError("invalid initial state")
    history = []
    for name in word:
        a = carrier.operation(name)
        history.append((a.name, a.chart, a.outputs[state]))
        state = a.next_states[state]
    return tuple(history), state


def shortest_separator(carrier, left, right):
    """Least-cost separating action word, or None for permanent equivalence.

    A witness separates this pair; it is NOT a universal single-run policy.
    """
    trace(carrier, left, ()); trace(carrier, right, ())
    queue = [(0, (), left, right)]
    seen = set()
    while queue:
        cost, word, x, y = heappop(queue)
        if x == -1:
            return cost, word
        if (x, y) in seen:
            continue
        seen.add((x, y))
        for a in carrier.instruments:
            pair = (-1, -1) if a.outputs[x] != a.outputs[y] else (a.next_states[x], a.next_states[y])
            heappush(queue, (cost + a.cost, word + (a.name,), *pair))
    return None


def target_obstruction(carrier, target):
    """Opposite target values with identical ALL-word traces, or None.

    A returned pair proves nonidentifiability in this finite declared toolkit.
    None does NOT guarantee one-run access when measurements are destructive.
    """
    target.validate(carrier)
    for block in behavioral_partition(carrier):
        for left in block:
            for right in block:
                if target.values[left] != target.values[right]:
                    return left, right
    return None



def _linear_expression(vector, basis):
    """Independent rational row reduction; return coefficients or None."""
    n, d = len(vector), len(basis)
    pivots = []
    for i, original in enumerate(basis):
        row = list(original)
        coeff = [Q(int(i == j)) for j in range(d)]
        for p, b, c in pivots:
            scale = row[p]
            row = [x - scale*y for x, y in zip(row, b)]
            coeff = [x - scale*y for x, y in zip(coeff, c)]
        p = next((j for j in range(n) if row[j]), None)
        if p is not None:
            scale = row[p]
            pivots.append((p, tuple(x/scale for x in row), tuple(x/scale for x in coeff)))
    row, answer = list(vector), [Q(0)]*d
    for p, b, c in pivots:
        scale = row[p]
        row = [x - scale*y for x, y in zip(row, b)]
        answer = [x + scale*y for x, y in zip(answer, c)]
    return tuple(answer) if not any(row) else None


@dataclass(frozen=True)
class AlgebraRow:
    rule: str
    args: tuple
    values: tuple[Q, ...]


@dataclass(frozen=True)
class ObservableAlgebra:
    carrier_fingerprint: str
    rows: tuple[AlgebraRow, ...]

    @property
    def basis(self):
        return tuple(row.values for row in self.rows)

    def express(self, carrier, target):
        target.validate(carrier)
        verify_algebra(carrier, self)
        return _linear_expression(target.values, self.basis)


def observable_algebra(carrier):
    """Build the function algebra generated by lawful transcript readouts.

    Row-span alone is insufficient: retain products (joint observations) and
    transition pullbacks (future readouts). Each independent row has a recipe.
    This is the algebra of counterfactual experiments, NOT an execution oracle.
    """
    rows = []

    def add(rule, args, values):
        if _linear_expression(values, [r.values for r in rows]) is None:
            rows.append(AlgebraRow(rule, args, values))

    add("one", (), (Q(1),)*carrier.size)
    for a in carrier.instruments:
        for v in sorted(set(a.outputs)):
            add("read", (a.name, v), tuple(Q(x == v) for x in a.outputs))
    cursor = 0
    while cursor < len(rows):
        r = rows[cursor].values
        for a in carrier.instruments:
            add("pull", (cursor, a.name), tuple(r[x] for x in a.next_states))
        for j in range(cursor + 1):
            add("product", (cursor, j), tuple(x*y for x, y in zip(r, rows[j].values)))
        cursor += 1
    certificate = ObservableAlgebra(carrier.fingerprint, tuple(rows))
    verify_algebra(carrier, certificate)
    return certificate


def verify_algebra(carrier, certificate):
    """Replay each construction, verify independence and closure; reject spoofing."""
    if certificate.carrier_fingerprint != carrier.fingerprint:
        raise CarrierError("certificate belongs to a different carrier")
    basis = []
    for row in certificate.rows:
        rule, args = row.rule, row.args
        try:
            if rule == "one" and args == ():
                expected = (Q(1),)*carrier.size
            elif rule == "read" and len(args) == 2:
                a = carrier.operation(args[0])
                expected = tuple(Q(x == args[1]) for x in a.outputs)
            elif rule == "pull" and len(args) == 2 and type(args[0]) is int and 0 <= args[0] < len(basis):
                a = carrier.operation(args[1])
                expected = tuple(basis[args[0]][x] for x in a.next_states)
            elif rule == "product" and len(args) == 2 and all(type(i) is int and 0 <= i < len(basis) for i in args):
                expected = tuple(x*y for x, y in zip(basis[args[0]], basis[args[1]]))
            else:
                raise CarrierError("invalid or future-referencing algebra recipe")
        except (IndexError, TypeError) as exc:
            raise CarrierError("malformed algebra recipe") from exc
        if (row.values != expected or len(row.values) != carrier.size or
                any(type(x) is not Q for x in row.values) or
                _linear_expression(row.values, basis) is not None):
            raise CarrierError("invalid or dependent algebra row")
        basis.append(row.values)
    required = [(Q(1),)*carrier.size]
    for a in carrier.instruments:
        required += [tuple(Q(x == v) for x in a.outputs) for v in set(a.outputs)]
        required += [tuple(row[x] for x in a.next_states) for row in basis]
    required += [tuple(x*y for x, y in zip(a, b)) for a in basis for b in basis]
    if any(_linear_expression(row, basis) is None for row in required):
        raise CarrierError("certificate is not closed under declared observations")
    return True


@dataclass(frozen=True)
class TargetResolution:
    status: str
    possible: tuple[int, ...]
    values: tuple[Q, ...]
    midpoint: Q | None
    minimax_error: Q | None


def resolve_target(carrier, target, possible):
    """Truth/value on a fiber. Empty fiber is INCOHERENT, never vacuous truth."""
    target.validate(carrier)
    if (type(possible) is not tuple or possible != tuple(sorted(set(possible))) or
            any(type(i) is not int or not 0 <= i < carrier.size for i in possible)):
        raise CarrierError("sorted exact source-state support required")
    values = tuple(sorted(set(target.values[i] for i in possible)))
    if not values:
        return TargetResolution("INCOHERENT", possible, (), None, None)
    lo, hi = values[0], values[-1]
    return TargetResolution("IDENTIFIED" if lo == hi else "AMBIGUOUS",
                            possible, values, (lo+hi)/2, (hi-lo)/2)


def static_fiber(carrier, readings):
    """Joint same-state noninvasive readouts. Requires explicitly shared source.

    Each reading is (source, instrument, chart, exact reported value). For
    invasive experiments use policy state, not a fictional simultaneous fiber.
    """
    possible = tuple(range(carrier.size))
    for source, name, chart, value in readings:
        a = carrier.operation(name)
        if (source != carrier.source or chart != a.chart or
                a.next_states != tuple(range(carrier.size))):
            raise CarrierError("source/chart mismatch or nonjoint invasive reading")
        value = rational(value)
        possible = tuple(i for i in possible if a.outputs[i] == value)
    return possible


@dataclass(frozen=True)
class Policy:
    answer: Q | None
    operation: str | None
    children: tuple[tuple[Q, Policy], ...] = ()


@dataclass(frozen=True)
class PolicyResult:
    policy: Policy | None
    worst_cost: int | None
    searched_budget: int
    status: str


def plan_target(carrier, target, budget, possible=None):
    """Optimal worst-case cost within a FINITE budget, single unresettable copy.

    Belief pairs retain (original state, current state), so learning after a
    destructive probe is never confused with recovering the original target.
    Failure is a finite-budget result, not general undecidability.
    """
    target.validate(carrier)
    if type(budget) is not int or not 0 <= budget <= 16:
        raise CarrierError("bounded nonnegative planning budget 0..16 required")
    possible = tuple(range(carrier.size)) if possible is None else possible
    if resolve_target(carrier, target, possible).status == "INCOHERENT":
        raise CarrierError("cannot plan on an empty source support")

    @lru_cache(None)
    def solve(pairs, remaining):
        values = {target.values[original] for original, _ in pairs}
        if len(values) == 1:
            return 0, Policy(next(iter(values)), None)
        best = None
        for a in carrier.instruments:
            if a.cost > remaining:
                continue
            groups = {}
            for original, current in pairs:
                groups.setdefault(a.outputs[current], []).append((original, a.next_states[current]))
            children, worst = [], 0
            for outcome, group in sorted(groups.items()):
                got = solve(tuple(sorted(set(group))), remaining-a.cost)
                if got is None:
                    break
                worst = max(worst, got[0]); children.append((outcome, got[1]))
            else:
                candidate = (a.cost+worst, Policy(None, a.name, tuple(children)))
                if best is None or candidate[0] < best[0]:
                    best = candidate
        return best

    found = solve(tuple((i, i) for i in possible), budget)
    if found is None:
        return PolicyResult(None, None, budget, "NO_POLICY_WITHIN_BUDGET")
    verify_policy(carrier, target, found[1], budget, possible)
    return PolicyResult(found[1], found[0], budget, "CERTIFIED_FINITE_POLICY")


def verify_policy(carrier, target, policy, budget, possible=None):
    """Separate exhaustive execution oracle; no planner recursion reused."""
    target.validate(carrier)
    if type(budget) is not int or not 0 <= budget <= 16 or type(policy) is not Policy:
        raise CarrierError("typed policy and bounded budget required")
    possible = tuple(range(carrier.size)) if possible is None else possible
    if resolve_target(carrier, target, possible).status == "INCOHERENT":
        raise CarrierError("policy needs a nonempty support")
    worst = 0
    for initial in possible:
        state, spent, node = initial, 0, policy
        for _ in range(budget+2):
            if node.answer is not None:
                if (type(node.answer) is not Q or node.operation is not None or node.children or
                        node.answer != target.values[initial]):
                    raise CarrierError("unsound target policy leaf")
                worst = max(worst, spent)
                break
            a = carrier.operation(node.operation)
            if spent+a.cost > budget:
                raise CarrierError("policy exceeds resource budget")
            children = dict(node.children)
            if len(children) != len(node.children) or a.outputs[state] not in children:
                raise CarrierError("missing or duplicated outcome branch")
            node = children[a.outputs[state]]
            state = a.next_states[state]; spent += a.cost
        else:
            raise CarrierError("nonterminating/cyclic policy")
    return worst


def first_step_erasure_obstruction(carrier, target):
    """One forced target-conflicting merge for EVERY possible first action.

    A nonempty returned tuple is a finite certificate that no single-copy
    policy can decide this ORIGINAL target at any horizon. None makes no
    such claim. Both indistinguishability and backaction are model-relative.
    """
    target.validate(carrier)
    if not carrier.instruments or len(set(target.values)) < 2:
        return None
    witnesses = []
    for a in carrier.instruments:
        pair = next(((i, j) for i in range(carrier.size) for j in range(i+1, carrier.size)
            if a.outputs[i] == a.outputs[j] and a.next_states[i] == a.next_states[j]
            and target.values[i] != target.values[j]), None)
        if pair is None:
            return None
        i, j = pair
        witnesses.append((a.name, a.outputs[i], i, j, a.next_states[i]))
    return tuple(witnesses)


def prefix_value_interval(prefix, radix=16):
    """Closed enclosure for all infinite radix continuations; not normality."""
    if (type(radix) is not int or radix < 2 or type(prefix) is not tuple or
            any(type(d) is not int or not 0 <= d < radix for d in prefix)):
        raise CarrierError("valid exact radix digit prefix required")
    integer = 0
    for d in prefix:
        integer = radix*integer+d
    scale = radix**len(prefix)
    return Q(integer, scale), Q(integer+1, scale)


def from_contextual_field(field):
    """Native adapter: imports the real CZB type; never uses a local API shim."""
    from .contextual_zero_navigation import SourceField
    if not isinstance(field, SourceField):
        raise CarrierError("native contextual SourceField required")
    n = len(field.states)
    instruments = tuple(Instrument("probe:"+p.name, "CZB:Q:"+p.name,
        tuple(p.readout.at(s) for s in field.states), tuple(range(n)), p.cost)
        for p in field.probes)
    instruments += tuple(Instrument("move:"+m.name, "CZB:silent", (Q(0),)*n,
                         m.successor, m.cost) for m in field.moves)
    return Carrier(field.source_id, n, instruments)
