"""Exact, standalone controls for the weighted finite-window BBP paper. Python stdlib."""
from fractions import Fraction as Q
from itertools import permutations, product
import json
from math import isqrt


def four_pole(n):
    return sum(Q(coefficient, 8 * n + shift) for coefficient, shift in
               ((4, -7), (-2, -4), (-1, -3), (-1, -2)))


def determinant(matrix):
    """Leibniz expansion for independent small-matrix controls (sizes at most 4)."""
    value = Q(0)
    for perm in permutations(range(len(matrix))):
        inversions = sum(i < j and perm[i] > perm[j]
                         for i in range(len(perm)) for j in range(len(perm)))
        term = Q((-1) ** inversions)
        for row, col in enumerate(perm):
            term *= matrix[row][col]
        value += term
    return value


def solve(matrix, rhs):
    denominator = determinant(matrix)
    assert denominator
    coefficients = []
    for replaced in range(len(rhs)):
        copy = [[rhs[i] if j == replaced else a for j, a in enumerate(row)]
                for i, row in enumerate(matrix)]
        coefficients.append(determinant(copy) / denominator)
    return coefficients


def block(moments, size, offset=0):
    return [[moments[offset + i + j] for j in range(size)] for i in range(size)]


def positive_definite(moments, size):
    return all(determinant(block(moments, n)) > 0 for n in range(1, size + 1))


def geometric_case(n, d, r):
    moments = [four_pole(n + k) for k in range(2 * d + 2)]
    vector = [(-r) ** i for i in range(d + 1)]
    inv_v = solve(block(moments, d + 1), vector)
    t = 1 / sum(a * b for a, b in zip(vector, inv_v))
    fitted = [m - t * (-r) ** k for k, m in enumerate(moments[:-1])]
    assert determinant(block(fitted, d + 1)) == 0
    assert positive_definite(fitted, d)
    # Together these two positive shifted forms certify every real node lies in (0,1).
    assert positive_definite(fitted[1:], d)
    assert positive_definite([a - b for a, b in zip(fitted, fitted[1:])], d)
    q = solve(block(fitted, d), [-m for m in fitted[d:2 * d]]) + [Q(1)]
    assert all(sum(q[j] * fitted[i+j] for j in range(d+1)) == 0 for i in range(d+1))
    predicted_next = -sum(q[j] * fitted[d + 1 + j] for j in range(d))
    J = sum(q[i] * q[j] * (moments[1+i+j] + r * moments[i+j])
            for i in range(d+1) for j in range(d+1))
    residual = moments[-1] - predicted_next
    assert residual == J - t * r ** (2 * d + 1)
    return {"N": n, "d": d, "r": str(r), "t": str(t),
            "heldout_to_threshold": str(residual / (t * r ** (2 * d + 1)))}


def varied_envelope(n, d, weights):
    """Bracket the algebraic boundary by exact definiteness and check all matrix corners."""
    moments = [four_pole(n + k) for k in range(2 * d + 1)]
    def shifted(step, signs):
        return [m - step * sign * w for m, sign, w in zip(moments, signs, weights)]
    signs = [(-1) ** k for k in range(2 * d + 1)]
    lower, upper = Q(0), Q(1)
    while positive_definite(shifted(upper, signs), d + 1):
        upper *= 2
    for _ in range(38):
        midpoint = (lower + upper) / 2
        if positive_definite(shifted(midpoint, signs), d + 1):
            lower = midpoint
        else:
            upper = midpoint
    corners = list(product((-1, 1), repeat=2*d+1))
    assert all(positive_definite(shifted(lower, corner), d+1) for corner in corners)
    failed = [corner for corner in corners
              if not positive_definite(shifted(upper, corner), d+1)]
    assert failed == [tuple(signs)]
    # Independent tests in the original coordinate pencil, using positive-support forms.
    for step in (lower, upper):
        fitted = shifted(step, signs)
        assert positive_definite(fitted, d)
        assert positive_definite(fitted[1:], d)
        assert positive_definite([a-b for a, b in zip(fitted, fitted[1:])], d)
    return {"N": n, "d": d, "c": weights, "lower": str(lower), "upper": str(upper),
            "corners_each_side": len(corners), "unique_first_failing_corner": signs}


def allocation_control():
    moments = [four_pole(n) for n in (1, 2, 3)]
    def feasible_counts(counts):
        errors = [Q(2, 2**b) for b in counts]
        shifted = [m - (-1)**k * err for k, (m, err) in enumerate(zip(moments, errors))]
        return positive_definite(shifted, 2)

    uniform_bits = next(b for b in range(100) if feasible_counts((b, b, b)))
    for total in range(100):
        feasible = []
        for first in range(total + 1):
            for second in range(total - first + 1):
                counts = (first, second, total - first - second)
                if feasible_counts(counts):
                    feasible.append(counts)
        if feasible:
            return {"N": 1, "d": 1, "minimum_total_bits": total,
                    "all_minimizers": feasible, "uniform_bits_each": uniform_bits}
    raise AssertionError("no feasible schedule in declared search range")


def main():
    geometric = [geometric_case(n, d, r) for n in (1, 9, 100)
                 for d in (1, 2, 3) for r in (Q(1, 2), Q(1), Q(3))]
    assert all(Q(row["heldout_to_threshold"]) > 1 for row in geometric
               if row["N"] == 100 and row["r"] == "1")
    varied = [varied_envelope(1, 1, [1, 1, 2]),
              varied_envelope(3, 1, [1, 3, 1]),
              varied_envelope(2, 2, [4, 1, 3, 2, 5]),
              varied_envelope(11, 2, [2, 3, 1, 3, 1])]
    # Independent direct quadratic, no matrix eigenvalue or floating arithmetic.
    a, b, c = [four_pole(i) for i in (1, 2, 3)]
    linear = -(2*a + c + 2*b)
    constant = a*c - b*b
    discr = linear*linear - 4*constant
    assert isqrt(discr.denominator)**2 == discr.denominator
    assert isqrt(discr.numerator)**2 < discr.numerator < (isqrt(discr.numerator)+1)**2
    assert all((step*step + linear*step + constant) * sign > 0 for step, sign in
               ((Q(varied[0]["lower"]), 1), (Q(varied[0]["upper"]), -1)))
    harmonic = [Q(1, k+1) for k in range(3)]
    a, b, c = harmonic
    assert (a*c-b*b)/(a+2*b+c) == Q(1, 28)
    return {"geometric": geometric, "weighted_corners": varied, "allocation": allocation_control(),
            "irrational_radius_quadratic": list(map(str, (1, linear, constant))),
            "discriminant": str(discr), "harmonic_d1_uniform_radius": "1/28"}


if __name__ == "__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
