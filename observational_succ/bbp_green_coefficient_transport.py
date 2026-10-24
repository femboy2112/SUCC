"""Exact BBP Green-to-asymptotic coefficient transport (source-specific).

Four *signed index poles* determine rational 1/n tail coefficients through
geometric Green moments. Signed pole Hankel rank is four, whereas the genuine
positive Green Hausdorff Hankel rank is infinite. These are different spaces.

Universal analytic claims and the source-typing boundary are proved in
research/2026-10-24/BBP_GREEN_RANK_COEFFICIENT_DUALITY.md.
No pi-normality, RH, or originality claim is made here.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import comb

from observational_succ.bbp_source_memory import (
    POLE_DATA, forcing, pole_moment, tail_interval, fraction_determinant,
)


def _natural(n: int, minimum: int = 0) -> int:
    if type(n) is not int or n < minimum:
        raise ValueError(f"expected integer >= {minimum}")
    return n


def geometric_green_moment(order: int) -> Q:
    """Exact M_j=sum_{k>=1}k^j/16^k; Eulerian rational recurrence."""
    _natural(order)
    # F_j(z) = A_j(z)/(1-z)^(j+1), A_0(z)=z;
    # A_(j+1)(z) = z*((1-z)*A'_j(z)+(j+1)*A_j(z)).
    coeffs = [0, 1]
    for j in range(order):
        nxt = [0]*(len(coeffs)+1)
        for i in range(len(coeffs)):
            following = coeffs[i+1] if i+1 < len(coeffs) else 0
            nxt[i+1] = (i+1)*following + (j+1-i)*coeffs[i]
        coeffs = nxt
    z = Q(1,16)
    numerator = Q(0)
    for c in reversed(coeffs):
        numerator = numerator*z+c
    return numerator/(1-z)**(order+1)


def tail_coefficient(order: int) -> Q:
    """c_q in t_n ~ sum_{q>=0}c_q/n^(q+1); actual c_0=0.

    c_q = sum_{j<=q}(-1)^(q-j) binom(q,j) m_j M_(q-j).
    """
    _natural(order)
    return sum(((-1)**(order-j)*comb(order,j)*pole_moment(j)
                *geometric_green_moment(order-j) for j in range(order+1)), Q())


def tail_asymptotic_polynomial(n: int, degree: int) -> Q:
    """Exact inverse-power truncation through n^(-degree-1), n >= 1."""
    _natural(n,1); _natural(degree)
    return sum((tail_coefficient(q)/n**(q+1) for q in range(degree+1)), Q())


def absolute_remainder_bound(n: int, degree: int) -> Q:
    """Rigorous |t_n - polynomial| <= K_(degree+1)/n^(degree+2).

    K_p = sum_i |rho_i| sum_{k>=1}16^-k (k-a_i)^p, finite rational.
    Formula uses exact geometric division with k-a_i >= 0.
    """
    _natural(n,1); _natural(degree)
    p = degree+1
    def centered_green_moment(a: Q) -> Q:
        return sum(((-1)**j*comb(p,j)*a**j*geometric_green_moment(p-j)
                    for j in range(p+1)), Q())
    k = sum((abs(rho)*centered_green_moment(a) for a,rho in POLE_DATA), Q())
    assert k > 0
    return k/n**(p+1)


def recover_pole_moments(coefficients) -> tuple[Q,...]:
    """Invert the unit-triangular geometric transport; M0=1/15 nonzero."""
    recovered = []
    m0 = geometric_green_moment(0)
    for q, c in enumerate(coefficients):
        c = Q(c)
        lower = sum(((-1)**(q-j)*comb(q,j)*recovered[j]
                     *geometric_green_moment(q-j) for j in range(q)), Q())
        recovered.append((c-lower)/m0)
    return tuple(recovered)


def _fraction_solve(matrix, values) -> tuple[Q,...]:
    """Exact linear solver, including singular-source rejection."""
    n = len(values)
    if len(matrix) != n or any(len(row) != n for row in matrix):
        raise ValueError("square linear system required")
    a = [[Q(x) for x in row]+[Q(y)] for row,y in zip(matrix, values)]
    for j in range(n):
        pivot = next((i for i in range(j,n) if a[i][j]), None)
        if pivot is None:
            raise ArithmeticError("singular source reconstruction")
        a[j],a[pivot] = a[pivot],a[j]
        scale = a[j][j]
        a[j] = [x/scale for x in a[j]]
        for i in range(n):
            if i != j:
                scale = a[i][j]
                a[i] = [v-scale*w for v,w in zip(a[i],a[j])]
    return tuple(row[-1] for row in a)


def known_pole_weights_from_coefficients(coefficients) -> tuple[Q,...]:
    """First four coefficients c0..c3 determine weights at four KNOWN poles."""
    coefficients = tuple(coefficients)
    if len(coefficients) < 4:
        raise ValueError("four tail coefficients required for fixed-pole family")
    poles = tuple(a for a,_ in POLE_DATA)
    moments = recover_pole_moments(coefficients[:4])
    return _fraction_solve([[a**j for a in poles] for j in range(4)], moments)


def signed_pole_hankel_determinant() -> Q:
    """Exact rank-four witness; signed determinant need not be positive."""
    return fraction_determinant([[pole_moment(i+j) for j in range(4)]
                                 for i in range(4)])


def prony_polynomial_from_coefficients(coefficients) -> tuple[Q,...]:
    """Eight c0..c7 recover UNKNOWN four distinct poles (via Prony).

    Returns ascending coefficients of monic P(x)=prod_i(x-a_i).
    Requires four-atom signed source with invertible moment Hankel.
    """
    coefficients = tuple(coefficients)
    if len(coefficients) < 8:
        raise ValueError("eight coefficients needed for unknown four poles")
    m = recover_pole_moments(coefficients[:8])
    p = _fraction_solve([[m[i+j] for j in range(4)] for i in range(4)],
                        [-m[i+4] for i in range(4)])
    return p+(Q(1),)


def holonomic_ratio(n: int) -> Q:
    """R_n=r(n+2)/r(n+1); exact coefficient of order-two tail law."""
    _natural(n)
    return forcing(n+2)/forcing(n+1)


def holonomic_residual_interval(n: int, terms: int = 12) -> tuple[Q,Q]:
    """Exact enclosure of t_(n+2)-(16+R_n)t_(n+1)+16R_n*t_n."""
    _natural(n); _natural(terms,1)
    r = holonomic_ratio(n)
    a,b,c = (tail_interval(n+j,terms) for j in range(3))
    return (c[0]-(16+r)*b[1]+16*r*a[0],
            c[1]-(16+r)*b[0]+16*r*a[1])


def compact_bump_moment(n: int) -> Q:
    """Moments of 8*(1/2-u)_+ du on [0,1]; unit mass, O(2^-n/n^2)."""
    _natural(n)
    return Q(2, 2**n*(n+1)*(n+2))


def compact_bump_forcing(n: int) -> Q:
    """Positive perturbation 16*q_(n-1)-q_n to the source forcing."""
    _natural(n,1)
    return 16*compact_bump_moment(n-1)-compact_bump_moment(n)


def zero_contact_moment(n: int) -> Q:
    """Moments of delta_0; all moments n>=1 vanish, n=0 detects it."""
    _natural(n)
    return Q(int(n == 0))


def rational_phase_shadows(count: int, degree: int | None = None) -> tuple[Q,...]:
    """Exact rational SUCC forward states, optionally corrected by c_q tails.

    Entries approximate fractional parts of 16^j*pi for j=0..count-1.
    degree=None means the uncorrected rational forced state y_(j+1).
    This is not a proof of digit equidistribution.
    """
    from observational_succ.bbp_source_memory import forced_step
    _natural(count)
    if degree is not None:
        _natural(degree)
    state = Q()
    prefix = []
    for j in range(count):
        state = forced_step(state,j+1)
        correction = (Q() if degree is None
                      else tail_asymptotic_polynomial(j+1,degree))
        prefix.append((state+correction)%1)
    return tuple(prefix)


def signed_shadow_error_budget(frequency: int, count: int,
                               degree: int | None = None) -> Q:
    """Rational strict upper for |sum e(k*16^j*pi)-sum e(k*shadow_j)|.

    Uses |e(a)-e(b)| <= 2*pi*|a-b| < 8*|a-b|.
    degree=None uses parent sharp beta tail upper; other degrees use
    all-order K bounds. Valid for every finite count, no float pi needed.
    """
    from observational_succ.bbp_source_memory import source_tail_beta_bracket
    if type(frequency) is not int:
        raise ValueError("integer Fourier frequency required")
    _natural(count)
    if degree is not None:
        _natural(degree)
    errors = (source_tail_beta_bracket(j)[1] if degree is None
              else absolute_remainder_bound(j,degree) for j in range(1,count+1))
    return 8*abs(frequency)*sum(errors,Q())


def uniform_uncorrected_shadow_budget(frequency: int) -> Q:
    """Any prefix: strict Fourier-sum difference < abs(k)/4.

    Since T_n < 1/(64n^2), sum_{n>=1}n^-2 <=2 and 2*pi<8.
    """
    if type(frequency) is not int:
        raise ValueError("integer Fourier frequency required")
    return Q(abs(frequency),4)


def signed_lag_shadow_budget(h: int, lag: int, horizon: int,
                             degree: int | None = None) -> Q:
    """Uniform finite-source error for cyclotomic lag k=h*(16^lag-1)."""
    if type(h) is not int:
        raise ValueError("integer Fourier frequency required")
    _natural(lag,1); _natural(horizon)
    return signed_shadow_error_budget(h*(16**lag-1),max(0,horizon-lag),degree)
