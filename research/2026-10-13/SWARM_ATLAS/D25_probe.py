"""Bounded exact receipts for SWM-D25; finite checks do not prove all widths."""
from __future__ import annotations

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from observational_succ.logistic_observer_tree import symbolic_path, tent
from observational_succ.misiurewicz_phase_quotient import (
    ALPHA, BOUNDARIES, CRITICAL, FIXED, LOW, MAXIMUM, ONE,
    classify_actual_cell, f, isolate_alpha, markov_adjacency,
)


def block_graph(adjacency, width):
    words = tuple(w for w in product(range(len(adjacency)), repeat=width)
                  if all(adjacency[a][b] for a, b in zip(w, w[1:])))
    edges = tuple((i, j) for i, u in enumerate(words)
                  for j, v in enumerate(words)
                  if u[1:] == v[:-1] and adjacency[u[-1]][v[-1]])
    return words, edges


def partitions(size):
    """Restricted-growth strings: enumerate each set partition exactly once."""
    def extend(prefix):
        if len(prefix) == size:
            yield prefix
            return
        for label in range(max(prefix) + 2):
            yield from extend(prefix + (label,))
    yield from extend((0,))


def induced_map(labels, edges):
    result = {}
    for i, j in edges:
        source, target = labels[i], labels[j]
        if source in result and result[source] != target:
            return None
        result[source] = target
    return result


def graph_period(size, edges):
    outgoing = {i: [] for i in range(size)}
    for i, j in edges:
        outgoing[i].append(j)
    for start in range(size):
        seen = {start}
        frontier = [start]
        while frontier:
            for target in outgoing[frontier.pop()]:
                if target not in seen:
                    seen.add(target)
                    frontier.append(target)
        assert len(seen) == size
    distances = {0: 0}
    frontier = [0]
    while frontier:
        i = frontier.pop(0)
        for j in outgoing[i]:
            if j not in distances:
                distances[j] = distances[i] + 1
                frontier.append(j)
    period = 0
    for i, j in edges:
        period = gcd(period, abs(distances[i] + 1 - distances[j]))
    return period


def audit(adjacency, period):
    result = []
    for width in (1, 2, 3):
        words, edges = block_graph(adjacency, width)
        assert graph_period(len(words), edges) == period
        total = 0
        lawful = []
        for labels in partitions(len(words)):
            total += 1
            transition = induced_map(labels, edges)
            if transition is not None:
                lawful.append((labels, transition))
        expected = {(0,) * len(words)}
        if period == 2:
            expected.add(tuple(int(w[0] == 2) for w in words))
        assert {labels for labels, _ in lawful} == expected
        result.append({"width": width, "word_count": len(words),
                       "partitions_examined": total, "period": period,
                       "lawful_factors": [{"partition": labels,
                                            "transition": transition}
                                           for labels, transition in lawful]})
    return result


def independent_multiply(left, right):
    """Ordinary polynomial convolution then monic long division, over Q."""
    coefficients = [F(0)] * 5
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            coefficients[i+j] += a*b
    while len(coefficients) > 3:
        top = coefficients.pop()
        offset = len(coefficients) - 3
        for j, coefficient in enumerate((8, 4, 2)):
            coefficients[offset+j] += coefficient*top
    return tuple(coefficients)


def independent_forward(x):
    complement = tuple((F(1) if i == 0 else F(0)) - a
                       for i, a in enumerate(x))
    return independent_multiply((F(0), F(1), F(0)),
                                independent_multiply(x, complement))


def exact_tent_cycle(initial):
    """A closed rational orbit certifies all future boundary avoidance."""
    orbit = []
    state = initial
    while state not in orbit:
        assert state not in (F(0), F(1, 2), F(1))
        assert len(orbit) < 100
        orbit.append(state)
        state = tent(state)
    return {"states_until_repeat": list(map(str, orbit)),
            "repeat_index": orbit.index(state),
            "all_future_boundary_avoidance_certified": True}


def main():
    adjacency = markov_adjacency()
    exact_orbit = [CRITICAL]
    for _ in range(4):
        exact_orbit.append(f(exact_orbit[-1]))
    assert tuple(exact_orbit) == (CRITICAL, MAXIMUM, LOW, FIXED, FIXED)
    independent = [CRITICAL.coeffs]
    for _ in range(4):
        independent.append(independent_forward(independent[-1]))
    assert independent == [x.coeffs for x in exact_orbit]
    assert f(FIXED) == FIXED
    binary_boundary_failures = [bit != 1-bit for bit in (0, 1)]
    assert all(binary_boundary_failures)
    # Boundary-only sink reports commute on the whole exact postcritical orbit.
    assert all(x in BOUNDARIES and f(x) in BOUNDARIES for x in BOUNDARIES)

    left, right = F(2, 5), F(3, 5)
    from observational_succ.misiurewicz_phase_quotient import CubicElement
    x, y = CubicElement.coerce(left), CubicElement.coerce(right)
    assert classify_actual_cell(x) == 0 and classify_actual_cell(y) == 1
    assert f(x) == f(y) == ALPHA * F(6, 25)
    assert classify_actual_cell(f(x)) == 2

    tent_sources = (F(1, 33), F(7, 33))
    before = tuple(symbolic_path(x, 2) for x in tent_sources)
    after = tuple(symbolic_path(tent(x), 2) for x in tent_sources)
    assert before == ((0, 0), (0, 0))
    assert after == ((0, 0), (0, 1))

    # Synthetic edge mutation, explicitly not a source-derived logistic graph.
    mutant = ((0, 0, 1), (0, 0, 1), (1, 1, 1))
    mutant_words, mutant_edges = block_graph(mutant, 1)
    assert graph_period(len(mutant_words), mutant_edges) == 1
    mutant_lawful = [p for p in partitions(3)
                     if induced_map(p, mutant_edges) is not None]
    assert mutant_lawful == [(0, 0, 0)]

    source_paths = ("observational_succ/logistic_observer_tree.py",
                    "observational_succ/chaos_source_quotient.py",
                    "observational_succ/misiurewicz_phase_quotient.py")
    output = {
        "claim_id": "SWM-D25",
        "source_parent": "5eb09e7cba36ec01b8f9d6834b78b5766fd93935",
        "proof_status": "CLASSICAL / PROVED LOCAL; finite receipts are calibration",
        "source_sha256": {p: sha256((ROOT/p).read_bytes()).hexdigest()
                          for p in source_paths},
        "alpha_rational_isolator": list(map(str, isolate_alpha())),
        "postcritical_orbit_independent_polynomial_replay":
            [list(map(str, value)) for value in independent],
        "misiurewicz_all_partitions": audit(adjacency, 2),
        "r4_binary_all_partitions": audit(((1, 1), (1, 1)), 1),
        "fixed_boundary": {"state": FIXED.as_strings(),
                           "forward_equals_state": True,
                           "binary_flip_fails_for_both_labels": binary_boundary_failures,
                           "boundary_orbit_sink_commutes": True},
        "actual_source_merge": {"originals": list(map(str, (left, right))),
                                "original_cells": [0, 1],
                                "same_first_image": f(x).as_strings(),
                                "image_cell": 2,
                                "all_future_boundary_avoidance_certified": False},
        "r4_deterministic_window_refutation": {
            "tent_coordinate_sources": list(map(str, tent_sources)),
            "width": 2, "initial_reports": before, "successor_reports": after,
            "exact_closed_orbits": [exact_tent_cycle(x) for x in tent_sources]},
        "synthetic_C_self_loop_mutation": {
            "source_is_actual_logistic": False, "period": 1,
            "lawful_partitions": mutant_lawful},
        "natural_acim_identified": False,
        "physical_source_authenticated": False,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
