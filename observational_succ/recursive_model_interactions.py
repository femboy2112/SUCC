"""Source-typed finite recursive model-of-model interaction calculus.

Claim scope: a fully declared finite tuple carrier; algebraic joins are proofs
relative to the declared relations, not independent physical observations.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations

class ModelInteractionError(ValueError):
    pass

@dataclass(frozen=True)
class SourceCarrier:
    source_id: str
    epoch: int
    basis: str
    variables: tuple[str, ...]
    worlds: tuple[tuple[str, ...], ...]

    def __post_init__(self):
        if (not isinstance(self.source_id, str) or not self.source_id.strip()
            or not isinstance(self.basis, str) or not self.basis.strip()
            or type(self.epoch) is not int or self.epoch < 0):
            raise ModelInteractionError('original-source/epoch/basis contract required')
        if not self.variables or len(set(self.variables)) != len(self.variables):
            raise ModelInteractionError('named distinct source coordinates required')
        if not self.worlds or len(set(self.worlds)) != len(self.worlds):
            raise ModelInteractionError('unique nonempty candidate world table')
        if any(len(w) != len(self.variables) for w in self.worlds):
            raise ModelInteractionError('world schema mismatch')
        if any(any(not isinstance(v, str) for v in w) for w in self.worlds):
            raise ModelInteractionError('source coordinates must be labelled strings')

    def project(self, world, scope):
        indices = tuple(self.variables.index(v) for v in scope)
        return tuple(world[i] for i in indices)

    def scope(self, names):
        if not names or len(set(names)) != len(names) or any(v not in self.variables for v in names):
            raise ModelInteractionError('scope outside original source')
        return tuple(v for v in self.variables if v in names)

@dataclass(frozen=True)
class Model:
    source_id: str
    epoch: int
    basis: str
    scope: tuple[str, ...]
    allowed: frozenset[tuple[str, ...]]
    support: frozenset[str]
    level: int
    parents: tuple[str, ...] = ()

    def __post_init__(self):
        if (not self.source_id or not self.basis or type(self.epoch) is not int
            or self.epoch < 0 or not self.scope or not self.support
            or len(self.scope) != len(set(self.scope)) or type(self.level) is not int
            or self.level < 0 or any(len(r) != len(self.scope) for r in self.allowed)):
            raise ModelInteractionError('malformed proof-bearing model')


def leaf(carrier: SourceCarrier, name: str, scope, allowed) -> Model:
    if not isinstance(name, str) or not name.strip():
        raise ModelInteractionError('named input law required')
    ordered = carrier.scope(tuple(scope))
    if tuple(scope) != ordered:
        raise ModelInteractionError('input scope must use canonical source basis')
    rows = frozenset(tuple(r) for r in allowed)
    physically_possible = {carrier.project(w, ordered) for w in carrier.worlds}
    if not rows <= physically_possible:
        raise ModelInteractionError('law names non-source tuple')
    return Model(carrier.source_id, carrier.epoch, carrier.basis,
                 ordered, rows, frozenset((name,)), 0)


def _check(carrier, models):
    for m in models:
        if (m.source_id, m.epoch, m.basis) != (carrier.source_id, carrier.epoch, carrier.basis):
            raise ModelInteractionError('incompatible source/epoch/basis')
        if carrier.scope(m.scope) != m.scope:
            raise ModelInteractionError('scope orientation is not the source basis')


def join(carrier: SourceCarrier, left: Model, right: Model) -> Model:
    """Natural relational join; no Cartesian ghosts across shared variables."""
    _check(carrier, (left,right))
    scope = carrier.scope(left.scope+tuple(v for v in right.scope if v not in left.scope))
    ia = [scope.index(v) for v in left.scope]
    ib = [scope.index(v) for v in right.scope]
    rows = set()
    for world in carrier.worlds:
        out = carrier.project(world,scope)
        if tuple(out[i] for i in ia) in left.allowed and tuple(out[i] for i in ib) in right.allowed:
            rows.add(out)
    # Source-relative join: enumerate only original-source worlds.
    return Model(carrier.source_id, carrier.epoch, carrier.basis,
                 scope, frozenset(rows), left.support | right.support,
                 max(left.level,right.level)+1, ('join',))


def project(carrier: SourceCarrier, model: Model, scope) -> Model:
    _check(carrier,(model,))
    scope=carrier.scope(tuple(scope))
    if any(v not in model.scope for v in scope):
        raise ModelInteractionError('projection cannot invent variables')
    ids=[model.scope.index(v) for v in scope]
    rows=frozenset(tuple(r[i] for i in ids) for r in model.allowed)
    return Model(carrier.source_id,carrier.epoch,carrier.basis,scope,
                 rows,model.support,model.level+1,('projection',))


def global_fiber(carrier: SourceCarrier, models: tuple[Model,...]):
    _check(carrier,models)
    return tuple(w for w in carrier.worlds
                 if all(carrier.project(w,m.scope) in m.allowed for m in models))


def sound_for_declared_truth(carrier, model, actual_world):
    """May only return YES conditional on a DECLARED source world and law."""
    _check(carrier,(model,))
    if actual_world not in carrier.worlds:
        raise ModelInteractionError('actual source outside declared world table')
    return carrier.project(actual_world,model.scope) in model.allowed


def closure(carrier: SourceCarrier, roots: tuple[Model,...], depth: int=3):
    """Enumerate proof-carrying source-relative relation interactions by levels.

    Finite normalization merges repeated (scope,rows,support) signatures; the
    retained level is only the earliest depth, never proof authority itself.
    """
    _check(carrier, roots)
    if type(depth) is not int or not 0 <= depth <= 6 or len(roots) > 8:
        raise ModelInteractionError('bounded research exhaustion 0<=depth<=6, <=8 laws')
    items = {}
    for model in roots:
        items[(model.scope,model.allowed,model.support)] = model
    for _ in range(depth):
        previous=tuple(items.values())
        for i,a in enumerate(previous):
            for b in previous[i:]:
                result=join(carrier,a,b)
                key=(result.scope,result.allowed,result.support)
                if key not in items:items[key]=result
        if len(items)==len(previous):break
        if len(items)>2000:raise ModelInteractionError('finite budget exceeded')
    return tuple(items.values())


def min_unsat_cores(carrier: SourceCarrier, roots: tuple[Model,...]):
    _check(carrier,roots)
    cores=[]
    for size in range(1,len(roots)+1):
        for combo in combinations(roots,size):
            support=frozenset().union(*(m.support for m in combo))
            if any(c <= support for c in cores):continue
            if not global_fiber(carrier,combo):cores.append(support)
    return tuple(sorted(cores,key=lambda s:(len(s),tuple(sorted(s)))))


def goal_projection(carrier,roots,scope):
    """Project THE JOINT ORIGINAL SOURCE fiber, not arbitrary pair marginals."""
    canonical=carrier.scope(tuple(scope))
    fiber=global_fiber(carrier,roots)
    return frozenset(carrier.project(w,canonical) for w in fiber)


def available_information_signature(carrier,root_charts):
    """Total deterministic chart models cannot distinguish their joint fibers."""
    if not root_charts or any(len(report)!=len(carrier.worlds) for report in root_charts):
        raise ModelInteractionError('complete deterministic charts required')
    return tuple(tuple(chart[i] for chart in root_charts) for i in range(len(carrier.worlds)))


def derived_chart(signature, program):
    """No additional original-state discrimination from deterministic recursion."""
    if not callable(program): raise ModelInteractionError('declared program required')
    return tuple(program(report) for report in signature)


def distinguishable_pairs(reports):
    return frozenset((i,j) for i in range(len(reports)) for j in range(i+1,len(reports))
                     if reports[i]!=reports[j])
