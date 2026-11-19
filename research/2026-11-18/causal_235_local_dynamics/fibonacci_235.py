"""Exact auxiliary Fibonacci/BBP-mask calculations; no orbit-mixing claims.

All matrices act on column vectors. Polynomial observation coordinates are
unscaled monomials, ordered by increasing exponent of the second variable.
Only Python's standard library is used.
"""

from fractions import Fraction
from math import comb


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def multiply(a, b):
    if len(a[0]) != len(b):
        raise ValueError("incompatible matrix shapes")
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) for col in zip(*b))
                 for row in a)


def subtract(a, b):
    return tuple(tuple(x-y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def power(a, n, modulus=None):
    if n < 0:
        raise ValueError("only forward powers are implemented")
    result = identity(len(a))
    while n:
        if n & 1:
            result = multiply(result, a)
            if modulus:
                result = tuple(tuple(x % modulus for x in row) for row in result)
        a = multiply(a, a)
        if modulus:
            a = tuple(tuple(x % modulus for x in row) for row in a)
        n //= 2
    return result


def determinant(a):
    """Exact independent elimination, not an eigenvalue formula."""
    b = [list(map(Fraction, row)) for row in a]
    value = Fraction(1)
    for j in range(len(b)):
        pivot = next((i for i in range(j, len(b)) if b[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            b[j], b[pivot] = b[pivot], b[j]
            value = -value
        v = b[j][j]
        value *= v
        for i in range(j+1, len(b)):
            q = b[i][j] / v
            for k in range(j+1, len(b)):
                b[i][k] -= q*b[j][k]
            b[i][j] = 0
    return value


def symmetric_power_2(a, degree):
    """Map monomials of (a00*x+a01*y, a10*x+a11*y)."""
    if len(a) != 2 or len(a[0]) != 2 or degree < 0:
        raise ValueError("requires a 2x2 matrix and nonnegative degree")
    rows = []
    for j in range(degree+1):
        row = [0]*(degree+1)
        for k in range(degree-j+1):
            for ell in range(j+1):
                row[k+ell] += (comb(degree-j, k)*comb(j, ell)
                              * a[0][0]**(degree-j-k)*a[0][1]**k
                              * a[1][0]**(j-ell)*a[1][1]**ell)
        rows.append(tuple(row))
    return tuple(rows)


def symmetric_square(a):
    """Symmetric square of any square matrix, coordinates x_i*x_j (i<=j)."""
    n = len(a)
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    return tuple(tuple(a[i][k]*a[j][ell]
                       + (a[i][ell]*a[j][k] if k != ell else 0)
                       for k, ell in pairs) for i, j in pairs)


def monomials(x, y, degree):
    return tuple((x**(degree-j)*y**j,) for j in range(degree+1))


def fibonacci(n):
    if n < 0:
        raise ValueError("nonnegative index required")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def valuation(n, prime):
    if n == 0:
        raise ValueError("valuation of zero is infinite")
    n = abs(n)
    k = 0
    while n % prime == 0:
        n //= prime
        k += 1
    return k


def matrix_valuation(a, prime):
    return min(valuation(x, prime) for row in a for x in row if x)


def polynomial(a, coefficients):
    result = tuple(tuple(0 for _ in row) for row in a)
    for c in reversed(coefficients):
        result = multiply(result, a)
        result = tuple(tuple(x+c*int(i == j) for j, x in enumerate(row))
                       for i, row in enumerate(result))
    return result


def mean_zero_restriction(a):
    """Basis e_0-e_4,...,e_3-e_4 for the sum-zero subspace."""
    col_sums = [sum(row[j] for row in a) for j in range(5)]
    if len(set(col_sums)) != 1:
        raise ValueError("matrix does not preserve the sum-zero subspace")
    return tuple(tuple(a[i][j]-a[i][4] for j in range(4)) for i in range(4))


A = ((1, 1), (1, 0))
M = ((0, 1), (1, -1))
B = power(A, 2)
S2 = symmetric_power_2(A, 2)
S4 = symmetric_power_2(A, 4)
T = symmetric_power_2(B, 4)
S6 = symmetric_square(S2)
J = ((1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0),
     (0, 0, 1, 0, 0), (0, 0, 0, 1, 0), (0, 0, 0, 0, 1))
L = ((0, 0, 1, -1, 0, 0),)
W = ((4,), (-2,), (0,), (-1,), (2,), (4,))
P = ((1, 0, -4, 4, 0, 0), (0, 1, 2, -2, 0, 0),
     (0, 0, 1, 0, 0, 0), (0, 0, -2, 2, 1, 0),
     (0, 0, -4, 4, 0, 1))
R = tuple(tuple(int(i == (j+1) % 5) for j in range(5)) for i in range(5))
H = (4, 4, 4, 2, 1)


def source_norms(stride, depth, mask=H):
    if stride < 1 or depth < 0:
        raise ValueError("positive stride and nonnegative depth required")
    fm = power(subtract(identity(2), power(M, 8*stride)), depth)
    fr = power(subtract(identity(5), power(R, 8*stride)), depth)
    nf = determinant(multiply(polynomial(M, mask), fm))
    n5 = determinant(mean_zero_restriction(multiply(polynomial(R, mask), fr)))
    return nf, n5


def forcing(n):
    if n < 1:
        raise ValueError("BBP source clocks start at one")
    return (Fraction(4, 8*n-7)-Fraction(2, 8*n-4)
            -Fraction(1, 8*n-3)-Fraction(1, 8*n-2))


def forward_null(n, stride, depth):
    return sum((-1)**j*comb(depth, j)*forcing(n+stride*j)
               for j in range(depth+1))


def delayed_null(t, stride, depth):
    if t-stride*depth < 1:
        raise ValueError("the observed history is too short")
    return (-1)**depth*sum((-1)**j*comb(depth, j)*forcing(t-stride*j)
                           for j in range(depth+1))
