"""Exact finite-field residue quotient and source-prime selector.

No phase approximation enters selection, polynomial reduction, or resonance
classification. Exponential-sum inequalities are paper theorems with declared
classical imports; this module does not turn numerical tests into proofs.
"""
from functools import lru_cache
from math import isqrt


def _int(value, name, minimum=None):
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError(f'{name} must be an exact integer >= {minimum}')
    return value


@lru_cache(maxsize=None)
def is_prime(p):
    _int(p, 'p', 2)
    return all(p % d for d in range(2, isqrt(p) + 1))


def _prime(p):
    if not is_prime(p):
        raise ValueError('prime modulus required')
    return p


def factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


@lru_cache(maxsize=None)
def order16(p):
    _prime(p)
    if p == 2:
        raise ValueError('odd prime required')
    m = p - 1
    for q in factors(p - 1):
        while m % q == 0 and pow(16, m // q, p) == 1:
            m //= q
    return m


def eligible(p):
    _int(p, 'p', 2)
    if p % 8 != 1 or not is_prime(p):
        return False
    return order16(p) ** 2 > p * 4 ** isqrt(p.bit_length())


def select_prime(A):
    _int(A, 'A', 1)
    start = 4 * A - ((4 * A - 1) % 8)
    for p in range(start, 16, -8):
        if eligible(p):
            return p
    return None


def normalize(coefficients, p):
    _prime(p)
    if not isinstance(coefficients, (tuple, list)) or not coefficients:
        raise ValueError('nonempty coefficient list required')
    values = [_int(x, 'coefficient') % p for x in coefficients]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def evaluate(coefficients, x, p):
    values = normalize(coefficients, p)
    _int(x, 'x')
    result = 0
    for coefficient in reversed(values):
        result = (result * x + coefficient) % p
    return result


def reduce_on_clock(coefficients, p, xi):
    """Remainder modulo X**m-xi**m; low-degree coefficient first."""
    values = normalize(coefficients, p)
    _int(xi, 'xi')
    xi %= p
    if not xi:
        raise ValueError('nonzero coset anchor required')
    m = order16(p)
    c = pow(xi, m, p)
    out = [0] * m
    for exponent, coefficient in enumerate(values):
        quotient, remainder = divmod(exponent, m)
        out[remainder] = (out[remainder] + coefficient * pow(c, quotient, p)) % p
    return normalize(out, p)


def classify(complement, p, xi, h=1):
    """Classify hX+P on the actual source coset, retaining constant phases."""
    _int(h, 'h')
    combined = normalize(complement, p)
    if len(combined) < 2:
        combined.append(0)
    combined[1] += h
    remainder = reduce_on_clock(combined, p, xi)
    D = len(remainder) - 1
    m = order16(p)
    return {'p': p, 'm': m, 'xi': xi % p, 'h': h,
            'remainder': remainder, 'degree': D, 'resonant': D == 0,
            'constant_phase_numerator': remainder[0] if D == 0 else None,
            'bound_squared_numerator': min(m * m, D * D * p) if D else m * m,
            'bound_squared_denominator': m * m}


def source_xi(p):
    _prime(p)
    if p % 8 != 1:
        raise ValueError('split source prime p=1 mod8 required')
    L = (p - 1) // 4
    return 4 * pow(16, L + 1 - (p + 7) // 8, p) % p


def clock(p, xi):
    _prime(p)
    _int(xi, 'xi')
    if not xi % p:
        raise ValueError('nonzero coset anchor required')
    m = order16(p)
    result = []
    x = xi % p
    for _ in range(m):
        result.append(x)
        x = x * 16 % p
    assert len(set(result)) == m and x == xi % p
    return result
