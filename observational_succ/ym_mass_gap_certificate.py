"""Exact finite matrix checks for a conditional 4D Yang--Mills gap criterion.

Given a positive OS semigroup and a dense physical observer bank, a single
fixed-physical-time Loewner contraction implies a mass gap. That theorem is
proved in the companion dossier. This module checks FINITE matrices only:
it cannot certify Wilson source provenance, bank density, RG uniformity,
an OS reconstruction, or the Yang--Mills mass gap.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations


class GapCertificateError(ValueError):
    """Malformed certificate, as distinct from a valid failed inequality."""


def _rat(x: Q, label: str) -> Q:
    if type(x) is not Q:
        raise GapCertificateError(f"{label}: exact Fraction required")
    return x


def _real_matrix(a, label: str):
    if type(a) is not tuple or not a or len(a) > 8:
        raise GapCertificateError(f"{label}: nonempty matrix, size <= 8")
    n = len(a)
    for row in a:
        if type(row) is not tuple or len(row) != n:
            raise GapCertificateError(f"{label}: non-square")
        for entry in row:
            _rat(entry, label)
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(i)):
        raise GapCertificateError(f"{label}: not symmetric")
    return a


def _det(rows):
    """Fraction/Gaussian rational exact Gaussian elimination, det(empty)=1."""
    a = [list(row) for row in rows]
    d = Q(1)
    for i in range(len(a)):
        p = next((j for j in range(i, len(a)) if a[j][i]), None)
        if p is None:
            return Q(0)
        if p != i:
            a[i], a[p] = a[p], a[i]
            d = -d
        h = a[i][i]
        d *= h
        for k in range(i + 1, len(a)):
            if a[k][i]:
                z = a[k][i] / h
                for j in range(i + 1, len(a)):
                    a[k][j] -= z * a[i][j]
                a[k][i] = Q(0)
    return d


def exact_psd(a) -> bool:
    """All principal minors, not only leading minors; singular PSD is valid."""
    a = _real_matrix(a, "matrix")
    for k in range(1, len(a) + 1):
        for ids in combinations(range(len(a)), k):
            if _det(tuple(tuple(a[i][j] for j in ids) for i in ids)) < 0:
                return False
    return True


def gram_gap_at_one_time(g0, gt, q: Q) -> bool:
    """Finite real Loewner qG0-Gt >= 0. Does not prove cyclic completeness."""
    a = _real_matrix(g0, "G0")
    b = _real_matrix(gt, "Gt")
    _rat(q, "q")
    if len(a) != len(b) or not Q(0) < q < Q(1):
        raise GapCertificateError("dimension mismatch or q outside (0,1)")
    d = tuple(tuple(q*a[i][j] - b[i][j] for j in range(len(a)))
              for i in range(len(a)))
    return exact_psd(a) and exact_psd(b) and exact_psd(d)


def entrywise_error_gap(g0hat, gthat, q: Q, e0: Q, et: Q) -> bool:
    """With independently proved entrywise errors, n(qe0+et)I is a safe margin.

    This verifies the algebraic implication, NOT the provided error claims.
    """
    a = _real_matrix(g0hat, "G0hat")
    b = _real_matrix(gthat, "Gthat")
    for name, val in (("q", q), ("e0", e0), ("et", et)):
        _rat(val, name)
    if len(a) != len(b) or not 0 < q < 1 or e0 < 0 or et < 0:
        raise GapCertificateError("invalid error margin data")
    n = len(a)
    margin = n*(q*e0+et)
    d = tuple(tuple(q*a[i][j] - b[i][j] - (margin if i == j else Q(0))
                    for j in range(n)) for i in range(n))
    return exact_psd(d)


def spectral_gram(spectrum: tuple[Q, ...], bank: tuple[tuple[Q, ...], ...],
                  steps: int):
    """Centered toy Gram. Eigenvalue 1 in coordinate 0 is vacuum; not YM."""
    if type(spectrum) is not tuple or len(spectrum) < 2:
        raise GapCertificateError("vacuum + excited modes required")
    for z in spectrum:
        _rat(z, "eigenvalue")
    if spectrum[0] != Q(1) or any(not 0 < z <= 1 for z in spectrum[1:]):
        raise GapCertificateError("positive semigroup and vacuum=1 required")
    if type(steps) is not int or steps < 0:
        raise GapCertificateError("steps must be nonnegative integer")
    if type(bank) is not tuple or not bank:
        raise GapCertificateError("nonempty bank required")
    for vec in bank:
        if type(vec) is not tuple or len(vec) != len(spectrum):
            raise GapCertificateError("wrong bank vector length")
        for z in vec:
            _rat(z, "bank entry")
    return tuple(tuple(sum((bank[i][k]*bank[j][k]*spectrum[k]**steps
                            for k in range(1, len(spectrum))), Q(0))
                       for j in range(len(bank))) for i in range(len(bank)))


def two_block_gap(alpha: Q, beta: Q, gamma: Q) -> bool:
    """Strict complete OS-orthogonal coarse/detail margin (conditional)."""
    for name, z in (("alpha", alpha), ("beta", beta), ("gamma", gamma)):
        _rat(z, name)
    if not (0 <= alpha <= 1 and 0 <= beta <= 1 and gamma >= 0):
        raise GapCertificateError("invalid nonnegative block bounds")
    return alpha < 1 and beta < 1 and gamma*gamma < (1-alpha)*(1-beta)


def weighted_block_gap(alpha: Q, beta: Q, gamma: Q, wc: Q, wd: Q, q: Q):
    """Rational weighted AM-GM certificate for a complete two-block split."""
    two_block_gap(alpha, beta, gamma)  # validates numerical domains
    for name, z in (("wc", wc), ("wd", wd), ("q", q)):
        _rat(z, name)
    if wc <= 0 or wd <= 0 or not 0 < q < 1:
        raise GapCertificateError("positive weights and 0<q<1 required")
    return (alpha*wc + gamma*wd <= q*wc and
            beta*wd + gamma*wc <= q*wd)


def two_state_ratio(n: int, regime: str) -> Q:
    """Normalized excited eigenvalue for T=(1+eps)^-1[[1,eps],[eps,1]].

    Physical mesh 1/n. For 'gapped', eps=1/(4n); for 'gapless',
    eps=1/n^2. For physical t=1 the actual transfer ratio is r^n.
    """
    if type(n) is not int or n < 2:
        raise GapCertificateError("integer mesh denominator n>=2 required")
    if regime == "gapped":
        eps = Q(1, 4*n)
    elif regime == "gapless":
        eps = Q(1, n*n)
    else:
        raise GapCertificateError("unknown toy regime")
    return (1-eps)/(1+eps)


@dataclass(frozen=True)
class GaussianQ:
    """Exact Q(i) amplitude, with no floating phase approximation."""
    re: Q
    im: Q = Q(0)

    def __post_init__(self):
        _rat(self.re, "real")
        _rat(self.im, "imag")

    @staticmethod
    def of(z):
        if type(z) is GaussianQ:
            return z
        if type(z) is Q:
            return GaussianQ(z)
        raise GapCertificateError("Q(i) or exact Fraction required")

    def conjugate(self):
        return GaussianQ(self.re, -self.im)

    def __bool__(self):
        return bool(self.re or self.im)

    def __neg__(self):
        return GaussianQ(-self.re, -self.im)

    def __add__(self, other):
        try:
            z = GaussianQ.of(other)
        except GapCertificateError:
            return NotImplemented
        return GaussianQ(self.re+z.re, self.im+z.im)

    __radd__ = __add__

    def __sub__(self, other):
        return self + (-GaussianQ.of(other))

    def __rsub__(self, other):
        return GaussianQ.of(other) - self

    def __mul__(self, other):
        try:
            z = GaussianQ.of(other)
        except GapCertificateError:
            return NotImplemented
        return GaussianQ(self.re*z.re-self.im*z.im,
                         self.re*z.im+self.im*z.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        z = GaussianQ.of(other)
        d = z.re*z.re+z.im*z.im
        if d == 0:
            raise ZeroDivisionError("Q(i) division by zero")
        p = self*z.conjugate()
        return GaussianQ(p.re/d, p.im/d)

    def __rtruediv__(self, other):
        return GaussianQ.of(other)/self


def _hermitian_matrix(value, name):
    if type(value) is not tuple or not value or len(value) > 8:
        raise GapCertificateError(f"{name}: nonempty square tuple size <=8 required")
    n = len(value)
    if any(type(row) is not tuple or len(row) != n for row in value):
        raise GapCertificateError(f"{name}: non-square")
    a = tuple(tuple(GaussianQ.of(x) for x in row) for row in value)
    for i in range(n):
        for j in range(i+1):
            if a[i][j] != a[j][i].conjugate():
                raise GapCertificateError(f"{name}: non-Hermitian")
    return a


def exact_hermitian_psd(matrix) -> bool:
    """Hermitian Q(i) positive semidefinite iff all real principal minors >=0."""
    a = _hermitian_matrix(matrix, "matrix")
    for k in range(1, len(a)+1):
        for ids in combinations(range(len(a)), k):
            d = GaussianQ.of(_det(tuple(tuple(a[i][j] for j in ids)
                                         for i in ids)))
            if d.im:
                raise ArithmeticError("Hermitian determinant must be real")
            if d.re < 0:
                return False
    return True


def hermitian_gap_at_one_time(g0, gt, q: Q) -> bool:
    """Exact Q(i) coherent-channel Loewner test at one physical time."""
    a = _hermitian_matrix(g0, "G0")
    b = _hermitian_matrix(gt, "Gt")
    _rat(q, "q")
    if len(a) != len(b) or not 0 < q < 1:
        raise GapCertificateError("dimension mismatch or invalid q")
    d = tuple(tuple(q*a[i][j]-b[i][j] for j in range(len(a)))
              for i in range(len(a)))
    return exact_hermitian_psd(a) and exact_hermitian_psd(b) and exact_hermitian_psd(d)


def coherent_spectral_gram(spectrum: tuple[Q, ...], bank: tuple[tuple, ...],
                           steps: int):
    """Centered Q(i) toy Gram; retains complex coherent cross terms."""
    if type(spectrum) is not tuple or len(spectrum) < 2:
        raise GapCertificateError("vacuum and excited eigenvalues required")
    for z in spectrum:
        _rat(z, "eigenvalue")
    if spectrum[0] != Q(1) or any(not 0 < z <= 1 for z in spectrum[1:]):
        raise GapCertificateError("vacuum=1 and positive semigroup required")
    if type(steps) is not int or steps < 0:
        raise GapCertificateError("nonnegative integer steps required")
    if type(bank) is not tuple or not bank or any(
        type(vec) is not tuple or len(vec) != len(spectrum) for vec in bank
    ):
        raise GapCertificateError("nonempty complete finite bank vectors required")
    vectors = tuple(tuple(GaussianQ.of(x) for x in v) for v in bank)
    return tuple(tuple(sum((vectors[i][k].conjugate()*vectors[j][k]
                            *spectrum[k]**steps for k in range(1,len(spectrum))),
                           GaussianQ(Q(0)))
                       for j in range(len(bank))) for i in range(len(bank)))


def coherent_entrywise_error_gap(g0hat, gthat, q: Q, e0: Q, et: Q) -> bool:
    """Q(i) sufficient margin assuming independently proved complex error norms."""
    a = _hermitian_matrix(g0hat, "G0hat")
    b = _hermitian_matrix(gthat, "Gthat")
    for name, z in (("q", q), ("e0", e0), ("et", et)):
        _rat(z, name)
    if len(a) != len(b) or not 0 < q < 1 or e0 < 0 or et < 0:
        raise GapCertificateError("invalid complex matrix margin")
    n = len(a)
    margin = n*(q*e0+et)
    d = tuple(tuple(q*a[i][j]-b[i][j] -
                    (GaussianQ(margin) if i==j else GaussianQ(Q(0)))
                    for j in range(n)) for i in range(n))
    return exact_hermitian_psd(d)
