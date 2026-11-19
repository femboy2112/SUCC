"""Exact forward-path phase reconstruction and Jacobian graph adapters.

Research instrument for PATH_GEOMETRY.md. Phases are rational turns modulo one.
This implements a declared known-support experiment, not a discovered physical
carrier. Matrix semantics reuse SUCC's exact Q(i) graph implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q

from observational_succ.collective_spectral import Gaussian
from observational_succ.ym_graph_semantics import Edge, LayeredGraph, Matrix


def turn(value: int | Q) -> Q:
    if type(value) not in (int, Q):
        raise ValueError("phase must be an exact integer or Fraction of a turn")
    return Q(value) % 1


@dataclass(frozen=True)
class PhaseEdge:
    source: int
    target: int
    phase: Q

    def __post_init__(self):
        object.__setattr__(self, "phase", turn(self.phase))


@dataclass(frozen=True)
class CausalPhaseNetwork:
    """Known directed graph with an explicitly available rooted out-tree.

    Edge indices are distinct instrument/action labels. Parallel edges are
    separately addressable. An algebraic inverse phase never executes an edge
    backward. Repeating paths requires the experiment's preparation/replay
    contract; this class does not infer that such access exists.
    """
    vertex_count: int
    root: int
    edges: tuple[PhaseEdge, ...]
    tree_edges: tuple[int, ...]

    def __post_init__(self):
        if type(self.vertex_count) is not int or self.vertex_count < 1:
            raise ValueError("positive vertex count required")
        if type(self.root) is not int or not 0 <= self.root < self.vertex_count:
            raise ValueError("root outside graph")
        if type(self.edges) is not tuple or any(type(e) is not PhaseEdge for e in self.edges):
            raise ValueError("immutable declared edge family required")
        for edge in self.edges:
            if any(type(v) is not int or not 0 <= v < self.vertex_count
                   for v in (edge.source, edge.target)):
                raise ValueError("edge endpoint outside graph")
        if (type(self.tree_edges) is not tuple or
                len(self.tree_edges) != self.vertex_count - 1 or
                len(set(self.tree_edges)) != len(self.tree_edges) or
                any(type(k) is not int or not 0 <= k < len(self.edges)
                    for k in self.tree_edges)):
            raise ValueError("a spanning out-tree has exactly V-1 distinct edge labels")
        incoming = [0] * self.vertex_count
        for index in self.tree_edges:
            incoming[self.edges[index].target] += 1
        if incoming[self.root] or any(incoming[v] != 1 for v in range(self.vertex_count)
                                      if v != self.root):
            raise ValueError("tree must point forward from the declared root")
        self.tree_paths()  # Reachability rejects a detached directed cycle.

    def tree_paths(self) -> tuple[tuple[int, ...], ...]:
        paths = {self.root: ()}
        pending = list(self.tree_edges)
        while pending:
            progressed = False
            for index in tuple(pending):
                edge = self.edges[index]
                if edge.source in paths:
                    if edge.target in paths:
                        raise ValueError("tree cycle or duplicate child")
                    paths[edge.target] = paths[edge.source] + (index,)
                    pending.remove(index)
                    progressed = True
            if not progressed:
                raise ValueError("tree contains vertices not causally reachable from root")
        if len(paths) != self.vertex_count:
            raise ValueError("root does not reach the entire declared graph")
        return tuple(paths[v] for v in range(self.vertex_count))

    @property
    def chords(self) -> tuple[int, ...]:
        return tuple(k for k in range(len(self.edges)) if k not in self.tree_edges)

    def path_phase(self, path: tuple[int, ...], start: int | None = None) -> tuple[int, Q]:
        current = self.root if start is None else start
        if type(current) is not int or not 0 <= current < self.vertex_count:
            raise ValueError("path origin outside graph")
        total = Q()
        for index in path:
            if type(index) is not int or not 0 <= index < len(self.edges):
                raise ValueError("unknown edge label")
            edge = self.edges[index]
            if edge.source != current:
                raise ValueError("path attempts a noncausal or mismatched edge")
            total += edge.phase
            current = edge.target
        return current, total % 1

    def tree_phases(self) -> tuple[Q, ...]:
        return tuple(self.path_phase(path)[1] for path in self.tree_paths())

    def chord_holonomies(self) -> dict[int, Q]:
        tau = self.tree_phases()
        return {index: (tau[self.edges[index].source] + self.edges[index].phase
                        - tau[self.edges[index].target]) % 1 for index in self.chords}

    def gauge(self, vertex_turns: tuple[int | Q, ...]) -> "CausalPhaseNetwork":
        if len(vertex_turns) != self.vertex_count:
            raise ValueError("one chart phase is required at each vertex")
        offsets = tuple(turn(x) for x in vertex_turns)
        edges = tuple(PhaseEdge(e.source, e.target,
                                e.phase + offsets[e.target] - offsets[e.source])
                      for e in self.edges)
        return CausalPhaseNetwork(self.vertex_count, self.root, edges, self.tree_edges)

    def from_holonomies(self, records: dict[int, int | Q]) -> "CausalPhaseNetwork":
        """Recover the unique tree-gauge representative; reject missing data."""
        if set(records) != set(self.chords):
            raise ValueError("every chord response, and no invented chord, is required")
        edges = tuple(PhaseEdge(e.source, e.target, records.get(index, Q()))
                      for index, e in enumerate(self.edges))
        return CausalPhaseNetwork(self.vertex_count, self.root, edges, self.tree_edges)

    def comparison_cost(self) -> int:
        """Edge traversals if each of the two paths is freshly prepared per chord.

        This excludes device-specific preparation, waiting and phase-reference
        costs; it is not the minimum under every possible memory architecture.
        """
        paths = self.tree_paths()
        return sum(len(paths[self.edges[k].source]) + 1
                   + len(paths[self.edges[k].target]) for k in self.chords)


def jacobian_graph(jacobians: tuple[Matrix, ...]) -> LayeredGraph:
    """Time-layered graph of the exact first-variation matrices supplied."""
    if not jacobians:
        raise ValueError("at least one Jacobian is needed to specify dimensions")
    dimensions = [jacobians[0].shape[1]]
    edges = []
    for time, matrix in enumerate(jacobians):
        if matrix.shape[1] != dimensions[-1]:
            raise ValueError("Jacobian boundary dimensions do not compose")
        dimensions.append(matrix.shape[0])
        edges.extend(Edge(time, j, i, value)
                     for i, row in enumerate(matrix.entries)
                     for j, value in enumerate(row) if value != Gaussian())
    return LayeredGraph(tuple(dimensions), tuple(edges))


def transported_jacobians(jacobians: tuple[Matrix, ...], frames: tuple[Matrix, ...],
                          inverse_frames: tuple[Matrix, ...]) -> tuple[Matrix, ...]:
    """Apply K_t=B_(t+1) J_t B_t^-1 after checking each supplied inverse."""
    if len(frames) != len(jacobians) + 1 or len(inverse_frames) != len(frames):
        raise ValueError("a frame and its inverse are required at every time")
    for frame, inverse in zip(frames, inverse_frames):
        if (frame.shape[0] != frame.shape[1] or
                frame @ inverse != Matrix.identity(frame.shape[0]) or
                inverse @ frame != Matrix.identity(frame.shape[0])):
            raise ValueError("unverified or singular frame inverse")
    return tuple(frames[t + 1] @ matrix @ inverse_frames[t]
                 for t, matrix in enumerate(jacobians))
