"""Context-relative SUCC observer: lawful zero relations, probes, and movements.

Exact finite model: not an ontological claim about QFT, physical access, or
infinite mathematics. Actual state IDs occur ONLY in a labelled synthetic-model
execution, not in the observer's belief or its source-independent proof.

Zero claims are source-relative: polynomial equalities may hold on the whole
finite source carrier, only on the present belief fiber, or neither. A field
can carry multiple simultaneous compatible zeros without asserting a false
universal polynomial identity. No source string constitutes external attestation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache

from .coherent_zero_relations import Poly, ZeroRelation, ZeroDomainError


class NavigationError(ValueError):
    """Invalid source, context, epistemic step, or operational typing."""


def _q(x):
    if type(x) not in (int, Q):
        raise NavigationError("exact integer/Fraction required, no float or bool")
    return Q(x)


def _label(s):
    if type(s) is not str or not s.strip() or len(s) > 160:
        raise NavigationError("nonempty bounded source / operation label required")
    return s


def _budget(n, maximum=32):
    if type(n) is not int or not 0 <= n <= maximum:
        raise NavigationError("finite nonnegative resource budget required")
    return n


@dataclass(frozen=True)
class Probe:
    """An exact, declared source->Q measurement with positive resource cost."""
    source_id: str
    name: str
    readout: Poly
    cost: int = 1


@dataclass(frozen=True)
class Move:
    """An exact total source->same-source transition on a finite carrier."""
    source_id: str
    name: str
    successor: tuple[int, ...]
    cost: int = 1


@dataclass(frozen=True)
class SourceField:
    """A fully DECLARED finite world model, not externally certified Nature."""
    source_id: str
    coordinates: tuple[str, ...]
    states: tuple[tuple[Q, ...], ...]
    universal_zeros: tuple[ZeroRelation, ...]
    probes: tuple[Probe, ...]
    moves: tuple[Move, ...]

    def __post_init__(self):
        _label(self.source_id)
        names = self.coordinates
        if (type(names) is not tuple or not 1 <= len(names) <= 6
                or len(set(names)) != len(names)
                or any(type(s) is not str or not s for s in names)):
            raise NavigationError("one consistent finite source coordinate chart required")
        if (type(self.states) is not tuple or not 1 <= len(self.states) <= 24
                or any(type(s) is not tuple or len(s) != len(names)
                       or any(type(c) is not Q for c in s) for s in self.states)
                or len(set(self.states)) != len(self.states)):
            raise NavigationError("finite distinct exact source states required")
        if (type(self.universal_zeros) is not tuple or type(self.probes) is not tuple
                or type(self.moves) is not tuple):
            raise NavigationError("typed source zero/probe/move tuples required")
        for law in self.universal_zeros:
            if (not isinstance(law, ZeroRelation) or law.source_id != self.source_id
                    or law.expression.variables != self.coordinates):
                raise NavigationError("global zero law requires original-source chart")
            if any(law.expression.at(x) != 0 for x in self.states):
                raise NavigationError("claimed global zero false on declared source states")
        labels = set()
        for probe in self.probes:
            if (not isinstance(probe, Probe) or probe.source_id != self.source_id
                    or probe.readout.variables != names or _budget(probe.cost) == 0):
                raise NavigationError("probe must be a typed, paid source observation")
            _label(probe.name)
            if probe.name in labels:
                raise NavigationError("probe names must be unique")
            labels.add(probe.name)
        labels.clear()
        for move in self.moves:
            if (not isinstance(move, Move) or move.source_id != self.source_id
                    or type(move.successor) is not tuple or len(move.successor) != len(self.states)
                    or any(type(j) is not int or not 0 <= j < len(self.states)
                           for j in move.successor) or _budget(move.cost) == 0):
                raise NavigationError("move must be a typed, total, paid source transition")
            _label(move.name)
            if move.name in labels:
                raise NavigationError("move names must be unique")
            labels.add(move.name)

    def probe(self, name):
        return next((p for p in self.probes if p.name == name), None)

    def move(self, name):
        return next((m for m in self.moves if m.name == name), None)


@dataclass(frozen=True)
class RealizedEvent:
    """Model-simulated source event; it does not authenticate a physical outcome."""
    source_id: str
    kind: str
    name: str
    before: tuple[int, ...]
    after: tuple[int, ...]
    spent: int
    reported_value: Q | None


@dataclass(frozen=True)
class Knowledge:
    source_id: str
    possible: tuple[int, ...]
    budget: int
    journal: tuple[RealizedEvent, ...] = ()


def initial_knowledge(field, *, possible=None, budget=8):
    if not isinstance(field, SourceField):
        raise NavigationError("typed finite source needed")
    p = tuple(range(len(field.states))) if possible is None else possible
    _validate_possible(field, p)
    return Knowledge(field.source_id, p, _budget(budget))


def _validate_possible(field, possible):
    if (type(possible) is not tuple or not possible or possible != tuple(sorted(set(possible)))
            or any(type(k) is not int or not 0 <= k < len(field.states)
                   for k in possible)):
        raise NavigationError("nonempty sorted source-compatible belief fiber required")


def _validate_knowledge(field, knowledge):
    if not isinstance(knowledge, Knowledge) or knowledge.source_id != field.source_id:
        raise NavigationError("source/observer identity mismatch")
    _validate_possible(field, knowledge.possible)
    _budget(knowledge.budget)


def _actual_in_knowledge(field, knowledge, world_index):
    _validate_knowledge(field, knowledge)
    if type(world_index) is not int or world_index not in knowledge.possible:
        raise NavigationError("simulated realized world must remain within observer support")


def _charge(knowledge, cost):
    if knowledge.budget < cost:
        raise NavigationError("insufficient permitted observation/movement budget")


def model_observe(field, knowledge, world_index, name):
    """Only a named model probe can supply a synthetic observed outcome."""
    _actual_in_knowledge(field, knowledge, world_index)
    p = field.probe(name)
    if p is None:
        raise NavigationError("undeclared probe is inaccessible")
    _charge(knowledge, p.cost)
    value = p.readout.at(field.states[world_index])
    next_possible = tuple(i for i in knowledge.possible
                          if p.readout.at(field.states[i]) == value)
    event = RealizedEvent(field.source_id, "observation", p.name, knowledge.possible,
                          next_possible, p.cost, value)
    return Knowledge(field.source_id, next_possible, knowledge.budget-p.cost,
                     knowledge.journal + (event,))


def model_move(field, knowledge, world_index, name):
    """A legal action maps the world and ALL live epistemic alternatives."""
    _actual_in_knowledge(field, knowledge, world_index)
    m = field.move(name)
    if m is None:
        raise NavigationError("undeclared transition does not exist on this field")
    _charge(knowledge, m.cost)
    next_world = m.successor[world_index]
    next_possible = tuple(sorted({m.successor[i] for i in knowledge.possible}))
    event = RealizedEvent(field.source_id, "movement", m.name, knowledge.possible,
                          next_possible, m.cost, None)
    return (Knowledge(field.source_id, next_possible, knowledge.budget-m.cost,
                      knowledge.journal + (event,)), next_world)


@dataclass(frozen=True)
class ZeroStatus:
    """Separate finite-model global law, current-belief entailment, and possibility."""
    source_id: str
    transported: Poly
    global_on_finite_carrier: bool
    entailed_at_current_belief: bool
    compatible_with_current_belief: bool
    current_counterexamples: tuple[int, ...]
    global_counterexamples: tuple[int, ...]


@dataclass(frozen=True)
class CoordinateChart:
    """Q-polynomial source->target chart; no inverse is inferred."""
    source_id: str
    target_coordinates: tuple[str, ...]
    images: tuple[Poly, ...]


def inspect_zero(field, knowledge, relation, *, chart=None):
    """Check a zero on ALL finite model states vs only learned belief candidates."""
    _validate_knowledge(field, knowledge)
    if not isinstance(relation, Poly):
        raise NavigationError("polynomial zero statement required")
    if chart is None:
        if relation.variables != field.coordinates:
            raise NavigationError("zero coordinates differ; declare source chart")
        transported = relation
    else:
        if (not isinstance(chart, CoordinateChart) or chart.source_id != field.source_id
                or relation.variables != chart.target_coordinates
                or type(chart.images) is not tuple or len(chart.images) != len(chart.target_coordinates)
                or any(not isinstance(p, Poly) or p.variables != field.coordinates
                       for p in chart.images)):
            raise NavigationError("source/codomain chart must commute on declared variables")
        transported = relation.substitute(chart.images)
    wrong_global = tuple(i for i,x in enumerate(field.states) if transported.at(x) != 0)
    wrong_local = tuple(i for i in knowledge.possible if transported.at(field.states[i]) != 0)
    return ZeroStatus(field.source_id, transported, not wrong_global, not wrong_local,
                      len(wrong_local) < len(knowledge.possible), wrong_local, wrong_global)


def gauge_potential(values, anchor):
    """Relative scalar potential v(i)-v(anchor): invariant under v->v+c."""
    if (type(values) is not tuple or not values or type(anchor) is not int
            or not 0 <= anchor < len(values)):
        raise NavigationError("declared finite potential and reference port required")
    val=tuple(_q(v) for v in values)
    return tuple(v-val[anchor] for v in val)


@dataclass(frozen=True)
class Policy:
    """Proof-carrying min-max future plan in a finite declared toolkit."""
    source_id: str
    belief: tuple[int, ...]
    kind: str
    name: str | None
    worst_cost: int
    continuation: Policy | None = None
    outcomes: tuple[tuple[Q, Policy], ...] = ()


@dataclass(frozen=True)
class NavigationResult:
    source_id: str
    goal: tuple[int, ...]
    policy: Policy | None
    available_budget: int
    worst_cost: int | None
    status: str


def _goal(field, goal):
    if (type(goal) is not tuple or not goal or goal != tuple(sorted(set(goal)))
            or any(type(i) is not int or not 0 <= i < len(field.states) for i in goal)):
        raise NavigationError("nonempty finite source-indexed goal subset required")
    return goal


def _groups(field, belief, probe):
    grouped = {}
    for i in belief:
        val=probe.readout.at(field.states[i])
        grouped.setdefault(val, []).append(i)
    return tuple((k, tuple(v)) for k,v in sorted(grouped.items()))


def plan_guaranteed(field, knowledge, goal):
    """Solve finite worst-case adaptive reachability, with only paid operations.

    Success is *relative to this entire finite model/menu/budget*, not an
    assertion about all of mathematics or unobserved physical worlds.
    Uniform positive costs ensure recursion terminates. Every observation
    branch must be solvable; no guessed measurement outcomes allowed.
    """
    _validate_knowledge(field, knowledge)
    goal=_goal(field, goal)
    goal_set=set(goal)

    @lru_cache(None)
    def search(belief, budget):
        if all(i in goal_set for i in belief):
            return Policy(field.source_id, belief, "goal", None, 0)
        if budget == 0:
            return None
        options=[]
        for m in field.moves:
            if m.cost > budget:
                continue
            future=tuple(sorted({m.successor[i] for i in belief}))
            child=search(future,budget-m.cost)
            if child is not None:
                cost=m.cost+child.worst_cost
                options.append((cost,0,m.name,Policy(field.source_id,belief,"move",m.name,cost,child)))
        for p in field.probes:
            if p.cost>budget:
                continue
            branches=_groups(field,belief,p)
            if len(branches)<2:
                continue  # Cannot learn anything at a positive observation cost.
            children=[]
            for value,b in branches:
                child=search(b,budget-p.cost)
                if child is None:
                    break
                children.append((value,child))
            else:
                cost=p.cost+max(c.worst_cost for _,c in children)
                options.append((cost,1,p.name,Policy(field.source_id,belief,"probe",p.name,cost,None,tuple(children))))
        return min(options,key=lambda x:(x[0],x[1],x[2]))[3] if options else None

    found=search(knowledge.possible,knowledge.budget)
    return NavigationResult(field.source_id,goal,found,knowledge.budget,
                            found.worst_cost if found else None,
                            "guaranteed_within_declared_toolkit" if found else "no_guarantee_within_declared_toolkit")


def check_policy(field, knowledge, goal, policy):
    """Independent universal verification of a policy's declared branching.

    Rechecks action maps, observation partitions, terminal condition, costs,
    and strict source identity, rather than trusting a planner's success flag.
    """
    _validate_knowledge(field, knowledge)
    goal=_goal(field,goal)
    goals=set(goal)
    if not isinstance(policy,Policy) or policy.source_id!=field.source_id:
        raise NavigationError("wrong proof policy source")

    def verify(p,belief,budget):
        if p.source_id!=field.source_id or p.belief!=belief or p.worst_cost<0:
            raise NavigationError("policy lies about source/belief/cost")
        if p.kind == "goal":
            if (p.name is not None or p.continuation is not None or p.outcomes
                    or p.worst_cost!=0 or not set(belief).issubset(goals)):
                raise NavigationError("goal node was not proved for all possible worlds")
            return 0
        if p.kind == "move":
            m=field.move(p.name)
            if m is None or m.cost>budget or p.continuation is None or p.outcomes:
                raise NavigationError("illegal move branch")
            next_b=tuple(sorted({m.successor[i] for i in belief}))
            actual=m.cost+verify(p.continuation,next_b,budget-m.cost)
        elif p.kind == "probe":
            probe=field.probe(p.name)
            if probe is None or probe.cost>budget or p.continuation is not None:
                raise NavigationError("illegal probe branch")
            branches=_groups(field,belief,probe)
            if len(branches)<2 or len(p.outcomes)!=len(branches) or any(
                 x!=y for (x,_),(y,_) in zip(branches,p.outcomes)):
                raise NavigationError("incomplete or invented observation outcomes")
            actual=probe.cost+max(verify(child,next_b,budget-probe.cost)
                                  for (value,next_b),(_,child) in zip(branches,p.outcomes))
        else:
            raise NavigationError("unknown proof policy constructor")
        if p.worst_cost!=actual or actual>budget:
            raise NavigationError("false worst-case budget certificate")
        return actual

    return verify(policy,knowledge.possible,knowledge.budget)


def realize_policy_in_model(field, knowledge, world_index, goal, policy):
    """Synthetic full execution for ONE hidden model state; not a physical run."""
    _actual_in_knowledge(field, knowledge, world_index)
    check_policy(field,knowledge,goal,policy)
    world=world_index
    current=knowledge
    p=policy
    while p.kind!="goal":
        if p.kind=="move":
            current,world=model_move(field,current,world,p.name)
            p=p.continuation
        else:
            current=model_observe(field,current,world,p.name)
            val=current.journal[-1].reported_value
            p=dict(p.outcomes)[val]
    if world not in goal or not set(current.possible).issubset(set(goal)):
        raise ArithmeticError("policy failed original-source hidden world")
    return current,world
