"""Exact finite carry control-variate algebra; no source-decay assertion.

Complex numbers are pairs of Fraction, never binary floating-point values.
The uniform append operator is a reference model, not the actual carry law.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product

ZERO = (Q(0), Q(0))


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def scale(z, c):
    return (z[0] * c, z[1] * c)


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1],
            z[0] * w[1] + z[1] * w[0])


def conjugate(z):
    return (z[0], -z[1])


def norm_squared(z):
    return z[0] * z[0] + z[1] * z[1]


def total(values):
    ans = ZERO
    for z in values:
        ans = add(ans, z)
    return ans


def mean(values):
    values = tuple(values)
    if not values:
        raise ValueError("nonempty values required")
    return scale(total(values), Q(1, len(values)))


def states(base, depth):
    if type(base) is not int or base < 2:
        raise ValueError("integer base >= 2 required")
    if type(depth) is not int or depth < 1:
        raise ValueError("integer depth >= 1 required")
    return tuple(product(range(base), repeat=depth))


def validated_table(table, base, depth):
    support = states(base, depth)
    if set(table) != set(support):
        raise ValueError("complete table on the declared state space required")
    for z in table.values():
        if type(z) is not tuple or len(z) != 2 or any(type(q) is not Q for q in z):
            raise ValueError("Gaussian Fraction entries required")
    return support


def append_operator(table, base, depth):
    support = validated_table(table, base, depth)
    return {w: mean(table[w[1:] + (d,)] for d in range(base)) for w in support}


def poisson_compile(table, base=16, depth=1):
    support = validated_table(table, base, depth)
    mu = mean(table[w] for w in support)
    term = {w: sub(table[w], mu) for w in support}
    psi = {w: ZERO for w in support}
    for _ in range(depth):
        psi = {w: add(psi[w], term[w]) for w in support}
        term = append_operator(term, base, depth)
    if any(z != ZERO for z in term.values()):
        raise ArithmeticError("reference operator did not forget depth symbols")
    ppsi = append_operator(psi, base, depth)
    if any(sub(psi[w], ppsi[w]) != sub(table[w], mu) for w in support):
        raise ArithmeticError("Poisson identity failed")
    return {"mean": mu, "potential": psi, "reference_potential": ppsi}


def transient_literal_poisson_compile(table, base=16, depth=1):
    """CCV1-L: states allow carry==base, reference appends only 0,...,base-1."""
    support = validated_table(table, base+1, depth)
    ordinary = states(base, depth)
    mu = mean(table[w] for w in ordinary)
    def reference(value):
        return {w: mean(value[w[1:] + (d,)] for d in range(base)) for w in support}
    term = {w: sub(table[w], mu) for w in support}
    psi = {w: ZERO for w in support}
    for _ in range(depth):
        psi = {w: add(psi[w], term[w]) for w in support}
        term = reference(term)
    if any(z != ZERO for z in term.values()):
        raise ArithmeticError("literal transient state did not vanish after depth appends")
    ppsi = reference(psi)
    if any(sub(psi[w], ppsi[w]) != sub(table[w], mu) for w in support):
        raise ArithmeticError("literal reference Poisson identity failed")
    return {"mean": mu, "potential": psi, "reference_potential": ppsi}


def integer_lift_poisson_compile(values, base=16, depth=1):
    """Exact target quotient: state is floor(U_n) modulo base**depth."""
    states(base, depth)  # Validate integer parameters using the shared guard.
    q = base**depth
    values = tuple(values)
    if len(values) != q or any(type(z) is not tuple or len(z) != 2 or
                              any(type(v) is not Q for v in z) for z in values):
        raise ValueError("base**depth Gaussian Fraction values required")
    def reference(vector):
        return tuple(mean(vector[(base*s+d) % q] for d in range(base)) for s in range(q))
    mu = mean(values)
    term = tuple(sub(z, mu) for z in values)
    psi = (ZERO,) * q
    for _ in range(depth):
        psi = tuple(add(a, b) for a, b in zip(psi, term))
        term = reference(term)
    if any(z != ZERO for z in term):
        raise ArithmeticError("integer-lift reference failed to forget its state")
    ppsi = reference(psi)
    if any(sub(a, b) != sub(z, mu) for a, b, z in zip(psi, ppsi, values)):
        raise ArithmeticError("integer-lift Poisson identity failed")
    return {"mean": mu, "potential": psi, "reference_potential": ppsi}


def occupation_identity(table, path, base=16, depth=1):
    compiled = poisson_compile(table, base, depth)
    path = tuple(path)
    if len(path) < 2:
        raise ValueError("path needs at least one edge")
    if any(w not in table for w in path):
        raise ValueError("path state outside declared space")
    if any(v[:-1] != w[1:] for w, v in zip(path, path[1:])):
        raise ValueError("noncausal append path")
    n = len(path) - 1
    psi, ppsi = compiled["potential"], compiled["reference_potential"]
    boundary = scale(sub(psi[path[0]], psi[path[-1]]), Q(1, n))
    innovation = mean(sub(psi[v], ppsi[w]) for w, v in zip(path, path[1:]))
    actual = mean(table[w] for w in path[:-1])
    if actual != add(compiled["mean"], add(boundary, innovation)):
        raise ArithmeticError("carry occupation identity failed")
    return dict(compiled, boundary=boundary, innovation=innovation, actual=actual)


def literal_occupation_identity(table, path, base=16, depth=1):
    """Retain exceptional literal carry==base as an explicit correction."""
    support = states(base, depth)
    ordinary = {w: table[w] for w in support}
    path = tuple(path)
    if len(path) < 2:
        raise ValueError("path needs at least one edge")
    if any(type(w) is not tuple or len(w) != depth or
           any(type(d) is not int or not 0 <= d <= base for d in w) for w in path):
        raise ValueError("late literal carry words must use 0,...,base")
    if any(v[:-1] != w[1:] for w, v in zip(path, path[1:])):
        raise ValueError("noncausal literal append path")
    for w in path[:-1]:
        z = table[w]
        if type(z) is not tuple or len(z) != 2 or any(type(q) is not Q for q in z):
            raise ValueError("Gaussian Fraction entries required")
    residue_path = tuple(tuple(d % base for d in w) for w in path)
    result = occupation_identity(ordinary, residue_path, base, depth)
    correction = mean(sub(table[v], ordinary[w])
                      for v, w in zip(path[:-1], residue_path[:-1]))
    literal_mean = mean(table[w] for w in path[:-1])
    if literal_mean != add(result["actual"], correction):
        raise ArithmeticError("literal carry correction failed")
    return dict(result, literal_correction=correction, literal_mean=literal_mean,
                exceptional_words=sum(base in w for w in path[:-1]))


def padded_vdc(values, horizon):
    """Exact nonnegative V_H using correlations and a separate window route."""
    values = tuple(values)
    n = len(values)
    if not n or type(horizon) is not int or not 1 <= horizon <= n:
        raise ValueError("1 <= integer horizon <= nonempty sample length required")
    correlations = tuple(
        scale(total(mul(values[i + d], conjugate(values[i]))
                    for i in range(n - d)), Q(1, n))
        for d in range(horizon)
    )
    bracket = correlations[0][0] + 2 * sum(
        (Q(horizon - d, horizon) * correlations[d][0]
         for d in range(1, horizon)), Q(0)
    )
    window_squares = sum((norm_squared(total(values[i]
                         for i in range(max(0, t), min(n, t + horizon))))
                         for t in range(1 - horizon, n)), Q(0))
    if window_squares != horizon * n * bracket or bracket < 0:
        raise ArithmeticError("padded-window Gram normalization failed")
    upper_squared = Q(n + horizon - 1, n * horizon) * bracket
    if norm_squared(mean(values)) > upper_squared:
        raise ArithmeticError("Cauchy-Schwarz certificate failed")
    return {"correlations": correlations, "bracket": bracket,
            "window_squares": window_squares, "upper_squared": upper_squared,
            "actual_mean_squared": norm_squared(mean(values))}


def conditional_l2_identity(values, path, table):
    """Finite empirical projection identity, with test-table mismatch retained."""
    values, path = tuple(values), tuple(path)
    if not values or len(values) != len(path):
        raise ValueError("equally sized nonempty phase and state records required")
    if any(norm_squared(z) != 1 for z in values):
        raise ValueError("exact unit phases required")
    if any(w not in table for w in path):
        raise ValueError("missing predictor state")
    grouped = {}
    for w, z in zip(path, values):
        grouped.setdefault(w, []).append(z)
    n = len(values)
    cell_means = {w: mean(v) for w, v in grouped.items()}
    optimum = 1 - sum((Q(len(v), n) * norm_squared(cell_means[w])
                       for w, v in grouped.items()), Q(0))
    mismatch = sum((Q(len(v), n) * norm_squared(sub(table[w], cell_means[w]))
                    for w, v in grouped.items()), Q(0))
    observed = sum((norm_squared(sub(z, table[w]))
                    for w, z in zip(path, values)), Q(0)) / n
    if observed != optimum + mismatch:
        raise ArithmeticError("conditional orthogonal projection failed")
    return {"risk": observed, "empirical_optimum": optimum,
            "transferred_table_mismatch": mismatch, "cell_means": cell_means}
