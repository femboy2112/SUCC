#!/usr/bin/env python3
"""Independent exact X10 audit/synthesis; imports no cohort implementation.

Run from the repository root. Fractions, source-path expansion, function-algebra
row reduction, pair orbits and Fourier convolution are independent witnesses.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path


def partitions(n):
    """Restricted growth words, each set partition once."""
    if n == 0:
        yield ()
        return
    def extend(prefix):
        if len(prefix) == n:
            yield prefix
        else:
            for value in range(max(prefix) + 2):
                yield from extend(prefix + (value,))
    yield from extend((0,))


def basis_add(basis, vector):
    """Add a rational function to a reduced echelon spanning family."""
    row = list(map(Q, vector))
    for pivot in sorted(basis):
        factor = row[pivot]
        if factor:
            row = [x - factor*y for x, y in zip(row, basis[pivot])]
    if not any(row):
        return False
    pivot = next(i for i, value in enumerate(row) if value)
    coefficient = row[pivot]
    row = [x / coefficient for x in row]
    for p, old in list(basis.items()):
        factor = old[pivot]
        if factor:
            basis[p] = tuple(x - factor*y for x, y in zip(old, row))
    basis[pivot] = tuple(row)
    return True


def generated_observable_algebra(report, actions):
    """Smallest rational unital algebra invariant under each pullback."""
    n = len(report)
    basis = {}
    for symbol in set(report):
        basis_add(basis, tuple(int(value == symbol) for value in report))
    while True:
        old_dimension = len(basis)
        vectors = list(basis.values())
        for vector in vectors:
            for action in actions:
                basis_add(basis, tuple(vector[action[s]] for s in range(n)))
        vectors = list(basis.values())
        for a, b in product(vectors, repeat=2):
            basis_add(basis, tuple(x*y for x, y in zip(a, b)))
        if len(basis) == old_dimension:
            return tuple(basis[p] for p in sorted(basis))


def word_orbit_relation(report, actions):
    """Pair BFS proves behavioral equality, without partition refinement."""
    n = len(report)
    relation = set()
    for start in product(range(n), repeat=2):
        queue, seen, compatible = [start], {start}, True
        while queue:
            s, t = queue.pop()
            if report[s] != report[t]:
                compatible = False
                break
            for action in actions:
                pair = (action[s], action[t])
                if pair not in seen:
                    seen.add(pair)
                    queue.append(pair)
        if compatible:
            relation.add(start)
    return relation


def partition_relation(report):
    return {(s, t) for s, t in product(range(len(report)), repeat=2)
            if report[s] == report[t]}


def algebra_audit():
    cases = universal_checks = 0
    for n in range(1, 5):
        maps = list(product(range(n), repeat=n))
        families = [(a,) for a in maps]
        if n <= 3:
            families += list(product(maps, repeat=2))
        for report in partitions(n):
            initial_relation = partition_relation(report)
            for actions in families:
                vectors = generated_observable_algebra(report, actions)
                relation = word_orbit_relation(report, actions)
                kernel = {(s, t) for s, t in product(range(n), repeat=2)
                          if all(v[s] == v[t] for v in vectors)}
                assert relation == kernel
                classes = {tuple(v[s] for v in vectors) for s in range(n)}
                assert len(vectors) == len(classes)
                for candidate in partitions(n):
                    candidate_relation = partition_relation(candidate)
                    stable = all((a[s], a[t]) in candidate_relation
                                 for a in actions for s, t in candidate_relation)
                    if stable and candidate_relation <= initial_relation:
                        assert candidate_relation <= relation
                        universal_checks += 1
                cases += 1
    # An invariant linear span can separate all four points yet omit products.
    bits = tuple(product((0, 1), repeat=2))
    report = tuple(a for a, b in bits)
    swap = tuple(bits.index((b, a)) for a, b in bits)
    linear = {}
    for v in ((1,)*4, report, tuple(v[1] for v in bits)):
        basis_add(linear, v)
    linear_dimension = len(linear)
    assert linear_dimension == 3
    assert basis_add(linear, tuple(a*b for a, b in bits))
    full = generated_observable_algebra(report, (swap,))
    assert len(full) == 4
    return {"finite_source_cases": cases, "universal_factor_checks": universal_checks,
            "false_linear_span_bridge": {"linear_dimension": 3, "algebra_dimension": 4,
                                         "source": bits, "report": report, "swap": swap}}


def observed_paths(kernel, report, initial, horizon):
    law = {(s, (report[s],)): mass for s, mass in enumerate(initial) if mass}
    for _ in range(horizon):
        next_law = defaultdict(Q)
        for (s, history), mass in law.items():
            for t, weight in enumerate(kernel[s]):
                if weight:
                    next_law[t, history + (report[t],)] += mass * weight
        law = next_law
    visible = defaultdict(Q)
    for (_, history), mass in law.items():
        visible[history] += mass
    return visible


def total_variation(a, b):
    return sum((abs(a.get(x, Q(0)) - b.get(x, Q(0)))
                for x in a.keys() | b.keys()), Q(0))/2


def stochastic_audit():
    report = (0, 0, 1)
    rows = ((Q(1), Q(0), Q(0)), (Q(1,2), Q(1,2), Q(0)),
            (Q(0), Q(1,2), Q(1,2)), (Q(0), Q(0), Q(1)))
    coarse_rows = ((Q(1), Q(0)), (Q(1,2), Q(1,2)), (Q(0), Q(1)))
    checks = zero_defect_cases = 0
    for kernel in product(rows, repeat=3):
        projected = [(row[0]+row[1], row[2]) for row in kernel]
        for candidate in product(coarse_rows, repeat=2):
            delta = max(sum(abs(a-b) for a, b in zip(projected[s], candidate[report[s]]))/2
                        for s in range(3))
            if delta == 0:
                zero_defect_cases += 1
            for start in range(3):
                initial = tuple(Q(int(s == start)) for s in range(3))
                coarse_initial = tuple(Q(int(o == report[start])) for o in range(2))
                for n in range(4):
                    actual = observed_paths(kernel, report, initial, n)
                    approximate = observed_paths(candidate, (0,1), coarse_initial, n)
                    error = total_variation(actual, approximate)
                    assert error <= min(Q(1), n*delta)
                    # A slightly stronger independent first-failure coupling bound.
                    assert error <= 1 - (1-delta)**n
                    checks += 1
    assert zero_defect_cases > 0
    return {"source_kernels": len(rows)**3, "candidate_kernels": len(coarse_rows)**2,
            "point_initial_laws": 3, "horizons": [0,1,2,3],
            "path_law_checks": checks, "zero_defect_kernel_pairs": zero_defect_cases}


def les_convolution(n):
    k, ell = (n, 1), (n-1, 1)
    a, b = (1, -n), (1, -(n-1))
    assert sum(x*y for x, y in zip(k, a)) == 0
    assert sum(x*y for x, y in zip(ell, b)) == 0
    velocity = {k: tuple(Q(x,2) for x in a), (-k[0],-k[1]): tuple(Q(x,2) for x in a),
                ell: tuple(Q(x,2) for x in b), (-ell[0],-ell[1]): tuple(Q(x,2) for x in b)}
    assert all(sum(x*x for x in mode) > 1 for mode in velocity)
    stress = defaultdict(lambda: [Q(0)]*4)
    for (p,u), (q,v) in product(velocity.items(), repeat=2):
        mode = tuple(x+y for x,y in zip(p,q))
        if sum(x*x for x in mode) <= 1:
            for i,j in product(range(2), repeat=2):
                stress[mode][2*i+j] += u[i]*v[j]
    assert set(stress) == {(0,0),(1,0),(-1,0)}
    sine_force = {}
    for mode, tensor in stress.items():
        norm = sum(x*x for x in mode)
        if not norm:
            continue
        imaginary_divergence = [sum(tensor[2*i+j]*mode[j] for j in range(2)) for i in range(2)]
        longitudinal = sum(x*y for x,y in zip(imaginary_divergence, mode))/norm
        leray = tuple(imaginary_divergence[i] - longitudinal*mode[i] for i in range(2))
        sine_force[mode] = tuple(-2*x for x in leray)
    assert sine_force[(1,0)] == (0, Q(2*n-1, 2))
    assert sine_force[(-1,0)] == (0, -Q(2*n-1, 2))
    return sine_force[(1,0)]


def delay_audit():
    cases = pairs = 0
    for n in range(1,5):
        for action in product(range(n), repeat=n):
            for report in product((0,1), repeat=n):
                for start in combinations(range(n), 2):
                    s,t = start
                    seen, discrepancy_time, tick = set(), None, 0
                    while (s,t) not in seen:
                        seen.add((s,t))
                        if report[s] != report[t]:
                            discrepancy_time = tick
                            break
                        s,t = action[s], action[t]
                        tick += 1
                    assert discrepancy_time is None or discrepancy_time < n-1
                    pairs += 1
                cases += 1
    sharp = []
    for n in range(2,17):
        report = tuple(int(s == n-1) for s in range(n))
        a = tuple(min(s+1,n-1) for s in range(n))
        s,t = 0,1
        tick = 0
        while report[s] == report[t]:
            s,t = a[s],a[t]
            tick += 1
        assert tick == n-2
        sharp.append({"states": n, "first_distinguishing_time": tick})
    return {"source_tables": cases, "independent_pair_orbits": pairs,
            "sharp_chain_controls": sharp}


def jet_controls():
    rows = []
    for m in range(12):
        # Polynomial g=x^(m+1); all supplied jets vanish, next jet is nonzero.
        coefficients = [0]*(m+1) + [1]
        jets = tuple(factorial(j)*coefficients[j] for j in range(m+1))
        next_jet = factorial(m+1)*coefficients[m+1]
        assert all(value == 0 for value in jets)
        assert next_jet != 0
        translated_value = sum(coefficients)
        assert translated_value == 1
        rows.append({"highest_reported_jet": m, "reported_jets": jets,
                     "missing_jet": next_jet, "value_after_unit_translation": translated_value})
    # Positive control: degree <= d jet vector obeys xdot=(x1,...,xd,0).
    positive_checks = 0
    for d in range(7):
        coefficients = tuple(Q(j-2, j+1) for j in range(d+1))
        jet = tuple(factorial(j)*coefficients[j] for j in range(d+1))
        for t in (Q(0),Q(1,3),Q(1),Q(-2)):
            translated = tuple(sum(coefficients[k]*comb(k,j)*t**(k-j) for k in range(j,d+1))
                               for j in range(d+1))
            expected = tuple(sum(jet[j+k]*t**k/factorial(k) for k in range(d-j+1))
                             for j in range(d+1))
            assert tuple(factorial(j)*translated[j] for j in range(d+1)) == expected
            positive_checks += 1
    return {"unbounded_degree_counterexamples": rows, "bounded_degree_exact_flow_checks": positive_checks}


def run():
    result = {"assignment": "X10", "status": "PROVED_LOCAL_PAPER_AND_EXACT_CONTROLS",
              "independence": "No A or D implementation imported; rational algebra, pair orbits, path expansion and Fourier convolution.",
              "base_commit": "e49dc2f", "academic_novelty": "UNVERIFIED", "kernel_formalization": "NOT_CLAIMED"}
    result["algebra_repair"] = algebra_audit()
    result["D27_path_review"] = stochastic_audit()
    result["D30_fourier_review"] = {"frequencies": list(range(2,102)),
                                   "forces": {str(n): les_convolution(n) for n in range(2,102)}}
    result["D32_delay_review"] = delay_audit()
    result["finite_jet_hierarchy"] = jet_controls()
    result["probe_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    encoded = json.dumps(run(), indent=2, default=lambda x: str(x) if isinstance(x,Q) else x) + "\n"
    if args.output:
        args.output.write_text(encoded)
        print(f"X10 exact probe passed; receipt: {args.output}")
    else:
        print(encoded)
