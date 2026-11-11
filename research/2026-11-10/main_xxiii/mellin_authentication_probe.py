"""Exact audit of finite Mellin aliasing and terminating rational controls."""

from fractions import Fraction
from math import prod


SOURCE = {0: 4, 3: -2, 4: -1, 5: -1}
POLES = (1, 4, 5, 6)


def mellin(polynomial, n):
    return sum(
        (Fraction(coefficient, 8 * n + exponent + 1)
         for exponent, coefficient in polynomial.items()),
        Fraction(),
    )


def endpoint_moment(m, k):
    start = m + 8 * k + 1
    return Fraction(1, start * (start + 1))


def inner(left, right, moments):
    return sum(
        (a * b * moments[i + j]
         for i, a in enumerate(left) for j, b in enumerate(right)),
        Fraction(),
    )


def orthogonal_basis(degree, moments):
    """Monic polynomials by projection of monomials, without solving a Gram system."""
    basis = []
    for j in range(degree + 1):
        monomial = [Fraction(0)] * j + [Fraction(1)]
        polynomial = monomial.copy()
        for q, norm in basis:
            projection = inner(monomial, q, moments) / norm
            for i, coefficient in enumerate(q):
                polynomial[i] -= projection * coefficient
        basis.append((polynomial, inner(polynomial, polynomial, moments)))
    return basis


def coefficient_norm(polynomial):
    return sum(map(abs, polynomial))


def ordinary_alias(n):
    degree = n + 1
    moments = [endpoint_moment(0, k) for k in range(2 * degree + 1)]
    q, norm = orthogonal_basis(degree, moments)[-1]
    assert q[-1] == 1 and norm > 0
    for k in range(degree):
        assert inner([0] * k + [1], q, moments) == 0
    assert inner([0] * degree + [1], q, moments) == norm
    if n == 0:
        assert q == [Fraction(-1, 45), 1]

    epsilon = 1 / coefficient_norm(q)
    lower = epsilon * norm / sum(a * 16**i for i, a in enumerate(q))
    upper = Fraction(16, 15) * lower
    horizon = 4 * degree + 12
    # Independently enclose the integral by its finite geometric expansion.
    partial = sum(
        (epsilon * sum(a * endpoint_moment(0, i + k) for i, a in enumerate(q))
         / 16**k for k in range(horizon)),
        Fraction(),
    )
    remainder = Fraction(16, 15 * 16**horizon) * moments[0]
    assert 0 < lower < partial - remainder < partial + remainder < upper
    print(f"ordinary alias N={n}: exact Gram-Schmidt and geometric enclosure agree")


def four_pole_control():
    # Coefficient of 1/(8s+a) in s(s-1)/prod_{a in POLES}(8s+a).
    residues = {
        a: Fraction(a * (a + 8), 64 * prod(b - a for b in POLES if b != a))
        for a in POLES
    }
    mutation = {a - 1: coefficient for a, coefficient in residues.items()}
    assert sum(residues.values()) == 0
    assert all(residues.values())
    quotient = [sum(mutation.get(k, 0) for k in range(j + 1)) for j in range(5)]
    assert coefficient_norm(quotient) < 1
    assert all(SOURCE[a - 1] + residues[a] for a in POLES)
    assert [mellin(mutation, n) for n in range(2)] == [0, 0]
    assert mellin(mutation, 2) > 0
    print(f"same-four-pole two-sample control: residues {list(residues.values())}")


def add_term(polynomial, exponent, coefficient):
    polynomial[exponent] = polynomial.get(exponent, Fraction()) + coefficient


def terminating_alias(n, m):
    assert m >= 6
    degree = n + 1
    moments = [
        endpoint_moment(m, k) - endpoint_moment(m, k + 1) / 16
        for k in range(2 * degree + 1)
    ]
    basis = orthogonal_basis(degree, moments)
    horizon = max(1, (m + 7) // 8)
    while True:
        errors = [mellin(SOURCE, horizon + k) / 16**horizon for k in range(n + 1)]
        correction = [Fraction(0)] * degree
        for q, norm in basis[:-1]:
            projection = sum(a * errors[i] for i, a in enumerate(q)) / norm
            for i, a in enumerate(q):
                correction[i] += projection * a
        if coefficient_norm(correction) <= 1:
            break
        horizon += 1

    quotient = {
        exponent + 8 * j: Fraction(a, 16**j)
        for exponent, a in SOURCE.items() for j in range(horizon)
    }
    for k, a in enumerate(correction):
        add_term(quotient, m + 8 * k, a)
        add_term(quotient, m + 8 * k + 1, -a)
    center = mellin(quotient, 0)
    q, norm = basis[-1]
    response = sum(a * endpoint_moment(m, k) for k, a in enumerate(q))
    assert norm > 0 and response > 0
    radius = response / (2 * coefficient_norm(q))
    scale = 2
    while Fraction(1, scale) >= radius:
        scale *= 2
    target = Fraction(center * scale // 1 + 1, scale)
    eta = (target - center) / response
    assert 0 < eta * coefficient_norm(q) < Fraction(1, 2)

    for k, a in enumerate(q):
        add_term(quotient, m + 8 * k, eta * a)
        add_term(quotient, m + 8 * k + 1, -eta * a)
    mutant = {}
    for exponent, a in quotient.items():
        add_term(mutant, exponent, a)
        add_term(mutant, exponent + 8, -a / 16)

    assert all(mutant.get(j, 0) == SOURCE.get(j, 0) for j in range(m))
    assert sum(mutant.values()) == 0
    assert all(mellin(mutant, k) == mellin(SOURCE, k) for k in range(n + 1))
    assert mellin(quotient, 0) == target
    assert target.denominator & (target.denominator - 1) == 0
    bits = target.denominator.bit_length() - 1
    first_constant = 1 + (bits + 3) // 4
    assert (16**(first_constant - 1) * target).denominator == 1
    support = sum(a != 0 for a in mutant.values())
    assert support > len(POLES)
    print(
        f"terminating alias N={n}, low jet <{m}: L={horizon}, "
        f"{support} poles, dyadic denominator 2^{bits}, phase 1 for n>={first_constant}"
    )


if __name__ == "__main__":
    for n in (0, 9, 12, 16):
        ordinary_alias(n)
    four_pole_control()
    for n, m in ((0, 6), (4, 15), (9, 24), (12, 41), (16, 64)):
        terminating_alias(n, m)
