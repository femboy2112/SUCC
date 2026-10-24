"""Selected-start reachability under a finite observation quotient.

Classical ancestral closure, adapted to the existing source-labelled Machine.
Actions, costs and intermediate reports are deliberately forgotten *only for
this endpoint question*. Use future_safe_quotient.audit_representation for
their stronger preservation contract. No source authentication, infinite
trace, frequency, or normality conclusion is supplied by this diagnostic.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass

from .future_safe_quotient import Edge, ForgettingError, Machine


@dataclass(frozen=True)
class GhostPath:
    """An abstract path and a hereditary-set obstruction to lifting its endpoint.

    Each edge is real in the declared source, but consecutive edges need only
    meet after observation. The list is NOT asserted to be an executable path.
    The boundary leaves the saturation of reachable_states. Its start has the
    same report as reachable_representative, while its target has no reachable
    representative at all.
    """

    reports: tuple[str, ...]
    source_edges: tuple[Edge, ...]
    reachable_states: tuple[str, ...]
    boundary: Edge
    reachable_representative: str


@dataclass(frozen=True)
class AncestralAudit:
    start: str
    reachable_states: tuple[str, ...]
    reachable_reports: tuple[str, ...]
    quotient_reports: tuple[str, ...]
    ghost_reports: tuple[str, ...]
    obstruction: GhostPath | None

    @property
    def endpoint_exact(self) -> bool:
        """Only this selected start and unlabelled finite-path endpoints."""
        return not self.ghost_reports


def audit_ancestral_observer(machine: Machine, labels: tuple[str, ...],
                             start: str) -> AncestralAudit:
    """Compare observe-after-reachability with reachability-after-observation.

    labels has one string per machine state, in declaration order. The abstract
    relation has an edge whenever *some* source edge has those endpoint labels.
    Closure includes the zero-step path, including at isolated states. This is
    modern reflexive closure; Principia's ancestral has a field restriction.

    Complete BFS computes both closures on this supplied finite machine. On
    failure it returns a shortest spurious abstract path and the concrete
    saturation boundary of the hereditary set Reach(start). A successful result
    is not a certificate for other starts or for action/cost/trace preservation.
    """
    if type(machine) is not Machine:
        raise ForgettingError("A declared finite source Machine is required")
    names = tuple(s.name for s in machine.states)
    if (type(labels) is not tuple or len(labels) != len(names)
            or any(type(label) is not str for label in labels)):
        raise ForgettingError("One immutable string observation per state required")
    if type(start) is not str or start not in names:
        raise ForgettingError("Selected start must be an actual declared source state")
    q = dict(zip(names, labels))
    source_rows: dict[str, list[Edge]] = {s: [] for s in names}
    reports = tuple(dict.fromkeys(labels))
    quotient_rows: dict[str, list[Edge]] = {label: [] for label in reports}
    for edge in machine.edges:
        source_rows[edge.start].append(edge)
        quotient_rows[q[edge.start]].append(edge)

    reached = {start}
    queue = deque([start])
    while queue:
        for edge in source_rows[queue.popleft()]:
            if edge.target not in reached:
                reached.add(edge.target)
                queue.append(edge.target)
    reached_reports = {q[s] for s in reached}
    abstract = {q[start]}
    predecessors: dict[str, Edge] = {}
    queue = deque([q[start]])
    first_ghost = None
    while queue:
        for edge in quotient_rows[queue.popleft()]:
            target = q[edge.target]
            if target not in abstract:
                abstract.add(target)
                predecessors[target] = edge
                queue.append(target)
                if first_ghost is None and target not in reached_reports:
                    first_ghost = target

    reachable_states = tuple(s for s in names if s in reached)
    obstruction = None
    if first_ghost is not None:
        backwards = []
        current = first_ghost
        while current != q[start]:
            edge = predecessors[current]
            backwards.append(edge)
            current = q[edge.start]
        path = tuple(reversed(backwards))
        boundary = next(e for e in path if q[e.start] in reached_reports
                        and q[e.target] not in reached_reports)
        representative = next(s for s in reachable_states
                              if q[s] == q[boundary.start])
        obstruction = GhostPath(
            (q[start],) + tuple(q[e.target] for e in path), path,
            reachable_states, boundary, representative,
        )
    return AncestralAudit(
        start, reachable_states,
        tuple(label for label in reports if label in reached_reports),
        tuple(label for label in reports if label in abstract),
        tuple(label for label in reports
              if label in abstract and label not in reached_reports),
        obstruction,
    )
