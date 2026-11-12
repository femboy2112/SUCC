#!/usr/bin/env python3
"""Exact finite controls for MOTION_AND_COHERENCE.md; no numerical proof lift."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path


Quat = tuple[Q, Q, Q, Q]


def mul(p: Quat, q: Quat) -> Quat:
    a, b, c, d = p
    w, x, y, z = q
    return (a*w-b*x-c*y-d*z, a*x+b*w+c*z-d*y,
            a*y-b*z+c*w+d*x, a*z+b*y-c*x+d*w)


def conjugate(q: Quat) -> Quat:
    return q[0], -q[1], -q[2], -q[3]


def negate(q: Quat) -> Quat:
    return tuple(-x for x in q)


def act(q: Quat, v: Quat) -> Quat:
    """Unit-quaternion conjugation; this probe validates each input's norm."""
    return mul(mul(q, v), conjugate(q))


def matrix(q: Quat):
    columns = [act(q, e)[1:] for e in IMAGINARY_BASIS]
    return tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))


def mmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


def determinant(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


ONE = (Q(1), Q(0), Q(0), Q(0))
IMAGINARY_BASIS = tuple(tuple(Q(int(j == i)) for j in range(4))
                       for i in range(1, 4))
IDENTITY = tuple(tuple(Q(int(i == j)) for j in range(3)) for i in range(3))


def bracketings(labels):
    if len(labels) == 1:
        return (labels[0],)
    return tuple((left, right)
                 for split in range(1, len(labels))
                 for left in bracketings(labels[:split])
                 for right in bracketings(labels[split:]))


def rotations(tree):
    """One associator or inverse, at any subtree; leaves stay ordered."""
    if isinstance(tree, str):
        return set()
    left, right = tree
    result = set()
    if isinstance(left, tuple):
        a, b = left
        result.add((a, (b, right)))
    if isinstance(right, tuple):
        b, c = right
        result.add(((left, b), c))
    result.update((rotated, right) for rotated in rotations(left))
    result.update((left, rotated) for rotated in rotations(right))
    return result


def alpha(value):
    (a, b), c = value
    return a, (b, c)


def short_route(value):
    return alpha(alpha(value))


def long_route(value):
    left, d = value
    step1 = alpha(left), d
    a, rest = alpha(step1)
    return a, alpha(rest)


def serial(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, tuple):
        return [serial(x) for x in value]
    return value


def main():
    counts = {}

    def check(name, condition):
        counts[name] = counts.get(name, 0) + 1
        if not condition:
            raise AssertionError(name)

    units = []
    for index in range(4):
        for sign in (-1, 1):
            units.append(tuple(Q(sign if index == j else 0) for j in range(4)))
    units.extend(tuple(Q(sign, 2) for sign in signs)
                 for signs in product((-1, 1), repeat=4))
    check("24_rational_units", len(set(units)) == 24)
    q = (Q(3, 5), Q(4, 5), Q(0), Q(0))
    r = (Q(3, 5), Q(0), Q(4, 5), Q(0))
    sample = units + [q, r]
    matrices = {u: matrix(u) for u in sample}
    for u in sample:
        check("unit_norm", sum(x*x for x in u) == 1)
        check("two_sided_inverse", mul(u, conjugate(u)) == mul(conjugate(u), u) == ONE)
        check("orthogonal_action", mmul(transpose(matrices[u]), matrices[u]) == IDENTITY)
        check("orientation_preserved", determinant(matrices[u]) == 1)
        check("sign_redundancy", matrix(negate(u)) == matrices[u])
    for u, v in product(sample, repeat=2):
        check("action_composition", matrix(mul(u, v)) == mmul(matrices[u], matrices[v]))
    for u, v in product(units, repeat=2):
        check("24_unit_closure", mul(u, v) in units)
    basis = (ONE,) + IMAGINARY_BASIS
    for u, v, w in product(basis, repeat=3):
        check("basis_associativity", mul(mul(u, v), w) == mul(u, mul(v, w)))

    i, j, k = IMAGINARY_BASIS
    check("half_turn_bad_witness", mul(i, j) != mul(j, i)
          and matrix(mul(i, j)) == matrix(mul(j, i)))
    expected_qr = (Q(0), Q(-175, 625), Q(576, 625), Q(168, 625))
    expected_rq = (Q(0), Q(-175, 625), Q(0), Q(-600, 625))
    check("order_witness_qr", act(mul(q, r), i) == expected_qr)
    check("order_witness_rq", act(mul(r, q), i) == expected_rq)
    check("different_rotations", expected_qr != expected_rq
          and mul(q, r) != negate(mul(r, q)))

    catalan_expected = (1, 1, 2, 5, 14, 42, 132, 429)
    for arity, expected in enumerate(catalan_expected, 1):
        check("bracketing_counts", len(bracketings(tuple(map(str, range(arity))))) == expected)
    vertices = bracketings(tuple("ABCD"))
    edges = {frozenset((v, w)) for v in vertices for w in rotations(v)}
    check("pentagon_vertices", len(vertices) == 5)
    check("pentagon_edges", len(edges) == 5)
    for v in vertices:
        check("pentagon_degree", len(rotations(v)) == 2)
        check("pentagon_closure", rotations(v).issubset(set(vertices)))
    reached, frontier = set(), [vertices[0]]
    while frontier:
        v = frontier.pop()
        if v in reached:
            continue
        reached.add(v)
        frontier.extend(rotations(v) - reached)
    check("pentagon_connected", len(reached) == 5)
    for a, b, c, d in product(range(3), repeat=4):
        value = (((a, b), c), d)
        check("cartesian_pentagon", short_route(value) == long_route(value) == (a, (b, (c, d))))
    for scalar in (Q(-1), Q(2), Q(1, 2), Q(-3, 2)):
        check("scalar_associator_mutation", scalar**2 != scalar**3)
    check("canonical_associator_control", Q(1)**2 == Q(1)**3)

    landmarks = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    range_profiles = [tuple(sum((x-y)**2 for x, y in zip(position, landmark))
                            for landmark in landmarks)
                      for position in ((0, 0, 1), (0, 0, -1))]
    check("three_range_mirror_ambiguity", range_profiles[0] == range_profiles[1] == (1, 2, 2))

    report = {
        "scope": "Exact finite implementation and countermodel checks; universal claims use displayed proofs/classical sources.",
        "arithmetic": "Python Fraction; no floating point",
        "counts": counts,
        "total_checks": sum(counts.values()),
        "failures": [],
        "rotation_witness": {"q": serial(q), "r": serial(r),
                             "qr_on_i": serial(expected_qr), "rq_on_i": serial(expected_rq)},
        "half_turn_control": "i*j=k and j*i=-k are unequal but have equal conjugation action",
        "pentagon": {"vertices": serial(vertices), "edges": len(edges),
                     "short_path_steps": 2, "long_path_steps": 3,
                     "minus_associator_outputs": {"short": 1, "long": -1}},
        "dimension_table": [{"space": d, "translation": d,
                             "rotation": d*(d-1)//2, "rigid_motion": d*(d+1)//2}
                            for d in range(1, 6)],
        "bracketing_counts_one_to_eight_inputs": list(catalan_expected),
    }
    destination = Path(__file__).resolve().parent / "receipts" / "MOTION_REPORT.json"
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"total_checks": report["total_checks"], "failures": 0,
                      "report": str(destination)}))


if __name__ == "__main__":
    main()
