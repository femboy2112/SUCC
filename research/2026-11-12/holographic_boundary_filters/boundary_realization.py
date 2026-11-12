"""Exact ordered boundary realization certificates over Gaussian rationals.

The mathematics is elementary cyclic realization and orthogonal projection.
The certificate concerns one authenticated, stationary linear filter family.
It does not authenticate measured data, identify an invisible direct summand,
or turn a finite observation into an arithmetic asymptotic theorem.

Words are chronological: ("x", "y") applies x first, then y, hence Y X.
Inner products are conjugate-linear in their first argument. No floats enter.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import json


def exact(value):
    if type(value) not in (int, F):
        raise TypeError("An exact integer or Fraction is required")
    return F(value)


@dataclass(frozen=True)
class C:
    """A Gaussian rational; no Python complex/float coercion."""

    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", exact(self.re))
        object.__setattr__(self, "im", exact(self.im))

    def __add__(self, other):
        other = scalar(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + -scalar(other)

    def __rsub__(self, other):
        return scalar(other) + -self

    def __mul__(self, other):
        other = scalar(other)
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = scalar(other)
        denominator = other.abs2()
        if not denominator:
            raise ZeroDivisionError("Gaussian rational division by zero")
        numerator = self * other.conj()
        return C(numerator.re / denominator, numerator.im / denominator)

    def conj(self):
        return C(self.re, -self.im)

    def abs2(self):
        return self.re ** 2 + self.im ** 2

    def __bool__(self):
        return bool(self.re or self.im)

    def text(self):
        return {"real": str(self.re), "imaginary": str(self.im)}


def scalar(value):
    return value if isinstance(value, C) else C(exact(value))


def matrix(rows):
    result = tuple(tuple(scalar(x) for x in row) for row in rows)
    if not result or not result[0] or any(len(r) != len(result[0]) for r in result):
        raise ValueError("A nonempty rectangular matrix is required")
    return result


def identity(n):
    if type(n) is not int or n < 1:
        raise ValueError("Positive exact dimension required")
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def adjoint(a):
    a = matrix(a)
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def multiply(a, b):
    a, b = matrix(a), matrix(b)
    if len(a[0]) != len(b):
        raise ValueError("Incompatible matrix dimensions")
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), C())
                       for j in range(len(b[0]))) for i in range(len(a)))


def subtract(a, b):
    a, b = matrix(a), matrix(b)
    if (len(a), len(a[0])) != (len(b), len(b[0])):
        raise ValueError("Incompatible matrix dimensions")
    return tuple(tuple(x-y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def is_zero(a):
    return all(not x for row in a for x in row)


def psd(a, *, strict=False):
    """Exact Hermitian congruence test, including singular zero pivots."""
    a = matrix(a)
    if len(a) != len(a[0]) or a != adjoint(a):
        return False
    work = [list(row) for row in a]
    n = len(a)
    for k in range(n):
        pivot = work[k][k]
        if pivot.im or pivot.re < 0:
            return False
        if not pivot:
            if strict or any(work[k][j] for j in range(k+1, n)):
                return False
            continue
        for i in range(k+1, n):
            for j in range(k+1, n):
                work[i][j] -= work[i][k] * work[k][j] / pivot
    return True


def inverse(a):
    a = matrix(a)
    n = len(a)
    if len(a[0]) != n:
        raise ValueError("Square matrix required")
    work = [list(a[i]) + list(identity(n)[i]) for i in range(n)]
    for k in range(n):
        pivot_row = next((i for i in range(k, n) if work[i][k]), None)
        if pivot_row is None:
            raise ValueError("Singular matrix")
        work[k], work[pivot_row] = work[pivot_row], work[k]
        pivot = work[k][k]
        work[k] = [x/pivot for x in work[k]]
        for i in range(n):
            if i != k:
                scale = work[i][k]
                work[i] = [x-scale*y for x, y in zip(work[i], work[k])]
    return tuple(tuple(row[n:]) for row in work)


def basis_column(n, index):
    return matrix([[int(j == index)] for j in range(n)])


def word_state(filters, word, state):
    value = matrix(state)
    for letter in word:
        value = multiply(filters[letter], value)
    return value


def word_return(filters, word, state):
    return multiply(adjoint(state), word_state(filters, word, state))[0][0]


def boundary_tables(filters, state, basis_words):
    """Forward laboratory oracle, distinct from the boundary-only verifier."""
    columns = [word_state(filters, word, state) for word in basis_words]
    v = matrix([[column[i][0] for column in columns] for i in range(len(state))])
    g = multiply(adjoint(v), v)
    h, q = {}, {}
    for name, operator in filters.items():
        child = multiply(operator, v)
        h[name] = multiply(adjoint(v), child)
        q[name] = multiply(adjoint(child), child)
    return g, h, q


class BoundaryCertificate:
    """Reconstruct from G, H_i, Q_i only; ambient operators are not supplied.

    Authentication, stationary linear dynamics and true word-labelled Gram
    data are hypotheses. A closed certificate also verifies all named basis
    words in its reconstructed matrices, catching contradictory word labels.
    """

    def __init__(self, basis_words, g, h, q):
        self.basis_words = tuple(tuple(w) for w in basis_words)
        self.g = matrix(g)
        n = len(self.g)
        if (len(self.g[0]) != n or not psd(self.g, strict=True)
                or len(self.basis_words) != n or self.basis_words[0] != ()
                or len(set(self.basis_words)) != n):
            raise ValueError("Independent ordered basis including the empty word is required")
        if not h or set(h) != set(q) or any(type(k) is not str or not k for k in h):
            raise ValueError("Matching nonempty labelled shift tables required")
        if any(letter not in h for word in self.basis_words for letter in word):
            raise ValueError("Unknown filter in basis word")
        self.h, self.q = {}, {}
        self.m, self.residual, self.defect_trace = {}, {}, {}
        self.contraction_on_observed_span = {}
        gi = inverse(self.g)
        for name in h:
            hi, qi = matrix(h[name]), matrix(q[name])
            if any((len(a), len(a[0])) != (n, n) for a in (hi, qi)):
                raise ValueError("Shift table shape differs from basis Gram")
            mi = multiply(gi, hi)
            ri = subtract(qi, multiply(adjoint(hi), mi))
            if not psd(ri):
                raise ValueError("Impossible boundary Gram: residual is not positive semidefinite")
            self.h[name], self.q[name] = hi, qi
            self.m[name], self.residual[name] = mi, ri
            tr = sum((multiply(gi, ri)[j][j] for j in range(n)), C())
            if tr.im or tr.re < 0:
                raise ArithmeticError("Positive residual has an invalid metric trace")
            self.defect_trace[name] = tr.re
            self.contraction_on_observed_span[name] = psd(subtract(self.g, qi))
        self.closed = all(is_zero(r) for r in self.residual.values())
        self.initial = basis_column(n, 0)
        if self.closed:
            for j, word in enumerate(self.basis_words):
                if word_state(self.m, word, self.initial) != basis_column(n, j):
                    raise ValueError("Shift matrices contradict their declared basis words")

    def return_value(self, word):
        """Exact if closed; otherwise the compressed model's prediction."""
        value = word_state(self.m, word, self.initial)
        return multiply(multiply(adjoint(self.initial), self.g), value)[0][0]

    def conditional_word_error_squared_bound(self, word):
        """Bounds ambient vector error ONLY IF every ambient filter is a contraction.

        That ambient norm promise is not inferable from these finite tables.
        The computable bound is ||xi||^2 L sum_j tr(G^-1 R_{word[j]}).
        """
        word = tuple(word)
        return self.g[0][0].re * len(word) * sum((self.defect_trace[i] for i in word), F())

    def receipt(self):
        return {
            "observed_dimension": len(self.g),
            "closed_under_every_declared_filter": self.closed,
            "metric_residual_trace": {k: str(v) for k, v in self.defect_trace.items()},
            "contraction_on_observed_span": self.contraction_on_observed_span,
            "ambient_dimension_or_ontology_identified": False,
            "ambient_contraction_bounds_certified": False,
            "source_authentication_certified": False,
            "arithmetic_asymptotic_bound_certified": False,
        }


def pauli_pair(sign=1):
    if sign not in (-1, 1) or type(sign) is not int:
        raise ValueError("Sign must be +1 or -1")
    return {"x": matrix([[0, 1], [1, 0]]),
            "y": matrix([[0, C(0, -sign)], [C(0, sign), 0]])}


def demo_receipt():
    state, words = basis_column(2, 0), ((), ("x",))
    plus, minus = pauli_pair(1), pauli_pair(-1)
    cert = BoundaryCertificate(words, *boundary_tables(plus, state, words))
    mismatch, equal_intensities = [], 0
    for length in range(7):
        for word in product(("x", "y"), repeat=length):
            a, b = word_return(plus, word, state), word_return(minus, word, state)
            if cert.return_value(word) != a:
                mismatch.append(list(word))
            if a.abs2() == b.abs2():
                equal_intensities += 1
    return {"status": "VERIFIED_FINITE", "certificate": cert.receipt(),
            "reconstruction_words_checked": 127,
            "reconstruction_mismatches": mismatch,
            "same_intensity_words_checked": equal_intensities,
            "chronological_y_then_x_returns": {
                "plus": word_return(plus, ("y", "x"), state).text(),
                "minus": word_return(minus, ("y", "x"), state).text()},
            "universal_proof": "ORDERED_REALIZATION.md; finite checks are not its proof"}


if __name__ == "__main__":
    print(json.dumps(demo_receipt(), indent=2, sort_keys=True))
