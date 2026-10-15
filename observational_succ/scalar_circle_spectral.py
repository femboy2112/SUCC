"""Physically motivated but STIPULATED scalar-field-on-a-circle spectral lab.

A_m = -d^2/dx^2 + m^2 on periodic circle, eigenmodes exp(2 pi i n x/L).
To keep exact arithmetic, alpha=(2*pi/L)^2 is a supplied rational parameter.
The field is a toy FREE Euclidean scalar, NOT the experimentally observed Higgs
field on real spacetime. Its spectral zeta is not a proof of RH.
"""

from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from math import exp, pi, sqrt


class SpectralSourceError(ValueError):
    """Non-source-typed mass, momentum spacing, or mode cutoff."""


def _q(x, *, positive=False):
    if type(x) not in (int,Q) or x<0 or (positive and x==0):
        raise SpectralSourceError("exact nonnegative mass², positive spacing² required")
    return Q(x)


@dataclass(frozen=True)
class CircleScalar:
    source_id: str
    epoch: int
    mass_squared: Q
    mode_spacing_squared: Q = Q(1)

    def __post_init__(self):
        if not self.source_id or type(self.epoch) is not int or self.epoch<0:
            raise SpectralSourceError("source id and nonnegative epoch required")
        _q(self.mass_squared)
        _q(self.mode_spacing_squared,positive=True)

    def eigenvalue(self, integer_mode: int) -> Q:
        if type(integer_mode) is not int:
            raise SpectralSourceError("periodic Fourier mode integer required")
        return Q(self.mass_squared)+Q(self.mode_spacing_squared)*integer_mode**2

    def truncated_spectral_zeta(self, integer_s: int, cutoff: int, *, nonzero_modes_only=False) -> Q:
        """Exact finite spectral sum; never analytic continuation or full zeta."""
        if type(integer_s) is not int or integer_s<1:
            raise SpectralSourceError("integer s>1/2 required for convergent full sum")
        if type(cutoff) is not int or cutoff<0:
            raise SpectralSourceError("finite nonnegative mode cutoff required")
        if self.mass_squared==0 and not nonzero_modes_only:
            raise SpectralSourceError("massless zero eigenmode is singular; omit it explicitly")
        return sum((Q(1,self.eigenvalue(n)**integer_s) for n in range(-cutoff,cutoff+1)
                    if n!=0 or not nonzero_modes_only),Q(0))

    def massless_dirichlet_truncation(self, integer_s: int, cutoff: int) -> Q:
        """2 alpha^-s sum_{n=1}^N n^-2s, *only* massless source m²=0."""
        if self.mass_squared!=0:
            raise SpectralSourceError("massive scalar is NOT the ordinary Riemann zeta model")
        if type(integer_s) is not int or integer_s<1 or type(cutoff) is not int or cutoff<0:
            raise SpectralSourceError("integer s>=1, cutoff>=0")
        return Q(2, Q(self.mode_spacing_squared)**integer_s)*sum((Q(1,n**(2*integer_s))
                  for n in range(1,cutoff+1)),Q(0))

    def normalized_eigenvalue(self, positive_mode: int) -> Q:
        """lambda_n/lambda_1; normalized source n=1 is exactly 1."""
        if type(positive_mode) is not int or positive_mode<1:
            raise SpectralSourceError("positive integer mode required")
        return self.eigenvalue(positive_mode)/self.eigenvalue(1)

    def multiplicative_two_three_defect(self) -> Q:
        """lambda_2/lambda_1 * lambda_3/lambda_1 - lambda_6/lambda_1.

        With c=m²/alpha, defect is exactly -24c/(1+c)^2.
        Therefore any strictly massive model has a NONMULTIPLICATIVE index
        weight, obstructing an Euler product from these native mode labels.
        """
        return self.normalized_eigenvalue(2)*self.normalized_eigenvalue(3) - self.normalized_eigenvalue(6)

    def relative_mass_perturbation(self, positive_mode: int) -> Q:
        """(lambda_n - alpha*n²)/(alpha*n²) = mass²/(alpha*n²)."""
        if type(positive_mode) is not int or positive_mode<1:
            raise SpectralSourceError("positive integer mode")
        return Q(self.mass_squared)/(Q(self.mode_spacing_squared)*positive_mode**2)


def poisson_theta_direct(t: float, spacing_squared: float, cutoff: int) -> float:
    """Numerical direct heat-kernel theta, no one-sided proof certificate."""
    if t<=0 or spacing_squared<=0 or type(cutoff) is not int or cutoff<1:
        raise SpectralSourceError("positive heat time, spacing and cutoff >=1")
    return sum(exp(-spacing_squared*n*n*t) for n in range(-cutoff,cutoff+1))


def poisson_theta_dual(t: float, spacing_squared: float, cutoff: int) -> float:
    """Numerical Poisson dual theta with prefactor sqrt(pi/(alpha*t))."""
    if t<=0 or spacing_squared<=0 or type(cutoff) is not int or cutoff<1:
        raise SpectralSourceError("positive heat time, spacing and cutoff >=1")
    return sqrt(pi/(spacing_squared*t))*sum(
        exp(-pi*pi*k*k/(spacing_squared*t)) for k in range(-cutoff,cutoff+1)
    )


def massless_zeta_tail_bound(integer_s: int, cutoff: int, alpha: Q=Q(1)) -> Q:
    """Rigorous upper bound on omitted positive/negative massless modes.

    2 alpha^-s sum_{n>N} n^-2s <= 2 alpha^-s N^(1-2s)/(2s-1).
    The convergence proof is the integral test, NOT a finite numerical fit.
    """
    if type(integer_s) is not int or integer_s<1 or type(cutoff) is not int or cutoff<1:
        raise SpectralSourceError("integer s>=1 and positive N")
    alpha=_q(alpha,positive=True)
    return Q(2, (2*integer_s-1)*cutoff**(2*integer_s-1)*alpha**integer_s)
