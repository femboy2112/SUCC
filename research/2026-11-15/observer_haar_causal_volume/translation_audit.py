"""Bounded translator audit; imports no SUCC production or research modules.

Exact matrix checks use SymPy rational algebra. The separately labelled Oily
quadratures are diagnostics, not interval certificates or universal proofs.
Run from any directory: python /absolute/path/to/translation_audit.py
"""
from itertools import combinations
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp
import sympy as sp


def partition_projection(weights, cells):
    n = len(weights)
    result = sp.zeros(n)
    for cell in cells:
        mass = sum(weights[j] for j in cell)
        for i in cell:
            for j in cell:
                result[i, j] = weights[j] / mass
    return result


def adjoint(matrix, weights):
    metric = sp.diag(*weights)
    return metric.inv() * matrix.T * metric


def psd_by_principal_minors(matrix):
    if matrix != matrix.T:
        return False
    return all(
        matrix.extract(indices, indices).det() >= 0
        for size in range(1, matrix.rows + 1)
        for indices in combinations(range(matrix.rows), size)
    )


def reversible_generator(weights):
    result = sp.zeros(len(weights))
    for i, j, conductance in (
        (0, 1, sp.Rational(1)),
        (1, 2, sp.Rational(2)),
        (2, 3, sp.Rational(1)),
        (0, 3, sp.Rational(1, 2)),
    ):
        result[i, j] += conductance / weights[i]
        result[j, i] += conductance / weights[j]
    for i in range(len(weights)):
        result[i, i] = -sum(result[i, j] for j in range(len(weights)) if j != i)
    return result


def run_exact():
    n = 4
    identity = sp.eye(n)
    checks = 0

    def require(condition):
        nonlocal checks
        assert condition
        checks += 1

    weights_list = (
        tuple(sp.Rational(1, 4) for _ in range(4)),
        tuple(sp.Rational(j, 10) for j in (1, 2, 3, 4)),
    )
    wrong_euclidean_gram_detected = False
    for weights in weights_list:
        metric = sp.diag(*weights)
        generator = reversible_generator(weights)
        p = partition_projection(weights, ((0, 1), (2, 3)))
        middle = partition_projection(weights, ((0,), (1,), (2, 3)))
        p_constant = partition_projection(weights, ((0, 1, 2, 3),))
        q = identity - p
        details = (middle - p, identity - middle)
        require(adjoint(generator, weights) == generator)
        require(adjoint(p, weights) == p)
        require(p * p == p)
        require(p * generator != generator * p)
        for rate in (sp.Rational(1), sp.Rational(2), sp.Rational(3, 2)):
            resolvent = (identity - generator / rate).inv()
            for depth in (1, 2, 3):
                g = resolvent ** depth
                defect = p * (g * g) * p - (p * g * p) ** 2
                leakage = q * g * p
                gram = adjoint(leakage, weights) * leakage
                graded = sum(
                    (adjoint(e * g * p, weights) * (e * g * p) for e in details),
                    sp.zeros(n),
                )
                require(defect == gram == graded)
                require(defect != sp.zeros(n))
                require(psd_by_principal_minors(metric * defect))
                require(psd_by_principal_minors(metric * (p / 4 - defect)))
                require(p_constant * (g * g) * p_constant == (p_constant * g * p_constant) ** 2)
                if weights != weights_list[0] and leakage.T * leakage != defect:
                    wrong_euclidean_gram_detected = True
        require(p * identity * p - (p * identity * p) ** 2 == sp.zeros(n))
    require(wrong_euclidean_gram_detected)

    # Same finite Markov class but without reversibility: the claimed Gram
    # positivity must fail for the genuine composition defect.
    shift = sp.zeros(n)
    for i in range(n):
        shift[i, (i + 1) % n] = 1
    g = (2 * identity - shift).inv()
    p = partition_projection(weights_list[0], ((0, 1), (2, 3)))
    v = sp.Matrix((1, 1, -1, -1))
    directed_defect = p * g * g * p - (p * g * p) ** 2
    require(directed_defect == -v * v.T / 100)
    require(directed_defect * v == -v / 25)
    require(not psd_by_principal_minors(directed_defect))

    # Unequal depths can destroy self-adjointness even when L is reversible.
    generator = reversible_generator(weights_list[0])
    g = (identity - generator).inv()
    p3 = partition_projection(weights_list[0], ((0, 1), (2,), (3,)))
    unequal = p3 * g ** 3 * p3 - (p3 * g * p3) * (p3 * g ** 2 * p3)
    require(unequal != unequal.T)

    x = sp.symbols("x", real=True)
    numerator = 4 - 2 * x ** 3 - x ** 4 - x ** 5
    source = numerator / (16 - x ** 8)
    u, v_rate = x - x ** 2 / 2, x ** 2 / 2
    a = sp.expand((1 - u) * (1 - v_rate))
    require(sp.expand(numerator - (1 - x) * (x ** 2 + 2) * (x ** 2 + 2 * x + 2)) == 0)
    require(sp.cancel(a * source - (1 - x) / 4) == 0)
    require(sp.integrate((1 - x) / 4, (x, 0, 1)) == sp.Rational(1, 8))
    require(sp.integrate((1 - x) * a / 4, (x, 0, 1)) == sp.Rational(7, 80))
    require(sp.expand(sp.diff(a, x) + 1 - x ** 2 * (sp.Rational(3, 2) - x)) == 0)
    require(sp.expand(sp.diff(a, x) + sp.Rational(1, 2) + (1 - x) ** 2 * (x + sp.Rational(1, 2))) == 0)
    return {
        "label": "exact rational identities and finite matrix controls",
        "checks_passed": checks,
        "reversible_matrix_cases": 18,
        "rates": ["1", "2", "3/2"],
        "integer_depths": [1, 2, 3],
        "stationary_weights": [[str(v) for v in w] for w in weights_list],
        "wrong_euclidean_adjoint_detected": wrong_euclidean_gram_detected,
        "nonreversible_defect": [[str(v) for v in directed_defect.row(i)] for i in range(n)],
        "nonreversible_negative_eigenvalue": "-1/25",
        "unequal_depth_defect_is_not_self_adjoint": True,
        "oily_first_unnormalized_moment": "1/8",
        "oily_second_unnormalized_moment": "7/80",
    }


def run_oily_quadrature():
    mp.mp.dps = 50

    def r(x):
        return (4 - 2 * x ** 3 - x ** 4 - x ** 5) / (16 - x ** 8)

    def a(x):
        return (1 - x + x * x / 2) * (1 - x * x / 2)

    z = mp.quad(r, [0, 1])
    first = mp.quad(lambda x: a(x) * r(x), [0, 1])
    second = mp.quad(lambda x: a(x) ** 2 * r(x), [0, 1])
    total = second / z - (first / z) ** 2
    rows = []
    for depth in range(6):
        coarse_second = mp.mpf("0")
        for index in range(2 ** depth):
            left = mp.mpf(index) / (2 ** depth)
            right = mp.mpf(index + 1) / (2 ** depth)
            mass = mp.quad(r, [left, right])
            local_first = mp.quad(lambda x: a(x) * r(x), [left, right])
            coarse_second += local_first ** 2 / mass / z
        haar_sum = coarse_second - (first / z) ** 2
        residual = second / z - coarse_second
        analytic_bound = mp.mpf(4) ** (-depth) / 4
        rows.append({
            "depth": depth,
            "haar_sum": mp.nstr(haar_sum, 50),
            "residual": mp.nstr(residual, 50),
            "proved_bound_value": mp.nstr(analytic_bound, 50),
            "diagnostic_bound_comparison": residual <= analytic_bound,
        })
    return {
        "label": "non-rigorous numerical diagnostic; no interval certificate",
        "precision_decimal_digits": mp.mp.dps,
        "source_mass": mp.nstr(z, 50),
        "source_mass_minus_pi_over_16": mp.nstr(z - mp.pi / 16, 10),
        "variance": mp.nstr(total, 50),
        "variance_minus_closed_formula": mp.nstr(total - (7 * mp.pi - 20) / (5 * mp.pi ** 2), 10),
        "rows": rows,
    }


if __name__ == "__main__":
    print(json.dumps({
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "mpmath": mp.__version__,
        "exact": run_exact(),
        "diagnostic": run_oily_quadrature(),
    }, indent=2))
