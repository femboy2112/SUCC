"""Exact finite calibrations for COMPLETE_SIGNED.md; no pi statistics claim.

Only standard-library rational arithmetic is used. Grid characters are averaged
over an explicitly declared complete root grid, never over a selected radix orbit.
The universal theorems are the paper proofs, not these finite examples.
"""

from fractions import Fraction as Q
import hashlib
import json


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise TypeError("Exact checks accept integers or Fractions only")
    return Q(value)


def matrix(rows):
    result = tuple(tuple(rational(x) for x in row) for row in rows)
    if not result or not result[0] or any(len(row) != len(result[0]) for row in result):
        raise ValueError("A matrix must be a nonempty rectangle")
    return result


def identity(size):
    if not isinstance(size, int) or size < 1:
        raise ValueError("Positive dimension required")
    return tuple(tuple(Q(i == j) for j in range(size)) for i in range(size))


def transpose(a):
    a = matrix(a)
    return tuple(zip(*a))


def matmul(a, b):
    a, b = matrix(a), matrix(b)
    if len(a[0]) != len(b):
        raise ValueError("Matrix dimensions do not compose")
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def matsub(a, b):
    a, b = matrix(a), matrix(b)
    if (len(a), len(a[0])) != (len(b), len(b[0])):
        raise ValueError("Matrix dimensions differ")
    return tuple(tuple(x - y for x, y in zip(row_a, row_b))
                 for row_a, row_b in zip(a, b))


def matadd(a, b):
    return matsub(a, tuple(tuple(-x for x in row) for row in matrix(b)))


def scale(a, scalar):
    scalar = rational(scalar)
    return tuple(tuple(scalar * x for x in row) for row in matrix(a))


def inf_norm(a):
    return max(sum(abs(x) for x in row) for row in matrix(a))


def chronological_product(matrices, dimension=None):
    matrices = tuple(matrix(a) for a in matrices)
    if matrices:
        dimension = len(matrices[0])
    if dimension is None:
        raise ValueError("An empty product needs its dimension")
    result = identity(dimension)
    for a in matrices:
        if len(a) != dimension or len(a[0]) != dimension:
            raise ValueError("Products require square matrices of one size")
        result = matmul(a, result)
    return result


def product_error_certificate(actual, estimated, dimension=None):
    actual = tuple(matrix(a) for a in actual)
    estimated = tuple(matrix(a) for a in estimated)
    if len(actual) != len(estimated):
        raise ValueError("Chronological lengths differ")
    if actual:
        dimension = len(actual[0])
    if dimension is None:
        raise ValueError("An empty product needs its dimension")
    left = matsub(chronological_product(actual, dimension),
                  chronological_product(estimated, dimension))
    right = scale(identity(dimension), 0)
    bound = Q(0)
    for j in range(len(actual)):
        suffix = chronological_product(actual[j + 1:], dimension)
        prefix = chronological_product(estimated[:j], dimension)
        error = matsub(actual[j], estimated[j])
        right = matadd(right, matmul(matmul(suffix, error), prefix))
        bound += inf_norm(suffix) * inf_norm(error) * inf_norm(prefix)
    return {"difference": left, "telescoped": right,
            "error_norm": inf_norm(left), "bound": bound}


def inverse(a):
    a = matrix(a)
    n = len(a)
    if len(a[0]) != n:
        raise ValueError("Inverse requires a square matrix")
    rows = [list(a[i]) + list(identity(n)[i]) for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            raise ValueError("Singular matrix")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        p = rows[j][j]
        rows[j] = [x / p for x in rows[j]]
        for i in range(n):
            if i != j:
                p = rows[i][j]
                rows[i] = [x - p * y for x, y in zip(rows[i], rows[j])]
    return tuple(tuple(row[n:]) for row in rows)


def rank(a):
    rows = [list(row) for row in matrix(a)]
    nr, nc = len(rows), len(rows[0])
    pivot_row = 0
    for j in range(nc):
        pivot = next((i for i in range(pivot_row, nr) if rows[i][j]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        p = rows[pivot_row][j]
        rows[pivot_row] = [x / p for x in rows[pivot_row]]
        for i in range(pivot_row + 1, nr):
            p = rows[i][j]
            rows[i] = [x - p * y for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == nr:
            break
    return pivot_row


def matvec(a, v):
    return tuple(row[0] for row in matmul(a, tuple((rational(x),) for x in v)))


def rowvec(v, a):
    return matmul((tuple(rational(x) for x in v),), a)[0]


def dot(a, b):
    a, b = tuple(a), tuple(b)
    if len(a) != len(b):
        raise ValueError("Vector dimensions differ")
    return sum(rational(x) * rational(y) for x, y in zip(a, b))


def moving_signed_certificate(states, operators, covectors, errors=None):
    states = tuple(tuple(rational(x) for x in v) for v in states)
    covectors = tuple(tuple(rational(x) for x in v) for v in covectors)
    operators = tuple(matrix(a) for a in operators)
    n = len(operators)
    if n < 1 or len(states) != n + 1 or len(covectors) != n + 1:
        raise ValueError("Need N operators and N+1 retained states/covectors")
    errors = tuple(Q(0) for _ in range(n)) if errors is None else tuple(map(rational, errors))
    if len(errors) != n:
        raise ValueError("Need one target error per chronological term")
    residuals, targets = [], []
    for j in range(n):
        aq = matvec(operators[j], states[j])
        r = tuple(x - y for x, y in zip(states[j + 1], aq))
        if len(r) != len(states[j + 1]) or len(aq) != len(states[j + 1]):
            raise ValueError("State dimensions differ")
        following = rowvec(covectors[j + 1], operators[j])
        f = tuple(x - y for x, y in zip(covectors[j], following))
        if len(f) != len(covectors[j]) or len(following) != len(covectors[j]):
            raise ValueError("Covector dimensions differ")
        residuals.append(r)
        targets.append(dot(f, states[j]) + errors[j])
    boundary = dot(covectors[0], states[0]) - dot(covectors[-1], states[-1])
    projected = sum(dot(covectors[j + 1], residuals[j]) for j in range(n))
    output_error = sum(errors)
    return {"count": n, "target_sum": sum(targets), "boundary": boundary,
            "projected_residual": projected, "output_error": output_error,
            "reconstructed_sum": boundary + projected + output_error,
            "targets": tuple(targets), "residuals": tuple(residuals)}


def hankel(sequence, width):
    sequence = tuple(map(rational, sequence))
    if not isinstance(width, int) or not 1 <= width <= len(sequence):
        raise ValueError("Width must fit the retained sequence")
    return tuple(tuple(sequence[n + j] for j in range(width))
                 for n in range(len(sequence) - width + 1))


def normalized_gram(a):
    a = matrix(a)
    return scale(matmul(transpose(a), a), Q(1, len(a)))


def gram_lower_bound(g):
    """Gershgorin lower bound for a symmetric matrix; no positivity assumed."""
    g = matrix(g)
    if len(g) != len(g[0]) or transpose(g) != g:
        raise ValueError("A symmetric rational matrix is required")
    return min(g[i][i] - sum(abs(g[i][j]) for j in range(len(g)) if j != i)
               for i in range(len(g)))


def compression_certificate(actual, prediction, width, rank_budget):
    actual, prediction = tuple(map(rational, actual)), tuple(map(rational, prediction))
    if len(actual) != len(prediction):
        raise ValueError("Time labels must have equal length")
    if not isinstance(rank_budget, int) or not 0 <= rank_budget < width:
        raise ValueError("Require 0 <= rank budget < delay width")
    hz, hy = hankel(actual, width), hankel(prediction, width)
    actual_rank = rank(hy)
    if actual_rank > rank_budget:
        raise ValueError("The proposed prediction fails its rank contract")
    g = normalized_gram(hz)
    # This matrix was constructed as H^T H/N, so its positivity is certified.
    gamma = max(Q(0), gram_lower_bound(g))
    length, n = len(actual), len(hz)
    error = sum((x - y) ** 2 for x, y in zip(actual, prediction)) / length
    lower = Q(n, length) * Q(width - rank_budget, width) * gamma
    matrix_error = sum(x * x for row in matsub(hz, hy) for x in row)
    return {"length": length, "rows": n, "width": width,
            "rank_budget": rank_budget, "prediction_rank": actual_rank,
            "gram": g, "gram_lower_bound": gamma,
            "mean_square_error": error, "error_lower_bound": lower,
            "hankel_squared_error": matrix_error,
            "multiplicity_upper_bound": width * length * error}


def complete_grid_delay_gram(base, frequency, width, modulus):
    """Gram over ALL a/modulus; this is an ensemble, not a radix trajectory."""
    if any(type(x) is not int for x in (base, frequency, width, modulus)):
        raise TypeError("Root-grid parameters must be exact integers")
    if base < 2 or width < 1 or modulus < 1:
        raise ValueError("Require base>=2, width>=1, modulus>=1")
    exponents = [frequency * pow(base, j, modulus) % modulus for j in range(width)]
    return tuple(tuple(Q((b - a) % modulus == 0) for b in exponents)
                 for a in exponents)


def radix_turns(base, initial, count, frequency=1):
    if any(type(x) is not int for x in (base, count, frequency)):
        raise TypeError("Radix, count, and frequency must be exact integers")
    if base < 2 or count < 0:
        raise ValueError("Invalid radix or observation count")
    x = (rational(initial) * frequency) % 1
    values = []
    for _ in range(count):
        values.append(x)
        x = base * x % 1
    return tuple(values)


def recurrence_root_bound(base, support):
    support = tuple(support)
    if type(base) is not int or base < 2 or not support or any(type(j) is not int or j < 0 for j in support):
        raise ValueError("Need nonempty nonnegative exponent support and base>=2")
    if len(set(support)) != len(support):
        raise ValueError("Support entries must be distinct")
    return base ** max(support) - base ** min(support)


def binary_debruijn(order):
    """Classical necklace recursion; used only as an exact auxiliary sign record."""
    if not isinstance(order, int) or order < 1:
        raise ValueError("Positive order required")
    a = [0] * (2 * order + 1)
    sequence = []

    def visit(t, p):
        if t > order:
            if order % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            visit(t + 1, p)
            for j in range(a[t - p] + 1, 2):
                a[t] = j
                visit(t + 1, t)

    visit(1, 1)
    return tuple(sequence)


def receipt():
    certificates = []
    for order in range(2, 8):
        bits = binary_debruijn(order)
        signs = tuple(1 - 2 * b for b in bits)
        for width in range(2, order + 1):
            observed = signs + signs[:width - 1]
            for constant in (Q(-1, 2), Q(0), Q(1), Q(3, 2)):
                cert = compression_certificate(observed, [constant] * len(observed), width, 1)
                assert cert["gram"] == identity(width)
                assert cert["mean_square_error"] >= cert["error_lower_bound"]
                certificates.append({k: str(v) for k, v in cert.items() if k != "gram"})
    serialized = json.dumps(certificates, sort_keys=True, separators=(",", ":"))
    return {"status": "EXACT_FINITE_CALIBRATION_ONLY",
            "compression_cases": len(certificates),
            "case_payload_sha256": hashlib.sha256(serialized.encode()).hexdigest(),
            "first_certificate": certificates[0], "last_certificate": certificates[-1],
            "pi_normality": "OPEN", "normality_corollary": "CONDITIONAL_PAPER_THEOREM"}


if __name__ == "__main__":
    print(json.dumps(receipt(), indent=2, sort_keys=True))
