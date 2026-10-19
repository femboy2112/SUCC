"""Minimum-cost global obstruction repair for F_2 parity transport.

This module extends the odd-loop obstruction of
`observational_succ/meta_choice_descent.py` (research round #188) from the
*decision* problem "does a global F_2 section exist?" to the *optimization*
problem "what is the minimum lawful cost to make the obstructed local system
globally representable while preserving the original source laws?".

Fix a finite undirected (multi)graph ``G=(V,E)``, edge targets
``t_e in F_2``, repair costs ``w_e >= 0`` (exact integers or Fractions), and
vertex assignments ``x_v in F_2``.  The repair cost of an assignment is the
total weight of edges whose observed parity ``x_u (+) x_v`` disagrees with the
declared target::

    C(x) = sum_{e=(u,v)}  w_e * 1[ x_u (+) x_v != t_e ].

The minimum-cost global obstruction repair is::

    C_*  =  min_x  C(x).

EXACT RELATION TO WEIGHTED PARITY (Max-2-LIN over F_2).  "Satisfied" means
``x_u (+) x_v == t_e``.  Each edge is a two-variable F_2 linear equation
``x_u (+) x_v = t_e``; maximizing the satisfied weight is weighted Max-2-LIN(2).
With ``W = sum_e w_e`` the total weight and ``MaxSAT`` the maximum satisfiable
weight::

    C_*  =  W  -  MaxSAT            (exact; Proposition PR-1 in the dossier).

ALL-FLIP (every ``t_e = 1``) UNIT-WEIGHT (every ``w_e = 1``).  A unit edge is
satisfied iff ``x_u != x_v`` iff the edge is cut by the partition
``(x^{-1}(0), x^{-1}(1))``.  Hence ``MaxSAT = MaxCut(G)`` and::

    C_*  =  |E|  -  MaxCut(G)       (exact; Theorem PR-2 in the dossier).

SIGNED-GRAPH FRUSTRATION.  Put ``sigma_e = (-1)^{t_e} in {+1,-1}``.  An
assignment satisfies edge ``e`` exactly when it respects ``sigma_e`` in Harary's
sense, so ``C_*`` (unit weight) is the *frustration index* (line index of
balance) of the signed graph ``(G, sigma)``, and the weighted ``C_*`` is the
weighted frustration index.  The signed graph is balanced
(``frustration index == 0``) iff a global F_2 section exists iff
``[t] = 0`` in ``H^1(G; F_2)`` — exactly the #188 odd-loop criterion.

ISING GROUND STATE.  Put spins ``s_v = (-1)^{x_v} in {+1,-1}`` and couplings
``J_e = w_e * sigma_e``.  Then for the Hamiltonian
``H(s) = - sum_e J_e s_u s_v`` one has, for every ``x`` and its spins,
``H(s) = 2 C(x) - W``; hence the ground-state energy is
``E_min = 2 C_* - W`` (Proposition PR-3).

COMPUTATIONAL STATUS.  Computing ``C_*`` for general graphs/targets is
NP-hard: it contains weighted Max-2-LIN over F_2 and, via Theorem PR-2,
unweighted MaxCut (Karp 1972).  NP-hardness is a *finite-computation
complexity* statement, NOT noncomputability: ``C_*`` is a finite minimum over
``2^{|V|}`` assignments, always computed here by brute force.  In the
taxonomy of `docs/OBSERVER_PROOF_ACCESS.md` this is a **SimpleField** (a
verified finite program returns the exact answer); it is emphatically NOT an
**IdealHardField** (which requires a *proof that no computable selector
exists*).  Slowness is not noncomputability.

CHEAP EXACT FAMILIES (stated; see the dossier for citations):
  * Forests/trees: acyclic => no closed walk => ``C_* = 0`` for any ``t`` (a
    section always exists); solved in linear time by spanning-forest
    propagation.  Implemented: :func:`forest_repair_cost`.
  * Bipartite graphs: ``MaxCut = |E|`` (the bipartition cuts every edge), so
    the all-flip unit ``C_* = 0``; O(|V|+|E|).  Implemented:
    :func:`bipartite_max_cut`.  (Bipartite does NOT make general-``t``
    frustration cheap: an even cycle with an odd number of flips is frustrated.)
  * Planar graphs: weighted MaxCut / frustration index is polynomial via a
    T-join / Chinese-postman matching in the dual (Hadlock 1975;
    Orlova-Dorfman 1972; Barahona 1982).  Stated, NOT implemented here.
General graphs: only the exhaustive exact solver below.

This is CLASSICAL combinatorial optimization, not a new theorem, not a
physical experiment on an observer, and not an RH result.  All source/basis
labels are *declared contracts*, not independent source authentication.  No
floats and no randomness appear anywhere: costs are exact ``int``/``Fraction``
and all optima are exhaustive.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, permutations, product

from observational_succ.meta_choice_descent import (
    FiniteTransportGraph,
    LoopObstruction,
    ParityEdge,
    solve_parity_descent,
    verify_loop,
)

# Exhaustive solvers enumerate 2**(n-1) assignments; cap mirrors the #188
# brute-force oracle guard.  NP-hardness lives above this finite horizon.
_EXHAUSTIVE_VERTEX_CAP = 20

Weight = int | Fraction


class RepairContractError(ValueError):
    """A malformed graph, target vector, weight vector, or assignment."""


@dataclass(frozen=True)
class RepairGraph:
    """A finite undirected (multi)graph with declared source/basis provenance.

    Edges are an ordered tuple of unordered endpoint pairs; targets ``t`` and
    weights ``w`` are supplied separately, index-aligned to :attr:`edges`.
    Parallel edges and self-loops are permitted (a self-loop ``(v, v)`` has
    ``x_v (+) x_v = 0`` always, so it is unsatisfiable precisely when its
    target is ``1`` — an always-paid hard constraint).
    """

    source_id: str
    basis_id: str
    vertices: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]

    def __post_init__(self) -> None:
        if (not isinstance(self.source_id, str) or not self.source_id
                or not isinstance(self.basis_id, str) or not self.basis_id):
            raise RepairContractError(
                "Explicit nonempty original source and basis required")
        if (not isinstance(self.vertices, tuple)
                or not all(type(v) is str and v for v in self.vertices)
                or len(set(self.vertices)) != len(self.vertices)):
            raise RepairContractError(
                "Unique nonempty string vertex identifiers required")
        if not isinstance(self.edges, tuple):
            raise RepairContractError("Edges must be an immutable tuple")
        allowed = set(self.vertices)
        for e in self.edges:
            if (not isinstance(e, tuple) or len(e) != 2
                    or e[0] not in allowed or e[1] not in allowed):
                raise RepairContractError(
                    f"Malformed edge {e!r}; endpoints must be declared vertices")

    @property
    def n_vertices(self) -> int:
        return len(self.vertices)

    @property
    def n_edges(self) -> int:
        return len(self.edges)


def repair_graph(vertices, edges,
                 source_id: str = "declared-repair-source",
                 basis_id: str = "GF2") -> RepairGraph:
    """Convenience builder from plain iterables of vertices and endpoint pairs."""
    return RepairGraph(source_id, basis_id, tuple(vertices),
                       tuple((u, v) for u, v in edges))


# --------------------------------------------------------------------------
# Validation of target / weight / assignment vectors
# --------------------------------------------------------------------------

def _check_targets(graph: RepairGraph, t) -> tuple[int, ...]:
    t = tuple(t)
    if len(t) != graph.n_edges:
        raise RepairContractError(
            f"Expected {graph.n_edges} targets, got {len(t)}")
    for value in t:
        if type(value) is not int or value not in (0, 1):
            raise RepairContractError("Each target must be an int in {0, 1}")
    return t


def _check_weights(graph: RepairGraph, w) -> tuple[Weight, ...]:
    w = tuple(w)
    if len(w) != graph.n_edges:
        raise RepairContractError(
            f"Expected {graph.n_edges} weights, got {len(w)}")
    for value in w:
        # bool is an int subclass; forbid it so True/False cannot pose as cost.
        if (type(value) not in (int, Fraction)) or value < 0:
            raise RepairContractError(
                "Each weight must be a nonnegative int or Fraction")
    return w


def _check_assignment(graph: RepairGraph, x) -> dict[str, int]:
    if set(x) != set(graph.vertices):
        raise RepairContractError(
            "Assignment must cover exactly the declared vertices")
    for value in x.values():
        if type(value) is not int or value not in (0, 1):
            raise RepairContractError("Each vertex bit must be an int in {0, 1}")
    return dict(x)


def all_flip_targets(graph: RepairGraph) -> tuple[int, ...]:
    """The ALL-FLIP target vector: every ``t_e = 1``."""
    return (1,) * graph.n_edges


def unit_weights(graph: RepairGraph) -> tuple[int, ...]:
    """The UNIT weight vector: every ``w_e = 1``."""
    return (1,) * graph.n_edges


# --------------------------------------------------------------------------
# Exact cost and exhaustive optima
# --------------------------------------------------------------------------

def repair_cost(graph: RepairGraph, t, w, x) -> Weight:
    """Exact repair cost ``C(x) = sum_e w_e * 1[x_u (+) x_v != t_e]``.

    Returns an exact ``int`` (when all weights are ints) or ``Fraction``.
    """
    t = _check_targets(graph, t)
    w = _check_weights(graph, w)
    x = _check_assignment(graph, x)
    total: Weight = 0
    for i, (u, v) in enumerate(graph.edges):
        if (x[u] ^ x[v]) != t[i]:
            total += w[i]
    return total


def _gauge_assignments(graph: RepairGraph):
    """Yield all ``2**(n-1)`` assignments with the first vertex gauge-fixed to 0.

    The cost and the cut are invariant under flipping every vertex of any
    connected component, so fixing one vertex loses no distinct cost value.
    """
    if graph.n_vertices == 0:
        yield {}
        return
    if graph.n_vertices - 1 > _EXHAUSTIVE_VERTEX_CAP:
        raise RepairContractError(
            f"Exhaustive solver restricted to <= {_EXHAUSTIVE_VERTEX_CAP + 1}"
            " vertices")
    head, *rest = graph.vertices
    for bits in product((0, 1), repeat=len(rest)):
        assignment = {head: 0}
        assignment.update(zip(rest, bits))
        yield assignment


@dataclass(frozen=True)
class RepairResult:
    """Exact minimum repair cost with a replayable optimal assignment."""

    cost: Weight
    assignment: tuple[tuple[str, int], ...]
    gauge_fixed_vertex: str | None
    source_targets_altered: bool = False
    lawful_succ_repair: bool = True
    physical_source_authenticated: bool = False
    RH_proved: bool = False

    def as_dict(self) -> dict[str, int]:
        return dict(self.assignment)


def min_repair_cost(graph: RepairGraph, t, w) -> RepairResult:
    """Exact ``C_*`` by exhaustive ``2**(n-1)`` gauge-fixed enumeration.

    The returned assignment is the lexicographically first minimizer (vertex
    order of ``graph``, head bit 0), making the result deterministic.
    """
    t = _check_targets(graph, t)
    w = _check_weights(graph, w)
    best_cost: Weight | None = None
    best_assignment: dict[str, int] | None = None
    for assignment in _gauge_assignments(graph):
        cost: Weight = 0
        for i, (u, v) in enumerate(graph.edges):
            if (assignment[u] ^ assignment[v]) != t[i]:
                cost += w[i]
        if best_cost is None or cost < best_cost:
            best_cost = cost
            best_assignment = assignment
    if best_cost is None:          # only when there are no assignments at all
        best_cost = 0
        best_assignment = {}
    head = graph.vertices[0] if graph.n_vertices else None
    return RepairResult(
        best_cost,
        tuple((v, best_assignment[v]) for v in graph.vertices),
        head,
    )


@dataclass(frozen=True)
class CutResult:
    value: int
    assignment: tuple[tuple[str, int], ...]
    gauge_fixed_vertex: str | None

    def as_dict(self) -> dict[str, int]:
        return dict(self.assignment)


def max_cut(graph: RepairGraph) -> CutResult:
    """Exact ``MaxCut(G)`` by exhaustive gauge-fixed enumeration.

    Multi-edges count with multiplicity; a self-loop is never cut.
    """
    best_value = -1
    best_assignment: dict[str, int] | None = None
    for assignment in _gauge_assignments(graph):
        value = sum(1 for (u, v) in graph.edges if assignment[u] != assignment[v])
        if value > best_value:
            best_value = value
            best_assignment = assignment
    if best_assignment is None:
        best_value = 0
        best_assignment = {}
    head = graph.vertices[0] if graph.n_vertices else None
    return CutResult(
        best_value,
        tuple((v, best_assignment[v]) for v in graph.vertices),
        head,
    )


@dataclass(frozen=True)
class MaxCutIdentity:
    """Certificate of ``C_* == |E| - MaxCut`` for ALL-FLIP UNIT-WEIGHT."""

    num_edges: int
    max_cut: int
    repair_cost_star: int
    holds: bool


def verify_maxcut_identity(graph: RepairGraph) -> MaxCutIdentity:
    """Assert and return the all-flip unit-weight identity ``C_* = |E| - MaxCut``."""
    t = all_flip_targets(graph)
    w = unit_weights(graph)
    c_star = min_repair_cost(graph, t, w).cost
    cut = max_cut(graph).value
    holds = c_star == graph.n_edges - cut
    if not holds:                  # exact arithmetic: this must never fire
        raise AssertionError(
            f"ALL-FLIP identity violated: C_*={c_star}, |E|={graph.n_edges},"
            f" MaxCut={cut}")
    return MaxCutIdentity(graph.n_edges, cut, c_star, holds)


# --------------------------------------------------------------------------
# Signed-graph frustration and Ising ground state (exact mappings)
# --------------------------------------------------------------------------

def signed_signs(t) -> tuple[int, ...]:
    """Signed-graph signs ``sigma_e = (-1)^{t_e} in {+1, -1}``."""
    return tuple(1 if value == 0 else -1 for value in t)


def frustration_index(graph: RepairGraph, t, w) -> Weight:
    """Weighted frustration index of the signed graph == ``C_*``."""
    return min_repair_cost(graph, t, w).cost


def is_balanced(graph: RepairGraph, t, w) -> bool:
    """Signed graph balanced iff ``C_* == 0`` iff a global F_2 section exists."""
    return frustration_index(graph, t, w) == 0


def ising_couplings(t, w) -> tuple[Weight, ...]:
    """Ising couplings ``J_e = w_e * sigma_e`` (ferro if ``t_e=0``, else antiferro)."""
    return tuple(weight if target == 0 else -weight
                 for target, weight in zip(t, w))


def spins_of_assignment(x: dict[str, int]) -> dict[str, int]:
    """Spin picture ``s_v = (-1)^{x_v}`` in ``{+1, -1}``."""
    return {v: 1 - 2 * bit for v, bit in x.items()}


def ising_energy(graph: RepairGraph, couplings, spins: dict[str, int]) -> Weight:
    """Exact Ising energy ``H(s) = - sum_e J_e s_u s_v``."""
    if set(spins) != set(graph.vertices):
        raise RepairContractError("Spins must cover exactly the vertices")
    for value in spins.values():
        if value not in (1, -1):
            raise RepairContractError("Each spin must be +1 or -1")
    couplings = tuple(couplings)
    if len(couplings) != graph.n_edges:
        raise RepairContractError("One coupling per edge required")
    total: Weight = 0
    for i, (u, v) in enumerate(graph.edges):
        total += couplings[i] * spins[u] * spins[v]
    return -total


def total_weight(w) -> Weight:
    total: Weight = 0
    for value in w:
        total += value
    return total


def ising_ground_state_energy(graph: RepairGraph, t, w) -> Weight:
    """Ground-state energy via the exact mapping ``E_min = 2 C_* - W``."""
    t = _check_targets(graph, t)
    w = _check_weights(graph, w)
    return 2 * min_repair_cost(graph, t, w).cost - total_weight(w)


@dataclass(frozen=True)
class IsingGroundState:
    energy: Weight
    spins: tuple[tuple[str, int], ...]


def ising_ground_state_bruteforce(graph: RepairGraph, couplings) -> IsingGroundState:
    """Independent exhaustive Ising ground state (gauge-fix head spin ``+1``)."""
    best_energy: Weight | None = None
    best_spins: dict[str, int] | None = None
    for assignment in _gauge_assignments(graph):
        spins = spins_of_assignment(assignment)
        energy = ising_energy(graph, couplings, spins)
        if best_energy is None or energy < best_energy:
            best_energy = energy
            best_spins = spins
    if best_spins is None:
        best_energy = 0
        best_spins = {}
    return IsingGroundState(
        best_energy,
        tuple((v, best_spins[v]) for v in graph.vertices),
    )


# --------------------------------------------------------------------------
# Bridge to the #188 transport system; tree / bipartite cheap exact cases
# --------------------------------------------------------------------------

def to_transport_graph(graph: RepairGraph, t) -> FiniteTransportGraph:
    """Build the #188 ``FiniteTransportGraph`` for targets ``t`` (self-loops dropped).

    A self-loop carries ``x_v (+) x_v = 0``; #188's section solver already
    treats a self-loop's single incidence correctly, but a self-loop with
    target 1 is an intrinsic obstruction with no vertex degree of freedom, so
    this bridge is only used for the loop-free tree / bipartite detectors.
    """
    t = _check_targets(graph, t)
    edges = tuple(
        ParityEdge(u, v, t[i], graph.source_id, graph.basis_id)
        for i, (u, v) in enumerate(graph.edges)
    )
    return FiniteTransportGraph(graph.source_id, graph.basis_id,
                               graph.vertices, edges)


def is_forest(graph: RepairGraph) -> bool:
    """True iff the graph is acyclic (union-find; self-loop/parallel => cycle)."""
    parent = {v: v for v in graph.vertices}

    def find(a: str) -> str:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for (u, v) in graph.edges:
        if u == v:
            return False
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def forest_repair_cost(graph: RepairGraph, t, w) -> RepairResult:
    """Linear-time exact ``C_* = 0`` for a forest, for ANY targets ``t``.

    Reuses #188 spanning-forest propagation: a forest has no closed walk, so
    the F_2 section always exists and satisfies every edge at zero cost.
    """
    t = _check_targets(graph, t)
    w = _check_weights(graph, w)
    if not is_forest(graph):
        raise RepairContractError(
            "forest_repair_cost requires an acyclic graph")
    verdict = solve_parity_descent(to_transport_graph(graph, t))
    if not verdict.section_exists:     # impossible for a forest
        raise AssertionError("Forest transport failed to descend")
    x = dict(verdict.rooted_potential)
    cost = repair_cost(graph, t, w, x)
    if cost != 0:                      # exact: a forest repair is always free
        raise AssertionError("Forest repair cost was nonzero")
    return RepairResult(0, tuple((v, x[v]) for v in graph.vertices),
                        graph.vertices[0] if graph.n_vertices else None)


def is_bipartite(graph: RepairGraph) -> bool:
    """True iff 2-colorable, i.e. the ALL-FLIP transport has an F_2 section."""
    if any(u == v for (u, v) in graph.edges):
        return False
    return solve_parity_descent(
        to_transport_graph(graph, all_flip_targets(graph))).section_exists


def bipartite_max_cut(graph: RepairGraph) -> CutResult:
    """O(|V|+|E|) exact ``MaxCut = |E|`` for a bipartite graph.

    Reuses #188: the ALL-FLIP section is a proper 2-coloring that cuts every
    edge, so the all-flip unit ``C_* = |E| - |E| = 0``.
    """
    if not is_bipartite(graph):
        raise RepairContractError(
            "bipartite_max_cut requires a bipartite graph")
    verdict = solve_parity_descent(
        to_transport_graph(graph, all_flip_targets(graph)))
    x = dict(verdict.rooted_potential)
    value = sum(1 for (u, v) in graph.edges if x[u] != x[v])
    if value != graph.n_edges:         # exact: a proper 2-coloring cuts all
        raise AssertionError("Bipartite 2-coloring failed to cut every edge")
    return CutResult(value, tuple((v, x[v]) for v in graph.vertices),
                     graph.vertices[0] if graph.n_vertices else None)


# --------------------------------------------------------------------------
# Negative controls: greedy / local-flip suboptimality
# --------------------------------------------------------------------------

def greedy_sequential_repair(graph: RepairGraph, t, w) -> RepairResult:
    """A deterministic greedy heuristic (NOT exact): assign vertices in order,
    head bit 0, each next vertex taking the bit that minimizes the cost on
    edges to already-assigned vertices (ties -> 0).  Provided only as a
    negative control to be beaten by :func:`min_repair_cost`.
    """
    t = _check_targets(graph, t)
    w = _check_weights(graph, w)
    adjacency: dict[str, list[tuple[str, int]]] = {v: [] for v in graph.vertices}
    for i, (u, v) in enumerate(graph.edges):
        adjacency[u].append((v, i))
        if u != v:
            adjacency[v].append((u, i))
    x: dict[str, int] = {}
    for vertex in graph.vertices:
        if not x:
            x[vertex] = 0
            continue
        trial: dict[int, Weight] = {0: 0, 1: 0}
        for neighbor, edge_index in adjacency[vertex]:
            if neighbor in x:
                for bit in (0, 1):
                    if (bit ^ x[neighbor]) != t[edge_index]:
                        trial[bit] += w[edge_index]
        x[vertex] = 0 if trial[0] <= trial[1] else 1
    cost = repair_cost(graph, t, w, x)
    return RepairResult(cost, tuple((v, x[v]) for v in graph.vertices),
                        graph.vertices[0] if graph.n_vertices else None)


@dataclass(frozen=True)
class LocalOptimumCertificate:
    """A strict single-flip local optimum that is NOT a global optimum."""

    local_cost: Weight
    global_cost: Weight
    assignment: tuple[tuple[str, int], ...]
    neighbor_costs: tuple[tuple[str, Weight], ...]
    is_strict_local_optimum: bool
    strictly_suboptimal: bool


def single_flip_local_certificate(graph: RepairGraph, t, w, x
                                  ) -> LocalOptimumCertificate:
    """Certify that assignment ``x`` is a single-flip local optimum worse than ``C_*``.

    ``is_strict_local_optimum`` holds iff no single-vertex flip strictly lowers
    the cost; ``strictly_suboptimal`` holds iff the local cost exceeds the exact
    minimum.  Both facts are established by exhaustive recomputation.
    """
    t = _check_targets(graph, t)
    w = _check_weights(graph, w)
    x = _check_assignment(graph, x)
    base = repair_cost(graph, t, w, x)
    neighbor_costs = []
    local_opt = True
    for vertex in graph.vertices:
        flipped = dict(x)
        flipped[vertex] ^= 1
        neighbor = repair_cost(graph, t, w, flipped)
        neighbor_costs.append((vertex, neighbor))
        if neighbor < base:
            local_opt = False
    c_star = min_repair_cost(graph, t, w).cost
    return LocalOptimumCertificate(
        base, c_star,
        tuple((v, x[v]) for v in graph.vertices),
        tuple(neighbor_costs),
        local_opt,
        base > c_star,
    )


# --------------------------------------------------------------------------
# Probe vs. model-repair vs. illegal source-law alteration (SUCC taxonomy)
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class ObstructionProbe:
    """An observational probe: reveals the H^1 obstruction, repairs nothing.

    A probe adds *information* (the replayable odd-loop witness of #188) at
    zero repair cost and alters no source law.  It does not by itself make a
    genuinely source-frustrated instance globally representable: a positive
    ``C_*`` is unchanged by probing.
    """

    reveals_obstruction: bool
    cohomology_class_trivial: bool
    repair_cost_paid: int
    source_targets_altered: bool
    makes_globally_representable: bool
    obstruction: LoopObstruction | None


def probe_reveal_obstruction(graph: RepairGraph, t) -> ObstructionProbe:
    """Run the #188 solver as a pure observation: reveal, do not repair."""
    t = _check_targets(graph, t)
    if any(u == v and t[i] == 1 for i, (u, v) in enumerate(graph.edges)):
        # A target-1 self-loop is a degenerate intrinsic obstruction with no
        # closed-walk witness in the #188 sense; report it honestly.
        return ObstructionProbe(True, False, 0, False, False, None)
    verdict = solve_parity_descent(to_transport_graph(graph, t))
    return ObstructionProbe(
        reveals_obstruction=not verdict.section_exists,
        cohomology_class_trivial=verdict.section_exists,
        repair_cost_paid=0,
        source_targets_altered=False,
        makes_globally_representable=verdict.section_exists,
        obstruction=verdict.obstruction,
    )


def lawful_model_repair(graph: RepairGraph, t, w) -> RepairResult:
    """The lawful SUCC repair: keep all source targets, pay the residual ``C_*``.

    Preserves the declared source laws exactly; the price is the irreducible
    frustration index.  ``source_targets_altered=False``, ``lawful_succ_repair=True``.
    """
    base = min_repair_cost(graph, t, w)
    return RepairResult(base.cost, base.assignment, base.gauge_fixed_vertex,
                        source_targets_altered=False, lawful_succ_repair=True)


@dataclass(frozen=True)
class SourceLawAlteration:
    """An ILLEGAL "repair" that rewrites source targets — NOT a lawful SUCC repair."""

    original_targets: tuple[int, ...]
    altered_targets: tuple[int, ...]
    altered_edge_indices: tuple[int, ...]
    apparent_repair_cost: Weight
    source_targets_altered: bool
    lawful_succ_repair: bool


def illegal_source_law_alteration(graph: RepairGraph, t, edge_indices,
                                  w=None) -> SourceLawAlteration:
    """Flip the declared target on ``edge_indices`` to cheapen the cost illegally.

    This is the forbidden move: it changes the ORIGINAL source law
    (``t_e``) rather than repairing the model.  The returned record always
    carries ``source_targets_altered=True`` and ``lawful_succ_repair=False``.
    The ``apparent_repair_cost`` is the (often zero) cost under the rewritten
    targets — cheap precisely because it cheated.
    """
    t = _check_targets(graph, t)
    indices = tuple(edge_indices)
    if not indices or any(type(i) is not int or not (0 <= i < graph.n_edges)
                          for i in indices):
        raise RepairContractError("edge_indices must be valid edge positions")
    if w is None:
        w = unit_weights(graph)
    w = _check_weights(graph, w)
    flip = set(indices)
    altered = tuple((1 - value) if i in flip else value
                    for i, value in enumerate(t))
    apparent = min_repair_cost(graph, altered, w).cost
    return SourceLawAlteration(
        original_targets=t,
        altered_targets=altered,
        altered_edge_indices=indices,
        apparent_repair_cost=apparent,
        source_targets_altered=True,
        lawful_succ_repair=False,
    )


# --------------------------------------------------------------------------
# Bounded certificate family: connected graphs on <= max_vertices vertices
# --------------------------------------------------------------------------

def _connected(verts: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> bool:
    if not verts:
        return True
    adjacency: dict[int, set[int]] = {v: set() for v in verts}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    seen = {verts[0]}
    stack = [verts[0]]
    while stack:
        node = stack.pop()
        for neighbor in adjacency[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    return len(seen) == len(verts)


def _canonical_edges(n: int, edges: tuple[tuple[int, int], ...]
                     ) -> tuple[tuple[int, int], ...]:
    """Lexicographically least edge set over all ``n!`` vertex relabelings."""
    best: tuple[tuple[int, int], ...] | None = None
    for perm in permutations(range(n)):
        relabeled = tuple(sorted(
            tuple(sorted((perm[u], perm[v]))) for (u, v) in edges))
        if best is None or relabeled < best:
            best = relabeled
    assert best is not None
    return best


def _connected_graph_classes(n: int) -> list[tuple[tuple[int, int], ...]]:
    """Canonical representatives of connected graphs on exactly ``n`` vertices."""
    verts = tuple(range(n))
    pairs = tuple(combinations(verts, 2))
    classes: set[tuple[tuple[int, int], ...]] = set()
    for mask in product((0, 1), repeat=len(pairs)):
        edges = tuple(p for p, bit in zip(pairs, mask) if bit)
        if _connected(verts, edges):
            classes.add(_canonical_edges(n, edges))
    return sorted(classes)


def connected_graph_certificates(max_vertices: int = 5) -> list[dict]:
    """Deterministic optimality certificates for all connected graphs
    (up to isomorphism) on 1..``max_vertices`` vertices.

    Each entry stores, for ALL-FLIP UNIT-WEIGHT: the canonical edge list,
    ``|E|``, ``MaxCut``, ``C_*`` (== frustration index), a lex-least optimal
    assignment, and the forest/bipartite flags.  Pure integers; a re-run
    reproduces the list bit-for-bit.
    """
    certificates: list[dict] = []
    for n in range(1, max_vertices + 1):
        for edges in _connected_graph_classes(n):
            vertices = tuple(f"v{i}" for i in range(n))
            graph = RepairGraph("certificate-family", "GF2", vertices,
                                tuple((f"v{u}", f"v{v}") for (u, v) in edges))
            identity = verify_maxcut_identity(graph)
            best = min_repair_cost(graph, all_flip_targets(graph),
                                   unit_weights(graph))
            certificates.append({
                "n_vertices": n,
                "edges": [[u, v] for (u, v) in edges],
                "num_edges": identity.num_edges,
                "max_cut": identity.max_cut,
                "repair_cost_star": identity.repair_cost_star,
                "frustration_index": identity.repair_cost_star,
                "maxcut_identity_holds": identity.holds,
                "optimal_assignment": [bit for (_, bit) in best.assignment],
                "is_forest": is_forest(graph),
                "is_bipartite": is_bipartite(graph),
            })
    return certificates
