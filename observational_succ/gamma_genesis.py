"""Pointed Gamma-wavefront research: exact rational source and observer controls.

The original Oily/BBP forcing is immutable. This module does not assert that
an independently constructed Gamma/Poisson observation channel is physically
implemented by the BBP recurrence. No RH/normality estimate follows from it.

Proofs: research/2026-11-14/gamma_genesis/THEOREMS.md.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

Q = Fraction


def rational(x):
    if type(x) not in (int, Q):
        raise TypeError("Exact rational input only; no untracked floating error")
    return Q(x)


def forcing(n: int) -> Q:
    """Immutable original four-pole forcing r(n), for n>=1."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    return Q(4, 8*n-7) - Q(2, 8*n-4) - Q(1, 8*n-3) - Q(1, 8*n-2)


def forcing_factored(n: int) -> Q:
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    return Q(120*n*n-89*n+16, (2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))


def beta_integer(m: int, k: int) -> Q:
    """Exact integral ∫_0^1 x^m (1-x)^k dx for m,k>=0 integers."""
    if type(m) is not int or type(k) is not int or m < 0 or k < 0:
        raise ValueError("Nonnegative integer beta exponents only")
    d = 1
    for j in range(1, k+2):
        d *= m+j
    return Q(factorial(k), d)


def oily_positive_moment_bounds(m: int) -> tuple[Q, Q]:
    """Source-specific rational enclosure for ∫ x^m R(x) dx.

    R(x)=(1-x)/[(2-x^2)(x^2-2x+2)] and pointwise, δ=1-x:
    δ(1-2δ) <= R(x) <= δ(1-2δ+4δ²).
    Bounds valid at every integer m>=0; they become positive at m>=2.
    """
    if type(m) is not int or m < 0:
        raise ValueError("Nonnegative integer moment depth only")
    lower = beta_integer(m, 1)-2*beta_integer(m, 2)
    upper = lower+4*beta_integer(m, 3)
    return lower, upper


def refined_oily_moment_bounds(m: int) -> tuple[Q, Q]:
    """Source-specific refined envelope with first THREE asymptotic terms.

    δ L(1-δ)=δ(1-2δ+4δ²)+rem, with -20δ⁴ <= rem <= 0.
    Thus I_m lies in A+4 B3 -20 B4 <= I_m <= A+4 B3.
    """
    if type(m) is not int or m < 0:
        raise ValueError("Nonnegative integer moment depth only")
    A = beta_integer(m, 1)-2*beta_integer(m, 2)+4*beta_integer(m, 3)
    return A-20*beta_integer(m, 4), A


def oily_gamma_total_variation_bound(m: int) -> Q:
    """Certified TV bound for a NEW declared posterior/source observer.

    Let X_m have density x^m R(x)/I_m with authentic positive Oily R.
    For m>=1 put Y_m=m(1-X_m). Then
      TV(Law(Y_m), Gamma(2,1)) <= 1-m^2 I_m <= this rational.
    This is conditional on a newly declared likelihood x^m; it is NOT
    a probability law of original BBP digits or an observed physical sensor.
    A separately declared Poisson(Y_m) readout inherits the SAME bound to
    NB(shape=2,p=1/2) by TV data processing.
    """
    if type(m) is not int or m < 1:
        raise ValueError("Positive posterior exponent m required")
    lower,_=oily_positive_moment_bounds(m)
    return 1-m*m*lower


def green_tail_bounds(n: int, depth: int) -> tuple[Q, Q]:
    """Certified rational enclosure of actual BBP future Green tail.

    T_n = Σ_{j>=1} 16^-j r(n+j) = ∫_0^1 x^(8n) R(x) dx.
    Uses positive monotone source forcing, not surrogate probability.
    """
    if type(n) is not int or type(depth) is not int or n < 0 or depth < 1:
        raise ValueError("Nonnegative n and positive summation depth")
    partial = sum((forcing(n+j)/16**j for j in range(1,depth+1)),Q(0))
    remainder_bound = forcing(n+depth+1) / (15*16**depth)
    return partial, partial + remainder_bound


def gamma_delay_pmf(shape: int, j: int) -> Q:
    """NB(shape, p=1/2) readout of Gamma shape, EXACT for integer shape.

    shape=0 is the origin impulse δ0, the weak-continuous semigroup unit.
    shape>0: C(j+shape-1,j)/2^(j+shape).
    """
    if type(shape) is not int or type(j) is not int or shape < 0 or j < 0:
        raise ValueError("Nonnegative integer depth and delay")
    if shape == 0:
        return Q(int(j == 0))
    return Q(comb(j+shape-1,j), 2**(j+shape))


def gamma_poisson_mixture_pmf(shape: int, j: int) -> Q:
    """Exact integral of Pois(j|t) against Gamma(shape,1), integer shapes.

    Equivalent algebraic route using factorial moments, not PMF recursion.
    """
    if type(shape) is not int or type(j) is not int or shape < 1 or j < 0:
        raise ValueError("Positive integer shape, nonnegative readout")
    return Q(factorial(shape+j-1),factorial(shape-1)*factorial(j)*2**(shape+j))


def convolution_coefficient(a: int, b: int, j: int) -> Q:
    if any(type(k) is not int or k < 0 for k in (a,b,j)):
        raise ValueError("Nonnegative integer depths")
    return sum((gamma_delay_pmf(a,k)*gamma_delay_pmf(b,j-k)
                for k in range(j+1)),Q(0))


def laplace_integer_shape(shape: int, q: Q) -> Q:
    """Laplace transform E[e^-q T] for Gamma(shape, rate=1)."""
    if type(shape) is not int or shape < 0 or rational(q) < 0:
        raise ValueError("Nonnegative shape and Laplace variable")
    return (1+rational(q))**(-shape)


def gamma_partition_integer_shape(shape: int, rate: Q) -> Q:
    """Z(shape,rate)=Γ(shape)/rate^shape, not probability without normalization."""
    if type(shape) is not int or shape < 1 or rational(rate) <= 0:
        raise ValueError("Positive integer shape and rate")
    return Q(factorial(shape-1)) / rational(rate)**shape


def gauge_compensated_partition(shape: int, rate: Q, clock_rescale: Q) -> tuple[Q,Q]:
    """Time t'=c*t and conjugate inverse-rate λ'=λ/c leave λ^s Z invariant."""
    rate, clock_rescale = rational(rate), rational(clock_rescale)
    if clock_rescale <= 0 or rate <= 0:
        raise ValueError("Positive clock and source rate only")
    old = rate**shape * gamma_partition_integer_shape(shape,rate)
    new_rate = rate/clock_rescale
    new = new_rate**shape * gamma_partition_integer_shape(shape,new_rate)
    return old,new


def causal_gamma_filter(data: tuple[Q,...], shape: int, delay: int=0) -> tuple[Q,...]:
    """Finite readout of a causal normalized negative-binomial filter.

    f_k=0 for k<0; y_n = Σ_j w_shape(j) f_(n-delay-j).
    Source signed values are preserved, not replaced by averaged source seeds.
    """
    if type(shape) is not int or type(delay) is not int or shape < 0 or delay < 0:
        raise ValueError("Nonnegative integer depth / compulsory delay")
    data=tuple(rational(x) for x in data)
    out=[]
    for n in range(len(data)):
        out.append(sum((gamma_delay_pmf(shape,j)*data[n-delay-j]
                        for j in range(n-delay+1)),Q(0)) if n>=delay else Q(0))
    return tuple(out)


def signed_mean_gap(data: tuple[Q,...], shape: int, delay: int=0) -> tuple[Q,Q]:
    """Actual finite signed sum gap and rigorous universal edge bound.

    |Σ_(n<N) y_n - Σ_(n<N) f_n| <= (shape+delay) sup|f_n|.
    No cancellation claim is made about either sum.
    """
    data=tuple(rational(x) for x in data)
    transformed=causal_gamma_filter(data,shape,delay)
    gap=abs(sum(transformed,Q(0))-sum(data,Q(0)))
    bound=(shape+delay)*max((abs(v) for v in data),default=Q(0))
    return gap,bound
