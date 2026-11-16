"""Exact arithmetic for the Gamma phase-disintegration research dossier.

No pi target, random orbit model, or normality premise is supplied. Rational
functions and polynomial identities are exact. Special-function diagnostics
live in the separately labelled audit scripts.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb, factorial

GQ = tuple[F, F]  # Exact Gaussian rational, (real, imaginary).
POLE_GAPS = ((3, 2), (4, 1), (5, 1))


def natural(value, name="index", minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def rational(value, name="value"):
    if type(value) not in (int, F):
        raise ValueError(f"{name} must be an exact rational")
    return F(value)


def gadd(x: GQ, y: GQ) -> GQ:
    return x[0] + y[0], x[1] + y[1]


def gmul(x: GQ, y: GQ) -> GQ:
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def gscale(x: GQ, scalar) -> GQ:
    scalar = rational(scalar)
    return scalar*x[0], scalar*x[1]


def pochhammer(real, imaginary, degree: int) -> GQ:
    """(real+i*imaginary)_degree with exact rational components."""
    real, imaginary = rational(real), rational(imaginary)
    natural(degree, "degree")
    value = F(1), F(0)
    for j in range(degree):
        value = gmul(value, (real+j, imaginary))
    return value


def forcing(n: int) -> F:
    natural(n, "source time", 1)
    return (F(4, 8*n-7)-F(2, 8*n-4)
            -F(1, 8*n-3)-F(1, 8*n-2))


def rate_mass(a) -> F:
    """Integral of the positive forcing rate measure; a>0."""
    a = rational(a, "rate")
    if a <= 0:
        raise ValueError("rate must be positive")
    return sum((F(v*d)/(a*(a+d)) for d, v in POLE_GAPS), F())


def forcing_disk(a) -> tuple[F, F, F]:
    """Center, radius, and strictly positive distance from the imaginary axis."""
    a = rational(a, "rate")
    if a <= 0:
        raise ValueError("rate must be positive")
    center = 4/a
    radius = sum((F(v)/(a+d) for d, v in POLE_GAPS), F())
    return center, radius, center-radius


def laguerre_poly(m: int) -> tuple[F, ...]:
    """Ascending coefficients of the classical L_m^(1)(x)."""
    natural(m, "degree")
    return tuple(F((-1)**j*comb(m+1, m-j), factorial(j))
                 for j in range(m+1))


def laguerre_inner(m: int, n: int) -> F:
    """Integral L_m^1 L_n^1 x exp(-x) dx by exact factorial moments."""
    left, right = laguerre_poly(m), laguerre_poly(n)
    return sum((a*b*factorial(j+k+1)
                for j, a in enumerate(left)
                for k, b in enumerate(right)), F())


def coefficient_ratio(m: int, omega) -> GQ:
    """Integral x^(i omega) L_m^1 x e^-x dx divided by Gamma(2+i omega).

    Divide this value by sqrt(m+1) to obtain the orthonormal coefficient
    divided by Gamma(2+i omega). The square root is kept symbolic.
    """
    natural(m, "degree")
    omega = rational(omega, "frequency")
    return gscale(pochhammer(0, -omega, m), F(1, factorial(m)))


def polynomial_coefficient_ratio(m: int, omega) -> GQ:
    """Independent finite polynomial integration, using (2+i omega)_j."""
    omega = rational(omega, "frequency")
    value = F(), F()
    for j, coeff in enumerate(laguerre_poly(m)):
        value = gadd(value, gscale(pochhammer(2, omega, j), coeff))
    return value


def relative_mode_weights(omega, max_degree: int) -> tuple[F, ...]:
    """p_m / |Gamma(2+i omega)|^2, for m=0..max_degree, exactly.

    These are relative weights, not normalized probabilities on a finite
    truncation. Do not renormalize them to conceal discarded energy.
    """
    omega = rational(omega, "frequency")
    natural(max_degree, "degree")
    z = omega*omega
    values = [F(1)]
    for m in range(max_degree):
        values.append(values[-1]*(m*m+z)/((m+1)*(m+2)))
    return tuple(values)


def mode_tail_bounds(omega, max_degree: int) -> tuple[F, F]:
    """Certified bounds for sum_{m>M}|c_m|^2 under Gamma(2), M>=1.

    The theorem, not a finite scan, supplies normalization and the tail.
    Bounds require no numeric Gamma, exponential, or pi evaluation.
    """
    omega = rational(omega, "frequency")
    m = natural(max_degree, "cutoff", 1)
    z = omega*omega
    c = z*(1+z)
    low = c*max(F(), 1-z/m)/(2*(m+1)*(m+2))
    high = min(F(1), z/(m+1), c/(2*m*(m+1)))
    return low, high


def required_mode_cutoff(omega, squared_error) -> int:
    """A sufficient retained degree for the declared mean-square error.

    This is an upper certificate, not an optimal algorithmic complexity claim.
    """
    omega = rational(omega, "frequency")
    error = rational(squared_error, "squared error")
    if not 0 < error < 1:
        raise ValueError("squared error must be in (0,1)")
    if omega == 0:
        return 0
    lo, hi = 0, 1
    while mode_tail_bounds(omega, hi)[1] > error:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mode_tail_bounds(omega, mid)[1] <= error:
            hi = mid
        else:
            lo = mid
    return hi


def rate_moment(order: int) -> F:
    """E B^order for B=8K+V, P(K=k)=15/16^(k+1).

    V has density sum v*1_[1,1+d]/15, independent of K. The geometric
    moments follow a finite exact recurrence, without an infinite truncation.
    """
    natural(order, "moment order")
    q = F(1, 16)
    geom = [F(1)]
    for j in range(1, order+1):
        geom.append(q/(1-q)*sum((comb(j,k)*geom[k]
                                for k in range(j)), F()))
    total = F()
    for j in range(order+1):
        power = order-j
        v_moment = sum((F(v*((1+d)**(power+1)-1),
                          15*(power+1)) for d,v in POLE_GAPS), F())
        total += comb(order,j)*8**j*geom[j]*v_moment
    return total


def tail_rate_interval(n: int, depth: int) -> tuple[F, F]:
    """Original Green moment via positive rate intervals, with strict tail bound."""
    natural(n, "source time")
    natural(depth, "depth")
    a = 8*n
    low = F()
    for j in range(1, depth+1):
        b = 8*j-7
        low += sum((F(v,16**j)*(F(1,a+b)-F(1,a+b+d))
                    for d,v in POLE_GAPS), F())
    remainder = F(1,16**depth*(a+8*depth+1)**2)
    return low, low+remainder


def resonance_error_bound(n: int, harmonic: int, detuning_radius) -> F:
    """Rational upper bound on |a Psi_a(a c+d)-L(c,d)|, |d|<=D.

    c=2*pi*k and a=8n. Uses 3<pi<22/7 only to bound the theorem's
    constants. It is conservative, valid at every n>=1, not a fitted error.
    """
    natural(n, "source time", 1)
    if type(harmonic) is not int or harmonic == 0:
        raise ValueError("harmonic must be a nonzero integer")
    d = rational(detuning_radius, "detuning radius")
    if d < 0:
        raise ValueError("detuning radius must be nonnegative")
    a, k = 8*n, abs(harmonic)
    m1, m2, m3, m4 = (rate_moment(j) for j in range(1,5))
    c_upper = F(44*k,7)
    leading_upper = m1+(d+1)/F(6*k)
    remainder = ((3+F(5,2)*d+d*d/2)*m2
                 +c_upper*(F(4,3)+d/2)*m3+c_upper*c_upper*m4/8)
    return (1+m1/a)**2*(remainder+2*m1*leading_upper)/a


def nonlinear_coin_sample_mean(p, angular_character):
    """Exact mean of a two-valued probe: (1-p)*1 + p*character(1).

    This exposes integer-circle aliasing without pretending the full
    characteristic function is constant. angular_character is a Gaussian
    rational representing the character at the integer 1.
    """
    p = rational(p, "coin probability")
    if not 0 <= p <= 1:
        raise ValueError("coin probability must be in [0,1]")
    u, v = (rational(x) for x in angular_character)
    return 1-p+p*u, p*v
