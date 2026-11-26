"""Finite coherent observer continuation and exact seam certificates.

Theorems are in the Principia Intermedia research dossier.  This module checks a
*declared finite model*: it does not authenticate an arithmetic source merely
because a caller supplied a source label.  A state must contain all information
needed to decide its lawful successors; nonlocal obligations must be expanded
into retained history or checked before supplying the edge relation.

Source and normalized comparison-target labels are preserved on every edge.
History is append-only.  A defect used for sign crossing is a separate relative
coordinate; an invariant comparison target cannot change sign along a coherent
path.  Finite witnesses do not certify a continuum or infinite refinement lift.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Mapping, Sequence


class ContinuationError(ValueError):
    """The supplied finite model or claimed exact bound is malformed."""


@dataclass(frozen=True)
class ObserverState:
    name: str
    source: str
    target: str
    history: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if any(not isinstance(x, str) or not x for x in (self.name, self.source, self.target)):
            raise ContinuationError("state, source and comparison-target labels must be nonempty strings")
        if not isinstance(self.history, tuple) or any(not isinstance(x, str) for x in self.history):
            raise ContinuationError("retained history must be an immutable tuple of strings")


@dataclass(frozen=True)
class LayeredModel:
    layers: tuple[tuple[ObserverState, ...], ...]
    edges: tuple[frozenset[tuple[str, str]], ...]
    starts: frozenset[str]
    ends: frozenset[str]

    def __post_init__(self) -> None:
        # Copy caller containers so later mutation cannot change a certificate.
        layers = tuple(tuple(layer) for layer in self.layers)
        edges = tuple(frozenset(tuple(edge) for edge in relation) for relation in self.edges)
        starts, ends = frozenset(self.starts), frozenset(self.ends)
        object.__setattr__(self, "layers", layers)
        object.__setattr__(self, "edges", edges)
        object.__setattr__(self, "starts", starts)
        object.__setattr__(self, "ends", ends)
        if not layers or len(edges) != len(layers) - 1:
            raise ContinuationError("a nonempty layer list needs exactly one relation per adjacent pair")
        for layer in layers:
            if any(not isinstance(state, ObserverState) for state in layer):
                raise ContinuationError("layers must contain ObserverState values")
            if len({state.name for state in layer}) != len(layer):
                raise ContinuationError("state names must be unique within each layer")
        lookup = tuple({state.name: state for state in layer} for layer in layers)
        if not starts <= lookup[0].keys() or not ends <= lookup[-1].keys():
            raise ContinuationError("anchor names must occur in their endpoint layers")
        for i, relation in enumerate(edges):
            for pair in relation:
                if len(pair) != 2 or pair[0] not in lookup[i] or pair[1] not in lookup[i + 1]:
                    raise ContinuationError("edge has an unknown endpoint or wrong arity")
                left, right = lookup[i][pair[0]], lookup[i + 1][pair[1]]
                if left.source != right.source:
                    raise ContinuationError("an edge changes the retained source witness")
                if left.target != right.target:
                    raise ContinuationError("an edge changes the normalized comparison target")
                if right.history[:len(left.history)] != left.history:
                    raise ContinuationError("an edge erases or rewrites retained history")


Vertex = tuple[int, str]


def _forbidden(model: LayeredModel, vertices: Iterable[Vertex]) -> frozenset[Vertex]:
    result = frozenset(vertices)
    known = {(i, state.name) for i, layer in enumerate(model.layers) for state in layer}
    if not result <= known:
        raise ContinuationError("a forbidden/seam vertex is absent from the model")
    return result


@dataclass(frozen=True)
class ContinuationResult:
    forward: tuple[frozenset[str], ...]
    backward: tuple[frozenset[str], ...]
    viable: tuple[frozenset[str], ...]
    witness: tuple[str, ...] | None
    # In a failed model every layer is a disjoint-cone cut.  We expose a middle
    # cut; its two cones are already present in the result for exact inspection.
    cut_layer: int | None

    @property
    def feasible(self) -> bool:
        return self.witness is not None


def continuation(model: LayeredModel, forbidden: Iterable[Vertex] = ()) -> ContinuationResult:
    """Compute both cones and a lawful anchored path, or a disjoint-cone cut."""
    excluded = _forbidden(model, forbidden)
    count = len(model.layers)
    forward: list[frozenset[str]] = [frozenset(name for name in model.starts if (0, name) not in excluded)]
    for i, relation in enumerate(model.edges):
        forward.append(frozenset(right for left, right in relation
                                 if left in forward[i] and (i + 1, right) not in excluded))
    backward: list[frozenset[str]] = [frozenset() for _ in model.layers]
    backward[-1] = frozenset(name for name in model.ends if (count - 1, name) not in excluded)
    for i in range(count - 2, -1, -1):
        backward[i] = frozenset(left for left, right in model.edges[i]
                                if right in backward[i + 1] and (i, left) not in excluded)
    viable = tuple(left & right for left, right in zip(forward, backward))
    witness: tuple[str, ...] | None = None
    if viable[0]:
        path = [min(viable[0])]
        for i, relation in enumerate(model.edges):
            path.append(min(right for left, right in relation
                            if left == path[-1] and right in backward[i + 1]))
        witness = tuple(path)
    return ContinuationResult(tuple(forward), tuple(backward), viable, witness,
                              None if witness is not None else count // 2)


def verify_witness(model: LayeredModel, witness: Sequence[str],
                   forbidden: Iterable[Vertex] = ()) -> tuple[ObserverState, ...]:
    """Verify a supplied witness independently of how it was selected."""
    excluded = _forbidden(model, forbidden)
    names = tuple(witness)
    if len(names) != len(model.layers) or not names:
        raise ContinuationError("witness must name one state at every layer")
    lookup = tuple({state.name: state for state in layer} for layer in model.layers)
    if any(name not in lookup[i] for i, name in enumerate(names)):
        raise ContinuationError("witness names an unknown state")
    if names[0] not in model.starts or names[-1] not in model.ends:
        raise ContinuationError("witness violates an endpoint anchor")
    if any((i, name) in excluded for i, name in enumerate(names)):
        raise ContinuationError("witness enters a forbidden vertex")
    if any((names[i], names[i + 1]) not in relation for i, relation in enumerate(model.edges)):
        raise ContinuationError("witness uses an undeclared transition")
    return tuple(lookup[i][name] for i, name in enumerate(names))


@dataclass(frozen=True)
class SeamReport:
    feasible: bool
    unavoidable: bool
    witness: tuple[str, ...] | None
    avoiding_witness: tuple[str, ...] | None
    avoidance_cut: int | None


def seam_report(model: LayeredModel, seam: Iterable[Vertex]) -> SeamReport:
    """A non-vacuous exact all-path seam test by deletion and reachability.

    ``unavoidable`` is false when there is no original path; inspect ``feasible``
    to distinguish this vacuous case from a real path avoiding the seam.
    """
    vertices = _forbidden(model, seam)
    original = continuation(model)
    avoiding = continuation(model, vertices)
    return SeamReport(original.feasible, original.feasible and not avoiding.feasible,
                      original.witness, avoiding.witness, avoiding.cut_layer)


def _rational(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise ContinuationError("exact arithmetic accepts integers or Fraction values, not floats")
    return Fraction(value)


def _values_and_bound(values: Sequence[int | Fraction], max_jump: int | Fraction | None):
    exact = tuple(_rational(value) for value in values)
    if not exact:
        raise ContinuationError("a scalar observer path must be nonempty")
    observed = max((abs(right - left) for left, right in zip(exact, exact[1:])), default=Fraction(0))
    bound = observed if max_jump is None else _rational(max_jump)
    if bound < 0 or observed > bound:
        raise ContinuationError("claimed jump bound is negative or violated by a declared edge")
    if exact[0] * exact[-1] > 0:
        raise ContinuationError("endpoint defects do not bracket zero")
    return exact, bound


@dataclass(frozen=True)
class ScalarCrossing:
    edge_index: int | None
    zero_index: int | None
    near_index: int
    near_value: Fraction
    jump_bound: Fraction
    near_bound: Fraction


def granular_crossing(values: Sequence[int | Fraction],
                       max_jump: int | Fraction | None = None) -> ScalarCrossing:
    """Find an exact zero or a sign edge and a vertex within ``max_jump / 2``.

    The path values already have to be expressed in a declared common signed
    coordinate.  Edge interpolation is not asserted to be a lawful observer.
    """
    exact, bound = _values_and_bound(values, max_jump)
    zero = next((i for i, value in enumerate(exact) if value == 0), None)
    if zero is not None:
        return ScalarCrossing(None, zero, zero, Fraction(0), bound, bound / 2)
    edge = next(i for i in range(len(exact) - 1) if exact[i] * exact[i + 1] < 0)
    near = edge if abs(exact[edge]) <= abs(exact[edge + 1]) else edge + 1
    return ScalarCrossing(edge, None, near, exact[near], bound, bound / 2)


def lattice_zero(values: Sequence[int | Fraction], spacing: int | Fraction,
                 max_jump: int | Fraction | None = None) -> int:
    """Certify an exact null vertex for hZ values with edge jumps strictly < 2h."""
    exact, bound = _values_and_bound(values, max_jump)
    step = _rational(spacing)
    if step <= 0:
        raise ContinuationError("lattice spacing must be positive")
    if any((value / step).denominator != 1 for value in exact):
        raise ContinuationError("defect values do not belong to the declared zero-centered lattice")
    if bound >= 2 * step:
        raise ContinuationError("the sharp lattice theorem needs a strict jump bound below twice the spacing")
    zero = next((i for i, value in enumerate(exact) if value == 0), None)
    if zero is None:  # This would contradict the checked lattice/sign hypotheses.
        raise AssertionError("checked lattice hypotheses failed to force a null vertex")
    return zero


@dataclass(frozen=True)
class TransportResult:
    coherent: bool
    assignment: tuple[tuple[str, int], ...]
    obstruction: tuple[str, str] | None


def transport_section(vertices: Sequence[str],
                      edges: Sequence[tuple[str, str, Sequence[int]]], *,
                      fiber_size: int, anchor_vertex: str, anchor_value: int,
                      required: Mapping[str, int] | None = None) -> TransportResult:
    """Check anchor-fixed holonomy for bijections of one finite labelled fiber.

    Each permutation represents an explicitly declared reversible transport.
    Its inverse is added automatically.  The underlying graph must be connected.
    A coherent anchor may exist even when the holonomy is nontrivial elsewhere
    in the fiber.  This function does not construct or authenticate the supplied
    transports, and has no carrier-specific source input.
    """
    names = tuple(vertices)
    if not names or any(not isinstance(name, str) or not name for name in names) or len(set(names)) != len(names):
        raise ContinuationError("transport vertices must be distinct nonempty names")
    if type(fiber_size) is not int or fiber_size <= 0:
        raise ContinuationError("transport fiber size must be a positive integer")
    valid_values = set(range(fiber_size))
    if anchor_vertex not in names or type(anchor_value) is not int or anchor_value not in valid_values:
        raise ContinuationError("transport anchor is outside its declared fiber")
    prescribed = dict(required or {})
    if any(vertex not in names or type(value) is not int or value not in valid_values
           for vertex, value in prescribed.items()):
        raise ContinuationError("a required transported endpoint is outside its fiber")
    adjacency: dict[str, list[tuple[str, tuple[int, ...]]]] = {name: [] for name in names}
    for left, right, values in edges:
        permutation = tuple(values)
        if left not in adjacency or right not in adjacency or len(permutation) != fiber_size:
            raise ContinuationError("transport edge has an unknown endpoint or wrong fiber size")
        if any(type(value) is not int for value in permutation) or set(permutation) != valid_values:
            raise ContinuationError("transport edge must be a bijection")
        inverse = [0] * fiber_size
        for value, image in enumerate(permutation):
            inverse[image] = value
        adjacency[left].append((right, permutation))
        adjacency[right].append((left, tuple(inverse)))
    # Validate the connected-graph hypothesis before returning a local conflict.
    reached = {anchor_vertex}
    pending = [anchor_vertex]
    while pending:
        left = pending.pop()
        for right, _ in adjacency[left]:
            if right not in reached:
                reached.add(right)
                pending.append(right)
    if reached != set(names):
        raise ContinuationError("the transport graph must be connected")
    assignment = {anchor_vertex: anchor_value}
    pending = [anchor_vertex]
    while pending:
        left = pending.pop()
        for right, permutation in adjacency[left]:
            image = permutation[assignment[left]]
            if right in assignment:
                if assignment[right] != image:
                    return TransportResult(False, tuple(sorted(assignment.items())), (left, right))
            else:
                assignment[right] = image
                pending.append(right)
    for vertex, value in prescribed.items():
        if assignment[vertex] != value:
            return TransportResult(False, tuple(sorted(assignment.items())), (vertex, vertex))
    return TransportResult(True, tuple(sorted(assignment.items())), None)
