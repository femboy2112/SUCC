#!/usr/bin/env python3
"""X02: exact permutation-holonomy/law-section oracle, independent of cohorts.

The optional A04 audit imports its implementation only as the system under test.
All proof oracles below use integer permutations or fractions.Fraction.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from collections import deque
from fractions import Fraction as Q
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def compose(g, h):
    return tuple(g[h[x]] for x in range(len(g)))


def inverse(g):
    if sorted(g) != list(range(len(g))):
        raise ValueError("A transport must be a permutation")
    return tuple(g.index(x) for x in range(len(g)))


def push(g, law):
    if len(g) != len(law):
        raise ValueError("Transport/law carrier mismatch")
    inv = inverse(g)
    return tuple(law[inv[x]] for x in range(len(g)))


def generated_group(degree, generators):
    unit = tuple(range(degree))
    if degree < 1:
        raise ValueError("Nonempty finite carrier required")
    for g in generators:
        if len(g) != degree:
            raise ValueError("Generator carrier mismatch")
        inverse(g)
    seen = {unit}
    pending = [unit]
    while pending:
        h = pending.pop()
        for g in generators:
            gh = compose(g, h)
            if gh not in seen:
                seen.add(gh)
                pending.append(gh)
    return tuple(sorted(seen))


def orbit_partition(degree, generators):
    group = generated_group(degree, generators)
    remaining = set(range(degree))
    parts = []
    while remaining:
        x = min(remaining)
        orbit = tuple(sorted({g[x] for g in group}))
        parts.append(orbit)
        remaining.difference_update(orbit)
    return tuple(parts)


def uniform_on(degree, subset):
    if not subset:
        raise ValueError("Cannot normalize empty orbit")
    return tuple(Q(1, len(subset)) if x in subset else Q(0) for x in range(degree))


def rank(rows, columns):
    matrix = [list(map(Q, r)) for r in rows]
    pivot = 0
    for col in range(columns):
        candidate = next((i for i in range(pivot, len(matrix)) if matrix[i][col]), None)
        if candidate is None:
            continue
        matrix[pivot], matrix[candidate] = matrix[candidate], matrix[pivot]
        scale = matrix[pivot][col]
        matrix[pivot] = [x / scale for x in matrix[pivot]]
        for i in range(len(matrix)):
            if i != pivot and matrix[i][col]:
                scale = matrix[i][col]
                matrix[i] = [x - scale * y for x, y in zip(matrix[i], matrix[pivot])]
        pivot += 1
    return pivot


def constraints(degree, generators):
    rows = []
    for g in generators:
        for x in range(degree):
            row = [Q(0)] * degree
            row[g[x]] += 1
            row[x] -= 1
            rows.append(row)
    return rows


def simplex_vertices_by_active_constraints(degree, generators):
    """Independent LP vertex oracle: enumerate zero-coordinate faces.

    Invariance forces equality along generator edges; normalized candidate
    support is tested directly. Full rank of equality + active-zero constraints
    certifies it is a vertex, without importing the group-orbit algorithm.
    """
    rows = constraints(degree, generators)
    answer = []
    for mask in range(1, 1 << degree):
        support = tuple(x for x in range(degree) if mask & (1 << x))
        mu = uniform_on(degree, support)
        if any(push(g, mu) != mu for g in generators):
            continue
        active = [[Q(int(i == x)) for i in range(degree)] for x in range(degree) if x not in support]
        if rank(rows + [[Q(1)] * degree] + active, degree) == degree:
            answer.append(mu)
    return tuple(sorted(answer))


def weak_compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for x in range(total + 1):
        for tail in weak_compositions(total - x, slots - 1):
            yield (x,) + tail


def tree_holonomy(vertices, edges, degree):
    """Connected finite graph; oriented edges carry invertible transports."""
    if not vertices or len(vertices) != len(set(vertices)) or degree < 1:
        raise ValueError("Invalid vertices or fiber")
    adjacency = {v: [] for v in vertices}
    for u, v, g in edges:
        if u not in adjacency or v not in adjacency or len(g) != degree:
            raise ValueError("Invalid edge type")
        adjacency[u].append((v, tuple(g)))
        adjacency[v].append((u, inverse(g)))
    paths = {vertices[0]: tuple(range(degree))}
    todo = deque([vertices[0]])
    while todo:
        u = todo.popleft()
        for v, g in adjacency[u]:
            if v not in paths:
                paths[v] = compose(g, paths[u])
                todo.append(v)
    if len(paths) != len(vertices):
        raise ValueError("This implementation requires a connected graph")
    holonomy = tuple(compose(inverse(paths[v]), compose(g, paths[u])) for u, v, g in edges)
    return paths, holonomy


def brute_sections(vertices, edges, degree):
    edges = tuple(edges)
    position = {v: i for i, v in enumerate(vertices)}
    return tuple(s for s in itertools.product(range(degree), repeat=len(vertices))
                 if all(s[position[v]] == g[s[position[u]]] for u, v, g in edges))


def predicted_sections(vertices, edges, degree):
    paths, loops = tree_holonomy(vertices, edges, degree)
    return tuple(tuple(paths[v][x] for v in vertices) for x in range(degree)
                 if all(h[x] == x for h in loops))


def joint_from_orbit_masses(degree, orbits, masses):
    """Rows indexed by original source; input row sums are its fixed marginal."""
    if sorted(x for orbit in orbits for x in orbit) != list(range(degree)):
        raise ValueError("Orbits must partition the carrier")
    if any(len(row) != len(orbits) or any(x < 0 for x in row) for row in masses):
        raise ValueError("Invalid nonnegative orbit masses")
    if sum(sum(row) for row in masses) != 1:
        raise ValueError("Joint law must have total mass one")
    return tuple(tuple(sum((Q(row[j], len(orbit)) for j, orbit in enumerate(orbits) if x in orbit), Q(0))
                       for x in range(degree)) for row in masses)


def posterior(joint, x):
    mass = sum(row[x] for row in joint)
    if not mass:
        raise ValueError("Cannot condition on a null event")
    return tuple(row[x] / mass for row in joint)


def decodes_target(joint, target):
    if len(joint) != len(target):
        raise ValueError("Target must retain the original source index")
    return all(len({target[o] for o, row in enumerate(joint) if row[x]}) <= 1
               for x in range(len(joint[0])))


def core_probe():
    classification_cases = 0
    grid_cases = 0
    for degree in range(1, 5):
        permutations = tuple(itertools.permutations(range(degree)))
        for generators in itertools.product(permutations, repeat=2):
            orbits = orbit_partition(degree, generators)
            expected = tuple(sorted(uniform_on(degree, orbit) for orbit in orbits))
            assert simplex_vertices_by_active_constraints(degree, generators) == expected
            assert degree - rank(constraints(degree, generators), degree) == len(orbits)
            fixed = {x for x in range(degree) if all(g[x] == x for g in generators)}
            assert fixed == {part[0] for part in orbits if len(part) == 1}
            classification_cases += 1
            # All denominator-six rational laws: independent pointwise invariance.
            for counts in weak_compositions(6, degree):
                mu = tuple(Q(c, 6) for c in counts)
                invariant = all(push(g, mu) == mu for g in generators)
                masses = tuple(sum(mu[x] for x in part) for part in orbits)
                reconstructed = tuple(sum(masses[j] * expected_mu[x]
                                          for j, expected_mu in enumerate(uniform_on(degree, p) for p in orbits))
                                      for x in range(degree))
                assert invariant == (mu == reconstructed)
                grid_cases += 1
    from observational_succ.swarm_categories import holonomy_sections
    triangle_cases = 0
    gauge_cases = 0
    permutations3 = tuple(itertools.permutations(range(3)))
    vertices = (0, 1, 2)
    gauges = ((1, 0, 2), (1, 2, 0), (2, 1, 0))
    for a, b, c in itertools.product(permutations3, repeat=3):
        edges = ((0, 1, a), (1, 2, b), (2, 0, c))
        direct = brute_sections(vertices, edges, 3)
        assert set(predicted_sections(vertices, edges, 3)) == set(direct)
        tagged = tuple((str(i), u, v, g) for i, (u, v, g) in enumerate(edges))
        result = holonomy_sections(vertices, tagged, 3, ("0", "1", "2"))
        assert set(result["sections"]) == set(direct)
        paths, loops = tree_holonomy(vertices, edges, 3)
        for orbit in orbit_partition(3, loops):
            root_law = uniform_on(3, orbit)
            laws = {v: push(paths[v], root_law) for v in vertices}
            assert all(push(g, laws[u]) == laws[v] for u, v, g in edges)
            gauge_edges = tuple((u, v, compose(gauges[v], compose(g, inverse(gauges[u])))) for u, v, g in edges)
            gauge_laws = {v: push(gauges[v], laws[v]) for v in vertices}
            assert all(push(g, gauge_laws[u]) == gauge_laws[v] for u, v, g in gauge_edges)
            gauge_cases += 1
        triangle_cases += 1
    identity = (0, 1, 2)
    transposition = (1, 0, 2)
    cycle = (1, 2, 0)
    # Simple graph with two independent cycle generators, no self-loops needed.
    nonabelian_edges = ((0, 1, identity), (1, 2, identity), (2, 3, identity),
                        (0, 2, transposition), (0, 3, cycle))
    paths, loops = tree_holonomy((0, 1, 2, 3), nonabelian_edges, 3)
    group = generated_group(3, loops)
    assert len(group) == 6 and any(compose(g, h) != compose(h, g) for g in group for h in group)
    assert brute_sections((0, 1, 2, 3), nonabelian_edges, 3) == ()
    assert orbit_partition(3, loops) == ((0, 1, 2),)
    assert simplex_vertices_by_active_constraints(3, loops) == ((Q(1, 3),) * 3,)
    # One fixed point plus one obstructed orbit: law sections strictly exceed
    # the convex hull of deterministic sections, even though a section exists.
    mixed_generators = ((1, 0, 2, 3), (1, 2, 0, 3))
    mixed_orbits = orbit_partition(4, mixed_generators)
    assert mixed_orbits == ((0, 1, 2), (3,))
    assert tuple(x for x in range(4) if all(g[x] == x for g in mixed_generators)) == (3,)
    # Original-source coupling and target condition, not just local marginals.
    orbits = ((0, 1), (2,), (3,))
    alpha = ((Q(1, 6), Q(1, 6), Q(0)), (Q(1, 3), Q(0), Q(1, 3)))
    joint = joint_from_orbit_masses(4, orbits, alpha)
    assert tuple(sum(row) for row in joint) == (Q(1, 3), Q(2, 3))
    assert all(push((1, 0, 2, 3), row) == row for row in joint)
    assert posterior(joint, 0) == posterior(joint, 1) == (Q(1, 3), Q(2, 3))
    assert posterior(joint, 2) == (Q(1), Q(0)) and posterior(joint, 3) == (Q(0), Q(1))
    assert not decodes_target(joint, (0, 1)) and decodes_target(joint, (7, 7))
    resolved = joint_from_orbit_masses(4, orbits, ((Q(1, 3), Q(0), Q(0)), (Q(0), Q(2, 3), Q(0))))
    assert decodes_target(resolved, (0, 1))
    for initial in range(3):
        delta = tuple(Q(int(x == initial)) for x in range(3))
        assert not all(push(g, delta) == delta for g in (transposition, cycle))
    # F47 bridge: translation holonomy has coset orbits, including frustration.
    import math
    clock_cases = 0
    for modulus in range(2, 9):
        for lags in itertools.product(range(modulus), repeat=3):
            residual = sum(lags) % modulus
            shift = tuple((x + residual) % modulus for x in range(modulus))
            parts = orbit_partition(modulus, (shift,))
            assert len(parts) == math.gcd(modulus, residual)
            direct_phases = tuple(s for s in itertools.product(range(modulus), repeat=3)
                                  if (s[1] - s[0]) % modulus == lags[0]
                                  and (s[2] - s[1]) % modulus == lags[1]
                                  and (s[0] - s[2]) % modulus == lags[2])
            assert bool(direct_phases) == (residual == 0)
            assert all(push(shift, uniform_on(modulus, part)) == uniform_on(modulus, part) for part in parts)
            clock_cases += 1
    return {
        "generator_pair_classifications_degrees_1_to_4": classification_cases,
        "denominator_6_rational_laws": grid_cases,
        "independent_A04_triangle_audits": triangle_cases,
        "gauge_transported_extreme_law_sections": gauge_cases,
        "clock_lag_triangle_cases_moduli_2_to_8": clock_cases,
        "S3_counterexample": {"group_order": len(group), "point_sections": 0,
                              "law_section_vertices": [["1/3", "1/3", "1/3"]]},
        "mixed_fixed_and_nonfixed_orbits": [list(x) for x in mixed_orbits],
        "joint_original_marginal": ["1/3", "2/3"],
        "ambiguous_orbit_posterior": ["1/3", "2/3"],
        "source_target_controls": "passed",
    }


def main():
    result = {
        "assignment": "SWM-X02",
        "base_commit": "7913e10",
        "status": "PROVED LOCAL / CLASSICAL finite theorem; exact finite controls passed",
        "proof_scope": "Paper proof; no Lean kernel formalization or novelty claim",
        "probe_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": core_probe(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
