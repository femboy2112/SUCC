"""Exact finite controls for Main XXVI's observer/Gamma transport proof.

No production Gamma implementation is imported.  Rational matrices independently
check the signed identity and integer-shape bounds.  Infinite-shape authority
belongs to the written proof, not to this bounded scan.
"""
from fractions import Fraction as Q
import json
import random


def eye(n):
    return tuple(tuple(Q(i == j) for j in range(n)) for i in range(n))


def mul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def sub(a, b):
    return tuple(tuple(x-y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def scale(a, s):
    return tuple(tuple(s*x for x in row) for row in a)


def power(a, n):
    result = eye(len(a))
    for _ in range(n):
        result = mul(result, a)
    return result


def inverse(a):
    n = len(a)
    rows = [list(row) + list(e) for row, e in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        d = rows[j][j]
        rows[j] = [v/d for v in rows[j]]
        for i in range(n):
            if i != j:
                d = rows[i][j]
                rows[i] = [v-d*w for v, w in zip(rows[i], rows[j])]
    return tuple(tuple(row[n:]) for row in rows)


def norm(a):
    return max(sum(map(abs, row), Q(0)) for row in a)


def gamma(a, order):
    return power(inverse(sub(scale(eye(len(a)), 2), a)), order)


def run_checks():
    rng = random.Random(20261116)
    matrix_cases = 0
    orientation_mutants = 0
    for _ in range(80):
        k = tuple(tuple(Q(rng.randrange(-2, 3), 4) for _ in range(2)) for _ in range(2))
        b = tuple(tuple(Q(rng.randrange(-2, 3), 4) for _ in range(2)) for _ in range(2))
        p = tuple(tuple(Q(rng.randrange(-3, 4), 3) for _ in range(2)) for _ in range(2))
        assert norm(k) <= 1 and norm(b) <= 1
        d = sub(mul(p, k), mul(b, p))
        rk, rb = gamma(k, 1), gamma(b, 1)
        left = sub(mul(p, rk), mul(rb, p))
        assert left == mul(mul(rb, d), rk)
        if left != mul(mul(rk, d), rb):
            orientation_mutants += 1
        for order in range(1, 5):
            defect = sub(mul(p, gamma(k, order)), mul(gamma(b, order), p))
            assert norm(defect) <= order * norm(d)
            matrix_cases += 1
    assert orientation_mutants > 0
    scalar_cases = 0
    for order in range(1, 9):
        for ki in range(-4, 5):
            for bi in range(-4, 5):
                k, b = Q(ki, 4), Q(bi, 4)
                assert abs((2-k)**(-order) - (2-b)**(-order)) <= order*abs(k-b)
                scalar_cases += 1
    for i in range(21):
        x = Q(i, 20)
        u, v = x-x*x/2, x*x/2
        assert 0 <= u <= Q(1, 2) and 0 <= v <= Q(1, 2)
        assert 0 <= u/(1-u) + v/(1-v) <= 2
    endpoint_ratios = []
    for order in range(1, 5):
        eps = Q(1, 1000)
        ratio = (1-(1+eps)**(-2*order))/eps
        assert 0 < ratio < 2*order
        endpoint_ratios.append({"alpha": order, "ratio": str(ratio), "upper": 2*order})
    k, b = Q(19, 10), Q(9, 5)
    assert abs((2-k)**(-1)-(2-b)**(-1)) == 5
    assert abs(k-b) == Q(1, 10)
    assert abs((2-k)**(-1)-(2-b)**(-1)) > abs(k-b)
    return {
        "status": "EXACT_FINITE_CONTROLS_PASS_NOT_UNIVERSAL_PROOF",
        "matrix_integer_shape_cases": matrix_cases,
        "reversed_orientation_mutants_rejected": orientation_mutants,
        "scalar_contraction_cases": scalar_cases,
        "retained_original_source_coordinates": 21,
        "two_loop_endpoint_ratios": endpoint_ratios,
        "noncontraction_mutant": {"actual_error": "5", "invalid_upper_bound": "1/10"},
        "R0_or_pi_normality_proved": False,
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
