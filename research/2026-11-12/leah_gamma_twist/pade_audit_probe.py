"""Independent exact Legendre-recurrence checks for GAUSSIAN_PADE.md.

No binomial polynomial evaluator or Gaussian probe implementation is imported.
The finite checks validate formulas; they do not prove the all-degree statement.
Run from any directory; JSON is emitted to stdout.
"""
from fractions import Fraction as F
from math import comb
import json


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def scale(c, x):
    return c * x[0], c * x[1]


def mul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def power(x, n):
    y = (F(1), F(0))
    while n:
        if n % 2:
            y = mul(y, x)
        x = mul(x, x)
        n //= 2
    return y


def v2(x):
    """Rational 2-adic valuation; zero is deliberately outside this helper."""
    if not x:
        raise ValueError("v2(0) is not a finite integer")

    def vi(m):
        m = abs(m)
        return (m & -m).bit_length() - 1

    return vi(x.numerator) - vi(x.denominator)


def q_legendre(n, q):
    if n < 1 or q < 3 or not q % 2:
        raise ValueError("requires n >= 1 and odd q >= 3")
    x = (F(0), F(-q))
    p0, p1 = (F(1), F(0)), x
    for k in range(1, n):
        p0, p1 = p1, scale(
            F(1, k + 1),
            add(scale(2 * k + 1, mul(x, p1)), scale(-k, p0)),
        )
    z = (F(-2, q * q + 1), F(2 * q, q * q + 1))
    return mul(power(z, n), p1)


def run():
    rows = []
    for n in [4, 8, 16, 32, 64, 128]:
        for q in [11, 13, 29, 43, 101]:
            a, b = q_legendre(n, q)
            norm = a * a + b * b
            gaussian_valuation = F(v2(norm), 2)
            assert gaussian_valuation == 1
            assert norm >= F(q * q, q * q + 1) ** n * comb(2 * n, n) ** 2
            rows.append({"n": n, "q": q, "v_Q": str(gaussian_valuation),
                         "squared_archimedean_bound": "PASS"})
    a, b = q_legendre(3, 5)
    control = F(v2(a * a + b * b), 2)
    assert control == F(15, 2)
    return {
        "authority": "exact finite implementation checks; universal proof is in the manuscript",
        "independent_legendre_cases": len(rows),
        "rows": rows,
        "nonpower_degree_control": {"n": 3, "q": 5, "v_Q": str(control)},
        "status": "PASS",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
