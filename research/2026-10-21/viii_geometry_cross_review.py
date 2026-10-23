"""Independent rank-two G4 oracle; does not import the geometry implementation.

Run: python research/2026-10-21/viii_geometry_cross_review.py DOSSIER OUTPUT
All geometry and counts are exact. The finite receipt supports, rather than
replaces, the separately reconstructed universal cell argument.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
import json
from math import ceil
from pathlib import Path
import sys


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull(points):
    result = []
    for ordered in (sorted(set(points)), sorted(set(points), reverse=True)):
        half = []
        for point in ordered:
            while len(half) >= 2 and cross(half[-2], half[-1], point) <= 0:
                half.pop()
            half.append(point)
        result += half[:-1]
    return result


def check(C):
    sums = tuple(sum(row[j] for row in C) for j in (0, 1))
    halfspaces = [(a, b, F(0)) for a, b in C] + [(-sums[0], -sums[1], F(-1))]
    points = []
    for (a, b, d), (e, f, g) in combinations(halfspaces, 2):
        determinant = a * f - b * e
        if determinant:
            u, v = F(d * f - b * g, determinant), F(a * g - d * e, determinant)
            if all(a0 * u + b0 * v >= d0 for a0, b0, d0 in halfspaces):
                points.append((u, v))
    vertices = hull(points)
    area = abs(sum(vertices[i][0] * vertices[(i + 1) % len(vertices)][1]
                   - vertices[i][1] * vertices[(i + 1) % len(vertices)][0]
                   for i in range(len(vertices)))) / 2
    center = tuple(sum(v[j] for v in vertices) / len(vertices) for j in (0, 1))
    z = [a * center[0] + b * center[1] for a, b in C]
    assert min(z) > 0 and sum(z) < 1
    beta = max([F(abs(a) + abs(b), 2) / zi for (a, b), zi in zip(C, z)]
               + [F(abs(sums[0]) + abs(sums[1]), 2) / (1 - sum(z))])
    inverse_bounds = []
    for (a, b), (e, f) in combinations(C, 2):
        determinant = a * f - b * e
        if determinant:
            inverse_bounds.append((max(abs(F(f, determinant)), abs(F(b, determinant))),
                                   max(abs(F(e, determinant)), abs(F(a, determinant)))))
    b1, b2 = min(inverse_bounds, key=lambda t: t[0] * t[1])
    maximum = 160
    census = Counter()
    for u in range(-ceil(maximum * b1), ceil(maximum * b1) + 1):
        for v in range(-ceil(maximum * b2), ceil(maximum * b2) + 1):
            xs = [a * u + b * v for a, b in C]
            energy = sum(xs)
            if min(xs) > 0 and energy <= maximum:
                census[energy] += 1
    total = 0
    for X in range(maximum + 1):
        total += census[X]
        assert area * max(F(0), X - beta) ** 2 <= total <= area * (X + beta) ** 2
    return {"basis": C, "coordinate_polygon_area_equals_aV": str(area),
            "interior_center": list(map(str, z)), "beta": str(beta),
            "integer_cutoffs_checked": maximum + 1, "count_at_160": total}


def main(dossier, output):
    cases = [((1, 0), (0, 1)), ((1, 0), (0, 1), (1, 1)),
             ((1, 0), (-1, 3), (0, 1)), ((2, -1), (1, 2), (1, 1)),
             ((4, 1), (-2, 3), (3, -1)), ((2, 2), (0, 3), (1, -1))]
    cases += [((1, 0), (M - 1, -1), (0, 1)) for M in (3, 7)]
    record = {
        "reviewer_lane": "viii_clocks",
        "method": "Independent exact rational halfspace-intersection convex hull and integer-coordinate census; no target code imported",
        "target_dossier_sha256": sha256(Path(dossier).read_bytes()).hexdigest(),
        "G4_cases": [check(C) for C in cases],
        "S1_independent_proof": "Remainder equals sum_j integral_0^(j/N) t^k/(1-t) dt, enclosed using 1<=1/(1-t)<=1/(1-rho).",
        "S2_precision_issue": "Asymptotic sentence must state N tends to infinity; constant sequence (2,1) otherwise contradicts literal implication.",
        "S3_verdict": "Exact population shift and positive summation bounds reconstruct correctly.",
    }
    Path(output).write_text(json.dumps(record, indent=2) + "\n")
    print("PASS: 8 rank-two sections, 161 exact integer cutoffs each")


if __name__ == "__main__":
    main(*sys.argv[1:])
