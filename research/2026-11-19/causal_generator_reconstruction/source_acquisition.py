"""Exact five-raw-state acquisition in a declared BBP source family.

This standalone research instrument does not infer an unknown source family,
claim finite-precision equality, or evaluate a normality limit.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product

POLES = (7, 4, 3, 2)
AUTHENTIC = (Q(4), Q(-2), Q(-1), Q(-1))


def check_times(times):
    times = tuple(times)
    if len(times) != 5 or any(type(t) is not int or t < 0 for t in times):
        raise ValueError("exactly five nonnegative integer clocks are required")
    if any(a >= b for a, b in zip(times, times[1:])):
        raise ValueError("clocks must be strictly increasing")
    return times


def forcing(n, coefficients=AUTHENTIC):
    if type(n) is not int or n < 1:
        raise ValueError("source clocks begin at one")
    if len(coefficients) != 4:
        raise ValueError("four coefficients are required")
    return sum((Q(c) / (8 * n - d) for c, d in zip(coefficients, POLES)), Q())


def states_through(n, coefficients=AUTHENTIC, seed=Q()):
    if type(n) is not int or n < 0:
        raise ValueError("nonnegative horizon required")
    states = [Q(seed)]
    for j in range(1, n + 1):
        states.append(16 * states[-1] + forcing(j, coefficients))
    return states


def normalized_rows(times):
    """Rows a_t from a single forward traversal, without retaining the journal."""
    times = check_times(times)
    selected = set(times)
    row = [Q() for _ in POLES]
    result = {0: tuple(row)} if 0 in selected else {}
    for j in range(1, times[-1] + 1):
        for a, pole in enumerate(POLES):
            row[a] += Q(1, 16**j * (8 * j - pole))
        if j in selected:
            result[j] = tuple(row)
    return [result[t] for t in times]


def sampling_matrix(times):
    """Parameter order is seed, then the four signed source coefficients."""
    times = check_times(times)
    return [[Q(16**t)] + [16**t * a for a in row]
            for t, row in zip(times, normalized_rows(times))]


def block_matrix(times):
    rows = normalized_rows(times)
    return [[rows[i][j] - rows[i - 1][j] for j in range(4)] for i in range(1, 5)]


def inverse(matrix):
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("a nonempty square matrix is required")
    a = [[Q(x) for x in row] + [Q(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            raise ValueError("singular observation matrix")
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [x / scale for x in a[j]]
        for i in range(n):
            if i != j:
                scale = a[i][j]
                a[i] = [x - scale * y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def determinant(matrix):
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("square matrix required")
    a = [[Q(x) for x in row] for row in matrix]
    det = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Q()
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det = -det
        value = a[j][j]
        det *= value
        for i in range(j + 1, n):
            scale = a[i][j] / value
            for k in range(j + 1, n):
                a[i][k] -= scale * a[j][k]
    return det


def matvec(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), Q()) for row in matrix]


def recover(times, readings):
    times = check_times(times)
    if len(readings) != 5:
        raise ValueError("five readings required")
    v = [Q(y) / 16**t for t, y in zip(times, readings)]
    differences = [v[i] - v[i - 1] for i in range(1, 5)]
    coefficients = matvec(inverse(block_matrix(times)), differences)
    a0 = normalized_rows(times)[0]
    seed = v[0] - sum((a * c for a, c in zip(a0, coefficients)), Q())
    return (seed, *coefficients)


def cauchy_determinant(clocks):
    clocks = tuple(clocks)
    if len(clocks) != 4 or any(n < 1 for n in clocks):
        raise ValueError("four positive clocks required")
    numerator = 120 * 8**6
    for i in range(4):
        for j in range(i + 1, 4):
            numerator *= clocks[j] - clocks[i]
    denominator = 1
    for n in clocks:
        for pole in POLES:
            denominator *= 8 * n - pole
    return Q(numerator, denominator)


def block_determinant_expansion(times, max_terms=100000):
    """Small-case certificate for formula (2), not a large-gap algorithm."""
    times = check_times(times)
    ranges = [range(a + 1, b + 1) for a, b in zip(times, times[1:])]
    count = 1
    for interval in ranges:
        count *= len(interval)
    if count > max_terms:
        raise ValueError("explicit determinant expansion exceeds declared budget")
    return sum((cauchy_determinant(js) / 16**sum(js) for js in product(*ranges)), Q())


def precision_budget(times, errors):
    if len(errors) != 5 or any(Q(x) < 0 for x in errors):
        raise ValueError("five nonnegative absolute raw error bounds required")
    inv = inverse(sampling_matrix(times))
    return [sum((abs(a) * Q(e) for a, e in zip(row, errors)), Q()) for row in inv]


def knowledge_volume(times, errors):
    if len(errors) != 5 or any(Q(x) <= 0 for x in errors):
        raise ValueError("five strictly positive widths required")
    volume = Q(1)
    for e in errors:
        volume *= 2 * Q(e)
    return volume / abs(determinant(sampling_matrix(times)))


def completion_error_bound(coefficients, horizon):
    """SA-05 bound for normalized endpoint, valid for any real coefficients."""
    if horizon < 0:
        raise ValueError("nonnegative horizon required")
    return sum((abs(Q(c)) for c in coefficients), Q()) / (
        15 * 16**horizon * (8 * horizon + 1))
