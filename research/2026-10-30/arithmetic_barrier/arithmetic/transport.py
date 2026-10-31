"""Exact additive research instruments; proofs are in ARITHMETIC_THEOREMS.md.

No imports from the parent stroboscope or production code. These functions
measure rational p-adic data, never distribution of the selected real circle.
"""
from fractions import Fraction as F
from math import isqrt

OFFSETS = (1, 4, 5, 6)
REFLECTED = (2, 3, 4, 7)
BBP = (F(4), F(-2), F(-1), F(-1))


def prime(p):
    return isinstance(p, int) and p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def rational_mod(x, m):
    x = F(x)
    if m < 2:
        raise ValueError("modulus >=2 required")
    try:
        return x.numerator * pow(x.denominator, -1, m) % m
    except ValueError as exc:
        raise ValueError("rational denominator is not a unit") from exc


def source(n, coefficients=BBP, offsets=OFFSETS):
    if n < 1 or len(coefficients) != len(offsets):
        raise ValueError("positive time and matching channels required")
    return sum((F(c) / (8 * (n - 1) + s) for s, c in zip(offsets, coefficients)), F())


def prefix(n, coefficients=BBP, offsets=OFFSETS, seed=F()):
    if n < 0:
        raise ValueError("nonnegative time required")
    u = F(seed)
    for j in range(1, n + 1):
        u = 16 * u + source(j, coefficients, offsets)
    return u


def valuation_integer(n, p):
    if n == 0:
        raise ValueError("zero has infinite valuation")
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def valuation(x, p):
    x = F(x)
    if not prime(p):
        raise ValueError("prime required")
    return valuation_integer(x.numerator, p) - valuation_integer(x.denominator, p)


def clock(p, a, k):
    if not prime(p) or p == 2 or a < 1 or k < 1:
        raise ValueError("odd prime and positive exponent/clock required")
    Q = p ** a
    qmax = 8 * k - (2 if Q % 4 == 1 else 1)
    if p <= qmax:
        raise ValueError("p must exceed last condensed denominator")
    last = Q * qmax % 8
    assert last in OFFSETS
    N = (Q * qmax + 8 - last) // 8
    assert 8 * N - 2 < p * Q
    return N


def shadow(p, a, coefficients=BBP):
    A, B, C, D = map(F, coefficients)
    for c in (A, B, C, D):
        rational_mod(c, p)
    cls = p ** a % 8
    if cls == 1:
        return OFFSETS, (A, B, C, D)
    if cls == 5:
        return OFFSETS, (-4 * C, B, -A / 4, D)
    if cls == 3:
        return REFLECTED, (-8 * D, A, -2 * B, C)
    return REFLECTED, (32 * D, 16 * C, 8 * B, A)


def shadow_prefix(p, a, k, coefficients=BBP):
    clock(p, a, k)
    offsets, weights = shadow(p, a, coefficients)
    return prefix(k, weights, offsets)


def layer_residue(p, a, k, precision=1, coefficients=BBP, seed=F()):
    """Sum only the denominator valuation layers visible modulo p^precision."""
    if precision < 1:
        raise ValueError("positive precision required")
    N = clock(p, a, k)
    modulus = p ** precision
    answer = rational_mod(p ** a * F(seed), modulus) * pow(16, N, modulus)
    for n in range(1, N + 1):
        factor = pow(16, N - n, modulus)
        for s, c in zip(OFFSETS, coefficients):
            denominator = 8 * (n - 1) + s
            v = valuation_integer(denominator, p)
            assert v <= a
            if a - v < precision:
                unit = denominator // p ** v
                answer += factor * p ** (a - v) * rational_mod(F(c) / unit, modulus)
    return answer % modulus


def half_fermat_quotient(p):
    if not prime(p) or p == 2:
        raise ValueError("odd prime required")
    chi = 1 if p % 8 in (1, 7) else -1
    return (chi * pow(2, (p - 1) // 2) - 1) // p


def next_layer(p, a, k, coefficients=BBP):
    """The unit-denominator remainder at a=1, next valuation layer at a>1."""
    N = clock(p, a, k)
    result = 0
    for n in range(1, N + 1):
        for s, c in zip(OFFSETS, coefficients):
            denominator = 8 * (n - 1) + s
            if valuation_integer(denominator, p) == a - 1:
                unit = denominator // p ** (a - 1)
                result += pow(16, N - n, p) * rational_mod(F(c) / unit, p)
    return result % p


def first_lift(p, a, k, coefficients=BBP):
    """Predicted p^a U_clock modulo p², retaining both exact corrections."""
    offsets, weights = shadow(p, a, coefficients)
    V = shadow_prefix(p, a, k, coefficients)
    qmax = 8 * k - (2 if p ** a % 4 == 1 else 1)
    derivative = qmax * V - sum(weights) * F(16 ** k - 1, 15)
    remainder = next_layer(p, a, k, coefficients)
    return (rational_mod(V, p * p) + p * (
        half_fermat_quotient(p) * rational_mod(derivative, p) + remainder
    )) % (p * p)


def power_birth(p, a):
    """First denominator divisible by p^a, including exceptional primes 3 and 5."""
    if not prime(p) or p == 2 or a < 1:
        raise ValueError("odd prime and positive exponent required")
    Q = p ** a
    if Q % 8 == 1:
        return (Q + 7) // 8, F(4)
    if Q % 8 == 5:
        return (Q + 3) // 8, F(-1)
    return (Q + 1) // 4, F(-1, 2)


def packet(p):
    """Four first-layer encounter times and their authentic predicted residues."""
    if not prime(p) or p <= 7:
        raise ValueError("prime >7 required for this full packet")
    cls = p % 8
    qs = OFFSETS if cls in (1, 5) else REFLECTED
    times = tuple((p * q + 8 - (p * q % 8)) // 8 for q in qs)
    values = {
        1: (F(4), F(7, 2), F(33, 10), F(47, 15)),
        5: (F(-1), F(7, 2), F(-66, 5), F(47, 15)),
        3: (F(-1, 2), F(16, 3), F(-19, 6), F(130, 21)),
        7: (F(-1, 2), F(-4, 3), F(-19, 6), F(-520, 21)),
    }[cls]
    return times, tuple(rational_mod(x, p) for x in values)
