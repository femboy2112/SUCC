"""Classical stable repair and exact lawful acquisition of ORIGINAL labels.

Final repair storage, prior retained advice, and temporary controller memory
are different resources. Probe costs are abstract nonnegative rationals.
Destructive probes do not restore a source or authenticate its provenance.
"""
from collections import deque
from dataclasses import asdict, dataclass, replace
from fractions import Fraction as Q
from itertools import combinations
import json

from .future_safe_quotient import Machine, QuotientCertificate, minimize, verify_certificate


class RepairError(ValueError):
    pass


@dataclass(frozen=True)
class Repair:
    quotient: QuotientCertificate
    auxiliary: tuple[int, ...]
    labels: int
    bits: int


def enriched(machine: Machine, q: tuple[str, ...]) -> Machine:
    if (type(q) is not tuple or len(q) != len(machine.states)
            or any(type(v) is not str for v in q)):
        raise RepairError("One exact representation value per state required")
    return replace(machine, states=tuple(replace(s, observation=json.dumps([s.observation, y]))
                                        for s, y in zip(machine.states, q)))


def stable_repair(machine: Machine, q: tuple[str, ...]) -> Repair:
    """Greatest stable equivalence refining q AND all declared machine outputs."""
    cert = minimize(enriched(machine, q))
    block = {s: i for i, b in enumerate(cert.blocks) for s in b}
    local = {}
    codes = []
    for s, y in zip(machine.states, q):
        codebook = local.setdefault(y, {})
        codes.append(codebook.setdefault(block[s.name], len(codebook)))
    k = max(map(len, local.values()))
    return Repair(cert, tuple(codes), k, (k - 1).bit_length())


def check_repair(machine: Machine, q: tuple[str, ...], repair: Repair) -> bool:
    verify_certificate(enriched(machine, q), repair.quotient)
    if (type(repair.auxiliary) is not tuple or len(repair.auxiliary) != len(q)
            or any(type(c) is not int or c < 0 for c in repair.auxiliary)):
        raise RepairError("Finite nonnegative auxiliary codes required")
    block = {s: i for i, b in enumerate(repair.quotient.blocks) for s in b}
    per_q = {}
    for s, y in zip(machine.states, q):
        per_q.setdefault(y, set()).add(block[s.name])
    k = max(map(len, per_q.values()))
    if (type(repair.labels) is not int or repair.labels != k
            or type(repair.bits) is not int or repair.bits != (k - 1).bit_length()
            or any(c >= k for c in repair.auxiliary)):
        raise RepairError("Incorrect minimal fixed alphabet/bit bound")
    for i, j in combinations(range(len(q)), 2):
        # The produced repair is exactly the canonical one, not just sufficient.
        same = q[i] == q[j] and repair.auxiliary[i] == repair.auxiliary[j]
        if same != (block[machine.states[i].name] == block[machine.states[j].name]):
            raise RepairError("Auxiliary encoding does not realize canonical repair")
    return True


@dataclass(frozen=True)
class ProbeEdge:
    start: str
    action: str
    target: str
    receipt: str
    cost: Q


@dataclass(frozen=True)
class Acquisition:
    carriers: tuple[str, ...]
    actions: tuple[str, ...]
    edges: tuple[ProbeEdge, ...]
    origins: tuple[str, ...]
    initial: tuple[str, ...]
    target: tuple[str, ...]  # immutable ORIGINAL target class, not current state
    q: tuple[str, ...]       # initially known observation

    def __post_init__(self):
        for field in (self.carriers, self.actions, self.origins, self.initial, self.target, self.q):
            if type(field) is not tuple or any(type(v) is not str for v in field):
                raise RepairError("Immutable string tables required")
        if (not self.carriers or not self.origins
                or any(not v for v in self.carriers + self.actions + self.origins)
                or any(len(set(f)) != len(f) for f in (self.carriers, self.actions, self.origins))
                or not len(self.origins) == len(self.initial) == len(self.target) == len(self.q)
                or any(x not in self.carriers for x in self.initial)
                or type(self.edges) is not tuple):
            raise RepairError("Distinct typed carriers/origins and aligned tables required")
        seen = set()
        for e in self.edges:
            if (type(e) is not ProbeEdge or e.start not in self.carriers
                    or e.target not in self.carriers or e.action not in self.actions
                    or type(e.receipt) is not str or type(e.cost) is not Q or e.cost < 0
                    or (e.start, e.action) in seen):
                raise RepairError("Partial deterministic exact-cost probes required")
            seen.add((e.start, e.action))

    def start(self, subset: tuple[str, ...]) -> tuple:
        initial = dict(zip(self.origins, self.initial))
        if not subset or len(set(subset)) != len(subset) or any(x not in initial for x in subset):
            raise RepairError("Nonempty distinct original-source subset required")
        return tuple(sorted((x, initial[x]) for x in subset))


def initial_subsets(problem: Acquisition, max_subsets=4096) -> tuple[tuple, ...]:
    """Every nonempty initial subset of every q fiber; explicit exponential task."""
    fibers = {}
    for x, y in zip(problem.origins, problem.q):
        fibers.setdefault(y, []).append(x)
    if (type(max_subsets) is not int or max_subsets < 1
            or sum((1 << len(f)) - 1 for f in fibers.values()) > max_subsets):
        raise RepairError("UNKNOWN: initial subset cap exceeded")
    return tuple(problem.start(c) for f in fibers.values()
                 for k in range(1, len(f) + 1) for c in combinations(f, k))


def goal(problem: Acquisition, belief: tuple) -> bool:
    targets = dict(zip(problem.origins, problem.target))
    return len({targets[x] for x, _ in belief}) == 1


def branches(problem: Acquisition, belief: tuple, action: str) -> tuple | None:
    """Only universally enabled probes are legal; NO refusal oracle."""
    edges = {(e.start, e.action): e for e in problem.edges}
    outcomes = {}
    for original, current in belief:
        e = edges.get((current, action))
        if e is None:
            return None
        outcomes.setdefault((e.receipt, e.cost), []).append((original, e.target))
    return tuple((receipt, cost, tuple(sorted(pairs)))
                 for (receipt, cost), pairs in sorted(outcomes.items()))


def arena(problem: Acquisition, starts: tuple[tuple, ...], max_beliefs=4096) -> tuple:
    if type(max_beliefs) is not int or max_beliefs < 1:
        raise RepairError("Positive finite belief cap required")
    if type(starts) is not tuple or not starts or len(set(starts)) != len(starts):
        raise RepairError("Nonempty distinct starting beliefs required")
    origins, carriers = set(problem.origins), set(problem.carriers)
    q = dict(zip(problem.origins, problem.q))
    for b in starts:
        if (type(b) is not tuple or not b or any(type(p) is not tuple or len(p) != 2 for p in b)
                or any(x not in origins or z not in carriers for x, z in b)
                or len({x for x, _ in b}) != len(b) or b != tuple(sorted(b))
                or len({q[x] for x, _ in b}) != 1):
            raise RepairError("Canonical source-indexed belief in one q fiber required")
    seen = set(starts)
    queue = deque(starts)
    if len(seen) > max_beliefs:
        raise RepairError("UNKNOWN: belief cap exceeded")
    while queue:
        b = queue.popleft()
        if goal(problem, b):
            continue  # identification can stop immediately
        for a in problem.actions:
            for _, _, child in branches(problem, b, a) or ():
                if child not in seen:
                    if len(seen) >= max_beliefs:
                        raise RepairError("UNKNOWN: belief cap exceeded")
                    seen.add(child)
                    queue.append(child)
    return tuple(sorted(seen))


@dataclass(frozen=True)
class AcquisitionCertificate:
    starts: tuple[tuple, ...]
    beliefs: tuple[tuple, ...]
    values: tuple[Q | None, ...]  # None = no terminating lawful strategy
    policy: tuple[str | None, ...]
    ranks: tuple[int | None, ...]


def solve_acquisition(problem: Acquisition, starts=None, *, max_beliefs=4096):
    starts = initial_subsets(problem, max_beliefs) if starts is None else starts
    beliefs = arena(problem, starts, max_beliefs)
    children = {(b, a): branches(problem, b, a) for b in beliefs if not goal(problem, b)
                for a in problem.actions}
    value = {b: Q(0) if goal(problem, b) else None for b in beliefs}
    # Finite horizon, not arbitrary Bellman fixed points: zero cycles cannot win.
    for _ in range(len(beliefs)):
        newer = dict(value)
        for b in beliefs:
            if goal(problem, b):
                continue
            for a in problem.actions:
                out = children[b, a]
                if out is not None and all(value[c] is not None for _, _, c in out):
                    bound = max(cost + value[c] for _, cost, c in out)
                    if newer[b] is None or bound < newer[b]:
                        newer[b] = bound
        if newer == value:
            break
        value = newer
    # Build decreasing termination ranks using only optimal-cost actions.
    rank = {b: 0 for b in beliefs if goal(problem, b)}
    policy = {}
    for k in range(1, len(beliefs) + 1):
        added = {}
        for b in beliefs:
            if b in rank or value[b] is None:
                continue
            for a in problem.actions:
                out = children[b, a]
                if (out is not None and all(c in rank for _, _, c in out)
                        and max(cost + value[c] for _, cost, c in out) <= value[b]):
                    added[b] = k
                    policy[b] = a
                    break
        rank.update(added)
        if not added:
            break
    if any(value[b] is not None and b not in rank for b in beliefs):
        raise AssertionError("Finite optimum lacks a proper rank certificate")
    return AcquisitionCertificate(starts, beliefs, tuple(value[b] for b in beliefs),
                                  tuple(policy.get(b) for b in beliefs),
                                  tuple(rank.get(b) for b in beliefs))


def check_acquisition(problem: Acquisition, cert: AcquisitionCertificate) -> bool:
    """Local lower inequalities + proper policy upper certificate, no optimization."""
    if (type(cert) is not AcquisitionCertificate
            or cert.beliefs != arena(problem, cert.starts, max(4096, len(cert.beliefs)))
            or any(type(t) is not tuple or len(t) != len(cert.beliefs)
                   for t in (cert.values, cert.policy, cert.ranks))):
        raise RepairError("Incomplete or malformed acquisition certificate")
    values = dict(zip(cert.beliefs, cert.values))
    policies = dict(zip(cert.beliefs, cert.policy))
    ranks = dict(zip(cert.beliefs, cert.ranks))
    for b in cert.beliefs:
        v, a, r = values[b], policies[b], ranks[b]
        if v is not None and (type(v) is not Q or v < 0):
            raise RepairError("Exact nonnegative value or infinity required")
        if goal(problem, b):
            if v != Q(0) or a is not None or type(r) is not int or r != 0:
                raise RepairError("Goal must terminate at zero cost")
            continue
        for action in problem.actions:
            out = branches(problem, b, action)
            if out is not None and all(values[c] is not None for _, _, c in out):
                bound = max(cost + values[c] for _, cost, c in out)
                if v is None or v > bound:
                    raise RepairError("False all-action cost lower bound")
        if v is None:
            if a is not None or r is not None:
                raise RepairError("Losing belief cannot carry a winning policy")
            continue
        out = branches(problem, b, a) if a in problem.actions else None
        if (out is None or type(r) is not int or r <= 0
                or any(values[c] is None or type(ranks[c]) is not int or ranks[c] >= r
                       for _, _, c in out)
                or max(cost + values[c] for _, cost, c in out) > v):
            raise RepairError("False policy upper bound or nonterminating rank")
    return True


def partitions(items: tuple):
    """Each set partition once, independent of any target/diagnosis structure."""
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(tuple(rest)):
        yield ((first,),) + p
        for i in range(len(p)):
            yield p[:i] + ((first,) + p[i],) + p[i + 1:]


def advice_at_budget(problem: Acquisition, cert: AcquisitionCertificate, budget: Q,
                     *, max_partitions=100000) -> dict:
    """Exact weak hypergraph coloring: no infeasible set may be monochromatic.

    Codes are prior already-retained advice, not free new measurements. Working
    memory and final target storage are excluded from this code-size statistic.
    """
    if (type(budget) is not Q or budget < 0
            or type(max_partitions) is not int or max_partitions < 1):
        raise RepairError("Nonnegative rational acquisition budget required")
    check_acquisition(problem, cert)
    values = dict(zip(cert.beliefs, cert.values))
    fibers = {}
    for x, y in zip(problem.origins, problem.q):
        fibers.setdefault(y, []).append(x)
    codes, hyperedges, max_labels = {}, [], 1
    for fiber in fibers.values():
        feasible = {}
        for k in range(1, len(fiber) + 1):
            for subset in combinations(fiber, k):
                b = problem.start(subset)
                if b not in values:
                    raise RepairError("Pareto certificate must cover all original subsets")
                v = values[b]
                feasible[frozenset(subset)] = v is not None and v <= budget
        for subset, ok in feasible.items():
            if not ok and all(feasible[subset - {x}] for x in subset if len(subset) > 1):
                hyperedges.append(tuple(sorted(subset)))
        best = None
        for trial, partition in enumerate(partitions(tuple(fiber)), 1):
            if trial > max_partitions:
                raise RepairError("UNKNOWN: partition enumeration cap exceeded")
            if (all(feasible[frozenset(b)] for b in partition)
                    and (best is None or (len(partition), partition) < (len(best), best))):
                best = partition
        assert best is not None  # every singleton is identified without a probe
        max_labels = max(max_labels, len(best))
        for code, block in enumerate(best):
            codes.update((x, code) for x in block)
    return {"budget": budget, "labels": max_labels, "advice_bits": (max_labels - 1).bit_length(),
            "codes": tuple(codes[x] for x in problem.origins),
            "minimal_infeasible": tuple(sorted(hyperedges))}


def advice_frontier(problem: Acquisition, *, max_beliefs=4096) -> tuple[dict, ...]:
    cert = solve_acquisition(problem, max_beliefs=max_beliefs)
    values = dict(zip(cert.beliefs, cert.values))
    costs = sorted({Q(0)} | {values[b] for b in cert.starts if values[b] is not None})
    frontier = []
    for cost in costs:
        point = advice_at_budget(problem, cert, cost)
        if not frontier or point["advice_bits"] < frontier[-1]["advice_bits"]:
            frontier.append(point)
    return tuple(frontier)


def acquisition_payload(problem: Acquisition, cert: AcquisitionCertificate) -> dict:
    """Exact portable certificate; each rational is [numerator, denominator]."""
    def exact(value):
        if type(value) is Q:
            return [value.numerator, value.denominator]
        if isinstance(value, (tuple, list)):
            return [exact(x) for x in value]
        if isinstance(value, dict):
            return {k: exact(v) for k, v in value.items()}
        return value
    return {"contract": {"target": "original class", "costs_observed": True,
                         "refusal_oracle": False, "controller_memory_bounded": False,
                         "source_restoration_certified": False},
            "problem": exact(asdict(problem)), "certificate": exact(asdict(cert))}
