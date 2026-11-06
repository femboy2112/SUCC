"""Exact finite source reflection, coefficient recovery, and signed Euler tape.

Run directly to reproduce the JSON receipt. No phase or zero oracle is used.
"""
from fractions import Fraction as Q
from math import comb, isqrt
import json


def primal_taps():
    original = (4, 0, 0, -2, -1, -1, 0, 0)
    transformed = []
    for ell in range(1, 9):
        j = (3 * ell - 1) % 8 + 1
        transformed.append((-1) ** (8 - ell) * Q(2) ** ((j - ell) // 2)
                           * original[j - 1])
    return tuple((a - b) / 2 for a, b in zip(original, transformed))


def reflected_coefficients(blocks, degree):
    """Integer numerators over 16^blocks, by truncated polynomial composition."""
    if blocks < 1 or degree < 0:
        raise ValueError("positive block count and nonnegative degree required")
    taps = primal_taps()
    result = [0] * (degree + 1)
    for k in reversed(range(blocks)):
        scale = 16 ** (blocks - k)
        for tap in reversed(taps):
            constant = tap * scale / 4
            assert constant.denominator == 1
            for j in range(degree, 0, -1):
                result[j] -= result[j - 1]
            result[0] += int(constant)
    return result


def error_numerators(blocks, degree):
    """Numerators of [x^ell](1-x)^(8N)/(1+x²), via short recurrence."""
    err = []
    for ell in range(degree + 1):
        numerator = (-1) ** ell * comb(8 * blocks, ell)
        err.append(numerator - (err[ell - 2] if ell >= 2 else 0))
    return err


def character(n):
    return (0, 1, 0, -1)[n % 4]


def log_derivative_tape(coefficients):
    """Exp of Dirichlet logarithmic derivative coefficients, no primality input."""
    if not coefficients or coefficients[0] != 1:
        raise ValueError("need a normalized coefficient sequence")
    nmax = len(coefficients)
    tape = [Q(1)] + [Q(n) ** coefficients[n - 1] for n in range(1, nmax + 1)]
    for n in range(2, nmax + 1):
        for multiple in range(2 * n, nmax + 1, n):
            tape[multiple] /= tape[n] ** coefficients[multiple // n - 1]
    return tape[1:]


def prime_power_oracle(nmax):
    tape = [Q(1)] * nmax
    for p in range(2, nmax + 1):
        if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
            continue
        power = p
        while power <= nmax:
            tape[power - 1] = Q(p) ** character(power)
            power *= p
    return tape


def receipt(blocks):
    degree = 2 * blocks
    scale = 16 ** blocks
    raw = reflected_coefficients(blocks, degree)
    errors = error_numerators(blocks, degree)
    assert all(raw[l] + errors[l] == scale * character(l + 1)
               for l in range(degree + 1))
    first = next(l for l, err in enumerate(errors) if 2 * abs(err) >= scale)
    assert all(2 * abs(errors[l]) < scale for l in range(4 * blocks // 5 + 1))
    hostile = 23 * blocks // 20
    assert 2 * abs(errors[hostile]) > scale
    integers = [(2 * integer + scale) // (2 * scale) for integer in raw[:first]]
    assert log_derivative_tape(integers) == prime_power_oracle(first)
    assert abs(primal_taps()[2] / 4 - character(3)) > Q(1, 2)  # wrong orientation
    assert abs(-Q(raw[0], scale) - character(1)) > Q(1, 2)  # reversed normalization
    return {"blocks": blocks, "first_degree_outside_strict_rounding": first,
            "exact_prefix_integer_coefficients": first, "hostile_degree": hostile,
            "last_good_error": str(Q(errors[first - 1], scale)),
            "first_bad_error": str(Q(errors[first], scale)),
            "euler_tape_matches_trial_factorization": True}


if __name__ == "__main__":
    print(json.dumps([receipt(n) for n in (29, 53, 101, 197)], indent=2))
