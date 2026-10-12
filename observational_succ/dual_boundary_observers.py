"""Dual SUCC boundary observers on ONE finite source and one harmonic carrier.

Finite source partitions, maximal common deterministic observations, exact
conditional expectations, and two-sided harmonic Dirichlet-to-Neumann gluing.
All claims are CLASSICAL finite probability/graph Laplacian mathematics. Source
IDs and probes are mathematical declarations, not empirical authentication.
"""
from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction as F
from typing import Hashable, Mapping, Sequence

from .shared_carrier_descent import SharedCarrierGraph, CarrierDescentError, _solve, exact as _exact


class DualBoundaryError(ValueError):
    """Stale source, nonfiltration, forged probe, unsupported carrier or boundary."""

def exact(value):
    try:
        return _exact(value)
    except CarrierDescentError as exc:
        raise DualBoundaryError(str(exc)) from exc


def _signature(values: Sequence[Hashable], n: int) -> tuple[Hashable, ...]:
    t = tuple(values)
    if len(t) != n:
        raise DualBoundaryError("Every level must report on ALL source states")
    for x in t:
        hash(x)
    return t


def _refines(finer: Sequence[Hashable], coarser: Sequence[Hashable]) -> bool:
    seen = {}
    for a, b in zip(finer, coarser):
        if a in seen and seen[a] != b:
            return False
        seen[a] = b
    return True


@dataclass(frozen=True)
class DualFiniteTower:
    """Two growing observation partitions of one known finite source universe.

    Each level signature is the full cumulative observation vector, NOT merely
    the most recent response. Finer equal fibers must lie in coarser equal
    fibers. No physical instrument semantics or source authenticity inferred.
    """
    source_id: str
    version: int
    states: tuple[Hashable, ...]
    prior: tuple[F, ...]
    left: tuple[tuple[Hashable, ...], ...]
    right: tuple[tuple[Hashable, ...], ...]

    def __post_init__(self) -> None:
        if not self.source_id or type(self.version) is not int or self.version < 0:
            raise DualBoundaryError("Declared source identity and version required")
        if not self.states or len(set(self.states)) != len(self.states):
            raise DualBoundaryError("Finite states must be nonempty, distinct and hashable")
        n = len(self.states)
        ps = tuple(exact(v) for v in self.prior)
        if len(ps) != n or any(v <= 0 for v in ps) or sum(ps, F(0)) != 1:
            raise DualBoundaryError("Strictly positive normalized exact prior required")
        object.__setattr__(self, "prior", ps)
        for side in (self.left, self.right):
            if not side or type(side) is not tuple:
                raise DualBoundaryError("Each observer needs at least one level")
            for j, signature in enumerate(side):
                if type(signature) is not tuple:
                    raise DualBoundaryError("Cumulative observations are immutable tuples")
                _signature(signature, n)
                if j and not _refines(signature, side[j - 1]):
                    raise DualBoundaryError("Refinement forgot earlier observations")

    def observations(self, side: str, level: int = -1) -> tuple[Hashable, ...]:
        if side not in ("left", "right"):
            raise DualBoundaryError("Observer must be left or right")
        levels = self.left if side == "left" else self.right
        if type(level) is not int or not (-len(levels) <= level < len(levels)):
            raise DualBoundaryError("Unobserved tower level")
        return levels[level]

    def _coarsest_common_factor(self, ls: tuple, rs: tuple) -> tuple[int, ...]:
        """Connected components of the bipartite joint-support graph.

        This is the maximal common deterministic factor of left and right.
        Every function simultaneously factored through both observations
        factors through these components (finite Gacs-Korner common part).
        """
        adjacency = defaultdict(set)
        for a, b in zip(ls, rs):
            u, v = ("L", a), ("R", b)
            adjacency[u].add(v)
            adjacency[v].add(u)
        owner = {}
        for u in adjacency:
            if u in owner:
                continue
            label = len(set(owner.values()))
            work = [u]
            owner[u] = label
            while work:
                v = work.pop()
                for w in adjacency[v]:
                    if w not in owner:
                        owner[w] = label
                        work.append(w)
        return tuple(owner[("L", a)] for a in ls)

    def common_factor(self, left_level: int = -1, right_level: int = -1) -> dict:
        ls = self.observations("left", left_level)
        rs = self.observations("right", right_level)
        components = self._coarsest_common_factor(ls, rs)
        labels = tuple(sorted(set(components)))
        probabilities = tuple(sum((p for p, c in zip(self.prior, components)
                                   if c == label), F(0)) for label in labels)
        witness_variance = (probabilities[0] * (1 - probabilities[0])
                            if len(labels) > 1 else F(0))
        # Both observers can decode the same component label, source by source.
        for obs in (ls, rs):
            decoder = {}
            for value, component in zip(obs, components):
                if value in decoder and decoder[value] != component:
                    raise AssertionError("Common-part decoder not well-defined")
                decoder[value] = component
        return {"states_to_component": components,
                "common_component_masses": probabilities,
                "component_count": len(labels),
                "nonconstant_common_witness": len(labels) > 1,
                "exact_common_witness_covariance": witness_variance}

    def conditional_expectation(self, target: Sequence[F],
                                side: str = "joint",
                                left_level: int = -1,
                                right_level: int = -1) -> tuple[F, ...]:
        """Exact L2 projection onto one tower, or information JOIN of both."""
        values = tuple(exact(v) for v in target)
        if len(values) != len(self.states):
            raise DualBoundaryError("Target must cover original source states")
        ls = self.observations("left", left_level)
        rs = self.observations("right", right_level)
        if side == "left":
            signature = ls
        elif side == "right":
            signature = rs
        elif side == "joint":
            signature = tuple(zip(ls, rs))
        else:
            raise DualBoundaryError("Projection must be left, right or joint")
        mass, total = defaultdict(F), defaultdict(F)
        for group, p, v in zip(signature, self.prior, values):
            mass[group] += p
            total[group] += p * v
        return tuple(total[group] / mass[group] for group in signature)

    def correlation_receipt(self, target: Sequence[F],
                            left_level: int = -1, right_level: int = -1) -> dict:
        """Exact dual conditional-projection correlation identity.

        X=E[T|left], Y=E[T|right] on ONE fixed source probability law.
        This is a theorem about shared knowledge of T, not general positive
        correlations of all carrier observables or any Archimedean limit.
        """
        values = tuple(exact(v) for v in target)
        x = self.conditional_expectation(values, "left", left_level,right_level)
        y = self.conditional_expectation(values, "right",left_level,right_level)
        mean = sum((p*v for p,v in zip(self.prior, values)),F(0))
        variance = sum((p*(v-mean)**2 for p,v in zip(self.prior, values)),F(0))
        left_error = sum((p*(v-a)**2 for p,v,a in zip(self.prior,values,x)),F(0))
        right_error = sum((p*(v-a)**2 for p,v,a in zip(self.prior,values,y)),F(0))
        distance = sum((p*(a-b)**2 for p,a,b in zip(self.prior,x,y)),F(0))
        covariance = sum((p*(a-mean)*(b-mean)
                          for p,a,b in zip(self.prior,x,y)),F(0))
        if 2*(variance-covariance) != left_error+right_error+distance:
            raise AssertionError("Conditional-projection Pythagorean identity failed")
        if distance>2*(left_error+right_error):
            raise AssertionError("L2 difference violates triangle Cauchy bound")
        lower = variance-F(3,2)*(left_error+right_error)
        if covariance<lower:
            raise AssertionError("The exact covariance lower bound was violated")
        return {"target_variance": variance,
                "left_l2_error_squared":left_error,
                "right_l2_error_squared":right_error,
                "cross_l2_distance_squared":distance,
                "estimate_covariance":covariance,
                "covariance_guaranteed_lower":lower,
                "strict_correlation_certified":lower>0}

    def claim_factors(self, target: Sequence[Hashable],
                      side: str = "joint", left_level: int = -1,
                      right_level: int = -1) -> dict:
        """Finite source-fiber necessary and sufficient claim-decoding test."""
        target = _signature(target, len(self.states))
        ls = self.observations("left", left_level)
        rs = self.observations("right", right_level)
        if side == "left":
            keys = ls
        elif side == "right":
            keys = rs
        elif side == "joint":
            keys = tuple(zip(ls, rs))
        else:
            raise DualBoundaryError("Unknown observer perspective")
        seen = {}
        for i, (key, value) in enumerate(zip(keys, target)):
            if key in seen and seen[key][1] != value:
                return {"factors": False,
                        "counterexample_states": (self.states[seen[key][0]], self.states[i])}
            seen[key] = (i, value)
        return {"factors": True, "decoded_fibers": len(seen)}


def _split_vertices(graph: SharedCarrierGraph, outer: Sequence[Hashable],
                    interface: Sequence[Hashable]) -> None:
    if (len(set(outer)) != len(tuple(outer)) or
        len(set(interface)) != len(tuple(interface)) or
        set(outer) & set(interface) or
        set(graph.boundary) != set(outer) | set(interface) or
        not outer or not interface):
        raise DualBoundaryError("Half-carrier boundary must partition into outer and interface")


@dataclass(frozen=True)
class TwoSidedHarmonicCarrier:
    """Two overlapping half-graphs on one source, meeting ONLY at interface.

    Both sides supply their own interior vertices and edge laws. A global
    harmonic solution requires potential matching AND flux conservation;
    just matching the interface values is not sufficient.
    """
    left: SharedCarrierGraph
    right: SharedCarrierGraph
    left_outer: tuple[Hashable, ...]
    right_outer: tuple[Hashable, ...]
    interface: tuple[Hashable, ...]

    def __post_init__(self) -> None:
        if not self.interface or len(set(self.interface)) != len(self.interface):
            raise DualBoundaryError("Exact nonempty interface required")
        if (self.left.carrier_id, self.left.version) != (self.right.carrier_id, self.right.version):
            raise DualBoundaryError("Different original carriers or stale carrier version")
        _split_vertices(self.left, self.left_outer, self.interface)
        _split_vertices(self.right, self.right_outer, self.interface)
        if set(self.left_outer) & set(self.right_outer):
            raise DualBoundaryError("Two outer boundaries must be disjoint")
        if set(self.left.vertices) & set(self.right.vertices) != set(self.interface):
            raise DualBoundaryError("Hidden vertex intersection outside declared interface")
        if ({frozenset((a,b)) for a,b,_ in self.left.edges} &
                {frozenset((a,b)) for a,b,_ in self.right.edges}):
            raise DualBoundaryError("An edge cannot be owned by both half-carriers")

    def merged_graph(self) -> SharedCarrierGraph:
        vertices = tuple(dict.fromkeys(self.left.vertices + self.right.vertices))
        edges = self.left.edges + self.right.edges
        boundary = self.left_outer + self.right_outer
        return SharedCarrierGraph(self.left.carrier_id, self.left.version,
                                  vertices, boundary, edges)

    def interface_solution(self, lvals: Mapping[Hashable,F],
                           rvals: Mapping[Hashable,F]) -> dict:
        if set(lvals) != set(self.left_outer) or set(rvals) != set(self.right_outer):
            raise DualBoundaryError("Missing or extra original source outer reports")
        lvals = {v:exact(k) for v,k in lvals.items()}
        rvals = {v:exact(k) for v,k in rvals.items()}
        faces = (self.left, self.right)
        reported = (lvals, rvals)
        n = len(self.interface)
        A = [[F(0) for _ in range(n)] for _ in range(n)]
        rhs = [F(0) for _ in range(n)]
        for graph, known in zip(faces, reported):
            lam = graph.boundary_operator()
            where = {v:i for i,v in enumerate(graph.boundary)}
            for i, v in enumerate(self.interface):
                for j, w in enumerate(self.interface):
                    A[i][j] += lam[where[v]][where[w]]
                rhs[i] -= sum((lam[where[v]][where[u]] * b
                               for u,b in known.items()), F(0))
        try:
            values = _solve(A, rhs)
        except CarrierDescentError as exc:
            raise DualBoundaryError("Unanchored or nonunique global interface") from exc
        mid = dict(zip(self.interface,values))
        lfield = self.left.complete_harmonic({**lvals,**mid})
        rfield = self.right.complete_harmonic({**rvals,**mid})
        lf,rf = self.left.flux(lfield), self.right.flux(rfield)
        matched_flux = {v:lf[v]+rf[v] for v in self.interface}
        if any(matched_flux.values()):
            raise AssertionError("Computed interface violates signed flux matching")
        full = {**lfield,**rfield}
        graph = self.merged_graph()
        directly = graph.complete_harmonic({**lvals,**rvals})
        if full != directly:
            raise AssertionError("Indirect half-gluing differs from direct global solution")
        total_energy = self.left.energy(lfield) + self.right.energy(rfield)
        if total_energy != graph.energy(full) or total_energy != graph.boundary_energy({**lvals,**rvals}):
            raise AssertionError("The interface energy failed to glue exactly")
        return {"interface":mid, "source_field":full,
                "interface_flux_residual":matched_flux,
                "global_energy":total_energy,
                "source_identical":True,
                "global_harmonic_verified":True}


def two_port_carrier(graph: SharedCarrierGraph,
                     left_boundary: Sequence[Hashable],
                     right_boundary: Sequence[Hashable]) -> dict:
    """Exact effective end-to-end conductance; a POSITIVE finite bridge
    need not have a positive lower bound under increasing separation.
    """
    left,right = tuple(left_boundary),tuple(right_boundary)
    if (not left or not right or len(set(left)) != len(left) or
            len(set(right)) != len(right) or set(left) & set(right) or
            set(left)|set(right) != set(graph.boundary)):
        raise DualBoundaryError("Nonempty disjoint complete two-port partition needed")
    lam = graph.boundary_operator()
    where = {v:i for i,v in enumerate(graph.boundary)}
    cross = -sum((lam[where[x]][where[y]] for x in left for y in right), F(0))
    if cross < 0:
        raise AssertionError("Passive conductance network has negative port coupling")
    data = {v:(F(0) if v in set(left) else F(1)) for v in graph.boundary}
    energy = graph.boundary_energy(data)
    if energy != cross / 2:
        raise AssertionError("Two-port energy/effective coupling identity failed")
    return {"effective_conductance": cross, "energy_for_unit_jump": energy,
            "strictly_coupled":cross>0}


def unit_path_two_port(n: int) -> dict:
    if type(n) is not int or n < 1:
        raise DualBoundaryError("At least one unit-resistor edge required")
    graph = SharedCarrierGraph("one-carrier-resistor-path", 1,
                               tuple(range(n+1)), (0,n),
                               tuple((k,k+1,F(1)) for k in range(n)))
    report = two_port_carrier(graph,(0,),(n,))
    if report["effective_conductance"] != F(1,n):
        raise AssertionError("Unit resistor path conductance formula failed")
    return {"edges": n, **report}


def symmetric_binary_chain_end_correlation(steps: int, flip: F) -> dict:
    """Two ends of one stationary 2-state Markov carrier can decorrelate.

    X_0 uniform in {-1,+1}; independent edge signs E_i are -1 with
    probability flip; X_n = X_0 product E_i. Exact Cov(X_0,X_n) is
    (1-2*flip)**n, despite shared carrier and identical endpoint marginals.
    """
    if type(steps) is not int or steps < 0:
        raise DualBoundaryError("Finite nonnegative number of steps required")
    p = exact(flip)
    if not 0 <= p <= 1:
        raise DualBoundaryError("Transition probability outside [0,1]")
    cov = (1-2*p)**steps
    return {"steps":steps,"flip_probability":p,
            "endpoint_covariance":cov,"both_marginals_symmetric":True,
            "shared_carrier":True}
