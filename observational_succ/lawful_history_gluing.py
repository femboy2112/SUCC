"""Exact certificates for source-preserving lifting of finite report paths.

The powerset recursion is classical and already appears in CAMBRIAN C18.2.
This module adds a complete finite *all projected paths* audit, independently
checked path/cut certificates, and the private-interface flow integrality gate.
No result labels a possible path as performed or a supported law as operational.
Paper proofs and priority boundaries: research/2026-10-18/LAWFUL_HISTORY_GLUING.md.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping


class GluingError(ValueError):
    """A certificate or a finite source contract is malformed."""


@dataclass(frozen=True, order=True)
class PrivateState:
    source: str
    name: str
    report: str

    def __post_init__(self):
        if any(type(v) is not str or not v for v in
               (self.source, self.name, self.report)):
            raise GluingError("Nonempty source, state, and report strings required")


@dataclass(frozen=True)
class SourceGraph:
    states: tuple[PrivateState, ...]
    initial: frozenset[PrivateState]
    edges: frozenset[tuple[PrivateState, str, PrivateState]]

    def __post_init__(self):
        if (type(self.states) is not tuple or not self.states
                or any(not isinstance(x, PrivateState) for x in self.states)
                or type(self.initial) is not frozenset
                or type(self.edges) is not frozenset):
            raise GluingError("Explicit immutable finite state and edge tables required")
        if len({(x.source, x.name) for x in self.states}) != len(self.states):
            raise GluingError("A source/state identity has exactly one report")
        if not self.initial <= set(self.states):
            raise GluingError("Initial state outside declared carrier")
        for edge in self.edges:
            if type(edge) is not tuple or len(edge) != 3:
                raise GluingError("Edges are (private input, action, private output)")
            x, action, z = edge
            if (x not in self.states or z not in self.states
                    or type(action) is not str or not action):
                raise GluingError("Transition outside declared carrier or action alphabet")
            if x.source != z.source:
                raise GluingError("A transition may not switch the original source")

    def projected_edges(self, source: str):
        _check_source(self, source)
        return frozenset((x.report, a, z.report) for x, a, z in self.edges
                         if x.source == source)


@dataclass(frozen=True)
class PathCertificate:
    source: str
    reports: tuple[str, ...]
    actions: tuple[str, ...]
    states: tuple[PrivateState, ...]


@dataclass(frozen=True)
class CutCertificate:
    source: str
    reports: tuple[str, ...]
    actions: tuple[str, ...]
    layers: tuple[frozenset[PrivateState], ...]


@dataclass(frozen=True)
class UniformCertificate:
    source: str
    configurations: frozenset[tuple[str, frozenset[PrivateState]]]


@dataclass(frozen=True)
class UniformAudit:
    status: str  # ALL_PROJECTED_PATHS_LIFT, SPURIOUS_PATH, or UNRESOLVED
    explored: int
    certificate: UniformCertificate | CutCertificate | None


def _check_source(model, source):
    if type(source) is not str or not any(x.source == source for x in model.states):
        raise GluingError("A declared original source is required")


def _check_word(model, source, reports, actions):
    _check_source(model, source)
    if (type(reports) is not tuple or type(actions) is not tuple
            or len(reports) != len(actions) + 1
            or any(type(v) is not str or not v for v in reports + actions)):
        raise GluingError("A nonempty report word and one action per transition required")


def locally_compatible(model, source, reports, actions):
    """Each report edge has a witness; the private witnesses may disagree."""
    _check_word(model, source, reports, actions)
    return (any(x.source == source and x.report == reports[0] for x in model.initial)
            and all((reports[i], a, reports[i + 1]) in model.projected_edges(source)
                    for i, a in enumerate(actions)))


def lift_or_cut(model, source, reports, actions):
    """Produce either one genuine private lift or a closed empty-terminal cut."""
    _check_word(model, source, reports, actions)
    current = {x: (x,) for x in model.initial
               if x.source == source and x.report == reports[0]}
    layers = [frozenset(current)]
    for i, action in enumerate(actions):
        following = {}
        for x, a, z in sorted(model.edges):
            if a == action and x in current and z.report == reports[i + 1]:
                following.setdefault(z, current[x] + (z,))
        current = following
        layers.append(frozenset(current))
    if current:
        return PathCertificate(source, reports, actions, current[min(current)])
    return CutCertificate(source, reports, actions, tuple(layers))


def verify_path(model, certificate):
    """Check original tables directly, without invoking the path generator."""
    if not isinstance(certificate, PathCertificate):
        return False
    c = certificate
    try:
        _check_word(model, c.source, c.reports, c.actions)
        return (type(c.states) is tuple and len(c.states) == len(c.reports)
                and c.states[0] in model.initial
                and all(x in model.states and x.source == c.source and x.report == y
                        for x, y in zip(c.states, c.reports))
                and all((c.states[i], a, c.states[i + 1]) in model.edges
                        for i, a in enumerate(c.actions)))
    except (GluingError, TypeError, AttributeError):
        return False


def verify_cut(model, certificate):
    """Verify an inductive overapproximation ending empty, independently.

    Equality with reachable layers is unnecessary: initial containment and
    transition closure suffice. This checker does not call lift_or_cut.
    """
    if not isinstance(certificate, CutCertificate):
        return False
    c = certificate
    try:
        _check_word(model, c.source, c.reports, c.actions)
        if (type(c.layers) is not tuple or len(c.layers) != len(c.reports)
                or any(type(layer) is not frozenset for layer in c.layers)
                or c.layers[-1]):
            return False
        if any(x not in model.states or x.source != c.source or x.report != y
               for layer, y in zip(c.layers, c.reports) for x in layer):
            return False
        if any(x not in c.layers[0] for x in model.initial
               if x.source == c.source and x.report == c.reports[0]):
            return False
        return all(z in c.layers[i + 1]
                   for i, action in enumerate(c.actions) for x, a, z in model.edges
                   if a == action and x in c.layers[i] and z.report == c.reports[i + 1])
    except (GluingError, TypeError, AttributeError):
        return False


def obstruction_bound(model, source):
    """If a projected path is spurious, a shortest one has <= this many edges."""
    _check_source(model, source)
    sizes = {}
    for x in model.states:
        if x.source == source:
            sizes[x.report] = sizes.get(x.report, 0) + 1
    return sum(2 ** n - 1 for n in sizes.values())


def audit_projection(model, source, *, max_configurations=100_000):
    """Complete powerset audit, with explicit UNRESOLVED on budget exhaustion.

    Every abstract path starts at a report of an allowed initial private state.
    The algorithm checks possible paths, not safe/causal online policies.
    """
    _check_source(model, source)
    if type(max_configurations) is not int or max_configurations < 1:
        raise GluingError("A positive exact configuration budget is required")
    initial_reports = sorted({x.report for x in model.initial if x.source == source})
    queue, seen = deque(), set()
    for y in initial_reports:
        support = frozenset(x for x in model.initial if x.source == source and x.report == y)
        if len(seen) == max_configurations:
            return UniformAudit("UNRESOLVED", len(seen), None)
        seen.add((y, support))
        queue.append((y, support, (y,), ()))
    quotient = sorted(model.projected_edges(source))
    while queue:
        y, support, reports, actions = queue.popleft()
        for before, action, after in quotient:
            if before != y:
                continue
            following = frozenset(z for x, a, z in model.edges
                                  if x in support and a == action and z.report == after)
            if not following:
                cut = lift_or_cut(model, source, reports + (after,), actions + (action,))
                return UniformAudit("SPURIOUS_PATH", len(seen), cut)
            key = (after, following)
            if key not in seen:
                if len(seen) == max_configurations:
                    return UniformAudit("UNRESOLVED", len(seen), None)
                seen.add(key)
                queue.append((after, following, reports + (after,), actions + (action,)))
    return UniformAudit("ALL_PROJECTED_PATHS_LIFT", len(seen),
                        UniformCertificate(source, frozenset(seen)))


def verify_uniform(model, certificate):
    """Check nonempty invariant supports; no search algorithm is trusted."""
    if not isinstance(certificate, UniformCertificate):
        return False
    c = certificate
    try:
        _check_source(model, c.source)
        if type(c.configurations) is not frozenset:
            return False
        for y, support in c.configurations:
            if (type(y) is not str or type(support) is not frozenset or not support
                    or any(x not in model.states or x.source != c.source or x.report != y
                           for x in support)):
                return False
        for y in {x.report for x in model.initial if x.source == c.source}:
            initial = frozenset(x for x in model.initial if x.source == c.source and x.report == y)
            if (y, initial) not in c.configurations:
                return False
        for y, support in c.configurations:
            for before, action, after in model.projected_edges(c.source):
                if before == y:
                    following = frozenset(z for x, a, z in model.edges
                                          if x in support and a == action and z.report == after)
                    if not following or (after, following) not in c.configurations:
                        return False
        return True
    except (GluingError, ValueError, TypeError, AttributeError):
        return False


def verify_unit_flow(model, source, reports, actions,
                     node_mass: tuple[Mapping[PrivateState, Fraction], ...],
                     edge_mass: tuple[Mapping[tuple[PrivateState, PrivateState], Fraction], ...]):
    """Exact supported unit flow on COMPLETE private time-layer interfaces.

    A valid flow implies an integral private path. Arbitrary prescribed
    marginal/chance/resource constraints cannot be appended to this theorem.
    Floats, even 0.0 or 1.0, and booleans are deliberately rejected.
    """
    try:
        _check_word(model, source, reports, actions)
        if len(node_mass) != len(reports) or len(edge_mass) != len(actions):
            return False
        for i, masses in enumerate(node_mass):
            if any(type(v) not in (int, Fraction) or v < 0 for v in masses.values()):
                return False
            if sum(masses.values()) != 1:
                return False
            if any(x not in model.states or x.source != source or x.report != reports[i]
                   for x in masses):
                return False
            if i == 0 and any(v and x not in model.initial for x, v in masses.items()):
                return False
        for i, masses in enumerate(edge_mass):
            if any(type(v) not in (int, Fraction) or v < 0 for v in masses.values()):
                return False
            if any((x, actions[i], z) not in model.edges
                   or x.source != source or x.report != reports[i] or z.report != reports[i + 1]
                   for x, z in masses):
                return False
            for x in model.states:
                if sum(v for (before, _), v in masses.items() if before == x) != node_mass[i].get(x, 0):
                    return False
                if sum(v for (_, after), v in masses.items() if after == x) != node_mass[i + 1].get(x, 0):
                    return False
        return True
    except (GluingError, ValueError, TypeError, AttributeError):
        return False


def path_from_flow(model, source, reports, actions, node_mass, edge_mass):
    """Extract a 0/1 path from a valid rational flow; fixed chance laws excluded."""
    if not verify_unit_flow(model, source, reports, actions, node_mass, edge_mass):
        raise GluingError("Invalid exact private-interface unit flow")
    states = [min(x for x, mass in node_mass[0].items() if mass > 0)]
    for masses in edge_mass:
        states.append(min(z for (x, z), mass in masses.items() if x == states[-1] and mass > 0))
    return PathCertificate(source, reports, actions, tuple(states))
