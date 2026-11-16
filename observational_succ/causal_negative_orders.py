"""Exact finite readouts of causal distributions and negative Mellin orders.

Time support stays nonnegative. Negative analytic order permits signed
distributions; no negative probability or backwards physical evolution is
asserted. The universal proofs and convergence domains are in
research/2026-11-15/causal_negative_orders/THEOREMS.md.

The BBP regulator family is inherited from euler_bbp_regulator. Only its
exponent-one, regulator-1/16 specialization is the original pi sum. This
module adds exact negative-order and causal-face readouts without changing
the original forcing, radix, seed, or selected phase.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb, factorial
from typing import Iterable


MAX_ORDER = 64
MAX_FACE = 24
SOURCE_SHIFTS = (0, 3, 4, 5)
SOURCE_COEFFICIENTS = (4, -2, -1, -1)


def _integer(value: int, maximum: int, name: str) -> int:
    if type(value) is not int or not 0 <= value <= maximum:
        raise ValueError(f"{name} must be an integer in 0..{maximum}")
    return value


def _rational(value: int | Q, name: str) -> Q:
    if type(value) not in (int, Q):
        raise TypeError(f"{name} must be an exact int or Fraction")
    return Q(value)


def _positive(value: int | Q, name: str) -> Q:
    value = _rational(value, name)
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def _regulator(value: int | Q) -> Q:
    value = _rational(value, "regulator")
    if not 0 <= value < 1:
        raise ValueError("the entire regulator family requires 0 <= z < 1")
    return value


@dataclass(frozen=True)
class CausalAtom:
    """A signed coefficient at a nonnegative lag, not a probability."""

    lag: Q
    coefficient: Q

    def __post_init__(self):
        lag = _rational(self.lag, "lag")
        if lag < 0:
            raise ValueError("causal lag must be nonnegative")
        object.__setattr__(self, "lag", lag)
        object.__setattr__(self, "coefficient", _rational(self.coefficient, "coefficient"))


def forward_delta_difference(order: int, step: int | Q) -> tuple[CausalAtom, ...]:
    """h^-m sum_j (-1)^j C(m,j) delta_(j*h), tending to D^m delta.

    The test-function pairing has the distributional sign (-1)^m.
    """
    m = _integer(order, MAX_ORDER, "order")
    h = _positive(step, "step")
    return tuple(CausalAtom(j*h, Q((-1)**j * comb(m, j))/h**m)
                 for j in range(m+1))


def polynomial_atom_pairing(atoms: Iterable[CausalAtom],
                            coefficients: Iterable[int | Q]) -> Q:
    """Pair finitely many atoms with a polynomial in ascending powers."""
    terms = tuple(atoms)
    if len(terms) > MAX_ORDER+1 or any(not isinstance(a, CausalAtom) for a in terms):
        raise ValueError("expected at most MAX_ORDER+1 causal atoms")
    poly = tuple(_rational(c, "polynomial coefficient") for c in coefficients)
    if not poly or len(poly) > MAX_ORDER+2:
        raise ValueError("polynomial length must be in 1..MAX_ORDER+2")
    result = Q(0)
    for atom in terms:
        value = Q(0)
        for coefficient in reversed(poly):
            value = value*atom.lag+coefficient
        result += atom.coefficient*value
    return result


def delta_difference_error_bound(order: int, step: int | Q,
                                 next_derivative_bound: int | Q) -> Q:
    """m*h*M/2 if |phi^(m+1)| <= M on [0,m*h]; a stated premise.

    This is the exact mean-distance bound from the m-dimensional cube
    integral for a forward difference. It is zero at m=0.
    """
    m = _integer(order, MAX_ORDER, "order")
    h = _positive(step, "step")
    bound = _rational(next_derivative_bound, "derivative bound")
    if bound < 0:
        raise ValueError("derivative bound must be nonnegative")
    return Q(m, 2)*h*bound


def delta_difference_noise_gain(order: int, step: int | Q) -> Q:
    """Exact l-infinity data-error to scalar-output norm 2^m/h^m."""
    m = _integer(order, MAX_ORDER, "order")
    return Q(2**m)/_positive(step, "step")**m


def tempered_negative_coefficients(order: int, rate: int | Q = 0) -> tuple[Q, ...]:
    """Coefficients of (D+rate)^m delta, in ascending delta derivatives.

    This is exp(-rate*t)*Phi_-m, without probability normalization.
    """
    m = _integer(order, MAX_ORDER, "order")
    rate = _rational(rate, "rate")
    if rate < 0:
        raise ValueError("tempering rate must be nonnegative")
    return tuple(Q(comb(m, j))*rate**(m-j) for j in range(m+1))


def negative_order_pairing(order: int, derivatives_at_zero: Iterable[int | Q],
                           rate: int | Q = 0) -> Q:
    """Pair exp(-rate*t)*Phi_-m with a supplied exact boundary jet."""
    coefficients = tempered_negative_coefficients(order, rate)
    jet = tuple(_rational(x, "derivative") for x in derivatives_at_zero)
    if len(jet) != len(coefficients):
        raise ValueError("supply exactly order+1 derivatives, starting at value")
    return sum((c*(-1)**j*jet[j] for j, c in enumerate(coefficients)), Q())


def source_negative_mellin(order: int, age: int | Q, face: int = 0) -> Q:
    """F_(a,k)(-m) for e^-at*q(t)*(1-e^-8t)^k; a>0.

    This is the analytic Mellin readout, not an integral of t^-m-1.
    """
    m = _integer(order, MAX_ORDER, "order")
    k = _integer(face, MAX_FACE, "face")
    a = _positive(age, "age")
    return sum((Q((-1)**j*comb(k, j)*c)*(a+8*j+d)**m
                for j in range(k+1)
                for d, c in zip(SOURCE_SHIFTS, SOURCE_COEFFICIENTS)), Q())


def geometric_power_moments(regulator: int | Q, through: int) -> tuple[Q, ...]:
    """Exact sum_(n>=0) z^n*n^j, with 0^0=1 and 0<=z<1."""
    z = _regulator(regulator)
    degree = _integer(through, MAX_ORDER, "moment degree")
    moments = [1/(1-z)]
    for j in range(1, degree+1):
        moments.append(z/(1-z)*sum((comb(j, i)*moments[i]
                                   for i in range(j)), Q()))
    return tuple(moments)


def bbp_negative_mellin(order: int, face: int = 0,
                        regulator: int | Q = Q(1, 16)) -> Q:
    """Entire B_(z,k)(-m), preserving all four source coefficients.

    B_(z,k)(s)=sum_n z^n sum_j (-1)^j C(k,j) F_(8n+1+8j)(s).
    Only B_(1/16,0)(1)=pi; k and s label analytic reports.
    """
    m = _integer(order, MAX_ORDER, "order")
    k = _integer(face, MAX_FACE, "face")
    moments = geometric_power_moments(regulator, m)
    polynomial = [Q(0)]*(m+1)
    for j in range(k+1):
        for d, c in zip(SOURCE_SHIFTS, SOURCE_COEFFICIENTS):
            weight = (-1)**j*comb(k, j)*c
            a = 1+8*j+d
            for power in range(m+1):
                polynomial[power] += weight*comb(m, power)*8**power*a**(m-power)
    return sum((p*v for p, v in zip(polynomial, moments)), Q())


def bbp_face_first_value(face: int, regulator: int | Q = Q(1, 16)) -> Q:
    """First nonzero negative-order value, at s=-(face+1)."""
    k = _integer(face, MAX_FACE, "face")
    z = _regulator(regulator)
    return Q((-1)**(k+1)*15*8**k*factorial(k+1))/(1-z)


def _multiply_series(left: tuple[Q, ...], right: tuple[Q, ...], degree: int) -> tuple[Q, ...]:
    return tuple(sum((left[i]*right[n-i]
                      for i in range(n+1)
                      if i < len(left) and n-i < len(right)), Q())
                 for n in range(degree+1))


def bbp_heat_coefficients(through: int, face: int = 0,
                          regulator: int | Q = Q(1, 16)) -> tuple[Q, ...]:
    """Taylor coefficients of H_(z,k)=e^-t*q(t)*(1-e^-8t)^k/(1-z*e^-8t).

    Independent local series division; coefficient j multiplies t^j,
    so the negative Mellin readout is (-1)^j*j!*coefficient[j].
    """
    degree = _integer(through, MAX_ORDER, "Taylor degree")
    k = _integer(face, MAX_FACE, "face")
    z = _regulator(regulator)
    numerator = tuple(sum((Q(c*(-1-d)**n, factorial(n))
                           for d, c in zip(SOURCE_SHIFTS, SOURCE_COEFFICIENTS)), Q())
                      for n in range(degree+1))
    face_series = (Q(0),)+tuple(Q(-(-8)**n, factorial(n)) for n in range(1, degree+1))
    for _ in range(k):
        numerator = _multiply_series(numerator, face_series, degree)
    denominator = (1-z,)+tuple(Q(-(-8)**n, factorial(n))*z
                               for n in range(1, degree+1))
    quotient: list[Q] = []
    for n in range(degree+1):
        quotient.append((numerator[n]-sum((denominator[j]*quotient[n-j]
                                          for j in range(1, n+1)), Q()))/denominator[0])
    return tuple(quotient)


def convolution_negative_mellin(power: int, order: int, age: int | Q) -> Q:
    """Mellin value at -order for exp(-age*t)*q^{*power}(t).

    Uses the inherited complete signed Gamma-kernel normal form, not only
    its leading endpoint. Its power bound is inherited (1..12).
    """
    from .bbp_gamma_kernel_algebra import source_kernel_power

    m = _integer(order, MAX_ORDER, "order")
    a = _positive(age, "age")
    kernel = source_kernel_power(power)
    coefficient = sum((kernel.taylor_coefficient(j)*(-a)**(m-j)/factorial(m-j)
                       for j in range(m+1)), Q())
    return (-1)**m*factorial(m)*coefficient


def bose_regular_coefficients(through: int) -> tuple[Q, ...]:
    """Taylor jet of 1/(e^t-1)-1/t via exact power-series inversion.

    The subtracted 1/t pole is explicit. No zeta function is used as an
    input. Oddness after adding 1/2 is the source of even-degree zeros.
    """
    degree = _integer(through, MAX_ORDER, "Taylor degree")
    inverse = [Q(1)]
    for n in range(1, degree+2):
        inverse.append(-sum((Q(1, factorial(j+1))*inverse[n-j]
                             for j in range(1, n+1)), Q()))
    return tuple(inverse[1:])


def zeta_negative_from_heat(order: int) -> Q:
    """Classical analytic value zeta(-m), derived from the Bose heat jet.

    This is not the ordinary sum of the divergent positive powers.
    """
    m = _integer(order, MAX_ORDER, "order")
    return (-1)**m*factorial(m)*bose_regular_coefficients(m)[m]


def pascal_face_negative_mellin(order: int, grade: int) -> Q:
    """Universal F_grade(-m) for e^-t*(1-e^-t)^grade.

    This inherited Pascal/Hasse carrier differs from the original BBP
    source face, whose stride is eight and whose base kernel is H_BBP.
    """
    m = _integer(order, MAX_ORDER, "order")
    n = _integer(grade, MAX_ORDER, "Pascal grade")
    return Q(sum((-1)**j*comb(n, j)*(j+1)**m for j in range(n+1)))


def eta_negative_from_causal_faces(order: int) -> Q:
    """Exact finite value of the entire positive-grade Hasse mixture at -m."""
    m = _integer(order, MAX_ORDER, "order")
    return sum((pascal_face_negative_mellin(m, n)/2**(n+1)
                for n in range(m+1)), Q())


def zeta_negative_from_causal_faces(order: int) -> Q:
    """Classical zeta(-m) via Pascal faces; denominator never zero here."""
    m = _integer(order, MAX_ORDER, "order")
    return eta_negative_from_causal_faces(m)/(1-2**(m+1))


def native_negative_face_mixture(order: int) -> Q:
    """Same weights on actual BBP faces: sum_k 2^-k-1 B_k(-m).

    The tail is exactly zero for k>=m. The kernel is H_BBP/(1+e^-8t),
    and its value at -2 is 8, not the eta or zeta value zero.
    """
    m = _integer(order, MAX_FACE+1, "native mixture order")
    return sum((bbp_negative_mellin(m, k)/2**(k+1) for k in range(m)), Q())
