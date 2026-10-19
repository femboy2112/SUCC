"""Nondeterministic public-belief safety with exact, source-bound certificates.

Declared finite models only. Possible transitions have no inferred probability.
Missing action rows are unavailable, never silently completed by failure/reset.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from types import MappingProxyType
from typing import Mapping


class CausalError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Report:
    outcome: str
    cost: Q
    observation: str

    def __post_init__(self):
        if (any(type(v) is not str or not v for v in (self.outcome, self.observation))
                or type(self.cost) not in (int, Q) or self.cost < 0):
            raise CausalError("Exact typed public outcome/cost/observation required")
        object.__setattr__(self, "cost", Q(self.cost))


@dataclass(frozen=True)
class Edge:
    target: str
    outcome: str = "ok"
    cost: Q = Q(1)

    def __post_init__(self):
        if (type(self.target) is not str or not self.target or type(self.outcome) is not str
                or not self.outcome or type(self.cost) not in (int, Q) or self.cost < 0):
            raise CausalError("Named target/outcome and nonnegative exact cost required")
        object.__setattr__(self, "cost", Q(self.cost))


@dataclass(frozen=True)
class Source:
    source_id: str
    basis: str
    states: tuple[str, ...]
    actions: tuple[str, ...]
    original: Mapping[str, str]
    observation: Mapping[str, str]
    transitions: Mapping[tuple[str, str], tuple[Edge, ...]]

    def __post_init__(self):
        for v in (self.source_id, self.basis):
            if type(v) is not str or not v:
                raise CausalError("Source identity and basis required")
        for seq in (self.states, self.actions):
            if (type(seq) is not tuple or not seq or len(set(seq)) != len(seq)
                    or any(type(v) is not str or not v for v in seq)):
                raise CausalError("Distinct nonempty named carrier and grammar required")
        for name in ("original", "observation"):
            data = dict(getattr(self, name))
            if set(data) != set(self.states) or any(type(v) is not str or not v for v in data.values()):
                raise CausalError("Total original tags and observations required")
            object.__setattr__(self, name, MappingProxyType(data))
        rows = dict(self.transitions)
        for key, row in rows.items():
            if (type(key) is not tuple or len(key) != 2 or key[0] not in self.states
                    or key[1] not in self.actions or type(row) is not tuple or not row
                    or any(type(e) is not Edge or e.target not in self.states for e in row)
                    or len(set(row)) != len(row)):
                raise CausalError("Nonempty distinct edges on declared state/action required")
            if any(self.original[key[0]] != self.original[e.target] for e in row):
                raise CausalError("Unauthorized original-source change")
        object.__setattr__(self, "transitions", MappingProxyType(rows))

    def report(self, edge):
        return Report(edge.outcome, edge.cost, self.observation[edge.target])

    def digest(self):
        data = [self.source_id, self.basis, self.states, self.actions,
                sorted(self.original.items()), sorted(self.observation.items()),
                [(s, a, [(e.target, e.outcome, str(e.cost)) for e in row])
                 for (s, a), row in sorted(self.transitions.items())]]
        return hashlib.sha256(json.dumps(data, separators=(",", ":")).encode()).hexdigest()


def _belief(model, belief, *, nonempty=True):
    if (type(belief) is not frozenset or not belief <= set(model.states)
            or (nonempty and not belief) or len({model.observation[s] for s in belief}) > 1):
        raise CausalError("Complete belief must be a single public observation fiber subset")


def post(model, belief, action):
    """Existential public successor supports; safe availability is separate."""
    result = {}
    for s in model.states:
        if s in belief:
            for edge in model.transitions.get((s, action), ()):
                result.setdefault(model.report(edge), set()).add(edge.target)
    return {label: frozenset(states) for label, states in result.items()}


def safe_menu(model, belief):
    return tuple(a for a in model.actions if all((s, a) in model.transitions for s in belief))


@dataclass(frozen=True)
class Policy:
    action: str | None = None
    branches: tuple[tuple[Report, "Policy"], ...] = ()


@dataclass(frozen=True)
class Blocker:
    action: str
    unavailable_state: str | None = None
    report: Report | None = None
    child: "Loss | None" = None


@dataclass(frozen=True)
class Loss:
    blockers: tuple[Blocker, ...]


@dataclass(frozen=True)
class Certificate:
    status: str
    source_digest: str
    initial: frozenset[str]
    horizon: int
    policy: Policy | None = None
    loss: Loss | None = None
    checked_nodes: int = 0


def synthesize(model, initial, horizon, *, max_nodes=100000):
    """Exact finite-horizon AND/OR synthesis and dual obstruction tree.

    Every possible outcome branch must continue to the full horizon. An
    unavailable hidden branch is a loss, never a postselection opportunity.
    Exhausting the explicit node budget returns UNRESOLVED.
    """
    _belief(model, initial)
    if type(horizon) is not int or not 0 <= horizon <= 128 or type(max_nodes) is not int or max_nodes < 0:
        raise CausalError("Bounded nonnegative integer horizon and node budget required")
    cache, checked = {}, 0

    def visit(belief, depth):
        nonlocal checked
        key = belief, depth
        if key in cache:
            return cache[key]
        checked += 1
        if checked > max_nodes:
            raise OverflowError
        if depth == 0:
            answer = Policy()
        else:
            blockers = []
            for action in model.actions:
                missing = next((s for s in model.states if s in belief and
                                (s, action) not in model.transitions), None)
                if missing is not None:
                    blockers.append(Blocker(action, unavailable_state=missing))
                    continue
                branches = []
                for report, successor in sorted(post(model, belief, action).items()):
                    child = visit(successor, depth - 1)
                    if isinstance(child, Loss):
                        blockers.append(Blocker(action, report=report, child=child))
                        break
                    branches.append((report, child))
                else:
                    answer = Policy(action, tuple(branches))
                    break
            else:
                answer = Loss(tuple(blockers))
        cache[key] = answer
        return answer

    try:
        answer = visit(initial, horizon)
    except OverflowError:
        return Certificate("UNRESOLVED", model.digest(), initial, horizon, checked_nodes=checked)
    if isinstance(answer, Policy):
        return Certificate("PUBLIC_POLICY_EXISTS", model.digest(), initial, horizon,
                           policy=answer, checked_nodes=checked)
    return Certificate("NO_PUBLIC_POLICY", model.digest(), initial, horizon,
                       loss=answer, checked_nodes=checked)


def verify_certificate(model, initial, horizon, cert, *, max_nodes=100000):
    """Independent direct private-frontier replay / AND-OR certificate check.

    No synthesis cache, safe_menu or post implementation is trusted. False
    denotes non-certification (including malformed input or verifier budget).
    """
    try:
        _belief(model, initial)
        if (type(cert) is not Certificate or type(horizon) is not int or not 0 <= horizon <= 128
                or type(max_nodes) is not int or max_nodes < 0 or cert.source_digest != model.digest()
                or cert.initial != initial or cert.horizon != horizon):
            return False
        count = 0

        def tick():
            nonlocal count
            count += 1
            if count > max_nodes:
                raise OverflowError

        def win(frontier, depth, policy):
            tick()
            if type(policy) is not Policy:
                return False
            if depth == 0:
                return policy.action is None and policy.branches == ()
            if policy.action not in model.actions or type(policy.branches) is not tuple:
                return False
            paths = {}
            for path in frontier:
                tick()
                state = path[-1]
                row = model.transitions.get((state, policy.action))
                if row is None:
                    return False
                for edge in row:
                    tick()
                    if model.original[state] != model.original[edge.target]:
                        return False
                    report = Report(edge.outcome, edge.cost, model.observation[edge.target])
                    paths.setdefault(report, []).append(path + (edge.target,))
            children = dict(policy.branches)
            if len(children) != len(policy.branches) or set(children) != set(paths):
                return False
            return all(win(tuple(paths[r]), depth - 1, children[r]) for r in paths)

        def lose(belief, depth, loss):
            tick()
            if depth == 0 or type(loss) is not Loss or type(loss.blockers) is not tuple:
                return False
            if tuple(b.action for b in loss.blockers) != model.actions:
                return False
            for blocker in loss.blockers:
                tick()
                if type(blocker) is not Blocker:
                    return False
                if blocker.unavailable_state is not None:
                    if (blocker.report is not None or blocker.child is not None
                            or blocker.unavailable_state not in belief or
                            (blocker.unavailable_state, blocker.action) in model.transitions):
                        return False
                    continue
                if blocker.report is None or blocker.child is None:
                    return False
                # Future blocker is valid only after a uniformly legal action.
                if any((s, blocker.action) not in model.transitions for s in belief):
                    return False
                successor = set()
                for s in belief:
                    tick()
                    for edge in model.transitions[(s, blocker.action)]:
                        tick()
                        if Report(edge.outcome, edge.cost, model.observation[edge.target]) == blocker.report:
                            successor.add(edge.target)
                if not successor or not lose(frozenset(successor), depth - 1, blocker.child):
                    return False
            return True

        if cert.status == "PUBLIC_POLICY_EXISTS" and cert.loss is None:
            return win(tuple((s,) for s in sorted(initial)), horizon, cert.policy)
        if cert.status == "NO_PUBLIC_POLICY" and cert.policy is None:
            return lose(initial, horizon, cert.loss)
        return False
    except (CausalError, TypeError, AttributeError, KeyError, ValueError, OverflowError):
        return False


def simulation(left, right, *, bisimulation=False):
    """Greatest finite simulation relation. Pair (s,t): right simulates left.

    This is a behavioral comparison, not a source-identity credential.
    """
    relation = {(s, t) for s in left.states for t in right.states
                if left.observation[s] == right.observation[t]}

    def matches(first, second, s, t, rel):
        return all(any(first.report(e) == second.report(f) and (e.target, f.target) in rel
                       for f in second.transitions.get((t, a), ()))
                   for a in first.actions for e in first.transitions.get((s, a), ()))

    while True:
        inverse = {(t, s) for s, t in relation}
        new = {(s, t) for s, t in relation if matches(left, right, s, t, relation)
               and (not bisimulation or matches(right, left, t, s, inverse))}
        if new == relation:
            return frozenset(new)
        relation = new


@dataclass(frozen=True)
class Comparison:
    status: str
    witness: tuple[tuple[str, Report], ...] = ()
    reason: str = ""
    checked_pairs: int = 0


def compare_interfaces(left, li, right, ri, *, public_safe=False, max_pairs=100000):
    """Complete finite powerset-product comparison with separating transcript.

    public_safe=False compares possible traces. True compares safe menus and
    outcomes only along prefixes attainable by a common safe public policy.
    The latter is the exact finite interface for public safe-policy testing
    with stopping allowed. It is not private-state bisimulation.
    """
    _belief(left, li)
    _belief(right, ri)
    if type(max_pairs) is not int or max_pairs < 0:
        raise CausalError("Nonnegative pair budget required")
    if left.observation[next(iter(li))] != right.observation[next(iter(ri))]:
        return Comparison("DISTINGUISHED", reason="INITIAL_REPORT")
    queue, seen = deque([(li, ri, ())]), {(li, ri)}
    checked = 0
    while queue:
        l, r, history = queue.popleft()
        if checked >= max_pairs:
            return Comparison("UNRESOLVED", reason="PAIR_BUDGET", checked_pairs=checked)
        checked += 1
        if public_safe:
            lm, rm = set(safe_menu(left, l)), set(safe_menu(right, r))
            if lm != rm:
                return Comparison("DISTINGUISHED", history, "PUBLIC_MENU", checked)
            actions = sorted(lm)
        else:
            actions = sorted(set(left.actions) | set(right.actions))
        for action in actions:
            lp, rp = post(left, l, action), post(right, r, action)
            for report in sorted(set(lp) | set(rp)):
                if report not in lp or report not in rp:
                    return Comparison("DISTINGUISHED", history + ((action, report),),
                                      "POSSIBLE_REPORT", checked)
                pair = lp[report], rp[report]
                if pair not in seen:
                    seen.add(pair)
                    queue.append((*pair, history + ((action, report),)))
    return Comparison("EQUIVALENT", checked_pairs=checked)


def split_combined(n=2):
    """n-way family: equal may traces, no common continuation on split source.

    n>=2; the n source branches each enable their own action. Combined source
    enables every action after a. Public initial branch outcome is identical.
    """
    if type(n) is not int or not 2 <= n <= 64:
        raise CausalError("Family parameter must be integer 2..64")
    actions = ("a",) + tuple("b" + str(i) for i in range(n))
    split_states = ("root",) + tuple("s" + str(i) for i in range(n)) + ("end",)
    split_rows = {("root", "a"): tuple(Edge("s" + str(i)) for i in range(n))}
    split_rows.update({("s" + str(i), "b" + str(i)): (Edge("end", "done"),) for i in range(n)})
    combined_states = ("root", "middle", "end")
    combined_rows = {("root", "a"): (Edge("middle"),)}
    combined_rows.update({("middle", "b" + str(i)): (Edge("end", "done"),) for i in range(n)})

    def make(label, states, rows):
        return Source(label, "private-origin-public-label-cost", states, actions,
                      {s: label for s in states},
                      {s: s if s in ("root", "end") else "middle" for s in states}, rows)
    return make("split-" + str(n), split_states, split_rows), make("combined-" + str(n), combined_states, combined_rows)


def guard_source(n):
    """n private immutable sources, 2n actions, 2**n-1 distinct safe menus.

    test_j always runs, reporting hit/miss without changing the private source.
    guard_j is unavailable exactly at j. All nonempty beliefs can be reached
    through safe miss observations and have different uniform guard menus.
    This lower bound concerns an EXACT MENU INTERFACE, not winning-policy memory.
    """
    if type(n) is not int or not 1 <= n <= 16:
        raise CausalError("Guard family size must be integer 1..16")
    states = tuple(str(j) for j in range(n))
    actions = tuple("test_" + s for s in states) + tuple("guard_" + s for s in states)
    rows = {}
    for s in states:
        for j in states:
            rows[s, "test_" + j] = (Edge(s, "hit" if s == j else "miss"),)
            if s != j:
                rows[s, "guard_" + j] = (Edge(s),)
    return Source("guard-family-" + str(n), "immutable-original-guard-test", states, actions,
                  {s: "original-" + s for s in states}, {s: "hidden" for s in states}, rows)


def output_split_combined():
    """Same safe public interface but not bisimilar: split OUTPUT branches.

    There is one universally enabled action. Hidden branch u emits b, v emits c;
    combined m can emit b or c. Terminal tick loops emit z in both sources.
    """
    def make(label, states, rows):
        return Source(label, "output-only-branching", states, ("tick",),
                      {s: label for s in states},
                      {s: s if s in ("root", "end") else "middle" for s in states}, rows)
    left = make("output-split", ("root", "u", "v", "end"),
                {("root", "tick"): (Edge("u", "a"), Edge("v", "a")),
                 ("u", "tick"): (Edge("end", "b"),),
                 ("v", "tick"): (Edge("end", "c"),),
                 ("end", "tick"): (Edge("end", "z"),)})
    right = make("output-combined", ("root", "m", "end"),
                 {("root", "tick"): (Edge("m", "a"),),
                  ("m", "tick"): (Edge("end", "b"), Edge("end", "c")),
                  ("end", "tick"): (Edge("end", "z"),)})
    return left, right


def stochastic_contract(model, probabilities=None):
    """Explicit rational chance-kernel adapter for the acyclic split family.

    This is an additional declared probability model, not inferred from the
    nondeterministic source. The default explicitly chooses uniform rows.
    """
    from .no_ghost import Event, FiniteContract, Step
    if ("root" not in model.states or "end" not in model.states or "a" not in model.actions
            or model.observation["root"] != "root" or model.observation["end"] != "end"):
        raise CausalError("Adapter is restricted to the declared two-step family")
    for (s, a), row in model.transitions.items():
        for e in row:
            root_edge = (s == "root" and a == "a" and e.outcome == "ok"
                         and model.observation[e.target] == "middle")
            final_edge = (model.observation[s] == "middle" and a != "a"
                          and e.target == "end" and e.outcome == "done")
            if not (root_edge or final_edge) or e.cost != 1:
                raise CausalError("Adapter must preserve the actual two-step source rows")
    probabilities = probabilities or {}
    if not set(probabilities) <= set(model.transitions):
        raise CausalError("Chance overrides must refer to actual source rows")
    h1 = (("a", "ok"),)
    kernels = {}
    for (s, a), row in model.transitions.items():
        values = probabilities.get((s, a), (Q(1, len(row)),) * len(row))
        if (len(values) != len(row) or any(type(p) not in (int, Q) or p <= 0 for p in values)
                or sum(values, Q()) != 1):
            raise CausalError("Explicit full-support rational normalized chance law required")
        h = () if a == "a" else h1
        kernels[h, a, model.original[s], s] = tuple(Step(e.outcome, e.target, str(i), Q(p))
                                                       for i, (e, p) in enumerate(zip(row, values)))
    contract = FiniteContract(model.source_id + "-explicit-chance", model.basis,
                             tuple(sorted(set(model.original.values()))), model.states,
                             {s: 0 if s == "root" else 2 if s == "end" else 1 for s in model.states},
                             tuple(Event(a, frozenset() if a == "a" else frozenset({"a"}))
                                   for a in model.actions),
                             ((model.original["root"], "root", Q(1)),), kernels)
    return contract.validate()
