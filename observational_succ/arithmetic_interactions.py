"""Additive vs multiplicative arithmetic interaction calculus (Proof Forge §3.1).

The whole point of this module is a *typed* distinction that the rest of the
repository can lean on: the **additive** convolution

    (f *+ g)(n) = sum_{a+b=n, a,b>=1} f(a) g(b)

and the **Dirichlet / multiplicative** convolution

    (f *x g)(n) = sum_{a*b=n} f(a) g(b)

are different operations with different generating-series carriers. Their
ordinary generating function (OGF), Dirichlet generating function (DGF) and
Euler-product representations must never be silently interchanged. In
particular, for the von Mangoldt function Lambda,

    DGF of (Lambda *x Lambda)  =  (-zeta'/zeta)^2          [TRUE, multiplicative]
    DGF of (Lambda *+ Lambda)  =/=  (-zeta'/zeta)^2         [FALSE, additive]

The smallest exact witness separating the two is n = 5:

    (Lambda *+ Lambda)(5) = 2 log 2 log 3   (additive: 2+3 = 3+2 = 5)
    (Lambda *x Lambda)(5) = 0               (multiplicative: 5 prime, only 1*5)

This module exposes both convolutions exactly (sympy-symbolic for Lambda, so
the witness is an exact closed form, never a float), the DGF-coefficient
reading, and a guard `illegal_interchange_witness` that returns the smallest
counterexample refuting the claim "DGF of the additive convolution is
(-zeta'/zeta)^2". It is the executable receipt behind the BS-G3 correction in
`black_sun_goldbach.py`.

Status: CLASSICAL (the convolution identities are standard). The contribution
here is the typed firewall against illegal interchange, with exact witnesses.

RH PROVED: NO. No zeta-zero ordinate is used anywhere in this module.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Dict, List, Tuple

import sympy as sp


class ArithmeticInteractionError(ValueError):
    pass


# --------------------------------------------------------------------------
# arithmetic functions (exact: integer or sympy-symbolic values)
# --------------------------------------------------------------------------

def _factorint(n: int) -> Dict[int, int]:
    if n < 1:
        raise ArithmeticInteractionError(f"need n>=1, got {n}")
    return dict(sp.factorint(n)) if n > 1 else {}


def is_prime_power(n: int) -> Tuple[bool, int, int]:
    """Return (is_pp, p, k) with n = p**k, or (False, 0, 0)."""
    if n < 2:
        return (False, 0, 0)
    f = _factorint(n)
    if len(f) == 1:
        p, k = next(iter(f.items()))
        return (True, p, k)
    return (False, 0, 0)


def von_mangoldt(n: int):
    """Lambda(n) = log p  if n = p^k (k>=1), else 0.  Exact sympy value."""
    pp, p, _k = is_prime_power(n)
    return sp.log(p) if pp else sp.Integer(0)


def radical_int(n: int) -> int:
    """rad(n) = product of distinct primes dividing n; rad(1)=1."""
    if n < 1:
        raise ArithmeticInteractionError(f"need n>=1, got {n}")
    r = 1
    for p in _factorint(n):
        r *= p
    return r


# --------------------------------------------------------------------------
# the two convolutions (the load-bearing distinction)
# --------------------------------------------------------------------------

def additive_convolution(f: Callable[[int], object], g: Callable[[int], object], n: int):
    """(f *+ g)(n) = sum_{a+b=n, a,b>=1} f(a) g(b).  Exact (sympy-simplified)."""
    if n < 2:
        return sp.Integer(0)
    total = sp.Integer(0)
    for a in range(1, n):
        total += sp.sympify(f(a)) * sp.sympify(g(n - a))
    return sp.simplify(total)


def dirichlet_convolution(f: Callable[[int], object], g: Callable[[int], object], n: int):
    """(f *x g)(n) = sum_{a*b=n} f(a) g(b).  Exact (sympy-simplified)."""
    if n < 1:
        raise ArithmeticInteractionError(f"need n>=1, got {n}")
    total = sp.Integer(0)
    a = 1
    while a * a <= n:
        if n % a == 0:
            b = n // a
            total += sp.sympify(f(a)) * sp.sympify(g(b))
            if a != b:
                total += sp.sympify(f(b)) * sp.sympify(g(a))
        a += 1
    return sp.simplify(total)


def dgf_coefficient_of_squared_logderiv(n: int):
    """Coefficient of n^{-s} in (-zeta'/zeta)(s)^2.

    (-zeta'/zeta)(s) = sum_m Lambda(m) m^{-s}, so its square is the DGF of the
    *Dirichlet* convolution (Lambda *x Lambda). This function returns that exact
    coefficient = (Lambda *x Lambda)(n).  It is NOT the additive convolution.
    """
    return dirichlet_convolution(von_mangoldt, von_mangoldt, n)


# --------------------------------------------------------------------------
# the firewall: illegal-interchange witness
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class InterchangeWitness:
    n: int
    additive_value: object       # (Lambda *+ Lambda)(n)
    dirichlet_value: object      # (Lambda *x Lambda)(n) = [n^-s] (-zeta'/zeta)^2
    equal: bool

    def as_receipt(self) -> Dict[str, str]:
        return {
            "n": str(self.n),
            "additive_Lambda_conv": str(self.additive_value),
            "dirichlet_Lambda_conv": str(self.dirichlet_value),
            "equal": str(self.equal),
        }


def illegal_interchange_witness(bound: int = 16) -> InterchangeWitness:
    """Smallest n<=bound where (Lambda *+ Lambda)(n) != (Lambda *x Lambda)(n).

    This refutes the claim "the Dirichlet series of the additive Goldbach
    convolution R_Lambda is (-zeta'/zeta)^2-type". The square is the DGF of the
    *multiplicative* convolution; equating it to the additive convolution is an
    illegal interchange. Returns the minimal counterexample (expected n=5).
    """
    for n in range(2, bound + 1):
        add = additive_convolution(von_mangoldt, von_mangoldt, n)
        mul = dirichlet_convolution(von_mangoldt, von_mangoldt, n)
        if sp.simplify(add - mul) != 0:
            return InterchangeWitness(n, add, mul, equal=False)
    raise ArithmeticInteractionError(
        f"no separating witness up to {bound}; both convolutions agreed "
        "(should not happen: n=5 separates them)"
    )


def goldbach_representation_R_Lambda(N: int):
    """R_Lambda(N) = (Lambda *+ Lambda)(N) = sum_{n+m=N} Lambda(n)Lambda(m).

    The genuine additive Goldbach-weighted representation function. Exact.
    """
    return additive_convolution(von_mangoldt, von_mangoldt, N)


# --------------------------------------------------------------------------
# valid bridge: the ONE legitimate interchange we actually use
# --------------------------------------------------------------------------

def finite_fourier_sum_diagonal(N: int, ngrid: int) -> complex:
    """Numeric cross-check of the valid identity (BS-G1):

        (1/2pi) int_0^2pi F_N(theta)^2 e^{-iN theta} dtheta = R_Lambda(N),

    with F_N(theta) = sum_{n=1}^{N-1} Lambda(n) e^{i n theta}. This is the
    *additive* Fourier carrier of the Goldbach convolution and is legitimate.
    Returns the grid estimate of the coefficient (compare to float(R_Lambda)).
    NUMERIC corroboration only -- never a certificate.
    """
    import cmath
    import math
    lam = [0.0] * N
    for n in range(1, N):
        v = von_mangoldt(n)
        lam[n] = float(v) if v != 0 else 0.0
    acc = 0j
    for j in range(ngrid):
        theta = 2 * math.pi * j / ngrid
        F = sum(lam[n] * cmath.exp(1j * n * theta) for n in range(1, N))
        acc += F * F * cmath.exp(-1j * N * theta)
    return acc / ngrid
