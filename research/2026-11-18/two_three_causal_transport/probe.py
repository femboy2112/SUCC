"""Exact certificates for BBP source filters and causal local-place transport.

All certificates use integers/Fraction. No pi digit table, numerical phase,
normality assumption, or nontrivial zeta zero is an input.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import gcd
import json

H = (4, 4, 4, 2, 1)
Q = (4, 0, 0, -2, -1, -1)
K = (4, -4, 0, 2, -1)
INVERSES = {
    3: (45, (16, -14, 1), (-19, -8, -12, 1)),
    5: (825, (206, -199, -4, 116, -64), (1, -28, -12, -64)),
}


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def cyclic_matrix(coefficients, m):
    if m < 1:
        raise ValueError("cycle length must be positive")
    a = [[0] * m for _ in range(m)]
    for j in range(m):
        for k, c in enumerate(coefficients):
            a[(j + k) % m][j] += c
    return a


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def causal_matrix(coefficients, n):
    if n < 1:
        raise ValueError("record length must be positive")
    return [[coefficients[i-j] if 0 <= i-j < len(coefficients) else 0
             for j in range(n)] for i in range(n)]


def causal_inverse_coefficients(n):
    out = [Fraction(0)] * n
    for j in range((n-1)//8+1):
        for k, c in enumerate(K):
            if 8*j+k < n:
                out[8*j+k] = Fraction(c, 16**(j+1))
    return out


def block_complement(blocks):
    if blocks < 1:
        raise ValueError("positive block count required")
    out = [0] * (8*blocks-3)
    for j in range(blocks):
        for k, c in enumerate(K):
            out[8*j+k] = 16**(blocks-1-j)*c
    return tuple(out)


def ternary_height_certificate(n):
    """The compact four-stratum version of inherited T1; see paper proof."""
    if n < 1:
        raise ValueError("positive source time required")
    if n == 1:
        return 3, 3, 3, 1  # denominator height, scale, modulus, residue
    q = 9
    while n >= (9*q+7)//8:
        q *= 9
    if n < (q+1)//2:
        return q, q, 3, 1
    if n < (5*q+3)//8:
        return q, q, 3, 2
    if n < (3*q+1)//4:
        return q//3, q, 9, 6
    return 3*q, 3*q, 3, 1


def determinant(a):
    """Fraction Gaussian elimination, separate from the resultant formula."""
    a = [[Fraction(x) for x in row] for row in a]
    d = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            d = -d
        d *= a[j][j]
        for i in range(j + 1, len(a)):
            factor = a[i][j] / a[j][j]
            for k in range(j + 1, len(a)):
                a[i][k] -= factor * a[j][k]
            a[i][j] = 0
    assert d.denominator == 1
    return d.numerator


def cyclic_determinant_formula(m):
    if m < 1:
        raise ValueError("cycle length must be positive")
    # L_m = (-1+i)^m + (-1-i)^m, computed without complex roundoff.
    prev, cur = 2, -2
    for _ in range(2, m + 1):
        prev, cur = cur, -2 * cur - 2 * prev
    a = 2**m + 1 if m % 2 else (2**(m // 2) - (-1)**(m // 2))**2
    return a * (2**m + 1 - cur)


def vp_integer(n, p):
    if n == 0:
        raise ValueError("zero has infinite valuation")
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp(x, p):
    x = Fraction(x)
    return vp_integer(x.numerator, p) - vp_integer(x.denominator, p)


def local_norm(x, p):
    if x == 0:
        return Fraction(0)
    v = vp(x, p)
    return Fraction(1, p**v) if v >= 0 else Fraction(p**(-v))


def residue(x, modulus):
    x = Fraction(x)
    if gcd(x.denominator, modulus) != 1:
        raise ValueError("rational is not integral at this modulus")
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def forcing(n):
    if n < 1:
        raise ValueError("the authenticated real timeline starts at n=1")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def moment(poly, exponent):
    if exponent < 0:
        raise ValueError("nonnegative reciprocal-moment exponent required")
    return sum((Fraction(c, exponent+j+1) for j, c in enumerate(poly)), Fraction())


def bbp_states(nmax):
    out = [Fraction(0)]
    for n in range(1, nmax + 1):
        out.append(16 * out[-1] + forcing(n))
    return out


def recent_window(n, length):
    if not 0 <= length <= n:
        raise ValueError("window must lie inside the observed history")
    out = Fraction(0)
    for j in range(n-length+1, n+1):
        out = 16*out + forcing(j)
    return out


def word_realizer(word):
    """Least positive odd representative of the prescribed valuation cylinder."""
    if not word or any(a < 1 for a in word):
        raise ValueError("nonempty positive valuation word required")
    total, offset = 0, 0
    for a in word:
        offset = 3*offset + 2**total
        total += a
    modulus = 2**(total+1)
    start = (2**total-offset)*pow(3**len(word), -1, modulus) % modulus
    assert start > 0 and start % 2
    return start, modulus


def syracuse_trace(start, length):
    if start < 1 or start % 2 == 0:
        raise ValueError("positive odd starting integer required")
    states, word = [start], []
    for _ in range(length):
        numerator = 3*states[-1]+1
        a = vp_integer(numerator, 2)
        word.append(a)
        states.append(numerator // 2**a)
    return tuple(states), tuple(word)


def terminal_ternary(word, depth):
    if not 1 <= depth <= len(word):
        raise ValueError("terminal depth must not exceed observed word length")
    modulus, total, out = 3**depth, 0, 0
    for i, a in enumerate(reversed(word[-depth:])):
        total += a
        out += 3**i * pow(pow(2, total, modulus), -1, modulus)
    return out % modulus


def finite_certificate():
    assert poly_mul((1, -1), H) == Q
    cycles = {}
    for m in (1, 2, 3, 5, 6, 10, 15, 17, 19):
        d = determinant(cyclic_matrix(H, m))
        assert d == cyclic_determinant_formula(m) and d % 2
        cycles[str(m)] = d
    for m, (d, g, j) in INVERSES.items():
        actual = list(poly_mul(H, g))
        actual[0] -= d
        target = poly_mul((-1,) + (0,)*(m-1) + (1,), j)
        assert tuple(actual) == target
        prod = matmul(cyclic_matrix(H, m), cyclic_matrix(g, m))
        assert prod == [[d*int(i == k) for k in range(m)] for i in range(m)]
        assert gcd(*g) == 1  # primitive adjugate: all but last Smith factor are 1
    states = bbp_states(768)
    source_checks = 0
    for n in range(1, len(states)):
        assert forcing(n) == moment(Q, 8*n-8)
        assert states[n].denominator % 2
        assert local_norm(states[n], 3) >= 3
        if n >= 11:
            q = 1
            while 3*q <= 8*n:
                q *= 3
            d3 = local_norm(states[n], 3)
            assert Fraction(q, 9) <= d3 <= q
            assert d3 > Fraction(8*n, 27)
        source_checks += 1
    window_checks = 0
    for n in (32, 64, 128, 256, 512, 768):
        for length in sorted({0, 1, 2, 4, 8, n//2, n-1, n}):
            err = states[n]-recent_window(n, length)
            assert err == 16**length*states[n-length]
            assert local_norm(err, 2) <= Fraction(1, 16**length)
            if length < n:
                assert local_norm(err, 3) == local_norm(states[n-length], 3) >= 3
            window_checks += 1
    words = memories = 0
    for length in range(1, 7):
        for word in product(range(1, 5), repeat=length):
            start, modulus = word_realizer(word)
            trace, observed = syracuse_trace(start, length)
            assert observed == word
            for depth in range(1, length+1):
                assert trace[-1] % 3**depth == terminal_ternary(word, depth)
                memories += 1
            assert syracuse_trace(start+modulus, length)[1] == word
            words += 1
    sharpness = 0
    for depth in range(1, 31):
        w1 = (1,)*depth
        w2 = (2,)+(1,)*(depth-1)
        diff = (terminal_ternary(w1, depth)-terminal_ternary(w2, depth)) % 3**depth
        assert vp_integer(diff, 3) == depth-1
        sharpness += 1
    return {
        "scope": "VERIFIED_FINITE; no asymptotic normality or Collatz conclusion",
        "cyclic_determinants": cycles,
        "inverse_polynomial_certificates": 2,
        "original_source_indices": source_checks,
        "causal_windows": window_checks,
        "positive_odd_valuation_words": words,
        "terminal_memory_identities": memories,
        "memory_depth_sharpness_cases": sharpness,
        "controls": {
            "ordered_words": {"11": list(syracuse_trace(11, 2)[0]),
                              "9": list(syracuse_trace(9, 2)[0])},
            "quotient_loss_at_n1": str(Fraction(5, (8-7)*(8-2))),
            "rejected_odd_k_formula_is_nonintegral": (3**3+3) % 8 != 0,
        },
    }


if __name__ == "__main__":
    print(json.dumps(finite_certificate(), indent=2, sort_keys=True))
