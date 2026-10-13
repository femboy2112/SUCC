"""CAMBRIAN C exact finite witnesses for realization and interface repairs.

The infinite compactness and covering minimality claims are proved in the
companion dossier, not by these finite computations.  Original source types
and action relations are declared inputs, not authenticated physical data.
Existing finite-category and permutation-graph implementations are reused.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product

from .core import DomainError
from .voltage_cover_synthesis import PermutationGraph
from .yoneda import (
    Arrow, DivisibilityCategory, PathCategory, enumerate_natural_transforms,
    representable_natural_transform, validate_yoneda,
)


class FiniteFunctionCategory:
    """Full finite-set category on the specified small cardinalities.

    Adapter to the repository's existing literal Yoneda checker.  Every
    function, identity, and composite is retained; no path truncation.
    """
    def __init__(self, cardinalities=(1, 2)):
        if (not cardinalities or len(set(cardinalities)) != len(cardinalities)
                or any(type(n) is not int or not 1 <= n <= 3 for n in cardinalities)):
            raise DomainError("Small positive finite-set cardinalities required")
        self.objects = tuple(cardinalities)

    def hom(self, a, b):
        if a not in self.objects or b not in self.objects:
            raise DomainError("Finite-set object outside declared category")
        return tuple(Arrow(a, b, values) for values in product(range(b), repeat=a))

    def identity(self, a):
        if a not in self.objects:
            raise DomainError("Finite-set object outside declared category")
        return Arrow(a, a, tuple(range(a)))

    def compose(self, left, right):
        if (right.target != left.source or right not in self.hom(right.source, right.target)
                or left not in self.hom(left.source, left.target)):
            raise DomainError("Invalid finite-set composite")
        return Arrow(right.source, left.target, tuple(left.word[i] for i in right.word))


@dataclass(frozen=True)
class FiniteHistorySystem:
    """A finite prefix of changing source types and relational instruments.

    The relation at t records all admissible post-instrument source states;
    receipts[t] is the exact source-state preimage of that time's receipt.
    No reset, determinism, stationarity, or probability law is assumed.
    """
    spaces: tuple[tuple[str, ...], ...]
    transitions: tuple[frozenset[tuple[str, str]], ...]
    receipts: tuple[frozenset[str], ...]
    source_id: str

    def __post_init__(self):
        if (not isinstance(self.source_id, str) or not self.source_id
                or not self.spaces
                or len(self.transitions) + 1 != len(self.spaces)
                or len(self.receipts) != len(self.spaces)):
            raise DomainError("Declare typed source, relation, and receipt at each time")
        for space, receipt in zip(self.spaces, self.receipts):
            if (not space or len(set(space)) != len(space)
                    or any(not isinstance(s, str) or not s for s in space)
                    or not receipt <= set(space)):
                raise DomainError("Receipt or source coordinate outside declared type")
        for t, relation in enumerate(self.transitions):
            if any(x not in self.spaces[t] or y not in self.spaces[t+1]
                   for x, y in relation):
                raise DomainError("Transition mixes undeclared changing source types")

    def prefix_paths(self, depth: int) -> tuple[tuple[str, ...], ...]:
        """Independent history enumeration, including literal middle witnesses."""
        if type(depth) is not int or not 0 <= depth < len(self.spaces):
            raise DomainError("Finite prefix depth outside supplied source horizon")
        paths = tuple((s,) for s in self.spaces[0] if s in self.receipts[0])
        for t in range(depth):
            paths = tuple(path + (y,) for path in paths for y in self.spaces[t+1]
                          if (path[-1], y) in self.transitions[t]
                          and y in self.receipts[t+1])
        return paths

    def support_history(self) -> tuple[frozenset[str], ...]:
        """Exact powerset memory: only states with an actual matched past survive."""
        support = [frozenset(self.receipts[0])]
        for t, relation in enumerate(self.transitions):
            support.append(frozenset(y for x, y in relation
                                     if x in support[-1] and y in self.receipts[t+1]))
        return tuple(support)

    def first_impossible_prefix(self) -> int | None:
        return next((t for t, states in enumerate(self.support_history())
                     if not states), None)


def restricted_yoneda_controls() -> dict:
    """Literal presheaves and naturality, not only counts or labels."""
    thin = DivisibilityCategory((1, 2, 3, 6))
    # Hom(1,2) and Hom(1,3) are singleton sets.  D={1} sees spurious
    # inverse natural transformations, although C has no 2<->3 arrows.
    forward = enumerate_natural_transforms(thin, 2, 3, (1,))
    backward = enumerate_natural_transforms(thin, 3, 2, (1,))
    inverse = bool(forward and backward) and all(
        backward[0][1][forward[0][1][a]] == a for a in thin.hom(1, 2))
    paths = PathCategory((1, 2, 3, 6), (2, 3))
    parallel = paths.hom(1, 6)
    blind = [representable_natural_transform(paths, f, (6,)) for f in parallel]
    seeing = [representable_natural_transform(paths, f, (1,)) for f in parallel]
    finite_sets = FiniteFunctionCategory()
    retract_probe = {f"{a}_to_{b}": validate_yoneda(finite_sets, a, b, (2,))
                     for a in finite_sets.objects for b in finite_sets.objects}
    return {
        "object_source_hom_2_to_3": len(thin.hom(2, 3)),
        "restricted_natural_isomorphism_2_3": inverse,
        "restricted_spurious_natural_transforms": len(forward),
        "parallel_source_paths": [list(f.word) for f in parallel],
        "blind_context_collapses_parallel_arrows": blind[0] == blind[1],
        "precursor_identity_context_distinguishes": seeing[0] != seeing[1],
        "full_yoneda": validate_yoneda(paths, 1, 6),
        "single_retract_probe_fully_faithful": all(v["surjective"] for v in retract_probe.values()),
        "single_retract_probe_hom_nat_counts": {
            k: [v["source_hom_count"], v["natural_transform_count"]]
            for k, v in retract_probe.items()},
        "ignoring_probe_endomorphism_laws_gives_256_instead_of_4":
            len(finite_sets.hom(2, 2)) ** len(finite_sets.hom(2, 2)),
    }


def glue_constraint_sections(
        variables: tuple[str, ...],
        charts: tuple[dict[str, int], ...],
        constraints: tuple[tuple[tuple[str, ...], frozenset[tuple[int, ...]]], ...],
        *, require_constraint_cover: bool = True) -> dict[str, int]:
    """Glue literal source witnesses in the constraint-adapted coverage.

    Every source constraint scope must lie in one chart.  Matching coarse
    observation images alone do not provide such witnesses.
    """
    if len(set(variables)) != len(variables):
        raise DomainError("Distinct source coordinates required")
    allowed_vars = set(variables)
    if (any(not set(chart) <= allowed_vars for chart in charts)
            or set().union(*(set(c) for c in charts)) != allowed_vars):
        raise DomainError("Charts must cover exactly declared source coordinates")
    for scope, allowed in constraints:
        if (not set(scope) <= allowed_vars or len(set(scope)) != len(scope)
                or any(len(row) != len(scope) for row in allowed)):
            raise DomainError("Malformed source constraint scope")
        if require_constraint_cover and not any(set(scope) <= set(c) for c in charts):
            raise DomainError("Cover omits a cross-chart source constraint")
    global_section = {}
    for chart in charts:
        for variable, value in chart.items():
            if variable in global_section and global_section[variable] != value:
                raise DomainError("Literal source witnesses disagree on overlap")
            global_section[variable] = value
        for scope, allowed in constraints:
            if set(scope) <= set(chart) and tuple(chart[v] for v in scope) not in allowed:
                raise DomainError("Local source certificate violates its own constraint")
    if any(tuple(global_section[v] for v in scope) not in allowed
           for scope, allowed in constraints):
        raise DomainError("Glued assignment violates omitted source constraint")
    return global_section


def orbit_section_cover(graph: PermutationGraph, root_value: int) -> dict:
    """The stabilizer cover for ONE desired section, not full trivialization.

    Its sheets form H.root_value, with exact based monodromy action.
    Minimality uses the subgroup-index proof in the dossier; this code
    verifies connectedness, covering fibers, and the constructed section.
    """
    if type(root_value) is not int or not 0 <= root_value < graph.fiber_size:
        raise DomainError("Desired root section value outside source fiber")
    group = graph.holonomy_group()
    orbit = tuple(sorted({h[root_value] for h in group}))
    stabilizer = tuple(h for h in group if h[root_value] == root_value)
    tree = graph.tree_transports()
    vertices = frozenset((v, y) for v in graph.vertices for y in orbit)
    edges = tuple(((u, y), (v, loop[y]), p)
                  for (u, v, p), loop in zip(graph.edges, graph.fundamental_loop_permutations())
                  for y in orbit)
    section = {(v, y): tree[v][y] for v, y in vertices}
    valid = all(p[section[a]] == section[b] for a, b, p in edges)
    adj = {v: [] for v in vertices}
    for a, b, _ in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen, queue = {(graph.vertices[0], root_value)}, [(graph.vertices[0], root_value)]
    for at in queue:
        for nxt in adj[at]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    if not valid or seen != set(vertices) or len(group) != len(orbit) * len(stabilizer):
        raise ArithmeticError("Constructed source section-cover laws failed")
    # Deck permutations of a connected cover centralize its monodromy
    # action.  A nonregular stabilizer cover may have ONLY the identity
    # deck transformation, so deck invariance alone is not descent.
    generators = graph.fundamental_loop_permutations()
    deck_maps = []
    for values in permutations(orbit):
        deck = dict(zip(orbit, values))
        if all(deck[g[y]] == g[deck[y]] for g in generators for y in orbit):
            deck_maps.append(deck)
    deck_invariant = all(tree[v][deck[y]] == tree[v][y]
                         for deck in deck_maps for v in graph.vertices for y in orbit)
    return {
        "source_id": graph.source_id,
        "root_value": root_value,
        "holonomy_order": len(group),
        "stabilizer_order": len(stabilizer),
        "minimum_degree_for_this_section": len(orbit),
        "minimum_degree_for_all_transport_trivialization": len(group),
        "source_section_valid": valid,
        "connected": seen == set(vertices),
        "orbit_cover_deck_group_order": len(deck_maps),
        "constructed_section_deck_invariant": deck_invariant,
        "constructed_section_descends_to_base": len(orbit) == 1,
        "vertices": tuple(sorted(vertices)),
    }


def relational_compose(left: frozenset[tuple], right: frozenset[tuple]) -> frozenset[tuple]:
    """Existentially eliminate exactly the SAME internal source witness."""
    return frozenset((x, z) for x, m in left for n, z in right if m == n)


def coarse_interface_composition(left: frozenset[tuple], right: frozenset[tuple],
                                 quotient: dict) -> frozenset[tuple]:
    if any(m not in quotient for _, m in left) or any(m not in quotient for m, _ in right):
        raise DomainError("Missing original source witness in interface quotient")
    projected_left = frozenset((x, quotient[m]) for x, m in left)
    projected_right = frozenset((quotient[m], z) for m, z in right)
    return relational_compose(projected_left, projected_right)


def canonical_interface_refinement(states: tuple, quotient: dict,
                                    right: frozenset[tuple]) -> dict:
    """Generate coarsest refinement preserving q and ALL right boundary outputs.

    Constructor, not template search: source states acquire signatures
    (q(state), exact set of possible right outputs).  Its universal property
    is stated in the dossier.  Repeated state-changing contexts require the
    corresponding entire future behavior, not just this one-step interface.
    """
    if len(set(states)) != len(states) or set(quotient) != set(states):
        raise DomainError("Complete source interface domain required")
    if any(m not in quotient for m, _ in right):
        raise DomainError("Right boundary relation contains undeclared source states")
    return {m: (quotient[m], frozenset(z for n, z in right if n == m)) for m in states}


def geometry_demo() -> dict:
    states = ("m0", "m1")
    q = {m: 0 for m in states}
    left = frozenset({("in", "m0")})
    right = frozenset({("m1", "out")})
    refined = canonical_interface_refinement(states, q, right)
    nonabelian = PermutationGraph(("root",),
        (("root", "root", (1, 0, 2)), ("root", "root", (0, 2, 1))), 3)
    nonfree = PermutationGraph(("root",), (("root", "root", (1, 0, 2)),), 3)
    # A source-changing nondeterministic instrument erases an observed bit,
    # while the support state retains which causal histories remain possible.
    history = FiniteHistorySystem(
        (("old0", "old1"), ("newA", "newB"), ("final",)),
        (frozenset({("old0", "newA"), ("old0", "newB"), ("old1", "newB")}),
         frozenset({("newA", "final"), ("newB", "final")})),
        (frozenset({"old0"}), frozenset({"newA", "newB"}), frozenset({"final"})),
        "cambrian-changing-destructive-source")
    # The missing cross-chart constraint x=y makes the singleton cover false.
    bad_constraint = ((("x", "y"), frozenset({(0, 0), (1, 1)})),)
    try:
        glue_constraint_sections(("x", "y"), ({"x": 0}, {"y": 1}), bad_constraint)
    except DomainError as exc:
        missing_constraint_receipt = str(exc)
    else:
        raise ArithmeticError("Negative gluing control accepted an impossible source")
    return {
        "yoneda": restricted_yoneda_controls(),
        "sheaf_missing_constraint_control": missing_constraint_receipt,
        "nonabelian_section_cover": orbit_section_cover(nonabelian, 0),
        "nonfree_fixed_section_cover": orbit_section_cover(nonfree, 2),
        "causal_history_paths": [list(path) for path in history.prefix_paths(2)],
        "causal_support_history": [sorted(layer) for layer in history.support_history()],
        "actual_interface_composite": sorted(relational_compose(left, right)),
        "coarse_spurious_composite": sorted(coarse_interface_composition(left, right, q)),
        "constructed_repair_composite": sorted(coarse_interface_composition(left, right, refined)),
        "constructor_class_count": len(set(refined.values())),
        "infinite_compactness_verified_by_python": False,
        "mathematical_novelty_established": False,
    }
