#!/usr/bin/env python3
"""Direct infinite-lattice BFS oracle, independent of quotient potentials.

This bounded audit regenerates arithmetic predicates and steps directly.
It confirms completed components for the declared finite benchmark inputs;
the general finite-to-infinite theorem is proved in the research dossier.
No potential constructor, component labels or source helpers are imported.
"""
from collections import Counter, deque
from math import isqrt, prod
import json


def rational_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def gaussian_prime(x, y):
    if x*y:
        return rational_prime(x*x+y*y)
    n = abs(x or y)
    return n % 4 == 3 and rational_prime(n)


def audit(primes):
    period = prod(primes)
    steps = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if x or y]

    def allowed(z):
        x, y = z
        return all((x*x+y*y) % p for p in primes)

    residues = {(x, y) for x in range(period) for y in range(period) if allowed((x, y))}

    def explore(root, membership, cap):
        reached = {root}
        queue = deque([root])
        while queue:
            x, y = queue.popleft()
            for dx, dy in steps:
                z = (x+dx, y+dy)
                if membership(z) and z not in reached:
                    reached.add(z)
                    if len(reached) > cap:
                        raise RuntimeError("Independent lift audit reached its point cap; unresolved")
                    queue.append(z)
        return reached

    unvisited = set(residues)
    histogram = Counter()
    while unvisited:
        root = min(unvisited)
        points = explore(root, allowed, len(residues))
        reduced = {(x % period, y % period) for x, y in points}
        if len(reduced) != len(points):
            raise ArithmeticError("A completed finite component repeated a residue")
        unvisited.difference_update(reduced)
        histogram[len(points)] += 1

    bound = max(primes)
    exceptions = {(x, y) for x in range(-bound, bound+1) for y in range(-bound, bound+1)
                  if gaussian_prime(x, y) and not allowed((x, y))}
    remaining = set(exceptions)
    clusters = []
    while remaining:
        root = min(remaining)
        points = explore(root, lambda z: z in exceptions or allowed(z),
                         len(exceptions) + len(exceptions)*len(steps)*len(residues))
        clusters.append(len(points))
        remaining.difference_update(points)
    maximum = max(max(histogram, default=0), max(clusters, default=0))
    return {"rational_primes": list(primes), "step_squared": 2, "period": period,
            "survivors": len(residues), "component_size_histogram": dict(sorted(histogram.items())),
            "periodic_maximum": max(histogram, default=0), "exception_count": len(exceptions),
            "exception_cluster_sizes": sorted(clusters), "enlarged_maximum": maximum,
            "all_direct_component_queues_exhausted": True}


if __name__ == "__main__":
    results = [audit((2, 5, 13)), audit((2, 3, 5, 13))]
    assert results[0]["enlarged_maximum"] == 580
    assert results[1]["enlarged_maximum"] == 104
    print(json.dumps({"status": "INDEPENDENT_DIRECT_LATTICE_AUDIT", "cases": results,
                      "uses_quotient_potentials": False}, indent=2, sort_keys=True))
