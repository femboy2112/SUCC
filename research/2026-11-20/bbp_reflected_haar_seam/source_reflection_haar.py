"""Exact algebra and calibrated synthetic two-path readouts for the ORIGINAL BBP Q.

This is a research representation of Q(t)=(1-t)H(t), NOT the real π orbit.
All chronology-independent root-filter claims are typed as source spectral data.
"""
from __future__ import annotations

from fractions import Fraction
from math import cos, pi, sin, sqrt
from cmath import exp

RADIUS = sqrt(2.0)
H_ASCENDING = (4, 4, 4, 2, 1)
Q_ASCENDING = (4, 0, 0, -2, -1, -1)
# 1/H(z) = [1/4-z/4+z^3/8-z^4/16] / [1-z^8/16].
EIGHT_MOTIF = (Fraction(1, 4), Fraction(-1, 4), Fraction(0),
               Fraction(1, 8), Fraction(-1, 16), Fraction(0),
               Fraction(0), Fraction(0))
ROOT_ANGLES = {"top": pi/2, "upper_left": 3*pi/4,
               "lower_left": 5*pi/4, "bottom": 3*pi/2}
ROOT_CLASSES = {"top": 1, "bottom": 1, "upper_left": -1, "lower_left": -1}


def poly_mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += Fraction(ai) * Fraction(bj)
    return tuple(out)


def impulse(n: int) -> Fraction:
    """Exact nth Taylor coefficient of 1/H(z), n>=0."""
    if type(n) is not int or n < 0:
        raise ValueError("index must be a nonnegative integer")
    return EIGHT_MOTIF[n % 8] / 16**(n // 8)


def filter_residual(n: int) -> Fraction:
    """Convolution H(z) * (1/H(z)) at z^n; δ_(n0) exactly."""
    if type(n) is not int or n < 0:
        raise ValueError("index must be a nonnegative integer")
    return sum((Fraction(H_ASCENDING[j]) * impulse(n-j)
                for j in range(min(4, n)+1)), Fraction(0))


def total_hardy_energy() -> Fraction:
    """Exact H² norm squared of auxiliary filter 1/H(z): 37/255."""
    return sum((u*u for u in EIGHT_MOTIF), Fraction(0)) / (1-Fraction(1, 256))


def root_phase_fourth(index: int) -> int:
    """Sign of (t/sqrt(2))^4 at one of four exact source roots.

    Their normalized 8th-root exponents are 2,3,5,6.
    """
    if index not in (2,3,5,6) or type(index) is not int:
        raise ValueError("index must be one of 2, 3, 5, 6")
    return 1 if index % 2 == 0 else -1


def source_class(name: str) -> tuple[int, int]:
    """(Haar port sign, auxiliary Fibonacci factor determinant)."""
    sign = ROOT_CLASSES[name]
    return sign, 11 if sign == 1 else 5


def complementary_arc_lengths(theta: float) -> tuple[float,float]:
    """Distances from left-semicircle position to the two fixed endpoints.

    These are complementary distances, NOT automatically mirror roundtrip paths.
    """
    if not pi/2 <= theta <= 3*pi/2:
        raise ValueError("theta must be in left semicircle [pi/2,3pi/2]")
    s = RADIUS * (theta - pi/2)
    return s, pi*RADIUS - s


def coherent_haar_ports(theta: float, *, wavenumber: float | None = None,
                        reference_phase: float = 0.0) -> tuple[float,float]:
    """Synthetic two-path intensities after a calibrated 2-point Haar transform.

    Input paths have equal sqrt(1/2) amplitudes; receiver recombines them.
    reference_phase models a known relative scattering/transport phase.
    """
    d1,d2 = complementary_arc_lengths(theta)
    k = 2 / RADIUS if wavenumber is None else float(wavenumber)
    aa = exp(1j*k*d1) / sqrt(2)
    bb = exp(1j*(k*d2+reference_phase)) / sqrt(2)
    xp = (aa+bb)/sqrt(2)
    xm = (aa-bb)/sqrt(2)
    return (abs(xp)**2, abs(xm)**2)


def source_mask_winding(radius: float) -> int | None:
    """Exact root-count index for Q(radius*z), z on unit circle.

    This is winding of polynomial Q, NOT winding of the π Weyl orbit.
    None means at critical radius, where Toeplitz symbol is non-Fredholm.
    """
    from fractions import Fraction
    if isinstance(radius, Fraction):
        if radius <= 0:
            raise ValueError("radius must be positive")
        r2 = radius*radius
        if radius == 1 or r2 == 2:
            return None
        return (0 if radius < 1 else 1 if r2 < 2 else 5)
    r = float(radius)
    if r <= 0:
        raise ValueError("radius must be positive")
    if abs(r-1) < 1e-12 or abs(r*r-2) < 1e-12:
        return None
    return (0 if r < 1 else 1 if r*r < 2 else 5)


def model_summary():
    return {
        "H_coefficients": H_ASCENDING,
        "Q_coefficients": Q_ASCENDING,
        "root_classifications": ROOT_CLASSES,
        "auxiliary_filter_H2_energy": str(total_hardy_energy()),
        "boundary_indices_Q": [source_mask_winding(Fraction(1,2)),
                               source_mask_winding(Fraction(5,4)),
                               source_mask_winding(Fraction(3,2))],
        "model_status": "source-filter algebra; not a BBP phase conjugacy",
    }
