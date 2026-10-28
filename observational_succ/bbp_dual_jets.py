"""Exact dual-number probes for SUCC's original four-pole BBP source.

This is a rational, finite, source-authenticated instrument. It makes no
normality, asymptotic Weyl, RH, or numerical floating-point claim.
Research proof: research/2026-10-27/BBP_DUAL_JET_SOURCE_RIGIDITY.md.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
from math import factorial

TOTAL = (Q(4), Q(0), Q(0), Q(-2), Q(-1), Q(-1), Q(0), Q(0))
PLUS = (Q(4), Q(2), Q(0), Q(-1), Q(-1), Q(-1, 2), Q(0), Q(1, 4))
MINUS = (Q(0), Q(-2), Q(0), Q(-1), Q(0), Q(-1, 2), Q(0), Q(-1, 4))
A = (16, -89, 120)
D = (21, -206, 712, -1024, 512)
W = (1427, -17744, 87800, -215040, 259584, -122880)
EXTRA_CRITICAL_PRIME = 52497217
EXTRA_CRITICAL_ROOT = 22168154


@dataclass(frozen=True)
class Dual:
    value: Q
    tangent: Q = Q(0)

    def __post_init__(self):
        object.__setattr__(self, 'value', Q(self.value))
        object.__setattr__(self, 'tangent', Q(self.tangent))

    def __add__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.value + other.value, self.tangent + other.tangent)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, -self.tangent)

    def __sub__(self, other):
        return self + -(other if isinstance(other, Dual) else Dual(other))

    def __mul__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.value * other.value,
                    self.value * other.tangent + self.tangent * other.value)

    __rmul__ = __mul__

    def inverse(self):
        if self.value == 0:
            raise ZeroDivisionError('dual element has non-unit real part')
        return Dual(1 / self.value, -self.tangent / (self.value * self.value))

    def __truediv__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return self * other.inverse()


def evaluate(coeffs, x):
    acc = 0
    for c in reversed(coeffs):
        acc = acc * x + c
    return acc


def derivative(coeffs):
    return tuple(k * coeffs[k] for k in range(1, len(coeffs)))


def multiply_polynomials(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
    return tuple(out)


def source_jet(n, taps=TOTAL):
    """Literal Mellin four-pole time shift n -> n + epsilon, not digit shift."""
    if type(n) is not int or not 1 <= n <= 100_000:
        raise ValueError('positive integer BBP time required')
    if len(taps) != 8:
        raise ValueError('eight authenticated first-shell taps required')
    return sum((Dual(c) / Dual(8 * (n - 1) + j + 1, 8)
                for j, c in enumerate(taps)), Dual(0))


def source_rational_jet(n):
    """Independent A/D rational representation of the original time source."""
    if type(n) is not int or n < 1:
        raise ValueError('positive integer required')
    den = evaluate(D, n)
    return Dual(Q(evaluate(A, n), den),
                Q(evaluate(W, n), den * den))


def endpoint_jet(taps=TOTAL):
    """P(1+epsilon): mass and first endpoint moment of a Mellin shell."""
    return evaluate(taps, Dual(1, 1))


def bareiss_determinant(data):
    """Exact integer determinant; no external symbolic algebra dependency."""
    n = len(data)
    if not n or any(len(row) != n for row in data):
        raise ValueError('nonempty square matrix required')
    a = [list(map(int, row)) for row in data]
    prev, sign = 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                val, rem = divmod(num, prev)
                if rem:
                    raise ArithmeticError('Bareiss exact division failed')
                a[i][j] = val
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def resultant(a, b):
    """Sylvester determinant of two integer polynomials in ascending order."""
    n, m = len(a) - 1, len(b) - 1
    if n < 1 or m < 1 or not a[-1] or not b[-1]:
        raise ValueError('positive-degree polynomials required')
    rows = []
    for i in range(m):
        rows.append([0] * i + list(reversed(a)) + [0] * (m - i - 1))
    for i in range(n):
        rows.append([0] * i + list(reversed(b)) + [0] * (n - i - 1))
    return bareiss_determinant(rows)


def discriminant(a):
    n = len(a) - 1
    if n < 2:
        raise ValueError('degree >= 2 required')
    num = (-1) ** (n * (n - 1) // 2) * resultant(a, derivative(a))
    val, rem = divmod(num, a[-1])
    if rem:
        raise ArithmeticError('discriminant must be integral')
    return val


def field_taylor(coeff_a, coeff_d, x, p, order=3):
    """Hasse/Taylor coefficients for A(x+t)/D(x+t) over F_p.

    Requires D(x) nonzero modulo p; works at derivative-critical classes.
    """
    if (type(p) is not int or type(x) is not int or type(order) is not int
            or not 0 <= order < p):
        raise ValueError('integer residue and 0 <= Taylor order < prime modulus required')
    aa, dd = [], []
    for cs, out in ((coeff_a, aa), (coeff_d, dd)):
        remaining = tuple(cs)
        for _ in range(order + 1):
            out.append(evaluate(remaining, x) % p if remaining else 0)
            remaining = derivative(remaining)
        # Divide by k! to obtain the Hasse/Taylor coefficient.
    aa = [(v * pow(factorial(k), -1, p)) % p for k, v in enumerate(aa)]
    dd = [(v * pow(factorial(k), -1, p)) % p for k, v in enumerate(dd)]
    if not dd[0]:
        raise ZeroDivisionError('pole modulo p: tangent undefined')
    inv = pow(dd[0], -1, p)
    out = []
    for k in range(order + 1):
        out.append(((aa[k] - sum(dd[j] * out[k-j]
                                   for j in range(1, k + 1))) * inv) % p)
    return tuple(out)


# This is the exact 4D rational matrix from PR #333 (even Gaussian, odd twist).
T = ((Q(1, 2), Q(-1, 2), Q(0), Q(0)),
     (Q(1, 2), Q(1, 2), Q(0), Q(0)),
     (Q(0), Q(0), Q(0), Q(1)),
     (Q(0), Q(0), Q(1, 2), Q(0)))
B = (Q(1), Q(0), Q(1), Q(0))
L = (Q(4), Q(0), Q(0), Q(-4))


def matmul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def identity(d=4):
    return tuple(tuple(Q(int(i == j)) for j in range(d)) for i in range(d))


def matrix_powers(n=8):
    powers = [identity()]
    for _ in range(n):
        powers.append(matmul(powers[-1], T))
    return powers


def matrix_rank(rows):
    a = [[Q(v) for v in row] for row in rows]
    if not a:
        return 0
    n, m, k = len(a), len(a[0]), 0
    for j in range(m):
        i = next((r for r in range(k, n) if a[r][j]), None)
        if i is None:
            continue
        a[k], a[i] = a[i], a[k]
        z = a[k][j]
        a[k] = [t / z for t in a[k]]
        for r in range(n):
            if r != k and a[r][j]:
                z = a[r][j]
                a[r] = [v - z * w for v, w in zip(a[r], a[k])]
        k += 1
        if k == n:
            break
    return k


def tangent_jacobian_ranks():
    """(8th-return Jacobian rank, 3 tap Jacobian rank, combined rank)."""
    powers = matrix_powers(8)
    holo_cols, tap_cols = [], []
    for i, j in product(range(4), repeat=2):
        perturb = tuple(tuple(Q(int(a == i and b == j))
                              for b in range(4)) for a in range(4))
        h = [[Q(0)] * 4 for _ in range(4)]
        for k in range(8):
            v = matmul(matmul(powers[7-k], perturb), powers[k])
            for a in range(4):
                for b in range(4):
                    h[a][b] += v[a][b]
        holo_cols.append([v for row in h for v in row])
        dtaps = []
        for m in range(1, 4):
            # Literal Leibniz expansion of L*T^m*B (input B, output L).
            dtaps.append(sum((matmul(
                matmul(matmul(matmul((L,), powers[m-1-k]), perturb), powers[k]),
                tuple((x,) for x in B))[0][0] for k in range(m)), Q(0)))
        tap_cols.append(dtaps)
    hr = [[holo_cols[i][j] for i in range(16)] for j in range(16)]
    sr = [[tap_cols[i][j] for i in range(16)] for j in range(3)]
    return matrix_rank(hr), matrix_rank(sr), matrix_rank(hr + sr)


def gain_dual_prefix(n):
    """16+epsilon recurrence with authentic, parameter-independent source."""
    if type(n) is not int or not 0 <= n <= 128:
        raise ValueError('finite time horizon 0..128 required')
    state = Dual(0)
    for k in range(1, n + 1):
        state = Dual(16, 1) * state + Dual(source_jet(k).value)
    return state
