"""Exact 0-4 observer-ladder primitives: C3 windows and Herm(2) spinors.

Pure stdlib research adapter, NOT a new category or a pi-normality proof.
Proofs and claim statuses live in research/2026-11-12/arity_0_5_observer_ladder/.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence


def _q(x: int | Fraction) -> Fraction:
    return Fraction(x)


@dataclass(frozen=True)
class Omega3:
    """Exact Q[omega]/(omega^2 + omega + 1), as a + b omega."""
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "a", _q(self.a))
        object.__setattr__(self, "b", _q(self.b))

    @staticmethod
    def lift(z: Omega3 | int | Fraction) -> Omega3:
        return z if isinstance(z, Omega3) else Omega3(_q(z))

    def __add__(self, other: Omega3 | int | Fraction) -> Omega3:
        o = self.lift(other)
        return Omega3(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self) -> Omega3:
        return Omega3(-self.a, -self.b)

    def __sub__(self, other: Omega3 | int | Fraction) -> Omega3:
        return self + (-self.lift(other))

    def __rsub__(self, other: Omega3 | int | Fraction) -> Omega3:
        return self.lift(other) - self

    def __mul__(self, other: Omega3 | int | Fraction) -> Omega3:
        o = self.lift(other)
        # omega^2 = -1 - omega
        return Omega3(self.a * o.a - self.b * o.b,
                      self.a * o.b + self.b * o.a - self.b * o.b)

    __rmul__ = __mul__

    def conjugate(self) -> Omega3:
        return Omega3(self.a - self.b, -self.b)


OMEGA = Omega3(0, 1)
OMEGA_POWERS = (Omega3(1), OMEGA, Omega3(-1, -1))


def triad_mode(values: Sequence[Omega3 | int | Fraction], k: int) -> Omega3:
    """Sum_{j=0}^2 omega^(k*j) values[j], k read mod 3."""
    if len(values) != 3:
        raise ValueError("a triad has exactly three entries")
    return sum((OMEGA_POWERS[(k * j) % 3] * Omega3.lift(v)
                for j, v in enumerate(values)), Omega3())


def triad_defect(values: Sequence[Omega3 | int | Fraction], k: int) -> Omega3:
    """Exact sliding-window (not cyclic!) transport defect for four entries."""
    if len(values) != 4:
        raise ValueError("sliding transfer requires four entries")
    return (triad_mode(values[1:4], k)
            - OMEGA_POWERS[(-k) % 3] * triad_mode(values[0:3], k))


def triad_boundary(values: Sequence[Omega3 | int | Fraction], k: int) -> Omega3:
    """Boundary of sum of N consecutive triads; input has N+2 entries."""
    if len(values) < 3:
        raise ValueError("at least one triad required")
    z = [Omega3.lift(v) for v in values]
    w, w2 = OMEGA_POWERS[k % 3], OMEGA_POWERS[(2 * k) % 3]
    return (-(w + w2) * z[0] - w2 * z[1]
            + (w + w2) * z[-2] + w2 * z[-1])


def triad_sum_identity(values: Sequence[Omega3 | int | Fraction], k: int) -> tuple[Omega3, Omega3]:
    """LHS=sum of windows; RHS=(1+w+w^2)*sum base + boundary."""
    if len(values) < 3:
        raise ValueError("at least one triad required")
    z = [Omega3.lift(v) for v in values]
    n = len(z) - 2
    lhs = sum((triad_mode(z[j:j+3], k) for j in range(n)), Omega3())
    coeff = Omega3(1) + OMEGA_POWERS[k % 3] + OMEGA_POWERS[(2*k) % 3]
    rhs = coeff * sum(z[:n], Omega3()) + triad_boundary(z, k)
    return lhs, rhs


@dataclass(frozen=True)
class GaussQ:
    """Exact Gaussian-rational complex number x + i*y."""
    x: Fraction = Fraction(0)
    y: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "x", _q(self.x))
        object.__setattr__(self, "y", _q(self.y))

    @staticmethod
    def lift(z: GaussQ | int | Fraction) -> GaussQ:
        return z if isinstance(z, GaussQ) else GaussQ(_q(z))

    def __add__(self, other: GaussQ | int | Fraction) -> GaussQ:
        o = self.lift(other)
        return GaussQ(self.x + o.x, self.y + o.y)

    __radd__ = __add__

    def __neg__(self) -> GaussQ:
        return GaussQ(-self.x, -self.y)

    def __sub__(self, other: GaussQ | int | Fraction) -> GaussQ:
        return self + (-self.lift(other))

    def __rsub__(self, other: GaussQ | int | Fraction) -> GaussQ:
        return self.lift(other) - self

    def __mul__(self, other: GaussQ | int | Fraction) -> GaussQ:
        o = self.lift(other)
        return GaussQ(self.x*o.x - self.y*o.y,
                      self.x*o.y + self.y*o.x)

    __rmul__ = __mul__

    def conjugate(self) -> GaussQ:
        return GaussQ(self.x, -self.y)


Matrix2 = tuple[tuple[GaussQ, GaussQ], tuple[GaussQ, GaussQ]]
ZERO = GaussQ()
ONE = GaussQ(1)
I = GaussQ(0, 1)
IDENTITY: Matrix2 = ((ONE, ZERO), (ZERO, ONE))


def matrix(a: GaussQ | int | Fraction, b: GaussQ | int | Fraction,
           c: GaussQ | int | Fraction, d: GaussQ | int | Fraction) -> Matrix2:
    return ((GaussQ.lift(a), GaussQ.lift(b)),
            (GaussQ.lift(c), GaussQ.lift(d)))


def mmul(a: Matrix2, b: Matrix2) -> Matrix2:
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(2)), ZERO)
                       for j in range(2)) for i in range(2))  # type: ignore[return-value]


def dagger(a: Matrix2) -> Matrix2:
    return matrix(a[0][0].conjugate(), a[1][0].conjugate(),
                  a[0][1].conjugate(), a[1][1].conjugate())


def trace(a: Matrix2) -> GaussQ:
    return a[0][0] + a[1][1]


def det(a: Matrix2) -> GaussQ:
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


def hermitian(t: int | Fraction, x: int | Fraction,
              y: int | Fraction, z: int | Fraction) -> Matrix2:
    """X=t I + x sigma_x + y sigma_y + z sigma_z."""
    t, x, y, z = map(_q, (t, x, y, z))
    return matrix(t + z, GaussQ(x, -y), GaussQ(x, y), t - z)


def coordinates(a: Matrix2) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Recover real Minkowski coordinates; reject non-Hermitian inputs."""
    if dagger(a) != a:
        raise ValueError("matrix is not Hermitian")
    return ((a[0][0].x + a[1][1].x)/2,
            a[0][1].x, -a[0][1].y,
            (a[0][0].x - a[1][1].x)/2)


def congruence(g: Matrix2, a: Matrix2) -> Matrix2:
    """Spinor lift X -> g X g^dagger (det g=1 required for Lorentz)."""
    return mmul(mmul(g, a), dagger(g))


def minkowski(v: Sequence[int | Fraction]) -> Fraction:
    if len(v) != 4:
        raise ValueError("a Minkowski vector has four coordinates")
    t, x, y, z = map(_q, v)
    return t*t - x*x - y*y - z*z


def hilbert_schmidt(v: Sequence[int | Fraction]) -> Fraction:
    if len(v) != 4:
        raise ValueError("a Hermitian matrix has four real coordinates")
    # Tr(X^dagger X)=2*(t^2+x^2+y^2+z^2), not its half.
    return 2 * sum((_q(q)**2 for q in v), Fraction(0))


def wilson_triangle(u01: Matrix2, u12: Matrix2, u20: Matrix2) -> Matrix2:
    """Path-ordered 0->1->2->0 holonomy, read right-to-left."""
    return mmul(u20, mmul(u12, u01))


def gauge_link(uij: Matrix2, gi: Matrix2, gj: Matrix2) -> Matrix2:
    """Gauge action for unitary vertex frames gi, gj, no general inverse."""
    return mmul(mmul(gj, uij), dagger(gi))


def bbp_forcing(n: int) -> Fraction:
    """Independent four-pole transcription for source-contract cross-checks."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    return (Fraction(4, 8*n-7) - Fraction(2, 8*n-4)
            - Fraction(1, 8*n-3) - Fraction(1, 8*n-2))


def bbp_residue_prefix(last_n: int, seed: Fraction | int = 0) -> list[Fraction]:
    """Zero-seeded selected residues x_0,...,x_last_n; exact, finite."""
    if type(last_n) is not int or last_n < 0:
        raise ValueError("last_n must be an integer >=0")
    x = Fraction(seed) % 1
    out = [x]
    for n in range(1, last_n+1):
        x = (16*x + bbp_forcing(n)) % 1
        out.append(x)
    return out
