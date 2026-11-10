"""Exact rational oracle: no trigonometric floating point or source extrapolation."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def partition_matrix(points, weights, m, theta):
    """Conditional expectation matrix at one origin, including repeated points."""
    n = len(points)
    cells = [int(m * ((x - theta) % 1)) for x in points]
    mass = {}
    for c, w in zip(cells, weights):
        mass[c] = mass.get(c, F(0)) + w
    return [[weights[j] / mass[cells[i]] if cells[i] == cells[j] else F(0)
             for j in range(n)] for i in range(n)]


def averaged_matrix(points, weights, m):
    """Integrate exactly over every open origin segment; endpoints have measure zero."""
    if m < 1 or not points or len(points) != len(weights):
        raise ValueError("nonempty matched arrays and positive integer m required")
    if any(w <= 0 for w in weights) or sum(weights) != 1:
        raise ValueError("positive normalized weights required")
    if any(not 0 <= x < 1 for x in points):
        raise ValueError("canonical circle representatives required")
    length = F(1, m)
    cuts = sorted({F(0), length, *(x % length for x in points)})
    n = len(points)
    result = [[F(0) for _ in points] for _ in points]
    for left, right in zip(cuts, cuts[1:]):
        matrix = partition_matrix(points, weights, m, (left + right) / 2)
        weight = m * (right - left)
        for i in range(n):
            for j in range(n):
                result[i][j] += weight * matrix[i][j]
    return result


def mean_product_from_cells(points, weights, m, a, b):
    """Independent direct scalar conditional means, not the matrix implementation."""
    length = F(1, m)
    cuts = sorted({F(0), length, *(x % length for x in points)})
    total = F(0)
    for left, right in zip(cuts, cuts[1:]):
        theta = (left + right) / 2
        groups = {}
        for x, w, av, bv in zip(points, weights, a, b):
            cell = int(m * ((x - theta) % 1))
            if cell not in groups:
                groups[cell] = [F(0), F(0), F(0)]
            groups[cell][0] += w
            groups[cell][1] += w * av
            groups[cell][2] += w * bv
        total += m * (right - left) * sum(sa * sb / mass
                                              for mass, sa, sb in groups.values())
    return total


def circle_discrepancy(points, weights):
    """Exact sup over circular intervals, allowing one-sided atomic endpoints."""
    masses = {}
    for x, w in zip(points, weights):
        masses[x] = masses.get(x, F(0)) + w
    cumulative = F(0)
    levels = [F(0)]
    for x in sorted(masses):
        levels.append(cumulative - x)
        cumulative += masses[x]
        levels.append(cumulative - x)
    return max(levels) - min(levels)


def cyclic_product(a, b):
    n = len(a)
    result = [F(0)] * n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[(i + j) % n] += x * y
    return result


def check_uniform_grid(n, m, h):
    """Independent finite spectral formula in Q[X]/(X^n-1)."""
    assert n % m == 0
    k = n // m
    points, weights = [F(i, n) for i in range(n)], [F(1, n)] * n
    matrix = averaged_matrix(points, weights, m)
    for i in range(n):
        for j in range(n):
            d = (j - i) % n
            expected = F(max(0, k - d) + max(0, k - (n - d)), k * k)
            assert matrix[i][j] == expected
    # An asymmetric bounded rational complement prevents a constant-only check.
    b = [F((i * i + 3 * i + 1) % 11 - 5, 5) for i in range(n)]
    response, weyl, multiplier = [F(0)] * n, [F(0)] * n, [F(0)] * n
    for i in range(n):
        weyl[(h * i) % n] += weights[i] * b[i]
        for j in range(n):
            response[(h * j) % n] += weights[i] * b[i] * matrix[i][j]
    for r in range(k):
        for s in range(k):
            multiplier[(h * (r - s)) % n] += F(1, k * k)
    assert response == cyclic_product(multiplier, weyl)
    return n * n + n


def run():
    exact_checks = 0
    cases = 0
    for n in (4, 6, 8, 12, 16, 24):
        for m in range(1, n + 1):
            if n % m:
                continue
            for h in (1, 3, n):
                exact_checks += check_uniform_grid(n, m, h)
                cases += 1
    weighted = [
        ([F(0), F(1, 8), F(1, 2), F(3, 4)], [F(1, 10), F(2, 10), F(3, 10), F(4, 10)]),
        ([F(0), F(0), F(1, 3), F(2, 3)], [F(1, 7), F(2, 7), F(1, 7), F(3, 7)]),
        ([F(1, 11), F(4, 11), F(7, 11)], [F(1, 3)] * 3),
    ]
    for points, weights in weighted:
        n = len(points)
        a = [F((-1) ** i * (i + 1), n) for i in range(n)]
        b = [F((3 * i + 1) % 5 - 2, 2) for i in range(n)]
        for m in (1, 2, 3, 4, 7, 16, 65):
            matrix = averaged_matrix(points, weights, m)
            assert all(sum(row) == 1 for row in matrix)
            assert all(weights[i] * matrix[i][j] == weights[j] * matrix[j][i]
                       for i in range(n) for j in range(n))
            direct = mean_product_from_cells(points, weights, m, a, b)
            pair = sum(weights[i] * b[i] * matrix[i][j] * a[j]
                       for i in range(n) for j in range(n))
            assert direct == pair
            exact_checks += n + n * n + 1
            cases += 1
    # Atomic discrepancy formula and exact one-origin versus average failure.
    assert circle_discrepancy([F(i, 12) for i in range(12)], [F(1, 12)] * 12) == F(1, 12)
    points, weights = [F(0), F(1, 4), F(1, 2), F(3, 4)], [F(1, 4)] * 4
    a, b = [F(1), F(0), F(-1), F(0)], [F(1), F(1), F(-1), F(-1)]
    avg = mean_product_from_cells(points, weights, 2, a, b)
    matrix = partition_matrix(points, weights, 2, F(0))
    fixed = sum(weights[i] * b[i] * matrix[i][j] * a[j]
                for i in range(4) for j in range(4))
    assert avg == F(1, 4) and fixed == F(1, 2)
    exact_checks += 3
    return {"status": "PASS", "arithmetic": "fractions.Fraction; formal Q[X]/(X^n-1)",
            "cases": cases, "exact_assertions": exact_checks,
            "fixed_origin_counterexample": {"fixed": str(fixed), "averaged": str(avg)},
            "boundaries": ["No finite test proves the continuum discrepancy bound.",
                           "No original-zero asymptotic cancellation asserted."],
            "oracle_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")
