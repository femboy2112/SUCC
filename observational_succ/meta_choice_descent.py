"""Finite source-typed Z/2 descent: local construction versus global coherence.

Every edge e=(u,v,t) imposes x[v] = x[u] XOR t.  A global section
exists iff the edge 1-cochain is a coboundary (equivalently, XOR around
every closed walk vanishes).  On a connected graph the number of sections
is then two; on a graph with c components it is 2**c.

This is elementary graph cohomology (CLASSICAL), not a new topos theorem,
an experiment on an actual observer, or an RH proof.  All source labels
are *declared contracts*, not independent source authentication.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product


class DescentContractError(ValueError):
    """A malformed graph or cross-source/coordinate comparison."""


@dataclass(frozen=True)
class ParityEdge:
    u: str
    v: str
    parity: int
    source_id: str
    basis_id: str


@dataclass(frozen=True)
class FiniteTransportGraph:
    source_id: str
    basis_id: str
    vertices: tuple[str, ...]
    edges: tuple[ParityEdge, ...]

    def __post_init__(self) -> None:
        if (not isinstance(self.source_id, str) or not self.source_id
                or not isinstance(self.basis_id, str) or not self.basis_id):
            raise DescentContractError("Explicit nonempty original source and basis required")
        if (not isinstance(self.vertices, tuple)
                or not all(type(v) is str and v for v in self.vertices)
                or len(set(self.vertices)) != len(self.vertices)):
            raise DescentContractError("Unique nonempty string vertex identifiers required")
        if not isinstance(self.edges, tuple):
            raise DescentContractError("Edges must be an immutable tuple")
        allowed = set(self.vertices)
        for e in self.edges:
            if (not isinstance(e, ParityEdge)
                    or e.u not in allowed or e.v not in allowed
                    or type(e.parity) is not int or e.parity not in (0, 1)
                    or e.source_id != self.source_id or e.basis_id != self.basis_id):
                raise DescentContractError(
                    "Malformed parity edge or source/basis mismatch; no transport authorized"
                )


@dataclass(frozen=True)
class LoopObstruction:
    """A verifier-replayable rooted CLOSED WALK with odd parity.

    Edge orientations are irrelevant only because the coefficient group
    is F_2.  For general nonabelian transports this interface is invalid.
    """
    vertices: tuple[str, ...]
    edge_indices: tuple[int, ...]
    parity: int


@dataclass(frozen=True)
class DescentVerdict:
    section_exists: bool
    number_of_components: int
    number_of_sections: int
    rooted_potential: tuple[tuple[str, int], ...] | None
    obstruction: LoopObstruction | None
    physical_source_authenticated: bool = False
    general_sheaf_descent_proved: bool = False
    RH_proved: bool = False


def verify_loop(graph: FiniteTransportGraph, witness: LoopObstruction) -> bool:
    """Independent elementary certificate checker, no trust in solver state."""
    if (type(witness) is not LoopObstruction
            or type(witness.parity) is not int or witness.parity != 1
            or not witness.edge_indices
            or len(witness.vertices) != len(witness.edge_indices) + 1
            or witness.vertices[0] != witness.vertices[-1]):
        return False
    parity = 0
    for u, v, i in zip(witness.vertices, witness.vertices[1:],
                       witness.edge_indices):
        if type(i) is not int or i < 0 or i >= len(graph.edges):
            return False
        edge = graph.edges[i]
        if not ((edge.u == u and edge.v == v) or
                (edge.u == v and edge.v == u)):
            return False
        parity ^= edge.parity
    return parity == witness.parity


def _root_path(node: str, parent: dict[str, tuple[str, int] | None]
               ) -> tuple[list[str], list[int]]:
    vertices = [node]
    edges = []
    while parent[vertices[-1]] is not None:
        step = parent[vertices[-1]]
        assert step is not None
        preceding, edge_idx = step
        edges.append(edge_idx)
        vertices.append(preceding)
    vertices.reverse()
    edges.reverse()
    return vertices, edges


def _odd_loop(u: str, v: str, index: int,
              parent: dict[str, tuple[str, int] | None]
              ) -> LoopObstruction:
    path_u, edges_u = _root_path(u, parent)
    path_v, edges_v = _root_path(v, parent)
    # Root -> u -> v -> Root.  Repeated tree edges are permitted: this
    # is a closed walk, not necessarily a simple cycle.
    return LoopObstruction(
        tuple(path_u + [v] + list(reversed(path_v[:-1]))),
        tuple(edges_u + [index] + list(reversed(edges_v))),
        1,
    )


def solve_parity_descent(graph: FiniteTransportGraph) -> DescentVerdict:
    """Linear-time spanning-forest solve with first exact odd-loop witness.

    A returned gauge sets one root per component to zero.  This convention
    is a mathematical construction, NOT a physically realized free choice.
    Unconstrained root bits yield 2**components distinct sections.
    """
    neighbors: dict[str, list[tuple[str, int]]] = {
        v: [] for v in graph.vertices
    }
    for idx, edge in enumerate(graph.edges):
        neighbors[edge.u].append((edge.v, idx))
        if edge.v != edge.u:
            neighbors[edge.v].append((edge.u, idx))
    potential: dict[str, int] = {}
    parent: dict[str, tuple[str, int] | None] = {}
    components = 0
    obstruction: LoopObstruction | None = None
    for root in graph.vertices:
        if root in potential:
            continue
        components += 1
        potential[root] = 0
        parent[root] = None
        frontier = deque([root])
        while frontier:
            u = frontier.popleft()
            for v, idx in neighbors[u]:
                target = potential[u] ^ graph.edges[idx].parity
                if v not in potential:
                    potential[v] = target
                    parent[v] = (u, idx)
                    frontier.append(v)
                elif potential[v] != target and obstruction is None:
                    obstruction = _odd_loop(u, v, idx, parent)
    if obstruction is not None:
        if not verify_loop(graph, obstruction):
            raise AssertionError("Internal odd-loop certificate failed replay")
        return DescentVerdict(False, components, 0, None, obstruction)
    return DescentVerdict(
        True, components, 1 << components,
        tuple((v, potential[v]) for v in graph.vertices), None,
    )


def verify_section(graph: FiniteTransportGraph,
                   assignment: dict[str, int]) -> bool:
    """Verify all original edge laws, not merely reconstructed tree laws."""
    if set(assignment) != set(graph.vertices):
        return False
    if any(type(x) is not int or x not in (0, 1)
           for x in assignment.values()):
        return False
    return all((assignment[e.u] ^ assignment[e.v]) == e.parity
               for e in graph.edges)


def brute_force_sections(graph: FiniteTransportGraph
                         ) -> tuple[tuple[int, ...], ...]:
    """Independent exact exhaustive oracle for small finite domains."""
    if len(graph.vertices) > 16:
        raise DescentContractError("Brute-force oracle restricted to <=16 vertices")
    return tuple(
        bits for bits in product((0, 1), repeat=len(graph.vertices))
        if verify_section(graph, dict(zip(graph.vertices, bits)))
    )


def local_edge_witnesses(edge: ParityEdge
                         ) -> tuple[tuple[int, int], ...]:
    """Each edge's local solution set; loops correctly share one variable."""
    return tuple(
        (a, b) for a, b in product((0, 1), repeat=2)
        if (a ^ b) == edge.parity and (edge.u != edge.v or a == b)
    )


def triangle(parities: tuple[int, int, int],
             source_id: str = "declared-triangle-source",
             basis_id: str = "GF2") -> FiniteTransportGraph:
    if not isinstance(parities, tuple) or len(parities) != 3:
        raise DescentContractError("Three parity constraints required")
    return FiniteTransportGraph(source_id, basis_id, ("A", "B", "C"), tuple(
        ParityEdge(a, b, value, source_id, basis_id)
        for (a, b), value in zip((("A", "B"), ("B", "C"), ("C", "A")),
                                 parities)
    ))
