"""Recursive Meta-SUCC: finite source-indexed relations and signed interaction holonomy.

No physical source attestation, real-world joint experiment, analytic Weil sign, or
proof of RH is implied.  The finite structures here are *declared* mathematical
source laws and explicitly witnessed consequences of those laws.

META-01..05: relational join, exact projection, recursive arity closure.
META-06..10: signed transport cycles, global frustration and exact certificates.
All computations are integer, tuple, or fractions.Fraction arithmetic.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from typing import Optional


class MetaError(ValueError):
    """Malformed source contract, unlicensed transport, or invalid certificate."""


def _token(s: str) -> bool:
    return isinstance(s, str) and bool(s.strip())


def _rational(x):
    if type(x) is int or isinstance(x, Fraction):
        return Fraction(x)
    raise MetaError("an exact integer or rational coefficient is required")


@dataclass(frozen=True)
class SourceWorld:
    """A declared COMPLETE FINITE original-source relation; not sensor evidence."""
    source_id: str
    epoch: int
    basis: str
    coordinates: tuple[str, ...]
    domains: tuple[tuple[str, ...], ...]
    states: tuple[tuple[str, ...], ...]

    def __post_init__(self):
        if not _token(self.source_id) or not _token(self.basis) or type(self.epoch) is not int or self.epoch < 0:
            raise MetaError("source ID, basis and nonnegative epoch required")
        if not self.coordinates or len(set(self.coordinates)) != len(self.coordinates) or any(not _token(c) for c in self.coordinates):
            raise MetaError("nonempty named coordinates without duplicates required")
        if len(self.domains) != len(self.coordinates):
            raise MetaError("domain/coordinate arity mismatch")
        if any(not d or len(set(d)) != len(d) or any(not _token(x) for x in d) for d in self.domains):
            raise MetaError("finite nonempty domains with distinct values required")
        if not self.states or len(self.states) != len(set(self.states)):
            raise MetaError("nonempty unique complete original-source states required")
        if any(len(s) != len(self.coordinates) or any(s[i] not in self.domains[i] for i in range(len(s))) for s in self.states):
            raise MetaError("source state outside declared product carrier")

    def universe(self) -> tuple[tuple[str, ...], ...]:
        return tuple(product(*self.domains))

    def projection(self, scope: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
        ix = _scope_indices(self.coordinates, scope)
        return tuple(sorted({tuple(s[i] for i in ix) for s in self.states}))

    def source_law(self, name: str, scope: tuple[str, ...]) -> "RelationLaw":
        return RelationLaw(name, self.source_id, self.epoch, self.basis,
                           scope, self.projection(scope), "SOURCE_PROJECTION", ())


def _scope_indices(coordinates: tuple[str, ...], scope: tuple[str, ...]) -> tuple[int, ...]:
    if not isinstance(scope, tuple) or not scope or len(set(scope)) != len(scope):
        raise MetaError("nonempty scope with no duplicates required")
    if any(x not in coordinates for x in scope):
        raise MetaError("unknown model-coordinate in scope")
    indices = tuple(coordinates.index(x) for x in scope)
    if indices != tuple(sorted(indices)):
        raise MetaError("scopes must use the original declared coordinate order")
    return indices


@dataclass(frozen=True)
class RelationLaw:
    """A local allowed-tuple relation, with explicitly typed provenance."""
    name: str
    source_id: str
    epoch: int
    basis: str
    scope: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    kind: str = "DECLARED_THEORY"
    parents: tuple[str, ...] = ()

    def __post_init__(self):
        if any(not _token(s) for s in (self.name, self.source_id, self.basis)):
            raise MetaError("named law, source and basis required")
        if type(self.epoch) is not int or self.epoch < 0:
            raise MetaError("nonnegative source epoch required")
        if not self.scope or len(set(self.scope)) != len(self.scope):
            raise MetaError("relation must have a nonempty unique coordinate scope")
        if self.kind not in ("DECLARED_THEORY", "SOURCE_PROJECTION", "MODEL_DERIVED"):
            raise MetaError("unknown provenance kind")
        if self.kind == "MODEL_DERIVED" and not self.parents:
            raise MetaError("derived law must name its witness parent laws")
        if len(set(self.rows)) != len(self.rows) or any(len(row) != len(self.scope) for row in self.rows):
            raise MetaError("relation rows must be distinct with exact arity")


@dataclass(frozen=True)
class Derivation:
    """Finite proof: projection of the exact join plus full witnesses."""
    relation: RelationLaw
    witnesses: tuple[tuple[tuple[str, ...], tuple[str, ...]], ...]
    parent_names: tuple[str, ...]
    original_joint_count: int
    declared_source_mathematical_only: bool = True
    physical_probe_executed: bool = False


@dataclass(frozen=True)
class GhostRepair:
    ghost: tuple[str, ...]
    separating_scope: tuple[str, ...]
    rejected_projection: tuple[str, ...]
    source_law: RelationLaw
    new_candidate_count: int
    source_mathematically_declared_only: bool = True


@dataclass(frozen=True)
class ModelSystem:
    """A model of models and their simultaneous relational interaction laws.

    If world is present its states are a *complete declared mathematical source*
    inside every relation.  `joint_candidates` is only the logical CSP join:
    it is never called a physically performed joint observation.
    """
    source_id: str
    epoch: int
    basis: str
    coordinates: tuple[str, ...]
    domains: tuple[tuple[str, ...], ...]
    laws: tuple[RelationLaw, ...]
    world: Optional[SourceWorld] = None

    def __post_init__(self):
        if not _token(self.source_id) or not _token(self.basis) or type(self.epoch) is not int or self.epoch < 0:
            raise MetaError("source/epoch/basis contract required")
        if not self.coordinates or len(self.coordinates) != len(self.domains) or len(set(self.coordinates)) != len(self.coordinates):
            raise MetaError("unique coordinates and matching finite domains required")
        if any(not _token(x) for x in self.coordinates) or any(not d or len(set(d)) != len(d) for d in self.domains):
            raise MetaError("named finite nonempty coordinate domains required")
        if len(set(l.name for l in self.laws)) != len(self.laws):
            raise MetaError("duplicate law name")
        for l in self.laws:
            if (l.source_id, l.epoch, l.basis) != (self.source_id, self.epoch, self.basis):
                raise MetaError("unlicensed cross-source/epoch/basis model interaction")
            ix = _scope_indices(self.coordinates, l.scope)
            if any(any(row[j] not in self.domains[i] for j, i in enumerate(ix)) for row in l.rows):
                raise MetaError("law contains untyped coordinate values")
        # A model is never allowed to self-label an invented relation "derived":
        # its exact extension must be reproduced from PRECEDING licensed laws.
        for position, law in enumerate(self.laws):
            if law.kind != "MODEL_DERIVED":
                continue
            previous = {l.name: l for l in self.laws[:position]}
            if law.parents == ("TAUTOLOGICAL_UNIVERSE",):
                premises = ()
            else:
                if len(set(law.parents)) != len(law.parents) or any(p not in previous for p in law.parents):
                    raise MetaError("unreproducible derived relation or missing prior source law")
                premises = tuple(previous[p] for p in law.parents)
            ix = _scope_indices(self.coordinates, law.scope)
            expected = tuple(sorted({tuple(x[i] for i in ix) for x in self._join(premises)}))
            if law.rows != expected:
                raise MetaError("derived relation does not follow from declared model parents")
        if self.world is None and any(l.kind == "SOURCE_PROJECTION" for l in self.laws):
            raise MetaError("cannot call a projection source-exact without a declared original source")
        if self.world is not None:
            w = self.world
            if (w.source_id, w.epoch, w.basis, w.coordinates, w.domains) != (self.source_id, self.epoch, self.basis, self.coordinates, self.domains):
                raise MetaError("declared full source is from another source/epoch/basis/carrier")
            for l in self.laws:
                ix = _scope_indices(self.coordinates, l.scope)
                allowed = set(l.rows)
                if any(tuple(s[i] for i in ix) not in allowed for s in w.states):
                    raise MetaError("law excludes an admitted original source state")
                if l.kind == "SOURCE_PROJECTION" and l.rows != w.projection(l.scope):
                    raise MetaError("forged or incomplete exact source projection")

    def relation(self, name: str) -> RelationLaw:
        for l in self.laws:
            if l.name == name:
                return l
        raise MetaError("unknown relation name")

    def _join(self, laws: tuple[RelationLaw, ...]) -> tuple[tuple[str, ...], ...]:
        restrictions = [(_scope_indices(self.coordinates, l.scope), set(l.rows)) for l in laws]
        return tuple(x for x in product(*self.domains)
                     if all(tuple(x[i] for i in ix) in rows for ix, rows in restrictions))

    def joint_candidates(self) -> tuple[tuple[str, ...], ...]:
        return self._join(self.laws)

    def ghosts(self) -> tuple[tuple[str, ...], ...]:
        if self.world is None:
            raise MetaError("ghost status needs a declared complete source law")
        return tuple(x for x in self.joint_candidates() if x not in set(self.world.states))

    def strongest_consequence(self, scope: tuple[str, ...], parents: tuple[str, ...] | None = None,
                              name: str = "derived") -> Derivation:
        ix = _scope_indices(self.coordinates, scope)
        used = tuple(l.name for l in self.laws) if parents is None else parents
        if len(set(used)) != len(used):
            raise MetaError("derived model parents must be distinct")
        input_laws = tuple(self.relation(x) for x in used)
        witnesses = {}
        joint = self._join(input_laws)
        for state in joint:
            key = tuple(state[i] for i in ix)
            witnesses.setdefault(key, state)
        law = RelationLaw(name, self.source_id, self.epoch, self.basis, scope,
                          tuple(sorted(witnesses)), "MODEL_DERIVED", used or ("TAUTOLOGICAL_UNIVERSE",))
        return Derivation(law, tuple(sorted(witnesses.items())), used, len(joint))

    def check_derivation(self, d: Derivation) -> bool:
        if d.parent_names != d.relation.parents and d.parent_names != ():
            return False
        if not d.declared_source_mathematical_only or d.physical_probe_executed:
            return False
        try:
            expected = self.strongest_consequence(d.relation.scope, d.parent_names, d.relation.name)
        except MetaError:
            return False
        return (expected.relation == d.relation and expected.witnesses == d.witnesses and
                expected.original_joint_count == d.original_joint_count)

    def with_derived(self, d: Derivation) -> "ModelSystem":
        if not self.check_derivation(d):
            raise MetaError("unverified meta derivation witness")
        if any(l.name == d.relation.name for l in self.laws):
            raise MetaError("derived name collides with an existing model")
        return ModelSystem(self.source_id, self.epoch, self.basis,
                           self.coordinates, self.domains, self.laws + (d.relation,), self.world)

    def saturate(self, max_arity: int) -> "ModelSystem":
        """Add ALL model-of-model projections as proof-carrying consequences.

        No new source axiom enters; candidates must remain EXACTLY unchanged.
        The new higher-order model carries consequences not individually in the
        original graph, but cannot invent a missing global source law.
        """
        if type(max_arity) is not int or not (1 <= max_arity <= len(self.coordinates)):
            raise MetaError("arity must be 1..number of coordinates")
        base = self
        for k in range(1, max_arity+1):
            for sc in combinations(self.coordinates, k):
                name = "closure:" + ":".join(sc)
                if any(l.name == name for l in base.laws):
                    # Deterministic idempotent semantic saturation on re-entry.
                    proposed = base.strongest_consequence(sc, name=name)
                    if base.relation(name).rows != proposed.relation.rows:
                        raise MetaError("stale or forged closure relation")
                else:
                    proof = base.strongest_consequence(sc, name=name)
                    base = base.with_derived(proof)
        if base.joint_candidates() != self.joint_candidates():
            raise AssertionError("conservative derivation illegally changed joint candidates")
        return base

    def entails(self, global_allowed: tuple[tuple[str, ...], ...]) -> dict:
        """Conditional entailment from THIS declared finite theory (not empirical truth)."""
        joint = self.joint_candidates()
        if not joint:
            # An inconsistent theory can imply every formula classically,
            # but its empty candidate class is NOT authenticated source truth.
            return {"status": "INCONSISTENT_THEORY", "entailed": False,
                    "countermodel": None, "declared_mathematical_source_only": True,
                    "physical_joint_execution_verified": False}
        allowed = set(global_allowed)
        witness = next((x for x in joint if x not in allowed), None)
        return {"status": "ENTAILED_IN_DECLARED_THEORY" if witness is None else "COUNTERMODEL",
                "entailed": witness is None, "countermodel": witness,
                "declared_mathematical_source_only": True,
                "physical_joint_execution_verified": False}


def shadow_system(world: SourceWorld, max_arity: int) -> ModelSystem:
    n = len(world.coordinates)
    if type(max_arity) is not int or not (1 <= max_arity <= n):
        raise MetaError("1 <= max_arity <= number of coordinates required")
    laws = tuple(world.source_law("source:" + ":".join(sc), sc)
                 for k in range(1, max_arity+1)
                 for sc in combinations(world.coordinates, k))
    return ModelSystem(world.source_id, world.epoch, world.basis, world.coordinates,
                       world.domains, laws, world)


def reconstruction_arity(world: SourceWorld) -> int:
    for k in range(1, len(world.coordinates)+1):
        if set(shadow_system(world, k).joint_candidates()) == set(world.states):
            return k
    raise AssertionError("full-arity projection must reconstruct finite declared source")


def minimal_missing_interaction(world: SourceWorld, ghost: tuple[str, ...]) -> tuple[str, ...]:
    if ghost not in world.universe() or ghost in set(world.states):
        raise MetaError("candidate must be a well-typed ghost, not an admitted source state")
    for k in range(1, len(world.coordinates)+1):
        for scope in combinations(world.coordinates, k):
            ix = _scope_indices(world.coordinates, scope)
            if tuple(ghost[i] for i in ix) not in set(world.projection(scope)):
                return scope
    raise AssertionError("full source relation distinguishes every ghost")


def repair_ghost(system: ModelSystem, ghost: tuple[str, ...], name: str = "new-source-law") -> tuple[ModelSystem, GhostRepair]:
    if system.world is None:
        raise MetaError("cannot manufacture source law from an unverified mathematical hypothesis")
    if ghost not in system.ghosts():
        raise MetaError("not a current ghost, or no real source identification")
    scope = minimal_missing_interaction(system.world, ghost)
    law = system.world.source_law(name, scope)
    refined = ModelSystem(system.source_id, system.epoch, system.basis,
                          system.coordinates, system.domains, system.laws + (law,), system.world)
    if ghost in refined.joint_candidates() or len(refined.joint_candidates()) >= len(system.joint_candidates()):
        raise AssertionError("source-justified repair must strictly remove the ghost")
    ix = _scope_indices(system.coordinates, scope)
    receipt = GhostRepair(ghost, scope, tuple(ghost[i] for i in ix), law,
                          len(refined.joint_candidates()))
    return refined, receipt


def even_parity_world(n: int, parity: int = 0, source_id: str = "parity-source") -> SourceWorld:
    if type(n) is not int or n < 2 or n > 14 or parity not in (0, 1):
        raise MetaError("parity requires 2..14 bits and parity 0/1")
    cs = tuple("x" + str(i) for i in range(n))
    states = tuple(v for v in product(("0", "1"), repeat=n)
                   if sum(int(x) for x in v) % 2 == parity)
    return SourceWorld(source_id, 0, "fixed-binary", cs,
                       (("0", "1"),)*n, states)


@dataclass(frozen=True)
class SignedEdge:
    """An exact signed unitary (±1) transport, indexed by its source contract."""
    name: str
    start: str
    end: str
    sign: int
    weight: Fraction
    source_id: str
    epoch: int
    basis: str

    def __post_init__(self):
        if not all(_token(x) for x in (self.name, self.start, self.end)) or self.start == self.end:
            raise MetaError("edge must be named between two distinct model vertices")
        if type(self.sign) is not int or self.sign not in (-1, 1):
            raise MetaError("signed transport unitary is +1 or -1")
        if not _token(self.source_id) or not _token(self.basis) or type(self.epoch) is not int or self.epoch < 0:
            raise MetaError("an edge needs its own declared source, epoch and basis")
        w = _rational(self.weight)
        if w <= 0:
            raise MetaError("strictly positive exact transport cost required")
        object.__setattr__(self, "weight", w)


@dataclass(frozen=True)
class SignedCycle:
    root: str
    steps: tuple[tuple[str, bool], ...]


@dataclass(frozen=True)
class SignedGraph:
    """Finite graph of model-interaction maps; execution is not assumed."""
    source_id: str
    epoch: int
    basis: str
    vertices: tuple[str, ...]
    edges: tuple[SignedEdge, ...]

    def __post_init__(self):
        if not _token(self.source_id) or not _token(self.basis) or type(self.epoch) is not int or self.epoch < 0:
            raise MetaError("signed transport needs source, epoch and basis")
        if not self.vertices or len(set(self.vertices)) != len(self.vertices) or any(not _token(v) for v in self.vertices):
            raise MetaError("nonempty distinct model vertices required")
        if len(set(e.name for e in self.edges)) != len(self.edges):
            raise MetaError("duplicate edge ID")
        if any(e.start not in self.vertices or e.end not in self.vertices for e in self.edges):
            raise MetaError("transport endpoints outside the declared model family")
        if any((e.source_id, e.epoch, e.basis) != (self.source_id, self.epoch, self.basis)
               for e in self.edges):
            raise MetaError("unlicensed cross-source/epoch/basis unitary transport")

    def edge(self, name: str) -> SignedEdge:
        for e in self.edges:
            if e.name == name:
                return e
        raise MetaError("unlicensed transport edge")

    def oriented_cycle(self, cycle: SignedCycle) -> tuple[int, Fraction]:
        """Check simple closed walk and return (holonomy sign, total resistance)."""
        if cycle.root not in self.vertices or len(cycle.steps) < 2:
            raise MetaError("cycle needs an actual root and >=2 comparisons")
        cur = cycle.root
        visited = {cur}
        used_edges = set()
        product_sign, resistance = 1, Fraction(0)
        for i, (ename, forward) in enumerate(cycle.steps):
            edge = self.edge(ename)
            if type(forward) is not bool or ename in used_edges:
                raise MetaError("cycle must have explicitly oriented, nonrepeated edges")
            used_edges.add(ename)
            src, dst = (edge.start, edge.end) if forward else (edge.end, edge.start)
            if src != cur:
                raise MetaError("broken source-indexed path composition")
            cur = dst
            if cur in visited and not (i == len(cycle.steps)-1 and cur == cycle.root):
                raise MetaError("closed-walk certificate must be a simple cycle")
            visited.add(cur)
            product_sign *= edge.sign
            resistance += 1/edge.weight
        if cur != cycle.root:
            raise MetaError("holonomy witness fails to close")
        return product_sign, resistance

    def find_frustrated_cycle(self) -> Optional[SignedCycle]:
        """Fundamental cycle of a spanning forest with signed XOR/phase -1."""
        adj = {v: [] for v in self.vertices}
        for e in self.edges:
            adj[e.start].append((e.end, e.name, True, e.sign))
            adj[e.end].append((e.start, e.name, False, e.sign))
        potential = {}
        tree_edges = set()
        tree_adj = {v: [] for v in self.vertices}
        for root in self.vertices:
            if root in potential:
                continue
            potential[root] = 1
            todo = deque([root])
            while todo:
                cur = todo.popleft()
                for nxt, name, forward, sign in adj[cur]:
                    if nxt not in potential:
                        potential[nxt] = potential[cur]*sign
                        todo.append(nxt)
                        tree_edges.add(name)
                        tree_adj[cur].append((nxt, name, forward))
                        tree_adj[nxt].append((cur, name, not forward))
        for e in self.edges:
            if e.name in tree_edges or potential[e.start]*e.sign == potential[e.end]:
                continue
            root, finish = e.start, e.end
            paths = deque([(root, ())])
            seen = {root}
            path = None
            while paths:
                v, p = paths.popleft()
                if v == finish:
                    path = p
                    break
                for nxt, name, forward in tree_adj[v]:
                    if nxt not in seen:
                        seen.add(nxt)
                        paths.append((nxt, p + ((name, forward),)))
            if path is None:
                raise AssertionError("tree path missing from own forest")
            cyc = SignedCycle(root, path + ((e.name, False),))
            if self.oriented_cycle(cyc)[0] != -1:
                raise AssertionError("inconsistent fundamental cycle must be frustrated")
            return cyc
        return None

    def signed_assignment(self) -> dict[str, int] | None:
        """Return one globally zero-energy ±1 section, or None with obstruction."""
        if self.find_frustrated_cycle() is not None:
            return None
        out = {}
        adj = {v: [] for v in self.vertices}
        for e in self.edges:
            adj[e.start].append((e.end, e.sign))
            adj[e.end].append((e.start, e.sign))
        for root in self.vertices:
            if root in out:
                continue
            out[root] = 1
            queue = deque([root])
            while queue:
                v = queue.popleft()
                for other, sign in adj[v]:
                    if other not in out:
                        out[other] = out[v]*sign
                        queue.append(other)
        if any(out[e.end] != e.sign*out[e.start] for e in self.edges):
            raise AssertionError("coherent transport must give global section")
        return out

    def energy(self, values: dict[str, int | Fraction]) -> Fraction:
        if set(values) != set(self.vertices):
            raise MetaError("total original vertex assignment required")
        if any(type(x) is not int and not isinstance(x, Fraction) for x in values.values()):
            raise MetaError("exact rational states required")
        return sum((e.weight*(_rational(values[e.end]) - e.sign*_rational(values[e.start]))**2
                    for e in self.edges), Fraction(0))

    def boolean_frustration(self, values: dict[str, int]) -> Fraction:
        if set(values) != set(self.vertices) or any(type(x) is not int or x not in (-1, 1) for x in values.values()):
            raise MetaError("total signed Boolean states required")
        return self.energy(values) / 4

    def holonomy_root_lower_bound(self, cycle: SignedCycle, root_norm_sq: int | Fraction = 1) -> Fraction:
        """The sharp path bound E >= ((1-h)^2/R_C) |x_root|² for ±1 transport."""
        h, resistance = self.oriented_cycle(cycle)
        norm = _rational(root_norm_sq)
        if norm < 0:
            raise MetaError("nonnegative norm square required")
        return Fraction((1-h)**2, 1)*norm/resistance

    def signed_cycle_boolean_lower_bound(self, cycle: SignedCycle) -> Fraction:
        h, _ = self.oriented_cycle(cycle)
        if h != -1:
            return Fraction(0)
        return min(self.edge(name).weight for name, _ in cycle.steps)

    def verify_fractional_cycle_packing(self, packing: tuple[tuple[SignedCycle, Fraction], ...]) -> Fraction:
        """Proof certificate E_bool >= Σ λ_C using edge-capacity inequalities.

        Every frustrated cycle forces at least one unsatisfied edge; summing
        weighted cycle inequalities is valid whenever per-edge load<=weight.
        """
        loads = {e.name: Fraction(0) for e in self.edges}
        result = Fraction(0)
        for cycle, lam in packing:
            weight = _rational(lam)
            if weight < 0 or self.oriented_cycle(cycle)[0] != -1:
                raise MetaError("packing only permits nonnegative frustrated-cycle multipliers")
            result += weight
            for name, _ in cycle.steps:
                loads[name] += weight
        if any(loads[e.name] > e.weight for e in self.edges):
            raise MetaError("cycle certificate overloads a signed source edge")
        return result

    def explicit_coercivity_constant(self, cycle: SignedCycle) -> Fraction:
        """A proven full-state norm bound for a connected signed graph with h=-1.

        Fix cycle.root and any rooted spanning tree. For each vertex, R_v is
        total inverse edge cost of its tree path. For σ=2 (h=-1),
          energy >= (2|V|R_cycle/4 + 2Σ_v R_v)^-1 * Σ_v |x_v|².
        This bound is conservative (the spectrum can give a larger constant).
        """
        h, resistance = self.oriented_cycle(cycle)
        if h != -1:
            raise MetaError("coercivity requires a nontrivial signed holonomy")
        adj = {v: [] for v in self.vertices}
        for e in self.edges:
            adj[e.start].append((e.end, 1/e.weight))
            adj[e.end].append((e.start, 1/e.weight))
        root = cycle.root
        seen = {root}
        q = deque([(root, Fraction(0))])
        total_resistance = Fraction(0)
        while q:
            v, R = q.popleft()
            total_resistance += R
            for u, invw in adj[v]:
                if u not in seen:
                    seen.add(u)
                    q.append((u, R+invw))
        if len(seen) != len(self.vertices):
            raise MetaError("single-cycle coercivity does not control disconnected components")
        return 1/(Fraction(len(self.vertices), 2)*resistance + 2*total_resistance)


def shift_approximate_invariance(n: int) -> Fraction:
    """Exact ℓ²(Z) counterexample: normalized constant on [-n,n] under shift."""
    if type(n) is not int or n < 0:
        raise MetaError("nonnegative interval radius required")
    return Fraction(2, 2*n+1)

# ---------------------------------------------------------------------------
# Meta-meta layer: an exact two-dimensional unitary transport *groupoid*.
# Individual cycle models may each have fixed vectors and no spectral gap;
# a system of cycle holonomies can nevertheless force positive global energy.
# ---------------------------------------------------------------------------
Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]
Vector2 = tuple[Fraction, Fraction]


def matrix2(value) -> Matrix2:
    if len(value) != 2 or any(len(r) != 2 for r in value):
        raise MetaError("2x2 exact matrix required")
    return tuple(tuple(_rational(x) for x in r) for r in value)  # type: ignore


def _id2() -> Matrix2:
    return ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))


def _t2(a: Matrix2) -> Matrix2:
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def _mul2(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)), Fraction(0))
                       for j in range(2)) for i in range(2))  # type: ignore


def _sub2(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(tuple(a[i][j]-b[i][j] for j in range(2)) for i in range(2))  # type: ignore


def _matvec2(a: Matrix2, v: Vector2) -> Vector2:
    return tuple(sum((a[i][j]*v[j] for j in range(2)), Fraction(0))
                 for i in range(2))  # type: ignore


def _psd2(a: Matrix2) -> bool:
    return (a[0][1] == a[1][0] and a[0][0] >= 0 and a[1][1] >= 0
            and a[0][0]*a[1][1]-a[0][1]**2 >= 0)


@dataclass(frozen=True)
class OrthogonalEdge:
    name: str
    start: str
    end: str
    U: Matrix2
    weight: Fraction
    source_id: str
    epoch: int
    basis: str

    def __post_init__(self):
        if not all(_token(s) for s in (self.name, self.start, self.end, self.source_id, self.basis)) or self.start == self.end:
            raise MetaError("exact transport requires named distinct endpoints and original source")
        if type(self.epoch) is not int or self.epoch < 0:
            raise MetaError("transport epoch must be nonnegative")
        mat = matrix2(self.U)
        if _mul2(_t2(mat), mat) != _id2():
            raise MetaError("declared transport is NOT orthogonal: telescoping proof invalid")
        w = _rational(self.weight)
        if w <= 0:
            raise MetaError("positive exact edge weights required")
        object.__setattr__(self, "U", mat)
        object.__setattr__(self, "weight", w)


@dataclass(frozen=True)
class JointHolonomyCertificate:
    cycle_names: tuple[tuple[tuple[str, bool], ...], ...]
    holonomies: tuple[Matrix2, ...]
    resistance_total: Fraction
    joint_gram: Matrix2
    claimed_gap: Fraction
    full_state_coercivity: Fraction
    has_unconditional_Weil_identification: bool = False
    physical_source_authenticated: bool = False


@dataclass(frozen=True)
class OrthogonalMetaGraph:
    source_id: str
    epoch: int
    basis: str
    vertices: tuple[str, ...]
    edges: tuple[OrthogonalEdge, ...]

    def __post_init__(self):
        if not _token(self.source_id) or not _token(self.basis) or type(self.epoch) is not int or self.epoch < 0:
            raise MetaError("common source contract required")
        if not self.vertices or len(set(self.vertices)) != len(self.vertices) or any(not _token(v) for v in self.vertices):
            raise MetaError("unique named observer-model vertices required")
        if len({e.name for e in self.edges}) != len(self.edges):
            raise MetaError("distinct transport edges required")
        if any(e.start not in self.vertices or e.end not in self.vertices for e in self.edges):
            raise MetaError("unavailable model endpoint")
        if any((e.source_id,e.epoch,e.basis) != (self.source_id,self.epoch,self.basis) for e in self.edges):
            raise MetaError("unitary meta-model cannot mix unrelated source laws")

    def edge(self, name: str) -> OrthogonalEdge:
        for e in self.edges:
            if e.name == name:
                return e
        raise MetaError("unknown unitary transport")

    def cycle(self, cycle: SignedCycle) -> tuple[Matrix2, Fraction]:
        """Product of declared unitary maps around one oriented simple cycle."""
        if cycle.root not in self.vertices or len(cycle.steps) < 2:
            raise MetaError("based cycle required")
        cur, visited, used = cycle.root, {cycle.root}, set()
        holonomy, resistance = _id2(), Fraction(0)
        for i, (name, forward) in enumerate(cycle.steps):
            e = self.edge(name)
            if type(forward) is not bool or name in used:
                raise MetaError("no repeated or unoriented cycle comparisons")
            used.add(name)
            src, dst = (e.start,e.end) if forward else (e.end,e.start)
            if src != cur:
                raise MetaError("noncomposable cross-model path")
            cur = dst
            if cur in visited and not (i == len(cycle.steps)-1 and cur == cycle.root):
                raise MetaError("simple closed cycle required")
            visited.add(cur)
            # Orthogonality justifies the inverse traversal as U^T.
            holonomy = _mul2(e.U if forward else _t2(e.U), holonomy)
            resistance += 1/e.weight
        if cur != cycle.root:
            raise MetaError("cycle doesn't return to the source chart")
        return holonomy, resistance

    def energy(self, values: dict[str, tuple[int | Fraction, int | Fraction]]) -> Fraction:
        if set(values) != set(self.vertices):
            raise MetaError("total 2D assignment required on the original model family")
        data = {k: tuple(_rational(z) for z in val) for k, val in values.items()}
        if any(len(v) != 2 for v in data.values()):
            raise MetaError("2D source vectors required")
        return sum((e.weight*sum((x-y)**2 for x,y in zip(data[e.end],_matvec2(e.U,data[e.start])))
                    for e in self.edges), Fraction(0))

    def _tree_resistance_sum(self, root: str) -> Fraction:
        adj = {v: [] for v in self.vertices}
        for e in self.edges:
            adj[e.start].append((e.end, 1/e.weight))
            adj[e.end].append((e.start, 1/e.weight))
        seen={root}
        q=deque([(root,Fraction(0))])
        total=Fraction(0)
        while q:
            v,r=q.popleft()
            total += r
            for nxt,inverse in adj[v]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt,r+inverse))
        if seen != set(self.vertices):
            raise MetaError("joint holonomy cannot control an unconnected component")
        return total

    def certify_joint_gap(self, based_cycles: tuple[SignedCycle, ...],
                          multipliers: tuple[Fraction, ...],
                          claimed_gap: Fraction) -> JointHolonomyCertificate:
        """Check a rational 2x2 PSD certificate; conclude a WHOLE-GRAPH inequality.

        If sum λ_j (I-H_j)^T(I-H_j) >= δ I, δ>0, and all cycles have a
        common root, then E >= c * sum_vertex ||x_v||², with exact
          c = δ / [2|V| sum_j λ_j R_j + 2δ sum_v R_tree(v)].
        This is a new-to-SUCC synthesis of classical unitary graph methods,
        NOT the authentic signed arithmetic Weil form.
        """
        if not based_cycles or len(based_cycles) != len(multipliers):
            raise MetaError("each independent cycle model requires its own cost multiplier")
        if len({c.root for c in based_cycles}) != 1:
            raise MetaError("untransported holonomy roots do not share an operational basis")
        lambdas=tuple(_rational(lam) for lam in multipliers)
        if any(lam < 0 for lam in lambdas):
            raise MetaError("invalid negative proof multiplier")
        delta=_rational(claimed_gap)
        if delta <= 0:
            raise MetaError("strict global gap must be positive")
        G=((Fraction(0),Fraction(0)),(Fraction(0),Fraction(0)))
        holonomies=[]
        Rtot=Fraction(0)
        for cycle, lam in zip(based_cycles,lambdas):
            H,R=self.cycle(cycle)
            holonomies.append(H)
            Rtot += lam*R
            defect=_sub2(_id2(),H)
            gram=_mul2(_t2(defect),defect)
            G=tuple(tuple(G[i][j]+lam*gram[i][j] for j in range(2))
                    for i in range(2))  # type: ignore
        if not _psd2(_sub2(G,((delta,Fraction(0)),(Fraction(0),delta)))):
            raise MetaError("operator positivity proof requires a TRUE source-derived joint Gram gap")
        treeR=self._tree_resistance_sum(based_cycles[0].root)
        coeff=delta/(2*len(self.vertices)*Rtot+2*delta*treeR)
        return JointHolonomyCertificate(tuple(c.steps for c in based_cycles),
                                        tuple(holonomies),Rtot,G,delta,coeff)
