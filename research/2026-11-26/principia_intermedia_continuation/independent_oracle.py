#!/usr/bin/env python3
"""Independent exhaustive finite controls for Principia Intermedia.

Expected paths are obtained by Cartesian-product enumeration, independently of
the implementation's reachability algorithm. Exact Fraction arithmetic is used
throughout. These finite receipts calibrate the implementation; the accompanying
paper proofs, not enumeration, establish universal claims.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from observational_succ.principia_intermedia import (
    ContinuationError,
    LayeredModel,
    ObserverState,
    continuation,
    granular_crossing,
    lattice_zero,
    seam_report,
    transport_section,
)


def require(condition, detail):
    if not condition:
        raise AssertionError(detail)


NAMES = (("a0", "a1"), ("b0", "b1"), ("c0", "c1"))
VERTICES = tuple((i, name) for i, layer in enumerate(NAMES) for name in layer)
EDGE_SLOTS = tuple(
    (i, left, right)
    for i in range(len(NAMES) - 1)
    for left in NAMES[i]
    for right in NAMES[i + 1]
)


def edges_for_mask(mask):
    return tuple(
        frozenset((left, right) for k, (j, left, right) in enumerate(EDGE_SLOTS)
                  if j == i and mask & (1 << k))
        for i in range(len(NAMES) - 1)
    )


def brute_paths(edges, starts, ends, forbidden=frozenset()):
    """Enumerate full paths directly; no prefix dynamic programming."""
    return tuple(
        path for path in product(*NAMES)
        if path[0] in starts and path[-1] in ends
        and all((i, name) not in forbidden for i, name in enumerate(path))
        and all((path[i], path[i + 1]) in edges[i]
                for i in range(len(edges)))
    )


def brute_cones(edges, starts, ends, forbidden=frozenset()):
    """Expected prefix/suffix cones by enumerating every partial word."""
    forward, backward = [], []
    for stop in range(len(NAMES)):
        forward.append(frozenset(
            path[-1] for path in product(*NAMES[:stop + 1])
            if path[0] in starts
            and all((i, name) not in forbidden for i, name in enumerate(path))
            and all((path[i], path[i + 1]) in edges[i]
                    for i in range(stop))
        ))
        backward.append(frozenset(
            path[0] for path in product(*NAMES[stop:])
            if path[-1] in ends
            and all((stop + j, name) not in forbidden
                    for j, name in enumerate(path))
            and all((path[j], path[j + 1]) in edges[stop + j]
                    for j in range(len(path) - 1))
        ))
    return tuple(forward), tuple(backward)


def make_model(edges, starts, ends, source_bits=0):
    layers = tuple(
        tuple(ObserverState(name, "source-" + str((source_bits >> (2 * i + j)) & 1),
                            "comparison-target")
              for j, name in enumerate(layer))
        for i, layer in enumerate(NAMES)
    )
    return LayeredModel(layers, edges, frozenset(starts), frozenset(ends))


def compare_continuation(model, edges, starts, ends, forbidden=frozenset()):
    paths = brute_paths(edges, starts, ends, forbidden)
    expected_forward, expected_backward = brute_cones(edges, starts, ends, forbidden)
    expected_viable = tuple(frozenset(path[i] for path in paths)
                            for i in range(len(NAMES)))
    actual = continuation(model, forbidden)
    require(actual.feasible == bool(paths), "Feasibility differs from full enumeration")
    require(actual.forward == expected_forward, "Forward cone differs from prefix enumeration")
    require(actual.backward == expected_backward, "Backward cone differs from suffix enumeration")
    require(actual.viable == expected_viable, "Viable cone differs from full paths")
    if paths:
        require(actual.witness in paths, "Returned witness is not an enumerated lawful path")
        require(actual.cut_layer is None, "Successful path must not have an obstruction cut")
    else:
        require(actual.witness is None, "Empty path set has a false witness")
        require(actual.cut_layer in range(len(NAMES)), "Missing failed-model cut")
        require(not expected_forward[actual.cut_layer] & expected_backward[actual.cut_layer],
                "Claimed cut cones overlap")
    return paths


def exhaustive_finite_models():
    counts = {"anchored_graphs": 0, "seam_models": 0,
              "source_tag_cases": 0, "source_mutations_rejected": 0}
    for mask in range(1 << len(EDGE_SLOTS)):
        edges = edges_for_mask(mask)
        for start in NAMES[0]:
            for end in NAMES[-1]:
                starts, ends = frozenset((start,)), frozenset((end,))
                model = make_model(edges, starts, ends)
                original_paths = compare_continuation(model, edges, starts, ends)
                counts["anchored_graphs"] += 1
                for seam_mask in range(1 << len(VERTICES)):
                    seam = frozenset(vertex for k, vertex in enumerate(VERTICES)
                                     if seam_mask & (1 << k))
                    avoiding_paths = compare_continuation(model, edges, starts, ends, seam)
                    report = seam_report(model, seam)
                    require(report.feasible == bool(original_paths), "Seam feasibility")
                    require(report.unavoidable == (bool(original_paths) and not avoiding_paths),
                            "Non-vacuous all-path seam verdict")
                    if avoiding_paths:
                        require(report.avoiding_witness in avoiding_paths,
                                "Avoiding witness violates the independent path list")
                    else:
                        require(report.avoiding_witness is None, "False seam-avoidance witness")
                    counts["seam_models"] += 1

        # Every assignment of two possible source identities to all six states.
        # Invalid transition relations must be rejected, not silently repaired.
        for source_bits in range(1 << len(VERTICES)):
            labels = {name: (source_bits >> k) & 1
                      for k, (_, name) in enumerate(VERTICES)}
            lawful = all(labels[left] == labels[right]
                         for relation in edges for left, right in relation)
            try:
                model = make_model(edges, NAMES[0], NAMES[-1], source_bits)
            except ContinuationError:
                require(not lawful, "Lawful source-tagged graph was rejected")
                counts["source_mutations_rejected"] += 1
            else:
                require(lawful, "A source-changing edge was accepted")
                paths = compare_continuation(model, edges, NAMES[0], NAMES[-1])
                require(all(len({labels[name] for name in path}) == 1 for path in paths),
                        "An accepted path changes source identity")
            counts["source_tag_cases"] += 1
    return counts


def retained_history_controls():
    def create(histories, targets=("q", "q", "q")):
        return LayeredModel(
            tuple((ObserverState(str(i), "source", targets[i], histories[i]),)
                  for i in range(3)),
            (frozenset((("0", "1"),)), frozenset((("1", "2"),))),
            frozenset(("0",)), frozenset(("2",)),
        )

    histories = (("seed",), ("seed", "event-1"), ("seed", "event-1", "event-2"))
    require(continuation(create(histories)).witness == ("0", "1", "2"),
            "Append-only history should be admitted")
    mutations = (
        (("seed",), (), ("seed", "event-2")),
        (("seed",), ("other-seed",), ("other-seed", "event-2")),
        (("seed",), ("seed", "event-1"), ("seed",)),
    )
    for mutation in mutations:
        try:
            create(mutation)
        except ContinuationError:
            pass
        else:
            raise AssertionError("A history erasure or rewrite was accepted")
    try:
        create(histories, ("q", "different-q", "q"))
    except ContinuationError:
        pass
    else:
        raise AssertionError("A transported comparison-target mutation was accepted")
    return 5


def exhaustive_transport():
    """All triangle transports for a three-element fiber, checked by assignments."""
    count = 0
    names = ("u", "v", "w")
    for p, q, r in product(tuple(permutations(range(3))), repeat=3):
        edges = (("u", "v", p), ("v", "w", q), ("w", "u", r))
        for anchor in range(3):
            for required_w in range(3):
                expected = tuple(values for values in product(range(3), repeat=3)
                                 if values[0] == anchor and values[2] == required_w
                                 and values[1] == p[values[0]]
                                 and values[2] == q[values[1]]
                                 and values[0] == r[values[2]])
                actual = transport_section(names, edges, fiber_size=3,
                                           anchor_vertex="u", anchor_value=anchor,
                                           required={"w": required_w})
                require(actual.coherent == bool(expected), "Holonomy vs full assignment enumeration")
                if expected:
                    assignment = dict(actual.assignment)
                    require(tuple(assignment[name] for name in names) in expected,
                            "Coherent transport assignment fails its equations")
                count += 1
    return count


def scalar_holdouts():
    """Fresh rational grids; no parameters inferred from toolkit outputs."""
    grid = tuple(Fraction(n, 17) for n in (-19, -11, -2, 0, 5, 13, 23))
    scalar_count = lattice_count = 0
    for length in range(2, 6):
        for values in product(grid, repeat=length):
            if values[0] * values[-1] > 0:
                continue
            jump = max(abs(b - a) for a, b in zip(values, values[1:]))
            declared = jump + Fraction(1, 19)
            actual = granular_crossing(values, declared)
            require(actual.near_value == values[actual.near_index], "Wrong scalar witness value")
            require(abs(actual.near_value) <= declared / 2, "Granular half-jump bound")
            require(actual.near_bound == declared / 2, "Misreported near-zero radius")
            if actual.zero_index is not None:
                require(values[actual.zero_index] == 0, "False exact scalar zero")
            else:
                require(values[actual.edge_index] * values[actual.edge_index + 1] < 0,
                        "Reported seam edge does not change sign")
            if jump:
                try:
                    granular_crossing(values, jump / 2)
                except ContinuationError:
                    pass
                else:
                    raise AssertionError("A false scalar jump bound was accepted")
            scalar_count += 1

    # Sharpness and the lattice's strict inequality are exact mutations.
    for delta in (Fraction(1, 17), Fraction(7, 13), Fraction(31, 5)):
        values = (-delta / 2, delta / 2)
        actual = granular_crossing(values, delta)
        require(actual.zero_index is None and abs(actual.near_value) == delta / 2,
                "The sharp half-jump control was not preserved")
    for spacing in (Fraction(1), Fraction(2, 7)):
        for values_integer in product(range(-3, 4), repeat=4):
            values = tuple(spacing * k for k in values_integer)
            if values[0] * values[-1] > 0:
                continue
            jump = max(abs(b - a) for a, b in zip(values, values[1:]))
            if jump < 2 * spacing:
                index = lattice_zero(values, spacing, jump)
                require(values[index] == 0, "Lattice theorem reported a nonzero vertex")
                lattice_count += 1
        try:
            lattice_zero((-spacing, spacing), spacing, 2 * spacing)
        except ContinuationError:
            pass
        else:
            raise AssertionError("The sharp lattice equality mutation was accepted")
    return {"rational_scalar_paths": scalar_count, "lattice_paths": lattice_count,
            "sharp_half_jump_controls": 3, "strict_lattice_mutations": 2}


def exact_algebra_controls():
    """Countermodels whose expected result has a short paper proof."""
    checked = 0

    candidates = ({0, 1}, {1, 2}, {0, 2})
    require(all(candidates[i] & candidates[j]
                for i in range(3) for j in range(i)),
            "Pairwise source compatibility control failed")
    require(not set.intersection(*candidates), "False global-source witness")
    checked += 1

    # Finite prefixes of a noncompact refinement tower can all be feasible.
    # P_n={k in N:k>=n}: k=m meets levels <=m and fails level m+1.
    # The nonexistence of an infinite common k is a paper proof, not a finite run.
    for m in range(1, 18):
        witness = m
        require(all(witness >= n for n in range(1, m + 1)), "Finite refinement prefix")
        require(not witness >= m + 1, "False infinite refinement witness")
        checked += 1

    # Individually changing signs does not force one common null.
    f = lambda t: 2 * t - 1
    g = lambda t: 2 * t - Fraction(1, 2)
    require(f(0) < 0 < f(1) and g(0) < 0 < g(1), "Scalar signs")
    require(f(Fraction(1, 2)) == 0 and g(Fraction(1, 2)) != 0,
            "Distinct scalar roots")
    require(g(Fraction(1, 4)) == 0 and f(Fraction(1, 4)) != 0,
            "Distinct scalar roots")
    checked += 1

    # A finite derivative tower can have individual roots but no common root.
    p = lambda t: (t - Fraction(1, 4)) * (t - Fraction(3, 4))
    dp = lambda t: 2 * t - 1
    for root in (Fraction(1, 4), Fraction(3, 4)):
        require(p(root) == 0 and dp(root) != 0, "Simple polynomial roots")
    require(dp(Fraction(1, 2)) == 0 and p(Fraction(1, 2)) != 0,
            "A derivative root is not a joint jet null")
    checked += 1

    # Opposite vector endpoints do not force the vector origin.
    # First component is zero only at 1/2, where the second is one.
    vector = lambda t: (2 * t - 1, 4 * t * (1 - t))
    require(vector(0) == (-1, 0) and vector(1) == (1, 0),
            "Antipodal endpoints")
    require(vector(Fraction(1, 2)) == (0, 1), "Projection vs full null")
    checked += 1

    # One negative edge in a real one-dimensional loop has holonomy -1.
    for x in (Fraction(-3, 2), Fraction(0), Fraction(7, 3)):
        require(((-1) * x == x) == (x == 0), "Holonomy fixed space")
    checked += 1

    # Arithmetic capacity: strict inequality and nonzero lattice are essential.
    for modulus in range(1, 18):
        for integer in range(-51, 52):
            impossible = (integer != 0 and integer % modulus == 0
                          and abs(integer) < modulus)
            require(not impossible, "Integer-capacity contradiction")
            checked += 1
    require(0 % 7 == 0 and abs(0) < 7, "Zero witness must be excluded")
    require(7 % 7 == 0 and abs(7) <= 7, "Strict capacity bound is necessary")
    require(0 < Fraction(1, 2) < 1, "Rational normalization control")
    checked += 3

    # Exact Gaussian-rational evaluation of the RH-symmetric quartic control.
    # z^4 + (15/8) z^2 + 289/256 at z = 1/4 + i is zero.
    def mul(a, b):
        return (a[0] * b[0] - a[1] * b[1],
                a[0] * b[1] + a[1] * b[0])

    z = (Fraction(1, 4), Fraction(1))
    z2 = mul(z, z)
    z4 = mul(z2, z2)
    require((z4[0] + Fraction(15, 8) * z2[0] + Fraction(289, 256),
             z4[1] + Fraction(15, 8) * z2[1]) == (0, 0),
            "Off-axis symmetric polynomial zero")
    for numerator in range(-23, 24):
        t = Fraction(numerator, 7)
        value = (Fraction(17, 16) - t * t) ** 2 + Fraction(1, 4) * t * t
        require(value > 0, "Critical-line polynomial positivity")
        checked += 1
    checked += 1
    return checked


def main():
    result = {"finite_models": exhaustive_finite_models(),
              "transport_models": exhaustive_transport(),
              "retained_history_controls": retained_history_controls(),
              "scalar_holdouts": scalar_holdouts(),
              "algebra_controls": exact_algebra_controls(),
              "status": "PASS", "arithmetic": "exact Fraction/integer",
              "scope": "Finite controls only; universal claims use paper proofs."}
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
