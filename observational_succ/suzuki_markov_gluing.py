"""Exact certificates for source-preserving Suzuki/Carleman/prime gluing.

Infinite-dimensional claims are proved in SUZUKI_MARKOV_GLUING_ROUND.md.
Finite graph checks are algebra controls, not continuum spectral certificates.
Only the prime-2 absorption sub-form is certified; RH is NOT proved.
"""
from __future__ import annotations

from fractions import Fraction as Q
from math import isqrt


class GluingError(ValueError):
    """Malformed, inexact, or out-of-contract source data."""


def rational(x: int | Q) -> Q:
    if type(x) not in (int, Q):
        raise GluingError("an exact integer or Fraction is required")
    return Q(x)


def integer(n: int, low: int = 0, high: int = 512) -> int:
    if type(n) is not int or not low <= n <= high:
        raise GluingError("integer outside the finite implementation budget")
    return n


def log_interval(x: int | Q, terms: int = 32) -> tuple[Q, Q]:
    x = rational(x)
    integer(terms, 1, 128)
    if not 1 <= x <= 8:
        raise GluingError("log interval requires 1 <= x <= 8")
    z = (x - 1) / (x + 1)
    lo = 2 * sum((z**(2*j+1) / (2*j+1) for j in range(terms)), Q())
    tail = 2*z**(2*terms+1) / ((2*terms+1)*(1-z*z))
    return lo, lo + tail


def pi_interval(terms: int = 12) -> tuple[Q, Q]:
    integer(terms, 1, 128)
    def atan(x: Q) -> tuple[Q, Q]:
        s = sum(((-1)**j*x**(2*j+1)/(2*j+1) for j in range(terms)), Q())
        nxt = (-1)**terms*x**(2*terms+1)/(2*terms+1)
        return min(s, s+nxt), max(s, s+nxt)
    a, b = atan(Q(1, 5))
    c, d = atan(Q(1, 239))
    return 16*a-4*d, 16*b-4*c


def sqrt_interval(n: int, digits: int = 12) -> tuple[Q, Q]:
    integer(n, 1, 1_000_000)
    integer(digits, 1, 32)
    scale = 10**digits
    k = isqrt(n*scale*scale)
    lo = Q(k, scale)
    return lo, lo if k*k == n*scale*scale else Q(k+1, scale)


def prime_power(n: int) -> tuple[int, int] | None:
    integer(n, 2, 1_000_000)
    p = next((d for d in range(2, isqrt(n)+1) if n % d == 0), n)
    rest, exponent = n, 0
    while rest % p == 0:
        rest //= p
        exponent += 1
    return (p, exponent) if rest == 1 else None


def gamma_density(z: int | Q) -> Q:
    """Actual Gamma jump kernel at z=exp(-abs(t)/2), t != 0."""
    z = rational(z)
    if not 0 < z < 1:
        raise GluingError("strictly positive finite time required")
    return z / (1-z**4)


def markov_density(z: int | Q, layer: int) -> Q:
    """nu_k(t)=exp(-k abs(t))/(2 cosh(t/2)), not a new source."""
    z = rational(z)
    integer(layer)
    if not 0 < z < 1:
        raise GluingError("strictly positive finite time required")
    return z**(2*layer+1) / (1+z*z)


def gamma_split(z: int | Q, count: int) -> tuple[Q, Q, Q]:
    z = rational(z)
    integer(count, 1)
    full = gamma_density(z)
    prefix = sum((markov_density(z, j) for j in range(count)), Q())
    tail = z**(2*count)*full
    if prefix + tail != full:
        raise ArithmeticError("Gamma source split failed")
    return prefix, tail, full


def rate_affine_pi(layer: int) -> tuple[Q, int]:
    """Exact r_k=A_k+B_k*pi; r_0=pi, r_k+r_(k+1)=4/(2k+1)."""
    integer(layer)
    a, b = Q(), 1
    for k in range(layer):
        a, b = Q(4, 2*k+1)-a, -b
    return a, b


def rate_interval(layer: int) -> tuple[Q, Q]:
    a, b = rate_affine_pi(layer)
    lo, hi = pi_interval()
    return (a+lo, a+hi) if b == 1 else (a-hi, a-lo)


def derivative_tail_bound(count: int) -> Q:
    """E_tail(v) <= bound * ||v'||^2, NOT bound * ||v||^2."""
    integer(count, 1)
    a = Q(2*count+1, 2)
    return 2/a**3 + 1/(2*a*a)


def first_prime_certificate(coefficient_upper: int | Q | None = None) -> dict:
    """Uniform whole-space sub-form inequality for 0<a<=log(3)/2.

    E_0(v)+Q_2(v) >= (4/5) E_0(v) >= 2 ||v||^2.
    The scalar and pole pieces of the full Weil form are NOT discarded.
    An override is a declared hostile coefficient, not an authentic source.
    """
    log2 = log_interval(2)
    log3 = log_interval(3)
    sqrt2 = sqrt_interval(2)
    pi_lo, _ = pi_interval()
    a_hi = log3[1]/2
    c_hi = log2[1]/sqrt2[0]
    if coefficient_upper is not None:
        c_hi = rational(coefficient_upper)
        if c_hi < 0:
            raise GluingError("nonnegative coefficient required")
    gap_lo = pi_lo-a_hi
    absorption = c_hi/gap_lo
    passes = absorption <= Q(1, 5) and gap_lo-c_hi >= 2
    return {
        "source": "actual_prime_2" if coefficient_upper is None else "mutated_coefficient",
        "a_upper": str(a_hi), "prime_coefficient_upper": str(c_hi),
        "markov_gap_lower": str(gap_lo), "absorption_ratio_upper": str(absorption),
        "one_fifth_certificate": passes,
        "coercive_subform_lower": "2" if passes else None,
        "full_Weil_positive": False, "RH_proved": False,
        "nontrivial_zero_inputs": False,
    }


def shift_fibers(length: int | Q, step: int | Q) -> tuple[tuple[int, Q], ...]:
    """Lengths of finite source orbits and their Lebesgue fiber widths.

    Decompose (0,L) by x=r+j*step, 0<=r<step. Each orbit is a path graph.
    At L/step an integer, the longer chain has ZERO measure and is omitted.
    """
    length, step = rational(length), rational(step)
    if length <= 0 or step <= 0:
        raise GluingError("positive interval and step required")
    ratio = length/step
    n = ratio.numerator // ratio.denominator
    integer(n, 0, 10_000)
    rem = length-n*step
    out = []
    if rem:
        out.append((n+1, rem))
    if n and step > rem:
        out.append((n, step-rem))
    if sum((vertices*width for vertices, width in out), Q()) != length:
        raise ArithmeticError("prime orbit measure lost")
    return tuple(out)


def compressed_shift(v: tuple[int | Q, ...], steps: int) -> tuple[Q, ...]:
    integer(steps, 0, 10_000)
    a = tuple(rational(x) for x in v)
    return tuple(a[k+steps] if k+steps < len(a) else Q() for k in range(len(a)))


def carleman_pullback(x: int | Q, y: int | Q) -> tuple[Q, Q]:
    """r=x^2, s=y^2. Exact log-half-density pullback of UNNORMALIZED nu_0."""
    x, y = rational(x), rational(y)
    if x <= 0 or y <= 0:
        raise GluingError("positive radial source coordinates required")
    nu = x*y/(x*x+y*y)
    return nu/(x*y), 1/(x*x+y*y)


def laplace_dilation(b: int | Q, t: int | Q, p: int) -> tuple[Q, Q]:
    """On exp(-b*r): L D_p = p^-1 D_(1/p) L; D_p is UNnormalized."""
    b, t = rational(b), rational(t)
    integer(p, 2, 1_000_000)
    if b <= 0 or t <= 0:
        raise GluingError("positive Laplace parameters required")
    return 1/(p*b+t), Q(1, p)/(b+t/p)


def laplace_boundary(base: int, b: int, t: int) -> tuple[Q, Q, Q]:
    """For h=log(base), source exp(-b*r), exact additive-SUCC boundary receipt.

    L S_h f=e^(ht)[Lf-int_0^h e^(-tr)f(r)dr]. Third output omits the receipt.
    """
    integer(base, 2, 20)
    integer(b, 1, 32)
    integer(t, 1, 32)
    lf = Q(1, b+t)
    lost = (1-Q(1, base)**(b+t))/(b+t)
    return Q(1, base)**b*lf, base**t*(lf-lost), base**t*lf


def successor_bulk_defect(r: int | Q, s: int | Q, h: int | Q) -> tuple[Q, Q]:
    r, s, h = rational(r), rational(s), rational(h)
    if r <= 0 or h <= 0 or s < h:
        raise GluingError("bulk formula requires r>0 and s>=h>0")
    return 1/(r+s+h)-1/(r+s-h), -2*h/((r+s)**2-h*h)


def localization(v, weights, charts, edges=(), coefficient=Q(1)) -> dict:
    """Exact finite-graph IMS and source-shift control, not continuum quadrature.

    charts[i] is a real unit vector, weights is a symmetric nonnegative matrix;
    each edge is an oriented-once atomic source coupling (i,j).
    """
    v = tuple(rational(x) for x in v)
    n = len(v)
    if not 1 <= n <= 64 or len(weights) != n or len(charts) != n:
        raise GluingError("inconsistent finite carrier")
    w = tuple(tuple(rational(x) for x in row) for row in weights)
    ph = tuple(tuple(rational(x) for x in row) for row in charts)
    rank = len(ph[0])
    if not rank or any(len(row) != n for row in w) or any(len(row) != rank for row in ph):
        raise GluingError("ragged geometry")
    if any(sum((x*x for x in row), Q()) != 1 for row in ph):
        raise GluingError("partition must have sum of squares exactly one")
    if any(w[i][j] < 0 or w[i][j] != w[j][i] for i in range(n) for j in range(n)):
        raise GluingError("invalid symmetric jump weights")
    coefficient = rational(coefficient)
    if coefficient < 0:
        raise GluingError("negative atomic coefficient")
    for i, j in edges:
        integer(i, 0, n-1)
        integer(j, 0, n-1)
        if i == j:
            raise GluingError("atomic self-loop not allowed here")
    def energy(u):
        return sum((w[i][j]*(u[i]-u[j])**2 for i in range(n) for j in range(n)), Q())/2
    def atomic(u):
        return -2*coefficient*sum((u[i]*u[j] for i, j in edges), Q())
    pieces = [tuple(ph[i][k]*v[i] for i in range(n)) for k in range(rank)]
    diff2 = lambda i, j: sum(((ph[i][k]-ph[j][k])**2 for k in range(rank)), Q())
    jump_debt = sum((w[i][j]*v[i]*v[j]*diff2(i, j) for i in range(n) for j in range(n)), Q())/2
    prime_debt = coefficient*sum((v[i]*v[j]*diff2(i, j) for i, j in edges), Q())
    if sum((energy(u) for u in pieces), Q())-energy(v) != jump_debt:
        raise ArithmeticError("jump IMS identity failed")
    if sum((atomic(u) for u in pieces), Q())-atomic(v) != prime_debt:
        raise ArithmeticError("atomic IMS identity failed")
    return {"jump_debt": str(jump_debt), "prime_debt": str(prime_debt),
            "prime_compatible": all(ph[i] == ph[j] for i, j in edges),
            "finite_control_not_continuum": True, "RH_proved": False}


def receipt() -> dict:
    gap = first_prime_certificate()
    pairs = [gamma_split(Q(1, 2), k) for k in (1, 2, 4, 8)]
    return {
        "parent": "17f1c8da3948ddce719cde301423cb3e31bf6716",
        "first_prime_absorption": gap,
        "hostile_large_coefficient_rejected": not first_prime_certificate(4)["one_fifth_certificate"],
        "Gamma_exact_splits": [[str(x) for x in row] for row in pairs],
        "positive_H1_tail_coefficients": {str(k): str(derivative_tail_bound(k)) for k in (2, 8, 32)},
        "Laplace_boundary_correct_and_omitted": [str(x) for x in laplace_boundary(2, 2, 3)],
        "fake_six_prime_power": prime_power(6),
        "source_4_is_true_prime_power": list(prime_power(4)),
        "full_Weil_positive": False, "RH_proved": False,
        "proof_assistant_checked": False, "physical_carrier_claimed": False,
    }
