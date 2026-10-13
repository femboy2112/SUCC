"""Finite connection/cover repair and fixed-point holonomy theorem.

A failed global potential is never declared true on the original carrier.
A voltage cover retains the same edge law but changes the state space.
For non-free permutation actions, nontrivial holonomy can still have a
parallel section: the right criterion is common fixed points, NOT flatness.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import gcd

from .relational_model_genetics import GeneticsError


@dataclass(frozen=True)
class VoltageGraph:
    vertices: tuple[str, ...]
    edges: tuple[tuple[str, str, int], ...]
    modulus: int
    source_id: str = "declared-graph"
    epoch: int = 0
    basis: str = "additive-transport"

    def __post_init__(self):
        if (type(self.modulus) is not int or not 2 <= self.modulus <= 12
                or not self.vertices or len(set(self.vertices)) != len(self.vertices)
                or type(self.edges) is not tuple
                or any(u not in self.vertices or v not in self.vertices
                       or type(w) is not int or not 0 <= w < self.modulus
                       for u, v, w in self.edges)
                or not self.source_id or not self.basis
                or type(self.epoch) is not int or self.epoch < 0):
            raise GeneticsError("Malformed source-typed finite voltage graph")

    def adjacency(self) -> dict[str, list[tuple[str, int]]]:
        adj = {v: [] for v in self.vertices}
        for u, v, w in self.edges:
            adj[u].append((v, w))
            adj[v].append((u, (-w) % self.modulus))
        return adj

    def tree_potentials(self) -> dict[str, int]:
        root = self.vertices[0]
        h = {root: 0}
        todo = [root]
        adj = self.adjacency()
        for u in todo:
            for v, w in adj[u]:
                if v not in h:
                    h[v] = (h[u] + w) % self.modulus
                    todo.append(v)
        if len(h) != len(self.vertices):
            raise GeneticsError("Connected base graph required; split components")
        return h

    def residuals(self) -> tuple[int, ...]:
        h = self.tree_potentials()
        return tuple((h[u] + w - h[v]) % self.modulus
                     for u, v, w in self.edges)

    def holonomy_subgroup(self) -> tuple[int, ...]:
        """Image of pi_1 in Z/m (fundamental cycle residual generators)."""
        d = gcd(self.modulus, *self.residuals())
        return tuple(range(0, self.modulus, d))

    def global_potential_exists(self) -> bool:
        return all(r == 0 for r in self.residuals())

    def brute_force_potentials(self) -> int:
        if self.modulus ** len(self.vertices) > 250000:
            raise GeneticsError("Independent exhaustive oracle exceeds budget")
        count = 0
        for values in product(range(self.modulus), repeat=len(self.vertices)):
            q = dict(zip(self.vertices, values))
            if all((q[v] - q[u]) % self.modulus == w
                   for u, v, w in self.edges):
                count += 1
        return count

    def lifted_reachable(self) -> frozenset[tuple[str, int]]:
        """One connected component of the canonical m-sheet voltage cover."""
        adj = self.adjacency()
        root = (self.vertices[0], 0)
        reached = {root}
        todo = [root]
        for v, level in todo:
            for w, delta in adj[v]:
                next_vertex = (w, (level + delta) % self.modulus)
                if next_vertex not in reached:
                    reached.add(next_vertex)
                    todo.append(next_vertex)
        return frozenset(reached)

    def verify_lifted_scalar(self) -> bool:
        """q(v,a)=a satisfies each lifted edge law. Does NOT descend."""
        return all(((level + w) - level) % self.modulus == w
                   for u, v, w in self.edges
                   for level in range(self.modulus))

    def cover_report(self) -> dict:
        subgroup = self.holonomy_subgroup()
        reached = self.lifted_reachable()
        fiber_sizes = {v: sum((v, a) in reached
                              for a in range(self.modulus)) for v in self.vertices}
        if any(n != len(subgroup) for n in fiber_sizes.values()):
            raise AssertionError("Cover monodromy and BFS disagree")
        return {
            "source_id": self.source_id,
            "epoch": self.epoch,
            "basis": self.basis,
            "nonzero_fundamental_residuals": [r for r in self.residuals() if r],
            "holonomy_image": list(subgroup),
            "global_base_potential": self.global_potential_exists(),
            "minimal_connected_trivializing_cover_degree": len(subgroup),
            "canonical_cover_components": self.modulus // len(subgroup),
            "connected_lift_vertices": len(reached),
            "fiber_sizes_on_one_lift_component": fiber_sizes,
            "scalar_on_cover_verified": self.verify_lifted_scalar(),
            "scalar_on_base_claimed_after_repair": False,
        }


def compose_permutations(first: tuple[int, ...],
                         second: tuple[int, ...]) -> tuple[int, ...]:
    """Second after first; used for actual oriented path transport."""
    if len(first) != len(second) or set(first) != set(range(len(first))) \
            or set(second) != set(range(len(second))):
        raise GeneticsError("Both transports must be permutations of same fiber")
    return tuple(second[first[i]] for i in range(len(first)))


@dataclass(frozen=True)
class PermutationGraph:
    vertices: tuple[str, ...]
    edges: tuple[tuple[str, str, tuple[int, ...]], ...]
    fiber_size: int

    def __post_init__(self):
        if (type(self.fiber_size) is not int or not 1 <= self.fiber_size <= 6
                or not self.vertices or len(set(self.vertices)) != len(self.vertices)
                or any(u not in self.vertices or v not in self.vertices
                       or len(p) != self.fiber_size
                       or set(p) != set(range(self.fiber_size))
                       for u, v, p in self.edges)):
            raise GeneticsError("Malformed invertible finite fiber transports")

    def oriented_adjacency(self):
        adj = {v: [] for v in self.vertices}
        for u, v, p in self.edges:
            inverse = tuple(p.index(i) for i in range(self.fiber_size))
            adj[u].append((v, p))
            adj[v].append((u, inverse))
        return adj

    def tree_transports(self):
        ident = tuple(range(self.fiber_size))
        tree = {self.vertices[0]: ident}
        todo = [self.vertices[0]]
        adj = self.oriented_adjacency()
        for u in todo:
            for v, p in adj[u]:
                if v not in tree:
                    tree[v] = compose_permutations(tree[u], p)
                    todo.append(v)
        if len(tree) != len(self.vertices):
            raise GeneticsError("Connected action graph required")
        return tree

    def root_fixed_points(self) -> tuple[int, ...]:
        """Root values that survive EVERY fundamental cycle equation."""
        t = self.tree_transports()
        return tuple(i for i in range(self.fiber_size)
                     if all(p[t[u][i]] == t[v][i] for u, v, p in self.edges))

    def independent_assignment_count(self) -> int:
        if self.fiber_size ** len(self.vertices) > 250000:
            raise GeneticsError("Finite independent action oracle exceeds budget")
        return sum(all(p[a[self.vertices.index(u)]] == a[self.vertices.index(v)]
                       for u, v, p in self.edges)
                   for a in product(range(self.fiber_size),
                                    repeat=len(self.vertices)))

    def nontrivial_holonomy(self) -> bool:
        """Check whether some edge has a nonidentity based loop transport."""
        t = self.tree_transports()
        return any(any(p[t[u][i]] != t[v][i]
                       for i in range(self.fiber_size))
                   for u, v, p in self.edges)


def language_birth_demo() -> dict:
    triangle = VoltageGraph(("x", "y", "z"),
                            (("x", "y", 1), ("y", "z", 1),
                             ("x", "z", 1)), 2)
    cover = triangle.cover_report()
    if triangle.brute_force_potentials() != 0:
        raise AssertionError("Independent source scalar oracle contradicts holonomy")
    transposition = (1, 0, 2)
    # One loop permutes two fiber values, leaving a third fixed.
    nonfree = PermutationGraph(("root",), (("root", "root", transposition),), 3)
    # Two separate nontrivial cycles each fix a DIFFERENT point.
    distinct = PermutationGraph(("root",),
                                (("root", "root", (1, 0, 2)),
                                 ("root", "root", (0, 2, 1))), 3)
    return {
        "parity_triangle": cover,
        "nonfree_nontrivial_holonomy": nonfree.nontrivial_holonomy(),
        "nonfree_parallel_sections": len(nonfree.root_fixed_points()),
        "independent_nonfree_section_count": nonfree.independent_assignment_count(),
        "incompatible_fixed_sets_section_count": len(distinct.root_fixed_points()),
        "independent_incompatible_count": distinct.independent_assignment_count(),
        "physical_gauge_field_claimed": False,
    }
