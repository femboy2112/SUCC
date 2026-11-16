"""Exact finite lawful-probe budget laboratory for source-typed observers.

A source-probe model is a DECLARED finite mathematical table; a probe being in
its menu does NOT authenticate availability in physical reality. Passive
identification, active single-copy identification, and equivariant/Markov-like
backward reconstruction are distinct contracts. No probability is inferred
from a set of possible states.

Pure standard library; all costs and stochastic certificates are rational.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from typing import Hashable

Q = Fraction


@dataclass(frozen=True)
class Probe:
    name: str
    outputs: tuple[Hashable, ...]
    cost: Fraction = Q(1)
    updates: tuple[int, ...] | None = None
    available: bool = True

    @property
    def is_passive(self) -> bool:
        return self.updates is None or self.updates == tuple(range(len(self.outputs)))


@dataclass(frozen=True)
class Carrier:
    """Finite source states 0..n-1, current report q, and lawful source actions."""

    q: tuple[int, ...]
    source_actions: tuple[tuple[int, ...], ...]
    probes: tuple[Probe, ...] = ()

    def __post_init__(self):
        n = len(self.q)
        if not n or any(type(x) is not int or x < 0 for x in self.q):
            raise ValueError("Source states and nonnegative integer report codes required")
        if set(self.q) != set(range(max(self.q) + 1)):
            raise ValueError("Report codes must be 0..ny-1 and surjective")
        if not self.source_actions:
            raise ValueError("Explicit source actions required, identity if appropriate")
        for t in self.source_actions:
            if len(t) != n or any(type(x) is not int or not 0 <= x < n for x in t):
                raise ValueError("Invalid total source action")
        names = set()
        for p in self.probes:
            if not p.name or p.name in names:
                raise ValueError("Probes require distinct nonempty names")
            names.add(p.name)
            if len(p.outputs) != n:
                raise ValueError("Every readout must be a total source-state function")
            try:
                for v in p.outputs:
                    hash(v)
                    if v != v:  # reject NaN/nonreflexive equalities in report charts
                        raise ValueError("Readout equality must be reflexive")
            except TypeError as exc:
                raise ValueError("Readout values must actually be hashable") from exc
            if type(p.cost) not in (int, Fraction) or p.cost <= 0:
                raise ValueError("Costs must be positive exact rationals")
            if type(p.available) is not bool:
                raise ValueError("Probe available flag must be explicit bool")
            if p.updates is not None and (len(p.updates) != n or
                    any(type(x) is not int or not 0 <= x < n for x in p.updates)):
                raise ValueError("Invalid total probe-induced state update")

    @property
    def nx(self) -> int:
        return len(self.q)

    @property
    def ny(self) -> int:
        return 1 + max(self.q)

    def admitted_passive(self) -> tuple[int, ...]:
        return tuple(i for i, p in enumerate(self.probes) if p.available and p.is_passive)

    def admitted_active(self) -> tuple[int, ...]:
        return tuple(i for i, p in enumerate(self.probes) if p.available)


@dataclass(frozen=True)
class Quotient:
    q: tuple[int, ...]
    report_actions: tuple[tuple[int, ...], ...]
    source_actions: tuple[tuple[int, ...], ...]

    @property
    def ny(self):
        return 1 + max(self.q)

    @property
    def fibers(self):
        return tuple(tuple(x for x, yy in enumerate(self.q) if yy == y)
                     for y in range(self.ny))


@dataclass(frozen=True)
class Noncongruence:
    action: int
    source_a: int
    source_b: int


def refined_quotient(c: Carrier, selected: tuple[int, ...] = ()) -> tuple[Quotient | None, Noncongruence | None]:
    """An actual report factor requires successors constant on each report fiber.

    Noncongruence is not 'no stochastic section': there is not even a lawful
    deterministic report T-action to lift. Source labels are NOT auto-exposed.
    """
    if len(selected) != len(set(selected)):
        raise ValueError("Repeated probe index")
    for i in selected:
        if type(i) is not int or not 0 <= i < len(c.probes) or not c.probes[i].available:
            raise ValueError("Probe outside actual permitted menu")
        if not c.probes[i].is_passive:
            raise ValueError("Destructive probe cannot be treated as persistent read-only refinement")
    signatures = tuple((c.q[x],) + tuple(c.probes[i].outputs[x] for i in selected)
                       for x in range(c.nx))
    labels: dict[tuple, int] = {}
    qnew = tuple(labels.setdefault(key, len(labels)) for key in signatures)
    u_all = []
    for gi, t in enumerate(c.source_actions):
        u: list[int | None] = [None] * len(labels)
        representative: list[int | None] = [None] * len(labels)
        for x, y in enumerate(qnew):
            yy = qnew[t[x]]
            if u[y] is not None and u[y] != yy:
                return None, Noncongruence(gi, int(representative[y]), x)
            u[y] = yy
            representative[y] = x
        assert all(y is not None for y in u)
        u_all.append(tuple(int(y) for y in u))
    return Quotient(qnew, tuple(u_all), c.source_actions), None


def verify_point(z: Quotient, s: tuple[int, ...]) -> bool:
    return (len(s) == z.ny and
            all(s[y] in z.fibers[y] for y in range(z.ny)) and
            all(t[s[y]] == s[u[y]]
                for t, u in zip(z.source_actions, z.report_actions)
                for y in range(z.ny)))


def point_lift(z: Quotient) -> tuple[int, ...] | None:
    for s in product(*z.fibers):
        if verify_point(z, s):
            return s
    return None


def verify_kernel(z: Quotient, K: tuple[tuple[Fraction, ...], ...]) -> bool:
    nx = len(z.q)
    if len(K) != z.ny or any(len(row) != nx for row in K):
        return False
    for y, row in enumerate(K):
        if (any(type(v) not in (Fraction, int) or v < 0 or
                (z.q[x] != y and v != 0) for x, v in enumerate(row)) or
                sum(row, Q(0)) != 1):
            return False
    for t, u in zip(z.source_actions, z.report_actions):
        for y in range(z.ny):
            pushed = [Q(0) for _ in range(nx)]
            for x, v in enumerate(K[y]):
                pushed[t[x]] += v
            if tuple(pushed) != K[u[y]]:
                return False
    return True


def _solve_unique_columns(A, b, support):
    """Solve A[:,support] v=b only if the selected columns are independent."""
    k = len(support)
    W = [[Q(row[j]) for j in support] + [Q(bi)] for row, bi in zip(A, b)]
    pivots = []
    top = 0
    for col in range(k):
        hit = next((row for row in range(top, len(W)) if W[row][col] != 0), None)
        if hit is None:
            return None
        W[top], W[hit] = W[hit], W[top]
        p = W[top][col]
        W[top] = [v / p for v in W[top]]
        for row in range(len(W)):
            if row != top and W[row][col]:
                v = W[row][col]
                W[row] = [a - v * b for a, b in zip(W[row], W[top])]
        pivots.append(top)
        top += 1
    if any(all(W[row][col] == 0 for col in range(k)) and W[row][k] != 0
           for row in range(len(W))):
        return None
    return tuple(W[row][k] for row in pivots)


def stochastic_lift(z: Quotient, *, max_states: int = 10) -> tuple[tuple[Fraction, ...], ...] | None:
    """Complete exact finite LP vertex search, explicitly capped.

    None is infeasibility *only if* search completes. Never a posterior.
    """
    nx = len(z.q)
    if nx > max_states:
        raise ValueError("Exact exhaustive LP search exceeds max_states cap")
    p = point_lift(z)
    if p is not None:
        return tuple(tuple(Q(int(x == p[y])) for x in range(nx)) for y in range(z.ny))
    uniform = tuple(tuple(Q(1, len(z.fibers[y])) if x in z.fibers[y] else Q(0)
                          for x in range(nx)) for y in range(z.ny))
    if verify_kernel(z, uniform):
        return uniform
    cols = tuple((y, x) for y in range(z.ny) for x in z.fibers[y])
    index = {yx: j for j, yx in enumerate(cols)}
    A, b = [], []
    for y in range(z.ny):
        row = [0] * len(cols)
        for x in z.fibers[y]:
            row[index[y, x]] = 1
        A.append(tuple(row)); b.append(1)
    for t, u in zip(z.source_actions, z.report_actions):
        for y in range(z.ny):
            for dst in z.fibers[u[y]]:
                row = [0] * len(cols)
                for src in z.fibers[y]:
                    if t[src] == dst:
                        row[index[y, src]] += 1
                row[index[u[y], dst]] -= 1
                A.append(tuple(row)); b.append(0)
    for size in range(z.ny, len(cols) + 1):
        for S in combinations(range(len(cols)), size):
            sol = _solve_unique_columns(A, b, S)
            if sol is None or any(v < 0 for v in sol):
                continue
            rows = [[Q(0)] * nx for _ in range(z.ny)]
            for j, v in zip(S, sol):
                y, x = cols[j]
                rows[y][x] = v
            K = tuple(tuple(row) for row in rows)
            if verify_kernel(z, K):
                return K
    return None


@dataclass(frozen=True)
class BudgetResult:
    cost: Fraction
    indices: tuple[int, ...]
    section_kind: str
    quotient: Quotient | None = None
    witness: object | None = None


def _candidate_sets(indices: tuple[int, ...], probes: tuple[Probe, ...], cap: int):
    if len(indices) > cap:
        raise ValueError("Exact probe subset enumeration exceeds cap")
    options = []
    for r in range(len(indices) + 1):
        for combo in combinations(indices, r):
            options.append((sum((Q(probes[i].cost) for i in combo), Q(0)), combo))
    options.sort(key=lambda item: (item[0], len(item[1]), item[1]))
    return options


def target_unresolved_pairs(c: Carrier, target: tuple[Hashable, ...]):
    if len(target) != c.nx:
        raise ValueError("Target length must equal source state count")
    return tuple((a, b) for a, b in combinations(range(c.nx), 2)
                 if c.q[a] == c.q[b] and target[a] != target[b])


def minimum_fixed_budget(c: Carrier, target: tuple[Hashable, ...], *, cap: int = 16) -> BudgetResult | None:
    """Exact weighted hitting-set for fixed repeatable nondisturbing probes.

    'None' means no separating fixed schedule from the *declared* menu.
    """
    pairs = target_unresolved_pairs(c, target)
    for price, S in _candidate_sets(c.admitted_passive(), c.probes, cap):
        if all(any(c.probes[i].outputs[a] != c.probes[i].outputs[b] for i in S)
               for a, b in pairs):
            return BudgetResult(price, S, 'target-identified')
    return None


def minimum_section_budget(c: Carrier, kind: str, *, cap: int = 16,
                           max_states: int = 10) -> BudgetResult | None:
    """Min-cost passive refinement admitting *exact* T-lift.

    Nonmonotone: an added legal readout can DESTROY a section. Enumerates all
    subsets and checks report congruence before lift feasibility.
    """
    if kind not in ('point', 'stochastic'):
        raise ValueError("kind must be 'point' or 'stochastic'")
    for price, S in _candidate_sets(c.admitted_passive(), c.probes, cap):
        z, defect = refined_quotient(c, S)
        if defect is not None:
            continue
        if kind == 'point':
            section = point_lift(z)
        else:
            section = stochastic_lift(z, max_states=max_states)
        if section is not None:
            return BudgetResult(price, S, kind, z, section)
    return None


# A belief carries (original state, current state), not just a current position.
Belief = frozenset[tuple[int, int]]


@dataclass
class AdaptiveSolution:
    """Exact sure-win worst-case budget and a verifiable finite policy certificate."""
    initial_costs: dict[Belief, Fraction | None]
    policy: dict[Belief, int]
    transitions: dict[Belief, tuple[tuple[Belief, ...], ...]]
    target: tuple[Hashable, ...]
    all_values: dict[Belief, Fraction | None]
    action_indices: tuple[int, ...]

    @property
    def worst_cost(self) -> Fraction | None:
        if any(v is None for v in self.initial_costs.values()):
            return None
        return max((Q(v) for v in self.initial_costs.values()), default=Q(0))


def _next_beliefs(B: Belief, c: Carrier, i: int) -> tuple[Belief, ...]:
    p = c.probes[i]
    by_output: dict[Hashable, set[tuple[int, int]]] = {}
    for original, current in B:
        new_current = current if p.updates is None else p.updates[current]
        by_output.setdefault(p.outputs[current], set()).add((original, new_current))
    return tuple(frozenset(v) for v in by_output.values())


def minimum_adaptive_budget(c: Carrier, target: tuple[Hashable, ...],
                            *, initial_beliefs: tuple[Belief, ...] | None = None,
                            max_beliefs: int = 10000) -> AdaptiveSolution:
    """Small finite single-copy AND/OR game: worst-case exact target recovery.

    Transcripts are read BEFORE probe update. Original/current pairs are kept
    explicitly. No reset is inferred and no favorable branch is discarded.
    """
    if len(target) != c.nx:
        raise ValueError("Target length mismatch")
    if initial_beliefs is None:
        initial_beliefs = tuple(frozenset((x, x) for x in range(c.nx) if c.q[x] == y)
                                for y in range(c.ny))
    else:
        for B in initial_beliefs:
            if not B or any(not isinstance(orig, int) or not isinstance(cur, int) or
                            orig < 0 or orig >= c.nx or cur < 0 or cur >= c.nx
                            for orig, cur in B):
                raise ValueError("Invalid nonempty source-labelled initial history belief")
    actions = c.admitted_active()
    discovered = set(initial_beliefs)
    stack = list(initial_beliefs)
    graph: dict[Belief, tuple[tuple[Belief, ...], ...]] = {}
    while stack:
        B = stack.pop()
        successors = tuple(_next_beliefs(B, c, i) for i in actions)
        graph[B] = successors
        for branches in successors:
            for nxt in branches:
                if nxt not in discovered:
                    discovered.add(nxt)
                    if len(discovered) > max_beliefs:
                        raise ValueError("Belief reachability exceeds explicit max_beliefs cap")
                    stack.append(nxt)

    # Backward finite-policy construction, starting with terminal target fibers.
    # Positive costs ensure a winning tree need never repeat a belief along a path.
    value: dict[Belief, Fraction | None] = {
        B: Q(0) if len({target[orig] for orig, _ in B}) == 1 else None
        for B in discovered
    }
    choices: dict[Belief, int] = {}
    for _ in range(len(discovered)):
        changed = False
        for B in discovered:
            if value[B] == 0:
                continue
            best = value[B]
            best_i = choices.get(B)
            for i, branches in zip(actions, graph[B]):
                if any(value[nxt] is None for nxt in branches):
                    continue
                cand = Q(c.probes[i].cost) + max(Q(value[nxt]) for nxt in branches)
                if best is None or cand < best or (cand == best and (best_i is None or i < best_i)):
                    best = cand
                    best_i = i
            if best is not None and (value[B] is None or best < value[B]):
                value[B] = best
                changed = True
                if best_i is not None:
                    choices[B] = best_i
            elif best is not None and best_i is not None and B not in choices:
                choices[B] = best_i
        if not changed:
            break
    return AdaptiveSolution({B: value[B] for B in initial_beliefs},
                            choices, graph, target, value, actions)


def verify_adaptive_solution(c: Carrier, solution: AdaptiveSolution) -> bool:
    """Independently verify upper policy, Bellman lower bounds, and losing trap.

    A root with value=None has a proof of IMPOSSIBILITY only if every probe
    retains a nonterminal branch in the certified losing region. Finite roots
    additionally require a policy tree achieving their certified Bellman value.
    """
    actions = c.admitted_active()
    if solution.action_indices != actions or len(solution.target) != c.nx:
        return False
    if set(solution.transitions) != set(solution.all_values):
        return False
    for B, branches_per_action in solution.transitions.items():
        goal = len({solution.target[orig] for orig, _ in B}) == 1
        val = solution.all_values[B]
        if len(branches_per_action) != len(actions) or any(
                old != _next_beliefs(B, c, i)
                for old, i in zip(branches_per_action, actions)):
            return False
        if goal:
            if val != 0:
                return False
            continue
        if val is None:
            # Adversary can remain in the nonterminal losing set for EVERY
            # available action, so no finite sure-win policy is possible.
            if any(not any(solution.all_values[ch] is None for ch in children)
                   for children in branches_per_action):
                return False
        else:
            exact_action = False
            for i, children in zip(actions, branches_per_action):
                if any(solution.all_values[ch] is None for ch in children):
                    continue
                bound = Q(c.probes[i].cost) + max(Q(solution.all_values[ch]) for ch in children)
                if val > bound:
                    return False  # invalid global Bellman lower bound
                if val == bound and solution.policy.get(B) == i:
                    exact_action = True
            if not exact_action:
                return False
    for root, promised in solution.initial_costs.items():
        if solution.all_values.get(root) != promised:
            return False
        if promised is None:
            continue
        def play(B: Belief, accumulated: Fraction, visited: frozenset[Belief]):
            if B in visited:
                return None
            if len({solution.target[orig] for orig, _ in B}) == 1:
                return accumulated
            if B not in solution.policy:
                return None
            i = solution.policy[B]
            if i not in actions:
                return None
            branch_costs = [play(nxt, accumulated + Q(c.probes[i].cost),
                                 visited | {B}) for nxt in _next_beliefs(B, c, i)]
            if any(v is None for v in branch_costs):
                return None
            return max(branch_costs)
        if play(root, Q(0), frozenset()) != promised:
            return False
    return True
