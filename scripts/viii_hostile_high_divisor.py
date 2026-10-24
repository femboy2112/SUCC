"""Exact finite oracles for Main VIII cofactor research, not proof authority.

No production arithmetic/counting routines are imported.  Rational powers are
enclosed by integer root comparisons; no floating-point result is certified.
"""
from fractions import Fraction
from itertools import product
from math import gcd, prod


def factor(n):
    if type(n) is not int or n < 1:
        raise ValueError('positive integer required')
    answer = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            answer[p] = answer.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        answer[n] = 1
    return answer


def powerful_divisors(n):
    options = [[1] + [p**j for j in range(2, k + 1)] for p, k in factor(n).items()]
    return sorted(prod(values) for values in product(*options))


def high_incidences(X, B=None):
    """Ordered primitive incidences, preserving every divisor selection."""
    if type(X) is not int or X < 2:
        raise ValueError('integer X>=2 required')
    for c in range(2, X + 1):
        for a in range(1, c):
            b = c - a
            if gcd(a, b) != 1:
                continue
            for d, e, f in product(powerful_divisors(a), powerful_divisors(b),
                                   powerful_divisors(c)):
                if d * e * f > X**2 and (B is None or min(d, e, f) <= B):
                    yield ((a, b, c), (d, e, f), (a // d, b // e, c // f))


def pythagorean_unit_cofactor(m):
    if type(m) is not int or m < 2 or m % 2:
        raise ValueError('even integer m>=2 required')
    roots = (m*m - 1, 2*m, m*m + 1)
    source = tuple(r*r for r in roots)
    return source, source, (1, 1, 1)


def integer_root(n, q):
    """Floor of n^(1/q), checked by integer powers."""
    low, high = 0, 1 << ((n.bit_length() + q - 1) // q)
    while high - low > 1:
        middle = (low + high) // 2
        if middle**q <= n:
            low = middle
        else:
            high = middle
    return high if high**q == n else low


def power_interval(n, exponent, bits=48):
    exponent = Fraction(exponent)
    if n < 1 or exponent < 0:
        raise ValueError('positive base and nonnegative exponent required')
    scale = 2**bits
    target = n**exponent.numerator * scale**exponent.denominator
    root = integer_root(target, exponent.denominator)
    return (Fraction(root, scale), Fraction(root if root**exponent.denominator == target
                                           else root + 1, scale))


def times(left, right):
    return left[0] * right[0], left[1] * right[1]


def plus(left, right):
    return left[0] + right[0], left[1] + right[1]


def g_interval(n, t):
    answer = (Fraction(1), Fraction(1))
    for p, k in factor(n).items():
        if k == 1:
            return Fraction(0), Fraction(0)
        pt = power_interval(p, t)
        answer = times(answer, times(power_interval(p, t * (k - 2)),
                                     (pt[0] - 1, pt[1] - 1)))
    return answer


def h_interval(n, t):
    answer = (Fraction(1), Fraction(1))
    for p, k in factor(n).items():
        if k < 3:
            return Fraction(0), Fraction(0)
        answer = times(answer, power_interval(p, t * (k - 1)))
    return answer


def g_at_one(n):
    answer = 1
    for p, k in factor(n).items():
        if k == 1:
            return 0
        answer *= p**(k - 2) * (p - 1)
    return answer


def finite_carrier_bound_intervals(Y, t):
    """Compare A_t(Y) with Y^alpha sum_{h<=Y} h_t(h)/h^alpha.

    This finite right side is below C_t Y^alpha, and is derived by the
    square-weight convolution proof. The return values are enclosures.
    """
    alpha = (1 + t) / 2
    actual = (Fraction(0), Fraction(0))
    finite_h = (Fraction(0), Fraction(0))
    for n in range(1, Y + 1):
        actual = plus(actual, g_interval(n, t))
        denominator = power_interval(n, alpha)
        finite_h = plus(finite_h, times(h_interval(n, t),
                                       (1 / denominator[1], 1 / denominator[0])))
    return actual, times(power_interval(Y, alpha), finite_h)
